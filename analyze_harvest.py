"""
analyze_harvest.py — what the harvested public Atlas traceroutes to Cloudflare's RPKI-invalid
beacon say about each network (atlas_harvest.py output, no credits).

A trace that reaches the invalid host shows every AS on its path forwarding the invalid route at
that time (most get it straight from Cloudflare, so it tests that session). A trace that doesn't
reach it attributes nothing: silence isn't a drop point (CLAUDE.md, IX hops). Hop IPs are mapped
with the iptoasn.com table; each probe's own ASN comes from the RIPE Atlas probe archive.

Inputs:  data/atlas/harvest/, data/atlas/ip2asn/ip2asn-combined.tsv.gz,
         data/atlas/probes/<YYYYMMDD>.json.bz2, rov_audit_v22_final.csv
Outputs: data/atlas/harvest_evidence.csv (per AS and address family),
         reports/atlas_harvest_analysis.md

Usage: python3 analyze_harvest.py
"""
import bisect
import bz2
import csv
import glob
import gzip
import ipaddress
import json
import os
import time
from collections import Counter, defaultdict

import rov_utils

BEACON_ORIGIN = 13335
CF_INVALID = {"103.21.244.9", "103.21.244.19", "2606:4700:7000::6715:f409"}
# Same freshness rule as the audit's own Atlas results (Terry, 2026-10-15: even 90 days is too old).
RECENT_DAYS = rov_utils.ATLAS_TTL_DAYS
DIR_HARVEST = os.path.join(rov_utils.DIR_ATLAS, "harvest")
FILE_IP2ASN = os.path.join(rov_utils.DIR_ATLAS, "ip2asn", "ip2asn-combined.tsv.gz")
GLOB_PROBES = os.path.join(rov_utils.DIR_ATLAS, "probes", "*.json.bz2")
DIR_PEERINGDB = os.path.join(rov_utils.DIR_ATLAS, "peeringdb")
FILE_EVIDENCE = os.path.join(rov_utils.DIR_ATLAS, "harvest_evidence.csv")
FILE_REPORT = os.path.join("reports", "atlas_harvest_analysis.md")


class IpAsn:
    """Range lookup over (start_int, end_int, asn) rows, kept apart per address family."""

    def __init__(self, rows):
        self.tables = {4: [], 6: []}
        for start, end, asn in rows:
            self.tables[4 if end < 2 ** 32 else 6].append((start, end, asn))
        for t in self.tables.values():
            t.sort()
        self.starts = {af: [r[0] for r in t] for af, t in self.tables.items()}

    def asn(self, ip: str) -> int | None:
        addr = ipaddress.ip_address(ip)
        t, starts = self.tables[addr.version], self.starts[addr.version]
        i = bisect.bisect_right(starts, int(addr)) - 1
        if i >= 0 and t[i][0] <= int(addr) <= t[i][1]:
            return t[i][2]
        return None


class IxMap:
    """IX LAN prefixes (PeeringDB ixpfx) and who holds each address on them (netixlan)."""

    def __init__(self, prefixes: list[dict], netixlan: list[dict]):
        ranges = {4: [], 6: []}
        for p in prefixes:
            try:
                net = ipaddress.ip_network(p["prefix"], strict=False)
            except (KeyError, ValueError):
                continue
            ranges[net.version].append((int(net.network_address), int(net.broadcast_address)))
        self.ranges = {af: sorted(r) for af, r in ranges.items()}
        self.starts = {af: [a for a, _ in r] for af, r in self.ranges.items()}
        self.owner = {}
        for n in netixlan:
            for key in ("ipaddr4", "ipaddr6"):
                if n.get(key):
                    self.owner[str(ipaddress.ip_address(n[key]))] = n["asn"]

    def lookup(self, ip: str) -> tuple[bool, int | None]:
        """(on an IX LAN, participant ASN or None)."""
        addr = ipaddress.ip_address(ip)
        r, starts, x = self.ranges[addr.version], self.starts[addr.version], int(addr)
        i = bisect.bisect_right(starts, x) - 1
        if i >= 0 and r[i][0] <= x <= r[i][1]:
            return True, self.owner.get(str(addr))
        return False, None


def load_ix(directory: str = DIR_PEERINGDB) -> tuple["IxMap | None", set]:
    """IxMap and the ASNs of PeeringDB route-server networks; (None, set()) without the files."""
    try:
        pfx = json.load(open(os.path.join(directory, "ixpfx.json")))["data"]
        nix = json.load(open(os.path.join(directory, "netixlan.json")))["data"]
    except (OSError, ValueError, KeyError):
        return None, set()
    try:
        rs = {r["asn"] for r in json.load(open(os.path.join(directory, "net_route_servers.json")))["data"]}
    except (OSError, ValueError, KeyError):
        rs = set()
    return IxMap(pfx, nix), rs


