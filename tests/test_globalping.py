"""
tests/test_globalping.py

Globalping shadow mode (globalping_client.py, globalping_verify.py, globalping_report.py):
MTR parsing, pairing, classification through the unchanged Atlas classifier, the budget
guard, target selection and the pass criteria. Synthetic MTR JSON only, no network.
"""
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest import mock

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from test_forensic_hops import load_forensic  # noqa: E402

load_forensic()  # the real classifier, with ripe.atlas.cousteau stubbed when CI lacks it

import analyze_harvest  # noqa: E402
import globalping_client as gp  # noqa: E402
import globalping_report as report  # noqa: E402
import globalping_verify as gv  # noqa: E402

T, C, U, ALT, FAR, CF = 100, 200, 300, 400, 500, 13335   # target, customer, upstream, other provider, far probe AS
VALID, INVALID = "104.17.231.6", "103.21.244.8"
PREFIX_ASN = {"60.234.": T, "124.157.": C, "80.80.": U, "90.90.": ALT, "70.70.": FAR, "104.17.": CF, "198.41.": CF,
              "172.68.": CF, "103.21.": CF}


class FakeLookup:
    def asn(self, ip):
        return next((a for p, a in PREFIX_ASN.items() if ip.startswith(p)), None)


LOOKUP = FakeLookup()
IX = analyze_harvest.IxMap([{"prefix": "43.243.21.0/24"}], [{"asn": CF, "ipaddr4": "43.243.21.2", "ipaddr6": None}])


def hop(ip, asn=(), rcv=3, total=3):
    return {"resolvedAddress": ip, "resolvedHostname": None, "asn": list(asn),
            "stats": {"total": total, "rcv": rcv, "drop": total - rcv, "loss": 100 * (total - rcv) / total},
            "timings": [{"rtt": 1.0}] * rcv}


SILENT = hop(None, rcv=0)
GW = hop("192.168.0.1")
H_C, H_T, H_T2, H_U, H_O, H_FAR = (hop("124.157.1.1", [C]), hop("60.234.8.50", [T]), hop("60.234.8.51", [T]),
                                    hop("80.80.1.1", [U]), hop("90.90.1.1", [ALT]), hop("70.70.1.1", [FAR]))
H_EDGE, H_DST_V, H_DST_I = hop("198.41.236.29", [CF]), hop(VALID, [CF]), hop(INVALID, [CF])
VALID_VIA_T = [GW, H_C, H_T, H_T2, H_U, H_EDGE, H_DST_V]          # [C, T, U, CF]


def result(hops, status="finished"):
    return {"status": status, "rawOutput": "", "hops": hops} if status == "finished" else \
        {"status": status, "rawOutput": "probe failed"}


def probe(asn=C, city="Hamilton", tags=("eyeball-network",)):
    return {"continent": "OC", "region": "Australia and New Zealand", "country": "NZ", "state": None, "city": city,
            "asn": asn, "network": f"Net {asn}", "latitude": -37.8, "longitude": 175.3, "tags": list(tags),
            "resolvers": ["private"]}


def measurement(mid, target, entries, created="2026-11-28T00:57:57.717Z"):
    return {"id": mid, "type": "mtr", "status": "finished", "createdAt": created, "target": target,
            "probesCount": len(entries), "results": [{"probe": p, "result": r} for p, r in entries]}


def one_probe(valid_hops, invalid_hops, asn=T, probe_asn=C, valid_status="finished", invalid_status="finished"):
    """Result file for one probe with the given hop lists."""
    p = probe(probe_asn)
    v = measurement("V1", VALID, [(p, result(valid_hops, valid_status))])
    i = measurement("I1", INVALID, [(p, result(invalid_hops, invalid_status))])
    return gv.analyze_target(asn, v, i, LOOKUP, IX, frozenset({C}))


def verdict_of(valid_hops, invalid_hops, **kw):
    return one_probe(valid_hops, invalid_hops, **kw)["probe_details"][0]["verdict"]


class TestReach(unittest.TestCase):
    def test_destination_hop_full(self):
        self.assertEqual(gv.mtr_reach(result(VALID_VIA_T), VALID), 100.0)

    def test_destination_hop_partial_loss(self):
        r = result([GW, H_C, hop(VALID, [CF], rcv=2)])
        self.assertAlmostEqual(gv.mtr_reach(r, VALID), 66.67, places=1)

    def test_no_destination_hop_is_zero_whatever_the_length(self):
        self.assertEqual(gv.mtr_reach(result([GW, H_C, H_T] + [SILENT] * 25), INVALID), 0.0)

    def test_another_hop_answering_is_not_reach(self):
        self.assertEqual(gv.mtr_reach(result([GW, H_C, H_DST_V]), INVALID), 0.0)

    def test_unfinished_results_are_no_data(self):
        for status in ("failed", "offline", "in-progress"):
            self.assertIsNone(gv.mtr_reach(result([], status), VALID), status)
        self.assertIsNone(gv.mtr_reach(result([]), VALID))
        self.assertIsNone(gv.mtr_reach(None, VALID))

    def test_ipv6_target_compared_as_address(self):
        r = result([hop("2606:4700:7000:0:0:0:6715:f409", [CF])])
        self.assertEqual(gv.mtr_reach(r, "2606:4700:7000::6715:f409"), 100.0)


