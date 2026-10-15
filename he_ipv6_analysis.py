"""
he_ipv6_analysis.py — what Hurricane Electric's (AS6939) IPv6 peering policy does at scale.

HE sends its full IPv6 table to its peers (Terry's operator knowledge; reports/caida_vs_project.md
measured HE passing peers' IPv6 routes upward 4,435 times against 2 in the other direction). Under
valley-free routing a network passes a peer's routes only to its customers. This script measures,
from the existing extractor output (no new BGP extraction):
  1. share of all RIS paths in which each AS passes a route on (mid-path), per address family;
  2. CAIDA peers whose routes an AS passes to a non-customer (a CAIDA peer or provider, or a
     Tier 1), per AS and address family: the export that makes a peer look like a customer;
  3. ASes whose observed paths mostly or only go through HE, per address family, by their CAIDA
     relationship with HE;
  4. consequences: HE's filtering status in the audit, its cone in our graph, and peers that rely
     on HE in IPv6 while their ASPA record leaves HE out.

Inputs:  output/rrc*/exports.csv (X,C,AF,Paths,Beyond,ToTier1: RIB entries per link),
         output/rrc*/triples.csv (AF,Y,X,C: X passed C's route to Y, distinct, any path position),
         data/caida/<date>.as-rel2.txt.bz2 (labels inferred from IPv4 paths), data/aspa_real.json,
         data/downstream_graph.json, data/asn_meta.json, rov_audit_v22_final.csv
Output:  reports/he_ipv6_peering.md

Usage: python3 he_ipv6_analysis.py
"""
import csv
import glob
import json
import os
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field

import caida_crosscheck as cc
import rov_utils
from caida_export_test import caida_role

HE = 6939
DIR_OUTPUT = "output"
FILE_REPORT = os.path.join("reports", "he_ipv6_peering.md")
SHARE_THRESHOLDS = (0.5, 0.9)
TOP_N = 8


# --- pure helpers (tested) ------------------------------------------------------
@dataclass
class PathTotals:
    paths: Counter = field(default_factory=Counter)                                  # af -> paths
    mid_path: dict = field(default_factory=lambda: defaultdict(Counter))             # af -> x -> paths
    passed_on: dict = field(default_factory=lambda: defaultdict(lambda: defaultdict(Counter)))  # af -> c -> x


def path_totals(rows) -> PathTotals:
    """From exports.csv rows (x, c, af, paths, beyond). Every path with two or more ASes has one
    link at its collector end (paths - beyond), so summing that counts each path once. An AS is
    mid-path in a path when it passed its right neighbour's route on (beyond)."""
    t = PathTotals()
    for x, c, af, paths, beyond in rows:
        t.paths[af] += paths - beyond
        if beyond:
            t.mid_path[af][x] += beyond
            t.passed_on[af][c][x] += beyond
    return t


def shares_via(t: PathTotals, x: int) -> dict:
    """{af: {c: share of the paths where c's route was passed on beyond c's neighbour, that x
    passed on}}. Paths where x is the collector's own peer are left out (HE peers with RIS)."""
    out = {}
    for af, by_c in t.passed_on.items():
        out[af] = {c: xs[x] / sum(xs.values()) for c, xs in by_c.items() if xs.get(x)}
    return out


class TripleStats:
    """Accumulates triples (af, y, x, c): x passed the route it learned from c on to y."""

    def __init__(self, rels: dict, tier1: set):
        self.rels, self.tier1 = rels, set(tier1)
        self.peers_seen = {4: defaultdict(set), 6: defaultdict(set)}      # x -> CAIDA peers c
        self.peers_passed_up = {4: defaultdict(set), 6: defaultdict(set)}  # ... passed to non-customer
        self.passers = {4: defaultdict(set), 6: defaultdict(set)}         # c -> x

    def add(self, af: int, y: int, x: int, c: int) -> None:
        self.passers[af][c].add(x)
        if caida_role(self.rels, x, c) != "peer":
            return
        self.peers_seen[af][x].add(c)
        if y in self.tier1 or caida_role(self.rels, x, y) in ("peer", "provider"):
            self.peers_passed_up[af][x].add(c)

    def only_passed_by(self, x: int, af: int) -> set:
        return {c for c, xs in self.passers[af].items() if xs == {x}}


