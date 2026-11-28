"""
tests/test_forensic_classify.py

verify_forensic_path_v2 changes of 2026-11-28 (Terry's decisions):
- results are fetched when every scheduled probe has reported (or the measurement stopped, or
  330 s passed), not after a fixed 60 s, which stored slow invalid traces as empty paths;
- an empty invalid path is no data, not "SECURE (Target Filtered)";
- an invalid trace that stops inside the target is SECURE (Target Filtered) only when the next AS
  on the valid path is the beacon origin; otherwise INCONCLUSIVE (Target Boundary).
No network access.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from test_forensic_hops import forensic  # noqa: E402  (loads the engine with Atlas stubbed)

T, C, U, CF, RIS = 64500, 64501, 64502, 13335, 12654


def verdict(path_v, path_i, score_i=0.0, asn=T):
    return forensic._classify_probe(asn, 1, path_v, path_i, 100.0, score_i)


class TestStopRules(unittest.TestCase):
    def test_empty_invalid_path_is_no_data(self):
        for path_v in ([T, U, CF], [C, T, U, CF], [T, CF]):
            d = verdict(path_v, [])
            self.assertEqual(d["verdict"], "INCONCLUSIVE (No Invalid Path)", path_v)
            self.assertIsNone(d["boundary_asn"])

    def test_stop_in_target_before_origin_is_target_filtered(self):
        for origin in (CF, RIS):
            d = verdict([T, origin], [T])
            self.assertEqual(d["verdict"], "SECURE (Target Filtered)", origin)
            self.assertEqual((d["boundary_asn"], d["boundary_type"]), (T, "target"))
        self.assertEqual(verdict([C, T, CF], [C, T])["verdict"], "SECURE (Target Filtered)")

    def test_stop_in_target_before_another_as_is_inconclusive(self):
        d = verdict([T, U, CF], [T])
        self.assertEqual(d["verdict"], "INCONCLUSIVE (Target Boundary)")
        self.assertIsNone(d["boundary_asn"])
        self.assertEqual(verdict([C, T, U, CF], [C, T])["verdict"], "INCONCLUSIVE (Target Boundary)")

    def test_stop_in_target_after_a_fork_uses_the_same_rule(self):
        self.assertEqual(verdict([C, T, U, CF], [U, T])["verdict"], "INCONCLUSIVE (Target Boundary)")
        self.assertEqual(verdict([C, T, CF], [U, T])["verdict"], "SECURE (Target Filtered)")

    def test_trace_past_the_target_still_counts_against_it(self):
        d = verdict([T, U, CF], [T, U])
        self.assertEqual(d["verdict"], "SECURE (Upstream Filtered)")
        self.assertEqual(d["boundary_asn"], CF)

    def test_unchanged_outcomes(self):
        self.assertEqual(verdict([T, U, CF], [T, U, CF], score_i=100.0)["verdict"], "VULNERABLE")
        self.assertEqual(verdict([C, T, U, CF], [C])["verdict"], "SECURE (Target Filtered)")
        self.assertEqual(verdict([C, U, T, CF], [C], asn=T)["verdict"], "SECURE (Pre-Target Filtered)")
        self.assertEqual(verdict([C, T, U, CF], [C, U, CF], score_i=100.0)["verdict"],
                         "VULNERABLE (Bypass Route)")
        self.assertEqual(verdict([C, T, U, CF], [C, U])["verdict"], "INCONCLUSIVE (Divergent)")


class FakeAtlas:
    """Measurement status and results that change with each poll."""

    def __init__(self, scheduled, arrivals, status=None):
        self.scheduled, self.arrivals, self.status = scheduled, arrivals, status or {}
        self.t = 0.0

    def clock(self):
        return self.t

    def sleep(self, s):
        self.t += s

    def fetch_status(self, m):
        return self.status.get(m, "Ongoing"), self.scheduled[m]

    def fetch_results(self, m):
        return [{"prb_id": p} for p, at in self.arrivals[m] if at <= self.t]


class TestWaitForResults(unittest.TestCase):
    def test_returns_once_every_probe_reported(self):
        a = FakeAtlas({1: 2, 2: 2}, {1: [(10, 20), (11, 25)], 2: [(10, 40), (11, 70)]})
        out = forensic.wait_for_results([1, 2], a.fetch_status, a.fetch_results,
                                        clock=a.clock, sleep=a.sleep)
        self.assertEqual({k: len(v) for k, v in out.items()}, {1: 2, 2: 2})
        self.assertLess(a.t, 100)              # well before the 330 s limit

    def test_slow_trace_is_waited_for(self):
        # The 2026-11-26 case: the invalid trace took 73 s, past the old fixed 60 s wait.
        a = FakeAtlas({1: 1}, {1: [(10312, 73)]})
        out = forensic.wait_for_results([1], a.fetch_status, a.fetch_results, clock=a.clock, sleep=a.sleep)
        self.assertEqual(out[1], [{"prb_id": 10312}])

    def test_stopped_measurement_ends_the_wait(self):
        a = FakeAtlas({1: 3}, {1: [(10, 5)]}, status={1: "Stopped"})
        out = forensic.wait_for_results([1], a.fetch_status, a.fetch_results, clock=a.clock, sleep=a.sleep)
        self.assertEqual(len(out[1]), 1)
        self.assertLessEqual(a.t, 30)

    def test_gives_up_at_the_limit_with_what_arrived(self):
        a = FakeAtlas({1: 2}, {1: [(10, 5), (11, 10_000)]})
        out = forensic.wait_for_results([1], a.fetch_status, a.fetch_results, max_wait=330,
                                        clock=a.clock, sleep=a.sleep)
        self.assertEqual(out[1], [{"prb_id": 10}])
        self.assertGreaterEqual(a.t, 330)
        self.assertLess(a.t, 330 + forensic.ATLAS_POLL_SECS + 1)

    def test_status_error_keeps_polling(self):
        a = FakeAtlas({1: 0}, {1: [(10, 5)]})       # (None, 0) from a failed status call
        a.fetch_status = lambda m: (None, 0)
        out = forensic.wait_for_results([1], a.fetch_status, a.fetch_results, max_wait=60,
                                        clock=a.clock, sleep=a.sleep)
        self.assertEqual(len(out[1]), 1)
        self.assertGreaterEqual(a.t, 60)


if __name__ == "__main__":
    unittest.main()