class TestPaths(unittest.TestCase):
    def test_private_hops_dropped_and_cloudflare_172_kept(self):
        hops = gv.mtr_hops(result([GW, hop("172.22.0.1"), hop("10.101.7.217"), hop("100.64.0.1"), H_T,
                                   hop("172.68.84.6", [CF]), SILENT]))
        ips = gv.public_hop_ips(hops)
        self.assertEqual(ips, ["60.234.8.50", "172.68.84.6"])
        self.assertEqual(analyze_harvest.as_runs(ips, LOOKUP, IX), [(T, 1), (CF, 1)])

    def test_ix_lan_hop_goes_to_the_address_holder(self):
        ips = gv.public_hop_ips(gv.mtr_hops(result([H_T, hop("43.243.21.2"), H_DST_V])))
        self.assertEqual(analyze_harvest.as_runs(ips, LOOKUP, IX), [(T, 1), (CF, 2)])

    def test_ix_lan_hop_without_a_holder_is_skipped(self):
        ips = gv.public_hop_ips(gv.mtr_hops(result([H_T, hop("43.243.21.99"), H_U])))
        self.assertEqual(analyze_harvest.as_runs(ips, LOOKUP, IX), [(T, 1), (U, 1)])

    def test_hop_asn_disagreements_recorded(self):
        hops = gv.mtr_hops(result([H_T, hop("80.80.1.1", [999]), hop("43.243.21.2", [64999]), hop("43.243.21.3"),
                                   hop("90.90.1.1", [ALT, 7])]))
        diffs = gv.hop_disagreements(hops, LOOKUP, IX)
        self.assertEqual(diffs, [{"ip": "80.80.1.1", "local": U, "globalping": [999], "ix_lan": False},
                                 {"ip": "43.243.21.2", "local": CF, "globalping": [64999], "ix_lan": True}])

    def test_disagreements_reach_the_result_file(self):
        d = one_probe([GW, H_C, H_T, hop("80.80.1.1", [999]), H_DST_V], [GW, H_C])["probe_details"][0]
        self.assertEqual([x["ip"] for x in d["hop_asn_disagreements"]], ["80.80.1.1"])


class TestPairing(unittest.TestCase):
    def test_pairs_by_index(self):
        a, b = probe(C, "Hamilton"), probe(T, "Clive")
        v = measurement("V", VALID, [(a, result(VALID_VIA_T)), (b, result(VALID_VIA_T))])
        i = measurement("I", INVALID, [(a, result([GW])), (b, result([GW]))])
        pairs = gv.pair_results(v, i)
        self.assertEqual([p["unpaired"] for p in pairs], [None, None])
        self.assertEqual([p["probe"]["city"] for p in pairs], ["Hamilton", "Clive"])

    def test_location_mismatch_is_unpaired(self):
        v = measurement("V", VALID, [(probe(C, "Hamilton"), result(VALID_VIA_T))])
        i = measurement("I", INVALID, [(probe(C, "Auckland"), result([GW, H_C]))])
        pair = gv.pair_results(v, i)[0]
        self.assertEqual(pair["unpaired"], "probe location mismatch")
        self.assertIsNone(pair["invalid"])

    def test_tags_do_not_break_a_pair(self):
        v = measurement("V", VALID, [(probe(C, tags=("eyeball-network",)), result(VALID_VIA_T))])
        i = measurement("I", INVALID, [(probe(C, tags=("eyeball-network", "u-someone")), result([GW, H_C]))])
        self.assertIsNone(gv.pair_results(v, i)[0]["unpaired"])

    def test_missing_invalid_measurement_or_index(self):
        v = measurement("V", VALID, [(probe(C), result(VALID_VIA_T)), (probe(T), result(VALID_VIA_T))])
        i = measurement("I", INVALID, [(probe(C), result([GW, H_C]))])
        self.assertEqual([p["unpaired"] for p in gv.pair_results(v, i)], [None, "no invalid result at this index"])
        self.assertTrue(all(p["unpaired"] for p in gv.pair_results(v, None)))

    def test_mismatched_pair_is_probe_down_not_secure(self):
        v = measurement("V", VALID, [(probe(C, "Hamilton"), result(VALID_VIA_T))])
        i = measurement("I", INVALID, [(probe(C, "Auckland"), result([GW, H_C]))])   # would read Target Filtered
        r = gv.analyze_target(T, v, i, LOOKUP, IX, frozenset({C}))
        self.assertEqual(r["probe_details"][0]["verdict"], "INCONCLUSIVE (Probe Down)")
        self.assertEqual(r["verdict"], "INCONCLUSIVE")


class TestNoData(unittest.TestCase):
    def test_invalid_side_not_finished_is_never_secure(self):
        for status in ("failed", "offline", "in-progress"):
            r = one_probe(VALID_VIA_T, [], invalid_status=status)
            d = r["probe_details"][0]
            self.assertEqual(d["verdict"], "INCONCLUSIVE (Probe Down)", status)
            self.assertEqual(d["no_data"], f"invalid result {status}")
            self.assertIsNone(d["score_i"])
            self.assertNotIn("SECURE", r["verdict"])
            self.assertNotIn("SECURE", r["verdict_origin_adjusted"])

    def test_valid_side_not_finished(self):
        for status in ("failed", "offline", "in-progress"):
            d = one_probe([], [GW, H_C], valid_status=status)["probe_details"][0]
            self.assertEqual(d["verdict"], "INCONCLUSIVE (Probe Down)", status)
            self.assertEqual(d["no_data"], f"valid result {status}")

    def test_finished_invalid_result_without_hops_is_no_data(self):
        d = one_probe(VALID_VIA_T, [])["probe_details"][0]
        self.assertEqual(d["verdict"], "INCONCLUSIVE (Probe Down)")
        self.assertEqual(d["no_data"], "invalid result finished")