def aspa_gap(shares: dict, rels: dict, aspa: dict, he: int, threshold: float) -> list:
    """CAIDA peers of he with at least `threshold` of their paths via he whose ASPA record exists
    and doesn't list he: an ASPA-validating network that receives these routes from he (which
    passes them to its peers) finds the hop c -> he unauthorised and drops them."""
    return sorted(c for c, s in shares.items()
                  if s >= threshold and caida_role(rels, he, c) == "peer"
                  and c in aspa and he not in aspa[c])


# --- I/O --------------------------------------------------------------------------
def read_exports(base_dir: str = DIR_OUTPUT):
    for path in sorted(glob.glob(os.path.join(base_dir, "rrc*", "exports.csv"))):
        with open(path) as f:
            reader = csv.reader(f)
            next(reader, None)
            for x, c, af, paths, beyond, _ in reader:
                yield int(x), int(c), int(af), int(paths), int(beyond)


def read_triples(stats: TripleStats, base_dir: str = DIR_OUTPUT) -> None:
    for path in sorted(glob.glob(os.path.join(base_dir, "rrc*", "triples.csv"))):
        with open(path) as f:
            next(f, None)
            for line in f:
                af, y, x, c = line.rstrip("\n").split(",")
                stats.add(int(af), int(y), int(x), int(c))


def role_label(rels: dict, c: int) -> str:
    return {"customer": "HE customer", "peer": "HE peer", "provider": "HE provider",
            None: "no CAIDA link"}[caida_role(rels, HE, c)]


def main() -> None:
    t0 = time.time()
    rels = cc.parse_as_rel2(cc.caida_lines(cc.URL_REL.format(d=cc.DEFAULT_DATE)))
    tier1 = set(rov_utils.TIER_1_ASNS)
    totals = path_totals(read_exports())
    stats = TripleStats(rels, tier1)
    read_triples(stats)
    shares = shares_via(totals, HE)
    aspa = {int(k): set(v) for k, v in json.load(open(os.path.join(rov_utils.DIR_DATA, "aspa_real.json"))).items()}
    meta = json.load(open(os.path.join(rov_utils.DIR_DATA, "asn_meta.json")))
    graph = json.load(open(os.path.join(rov_utils.DIR_DATA, "downstream_graph.json")))
    audit = next((r for r in csv.DictReader(open(rov_utils.FILE_AUDIT_FINAL)) if r["asn"] == str(HE)), {})
    write_report(rels, totals, stats, shares, aspa, meta, graph, audit)
    print(f"[+] {FILE_REPORT} ({time.time() - t0:.0f}s)")


def name(meta: dict, asn: int) -> str:
    m = meta.get(str(asn)) or {}
    return f"{str(m.get('name', ''))[:34]} ({m.get('cc', '')})" if m else ""


def pct(a: float, b: float) -> str:
    return f"{100 * a / b:.1f}%" if b else "-"


