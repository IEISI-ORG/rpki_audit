"""
tests/test_forensic_hops.py

Which traceroute hops verify_forensic_path_v2.resolve_asns sends to RIPEstat. Until
2026-11-28 every hop starting "172." was dropped as private, which removed Cloudflare's
public edge hops (172.68.x.x, AS13335) from Atlas paths. No network access.
"""
import importlib
import os
import sys
import types
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def load_forensic():
    """The real forensic engine. CI doesn't install ripe.atlas.cousteau, and
    test_batch_targets.py leaves an empty stand-in module behind in the same process."""
    try:
        importlib.import_module("ripe.atlas.cousteau")
    except ImportError:
        stub = types.ModuleType("ripe.atlas.cousteau")
        for name in ("ProbeRequest", "AtlasSource", "Ping", "Traceroute", "AtlasCreateRequest",
                     "AtlasResultsRequest"):
            setattr(stub, name, object)
        sys.modules.setdefault("ripe", types.ModuleType("ripe"))
        sys.modules.setdefault("ripe.atlas", types.ModuleType("ripe.atlas"))
        sys.modules["ripe.atlas.cousteau"] = stub
    if not hasattr(sys.modules.get("verify_forensic_path_v2"), "_classify_probe"):
        sys.modules.pop("verify_forensic_path_v2", None)
    return importlib.import_module("verify_forensic_path_v2")


forensic = load_forensic()


class TestPublicIps(unittest.TestCase):
    def test_cloudflare_172_hops_are_public(self):
        self.assertEqual(sorted(forensic.public_ips(["172.68.84.6", "172.71.0.1"])),
                         ["172.68.84.6", "172.71.0.1"])

    def test_rfc1918_172_block_is_private(self):
        self.assertEqual(forensic.public_ips(["172.16.0.1", "172.22.0.1", "172.31.255.254"]), [])

    def test_other_private_and_special_ranges_dropped(self):
        hops = ["10.101.7.217", "192.168.0.1", "100.64.0.1", "169.254.1.1", "127.0.0.1", "fd00::1", "fe80::1"]
        self.assertEqual(forensic.public_ips(hops), [])

    def test_public_v4_v6_kept_once(self):
        hops = ["60.234.8.50", "60.234.8.50", "2400:cb00:46:3::", None, "", "*", "not-an-ip"]
        self.assertEqual(sorted(forensic.public_ips(hops)), ["2400:cb00:46:3::", "60.234.8.50"])


class TestResolveAsns(unittest.TestCase):
    def test_only_public_hops_are_looked_up(self):
        asked = []

        def fake_get(url, timeout=None):
            asked.append(url.rsplit("=", 1)[1])
            return mock.Mock(status_code=200, json=lambda: {"data": {"asns": ["13335"]}})

        with mock.patch.object(forensic.requests, "get", fake_get), \
                mock.patch.object(forensic.time, "sleep", lambda s: None):
            mapping = forensic.resolve_asns(["172.22.0.1", "172.68.84.6", "192.168.1.1", "10.0.0.1"])
        self.assertEqual(asked, ["172.68.84.6"])
        self.assertEqual(mapping, {"172.68.84.6": 13335})

    def test_path_keeps_cloudflare_edge(self):
        path = forensic.ips_to_as_path(["192.168.0.1", "124.157.121.2", "172.68.84.6", "104.17.231.6"],
                                       {"124.157.121.2": 24324, "172.68.84.6": 13335, "104.17.231.6": 13335})
        self.assertEqual(path, [24324, 13335])


if __name__ == "__main__":
    unittest.main()
