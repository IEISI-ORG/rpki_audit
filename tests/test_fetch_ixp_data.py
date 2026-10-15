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



class TestConnectionLevelCheck(unittest.TestCase):
    """The check runs where urllib3 connects, on the host it parsed and the addresses it uses:
    no parser differential, no second DNS lookup, no environment proxies."""

    @staticmethod
    def resolver(addresses):
        return lambda host, port, type=0: [(2, 1, 6, "", (a, port)) for a in addresses]

    def test_public_addresses(self):
        infos = f.public_addresses("ix.example", 443, resolve=self.resolver(["193.0.6.139"]))
        self.assertEqual([i[4][0] for i in infos], ["193.0.6.139"])
        for bad in (["127.0.0.1"], ["193.0.6.139", "10.1.2.3"], ["169.254.169.254"], []):
            with self.assertRaises(f.UnsafeUrl):
                f.public_addresses("ix.example", 443, resolve=self.resolver(bad))

    def test_session_uses_public_only_connections_and_no_proxies(self):
        s = f.make_session()
        self.assertFalse(s.trust_env)
        pools = s.get_adapter("https://ix.example/").poolmanager.pool_classes_by_scheme
        self.assertIs(pools["https"].ConnectionCls, f.PublicHTTPSConnection)
        self.assertIs(pools["http"].ConnectionCls, f.PublicHTTPConnection)

    def test_request_to_loopback_is_refused_before_connecting(self):
        # urllib3 parses these hosts as loopback; the connection refuses them (no socket opened)
        for u in ("http://127.0.0.1:9/x", "http://user@127.0.0.1:9/", "http://[::1]:9/", "http://localhost:9/"):
            with self.assertRaises(Exception) as cm:
                f.make_session().get(u, timeout=5, allow_redirects=False)
            self.assertIn("refused", str(cm.exception), u)

    def test_differential_url_refused_by_prefilter(self):
        # urlparse reads this host as 127.0.0.1, urllib3 as 193.0.6.139: get() refuses it outright
        with self.assertRaises(f.UnsafeUrl):
            f.get("http://193.0.6.139\\@127.0.0.1:9/", cap=10)


if __name__ == "__main__":
    unittest.main()
