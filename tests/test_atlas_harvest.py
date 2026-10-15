"""
tests/test_atlas_harvest.py

Selection logic of atlas_harvest.py: which third-party Atlas measurements to
download. No network access.
"""
import unittest

import atlas_harvest as ah


def msm(i, desc, status="Stopped"):
    return {"id": i, "description": desc, "status": {"name": status}}


class TestIsOurs(unittest.TestCase):
    def test_own_measurements(self):
        for d in ("RPKI Invalid Trace v4 - AS8657", "RPKI Valid Ping v6 - AS1",
                  "rpki_audit NZ beacon baseline ping cf_invalid v4",
                  "RIS beacon invalid ping (rpki_audit check)"):
            self.assertTrue(ah.is_ours(d), d)

    def test_third_party(self):
        for d in ("RIPE RPKI experiment ICMP beacon test - x", "HE Network Tools Site",
                  "Traceroute measurement to 103.21.244.19", "", None):
            self.assertFalse(ah.is_ours(d), d)


class TestPlan(unittest.TestCase):
    def test_skips_ours_and_downloaded_stopped(self):
        ms = [msm(1, "RPKI Invalid Ping v4 - AS1"), msm(2, "HE Network Tools Site"),
              msm(3, "Traceroute measurement to x"), msm(4, "ROV invalid traceroute", "Ongoing")]
        plan = ah.plan_downloads(ms, have={2, 4})
        self.assertEqual([(m["id"], window) for m, window in plan], [(3, False), (4, True)])

    def test_ongoing_always_refetched_with_window(self):
        plan = ah.plan_downloads([msm(9, "daily trace", "Ongoing")], have={9})
        self.assertEqual([(m["id"], w) for m, w in plan], [(9, True)])

    def test_failed_measurements_skipped(self):
        plan = ah.plan_downloads([msm(5, "x", "Failed"), msm(6, "y", "No suitable probes")], have=set())
        self.assertEqual(plan, [])


    def test_daily_limit_new_measurements_first(self):
        self.assertEqual(ah.MAX_PER_RUN, 500)
        ms = [msm(1, "a", "Ongoing")] + [msm(i, "b") for i in range(2, 8)]
        plan = ah.plan_downloads(ms, have=set(), limit=3)
        self.assertEqual([m["id"] for m, _ in plan], [2, 3, 4])

    def test_skipped_measurements_not_retried(self):
        plan = ah.plan_downloads([msm(1, "a"), msm(2, "b")], have=set(), skip={1})
        self.assertEqual([m["id"] for m, _ in plan], [2])


class TestReadCapped(unittest.TestCase):
    """2026-10-15: one-off measurement 185673939 (1 probe) returned ~4.3 GB, read whole into memory."""

    def test_under_cap(self):
        self.assertEqual(ah.read_capped([b"[1,", b"2]"], cap=10), b"[1,2]")

    def test_over_cap_raises(self):
        with self.assertRaises(ah.ResponseTooLarge):
            ah.read_capped(iter([b"x" * 6, b"y" * 6]), cap=10)

    def test_default_cap(self):
        self.assertEqual(ah.MAX_RESPONSE_BYTES, 100_000_000)


if __name__ == "__main__":
    unittest.main()
