"""
tests/test_harvest_analysis.py

Trace parsing in analyze_harvest.py: public Atlas traceroutes to Cloudflare's RPKI-invalid
beacon, turned into AS paths and "forwarded the invalid route" evidence. No network access.
"""
import unittest

import analyze_harvest as ah

DST = "103.21.244.19"


def hop(*ips):
    return {"hop": 1, "result": [{"from": ip, "rtt": 1.0} if ip != "*" else {"x": "*"} for ip in ips]}


def trace(*hops, dst=DST, prb=1):
    return {"type": "traceroute", "dst_addr": dst, "af": 4, "prb_id": prb, "timestamp": 1_790_000_000,
            "result": list(hops)}


LOOKUP = ah.IpAsn([(int(ah.ipaddress.ip_address("8.8.8.0")), int(ah.ipaddress.ip_address("8.8.8.255")), 15169),
                   (int(ah.ipaddress.ip_address("103.21.244.0")), int(ah.ipaddress.ip_address("103.21.247.255")), 13335),
                   (int(ah.ipaddress.ip_address("1.1.1.0")), int(ah.ipaddress.ip_address("1.1.1.255")), 64500)])


class TestHops(unittest.TestCase):
    def test_first_public_responder_per_hop(self):
        t = trace(hop("192.168.1.1", "192.168.1.1"), hop("*", "1.1.1.5"), hop("*", "*", "*"), hop(DST))
        self.assertEqual(ah.hop_ips(t), ["1.1.1.5", DST])

    def test_reached_only_when_destination_answers(self):
        self.assertTrue(ah.reached(trace(hop("1.1.1.5"), hop(DST))))
        self.assertFalse(ah.reached(trace(hop("1.1.1.5"), hop("*", "*", "*"))))

    def test_malformed_hops_ignored(self):
        t = trace({"hop": 1, "error": "network unreachable"}, {"hop": 2}, hop("1.1.1.5"))
        self.assertEqual(ah.hop_ips(t), ["1.1.1.5"])


class TestAsPath(unittest.TestCase):
    def test_lookup(self):
        self.assertEqual(LOOKUP.asn("8.8.8.8"), 15169)
        self.assertIsNone(LOOKUP.asn("9.9.9.9"))
        self.assertIsNone(LOOKUP.asn("2001:db8::1"))

    def test_as_runs_count_hops_per_as(self):
        runs = ah.as_runs(["1.1.1.5", "1.1.1.6", "9.9.9.9", "8.8.8.8", DST], LOOKUP)
        self.assertEqual(runs, [(64500, 2), (15169, 1), (13335, 1)])

    def test_credible_forwarders(self):
        # probe's AS with a hop of its own; an AS with >= 2 hops; an AS handing the trace to the beacon
        self.assertEqual(ah.credible_forwarders([(64999, 1), (64500, 2), (15169, 1), (13335, 1)],
                                                probe_asn=64999), {64999, 64500, 15169})

    def test_probe_as_needs_a_hop_of_its_own(self):
        # Swisscom shape (2026-10-10): only the destination answered; in-network Atlas tests on
        # 2026-10-15 showed Swisscom dropping the invalid route. One data point isn't enough.
        self.assertEqual(ah.credible_forwarders([(13335, 1)], probe_asn=3303), set())

    def test_single_border_hop_between_two_ases_is_not_a_forwarder(self):
        # Lumen shape (2026-01-04): 399078 -> one 3356-numbered hop -> 26042 -> 13335
        runs = [(399078, 1), (3356, 1), (26042, 1), (13335, 1)]
        self.assertEqual(ah.credible_forwarders(runs, probe_asn=399078), {399078, 26042})

    def test_beacon_origin_never_a_forwarder(self):
        self.assertEqual(ah.credible_forwarders([(13335, 3)], probe_asn=None), set())


    def test_excluded_ases_are_not_forwarders(self):
        # IXP ASNs: they announce the IX LAN, so they appear on paths
        runs = [(64500, 2), (6895, 1), (13335, 1)]
        self.assertEqual(ah.credible_forwarders(runs, probe_asn=None, exclude={6895}), {64500})


