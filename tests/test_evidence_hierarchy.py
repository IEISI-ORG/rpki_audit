"""
tests/test_evidence_hierarchy.py

One ladder decides whether a network filters RPKI-invalid routes (2026-10-15):
our policy (HARDCODED_SECURE) > Atlas (<= 7 days) > APNIC (>= 95 / < 30) > declared (bgp.tools
tag, isbgpsafeyet) > unknown. rov_utils.filtering_status() returns (status, decided_by);
evidence_overrides() applies REGRESSED and INCONSISTENT from it. No network access.
"""
import unittest

import rov_utils

A = 64500
CF = 13335


def status(asn=A, *, atlas_secure=(), atlas_vulnerable=(), evidence="NONE", volatile=False,
           regression=False, rov_set=(), cf_set=()):
    return rov_utils.filtering_status(
        asn, atlas_secure=set(atlas_secure), atlas_vulnerable=set(atlas_vulnerable),
        evidence=evidence, volatile=volatile, regression=regression,
        rov_set=set(rov_set), cf_set=set(cf_set))


class TestFilteringStatus(unittest.TestCase):
    def test_policy_beats_atlas(self):
        # Cloudflare originates the Atlas invalid beacon, so Atlas can't test it
        self.assertIn(CF, rov_utils.HARDCODED_SECURE)
        self.assertEqual(status(CF, atlas_vulnerable={CF}, evidence="NOT_FILTERING"),
                         ("FILTERING", "policy"))

    def test_atlas_beats_apnic_both_ways(self):
        self.assertEqual(status(atlas_vulnerable={A}, evidence="FILTERING"), ("NOT_FILTERING", "atlas"))
        self.assertEqual(status(atlas_secure={A}, evidence="NOT_FILTERING"), ("FILTERING", "atlas"))

    def test_atlas_vulnerable_beats_tag_and_mid_apnic(self):
        # the old strong_current_rov guard (tag + APNIC >= 60) no longer overrides Atlas
        self.assertEqual(status(atlas_vulnerable={A}, evidence="NONE", rov_set={A}),
                         ("NOT_FILTERING", "atlas"))

    def test_apnic_beats_declaration(self):
        # China Telecom AS4134 shape: tagged, APNIC 0.24%
        self.assertEqual(status(evidence="NOT_FILTERING", rov_set={A}), ("NOT_FILTERING", "apnic"))
        self.assertEqual(status(evidence="FILTERING"), ("FILTERING", "apnic"))

    def test_noisy_apnic_falls_through(self):
        self.assertEqual(status(evidence="FILTERING", volatile=True, rov_set={A}), ("FILTERING", "declared"))
        self.assertEqual(status(evidence="FILTERING", volatile=True), ("UNKNOWN", "none"))

    def test_regression_is_evidence_not_noise(self):
        # is_volatile includes regression; a tagged regressed network must not fall to "declared"
        self.assertEqual(status(evidence="NOT_FILTERING", volatile=True, regression=True, rov_set={A}),
                         ("NOT_FILTERING", "apnic"))

    def test_declarations(self):
        self.assertEqual(status(rov_set={A}), ("FILTERING", "declared"))
        self.assertEqual(status(cf_set={A}), ("FILTERING", "declared"))

    def test_no_data_or_mid_range_is_unknown(self):
        self.assertEqual(status(evidence="NONE"), ("UNKNOWN", "none"))


class TestEvidenceOverrides(unittest.TestCase):
    def override(self, verdict, st, by, tagged=False, regression=False):
        return rov_utils.evidence_overrides(verdict, status=st, decided_by=by, tagged=tagged,
                                            regression=regression)

    def test_regressed_when_not_filtering_now(self):
        self.assertEqual(self.override("STUB: VULNERABLE", "NOT_FILTERING", "apnic", regression=True), "REGRESSED")
        self.assertEqual(self.override("STUB: VULNERABLE", "UNKNOWN", "none", regression=True), "REGRESSED")

    def test_no_regressed_while_filtering(self):
        self.assertEqual(self.override("ACTIVE LOCAL ROV", "FILTERING", "atlas", regression=True),
                         "ACTIVE LOCAL ROV")

    def test_inconsistent_when_measurement_contradicts_tag(self):
        self.assertEqual(self.override("PARTIAL: VULNERABLE (Mixed)", "NOT_FILTERING", "apnic", tagged=True),
                         "INCONSISTENT")
        self.assertEqual(self.override("VULNERABLE (Atlas Verified)", "NOT_FILTERING", "atlas", tagged=True),
                         "INCONSISTENT")
        # applied after REGRESSED, as before
        self.assertEqual(self.override("STUB: VULNERABLE", "NOT_FILTERING", "apnic", tagged=True,
                                       regression=True), "INCONSISTENT")

    def test_untagged_not_filtering_keeps_verdict(self):
        self.assertEqual(self.override("STUB: VULNERABLE", "NOT_FILTERING", "apnic"), "STUB: VULNERABLE")


if __name__ == "__main__":
    unittest.main()
