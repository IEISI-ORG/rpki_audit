"""
fetch_ixp_data.py — monthly refresh of the IXP data analyze_harvest.py uses to recognise IXP ASNs:
PeeringDB objects (data/atlas/peeringdb/) and the exchanges' public IX-F member exports
(data/atlas/ixf/, listed in PeeringDB as ixlan.ixf_ixp_member_list_url).

A PeeringDB file is replaced only by a valid, non-empty download, so a failed or rate-limited
refresh keeps last month's data. Each IX-F export is read in chunks with a 50 MB cap. Export URLs
come from third-party PeeringDB records (SSRF risk). Requests go through make_session(): its
connections resolve the host urllib3 actually parsed, refuse it unless every address is public,
and connect to the address they checked (no second DNS lookup, no parser differential), with
environment proxies off. Redirects (at most 3) are followed by hand through the same session.

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
import urllib3.connection
import urllib3.connectionpool
from requests.adapters import HTTPAdapter
from urllib3.exceptions import NewConnectionError

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


def public_addresses(host: str, port: int, resolve=socket.getaddrinfo) -> list:
    """getaddrinfo results for host, or UnsafeUrl unless every address is global and not multicast."""
    try:
        infos = resolve(host, port, type=socket.SOCK_STREAM)
        addrs = [ipaddress.ip_address(str(i[4][0]).split("%")[0]) for i in infos]
    except (OSError, ValueError, UnicodeError) as e:
        raise UnsafeUrl(f"refused {host}: {e}") from e
    if not addrs or not all(a.is_global and not a.is_multicast for a in addrs):
        raise UnsafeUrl(f"refused {host}: non-public address in {sorted(map(str, addrs))}")
    return infos


class _PublicOnly:
    """urllib3 connection that checks the addresses it is about to use, then connects to them."""

    def _new_conn(self):
        try:
            infos = public_addresses(self._dns_host, self.port)
        except UnsafeUrl as e:
            raise NewConnectionError(self, str(e)) from e
        timeout = self.timeout if isinstance(self.timeout, (int, float)) else None
        last = None
        for family, kind, proto, _, addr in infos:
            sock = socket.socket(family, kind, proto)
            try:
                sock.settimeout(timeout)
                sock.connect(addr)
                return sock
            except OSError as e:
                sock.close()
                last = e
        raise NewConnectionError(self, f"failed to connect to {self.host}: {last}")


class PublicHTTPConnection(_PublicOnly, urllib3.connection.HTTPConnection):
    pass


class PublicHTTPSConnection(_PublicOnly, urllib3.connection.HTTPSConnection):
    pass


class _PublicHTTPPool(urllib3.connectionpool.HTTPConnectionPool):
    ConnectionCls = PublicHTTPConnection


class _PublicHTTPSPool(urllib3.connectionpool.HTTPSConnectionPool):
    ConnectionCls = PublicHTTPSConnection


def make_session() -> requests.Session:
    """requests session whose connections only reach public addresses; environment proxies off."""
    s = requests.Session()
    s.trust_env = False
    adapter = HTTPAdapter()
    adapter.poolmanager.pool_classes_by_scheme = {"http": _PublicHTTPPool, "https": _PublicHTTPSPool}
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    s.headers.update(HEADERS)
    return s


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


def get(url: str, cap: int, timeout: int = 120, session: requests.Session | None = None) -> bytes:
    """Fetch with a byte cap through a public-only session; redirects followed by hand (at most 3).
    safe_url is only a cheap pre-filter; the connection itself enforces public addresses."""
    session = session or make_session()
    for _ in range(MAX_REDIRECTS + 1):
        if not safe_url(url):
            raise UnsafeUrl(f"refused: {url}")
        with session.get(url, timeout=timeout, stream=True, allow_redirects=False) as r:
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
