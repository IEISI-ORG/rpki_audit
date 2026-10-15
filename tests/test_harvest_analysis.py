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
        # probe's own AS always; an AS with >= 2 hops; an AS handing the trace straight to the beacon
        self.assertEqual(ah.credible_forwarders([(64500, 2), (15169, 1), (13335, 1)], probe_asn=64999),
                         {64999, 64500, 15169})

    def test_single_border_hop_between_two_ases_is_not_a_forwarder(self):
        # Lumen shape (2026-01-04): 399078 -> one 3356-numbered hop -> 26042 -> 13335
        runs = [(399078, 1), (3356, 1), (26042, 1), (13335, 1)]
        self.assertEqual(ah.credible_forwarders(runs, probe_asn=399078), {399078, 26042})

    def test_beacon_origin_never_a_forwarder(self):
        self.assertEqual(ah.credible_forwarders([(13335, 3)], probe_asn=None), set())


    def test_excluded_ases_are_not_forwarders(self):
        # PeeringDB route-server networks: their ASN announces the IX LAN, so they appear on paths
        runs = [(64500, 2), (6895, 1), (13335, 1)]
        self.assertEqual(ah.credible_forwarders(runs, probe_asn=None, exclude={6895}), {64500})


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
