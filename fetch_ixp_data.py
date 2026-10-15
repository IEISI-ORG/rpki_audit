"""
fetch_ixp_data.py — monthly refresh of the IXP data analyze_harvest.py uses to recognise IXP ASNs:
PeeringDB objects (data/atlas/peeringdb/) and the exchanges' public IX-F member exports
(data/atlas/ixf/, listed in PeeringDB as ixlan.ixf_ixp_member_list_url).

A PeeringDB file is replaced only by a valid, non-empty download, so a failed or rate-limited
refresh keeps last month's data. Each IX-F export is read in chunks with a 50 MB cap. Export URLs
come from third-party PeeringDB records, so every URL and redirect must be http(s) to a host that
resolves only to public addresses (safe_url), or it is skipped: no requests to this host's own
services or private networks (SSRF).

Usage: python3 fetch_ixp_data.py   (run monthly by rov_cron.sh ixp)
"""
import hashlib
import ipaddress
import json
import os
import socket
import time
from urllib.parse import urljoin, urlparse

import requests

import rov_utils
from atlas_harvest import ResponseTooLarge, read_capped

PDB_API = "https://www.peeringdb.com/api"
HEADERS = rov_utils.BGPTOOLS_HEADERS   # project name + repo URL
DIR_PEERINGDB = os.path.join(rov_utils.DIR_ATLAS, "peeringdb")
DIR_IXF = os.path.join(rov_utils.DIR_ATLAS, "ixf")
MAX_EXPORT_BYTES = 50_000_000
PDB_OBJECTS = {
    "ixpfx.json": "ixpfx?fields=prefix,ixlan_id,protocol",
    "netixlan.json": "netixlan?fields=asn,ipaddr4,ipaddr6,ixlan_id",
    "net_route_servers.json": "net?info_type=Route%20Server&fields=asn,name,info_type",
    "net_all.json": "net?fields=asn,name,org_id,info_type,info_types",
    "ix_org.json": "ix?fields=id,name,org_id",
    "ix.json": "ix?fields=id,name,city,country",
    "ixlan_ixf.json": "ixlan?fields=id,ix_id,ixf_ixp_member_list_url_visible,ixf_ixp_member_list_url",
}


def export_urls(lans: list[dict]) -> dict:
    """{export URL: [ix_id, ...]} for IX LANs that list an IX-F export publicly."""
    urls: dict = {}
    for lan in lans:
        u = lan.get("ixf_ixp_member_list_url")
        if u:
            urls.setdefault(u, []).append(lan.get("ix_id"))
    return urls


def save_if_valid(path: str, body: bytes) -> bool:
    """Write a PeeringDB download only if it parses and has data; otherwise keep the old file."""
    try:
        data = json.loads(body)
    except ValueError:
        return False
    if not isinstance(data, dict) or not data.get("data"):
        return False
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(body)
    os.replace(tmp, path)
    return True


MAX_REDIRECTS = 3


class UnsafeUrl(ValueError):
    pass


def safe_url(url: str, resolve=socket.getaddrinfo) -> bool:
    """http(s) URL whose host resolves only to public (global, non-multicast) addresses."""
    try:
        p = urlparse(url)
        if p.scheme not in ("http", "https") or not p.hostname:
            return False
        infos = resolve(p.hostname.rstrip("."), p.port or (443 if p.scheme == "https" else 80))
        addrs = [ipaddress.ip_address(info[4][0]) for info in infos]
    except (OSError, ValueError, UnicodeError):
        return False
    return bool(addrs) and all(a.is_global and not a.is_multicast for a in addrs)


def get(url: str, cap: int, timeout: int = 120) -> bytes:
    """Fetch with a byte cap, checking the URL and every redirect with safe_url."""
    for _ in range(MAX_REDIRECTS + 1):
        if not safe_url(url):
            raise UnsafeUrl(f"refused: {url}")
        with requests.get(url, timeout=timeout, stream=True, headers=HEADERS, allow_redirects=False) as r:
            if r.is_redirect and r.headers.get("Location"):
                url = urljoin(url, r.headers["Location"])
                continue
            r.raise_for_status()
            return read_capped(r.iter_content(1 << 20), cap)
    raise UnsafeUrl(f"too many redirects: {url}")


def main() -> None:
    os.makedirs(DIR_PEERINGDB, exist_ok=True)
    os.makedirs(DIR_IXF, exist_ok=True)
    for name, query in PDB_OBJECTS.items():
        try:
            ok = save_if_valid(os.path.join(DIR_PEERINGDB, name), get(f"{PDB_API}/{query}", 200_000_000))
        except (requests.RequestException, ResponseTooLarge, UnsafeUrl) as e:
            ok = False
            print(f"    [!] {name}: {e}")
        print(f"[*] PeeringDB {name}: {'updated' if ok else 'kept previous'}")
        time.sleep(3)   # anonymous API rate limit

    lans = json.load(open(os.path.join(DIR_PEERINGDB, "ixlan_ixf.json")))["data"]
    urls = export_urls(lans)
    index = {}
    for u, ix_ids in sorted(urls.items()):
        name = hashlib.sha1(u.encode()).hexdigest()[:16] + ".json"
        rec = {"url": u, "ix_ids": ix_ids}
        try:
            body = get(u, MAX_EXPORT_BYTES, timeout=60)
            json.loads(body)
            with open(os.path.join(DIR_IXF, name), "wb") as fh:
                fh.write(body)
            rec.update(file=name, bytes=len(body))
        except (requests.RequestException, ResponseTooLarge, ValueError) as e:   # UnsafeUrl is a ValueError
            rec["error"] = f"{type(e).__name__}: {str(e)[:120]}"
            if os.path.exists(os.path.join(DIR_IXF, name)):
                rec["file"] = name   # keep last month's copy in use
        index[u] = rec
        time.sleep(1)
    with open(os.path.join(DIR_IXF, "index.json"), "w") as fh:
        json.dump(index, fh, indent=1)
    ok = sum(1 for r in index.values() if "bytes" in r)
    print(f"[+] IX-F exports: {ok} of {len(index)} fetched; {DIR_IXF}/index.json")


if __name__ == "__main__":
    main()
