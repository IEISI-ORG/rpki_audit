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


def load_ix(directory: str = DIR_PEERINGDB) -> tuple["IxMap | None", set, list, list]:
    """IxMap, ASNs with PeeringDB info_type "Route Server", ixpfx rows and netixlan rows; empty without
    the files."""
    try:
        pfx = json.load(open(os.path.join(directory, "ixpfx.json")))["data"]
        nix = json.load(open(os.path.join(directory, "netixlan.json")))["data"]
    except (OSError, ValueError, KeyError):
        return None, set(), [], []
    try:
        rs = {r["asn"] for r in json.load(open(os.path.join(directory, "net_route_servers.json")))["data"]}
    except (OSError, ValueError, KeyError):
        rs = set()
    return IxMap(pfx, nix), rs, pfx, nix


def ix_announcers(prefixes: list[dict], netixlan: list[dict], lookup: IpAsn) -> set:
    """ASNs announcing an IX LAN prefix that PeeringDB also lists on that same IX LAN. iptoasn alone
    can't tell an IX's own announcement from a covering aggregate: IX LANs numbered out of Cogent's
    38/8 map to Cogent, which is on none of them (2026-10-15)."""
    members: dict = defaultdict(set)
    for n in netixlan:
        members[n.get("ixlan_id")].add(n.get("asn"))
    out = set()
    for p in prefixes:
        try:
            asn = lookup.asn(str(ipaddress.ip_network(p["prefix"], strict=False).network_address))
        except (KeyError, ValueError):
            continue
        if asn and asn in members.get(p.get("ixlan_id"), ()):
            out.add(asn)
    return out


def ixp_asns(peeringdb_rs: set, as0: set, ix_announcers: set, tier1: set = frozenset(),
             mid_path: set = frozenset()) -> set:
    """IXP ASNs: at least two of three signals, PeeringDB info_type "Route Server" (self-declared), an
    AS0 ASPA record (no providers) and announcing an IX LAN prefix while being on that LAN
    (ix_announcers). One signal alone isn't enough (Terry, 2026-10-15). Excluded whatever the signals:
    Tier 1s (for them AS0 is evidence of being a Tier 1) and ASNs that carry traffic in BGP (an IXP's
    route servers are transparent, RFC 7947; an ASN passing routes to >= 3 networks is transit)."""
    signals = Counter()
    for s in (peeringdb_rs, as0, ix_announcers):
        signals.update(set(s))
    return {asn for asn, n in signals.items() if n >= 2} - set(tier1) - set(mid_path)


MID_PATH_MIN_LEFT = 3


def load_mid_path(base_dir: str = "output", min_left: int = MID_PATH_MIN_LEFT) -> set:
    """ASNs that carry traffic in BGP: in some RIS dump (bgp-extractor asn_stats.csv) they have a
    neighbour on the origin side (Right_Count > 0, so they passed routes on) and at least min_left
    neighbours on the collector side. IXP ASNs turn up mid-path only for 1-2 members with
    non-transparent route-server sessions (AMS-IX 6777: 2; France-IX Paris, NIX.CZ, SGIX: 1); Cogent: 107."""
    out = set()
    for path in glob.glob(os.path.join(base_dir, "rrc*", "asn_stats.csv")):
        with open(path) as f:
            next(f, None)
            for line in f:
                p = line.split(",")
                if len(p) >= 3 and p[0].isdigit() and p[1].isdigit() and p[2].strip().isdigit() \
                        and int(p[2]) > 0 and int(p[1]) >= min_left:
                    out.add(int(p[0]))
    return out


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

    The probe's own AS counts when the trace shows a hop inside it (its users reached the host); a
    trace where only the destination answered names nobody (Swisscom, 2026-10-10: in-network Atlas
    tests then showed it dropping the invalid route). Another AS counts when it has >= 2 hops, or
    hands the trace straight to the beacon origin. A single hop between two other
    ASes is usually that AS's address on a border router (third-party address), not transit
    through it: e.g. 2026-01-04, 399078 -> one 3356-numbered hop -> 26042 -> 13335. exclude:
    ASes that can't be forwarders (IXP ASNs, NON_TRANSIT_ASNS).
    """
    out = set()
    for i, (asn, hops) in enumerate(runs):
        nxt = runs[i + 1][0] if i + 1 < len(runs) else None
        if hops >= 2 or nxt == BEACON_ORIGIN or asn == probe_asn:
            out.add(asn)
    return out - {BEACON_ORIGIN, 0} - set(exclude)


def main() -> None:
    t0 = time.time()
    lookup = load_ip2asn()
    probe_asns = load_probe_asns()
    ix, peeringdb_rs, ix_pfx, ix_members = load_ix()
    raw_aspa = json.load(open(os.path.join(rov_utils.DIR_DATA, "aspa_real.json")))
    as0 = {int(k) for k, v in raw_aspa.items() if not set(v) - {0}}
    announcers = ix_announcers(ix_pfx, ix_members, lookup)
    ixps = ixp_asns(peeringdb_rs, as0, announcers, set(rov_utils.TIER_1_ASNS), load_mid_path())
    exclude = ixps | set(rov_utils.NON_TRANSIT_ASNS)
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
    write_report(ev, totals, len(probe_asns), ix is not None, len(ixps))
    print(f"[+] {FILE_EVIDENCE}, {FILE_REPORT} ({time.time() - t0:.0f}s)")


def write_report(ev: dict, totals: Counter, n_probe_meta: int, have_ix: bool = False, n_ixp: int = 0) -> None:
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
             ("IX LAN hops are attributed to the participant holding the address (PeeringDB netixlan). "
              f"{n_ixp:,} IXP ASNs never count as forwarders: at least two of three signals agree (PeeringDB "
              "info_type 'Route Server', AS0 ASPA, announcing an IX LAN prefix while PeeringDB lists it on that "
              "LAN; one alone isn't enough), and the ASN doesn't carry traffic in RIS (an IXP's route servers are "
              "transparent; its ASN is mid-path for at most 2 members with non-transparent sessions). "
              "AS0 on its own means no providers: Cogent, Arelion, AT&T, GTT, Deutsche Telekom and Liberty Global "
              "publish it, which supports their Tier 1 status."
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
