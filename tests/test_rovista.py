"""
tests/test_rovista.py

ROVista is weighed the same as APNIC: both measure whether traffic from inside an
AS reaches RPKI-invalid prefixes, with the same thresholds. When one says
filtering and the other says not filtering, the AS is DISPUTED. No network access.
"""
import json
import os
import tempfile
import unittest
from datetime import date
from unittest import mock

import requests

import rov_utils

MISSING = -1.0


class TestMeasurementEvidence(unittest.TestCase):
    def ev(self, apnic, rovista):
        return rov_utils.measurement_evidence(apnic, rovista)

    def test_both_missing_is_none(self):
        self.assertEqual(self.ev(MISSING, MISSING), "NONE")

    def test_apnic_alone_keeps_current_thresholds(self):
        self.assertEqual(self.ev(95.0, MISSING), "FILTERING")
        self.assertEqual(self.ev(94.9, MISSING), "NONE")
        self.assertEqual(self.ev(29.9, MISSING), "NOT_FILTERING")
        self.assertEqual(self.ev(30.0, MISSING), "NONE")
        self.assertEqual(self.ev(0.0, MISSING), "NOT_FILTERING")

    def test_rovista_alone_counts_like_apnic(self):
        self.assertEqual(self.ev(MISSING, 100.0), "FILTERING")
        self.assertEqual(self.ev(MISSING, 0.0), "NOT_FILTERING")
        self.assertEqual(self.ev(MISSING, 50.0), "NONE")

    def test_agreement(self):
        self.assertEqual(self.ev(99.0, 100.0), "FILTERING")
        self.assertEqual(self.ev(1.0, 0.0), "NOT_FILTERING")

    def test_opposite_readings_are_disputed(self):
        self.assertEqual(self.ev(99.0, 0.0), "DISPUTED")
        self.assertEqual(self.ev(0.1, 100.0), "DISPUTED")

    def test_without_rovista_matches_old_apnic_rules(self):
        # Before ROVista: safe iff apnic >= 95; INCONSISTENT iff 0 <= apnic < 30.
        for apnic in (-1.0, -0.5, 0.0, 0.01, 29.99, 30.0, 59.99, 60.0, 94.99, 95.0, 100.0):
            ev = self.ev(apnic, MISSING)
            self.assertEqual(ev == "FILTERING", apnic >= 95.0, apnic)
            self.assertEqual(ev == "NOT_FILTERING", 0 <= apnic < 30.0, apnic)
            self.assertNotEqual(ev, "DISPUTED", apnic)

    def test_mid_range_does_not_contradict(self):
        self.assertEqual(self.ev(99.0, 50.0), "FILTERING")
        self.assertEqual(self.ev(50.0, 0.0), "NOT_FILTERING")
        self.assertEqual(self.ev(50.0, 50.0), "NONE")


class TestDisputedVerdict(unittest.TestCase):
    STUB_VERDICT = "STUB: ACTIVE LOCAL ROV"

    def test_disputed_replaces_topology_verdict(self):
        v = rov_utils.apply_dispute(self.STUB_VERDICT, "DISPUTED", 64500, "")
        self.assertEqual(v, "DISPUTED")

    def test_no_dispute_keeps_verdict(self):
        v = rov_utils.apply_dispute(self.STUB_VERDICT, "FILTERING", 64500, "")
        self.assertEqual(v, self.STUB_VERDICT)

    def test_tier1_keeps_core_label(self):
        for core in ("CORE: ACTIVE PROTECTOR", "CORE: UNPROTECTED"):
            self.assertEqual(rov_utils.apply_dispute(core, "DISPUTED", 3356, ""), core)

    def test_atlas_result_breaks_the_tie(self):
        for atlas in ("VULNERABLE (Verified Active)", "SECURE (Target Filtered)"):
            v = rov_utils.apply_dispute("ACTIVE (Atlas Verified)", "DISPUTED", 64500, atlas)
            self.assertEqual(v, "ACTIVE (Atlas Verified)")

    def test_inconclusive_atlas_does_not_break_the_tie(self):
        v = rov_utils.apply_dispute(self.STUB_VERDICT, "DISPUTED", 64500, "INCONCLUSIVE (Off-Path)")
        self.assertEqual(v, "DISPUTED")

    def test_hardcoded_secure_is_kept(self):
        asn = next(iter(rov_utils.HARDCODED_SECURE))
        v = rov_utils.apply_dispute("ACTIVE LOCAL ROV (Hardcoded)", "DISPUTED", asn, "")
        self.assertEqual(v, "ACTIVE LOCAL ROV (Hardcoded)")

    def test_disputed_counts_as_partial(self):
        self.assertEqual(rov_utils.classify_verdict("DISPUTED"), "PARTIAL")


def _row(asn, ratio, updated):
    return {"asn": asn, "ratio": ratio, "lastUpdatedDate": updated}


