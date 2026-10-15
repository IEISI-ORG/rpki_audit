"""
tests/test_audit_verdict.py

rov_utils.audit_verdict: the audit's verdict pipeline (assign_verdict, STUB: FORTUITOUS ROV,
dispute, evidence overrides) for one provider set, so the IPv4 and IPv6 verdicts are made the
same way (2026-10-16).
"""
import unittest

import rov_utils

HE, DIRTY, STUB = 6939, 64510, 64520


def verdict(parents, *, asn=STUB, safe=frozenset({HE}), cone=0, status=("NOT_FILTERING", "none"), **kw):
    args = dict(volatile=False, atlas_v="", in_bgp=True, evidence="none", regression=False,
                rov_set=set(), cf_set=set(), atlas_secure=set())
    args.update(kw)
    return rov_utils.audit_verdict(asn, parents, safe_asns=set(safe), cone=cone, status=status[0],
                                   decided_by=status[1], **args)


class TestAuditVerdict(unittest.TestCase):
    def test_filtering_provider_credited(self):
        # The HE case: IPv4 providers include a non-filtering one, IPv6 provider is HE alone
        self.assertEqual(verdict([DIRTY, HE]), ("STUB: VULNERABLE", 1))
        self.assertEqual(verdict([HE]), ("STUB: PASSIVE (Clean Pipe)", 0))

    def test_fortuitous_applied(self):
        v, _ = verdict([HE], safe={HE, STUB}, status=("FILTERING", "apnic"))
        self.assertEqual(v, "STUB: FORTUITOUS ROV")
        v, _ = verdict([HE], safe={HE, STUB}, status=("FILTERING", "declared"), rov_set={STUB})
        self.assertEqual(v, "STUB: ACTIVE LOCAL ROV")

    def test_evidence_overrides_applied(self):
        v, _ = verdict([HE], regression=True, status=("NOT_FILTERING", "apnic"))
        self.assertEqual(v, "REGRESSED")

    def test_no_providers(self):
        self.assertEqual(verdict([]), ("PROVIDER UNKNOWN (In BGP)", 0))


if __name__ == "__main__":
    unittest.main()
