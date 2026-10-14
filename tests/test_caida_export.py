"""
tests/test_caida_export.py

Pure helpers in caida_export_test.py: CAIDA role lookup, export classes, verdicts and the
ASPA upstream-verification outcome. No network access.
"""
import unittest
from collections import Counter

import caida_export_test as ce

T1 = {3356, 1299}
X, C, P, Q = 64500, 64501, 64502, 64503
# CAIDA: P provides X, X peers with Q, X provides C
RELS = {(min(P, X), max(P, X)): ("p2c", P),
        (min(X, Q), max(X, Q)): ("p2p", None),
        (min(X, C), max(X, C)): ("p2c", X)}


class TestCaidaRole(unittest.TestCase):
    def test_roles(self):
        self.assertEqual(ce.caida_role(RELS, X, P), "provider")
        self.assertEqual(ce.caida_role(RELS, P, X), "customer")
        self.assertEqual(ce.caida_role(RELS, X, Q), "peer")
        self.assertIsNone(ce.caida_role(RELS, X, 64999))


class TestExportClasses(unittest.TestCase):
    def test_to_tier1_is_strict(self):
        self.assertEqual(ce.export_classes(3356, X, RELS, T1), ["up_strict"])

    def test_tier1_exporting_is_not_strict(self):
        self.assertEqual(ce.export_classes(1299, 3356, RELS, T1), [])

    def test_to_caida_provider_or_peer_is_up(self):
        self.assertEqual(ce.export_classes(P, X, RELS, T1), ["up_caida"])
        self.assertEqual(ce.export_classes(Q, X, RELS, T1), ["up_caida"])

    def test_to_caida_customer_is_down(self):
        self.assertEqual(ce.export_classes(C, X, RELS, T1), ["down"])


class TestVerdict(unittest.TestCase):
    def test_order(self):
        self.assertEqual(ce.verdict(None), "not seen")
        self.assertEqual(ce.verdict(Counter(down=5, up_caida=1, up_strict=1)), "provider (strict)")
        self.assertEqual(ce.verdict(Counter(down=5, up_caida=1)), "provider (via CAIDA label)")
        self.assertEqual(ce.verdict(Counter(down=5)), "only passed down")


class TestAspaOutcome(unittest.TestCase):
    def test_outcomes(self):
        aspa = {C: {X}, Q: {P}, P: set()}          # P: AS0-only ASPA
        self.assertEqual(ce.aspa_outcome(C, X, aspa), "ASPA lists it: Valid")
        self.assertEqual(ce.aspa_outcome(Q, X, aspa), "ASPA omits it: Invalid, dropped")
        self.assertEqual(ce.aspa_outcome(P, X, aspa), "ASPA omits it: Invalid, dropped")
        self.assertEqual(ce.aspa_outcome(64999, X, aspa), "no ASPA: Unknown, kept")


if __name__ == "__main__":
    unittest.main()
