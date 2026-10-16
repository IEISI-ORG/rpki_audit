"""
tests/test_snapshot_verdicts.py

The daily verdict snapshot counts classes, rungs and IPv6 classes from the audit
CSV, and keeps one row per run date (a rerun replaces that day's row).
"""
import csv
import os
import tempfile
import unittest
from datetime import date

import snapshot_verdicts as sv

AUDIT_ROWS = [
    {"asn": "1", "verdict": "ACTIVE LOCAL ROV", "decided_by": "apnic",
     "v6_verdict": "ACTIVE LOCAL ROV", "rovista_score": "100.0"},
    {"asn": "2", "verdict": "STUB: VULNERABLE", "decided_by": "none",
     "v6_verdict": "", "rovista_score": "-1"},
    {"asn": "3", "verdict": "REGRESSED", "decided_by": "atlas",
     "v6_verdict": "STUB: VULNERABLE", "rovista_score": "-1.0"},
    {"asn": "4", "verdict": "NOT ROUTED", "decided_by": "none",
     "v6_verdict": "", "rovista_score": ""},
]


class TestCountVerdicts(unittest.TestCase):
    def test_counts(self):
        c = sv.count_verdicts(AUDIT_ROWS)
        self.assertEqual(c["rows"], 4)
        self.assertEqual((c["SECURE"], c["VULNERABLE"], c["UNKNOWN"]), (1, 2, 1))
        self.assertEqual(c["REGRESSED"], 1)
        self.assertEqual((c["decided_none"], c["decided_apnic"], c["decided_atlas"]), (2, 1, 1))
        self.assertEqual((c["v6_rows"], c["v6_SECURE"], c["v6_VULNERABLE"]), (2, 1, 1))
        self.assertEqual(c["rovista_fresh"], 1)

    def test_every_field_is_filled(self):
        c = sv.count_verdicts(AUDIT_ROWS)
        missing = set(sv.FIELDS) - set(c) - {"run_date", "audit_mtime", "graph_mtime", "git_head"}
        self.assertEqual(missing, set())


class TestWriteSnapshot(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.audit = os.path.join(self.tmp.name, "audit.csv")
        self.out = os.path.join(self.tmp.name, "logs", "verdict_counts.csv")
        with open(self.audit, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(AUDIT_ROWS[0]))
            w.writeheader()
            w.writerows(AUDIT_ROWS)

    def tearDown(self):
        self.tmp.cleanup()

    def read(self):
        with open(self.out, newline="") as fh:
            return list(csv.DictReader(fh))

    def test_one_row_per_day_and_rerun_replaces(self):
        sv.main(self.audit, self.out, today=date(2026, 10, 17))
        sv.main(self.audit, self.out, today=date(2026, 10, 16))
        sv.main(self.audit, self.out, today=date(2026, 10, 17))
        rows = self.read()
        self.assertEqual([r["run_date"] for r in rows], ["2026-10-16", "2026-10-17"])
        self.assertEqual(rows[1]["SECURE"], "1")

    def test_missing_audit_writes_nothing(self):
        self.assertEqual(sv.main(os.path.join(self.tmp.name, "nope.csv"), self.out), 1)
        self.assertFalse(os.path.exists(self.out))


if __name__ == "__main__":
    unittest.main()
