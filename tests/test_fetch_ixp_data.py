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


if __name__ == "__main__":
    unittest.main()
