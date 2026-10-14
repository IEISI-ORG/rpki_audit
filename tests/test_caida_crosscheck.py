"""
tests/test_caida_crosscheck.py

build_topology_from_go.infer_link (the per-link rule the builder runs, now with the
name of the rule that decided) and the CAIDA comparison helpers in caida_crosscheck.py.
No network access.
"""
import unittest

import build_topology_from_go as btg
import caida_crosscheck as cc
import rov_utils

T1 = 3356           # Lumen, in TIER_1_ASNS
T1B = 1299          # Arelion, in TIER_1_ASNS
NT = next(iter(rov_utils.NON_TRANSIT_ASNS))
A, B = 64500, 64501


def regions(n):
    """link_regions for the A-B link, seen from n distinct regions."""
    return {tuple(sorted((A, B))): set(["EU", "APAC", "NA"][:n])}


class TestInferLink(unittest.TestCase):
    def test_non_transit(self):
        self.assertEqual(btg.infer_link(NT, A, {NT: 100, A: 1}, {}), (None, None, "non_transit"))

    def test_tier1_pair_is_dropped(self):
        self.assertEqual(btg.infer_link(T1, T1B, {T1: 9, T1B: 9}, {}), (None, None, "t1_t1"))

    def test_tier1_always_provider(self):
        self.assertEqual(btg.infer_link(A, T1, {A: 5000, T1: 10}, {}), (T1, A, "tier1"))

    def test_ratio_4x_when_two_regions_see_it(self):
        deg = {A: 41, B: 10}
        self.assertEqual(btg.infer_link(A, B, deg, regions(2)), (A, B, "ratio_4x"))

    def test_exactly_4x_is_peering(self):
        self.assertEqual(btg.infer_link(A, B, {A: 40, B: 10}, regions(2)), (None, None, "peer"))

    # A link seen from one region is never transit by degree ratio (2026-10-14: the old 8x
    # rule agreed with CAIDA 18% of the time and with signed ASPA far less than ratio_4x).
    def test_single_region_is_never_transit_by_ratio(self):
        self.assertEqual(btg.infer_link(B, A, {A: 81, B: 10}, regions(1)), (None, None, "single_region"))
        self.assertEqual(btg.infer_link(A, B, {A: 100000, B: 1}, regions(1)), (None, None, "single_region"))
        self.assertEqual(btg.infer_link(A, B, {A: 50, B: 10}, regions(1)), (None, None, "single_region"))

    def test_single_region_below_4x_is_peer(self):
        self.assertEqual(btg.infer_link(A, B, {A: 40, B: 10}, regions(1)), (None, None, "peer"))

    def test_single_region_tier1_still_provider(self):
        self.assertEqual(btg.infer_link(A, T1, {A: 5000, T1: 10}, regions(1)), (T1, A, "tier1"))


class TestCaida(unittest.TestCase):
    LINES = ["# comment", "1|2|-1|bgp", "3|2|0|bgp", "4|5|-1|mlp"]

    def test_parse_as_rel2(self):
        rels = cc.parse_as_rel2(self.LINES)
        self.assertEqual(rels[(1, 2)], ("p2c", 1))
        self.assertEqual(rels[(2, 3)], ("p2p", None))
        self.assertEqual(rels[(4, 5)], ("p2c", 4))

    def test_compare_our_p2c(self):
        rels = cc.parse_as_rel2(self.LINES)
        self.assertEqual(cc.compare(1, 2, rels), "caida_same")
        self.assertEqual(cc.compare(2, 1, rels), "caida_reversed")
        self.assertEqual(cc.compare(3, 2, rels), "caida_p2p")
        self.assertEqual(cc.compare(7, 8, rels), "caida_absent")

    def test_compare_our_non_p2c(self):
        rels = cc.parse_as_rel2(self.LINES)
        self.assertEqual(cc.compare(None, None, rels, pair=(1, 2)), "caida_p2c")
        self.assertEqual(cc.compare(None, None, rels, pair=(2, 3)), "caida_p2p")
        self.assertEqual(cc.compare(None, None, rels, pair=(7, 8)), "caida_absent")

    def test_parse_ppdc(self):
        cones = cc.parse_ppdc(["# x", "10 10 11 12", "11 11"])
        self.assertEqual(cones, {10: 3, 11: 1})

    def test_customer_cone_size(self):
        down = {1: [2, 3], 2: [4], 3: [4, 5], 5: [1]}  # loop 5 -> 1 must not hang
        self.assertEqual(cc.cone_size(1, down), 5)  # 1 itself + 2,3,4,5
        self.assertEqual(cc.cone_size(9, down), 1)


if __name__ == "__main__":
    unittest.main()