class TestTaxonomy(unittest.TestCase):
    """Every outcome of verify_forensic_path_v2._classify_probe, reached from MTR fixtures."""

    def test_probe_down(self):
        self.assertEqual(verdict_of([GW, H_C, SILENT, SILENT], [GW, H_C]), "INCONCLUSIVE (Probe Down)")

    def test_off_path(self):
        self.assertEqual(verdict_of([GW, H_C, H_O, H_EDGE, H_DST_V], [GW, H_C]), "INCONCLUSIVE (Off-Path)")

    def test_partial(self):
        invalid = [GW, H_C, H_T, H_U, hop(INVALID, [CF], rcv=2)]
        self.assertEqual(verdict_of(VALID_VIA_T, invalid), "INCONCLUSIVE (Partial)")

    def test_vulnerable(self):
        self.assertEqual(verdict_of(VALID_VIA_T, [GW, H_C, H_T, H_T2, H_U, H_EDGE, H_DST_I]), "VULNERABLE")

    def test_bypass_route(self):
        self.assertEqual(verdict_of(VALID_VIA_T, [GW, H_C, H_O, H_EDGE, H_DST_I]), "VULNERABLE (Bypass Route)")

    def test_target_filtered(self):
        r = one_probe(VALID_VIA_T, [GW, H_C, SILENT, SILENT])
        d = r["probe_details"][0]
        self.assertEqual(d["verdict"], "SECURE (Target Filtered)")
        self.assertEqual((d["boundary_asn"], d["path_v"], d["path_i"]), (T, [C, T, U, CF], [C]))
        self.assertEqual(r["verdict"], "SECURE (Verified Active)")
        self.assertEqual(r["filter_boundary"], T)

    def test_upstream_filtered_counts_against_the_target(self):
        r = one_probe(VALID_VIA_T, [GW, H_C, H_T, SILENT])
        self.assertEqual(r["probe_details"][0]["verdict"], "SECURE (Upstream Filtered)")
        self.assertEqual(r["probe_details"][0]["boundary_asn"], U)
        self.assertEqual(r["verdict"], "VULNERABLE")
        self.assertEqual(r["verdict_origin_adjusted"], "VULNERABLE")

    def test_pre_target_filtered(self):
        valid = [GW, H_FAR, H_C, H_T, H_U, H_EDGE, H_DST_V]
        self.assertEqual(verdict_of(valid, [GW, H_FAR, SILENT], probe_asn=FAR), "SECURE (Pre-Target Filtered)")

    def test_divergent(self):
        self.assertEqual(verdict_of(VALID_VIA_T, [GW, H_C, H_O, SILENT]), "INCONCLUSIVE (Divergent)")

    def test_partial_deployment(self):
        a, b = probe(C, "Hamilton"), probe(T, "Clive")
        v = measurement("V", VALID, [(a, result(VALID_VIA_T)), (b, result(VALID_VIA_T))])
        i = measurement("I", INVALID, [(a, result([GW, H_C, SILENT])),
                                       (b, result([GW, H_C, H_T, H_T2, H_U, H_EDGE, H_DST_I]))])
        self.assertEqual(gv.analyze_target(T, v, i, LOOKUP, IX)["verdict"], "VULNERABLE (Partial Deployment)")

    def test_aggregate_matches_the_atlas_engine(self):
        self.assertEqual(gv.aggregate_verdict({"VULNERABLE (Bypass Route)": 2}), "INCONCLUSIVE (Divergent)")
        self.assertEqual(gv.aggregate_verdict({"INCONCLUSIVE (Off-Path)": 3}), "INCONCLUSIVE")
        self.assertEqual(gv.aggregate_verdict({"SECURE (Pre-Target Filtered)": 1}), "INCONCLUSIVE")


