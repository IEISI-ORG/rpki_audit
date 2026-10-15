"""
tests/test_he_ipv6_analysis.py

he_ipv6_analysis.py: path shares from exports.csv rows, peers' routes passed to non-customers
from triples, ASes that only one network passes on, ASPA gaps. No file access.
"""
import unittest

import he_ipv6_analysis as h

HE, T1, P, Q, CU, Y = 6939, 3356, 64500, 64501, 64502, 64503
# CAIDA as-rel2 shape: {(min, max): ("p2c", provider) | ("p2p", None)}
RELS = {(min(HE, P), max(HE, P)): ("p2p", None), (min(HE, Q), max(HE, Q)): ("p2p", None),
        (min(HE, CU), max(HE, CU)): ("p2c", HE), (min(HE, Y), max(HE, Y)): ("p2c", HE)}


class TestPathTotals(unittest.TestCase):
    def test_total_counts_each_path_once_at_its_collector_end(self):
        # path [Y, HE, P] x 10: link HE-P passed beyond (10/10), link Y-HE at the collector end (10/0)
        rows = [(HE, P, 6, 10, 10), (Y, HE, 6, 10, 0), (T1, P, 6, 30, 0)]
        t = h.path_totals(rows)
        self.assertEqual(t.paths[6], 40)
        self.assertEqual(t.mid_path[6][HE], 10)
        self.assertNotIn(Y, t.mid_path[6])

    def test_share_via_counts_only_paths_passed_beyond(self):
        # HE is a collector peer for 100 of P's paths (not counted), passes 30 on; T1 passes 10 on
        rows = [(HE, P, 6, 130, 30), (T1, P, 6, 10, 10), (HE, Q, 4, 5, 5)]
        shares = h.shares_via(h.path_totals(rows), HE)
        self.assertAlmostEqual(shares[6][P], 0.75)
        self.assertEqual(shares[4][Q], 1.0)
        self.assertNotIn(P, shares[4])


class TestTripleStats(unittest.TestCase):
    def stats(self, rows):
        s = h.TripleStats(RELS, tier1={T1})
        for r in rows:
            s.add(*r)
        return s

    def test_peer_route_passed_to_peer_or_tier1_is_counted(self):
        s = self.stats([(6, Q, HE, P), (6, T1, HE, Q)])
        self.assertEqual(s.peers_passed_up[6][HE], {P, Q})
        self.assertEqual(s.peers_seen[6][HE], {P, Q})

    def test_peer_route_passed_to_customer_is_valley_free(self):
        s = self.stats([(6, CU, HE, P)])
        self.assertEqual(s.peers_passed_up[6].get(HE, set()), set())
        self.assertEqual(s.peers_seen[6][HE], {P})

    def test_customer_route_passed_anywhere_is_not_counted(self):
        s = self.stats([(6, P, HE, CU), (6, T1, HE, CU)])
        self.assertEqual(s.peers_seen[6].get(HE, set()), set())

    def test_sole_passer_per_family(self):
        s = self.stats([(6, T1, HE, P), (4, T1, HE, P), (4, HE, Y, P), (6, T1, HE, Q), (6, T1, Y, Q)])
        self.assertEqual(s.only_passed_by(HE, 6), {P})
        self.assertEqual(s.only_passed_by(HE, 4), set())


class TestAspaGap(unittest.TestCase):
    def test_peers_relying_on_he_whose_aspa_omits_it(self):
        shares6 = {P: 0.9, Q: 0.8, CU: 0.95, Y: 0.2}
        aspa = {P: {T1}, Q: {HE, T1}, CU: {T1}, Y: {T1}}
        # P: peer, mostly via HE, ASPA without HE -> gap. Q lists HE. CU is a customer. Y below threshold.
        self.assertEqual(h.aspa_gap(shares6, RELS, aspa, HE, 0.5), [P])

    def test_as0_record_counts_as_omitting(self):
        self.assertEqual(h.aspa_gap({P: 1.0}, RELS, {P: {0}}, HE, 0.5), [P])

    def test_no_record_is_no_gap(self):
        self.assertEqual(h.aspa_gap({P: 1.0}, RELS, {}, HE, 0.5), [])


if __name__ == "__main__":
    unittest.main()
