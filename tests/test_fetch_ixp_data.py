"""
tests/test_fetch_ixp_data.py

fetch_ixp_data.py: which IX-F export URLs to fetch, and that a failed PeeringDB download keeps the
previous file. No network access.
"""
import json
import os
import tempfile
import unittest

import fetch_ixp_data as f


class TestExportUrls(unittest.TestCase):
    def test_distinct_urls_with_their_exchanges(self):
        lans = [{"ix_id": 1, "ixf_ixp_member_list_url": "https://a/x.json"},
                {"ix_id": 2, "ixf_ixp_member_list_url": "https://a/x.json"},
                {"ix_id": 3, "ixf_ixp_member_list_url": ""},
                {"ix_id": 4}]
        self.assertEqual(f.export_urls(lans), {"https://a/x.json": [1, 2]})


class TestSaveIfValid(unittest.TestCase):
    def test_keeps_previous_file_when_download_is_not_peeringdb_json(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "net_all.json")
            json.dump({"data": [{"asn": 1}]}, open(path, "w"))
            self.assertFalse(f.save_if_valid(path, b"<html>rate limited</html>"))
            self.assertFalse(f.save_if_valid(path, b'{"data": []}'))
            self.assertEqual(json.load(open(path)), {"data": [{"asn": 1}]})
            self.assertTrue(f.save_if_valid(path, b'{"data": [{"asn": 2}]}'))
            self.assertEqual(json.load(open(path)), {"data": [{"asn": 2}]})



class TestSafeUrl(unittest.TestCase):
    """Export URLs come from third-party PeeringDB records: only public http(s) hosts (SSRF)."""

    @staticmethod
    def resolver(addresses):
        return lambda host, port: [(None, None, None, None, (a, port)) for a in addresses[host]]

    def test_public_https_allowed(self):
        r = self.resolver({"ix.example": ["193.0.6.139"]})
        self.assertTrue(f.safe_url("https://ix.example/members.json", resolve=r))

    def test_internal_targets_refused(self):
        r = self.resolver({"lo.example": ["127.0.0.1"], "lan.example": ["192.168.1.5"],
                           "meta.example": ["169.254.169.254"], "mixed.example": ["193.0.6.139", "10.0.0.1"],
                           "v6.example": ["::1"]})
        for u in ("http://lo.example/", "https://lan.example/x", "http://meta.example/latest",
                  "https://mixed.example/", "https://v6.example/"):
            self.assertFalse(f.safe_url(u, resolve=r), u)

    def test_other_schemes_and_bad_urls_refused(self):
        r = self.resolver({"ix.example": ["193.0.6.139"]})
        for u in ("file:///etc/passwd", "ftp://ix.example/x", "https:///nohost", "not a url"):
            self.assertFalse(f.safe_url(u, resolve=r), u)


if __name__ == "__main__":
    unittest.main()