class TestOriginAndProvenance(unittest.TestCase):
    IN_TARGET_VALID = [GW, H_T, hop("43.243.21.2"), H_EDGE, H_DST_V]   # [T, CF] across an IX LAN

    def test_origin_named_as_drop_point_is_flagged_and_kept_apart(self):
        r = one_probe(self.IN_TARGET_VALID, [GW, H_T, SILENT, hop("10.101.7.217", rcv=2), SILENT], probe_asn=T)
        d = r["probe_details"][0]
        self.assertEqual(d["verdict"], "SECURE (Upstream Filtered)")      # the classifier, unchanged
        self.assertTrue(d["origin_boundary"])
        self.assertEqual(d["verdict_origin_adjusted"], "SECURE (Target Filtered)")
        self.assertEqual((r["verdict"], r["verdict_origin_adjusted"]), ("VULNERABLE", "SECURE (Verified Active)"))

    def test_adjustment_only_when_the_invalid_trace_ends_in_the_target(self):
        valid = [GW, H_C, H_T, H_U, H_EDGE, H_DST_V]                        # [C, T, U, CF]
        d = one_probe(valid, [GW, H_C, H_T, H_U, SILENT])["probe_details"][0]   # ends in U, next is CF
        self.assertTrue(d["origin_boundary"])
        self.assertEqual(d["verdict_origin_adjusted"], "SECURE (Upstream Filtered)")

    def test_no_non_rov_hops_anywhere(self):
        r = one_probe(VALID_VIA_T, [GW, H_C, H_T, H_T2, H_U, H_EDGE, H_DST_I])
        self.assertNotIn("non_rov_hops", json.dumps(r))

    def test_schema_and_provenance(self):
        r = one_probe(VALID_VIA_T, [GW, H_C, SILENT])
        for key in ("asn", "af", "measurement_ids", "probe_ids", "verdict", "notes", "n_vulnerable", "n_secure_local",
                    "n_bypass", "n_upstream_filtered", "verdict_counts", "filter_boundary", "successful_probes",
                    "total_probes", "probe_details", "timestamp"):
            self.assertIn(key, r)
        self.assertEqual(r["source"], "globalping")
        self.assertEqual(r["measurement_ids"], {"mtr_valid": "V1", "mtr_invalid": "I1"})
        self.assertEqual(r["targets"], {"valid": VALID, "invalid": INVALID})
        self.assertEqual(datetime.fromisoformat(r["timestamp"]),
                         datetime(2026, 11, 28, 0, 57, 57, 717000, tzinfo=timezone.utc))
        d = r["probe_details"][0]
        self.assertEqual((d["probe"]["city"], d["probe"]["asn"], d["tags"]), ("Hamilton", C, ["eyeball-network"]))
        self.assertEqual((d["network_type"], d["relation"], d["target_hops_v"]), ("eyeball", "customer", 2))
        self.assertTrue(d["probe_asn_on_path"])
        self.assertEqual(d["hops_v"][1], ["124.157.1.1", [C], 3, 3])

    def test_relation_and_network_type(self):
        p = probe(T, tags=("datacenter-network", "aws"))
        v, i = measurement("V", VALID, [(p, result(self.IN_TARGET_VALID))]), measurement("I", INVALID, [(p, result([GW]))])
        d = gv.analyze_target(T, v, i, LOOKUP, IX, frozenset({C}))["probe_details"][0]
        self.assertEqual((d["network_type"], d["relation"]), ("datacenter", "in-target"))
        self.assertEqual(one_probe(VALID_VIA_T, [GW], probe_asn=FAR)["probe_details"][0]["relation"], "other")

    def test_single_target_hop_between_other_ases_is_weak(self):
        d = one_probe([GW, H_C, H_T, H_U, H_EDGE, H_DST_V], [GW, H_C])["probe_details"][0]
        self.assertTrue(d["weak_on_path"])
        self.assertFalse(one_probe(VALID_VIA_T, [GW, H_C])["probe_details"][0]["weak_on_path"])

    def test_geoip_probe_as_not_on_path(self):
        d = one_probe([GW, H_O, H_T, H_T2, H_U, H_EDGE, H_DST_V], [GW, H_O])["probe_details"][0]   # probe says C
        self.assertFalse(d["probe_asn_on_path"])


def now_iso(days_ago=0.0):
    return (datetime.now(timezone.utc) - timedelta(days=days_ago)).isoformat()


class TestSelection(unittest.TestCase):
    BY_ASN = {1: [{"tags": ["datacenter-network"]}], 21: [{"tags": ["eyeball-network"]}],
              22: [{"tags": ["datacenter-network"]}], 23: [{"tags": ["eyeball-network"]}], 3: [{"tags": []}] * 5}
    DOWN = {1: [21, 22, 23, 24], 2: [21], 9: [23], 5: [99]}
    PROVIDERS = {21: {1, 2}, 22: {1}, 23: {1, 9}, 24: {1}}

    def test_locations_single_homed_then_inside_then_multi_homed(self):
        locs = gv.probe_locations(1, self.BY_ASN, self.DOWN, self.PROVIDERS, count=3)
        self.assertEqual(locs, [{"asn": 22, "limit": 1}, {"asn": 1, "limit": 1}, {"asn": 21, "limit": 1}])

    def test_locations_inside_only_takes_what_exists(self):
        self.assertEqual(gv.probe_locations(3, self.BY_ASN, {}, {}, count=3), [{"asn": 3, "limit": 3}])
        self.assertEqual(gv.probe_locations(5, self.BY_ASN, self.DOWN, self.PROVIDERS), [])

    def test_secure_first_then_newest(self):
        atlas = {1: {"verdict": "VULNERABLE", "timestamp": now_iso(1)},
                 2: {"verdict": "SECURE (Verified Active)", "timestamp": now_iso(5)},
                 3: {"verdict": "SECURE (Verified Active)", "timestamp": now_iso(2)},
                 9: {"verdict": "VULNERABLE (Partial Deployment)", "timestamp": now_iso(0.5)}}
        self.assertEqual(gv.select_targets(atlas, self.BY_ASN, self.DOWN, set(), 10), [3, 2, 9, 1])
        self.assertEqual(gv.select_targets(atlas, self.BY_ASN, self.DOWN, {3}, 2), [2, 9])

    def test_stale_inconclusive_and_unreachable_left_out(self):
        atlas = {1: {"verdict": "VULNERABLE", "timestamp": now_iso(8)},
                 2: {"verdict": "INCONCLUSIVE (Divergent)", "timestamp": now_iso(1)},
                 3: {"verdict": "INCONCLUSIVE", "timestamp": now_iso(1)},
                 5: {"verdict": "SECURE (Verified Active)", "timestamp": now_iso(1)},
                 CF: {"verdict": "SECURE (Verified Active)", "timestamp": now_iso(1)}}
        self.assertEqual(gv.select_targets(atlas, {**self.BY_ASN, CF: [{}]}, self.DOWN, set(), 10), [])


