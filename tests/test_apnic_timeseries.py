"""
tests/test_apnic_timeseries.py

APNIC timeseries cache formats and the APNIC_EXCLUDED_WINDOWS mask.

The APNIC Labs test window (5-18 Aug 2026) lifted readings for non-filtering
NZ and AU networks. Without the mask, a network at 0% now and ~100% during
the window is flagged REGRESSED until Aug 2027. No network access is used.
"""
import unittest
from datetime import date, timedelta

import rov_utils


def _series(start: str, rates: list[float], n: int = 500, window: int = 7) -> list:
    """Dated cache rows [date, rate, samples, window] for consecutive days."""
    d0 = date.fromisoformat(start)
    return [[(d0 + timedelta(days=i)).isoformat(), r, n, window] for i, r in enumerate(rates)]


def _test_window_series(window: int = 7) -> list:
    """0% all year except ~100% for days whose window overlaps 5-18 Aug 2026."""
    rows = _series("2025-10-10", [0.0] * 365, window=window)
    for row in rows:
        if rov_utils._ts_point_excluded(row[0], row[3], "NZ"):
            row[1] = 99.0
    return rows


class TestPointExclusion(unittest.TestCase):
    def test_inside_window(self):
        self.assertTrue(rov_utils._ts_point_excluded("2026-08-10", 7, "NZ"))

    def test_rolling_window_overlap_after_end(self):
        # 7-day reading on 24 Aug covers 18-24 Aug: overlaps the last day.
        self.assertTrue(rov_utils._ts_point_excluded("2026-08-24", 7, "NZ"))
        self.assertFalse(rov_utils._ts_point_excluded("2026-08-25", 7, "NZ"))

    def test_long_window_reaches_further(self):
        self.assertTrue(rov_utils._ts_point_excluded("2026-09-30", 112, "AU"))

    def test_before_window(self):
        self.assertFalse(rov_utils._ts_point_excluded("2026-08-04", 7, "NZ"))

    def test_other_country_unaffected(self):
        self.assertFalse(rov_utils._ts_point_excluded("2026-08-10", 7, "US"))


class TestTsStats(unittest.TestCase):
    def test_test_window_spike_is_not_regression_for_nz(self):
        stats = rov_utils._ts_stats(_test_window_series(), "NZ")
        self.assertIsNotNone(stats)
        sd, mn, mx, volatile, regression = stats
        self.assertFalse(regression)
        self.assertFalse(volatile)
        self.assertEqual(mx, 0.0)

    def test_same_spike_still_regression_outside_nz_au(self):
        stats = rov_utils._ts_stats(_test_window_series(), "US")
        self.assertTrue(stats[4])

    def test_genuine_regression_still_detected_for_nz(self):
        # Filtering at 99% until June 2026, 0% since: a real rollback.
        rows = _series("2025-10-10", [99.0] * 240 + [0.0] * 125)
        self.assertTrue(rov_utils._ts_stats(rows, "NZ")[4])

    def test_genuine_deployment_is_volatile_not_regression(self):
        # 0% until 19 Aug 2026, ~99% after: crosses 95/60 inside 90 days.
        rows = _series("2025-10-10", [0.0] * 313 + [99.0] * 52)
        sd, mn, mx, volatile, regression = rov_utils._ts_stats(rows, "NZ")
        self.assertFalse(regression)
        self.assertTrue(volatile)

    def test_current_needs_reliable_samples(self):
        rows = _series("2025-10-10", [99.0] * 335 + [0.0] * 30, n=50)
        self.assertFalse(rov_utils._ts_stats(rows, "NZ")[4])

    def test_masked_point_is_never_current(self):
        # 112-day readings: every point to early Dec overlaps the test window.
        # Spike to 99% inside the overlap must not become 'current' for NZ.
        rows = _series("2025-12-01", [99.0] * 250, window=7)
        rows += _series("2026-08-08", [0.0] * 60, window=112)
        self.assertFalse(rov_utils._ts_stats(rows, "NZ")[4])

    def test_too_sparse_returns_none(self):
        self.assertIsNone(rov_utils._ts_stats(_series("2026-10-01", [50.0] * 10), "NZ"))


class TestLegacyFormats(unittest.TestCase):
    def test_undated_pairs_still_analysed(self):
        raw = [[99.0, 500]] * 300 + [[0.0, 500]] * 65
        self.assertTrue(rov_utils._ts_stats(raw, "US")[4])

    def test_plain_floats_still_analysed(self):
        raw = [50.0, 52.0] * 20
        self.assertIsNotNone(rov_utils._ts_stats(raw, "US"))

    def test_cache_format_detection(self):
        self.assertTrue(rov_utils._ts_cache_is_dated([["2026-10-01", 1.0, 40, 7]]))
        self.assertFalse(rov_utils._ts_cache_is_dated([[1.0, 40]]))
        self.assertFalse(rov_utils._ts_cache_is_dated([1.0]))
        self.assertFalse(rov_utils._ts_cache_is_dated([]))


class TestNzTimeline(unittest.TestCase):
    """State-change detection used by analyze_nz_project_report.py."""

    @staticmethod
    def _recent(rates: list[float]) -> list:
        start = (date.today() - timedelta(days=len(rates))).isoformat()
        return _series(start, rates)

    def test_single_deployment_is_one_change(self):
        import analyze_nz_project_report as nz
        rows = self._recent([0.0] * 100 + [99.0] * 100)
        changes = nz.timeline(rows, "US")
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0][0], rows[100][0])
        self.assertEqual(changes[0][1:], ("NOT FILTERING", "FILTERING"))

    def test_one_day_dip_is_ignored(self):
        import analyze_nz_project_report as nz
        rows = self._recent([99.0] * 50 + [0.0] + [99.0] * 50)
        self.assertEqual(nz.timeline(rows, "US"), [])

    def test_low_sample_points_are_ignored(self):
        import analyze_nz_project_report as nz
        rows = self._recent([0.0] * 50 + [99.0] * 50)
        for r in rows[50:]:
            r[2] = 40  # below APNIC_REGRESSION_CURRENT_MIN_SAMPLES
        self.assertEqual(nz.timeline(rows, "US"), [])


if __name__ == "__main__":
    unittest.main()
