"""
nz_beacon_baseline.py — country-wide ROV baseline from every connected RIPE Atlas probe.

Each probe pings (3 packets) and ICMP-traceroutes two valid/invalid beacon pairs:
  cf  — Cloudflare's isbgpsafeyet.com pair (the one the audit uses). Cloudflare
        announces the invalid prefix straight to its many peers, so this mostly
        tests the network's session with Cloudflare.
  ris — RIPE NCC RIS beacons (AS12654). Few upstreams carry the invalid prefix
        (52 of 327 RIS peers on 2026-10-14), so "invalid-unreachable" here usually
        means no upstream offered the route, not that the probe's network filters.

Outputs go to data/atlas/baseline/<cc>_<date>/ (raw results, probes, ip→ASN map,
probes.csv, ases.csv) and a summary to reports/<cc>_beacon_baseline.md. An IX hop
never shows who dropped a route; stop ASNs are where traces went silent, nothing more.

Usage:
  python3 nz_beacon_baseline.py                 # NZ, IPv4 and IPv6
  python3 nz_beacon_baseline.py --dry-run       # list probes and targets, no credits
  python3 nz_beacon_baseline.py --reanalyse data/atlas/baseline/nz_2026-10-14
"""
import argparse
import csv
import ipaddress
import json
import os
import socket
import time
from collections import defaultdict
from datetime import date, datetime, timezone

import requests
import yaml

import rov_utils

PAIRS = ("cf", "ris")
KINDS = ("ping", "trace")
RIS_TARGETS = {4: {"ris_valid": "93.175.146.1", "ris_invalid": "93.175.147.1"},
               6: {"ris_valid": "2001:7fb:fd02::1", "ris_invalid": "2001:7fb:fd03::1"}}
CF_DOMAINS = {"cf_valid": "valid.rpki.isbgpsafeyet.com", "cf_invalid": "invalid.rpki.isbgpsafeyet.com"}
ATLAS_API = "https://atlas.ripe.net/api/v2"
RIPESTAT_NETINFO = "https://stat.ripe.net/data/network-info/data.json?resource="
PEERINGDB_NETIXLAN = "https://www.peeringdb.com/api/netixlan"
POLL_SECS, POLL_LIMIT_SECS = 30, 1200
DIR_BASELINE = os.path.join(rov_utils.DIR_ATLAS, "baseline")


# --- pure parsing / summary (tested) -----------------------------------------
def ping_reached(res: dict | None) -> bool | None:
    """True if any echo reply came back; None when the probe returned no usable result."""
    if not res or "rcvd" not in res:
        return None
    return res["rcvd"] > 0


def trace_hops(res: dict | None) -> list[str | None]:
    """First responding address per hop, None for a silent hop."""
    hops = []
    for h in (res or {}).get("result", []):
        replies = [r["from"] for r in h.get("result", []) if "from" in r]
        hops.append(replies[0] if replies else None)
    return hops


def public_hops(hops: list[str | None]) -> list[str]:
    out = []
    for h in hops:
        try:
            if h and ipaddress.ip_address(h).is_global:
                out.append(h)
        except ValueError:
            pass
    return out


def as_path(hops: list[str | None], ip2asn: dict) -> list[int]:
    path: list[int] = []
    for h in hops:
        asn = ip2asn.get(h)
        if asn and (not path or path[-1] != asn):
            path.append(asn)
    return path


def stop_asn(hops: list[str | None], ip2asn: dict) -> int | None:
    """ASN of the last hop that answered and resolved: where the trace went silent."""
    for h in reversed(hops):
        if h in ip2asn:
            return ip2asn[h]
    return None


def pair_outcome(valid_ok: bool | None, invalid_ping: bool | None, invalid_trace: bool) -> str:
    if invalid_ping or invalid_trace:
        return "reaches-invalid"
    if valid_ok is None:
        return "no-data"
    if not valid_ok:
        return "no-valid"
    return "invalid-unreachable"


def probe_row(probe: dict, af: int, results: dict, targets: dict, ip2asn: dict) -> dict:
    pid = probe["id"]
    row = {"probe_id": pid, "af": af, "probe_asn": probe.get(f"asn_v{af}"),
           "anchor": bool(probe.get("is_anchor"))}
    for pair in PAIRS:
        hops = {}
        for side in ("valid", "invalid"):
            key = f"{pair}_{side}"
            hops[side] = trace_hops(results.get(("trace", key), {}).get(pid))
            row[f"{key}_ping"] = ping_reached(results.get(("ping", key), {}).get(pid))
            row[f"{key}_path"] = " ".join(map(str, as_path(hops[side], ip2asn)))
        reached = {s: targets[f"{pair}_{s}"] in hops[s] for s in hops}
        valid_ok = (row[f"{pair}_valid_ping"] or reached["valid"]
                    if row[f"{pair}_valid_ping"] is not None or hops["valid"] else None)
        row[pair] = pair_outcome(valid_ok, row[f"{pair}_invalid_ping"], reached["invalid"])
        row[f"{pair}_invalid_stop_asn"] = (stop_asn(hops["invalid"], ip2asn)
                                           if row[pair] == "invalid-unreachable" else None)
    return row