def load_ip2asn(path: str = FILE_IP2ASN) -> IpAsn:
    rows = []
    with gzip.open(path, "rt") as f:
        for line in f:
            start, end, asn = line.split("\t")[:3]
            if asn != "0":
                rows.append((int(ipaddress.ip_address(start)), int(ipaddress.ip_address(end)), int(asn)))
    return IpAsn(rows)


def load_probe_asns(pattern: str = GLOB_PROBES) -> dict:
    """{probe id: {4: asn_v4, 6: asn_v6}} from the newest RIPE Atlas probe archive file."""
    files = sorted(glob.glob(pattern))
    if not files:
        return {}
    data = json.load(bz2.open(files[-1], "rt"))
    probes = data.get("objects", data) if isinstance(data, dict) else data
    return {p["id"]: {4: p.get("asn_v4"), 6: p.get("asn_v6")} for p in probes}


def hop_ips(trace: dict) -> list[str]:
    """First responding public address of each hop, in order."""
    out = []
    for h in trace.get("result", []):
        for r in h.get("result", []) if isinstance(h, dict) else []:
            ip = r.get("from") if isinstance(r, dict) else None
            if not ip:
                continue
            try:
                if not ipaddress.ip_address(ip).is_global:
                    continue
            except ValueError:
                continue
            out.append(ip)
            break
    return out


def reached(trace: dict) -> bool:
    return trace.get("dst_addr") in hop_ips(trace)


def as_runs(ips: list[str], lookup: IpAsn, ix: "IxMap | None" = None) -> list[tuple[int, int]]:
    """[(asn, hops)] along the trace: consecutive hops in the same AS merged, unmapped hops skipped.
    A hop on an IX LAN belongs to the participant holding that address (PeeringDB netixlan), not to
    whoever announces the LAN prefix; with no known holder it is skipped."""
    runs: list[list[int]] = []
    for ip in ips:
        on_ix, holder = ix.lookup(ip) if ix else (False, None)
        asn = holder if on_ix else lookup.asn(ip)
        if not asn:
            continue
        if runs and runs[-1][0] == asn:
            runs[-1][1] += 1
        else:
            runs.append([asn, 1])
    return [(a, n) for a, n in runs]


def credible_forwarders(runs: list[tuple[int, int]], probe_asn: int | None,
                        exclude: set = frozenset()) -> set[int]:
    """ASes a trace that reached the invalid host shows forwarding the invalid route.

    The probe's own AS always counts (its users reached the host). Another AS counts when it has
    >= 2 hops, or hands the trace straight to the beacon origin. A single hop between two other
    ASes is usually that AS's address on a border router (third-party address), not transit
    through it: e.g. 2026-01-04, 399078 -> one 3356-numbered hop -> 26042 -> 13335. exclude:
    ASes that can't be forwarders (PeeringDB route-server networks, NON_TRANSIT_ASNS).
    """
    out = {probe_asn} if probe_asn else set()
    for i, (asn, hops) in enumerate(runs):
        nxt = runs[i + 1][0] if i + 1 < len(runs) else None
        if hops >= 2 or nxt == BEACON_ORIGIN or asn == probe_asn:
            out.add(asn)
    return out - {BEACON_ORIGIN, 0} - set(exclude)


def main() -> None:
    t0 = time.time()
    lookup = load_ip2asn()
    probe_asns = load_probe_asns()
    ix, route_servers = load_ix()
    exclude = route_servers | set(rov_utils.NON_TRANSIT_ASNS)
    index = json.load(open(os.path.join(DIR_HARVEST, "index.json")))
    recent_from = time.time() - RECENT_DAYS * 86400
    ev = defaultdict(lambda: {"probes": set(), "traces": 0, "last": 0, "recent_probes": set()})
    totals = Counter()
    for msm_id, m in index.items():
        if m.get("type") != "traceroute" or m.get("target") not in CF_INVALID or not m.get("results"):
            continue
        path_file = os.path.join(DIR_HARVEST, f"{msm_id}.json.gz")
        if not os.path.exists(path_file):
            continue
        for t in json.load(gzip.open(path_file, "rt")):
            af, ts = t.get("af"), t.get("timestamp", 0)
            totals[(af, "traces")] += 1
            if not reached(t):
                continue
            totals[(af, "reached")] += 1
            if ts >= recent_from:
                totals[(af, "recent reached")] += 1
            probe_asn = probe_asns.get(t.get("prb_id"), {}).get(af)
            for asn in credible_forwarders(as_runs(hop_ips(t), lookup, ix), probe_asn, exclude):
                e = ev[(asn, af)]
                e["probes"].add(t.get("prb_id"))
                e["traces"] += 1
                e["last"] = max(e["last"], ts)
                if ts >= recent_from:
                    e["recent_probes"].add(t.get("prb_id"))
    with open(FILE_EVIDENCE, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["asn", "af", "probes", "traces", "last_seen", "recent_probes"])
        for (asn, af), e in sorted(ev.items()):
            w.writerow([asn, af, len(e["probes"]), e["traces"],
                        time.strftime("%Y-%m-%d", time.gmtime(e["last"])), len(e["recent_probes"])])
    write_report(ev, totals, len(probe_asns), ix is not None, len(route_servers))
    print(f"[+] {FILE_EVIDENCE}, {FILE_REPORT} ({time.time() - t0:.0f}s)")


