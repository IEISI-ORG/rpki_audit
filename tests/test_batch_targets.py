"""
tests/test_batch_targets.py

Atlas target selection in batch_verify_smart_v4.py. DISPUTED ASes (APNIC and
ROVista disagree) go first, because a conclusive Atlas result is what settles
them. ASes with no usable probes are skipped for 7 days so they can't hold a
slot every run. No network access.
"""
import json
import os
import sys
import tempfile
import types
import unittest
from datetime import date

import pandas as pd

# The forensic engine imports ripe.atlas.cousteau, which CI doesn't install.
sys.modules.setdefault("verify_forensic_path_v2", types.ModuleType("verify_forensic_path_v2"))
import batch_verify_smart_v4 as bv  # noqa: E402


def audit(rows):
    return pd.DataFrame(rows, columns=["asn", "verdict", "cone"])


NEVER_FRESH = lambda asn: False  # noqa: E731


class TestSelectTargets(unittest.TestCase):
    def test_disputed_before_stale_and_priority(self):
        df = audit([(1, "REGRESSED", 9000), (2, "DISPUTED", 5), (3, "VULNERABLE", 100)])
        t = bv.select_targets(df, stale={4}, is_fresh=NEVER_FRESH, skip=set(), limit=10)
        self.assertEqual(t[0], 2)
        self.assertEqual(t[1], 4)
        self.assertEqual(t[2:], [1, 3])

    def test_disputed_ordered_by_cone(self):
        df = audit([(1, "DISPUTED", 3), (2, "DISPUTED", 3000), (3, "DISPUTED", 40)])
        t = bv.select_targets(df, stale=set(), is_fresh=NEVER_FRESH, skip=set(), limit=10)
        self.assertEqual(t, [2, 3, 1])

    def test_disputed_can_take_every_slot(self):
        df = audit([(a, "DISPUTED", a) for a in range(1, 61)])
        t = bv.select_targets(df, stale={999}, is_fresh=NEVER_FRESH, skip=set(), limit=50)
        self.assertEqual(len(t), 50)
        self.assertNotIn(999, t)

    def test_disputed_slots_cap(self):
        df = audit([(a, "DISPUTED", a) for a in range(1, 11)])
        t = bv.select_targets(df, stale={999}, is_fresh=NEVER_FRESH, skip=set(),
                              limit=5, disputed_slots=2)
        self.assertEqual(t, [10, 9, 999])

    def test_fresh_disputed_is_not_queued(self):
        df = audit([(1, "DISPUTED", 100), (2, "DISPUTED", 50)])
        t = bv.select_targets(df, stale=set(), is_fresh=lambda a: a == 1, skip=set(), limit=10)
        self.assertEqual(t, [2])

    def test_skip_set_applies_everywhere(self):
        df = audit([(1, "DISPUTED", 100), (2, "REGRESSED", 100)])
        t = bv.select_targets(df, stale={3}, is_fresh=NEVER_FRESH, skip={1, 2, 3}, limit=10)
        self.assertEqual(t, [])

    def test_no_duplicates(self):
        df = audit([(1, "DISPUTED", 100)])
        t = bv.select_targets(df, stale={1}, is_fresh=NEVER_FRESH, skip=set(), limit=10)
        self.assertEqual(t, [1])


class TestNoProbes(unittest.TestCase):
    TODAY = date(2026, 10, 14)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "no_probes.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_missing_file_is_empty(self):
        self.assertEqual(bv.load_no_probes(self.path, self.TODAY), set())

    def test_record_then_load(self):
        bv.record_no_probes(self.path, 64500, self.TODAY)
        self.assertEqual(bv.load_no_probes(self.path, self.TODAY), {64500})

    def test_entries_expire_after_ttl(self):
        with open(self.path, "w") as fh:
            json.dump({"1": "2026-10-08", "2": "2026-10-07"}, fh)  # 6 and 7 days old
        self.assertEqual(bv.load_no_probes(self.path, self.TODAY), {1})

    def test_record_keeps_other_entries(self):
        bv.record_no_probes(self.path, 1, self.TODAY)
        bv.record_no_probes(self.path, 2, self.TODAY)
        self.assertEqual(bv.load_no_probes(self.path, self.TODAY), {1, 2})

    def test_corrupt_file_is_empty(self):
        with open(self.path, "w") as fh:
            fh.write('{"1": ')
        self.assertEqual(bv.load_no_probes(self.path, self.TODAY), set())
        bv.record_no_probes(self.path, 5, self.TODAY)  # recovers instead of crashing
        self.assertEqual(bv.load_no_probes(self.path, self.TODAY), {5})


if __name__ == "__main__":
    unittest.main()
