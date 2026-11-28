"""
tests/test_roa_signing_trends.py

A failed APNIC ROA snapshot ({} or {'date': None}, as on 2026-11-26 for three lookback dates)
must print "no data" / "n/a" rows, not crash or read as 0.0%. No network access.
"""
import contextlib
import io
import os
import tempfile
import unittest
from unittest import mock

import pandas as pd

import analyze_roa_signing_trends as rt

GOOD = {"date": "28/08/2026", "NZ": {"valid": 80, "total": 100}, "AU": {"valid": 30, "total": 100}}
RIRS = {"NZ": "APNIC", "AU": "APNIC"}


class TestMissingSnapshot(unittest.TestCase):
    def test_has_data(self):
        self.assertTrue(rt.has_data(GOOD))
        self.assertFalse(rt.has_data({}))
        self.assertFalse(rt.has_data({"date": None}))

    def test_reported_date(self):
        self.assertEqual(rt.reported_date(GOOD), "28/08/2026")
        self.assertEqual(rt.reported_date({"date": None}), "no data")
        self.assertEqual(rt.reported_date({}), "no data")
        self.assertEqual(rt.reported_date({"date": None, "NZ": GOOD["NZ"]}), "unknown date")

    def test_world_line_with_data(self):
        line = rt.world_line("3mo", GOOD, rt.rir_rollup(GOOD, RIRS))
        self.assertIn("28/08/2026", line)
        self.assertIn("55.0%", line)
        self.assertIn("200", line)

    def test_world_line_without_data(self):
        for snap in ({}, {"date": None}):
            line = rt.world_line("3mo", snap, rt.rir_rollup(snap, RIRS))
            self.assertIn("no data", line)
            self.assertIn("n/a", line)
            self.assertNotIn("0.0%", line)

    def test_rir_cell(self):
        self.assertEqual(rt.rir_cell(rt.rir_rollup(GOOD, RIRS), "APNIC").strip(), "55.0%")
        self.assertEqual(rt.rir_cell(rt.rir_rollup({"date": None}, RIRS), "APNIC").strip(), "n/a")


class TestEmptyNowSnapshot(unittest.TestCase):
    """No current snapshot: stop before the per-country section and keep the existing CSV."""

    def test_csv_left_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = os.path.join(tmp, "roa_signing_trends.csv")
            with open(csv_path, "w") as fh:
                fh.write("cc,valid_pct_now\nNZ,80\n")
            audit = pd.DataFrame({"asn": [1, 2], "cc": ["NZ", "AU"]})
            fetch = lambda d=None: {} if d is None else GOOD  # noqa: E731
            cwd = os.getcwd()
            try:
                with mock.patch.object(rt.os.path, "exists", return_value=True), \
                        mock.patch.object(rt.rov_utils, "load_cc_to_rir", return_value=RIRS), \
                        mock.patch.object(rt.rov_utils, "load_audit_csv", return_value=audit), \
                        mock.patch.object(rt.rov_utils, "fetch_apnic_roa_by_country", side_effect=fetch), \
                        contextlib.redirect_stdout(io.StringIO()) as out:
                    os.chdir(tmp)
                    rt.analyze()
            finally:
                os.chdir(cwd)
            with open(csv_path) as fh:
                self.assertEqual(fh.read(), "cc,valid_pct_now\nNZ,80\n")
            self.assertIn("left unchanged", out.getvalue())


if __name__ == "__main__":
    unittest.main()
