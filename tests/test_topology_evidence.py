"""
tests/test_topology_evidence.py

Export evidence from bgp-extractor (exports.csv) and how build_topology_from_go.build_graph
uses it: per-link phantom pruning, restoring dropped links the evidence confirms (loop-free),
and EVIDENCE_REQUIRED_ASNS (Hurricane Electric: provider only with IPv4 Tier 1 evidence).
No network access.
"""
import os
import tempfile
import unittest

import build_topology_from_go as btg
import rov_utils

T1 = 3356
HE = 6939
A, B, C, D = 64500, 64501, 64502, 64503
B4, B6, T4, T6 = btg.EV_BEYOND_4, btg.EV_BEYOND_6, btg.EV_T1_4, btg.EV_T1_6


def regions(pairs_n):
    return {tuple(sorted(p)): {f"R{i}" for i in range(n)} for p, n in pairs_n.items()}


def graph(links):
    adj = {}
    for a, b in links:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return adj


class TestLoadExports(unittest.TestCase):
    def test_bits_per_family(self):
        with tempfile.TemporaryDirectory() as d:
            for rrc, rows in (("rrc00", ["64500,64501,4,10,3,0", "64500,64501,6,5,5,2"]),
                              ("rrc23", ["64502,64503,4,7,0,0", "64501,64500,4,2,2,1"])):
                os.makedirs(os.path.join(d, rrc))
                with open(os.path.join(d, rrc, "exports.csv"), "w") as f:
                    f.write("X,C,AF,Paths,Beyond,ToTier1\n" + "\n".join(rows) + "\n")
            ev = btg.load_exports(d)
        self.assertEqual(ev[(A, B)], B4 | B6 | T6)
        self.assertEqual(ev[(B, A)], B4 | T4)
        self.assertEqual(ev[(C, D)], 0)

    def test_no_files_returns_none(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(btg.load_exports(d))


class TestBuildGraph(unittest.TestCase):
    def build(self, links, degrees, regions_n, evidence):
        down, labels = btg.build_graph(graph(links), degrees, regions(regions_n), evidence)
        return {p: set(cs) for p, cs in down.items() if cs}, labels

    def test_link_only_at_collector_end_is_pruned(self):
        down, labels = self.build([(A, B)], {A: 50, B: 10}, {(A, B): 2}, {(A, B): 0})
        self.assertEqual(down, {})
        self.assertEqual(labels[(A, B)], (A, B, "pruned"))

    def test_link_passed_on_is_kept(self):
        down, labels = self.build([(A, B)], {A: 50, B: 10}, {(A, B): 2}, {(A, B): B4})
        self.assertEqual(down, {A: {B}})
        self.assertEqual(labels[(A, B)][2], "ratio_4x")

    def test_tier1_links_are_never_pruned(self):
        down, _ = self.build([(T1, A)], {T1: 10, A: 50}, {(T1, A): 1}, {})
        self.assertEqual(down, {T1: {A}})

    def test_single_region_link_restored_by_tier1_evidence(self):
        down, labels = self.build([(A, B)], {A: 50, B: 10}, {(A, B): 1}, {(A, B): B4 | T4})
        self.assertEqual(down, {A: {B}})
        self.assertEqual(labels[(A, B)], (A, B, "restored"))

    def test_peer_link_restored_by_tier1_evidence(self):
        down, _ = self.build([(A, B)], {A: 30, B: 10}, {(A, B): 2}, {(A, B): B6 | T6})
        self.assertEqual(down, {A: {B}})

    def test_no_restore_against_the_degree_order(self):
        # evidence says the smaller network provides the larger: would allow loops, so skipped
        down, labels = self.build([(A, B)], {A: 50, B: 10}, {(A, B): 1}, {(B, A): B4 | T4})
        self.assertEqual(down, {})
        self.assertEqual(labels[(A, B)][2], "single_region")

    def test_no_restore_when_evidence_points_both_ways(self):
        ev = {(A, B): B4 | T4, (B, A): B4 | T4}
        down, _ = self.build([(A, B)], {A: 50, B: 10}, {(A, B): 1}, ev)
        self.assertEqual(down, {})

    def test_evidence_required_provider_needs_ipv4_tier1_export(self):
        self.assertIn(HE, rov_utils.EVIDENCE_REQUIRED_ASNS)
        ev = {(HE, A): B4 | B6 | T6, (HE, B): B4 | T4}
        down, labels = self.build([(HE, A), (HE, B)], {HE: 500, A: 10, B: 10},
                                  {(HE, A): 2, (HE, B): 2}, ev)
        self.assertEqual(down, {HE: {B}})
        self.assertEqual(labels[(HE, A)], (HE, A, "evidence_required"))

    def test_restored_graph_has_no_loops(self):
        # A>B>C by degree; evidence for A->B, B->C and the loop-closing C->A
        links = [(A, B), (B, C), (C, A)]
        ev = {(A, B): B4 | T4, (B, C): B4 | T4, (C, A): B4 | T4}
        down, _ = self.build(links, {A: 30, B: 20, C: 10}, {p: 1 for p in links}, ev)
        self.assertEqual(down, {A: {B}, B: {C}})

    def test_without_evidence_falls_back_to_provider_pruning(self):
        down, labels = self.build([(A, B)], {A: 50, B: 10}, {(A, B): 2}, None)
        self.assertEqual(down, {A: {B}})
        self.assertEqual(labels[(A, B)][2], "ratio_4x")


if __name__ == "__main__":
    unittest.main()