def as_summary(rows: list[dict]) -> list[dict]:
    groups: dict = defaultdict(list)
    for r in rows:
        groups[(r["probe_asn"], r["af"])].append(r)
    out = []
    for (asn, af), rs in sorted(groups.items(), key=lambda x: (x[0][1], -len(x[1]), str(x[0][0]))):
        rec = {"asn": asn, "af": af, "probes": len(rs)}
        for pair in PAIRS:
            tested = [r for r in rs if r[pair] in ("reaches-invalid", "invalid-unreachable")]
            hit = sum(r[pair] == "reaches-invalid" for r in tested)
            rec[f"{pair}_reach_invalid"] = f"{hit}/{len(tested)}"
        stops = sorted({r["ris_invalid_stop_asn"] for r in rs if r.get("ris_invalid_stop_asn")})
        rec["ris_stop_asns"] = " ".join(map(str, stops))
        out.append(rec)
    return out


# --- Atlas / lookups (network) ------------------------------------------------
def atlas_key() -> str:
    with open("secrets.yaml") as f:
        return yaml.safe_load(f)["ripe_atlas_key"]


def connected_probes(cc: str) -> list[dict]:
    url = f"{ATLAS_API}/probes/?country_code={cc}&status=1&page_size=500&fields=id,asn_v4,asn_v6,is_anchor,tags"
    probes = []
    while url:
        page = requests.get(url, timeout=60).json()
        probes += page["results"]
        url = page.get("next")
    return probes


def build_targets(af: int) -> dict:
    fam = socket.AF_INET6 if af == 6 else socket.AF_INET
    t = {k: socket.getaddrinfo(d, None, fam)[0][4][0] for k, d in CF_DOMAINS.items()}
    return {**t, **RIS_TARGETS[af]}


def launch(af: int, probe_ids: list[int], targets: dict, cc: str) -> dict:
    from ripe.atlas.cousteau import AtlasCreateRequest, AtlasSource, Ping, Traceroute
    defs, order = [], []
    for kind in KINDS:
        for name, ip in targets.items():
            desc = f"rpki_audit {cc} beacon baseline {kind} {name} v{af}"
            cls = Ping(af=af, target=ip, description=desc, is_oneoff=True, packets=3) if kind == "ping" else \
                Traceroute(af=af, target=ip, description=desc, is_oneoff=True, protocol="ICMP")
            defs.append(cls)
            order.append((kind, name))
    src = AtlasSource(type="probes", value=",".join(map(str, probe_ids)), requested=len(probe_ids))
    ok, resp = AtlasCreateRequest(start_time=datetime.now(timezone.utc), key=atlas_key(),
                                  measurements=defs, sources=[src], is_oneoff=True).create()
    if not ok:
        raise RuntimeError(f"Atlas create failed: {resp}")
    return {f"{k}:{n}": m for (k, n), m in zip(order, resp["measurements"])}


def wait_and_fetch(ids: dict, outdir: str) -> None:
    pending, waited = set(ids.values()), 0
    while pending and waited < POLL_LIMIT_SECS:
        time.sleep(POLL_SECS)
        waited += POLL_SECS
        for m in list(pending):
            st = requests.get(f"{ATLAS_API}/measurements/{m}/?fields=status", timeout=30).json()
            if st.get("status", {}).get("name") in ("Stopped", "Failed", "No suitable probes"):
                pending.discard(m)
        print(f"    - {len(ids) - len(pending)}/{len(ids)} measurements finished after {waited}s")
    for m in ids.values():
        res = requests.get(f"{ATLAS_API}/measurements/{m}/results/", timeout=120).json()
        with open(os.path.join(outdir, f"raw_{m}.json"), "w") as f:
            json.dump(res, f)


def resolve(ips: set[str], cache_path: str) -> dict:
    """ip → ASN via RIPEstat, then PeeringDB netixlan for unannounced IX LAN addresses."""
    cache = {}
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            cache = json.load(f)
    for ip in sorted(ips - set(cache)):
        asn = None
        try:
            asns = requests.get(RIPESTAT_NETINFO + ip, timeout=10).json()["data"].get("asns", [])
            asn = int(asns[0]) if asns else None
            if asn is None:
                fam = "ipaddr6" if ":" in ip else "ipaddr4"
                data = requests.get(f"{PEERINGDB_NETIXLAN}?{fam}={ip}", timeout=20).json().get("data", [])
                asn = int(data[0]["asn"]) if data else None
                time.sleep(3)  # PeeringDB anonymous rate limit
        except (requests.RequestException, ValueError, KeyError, IndexError):
            pass
        cache[ip] = asn
    with open(cache_path, "w") as f:
        json.dump(cache, f, indent=1, sort_keys=True)
    return {ip: a for ip, a in cache.items() if a}