class FakeClient:
    """Stands in for globalping_client: every probe reaches the valid target and not the invalid one."""

    RateLimited = gp.RateLimited

    def __init__(self, remaining=250, header_remaining=None, fail_after=None):
        self.remaining, self.header_remaining, self.fail_after = remaining, header_remaining, fail_after
        self.posts, self.store, self.limit_calls = [], {}, 0

    def load_token(self):
        return None

    def fetch_probes(self, token=None):
        return [{"location": probe(a), "tags": ["eyeball-network"]} for a in (11, 12, 13) for _ in range(3)]

    def get_limits(self, token=None):
        self.limit_calls += 1
        return gp.Limits("ip", 250, self.remaining, 0)

    def create_measurement(self, target, locations, mtype="mtr", options=None, token=None):
        if self.fail_after is not None and len(self.posts) >= self.fail_after:
            raise gp.RateLimited("too many")
        mid = f"M{len(self.posts)}"
        if isinstance(locations, str):
            entries = [(r["probe"], result([GW, hop("60.234.8.50", [11]), SILENT])) for r in self.store[locations]["results"]]
        else:
            entries = [(probe(loc["asn"]), result([GW, hop("60.234.8.50", [11]), H_DST_V]))
                       for loc in locations for _ in range(loc["limit"])]
        self.store[mid] = measurement(mid, target, entries, created=now_iso().replace("+00:00", "Z"))
        self.posts.append((target, locations))
        self.remaining -= len(entries)
        header = self.header_remaining if self.header_remaining is not None else self.remaining
        return gp.Created(mid, len(entries), header)

    def wait_for_all(self, ids, timeout_s=0, poll_s=0, token=None):
        return {i: self.store[i] for i in ids}