class TestIxAnnouncers(unittest.TestCase):
    def test_announcer_must_be_on_that_ix_lan(self):
        ip = ah.ipaddress.ip_address
        t = ah.IpAsn([(int(ip("38.10.0.0")), int(ip("38.10.0.255")), 174),         # left over from 38/8
                      (int(ip("185.1.1.0")), int(ip("185.1.1.255")), 64600)])      # the IX's own ASN
        pfx = [{"prefix": "38.10.0.0/24", "ixlan_id": 1}, {"prefix": "185.1.1.0/24", "ixlan_id": 2}]
        nix = [{"ixlan_id": 1, "asn": 49378}, {"ixlan_id": 2, "asn": 64600}, {"ixlan_id": 2, "asn": 13335}]
        # 2026-10-15: IX LANs numbered out of Cogent's 38/8 mapped to Cogent, a member of none of them
        self.assertEqual(ah.ix_announcers(pfx, nix, t), {64600})


class TestIxpAsns(unittest.TestCase):
    """An IXP ASN needs two of three signals (Terry, 2026-10-15: more than one data point)."""

    def test_two_signals_needed(self):
        rs = ah.ixp_asns(peeringdb_rs={1, 2, 3}, as0={2, 3, 4}, ix_announcers={3, 4, 5})
        self.assertEqual(rs, {2, 3, 4})

    def test_two_peeringdb_fields_alone_are_not_enough(self):
        # "Route Server" type and exchange ownership are both entered by PeeringDB admins
        rs = ah.ixp_asns(peeringdb_rs={1}, as0=set(), ix_announcers=set(), exchange_owned={1})
        self.assertEqual(rs, set())

    def test_exchange_owned_with_as0_counts(self):
        # e.g. an exchange's own ASN that publishes AS0 but isn't typed "Route Server"
        rs = ah.ixp_asns(peeringdb_rs=set(), as0={2}, ix_announcers=set(), exchange_owned={2})
        self.assertEqual(rs, {2})

    def test_load_exchange_owned(self):
        import json
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            json.dump({"data": [{"asn": 6777, "org_id": 1}, {"asn": 174, "org_id": 2}]},
                      open(os.path.join(d, "net_all.json"), "w"))
            json.dump({"data": [{"id": 26, "org_id": 1}]}, open(os.path.join(d, "ix_org.json"), "w"))
            self.assertEqual(ah.load_exchange_owned(d), {6777})
            self.assertEqual(ah.load_exchange_owned(os.path.join(d, "missing")), set())

    def test_asn_with_providers_is_not_an_ixp_asn(self):
        # an exchange's cache-fill or operator ASN buys transit (Terry, 2026-10-15); an IXP's
        # route-server ASN has no providers
        rs = ah.ixp_asns(peeringdb_rs=set(), as0=set(), ix_announcers={3, 4}, exchange_owned={3, 4},
                         with_providers={3})
        self.assertEqual(rs, set())   # 4: owned + announces is one fact (it numbers the LAN), see below

    def test_owned_and_announcing_is_one_signal(self):
        # the operator numbering the IX LAN from its own space makes both true at once
        self.assertEqual(ah.ixp_asns(peeringdb_rs=set(), as0=set(), ix_announcers={4}, exchange_owned={4}), set())
        self.assertEqual(ah.ixp_asns(peeringdb_rs={4}, as0=set(), ix_announcers={4}, exchange_owned={4}), {4})

    def test_providers_from_aspa_and_graph(self):
        aspa = {10: {0}, 11: {174}, 12: {0}}
        graph_providers = {12: {3356}, 13: {1299}}
        # 11: ASPA lists a provider; 13: inferred provider, no AS0; 12: inferred, but signed AS0 wins
        self.assertEqual(ah.asns_with_providers(aspa, graph_providers), {11, 13})

    def test_ixf_export_is_an_outside_signal(self):
        # JINX shape: "Route Server" type + exchange-owned, marked member_type "ixp" in the IX-F export
        self.assertEqual(ah.ixp_asns(peeringdb_rs={37700}, as0=set(), ix_announcers=set(),
                                     exchange_owned={37700}, ixf_ixp={37700}), {37700})
        # the export mark alone isn't enough
        self.assertEqual(ah.ixp_asns(peeringdb_rs=set(), as0=set(), ix_announcers=set(), ixf_ixp={5}), set())

    def test_ixf_management_asn_with_providers_rejected(self):
        # DE-CIX Management 51531: marked "ixp", exchange-owned, but buys transit
        self.assertEqual(ah.ixp_asns(peeringdb_rs=set(), as0=set(), ix_announcers=set(), exchange_owned={51531},
                                     ixf_ixp={51531}, with_providers={51531}), set())

    def test_load_ixf_ixp(self):
        import json
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            json.dump({"version": "1.0", "member_list": [{"asnum": 37700, "member_type": "ixp"},
                                                         {"asnum": 174, "member_type": "peering"},
                                                         {"asnum": "x", "member_type": "ixp"}]},
                      open(os.path.join(d, "a.json"), "w"))
            open(os.path.join(d, "broken.json"), "w").write("{not json")
            json.dump({"https://ix.example/x.json": {"file": "a.json"}, "https://bad": {"error": "x"}},
                      open(os.path.join(d, "index.json"), "w"))
            self.assertEqual(ah.load_ixf_ixp(d), {37700})

    def test_seen_mid_path_is_not_an_ixp_asn(self):
        # an IXP's route servers are transparent (RFC 7947): its ASN doesn't carry traffic in BGP
        rs = ah.ixp_asns(peeringdb_rs={1, 2}, as0={1, 2}, ix_announcers=set(), mid_path={2})
        self.assertEqual(rs, {1})

    def test_mid_path_from_asn_stats(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            # 64600: origin only (no right neighbour). 6777 (AMS-IX RS): mid-path for 2 members using
            # non-transparent sessions. 174: transit for hundreds of networks.
            for rrc, rows in (("rrc00", ["64600,40,0,40,90", "6777,2,4,6,64", "174,107,6495,6602,9000"]),
                              ("rrc23", ["6777,1,3,4,5"])):
                os.makedirs(os.path.join(d, rrc))
                with open(os.path.join(d, rrc, "asn_stats.csv"), "w") as f:
                    f.write("ASN,Left_Count,Right_Count,Total_Neighbors,Total_Paths\n" + "\n".join(rows) + "\n")
            self.assertEqual(ah.load_mid_path(d), {174})

    def test_tier1_with_as0_is_not_an_ixp_asn(self):
        # Cogent publishes AS0 and announces an IX LAN prefix: for a Tier 1, AS0 supports Tier 1
        self.assertEqual(ah.ixp_asns(peeringdb_rs=set(), as0={174, 1299}, ix_announcers={174},
                                              tier1={174, 1299}), set())


class TestIxHops(unittest.TestCase):
    IX = ah.IxMap([{"prefix": "198.32.118.0/24"}, {"prefix": "2001:504:f::/64"}],
                  [{"asn": 8075, "ipaddr4": "198.32.118.91", "ipaddr6": "2001:504:f::8075:2"}])

    def test_participant_owns_the_ix_address(self):
        self.assertEqual(self.IX.lookup("198.32.118.91"), (True, 8075))
        self.assertEqual(self.IX.lookup("2001:504:f::8075:2"), (True, 8075))
        self.assertEqual(self.IX.lookup("198.32.118.7"), (True, None))
        self.assertEqual(self.IX.lookup("8.8.8.8"), (False, None))

    def test_ix_hop_attributed_to_participant_or_dropped(self):
        runs = ah.as_runs(["1.1.1.5", "198.32.118.91", "198.32.118.7", "8.8.8.8"], LOOKUP, ix=self.IX)
        self.assertEqual(runs, [(64500, 1), (8075, 1), (15169, 1)])


if __name__ == "__main__":
    unittest.main()
