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


if __name__ == "__main__":
    unittest.main()