# --- analysis + reporting -------------------------------------------------------
def load_results(outdir: str, ids: dict) -> dict:
    res: dict = {}
    for key, m in ids.items():
        kind, name = key.split(":")
        path = os.path.join(outdir, f"raw_{m}.json")
        rows = json.load(open(path)) if os.path.exists(path) else []
        res[(kind, name)] = {r["prb_id"]: r for r in rows if isinstance(r, dict) and "prb_id" in r}
    return res


def analyse(outdir: str, cc: str) -> None:
    meta = json.load(open(os.path.join(outdir, "meta.json")))
    probes = {p["id"]: p for p in meta["probes"]}
    rows = []
    for af_s, run in meta["runs"].items():
        af = int(af_s)
        results = load_results(outdir, run["ids"])
        ips = {h for r in results.values() for x in r.values() for h in public_hops(trace_hops(x))}
        ip2asn = resolve(ips, os.path.join(outdir, "ip2asn.json"))
        for pid in run["probe_ids"]:
            rows.append(probe_row(probes[pid], af, results, run["targets"], ip2asn))
    write_csv(os.path.join(outdir, "probes.csv"), rows)
    summary = as_summary(rows)
    write_csv(os.path.join(outdir, "ases.csv"), summary)
    write_report(cc, meta, rows, summary)


def write_csv(path: str, rows: list[dict]) -> None:
    if not rows:
        return
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_report(cc: str, meta: dict, rows: list[dict], summary: list[dict]) -> None:
    audit = rov_utils.load_audit_csv().set_index("asn")

    def col(asn, c):
        try:
            return audit.loc[int(asn), c]
        except (KeyError, ValueError, TypeError):
            return ""
    lines = [f"# {cc} beacon baseline ({meta['date']})", "",
             "Every connected RIPE Atlas probe in the country pinged and traced two valid/invalid "
             "beacon pairs. **cf** = Cloudflare (most networks get its invalid route straight from "
             "Cloudflare); **ris** = RIPE NCC RIS beacons AS12654 (few upstreams carry the invalid "
             "route, so failing to reach it usually means it was never offered).", "",
             "Measurement IDs: " + "; ".join(
                 f"v{af}: " + ", ".join(f"{k}={m}" for k, m in run["ids"].items())
                 for af, run in meta["runs"].items()), ""]
    for af in sorted({r["af"] for r in rows}):
        rs = [r for r in rows if r["af"] == af]
        lines.append(f"## IPv{af}: {len(rs)} probes")
        for pair in PAIRS:
            c = defaultdict(int)
            for r in rs:
                c[r[pair]] += 1
            lines.append(f"- {pair}: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
        lines += ["", "| AS | name | probes | cf reach invalid | ris reach invalid | ris stop ASNs | "
                  "verdict | APNIC | ROVista |", "|---|---|---|---|---|---|---|---|---|"]
        for s in [s for s in summary if s["af"] == af]:
            lines.append(f"| {s['asn']} | {str(col(s['asn'], 'name'))[:28]} | {s['probes']} | "
                         f"{s['cf_reach_invalid']} | {s['ris_reach_invalid']} | {s['ris_stop_asns']} | "
                         f"{col(s['asn'], 'verdict')} | {col(s['asn'], 'apnic_score')} | "
                         f"{col(s['asn'], 'rovista_score')} |")
        lines.append("")
    path = os.path.join("reports", f"{cc.lower()}_beacon_baseline.md")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"[+] {path}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cc", default="NZ")
    ap.add_argument("--af", default="4,6")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reanalyse", help="existing baseline directory; no new measurements")
    args = ap.parse_args()
    cc = args.cc.upper()
    if args.reanalyse:
        analyse(args.reanalyse, cc)
        return
    probes = connected_probes(cc)
    meta = {"cc": cc, "date": date.today().isoformat(), "probes": probes, "runs": {}}
    for af in (int(a) for a in args.af.split(",")):
        ids_ = [p["id"] for p in probes if p.get(f"asn_v{af}")]
        targets = build_targets(af)
        print(f"[*] IPv{af}: {len(ids_)} probes, targets {targets}")
        meta["runs"][str(af)] = {"probe_ids": ids_, "targets": targets, "ids": {}}
    if args.dry_run:
        return
    outdir = os.path.join(DIR_BASELINE, f"{cc.lower()}_{meta['date']}")
    os.makedirs(outdir, exist_ok=True)
    for af_s, run in meta["runs"].items():
        run["ids"] = launch(int(af_s), run["probe_ids"], run["targets"], cc)
        print(f"    - IPv{af_s} measurements: {run['ids']}")
    with open(os.path.join(outdir, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)
    for run in meta["runs"].values():
        wait_and_fetch(run["ids"], outdir)
    analyse(outdir, cc)


if __name__ == "__main__":
    main()
