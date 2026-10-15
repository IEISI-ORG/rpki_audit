"""
tests/test_topology_evidence.py

Export evidence from bgp-extractor (exports.csv) and how build_topology_from_go.build_graph
uses it: per-link phantom pruning, restoring dropped links the evidence confirms (loop-free),
and EVIDENCE_REQUIRED_ASNS (Hurricane Electric: provider only with IPv4 Tier 1 evidence).
Path triples (triples.csv) and the top-down inference that replaces the Tier 1 override and
the degree ratio when they exist. No network access.
"""
import os
import tempfile
import unittest

import build_topology_from_go as btg
import rov_utils

T1 = 3356
T1B = 1299
HE = 6939
A, B, C, D, E = 64500, 64501, 64502, 64503, 64504
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



def triples(rows):
    out = {}
    for y, x, c, af in rows:
        out.setdefault(x, set()).add((y, c, af))
    return out


class TestLoadTriples(unittest.TestCase):
    def test_grouped_by_x_across_collectors(self):
        with tempfile.TemporaryDirectory() as d:
            for rrc, rows in (("rrc00", ["4,1299,3356,64500", "6,1299,3356,64500"]),
                              ("rrc23", ["4,1299,3356,64500", "4,3356,64500,64501"])):
                os.makedirs(os.path.join(d, rrc))
                with open(os.path.join(d, rrc, "triples.csv"), "w") as f:
                    f.write("AF,Y,X,C\n" + "\n".join(rows) + "\n")
            tr = btg.load_triples(d)
        self.assertEqual(tr, {T1: {(T1B, A, 4), (T1B, A, 6)}, A: {(T1, B, 4)}})

    def test_no_files_returns_none(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(btg.load_triples(d))


class TestTopDown(unittest.TestCase):
    """build_graph with path triples: x provides c when x passed c's route to its provider,
    or a Tier 1 passed it to another Tier 1."""

    def build(self, links, rows, degrees=None, regions_n=None, evidence=None, never_providers=frozenset()):
        degrees = degrees or {}
        for a, b in links:
            degrees.setdefault(a, 10)
            degrees.setdefault(b, 10)
        regions_n = regions_n or {p: 2 for p in links}
        evidence = evidence if evidence is not None else {}
        down, labels = btg.build_graph(graph(links), degrees, regions(regions_n), evidence,
                                       triples(rows), never_providers=never_providers)
        return {p: set(cs) for p, cs in down.items() if cs}, labels

    def test_tier1_provides_only_what_it_passes_to_another_tier1(self):
        # B is a transit AS (it passes D's route to C), so the T1-B link needs path evidence
        down, labels = self.build([(T1, A), (T1, B), (T1, T1B), (B, C), (B, D)],
                                  [(T1B, T1, A, 4), (C, B, D, 4)])
        self.assertEqual(down, {T1: {A}})
        self.assertEqual(labels[(T1, A)], (T1, A, "path"))
        self.assertEqual(labels[(T1, B)], (None, None, "unconfirmed"))

    def test_stub_next_to_a_tier1_is_its_customer(self):
        # B is never seen mid-path (a stub) and already has provider A from path evidence;
        # its link to T1 has none. A stub's Tier 1 neighbour is its provider (AS Rank step 9).
        links = [(T1, T1B), (T1, A), (A, B), (T1, B)]
        rows = [(T1B, T1, A, 4), (T1, A, B, 4)]
        down, labels = self.build(links, rows)
        self.assertEqual(down, {T1: {A, B}, A: {B}})
        self.assertEqual(labels[(T1, B)], (T1, B, "tier1"))

    def test_triples_used_without_export_evidence(self):
        down, btg_labels = btg.build_graph(graph([(T1, A), (T1, T1B)]), {T1: 10, T1B: 10, A: 10},
                                           regions({(T1, A): 2, (T1, T1B): 2}), None,
                                           triples([(T1B, T1, A, 4)]))
        self.assertEqual({p: set(cs) for p, cs in down.items() if cs}, {T1: {A}})
        self.assertEqual(btg_labels[(T1, A)], (T1, A, "path"))

    def test_customer_passed_to_a_provider_is_a_customer(self):
        down, labels = self.build([(T1, A), (A, B), (T1, T1B)], [(T1B, T1, A, 4), (T1, A, B, 4)])
        self.assertEqual(down, {T1: {A}, A: {B}})
        self.assertEqual(labels[(A, B)], (A, B, "path"))

    def test_route_passed_to_a_non_provider_says_nothing(self):
        # A passes B's route to C, but C is not A's provider (C could be A's customer)
        down, _ = self.build([(A, B), (A, C)], [(C, A, B, 4)])
        self.assertEqual(down, {})

    def test_no_loops_from_conflicting_evidence(self):
        links = [(T1, A), (T1, B), (T1, C), (A, B), (B, C), (C, A), (T1, T1B)]
        rows = [(T1B, T1, A, 4), (T1B, T1, B, 4), (T1B, T1, C, 4),
                (T1, A, B, 4), (T1, B, C, 4), (T1, C, A, 4)]
        down, _ = self.build(links, rows)
        edges = {(p, c) for p, cs in down.items() for c in cs}
        self.assertFalse({(A, B), (B, C), (C, A)} <= edges)
        self.assertEqual(len(edges & {(A, B), (B, C), (C, A)}), 2)

    def test_route_passed_to_a_tier1_peer_is_a_customer_route(self):
        # HE shape: no provider of its own, passes B's IPv4 route to a Tier 1 it peers with.
        # A Tier 1 is never a customer, so B must be HE's customer.
        down, _ = self.build([(T1, HE), (HE, B)], [(T1, HE, B, 4)])
        self.assertEqual(down, {HE: {B}})

    def test_cloudflare_is_a_provider(self):
        # Magic Transit / BYOIP shape (Windcave AS131168): RIS sees the customer only behind
        # Cloudflare, which passes its route to Tier 1s. reports/cloudflare_transit_rov.md
        cf = 13335
        self.assertNotIn(cf, rov_utils.NON_TRANSIT_ASNS)
        self.assertIn(cf, rov_utils.HARDCODED_SECURE)
        down, labels = self.build([(T1, cf), (cf, 131168)], [(T1, cf, 131168, 4)])
        self.assertEqual(down, {cf: {131168}})
        self.assertEqual(labels[(cf, 131168)], (cf, 131168, "path"))

    # Item 4 (2026-10-15): a ratio_4x link to a stub without path evidence is kept when >= 3
    # collector regions see it (signed ASPA 132 confirmed / 7 denied; 2 regions: 33 / 87).
    RATIO_STUB_LINKS = [(T1, T1B), (T1, A), (T1, D), (A, D)]
    RATIO_STUB_ROWS = [(T1B, T1, A, 4), (T1B, T1, D, 4)]   # D: a stub with path provider T1

    def ratio_stub_case(self, regions_ad, **kw):
        regions_n = {p: 3 for p in self.RATIO_STUB_LINKS}
        regions_n[(A, D)] = regions_ad
        return self.build(self.RATIO_STUB_LINKS, self.RATIO_STUB_ROWS, degrees={A: 50, D: 10},
                          regions_n=regions_n, evidence={(A, D): B4}, **kw)

    def test_ratio_link_to_stub_seen_in_three_regions_is_kept(self):
        self.assertEqual(rov_utils.STUB_RATIO_MIN_REGIONS, 3)
        down, labels = self.ratio_stub_case(3)
        self.assertEqual(down, {T1: {A, D}, A: {D}})
        self.assertEqual(labels[(A, D)], (A, D, "ratio_stub"))

    def test_ratio_link_to_stub_seen_in_two_regions_is_dropped(self):
        down, labels = self.ratio_stub_case(2)
        self.assertEqual(down, {T1: {A, D}})
        self.assertEqual(labels[(A, D)], (None, None, "unconfirmed"))

    def test_ratio_link_to_a_transit_network_is_not_kept_by_this_rule(self):
        # D passes E's route on (transit degree > 0), so the stub rule doesn't apply
        links = self.RATIO_STUB_LINKS + [(D, E)]
        rows = self.RATIO_STUB_ROWS + [(T1, D, E, 4)]
        down, labels = self.build(links, rows, degrees={A: 50, D: 10},
                                  regions_n={p: 5 for p in links}, evidence={(A, D): B4})
        self.assertEqual(labels[(A, D)], (None, None, "unconfirmed"))

    def test_ixp_asn_is_never_a_ratio_stub_provider(self):
        down, labels = self.ratio_stub_case(5, never_providers={A})
        self.assertEqual(down, {T1: {A, D}})
        self.assertEqual(labels[(A, D)], (None, None, "unconfirmed"))

    def test_customer_ranked_above_its_provider_is_accepted_when_no_loop(self):
        # One NZ / AS4768 shape: B passes C's route to its provider T1, but RIS sees C with more
        # transit neighbours than B, so C ranks above B. C's transit degree (3) is within
        # PATH_UP_RANK_MAX_RATIO (2) x B's (2), and B -> C closes no loop.
        links = [(T1, T1B), (T1, B), (B, C), (C, D), (C, E)]
        rows = [(T1B, T1, B, 4), (T1, B, C, 4), (B, C, D, 4), (B, C, E, 4)]
        self.assertEqual(rov_utils.PATH_UP_RANK_MAX_RATIO, 2)
        down, labels = self.build(links, rows)
        self.assertEqual(down, {T1: {B}, B: {C}, C: {D, E}})
        self.assertEqual(labels[(B, C)], (B, C, "path"))

    def test_customer_far_above_its_provider_is_not_accepted(self):
        # same, but C's transit degree (5) is more than twice B's (2)
        links = [(T1, T1B), (T1, B), (B, C), (C, D), (C, E), (C, A), (C, 64505)]
        rows = [(T1B, T1, B, 4), (T1, B, C, 4), (B, C, D, 4), (B, C, E, 4), (B, C, A, 4),
                (B, C, 64505, 4)]
        down, _ = self.build(links, rows)
        self.assertEqual(down, {T1: {B}})

    def test_evidence_required_provider_counts_ipv4_only(self):
        self.assertIn(HE, rov_utils.EVIDENCE_REQUIRED_ASNS)
        links = [(T1, HE), (HE, A), (HE, B), (T1, T1B)]
        rows = [(T1B, T1, HE, 4), (T1, HE, A, 6), (T1, HE, B, 4)]
        down, _ = self.build(links, rows)
        self.assertEqual(down, {T1: {HE}, HE: {B}})

    def test_ratio_fallback_only_for_ases_without_a_path_provider(self):
        # D and E have no path evidence; A-D and A-E are ratio_4x by degree. E already has
        # provider B from path evidence, so only D falls back.
        links = [(T1, A), (T1, B), (T1, T1B), (A, D), (A, E), (B, E)]
        rows = [(T1B, T1, A, 4), (T1B, T1, B, 4), (T1, B, E, 4)]
        degrees = {A: 50, B: 50, D: 10, E: 10}
        ev = {(A, D): B4, (A, E): B4}
        down, labels = self.build(links, rows, degrees=degrees, evidence=ev)
        self.assertEqual(down, {T1: {A, B}, A: {D}, B: {E}})
        self.assertEqual(labels[(A, D)], (A, D, "ratio_4x"))
        self.assertEqual(labels[(A, E)], (None, None, "unconfirmed"))



class TestIxpAsnsNonTransit(unittest.TestCase):
    # 2026-10-15: IXP ASNs: PeeringDB info_type "Route Server" and an AS0 ASPA record (two signals)
    AS0_IXP_ASNS = {6777, 32801, 41441, 42064, 43100, 44596, 46210, 47184, 47200, 47627, 49624, 51706,
                         53679, 55518, 57328, 58171, 59552, 60247, 62228, 197032, 201376, 212557, 212674,
                         213874, 215405, 218511, 219524}

    def test_as0_ixp_asns_are_non_transit(self):
        self.assertEqual(self.AS0_IXP_ASNS - rov_utils.NON_TRANSIT_ASNS, set())


if __name__ == "__main__":
    unittest.main()
