"""
tests/test_fetch_fallback.py

Guards against the 2026-10-11 failure: bgp.tools timed out, fetch_csv() returned
an empty DataFrame, and the engine wrote an audit with ~30% of ASNs missing,
every name 'Unknown' and 0 ROV tags. No network access is used.
"""
import os
import tempfile
import unittest
from unittest import mock

import requests

import rov_no_scrape_v22
import rov_utils

CSV_TEXT = "asn,name\nAS1,One\nAS2,Two\n"


def _ok_response(text: str) -> mock.Mock:
    resp = mock.Mock()
    resp.text = text
    resp.content = text.encode()
    resp.raise_for_status = mock.Mock()
    return resp


class TestFetchCsvFallback(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.primary = os.path.join(self.tmp.name, "cache", "asns.csv")
        self.secondary = os.path.join(self.tmp.name, "old_asns.csv")

    def tearDown(self):
        self.tmp.cleanup()

    def test_success_writes_primary_cache(self):
        with mock.patch.object(rov_utils.requests, "get", return_value=_ok_response(CSV_TEXT)):
            df = rov_utils.fetch_csv("http://x", "t", cache_paths=(self.primary,))
        self.assertEqual(len(df), 2)
        with open(self.primary) as fh:
            self.assertEqual(fh.read(), CSV_TEXT)

    def test_failure_uses_primary_cache(self):
        os.makedirs(os.path.dirname(self.primary))
        with open(self.primary, "w") as fh:
            fh.write(CSV_TEXT)
        with mock.patch.object(rov_utils.requests, "get",
                               side_effect=requests.ConnectTimeout("down")):
            df = rov_utils.fetch_csv("http://x", "t", cache_paths=(self.primary, self.secondary))
        self.assertEqual(list(df["name"]), ["One", "Two"])

    def test_failure_falls_through_to_secondary(self):
        with open(self.secondary, "w") as fh:
            fh.write(CSV_TEXT)
        with mock.patch.object(rov_utils.requests, "get",
                               side_effect=requests.ConnectTimeout("down")):
            df = rov_utils.fetch_csv("http://x", "t", cache_paths=(self.primary, self.secondary))
        self.assertEqual(len(df), 2)
        self.assertFalse(os.path.exists(self.primary))  # failure must not write a cache

    def test_failure_without_cache_is_empty(self):
        with mock.patch.object(rov_utils.requests, "get",
                               side_effect=requests.ConnectTimeout("down")):
            df = rov_utils.fetch_csv("http://x", "t", cache_paths=(self.primary,))
        self.assertTrue(df.empty)


class TestDegradedAuditGuard(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.audit = os.path.join(self.tmp.name, "audit.csv")
        with open(self.audit, "w") as fh:
            fh.write("asn\n" + "".join(f"{i}\n" for i in range(1000)))
        patcher = mock.patch.object(rov_utils, "FILE_AUDIT_FINAL", self.audit)
        patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        self.tmp.cleanup()

    def test_healthy_inputs_pass(self):
        self.assertEqual(rov_no_scrape_v22.degraded_input_reasons(990, 4000), [])

    def test_zero_rov_tags_blocks(self):
        reasons = rov_no_scrape_v22.degraded_input_reasons(1000, 0)
        self.assertEqual(len(reasons), 1)
        self.assertIn("ROV tags", reasons[0])

    def test_row_drop_blocks(self):
        # 2026-10-11 shape: 88,254 vs 123,155 rows = 72%
        reasons = rov_no_scrape_v22.degraded_input_reasons(717, 4000)
        self.assertEqual(len(reasons), 1)
        self.assertIn("717", reasons[0])

    def test_exactly_ninety_percent_passes(self):
        self.assertEqual(rov_no_scrape_v22.degraded_input_reasons(900, 4000), [])

    def test_no_previous_audit_skips_row_check(self):
        os.remove(self.audit)
        self.assertEqual(rov_no_scrape_v22.degraded_input_reasons(5, 4000), [])


if __name__ == "__main__":
    unittest.main()
