"""
caida_crosscheck.py — compare our inferred topology with CAIDA's AS relationships, link by
link, and attribute every disagreement to the inference rule that produced it.

Inputs: output/rrc*/relationships.csv (via build_topology_from_go.load_multi_collector_relationships),
data/downstream_graph.json, rov_audit_v22_final.csv (Go cone sizes), and CAIDA's monthly
serial-2 as-rel2 and serial-1 ppdc-ases files in data/caida/ (downloaded when missing).

Each observed link is labelled with the rule build_topology_from_go.build_graph ends with
(tier1, ratio_4x, restored, peer, single_region, t1_t1, non_transit, pruned,
evidence_required) and compared with CAIDA (same direction, reversed, peer, absent). Report: reports/caida_crosscheck.md.

Usage: python3 caida_crosscheck.py [--date YYYYMMDD]
"""
import argparse
import bz2
import json
import os
from collections import Counter, defaultdict, deque

import requests

import build_topology_from_go as btg
import rov_utils

URL_REL = "https://publicdata.caida.org/datasets/as-relationships/serial-2/{d}.as-rel2.txt.bz2"
URL_PPDC = "https://publicdata.caida.org/datasets/as-relationships/serial-1/{d}.ppdc-ases.txt.bz2"
DEFAULT_DATE = "20261001"
CLASSES = ("caida_same", "caida_reversed", "caida_p2p", "caida_p2c", "caida_absent")


# --- pure helpers (tested) ------------------------------------------------------
def parse_as_rel2(lines) -> dict:
    """{(min_asn, max_asn): ("p2c", provider) | ("p2p", None)}"""
    rels = {}
    for line in lines:
        if not line or line.startswith("#"):
            continue
        a, b, r = line.split("|")[:3]
        a, b = int(a), int(b)
        rels[(min(a, b), max(a, b))] = ("p2c", a) if r == "-1" else ("p2p", None)
    return rels


def parse_ppdc(lines) -> dict:
    """{asn: customer-cone size incl. itself} from a ppdc-ases file."""
    out = {}
    for line in lines:
        if line and not line.startswith("#"):
            parts = line.split()
            out[int(parts[0])] = len(parts) - 1
    return out


def compare(provider, customer, rels: dict, pair: tuple | None = None) -> str:
    """CAIDA's view of one link we labelled provider→customer (or dropped, with pair given)."""
    key = tuple(sorted(pair if provider is None else (provider, customer)))
    c = rels.get(key)
    if c is None:
        return "caida_absent"
    if c[0] == "p2p":
        return "caida_p2p"
    if provider is None:
        return "caida_p2c"
    return "caida_same" if c[1] == provider else "caida_reversed"


def cone_size(asn: int, down: dict) -> int:
    seen, q = {asn}, deque([asn])
    while q:
        for c in down.get(q.popleft(), []):
            if c not in seen:
                seen.add(c)
                q.append(c)
    return len(seen)


# --- I/O --------------------------------------------------------------------------
def caida_lines(url: str) -> list[str]:
    path = os.path.join(rov_utils.DIR_CAIDA, os.path.basename(url))
    if not os.path.exists(path):
        os.makedirs(rov_utils.DIR_CAIDA, exist_ok=True)
        resp = requests.get(url, headers=rov_utils.HEADERS, timeout=300)
        resp.raise_for_status()
        with open(path, "wb") as f:
            f.write(resp.content)
    with bz2.open(path, "rt") as f:
        return f.read().splitlines()


