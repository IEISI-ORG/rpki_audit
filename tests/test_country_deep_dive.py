"""
tests/test_country_deep_dive.py

analyze_country_deep_dive_v2.py: the IPv6 verdict summary and the list of networks whose IPv6
verdict class differs from the main one (2026-10-16). No file access.
"""
import unittest

import numpy as np
import pandas as pd

import analyze_country_deep_dive_v2 as dd


def frame(rows):
    return pd.DataFrame(rows, columns=["asn", "name", "cone", "verdict", "v6_verdict", "v6_dirty_feeds", "v6_total_feeds"])


ROWS = [
    (1, "Stub behind HE", 0, "STUB: VULNERABLE", "STUB: PASSIVE (Clean Pipe)", 0, 1),
    (2, "Same both", 5, "VULNERABLE", "VULNERABLE", 2, 2),
    (3, "Worse in v6", 9, "PASSIVE (Clean Pipe)", "PARTIAL: VULNERABLE (Mixed)", 1, 2),
    (4, "IPv4 only", 3, "STUB: VULNERABLE", np.nan, np.nan, np.nan),   # blank cells load as NaN
]


class TestV6Summary(unittest.TestCase):
    def test_counts_only_networks_with_an_ipv6_verdict(self):
        s = dd.v6_summary(frame(ROWS))
        self.assertEqual(s["networks"], 3)
        self.assertEqual(s["main"]["SECURE"], 1)       # only AS3, among the three seen in IPv6
        self.assertEqual(s["v6"]["SECURE"], 1)         # AS1
        self.assertEqual(s["main"]["VULNERABLE"], 2)
        self.assertEqual(s["v6"]["VULNERABLE"], 1)

    def test_audit_without_ipv6_columns(self):
        df = frame(ROWS).drop(columns=["v6_verdict", "v6_dirty_feeds", "v6_total_feeds"])
        self.assertIsNone(dd.v6_summary(df))
        self.assertTrue(dd.v6_differences(df).empty)


class TestV6Differences(unittest.TestCase):
    def test_class_changes_sorted_by_cone(self):
        diff = dd.v6_differences(frame(ROWS))
        self.assertEqual(diff["asn"].tolist(), [3, 1])

    def test_limit(self):
        self.assertEqual(len(dd.v6_differences(frame(ROWS), limit=1)), 1)


if __name__ == "__main__":
    unittest.main()