def write_report(ev: dict, totals: Counter, n_probe_meta: int, have_ix: bool = False, n_rs: int = 0) -> None:
    audit = {int(r["asn"]): r for r in csv.DictReader(open(rov_utils.FILE_AUDIT_FINAL))}
    recent4 = {asn: e for (asn, af), e in ev.items() if af == 4 and e["recent_probes"]}
    n_recent = {af: sum(1 for (a, f), e in ev.items() if f == af and e["recent_probes"]) for af in (4, 6)}
    n_any = {af: sum(1 for (a, f) in ev if f == af) for af in (4, 6)}
    conflicts, new = [], []
    for asn, e in recent4.items():
        r = audit.get(asn)
        if not r:
            continue
        row = (int(r["cone"] or 0), asn, e, r)
        if rov_utils.classify_verdict(r["verdict"]) == "SECURE":
            conflicts.append(row)
        elif r.get("decided_by") in ("none", "declared"):
            new.append(row)
    lines = ["# Public Atlas traces to Cloudflare's RPKI-invalid beacon", "",
             f"Generated {time.strftime('%Y-%m-%d')} by `analyze_harvest.py` from `atlas_harvest.py` output "
             "(third-party measurements, no credits). A trace that reaches the invalid host means the ASes on its "
             "path forwarded the invalid route then; most receive it straight from Cloudflare, so this tests that "
             "session. Traces that stop attribute nothing. Invalid side only: there is no paired valid trace, so "
             "there is no off-path check. An AS counts as a forwarder only if it is the probe's own AS, has >= 2 "
             "hops, or hands the trace straight to Cloudflare (a single hop between two other ASes is usually a "
             f"border-router address). Probe home ASNs known for {n_probe_meta:,} probes.", "",
             ("IX LAN hops are attributed to the participant holding the address (PeeringDB netixlan), and "
              f"{n_rs:,} PeeringDB route-server networks never count as forwarders. AS0 ASPA records are not used "
              "to exclude: Cogent, Arelion, AT&T, GTT, Deutsche Telekom and Liberty Global publish AS0 too."
              if have_ix else "PeeringDB files missing: IX LAN hops are not resolved."), "",
             f"Only traces from the last {RECENT_DAYS} days count, the same freshness rule as the audit's own Atlas "
             "results. The first harvest is mostly older campaigns (IPv6: 7,423 of 7,499 traces in June 2026; IPv4: "
             "mostly January 2026), so little of it is current; the daily harvest adds new public measurements.", "",
             "| | IPv4 | IPv6 |", "|---|---|---|",
             f"| traces (any age) | {totals[(4, 'traces')]:,} | {totals[(6, 'traces')]:,} |",
             f"| reached the invalid host (any age) | {totals[(4, 'reached')]:,} | {totals[(6, 'reached')]:,} |",
             f"| reached it, last {RECENT_DAYS} days | {totals[(4, 'recent reached')]:,} | "
             f"{totals[(6, 'recent reached')]:,} |",
             f"| ASes seen forwarding (any age) | {n_any[4]:,} | {n_any[6]:,} |",
             f"| ASes seen forwarding, last {RECENT_DAYS} days | {n_recent[4]:,} | {n_recent[6]:,} |", ""]

    def table(title, rows, note):
        out = [f"## {title}", "", note, "",
               f"| AS | name | cc | cone | verdict | decided by | probes ({RECENT_DAYS} d) | last seen |",
               "|---|---|---|---|---|---|---|---|"]
        for cone, asn, e, r in sorted(rows, key=lambda x: (-x[0], -len(x[2]["recent_probes"])))[:40]:
            out.append(f"| {asn} | {r['name'][:30]} | {r['cc']} | {cone:,} | {r['verdict']} | "
                       f"{r.get('decided_by', '')} | {len(e['recent_probes'])} | "
                       f"{time.strftime('%Y-%m-%d', time.gmtime(e['last']))} |")
        return out + ["", f"{len(rows):,} ASes in all.", ""]

    lines += table("IPv4: audit says SECURE, but current traces show the AS forwarding", conflicts,
                   "Candidates for an Atlas re-test. A PASSIVE stub here means its users reached the invalid host.")
    lines += table("IPv4: current evidence where the audit has only a declaration or nothing", new,
                   "Decided by a declaration (bgp.tools tag, isbgpsafeyet) or not at all in the audit.")
    nz = [(int(audit[a]["cone"] or 0), a, e, audit[a]) for a, e in recent4.items()
          if a in audit and audit[a]["cc"] == "NZ"]
    lines += table("NZ networks seen forwarding (IPv4, current)", nz, "")
    with open(FILE_REPORT, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
