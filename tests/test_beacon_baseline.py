"""
tests/test_beacon_baseline.py

Parsing and summary logic of nz_beacon_baseline.py, on synthetic RIPE Atlas
results. No network access, no Atlas credits.
"""
import unittest

import nz_beacon_baseline as nb


def ping(prb, rcvd, sent=3):
    return {"prb_id": prb, "rcvd": rcvd, "sent": sent}


def trace(prb, hops):
    """hops: list of IP strings, or None for a silent hop."""
    return {"prb_id": prb, "result": [
        {"hop": i + 1, "result": [{"from": h, "rtt": 1.0}] if h else [{"x": "*"}]}
        for i, h in enumerate(hops)]}


class TestParsing(unittest.TestCase):
    def test_ping_reached(self):
        self.assertTrue(nb.ping_reached(ping(1, 2)))
        self.assertFalse(nb.ping_reached(ping(1, 0)))
        self.assertIsNone(nb.ping_reached(None))
        self.assertIsNone(nb.ping_reached({"prb_id": 1, "error": "timeout"}))

    def test_trace_hops_keeps_silent_hops(self):
        t = trace(1, ["192.168.1.1", None, "203.0.113.1"])
        self.assertEqual(nb.trace_hops(t), ["192.168.1.1", None, "203.0.113.1"])

    def test_trace_hops_first_responder_per_hop(self):
        t = {"prb_id": 1, "result": [{"hop": 1, "result": [{"x": "*"}, {"from": "198.51.100.1"}]}]}
        self.assertEqual(nb.trace_hops(t), ["198.51.100.1"])

    def test_trace_hops_missing(self):
        self.assertEqual(nb.trace_hops(None), [])

    def test_public_hops_skips_private_but_not_all_172(self):
        hops = ["192.168.88.1", "172.31.0.74", "172.68.84.6", "100.64.0.1", None, "10.0.0.1"]
        self.assertEqual(nb.public_hops(hops), ["172.68.84.6"])


class TestPaths(unittest.TestCase):
    MAP = {"203.0.113.1": 64500, "203.0.113.2": 64500, "198.51.100.1": 64501}

    def test_as_path_dedups_and_skips_unknown(self):
        hops = ["192.168.1.1", "203.0.113.1", None, "203.0.113.2", "192.0.2.9", "198.51.100.1"]
        self.assertEqual(nb.as_path(hops, self.MAP), [64500, 64501])

    def test_stop_asn_is_last_resolved_hop(self):
        hops = ["203.0.113.1", "198.51.100.1", None, None]
        self.assertEqual(nb.stop_asn(hops, self.MAP), 64501)
        self.assertIsNone(nb.stop_asn(["192.168.1.1", None], self.MAP))


class TestOutcome(unittest.TestCase):
    def test_reaches_invalid_by_ping_or_trace(self):
        self.assertEqual(nb.pair_outcome(True, True, False), "reaches-invalid")
        self.assertEqual(nb.pair_outcome(True, False, True), "reaches-invalid")

    def test_invalid_unreachable(self):
        self.assertEqual(nb.pair_outcome(True, False, False), "invalid-unreachable")

    def test_valid_unreachable_means_no_test(self):
        self.assertEqual(nb.pair_outcome(False, False, False), "no-valid")
        self.assertEqual(nb.pair_outcome(None, None, False), "no-data")


class TestProbeRows(unittest.TestCase):
    TARGETS = {"cf_valid": "192.0.2.10", "cf_invalid": "192.0.2.20",
               "ris_valid": "198.51.100.10", "ris_invalid": "198.51.100.20"}
    MAP = {"203.0.113.1": 64500, "192.0.2.20": 13335, "192.0.2.10": 13335,
           "198.51.100.10": 12654}

    def results(self):
        return {
            ("ping", "cf_valid"): {7: ping(7, 3)},
            ("ping", "cf_invalid"): {7: ping(7, 3)},
            ("ping", "ris_valid"): {7: ping(7, 3)},
            ("ping", "ris_invalid"): {7: ping(7, 0)},
            ("trace", "cf_valid"): {7: trace(7, ["203.0.113.1", "192.0.2.10"])},
            ("trace", "cf_invalid"): {7: trace(7, ["203.0.113.1", "192.0.2.20"])},
            ("trace", "ris_valid"): {7: trace(7, ["203.0.113.1", "198.51.100.10"])},
            ("trace", "ris_invalid"): {7: trace(7, ["203.0.113.1", None, None])},
        }

    def test_probe_row(self):
        probe = {"id": 7, "asn_v4": 64500, "is_anchor": False}
        row = nb.probe_row(probe, 4, self.results(), self.TARGETS, self.MAP)
        self.assertEqual(row["probe_asn"], 64500)
        self.assertEqual(row["cf"], "reaches-invalid")
        self.assertEqual(row["ris"], "invalid-unreachable")
        self.assertEqual(row["cf_invalid_path"], "64500 13335")
        self.assertEqual(row["ris_invalid_stop_asn"], 64500)

    def test_as_summary_counts(self):
        rows = [
            {"probe_asn": 64500, "af": 4, "cf": "reaches-invalid", "ris": "invalid-unreachable",
             "ris_invalid_stop_asn": 64500},
            {"probe_asn": 64500, "af": 4, "cf": "invalid-unreachable", "ris": "invalid-unreachable",
             "ris_invalid_stop_asn": 64501},
            {"probe_asn": 64500, "af": 4, "cf": "no-valid", "ris": "no-valid",
             "ris_invalid_stop_asn": None},
        ]
        s = nb.as_summary(rows)
        self.assertEqual(len(s), 1)
        r = s[0]
        self.assertEqual((r["asn"], r["af"], r["probes"]), (64500, 4, 3))
        self.assertEqual(r["cf_reach_invalid"], "1/2")
        self.assertEqual(r["ris_reach_invalid"], "0/2")


if __name__ == "__main__":
    unittest.main()