def label_links(adj: dict, degrees: dict, link_regions: dict, evidence: dict | None) -> tuple[dict, dict]:
    """{pair: (provider, customer, rule)} for every observed link, and the final graph."""
    down, labels = btg.build_graph(adj, degrees, link_regions, evidence)
    return labels, down


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=DEFAULT_DATE)
    args = ap.parse_args()
    rels = parse_as_rel2(caida_lines(URL_REL.format(d=args.date)))
    ppdc = parse_ppdc(caida_lines(URL_PPDC.format(d=args.date)))
    adj, degrees, link_regions = btg.load_multi_collector_relationships()
    labels, final = label_links(adj, degrees, link_regions, btg.load_exports())

    saved = json.load(open(os.path.join(rov_utils.DIR_DATA, "downstream_graph.json")))
    saved_links = {(int(p), c) for p, cs in saved.items() for c in cs}
    final_links = {(p, c) for p, cs in final.items() for c in cs}
    same_as_saved = saved_links == final_links
    print(f"[*] rebuilt graph == downstream_graph.json: {same_as_saved} "
          f"({len(final_links):,} vs {len(saved_links):,} links)")

    matrix: dict = defaultdict(Counter)
    for pair, (p, c, rule) in labels.items():
        matrix[rule][compare(p, c, rels, pair=pair)] += 1
    unseen = Counter(r[0] for k, r in rels.items() if k not in labels)

    write_report(args.date, rels, ppdc, labels, final, matrix, unseen, same_as_saved)


def write_report(date, rels, ppdc, labels, final, matrix, unseen, same_as_saved) -> None:
    audit = rov_utils.load_audit_csv().set_index("asn")
    lines = [f"# Topology cross-check against CAIDA AS relationships ({date})", "",
             f"Observed links: {len(labels):,}. CAIDA links: {len(rels):,} "
             f"({unseen['p2c']:,} p2c and {unseen['p2p']:,} p2p of them never seen by our collectors). "
             f"Rebuilt graph identical to downstream_graph.json: **{same_as_saved}**.", "",
             "## Our rule vs CAIDA, per observed link", "",
             "| our rule | links | " + " | ".join(CLASSES) + " |", "|---|---|" + "---|" * len(CLASSES)]
    for rule in sorted(matrix, key=lambda r: -sum(matrix[r].values())):
        n = sum(matrix[rule].values())
        lines.append(f"| {rule} | {n:,} | " + " | ".join(
            f"{matrix[rule][k]:,} ({100 * matrix[rule][k] / n:.0f}%)" for k in CLASSES) + " |")
    lines += ["", "Kept p2c rules (tier1, ratio_4x, restored) should land in caida_same; dropped rules "
              "(peer, single_region, t1_t1, non_transit) in caida_p2p or caida_absent. pruned and "
              "evidence_required are p2c candidates we removed: caida_same there is a lost link.", ""]

    def row(asn):
        name = str(audit.name.get(asn, ""))[:28]
        return (f"| {asn} | {name} | {audit.cc.get(asn, '')} | {audit.cone.get(asn, '')} | "
                f"{cone_size(asn, final) - 1} | {ppdc.get(asn, 1) - 1} |")
    head = ["| AS | name | cc | audit cone (Go, rrc00) | our graph cone | CAIDA cone |",
            "|---|---|---|---|---|---|"]
    top = sorted(ppdc, key=lambda a: -ppdc[a])[:25]
    lines += ["## Cone sizes: CAIDA's 25 largest", ""] + head + [row(a) for a in top]
    nz = [a for a in audit.index if audit.cc.get(a) == "NZ" and ppdc.get(a, 1) > 1]
    nz = sorted(nz, key=lambda a: -ppdc[a])[:25]
    lines += ["", "## Cone sizes: NZ (CAIDA cone > 0)", ""] + head + [row(a) for a in nz]

    lines += ["", "## NZ customer links CAIDA has and we don't", "",
              "| provider | customer | our rule for the link |", "|---|---|---|"]
    for a in nz[:12]:
        caida_cust = [b if k[0] == a else k[0] for k, r in rels.items()
                      if r[0] == "p2c" and r[1] == a for b in [k[1]]]
        ours = set(final.get(a, []))
        for b in sorted(set(caida_cust) - ours)[:15]:
            lab = labels.get((min(a, b), max(a, b)))
            lines.append(f"| {a} | {b} | {lab[2] if lab else 'not observed'} |")
    path = os.path.join("reports", "caida_crosscheck.md")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[+] {path}")


if __name__ == "__main__":
    main()