class TestRun(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.data = os.path.join(self.tmp.name, "data")
        self.paths = gv.Paths(self.data, os.path.join(self.tmp.name, "reports"))
        os.makedirs(self.paths.atlas)
        with open(self.paths.graph, "w") as fh:
            json.dump({}, fh)
        for asn in (11, 12, 13):
            with open(os.path.join(self.paths.atlas, f"as_{asn}.json"), "w") as fh:
                json.dump({"asn": asn, "verdict": "SECURE (Verified Active)", "timestamp": now_iso(asn / 10)}, fh)
        for target, value in ((gv.analyze_harvest, {"load_ip2asn": lambda p: LOOKUP, "load_ix": lambda d: (IX, set(), [], [])}),
                              (gv.forensic, {"resolve_ip": lambda d, af=4: VALID if d.startswith("valid") else INVALID})):
            for name, fn in value.items():
                patcher = mock.patch.object(target, name, fn)
                patcher.start()
                self.addCleanup(patcher.stop)

    def run_it(self, client, *argv):
        return gv.main(["--data-dir", self.data, "--reports-dir", self.paths.reports, *argv], client)

    def results(self):
        return sorted(f for f in os.listdir(self.paths.gp) if f.startswith("as_")) if os.path.isdir(self.paths.gp) else []

    def test_limits_guard_stops_before_any_measurement(self):
        client = FakeClient(remaining=150)
        self.assertEqual(self.run_it(client), 0)
        self.assertEqual((client.limit_calls, client.posts, self.results()), (1, [], []))

    def test_run_writes_results_outside_atlas(self):
        client = FakeClient()
        self.run_it(client)
        self.assertEqual(self.results(), ["as_11.json", "as_12.json", "as_13.json"])
        self.assertEqual(len(client.posts), 6)
        self.assertEqual([p[0] for p in client.posts[:2]], [VALID, INVALID])
        self.assertEqual(client.posts[1][1], "M0")                       # invalid reuses the valid measurement's probes
        self.assertEqual(sorted(os.listdir(self.paths.atlas)), ["as_11.json", "as_12.json", "as_13.json"])
        self.assertEqual(len(os.listdir(self.paths.raw)), 6)
        self.assertEqual(len(os.listdir(self.paths.probes)), 1)
        saved = gv._read_json(self.paths.result(11), None)
        self.assertEqual((saved["source"], saved["total_probes"]), ("globalping", 3))
        self.assertNotIn("non_rov_hops", json.dumps(saved))
        self.assertEqual(gv.spent_today(self.paths), 18)
        self.assertEqual(len(report.load_runs(self.paths)), 3)

    def test_budget_stops_the_run_and_carries_over_the_day(self):
        client = FakeClient()
        self.run_it(client, "--budget", "12")
        self.assertEqual(self.results(), ["as_11.json", "as_12.json"])
        self.assertEqual(gv.spent_today(self.paths), 12)
        again = FakeClient()
        self.run_it(again, "--budget", "12")                               # nothing left today
        self.assertEqual(again.posts, [])

    def test_rate_limit_header_is_honoured(self):
        client = FakeClient(header_remaining=4)                            # another client used the allowance
        self.run_it(client)
        self.assertEqual(self.results(), ["as_11.json"])
        self.assertEqual(len(client.posts), 2)

    def test_http_429_stops_the_run(self):
        client = FakeClient(fail_after=2)
        self.assertEqual(self.run_it(client), 0)
        self.assertEqual(self.results(), ["as_11.json"])
        self.assertEqual(gv.spent_today(self.paths), 6)

    def test_dry_run_creates_nothing(self):
        client = FakeClient()
        self.run_it(client, "--dry-run")
        self.assertEqual((client.posts, client.limit_calls), ([], 0))
        self.assertFalse(os.path.exists(self.paths.gp))

    def test_named_targets_and_no_probes(self):
        client = FakeClient()
        self.run_it(client, "--asns", "AS12, 777")
        self.assertEqual(self.results(), ["as_12.json"])
        self.assertIn("777", gv.load_dated(os.path.join(self.paths.gp, "no_probes.json")))

    def test_fresh_results_are_not_selected_again(self):
        self.run_it(FakeClient())
        second = FakeClient()
        self.run_it(second, "--budget", "400")
        self.assertEqual(second.posts, [])

    def test_reanalyse_rebuilds_from_raw(self):
        self.run_it(FakeClient())
        before = gv._read_json(self.paths.result(11), None)
        os.remove(self.paths.result(12))
        with open(self.paths.result(11), "w") as fh:
            json.dump({**before, "verdict": "VULNERABLE"}, fh)
        self.assertEqual(gv.main(["--data-dir", self.data, "--reanalyse"]), 0)
        self.assertEqual(gv._read_json(self.paths.result(11), None), before)
        self.assertEqual(self.results(), ["as_11.json", "as_13.json"])

    def test_output_under_an_atlas_directory_is_refused(self):
        bad = gv.Paths(self.paths.atlas)
        with self.assertRaises(ValueError):
            gv.check_output_dir(bad)
        with self.assertRaises(ValueError):
            gv.write_result(bad, one_probe(VALID_VIA_T, [GW, H_C]))
        gv.check_output_dir(self.paths)
        self.assertFalse(os.path.abspath(self.paths.result(1)).startswith(os.path.abspath(self.paths.atlas) + os.sep))

    def test_write_result_refuses_non_rov_hops(self):
        r = one_probe(VALID_VIA_T, [GW, H_C])
        r["non_rov_hops"] = [1]
        with self.assertRaises(ValueError):
            gv.write_result(self.paths, r)


def pair_row(asn, g, a, g_adj=None, a_adj=None):
    return {"asn": asn, "gp_class": g, "atlas_class": a, "gp_class_adj": g_adj or g, "atlas_class_adj": a_adj or a}


class TestCompare(unittest.TestCase):
    def good_sample(self):
        return [pair_row(i, "SECURE", "SECURE") for i in range(30)] + \
               [pair_row(100 + i, "VULNERABLE", "VULNERABLE") for i in range(30)]

    def test_pass_needs_every_criterion(self):
        crit = report.evaluate(self.good_sample(), (20, 20))
        self.assertTrue(report.passed(crit))
        self.assertFalse(report.passed(report.evaluate(self.good_sample(), (19, 19))))     # too few repeats
        self.assertFalse(report.passed(report.evaluate(self.good_sample(), (20, 18))))     # 90% the same

    def test_small_or_one_sided_sample_is_not_yet(self):
        few = [pair_row(i, "VULNERABLE", "VULNERABLE") for i in range(70)]
        crit = {c["name"]: c for c in report.evaluate(few, (20, 20))}
        self.assertFalse(crit["Sample"]["ok"])
        self.assertTrue(crit["Overall agreement"]["ok"])
        self.assertFalse(crit["Globalping SECURE confirmed by Atlas"]["ok"])              # nothing to count is not a pass
        self.assertFalse(report.passed(list(crit.values())))

    def test_no_data_at_all_is_not_yet(self):
        self.assertFalse(any(c["ok"] for c in report.evaluate([], (0, 0))))

    def test_false_secure_fails_the_secure_criterion(self):
        pairs = self.good_sample() + [pair_row(900 + i, "SECURE", "VULNERABLE") for i in range(4)]
        crit = {c["name"]: c for c in report.evaluate(pairs, (20, 20))}
        self.assertFalse(crit["Globalping SECURE confirmed by Atlas"]["ok"])              # 30/34 = 88%
        self.assertFalse(crit["Overall agreement"]["ok"])                                  # 60/64 = 94%

    def test_inconclusive_sides_are_left_out(self):
        pairs = self.good_sample() + [pair_row(900, None, "SECURE"), pair_row(901, "VULNERABLE", None)]
        self.assertTrue(report.passed(report.evaluate(pairs, (20, 20))))

    def test_adjusted_columns_are_judged_apart(self):
        pairs = self.good_sample() + [pair_row(900 + i, "VULNERABLE", "SECURE", "SECURE", "SECURE") for i in range(5)]
        self.assertFalse(report.passed(report.evaluate(pairs, (20, 20))))
        self.assertTrue(report.passed(report.evaluate(pairs, (20, 20), "_adj")))

    def test_pairs_need_results_within_seven_days(self):
        g = {1: {"verdict": "VULNERABLE", "timestamp": now_iso(0)}, 2: {"verdict": "VULNERABLE", "timestamp": now_iso(0)},
             3: {"verdict": "INCONCLUSIVE", "timestamp": now_iso(0)}}
        a = {1: {"asn": 1, "verdict": "VULNERABLE", "timestamp": now_iso(6.5)},
             2: {"asn": 2, "verdict": "VULNERABLE", "timestamp": now_iso(7.5)},
             3: {"asn": 3, "verdict": "SECURE (Verified Active)", "timestamp": now_iso(1)}}
        pairs = report.build_pairs(g, a)
        self.assertEqual([(p["asn"], p["gp_class"], p["atlas_class"]) for p in pairs],
                         [(1, "VULNERABLE", "VULNERABLE"), (3, None, "SECURE")])

    def test_atlas_result_with_origin_as_drop_point(self):
        a = {"asn": T, "verdict": "VULNERABLE", "timestamp": now_iso(),
             "probe_details": [{"verdict": "SECURE (Upstream Filtered)", "boundary_asn": CF, "path_i": [T]},
                               {"verdict": "INCONCLUSIVE (Off-Path)", "boundary_asn": None, "path_i": []}]}
        self.assertEqual(report.atlas_adjusted(a), "SECURE (Verified Active)")
        self.assertEqual(report.atlas_adjusted({"asn": T, "verdict": "VULNERABLE"}), "VULNERABLE")

    def test_repeatability_counts_reruns_a_day_apart(self):
        t0 = datetime(2026, 11, 28, 3, 20, tzinfo=timezone.utc)
        runs = [{"asn": 1, "timestamp": t0.isoformat(), "verdict": "VULNERABLE"},
                {"asn": 1, "timestamp": (t0 + timedelta(hours=24)).isoformat(), "verdict": "VULNERABLE"},
                {"asn": 2, "timestamp": t0.isoformat(), "verdict": "SECURE (Verified Active)"},
                {"asn": 2, "timestamp": (t0 + timedelta(hours=24)).isoformat(), "verdict": "VULNERABLE"},
                {"asn": 3, "timestamp": t0.isoformat(), "verdict": "VULNERABLE"},
                {"asn": 3, "timestamp": (t0 + timedelta(hours=2)).isoformat(), "verdict": "VULNERABLE"},
                {"asn": 4, "timestamp": t0.isoformat(), "verdict": "INCONCLUSIVE"},
                {"asn": 4, "timestamp": (t0 + timedelta(hours=24)).isoformat(), "verdict": "VULNERABLE"}]
        self.assertEqual(report.repeatability(runs), (2, 1))

    def test_report_lists_disagreements_with_both_measurement_ids(self):
        g = one_probe(VALID_VIA_T, [GW, H_C, H_T, H_T2, H_U, H_EDGE, H_DST_I])
        g["timestamp"] = now_iso()
        a = {"asn": T, "verdict": "SECURE (Verified Active)", "timestamp": now_iso(1), "verdict_counts": {},
             "measurement_ids": {"trace_valid": 111, "trace_invalid": 222}}
        text, summary = report.render_compare(report.build_pairs({T: g}, {T: a}), [], {T: {"name": "Target Net"}}, 1)
        self.assertIn("**Result: NOT YET**", text)
        self.assertEqual(summary["disagreements"], [T])
        for needle in ("AS100 Target Net", "trace_valid 111", "trace_invalid 222", "mtr_valid V1", "mtr_invalid I1",
                       "| eyeball | customer | 1 | 0 | 0 | 1 | 0.0% (0/1) |"):
            self.assertIn(needle, text)

    def test_coverage_counts(self):
        probes = [{"location": {"country": "NZ", "asn": 21}, "tags": ["eyeball-network"]},
                  {"location": {"country": "NZ", "asn": 22}, "tags": ["datacenter-network"]},
                  {"location": {"country": "SB", "asn": 23}, "tags": ["datacenter-network"]}]
        meta = {1: {"cone": 5, "cc": "NZ"}, 5: {"cone": 2, "cc": "NZ"}, 21: {"cone": 0, "cc": "NZ"}}
        atlas = {1: {"verdict": "SECURE (Verified Active)", "timestamp": now_iso(1)},
                 21: {"verdict": "INCONCLUSIVE", "timestamp": now_iso(1)},
                 5: {"verdict": "VULNERABLE", "timestamp": now_iso(30)}}
        s = report.coverage_stats(probes, {1: [21, 22], 5: [99]}, meta, {21}, atlas, [1, 5, 22])
        self.assertEqual((s["probes"], s["asns"], s["dc_only_asns"], s["also_atlas"], s["not_atlas"]), (3, 3, 2, 1, 2))
        self.assertEqual((s["transit"], s["t_gp"], s["t_atlas"], s["t_gp_only"]), (2, 1, 1, []))
        self.assertEqual(s["no_probes"], {1: "customer", 5: None, 22: "inside"})
        self.assertEqual(s["fresh"], {"SECURE": {"customer": 1}, "INCONCLUSIVE": {"inside": 1}})
        nz = next(c for c in s["pacific"] if c["cc"] == "NZ")
        self.assertEqual((nz["probes"], nz["asns"], nz["new"]), (2, [21, 22], [22]))


class FakeResponse:
    def __init__(self, status=200, payload=None, headers=None):
        self.status_code, self._payload, self.headers, self.text = status, payload, headers or {}, json.dumps(payload)

    def json(self):
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise gp.requests.HTTPError(str(self.status_code), response=self)


class TestClient(unittest.TestCase):
    def test_create_sends_generic_user_agent_and_reads_rate_limit(self):
        seen = {}

        def post(url, json=None, headers=None, timeout=None):
            seen.update(url=url, body=json, headers=headers)
            return FakeResponse(202, {"id": "abc", "probesCount": 3}, {"X-RateLimit-Remaining": "241"})

        with mock.patch.object(gp.requests, "post", post):
            created = gp.create_measurement(VALID, [{"asn": T, "limit": 3}], "mtr", {"protocol": "ICMP", "packets": 3})
        self.assertEqual(created, gp.Created("abc", 3, 241))
        self.assertEqual(seen["headers"]["User-Agent"], "rov-audit-measurement-client")
        self.assertIn("gzip", seen["headers"]["Accept-Encoding"])
        self.assertNotIn("Authorization", seen["headers"])
        self.assertEqual(seen["body"], {"type": "mtr", "target": VALID, "locations": [{"asn": T, "limit": 3}],
                                        "measurementOptions": {"protocol": "ICMP", "packets": 3}})

    def test_reusing_a_measurement_sends_its_id_as_locations(self):
        seen = {}

        def post(url, json=None, headers=None, timeout=None):
            seen.update(body=json)
            return FakeResponse(202, {"id": "def", "probesCount": 3})

        with mock.patch.object(gp.requests, "post", post):
            created = gp.create_measurement(INVALID, "abc")
        self.assertEqual(seen["body"]["locations"], "abc")
        self.assertIsNone(created.rate_limit_remaining)

    def test_429_raises_rate_limited(self):
        with mock.patch.object(gp.requests, "post", lambda *a, **k: FakeResponse(429, {"error": "limit"})):
            with self.assertRaises(gp.RateLimited):
                gp.create_measurement(VALID, [{"asn": T, "limit": 1}])

    def test_limits_and_token(self):
        payload = {"rateLimit": {"measurements": {"create": {"type": "ip", "limit": 250, "remaining": 225, "reset": 9}}}}
        seen = {}

        def get(url, headers=None, timeout=None):
            seen.update(headers=headers)
            return FakeResponse(200, payload)

        with mock.patch.object(gp.requests, "get", get):
            self.assertEqual(gp.get_limits("tok"), gp.Limits("ip", 250, 225, 9))
        self.assertEqual(seen["headers"]["Authorization"], "Bearer tok")

    def test_token_is_optional(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(gp.load_token(os.path.join(d, "missing.yaml")))
            path = os.path.join(d, "secrets.yaml")
            with open(path, "w") as fh:
                fh.write('ripe_atlas_key: "x"\n')
            self.assertIsNone(gp.load_token(path))
            with open(path, "a") as fh:
                fh.write('globalping_token: "abc123"\n')
            self.assertEqual(gp.load_token(path), "abc123")

    def test_polling_uses_etags_and_waits_between_gets(self):
        clock = {"t": 0.0}
        calls = []
        replies = [FakeResponse(200, {"id": "m", "status": "in-progress"}, {"ETag": 'W/"1"'}),
                   FakeResponse(304, None),
                   FakeResponse(200, {"id": "m", "status": "finished"}, {"ETag": 'W/"2"'})]

        def get(url, headers=None, timeout=None):
            calls.append((clock["t"], headers.get("If-None-Match")))
            return replies[len(calls) - 1]

        def sleep(s):
            clock["t"] += s

        with mock.patch.object(gp.requests, "get", get), mock.patch.object(gp.time, "sleep", sleep), \
                mock.patch.object(gp.time, "monotonic", lambda: clock["t"]):
            done = gp.wait_for_all(["m"], timeout_s=60, poll_s=0.1)
        self.assertEqual(done["m"]["status"], "finished")
        self.assertEqual([etag for _, etag in calls], [None, 'W/"1"', 'W/"1"'])
        gaps = [b[0] - a[0] for a, b in zip(calls, calls[1:])]
        self.assertTrue(all(g >= gp.MIN_POLL_GAP_S for g in gaps), gaps)

    def test_unfinished_measurement_is_returned_as_last_seen(self):
        clock = {"t": 0.0}

        def get(url, headers=None, timeout=None):
            return FakeResponse(200, {"id": "m", "status": "in-progress", "results": [{"result": {"status": "in-progress"}}]})

        def sleep(s):
            clock["t"] += s

        with mock.patch.object(gp.requests, "get", get), mock.patch.object(gp.time, "sleep", sleep), \
                mock.patch.object(gp.time, "monotonic", lambda: clock["t"]):
            done = gp.wait_for_all(["m"], timeout_s=5, poll_s=1)
        self.assertEqual(done["m"]["status"], "in-progress")
        self.assertIsNone(gv.mtr_reach(done["m"]["results"][0]["result"], VALID))


if __name__ == "__main__":
    unittest.main()