class TestParseOverview(unittest.TestCase):
    TODAY = date(2026, 10, 13)

    def test_scales_ratio_to_percent(self):
        payload = {"data": [_row(1, 1.0, "2026-10-12"), _row(2, 0.5, "2026-10-12")]}
        self.assertEqual(rov_utils.parse_rovista_overview(payload, self.TODAY), {1: 100.0, 2: 50.0})

    def test_drops_rows_older_than_ttl(self):
        payload = {"data": [_row(1, 1.0, "2026-10-06"),   # 7 days old: kept
                            _row(2, 1.0, "2026-10-05"),   # 8 days old: dropped
                            _row(3, 0.0, "2025-03-03")]}  # long-stale leftover
        self.assertEqual(rov_utils.parse_rovista_overview(payload, self.TODAY), {1: 100.0})

    def test_skips_malformed_rows(self):
        payload = {"data": [_row(1, 1.0, "2026-10-12"),
                            _row("AS2", 1.0, "2026-10-12"),
                            _row(3, "n/a", "2026-10-12"),
                            _row(4, 0.0, None),
                            {"asn": 5},
                            "junk"]}
        self.assertEqual(rov_utils.parse_rovista_overview(payload, self.TODAY), {1: 100.0})

    def test_malformed_payload_is_empty(self):
        for payload in (None, [], [_row(1, 1.0, "2026-10-12")], {"data": "oops"}, {"data": {"1": 1}}):
            self.assertEqual(rov_utils.parse_rovista_overview(payload, self.TODAY), {}, payload)


class TestSyncRovista(unittest.TestCase):
    PAYLOAD = {"data": [_row(681, 1.0, "2026-10-12")]}

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.cache = os.path.join(self.tmp.name, "rovista", "overview.json")

    def tearDown(self):
        self.tmp.cleanup()

    def _resp(self, payload=None):
        payload = self.PAYLOAD if payload is None else payload
        resp = mock.Mock()
        resp.json.return_value = payload
        resp.raise_for_status = mock.Mock()
        return resp

    def _write_old_cache(self):
        os.makedirs(os.path.dirname(self.cache), exist_ok=True)
        with open(self.cache, "w") as fh:
            json.dump(self.PAYLOAD, fh)
        os.utime(self.cache, (0, 0))  # old, so a refresh is attempted

    def test_fresh_cache_skips_network(self):
        os.makedirs(os.path.dirname(self.cache))
        with open(self.cache, "w") as fh:
            json.dump(self.PAYLOAD, fh)
        with mock.patch.object(rov_utils.requests, "get") as get:
            scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13))
        get.assert_not_called()
        self.assertEqual(scores, {681: 100.0})

    def test_unusable_response_keeps_good_cache(self):
        # Empty, wrong shape, or no valid fresh rows: fall back, don't overwrite.
        for bad in ({"data": []}, {"data": "oops"}, [], {"data": [_row("AS1", 1.0, "2026-10-12")]}):
            self._write_old_cache()
            with mock.patch.object(rov_utils.requests, "get", return_value=self._resp(bad)):
                scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13))
            self.assertEqual(scores, {681: 100.0}, bad)
            with open(self.cache) as fh:
                self.assertEqual(json.load(fh), self.PAYLOAD, bad)

    def test_corrupt_cache_returns_empty(self):
        os.makedirs(os.path.dirname(self.cache))
        with open(self.cache, "w") as fh:
            fh.write('{"data": [')  # truncated write
        with mock.patch.object(rov_utils.requests, "get",
                               side_effect=requests.ConnectTimeout("down")):
            scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13),
                                            force=True)
        self.assertEqual(scores, {})

    def test_cache_write_failure_still_returns_scores(self):
        with mock.patch.object(rov_utils.requests, "get", return_value=self._resp()), \
                mock.patch.object(rov_utils.json, "dump", side_effect=OSError("disk full")):
            scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13))
        self.assertEqual(scores, {681: 100.0})
        self.assertFalse(os.path.exists(self.cache))

    def test_download_is_cached(self):
        with mock.patch.object(rov_utils.requests, "get", return_value=self._resp()):
            scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13))
        self.assertEqual(scores, {681: 100.0})
        self.assertTrue(os.path.exists(self.cache))

    def test_failure_falls_back_to_cache(self):
        os.makedirs(os.path.dirname(self.cache))
        with open(self.cache, "w") as fh:
            json.dump(self.PAYLOAD, fh)
        os.utime(self.cache, (0, 0))  # cache is old, so a refresh is attempted
        with mock.patch.object(rov_utils.requests, "get",
                               side_effect=requests.ConnectTimeout("down")):
            scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13))
        self.assertEqual(scores, {681: 100.0})

    def test_failure_without_cache_returns_empty(self):
        with mock.patch.object(rov_utils.requests, "get",
                               side_effect=requests.ConnectTimeout("down")):
            scores = rov_utils.sync_rovista(cache_path=self.cache, today=date(2026, 10, 13))
        self.assertEqual(scores, {})


if __name__ == "__main__":
    unittest.main()