def write_report(rels, totals, stats, shares, aspa, meta, graph, audit) -> None:
    roles = ("HE customer", "HE peer", "no CAIDA link")
    caida_cust = sum(1 for (a, b), (r, p) in rels.items() if r == "p2c" and p == HE)
    caida_peers = sum(1 for (a, b), (r, p) in rels.items() if r == "p2p" and HE in (a, b))
    dep = {}
    for af in (4, 6):
        for thr in SHARE_THRESHOLDS:
            dep[(af, thr)] = Counter(role_label(rels, c) for c, s in shares.get(af, {}).items() if s >= thr)
        dep[(af, "only")] = Counter(role_label(rels, c) for c in stats.only_passed_by(HE, af))
    only6 = stats.only_passed_by(HE, 6)
    only6_other4 = {c for c in only6 if stats.passers[4].get(c, set()) - {HE}}
    gap = aspa_gap(shares.get(6, {}), rels, aspa, HE, SHARE_THRESHOLDS[0])
    maj6_peers = [c for c, s in shares.get(6, {}).items() if s >= SHARE_THRESHOLDS[0] and caida_role(rels, HE, c) == "peer"]
    with_aspa = [c for c in maj6_peers if c in aspa]
    he_up = {af: len(stats.peers_passed_up[af].get(HE, ())) for af in (4, 6)}
    he_seen = {af: len(stats.peers_seen[af].get(HE, ())) for af in (4, 6)}
    mid = {af: totals.mid_path[af].get(HE, 0) for af in (4, 6)}
    graph_cust = len(graph.get(str(HE), []))

    L = ["# Hurricane Electric's IPv6 peering at scale", "",
         f"Generated {time.strftime('%Y-%m-%d')} by `he_ipv6_analysis.py` from the RIPE RIS dumps of 11 Oct 2026 "
         f"(rrc00, rrc14, rrc19, rrc23, rrc24; existing `bgp-extractor` output) and CAIDA AS relationships "
         f"{cc.DEFAULT_DATE}. CAIDA infers its labels from IPv4 paths, so \"HE peer\" below means a network "
         "HE peers with in IPv4.", "",
         "## Summary", "",
         f"- **HE is mid-path in {pct(mid[6], totals.paths[6])} of IPv6 paths** seen by RIS "
         f"({mid[6]:,} of {totals.paths[6]:,}), against {pct(mid[4], totals.paths[4])} of IPv4 paths. "
         "No other network passes on more than "
         f"{pct(max(n for x, n in totals.mid_path[6].items() if x != HE), totals.paths[6])} of IPv6 paths.",
         f"- **HE passes its peers' IPv6 routes to its other peers.** In IPv6 it passed the routes of "
         f"{he_up[6]:,} of the {he_seen[6]:,} CAIDA peers seen behind it to a non-customer (another peer, a "
         f"provider or a Tier 1); in IPv4, {he_up[4]:,} of {he_seen[4]:,}. Valley-free routing passes a peer's "
         "routes to customers only, so in IPv6 HE acts as transit for its peers.",
         f"- **Many networks reach the IPv6 Internet mostly through HE.** For "
         f"{sum(dep[(6, 0.5)].values()):,} ASes, HE passed on at least half of their observed IPv6 paths "
         f"({dep[(6, 0.5)]['HE peer']:,} of them HE peers); in IPv4, {sum(dep[(4, 0.5)].values()):,} "
         f"({dep[(4, 0.5)]['HE peer']:,} peers). {len(only6):,} ASes are passed on by HE alone in IPv6; "
         f"{len(only6_other4):,} of these have another network passing their routes in IPv4.",
         f"- **ROV:** the audit rates HE `{audit.get('verdict', '?')}` (decided by {audit.get('decided_by', '?')}, "
         f"APNIC {audit.get('apnic_score', '?')}%). Peers that take HE's IPv6 table get HE's filtering on the "
         "routes they use from it. The audit's topology does not show this (see Consequences).",
         f"- **ASPA:** {len(with_aspa)} of the {len(maj6_peers):,} HE peers that rely on HE for at least half of "
         f"their IPv6 paths publish ASPA; {len(with_aspa) - len(gap)} list HE as a provider and **{len(gap)} leave "
         "it out**. ASPA-validating networks would drop their paths that run through HE.", ""]

    L += ["## 1. Share of paths each network passes on", "",
          "Paths in which the AS passed its right neighbour's route on to another AS (it is mid-path), "
          "out of all paths with two or more ASes. A path counts once per collector peer and prefix.", "",
          "| | IPv4 | | IPv6 | |", "|---|---|---|---|---|", "| rank | AS | share | AS | share |"]
    tops = {af: totals.mid_path[af].most_common(TOP_N) for af in (4, 6)}
    for i in range(TOP_N):
        cells = []
        for af in (4, 6):
            x, n = tops[af][i]
            cells += [f"{x} {name(meta, x)}", pct(n, totals.paths[af])]
        L.append(f"| {i + 1} | " + " | ".join(cells) + " |")
    L += ["", f"Totals: IPv4 {totals.paths[4]:,} paths, IPv6 {totals.paths[6]:,}.", ""]

    L += ["## 2. Peers' routes passed to non-customers", "",
          "Per AS: CAIDA peers whose routes it passed to a CAIDA peer or provider of its own, or to a Tier 1 "
          "(from `triples.csv`, any path position). Valley-free routing never does this; a network that does "
          "it for all its peers is giving them transit. Top networks by IPv6 count:", "",
          "| AS | IPv6 passed up / peers seen | IPv4 passed up / peers seen |", "|---|---|---|"]
    top_x = sorted(stats.peers_seen[6], key=lambda x: -len(stats.peers_passed_up[6].get(x, ())))[:TOP_N]
    for x in top_x:
        cells = [f"{len(stats.peers_passed_up[af].get(x, ())):,} / {len(stats.peers_seen[af].get(x, ())):,}" for af in (6, 4)]
        L.append(f"| {x} {name(meta, x)} | " + " | ".join(cells) + " |")
    L += ["", "The networks after HE pass on every CAIDA peer's route in IPv4 as well, which points to CAIDA "
          "labelling some of their customers as peers rather than to an IPv6-only policy; none comes near "
          "HE's scale.", ""]

    L += ["## 3. Networks whose paths go mostly through HE", "",
          "Share of an AS's paths that HE passed on, out of all paths where its route was passed beyond its "
          "neighbour (paths where HE is the collector's own peer are left out: HE peers with RIS directly). "
          "By the AS's CAIDA relationship with HE:", "",
          "| | IPv4 | | | IPv6 | | |", "|---|---|---|---|---|---|---|",
          "| ASes | " + " | ".join(roles) + " | " + " | ".join(roles) + " |"]
    for key, label in ((0.5, ">= 50% via HE"), (0.9, ">= 90% via HE"), ("only", "only HE passes it on")):
        L.append(f"| {label} | " + " | ".join(f"{dep[(af, key)][r]:,}" for af in (4, 6) for r in roles) + " |")
    L += ["", f"CAIDA lists {caida_cust:,} HE customers and {caida_peers:,} HE peers. In IPv4, HE carries most "
          "paths only for its customers. In IPv6, its peers join them: they get IPv6 transit from HE over "
          "their peering sessions.", ""]

    L += ["## 4. Consequences for this audit", "",
          f"- **Topology.** `HE` is in `EVIDENCE_REQUIRED_ASNS`: path inference counts only its IPv4 triples, "
          f"and a degree-rule customer needs an IPv4 Tier 1 export. Our graph gives HE {graph_cust:,} direct "
          f"customers (CAIDA {caida_cust:,}). Counting IPv6 triples would add HE's peers as customers and "
          "push its cone toward the whole Internet, as it was when HE was a Tier 1 (cone 80,275).",
          "- **ROV.** The audit's dirty-feed logic follows the IPv4 graph. A network that uses HE for IPv6 "
          "gets HE's filtered feed on those routes, which the audit doesn't credit; and a network whose "
          "other providers don't filter is less exposed in IPv6 than its verdict says. This is inferred from "
          "how HE's routes are exported: RIS shows the routes HE passes on, not which routes each peer "
          "installs from HE.",
          f"- **ASPA.** One ASPA record covers IPv4 and IPv6. The {len(gap)} peers below rely on HE for at least "
          "half of their IPv6 paths but leave HE out of their record. Validating networks that receive their "
          "routes from HE (a peer) check the hop to HE and drop those paths. Listing HE fixes IPv6 but also "
          "authorises HE to pass their IPv4 routes upward.", ""]
    if gap:
        L += ["| AS | name | IPv6 share via HE | ASPA providers |", "|---|---|---|---|"]
        for c in sorted(gap, key=lambda c: -shares[6][c]):
            provs = sorted(aspa[c] - {0})
            L.append(f"| {c} | {name(meta, c)} | {shares[6][c]:.0%} | "
                     f"{', '.join(map(str, provs[:6])) or 'AS0'}{' …' if len(provs) > 6 else ''} |")
        L.append("")

    L += ["## Method and limits", "",
          "- RIS sees paths from its collector peers only, so shares describe those views, not traffic.",
          "- CAIDA's labels come from IPv4 paths; where a network has a real IPv6 transit contract with HE "
          "it still counts as an HE peer here. That is the effect being measured.",
          "- `triples.csv` is distinct per collector (no path counts); `exports.csv` counts RIB entries.",
          "- No new BGP extraction was run (Terry, 2026-10-15). Related: `reports/caida_vs_project.md` "
          "(last-three-hop test, ASPA counts for HE's upward exports)."]
    with open(FILE_REPORT, "w") as fh:
        fh.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
