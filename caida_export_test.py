"""
caida_export_test.py — test CAIDA's AS relationships (and signed ASPA) against observed exports.

For a RIS path ending `Y X C` (C = origin), X passed C's route to Y. If Y is not X's customer,
valley-free routing says C is X's customer (or the export is a route leak). Two tests:
  strict     Y is in the tested Tier 1 clique (rov_utils.TIER_1_ASNS) and X is not. Independent
             of CAIDA.
  via label  CAIDA labels Y as X's provider or peer. Leans on CAIDA's label for another link,
             so it is reported separately.
`down` means X passed C's route only to CAIDA-labelled customers, which fits any relationship.

It also counts, per origin with HE (AS6939) exporting its route upward, what ASPA verification
(draft-ietf-sidrops-aspa-verification) at the receiving network would do: the receiver applies
upstream verification to a route from a peer or customer, so the hop C→HE is checked against
C's ASPA. ASPA has one provider set for IPv4 and IPv6.

Input: last-three-hop triples, one file per collector, lines `af y x c` (`_` for y when the
path has two ASes), written by `extract()` from output/rrc*-bview.gz with bgpdump.
Output: tables on stdout, written up in reports/caida_vs_project.md.

Usage: python3 caida_export_test.py [--extract] [--triples DIR]
"""
import argparse
import glob
import json
import os
import subprocess
from collections import Counter, defaultdict

import caida_crosscheck as cc
import rov_utils

HE = 6939
DIR_OUTPUT = "output"
AWK = (r"""$7 !~ /[{}]/ { af = index($6, ":") ? 6 : 4; n = split($7, a, " "); m = 0; """
       r"""for (i = 1; i <= n; i++) if (m == 0 || b[m] != a[i]) b[++m] = a[i]; """
       r"""if (m >= 3) print af, b[m-2], b[m-1], b[m]; else if (m == 2) print af, "_", b[1], b[2] }""")
VERDICTS = ("provider (strict)", "provider (via CAIDA label)", "only passed down", "not seen")


# --- pure helpers (tested) ------------------------------------------------------
def caida_role(rels: dict, a: int, b: int):
    """CAIDA's view of b relative to a: 'provider' (b provides a), 'customer', 'peer' or None."""
    r = rels.get((min(a, b), max(a, b)))
    if r is None:
        return None
    if r[0] == "p2p":
        return "peer"
    return "provider" if r[1] == b else "customer"


def export_classes(y: int, x: int, rels: dict, tier1: set) -> list[str]:
    """Classes one observed export of an origin's route by x to y falls into."""
    out = []
    if y in tier1 and x not in tier1:
        out.append("up_strict")
    role = caida_role(rels, x, y)
    if role in ("provider", "peer"):
        out.append("up_caida")
    elif role == "customer":
        out.append("down")
    return out


def verdict(counts: Counter | None) -> str:
    if not counts:
        return "not seen"
    if counts["up_strict"]:
        return "provider (strict)"
    if counts["up_caida"]:
        return "provider (via CAIDA label)"
    return "only passed down"


def aspa_outcome(customer: int, provider: int, aspa: dict) -> str:
    """ASPA upstream verification of the hop customer→provider at a validating receiver."""
    if customer not in aspa:
        return "no ASPA: Unknown, kept"
    if provider in aspa[customer]:
        return "ASPA lists it: Valid"
    return "ASPA omits it: Invalid, dropped"


# --- I/O --------------------------------------------------------------------------
def extract(out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    procs = []
    for rrc in rov_utils.RRC_COLLECTORS:
        src = os.path.join(DIR_OUTPUT, f"{rrc}-bview.gz")
        cmd = f"bgpdump -m {src} 2>/dev/null | awk -F'|' '{AWK}' | sort -u > {out_dir}/{rrc}.triples"
        procs.append(subprocess.Popen(["bash", "-c", cmd]))
    for p in procs:
        p.wait()


def load_exports(triples_dir: str, rels: dict, tier1: set) -> dict:
    """{af: {(x, c): Counter(class)}}"""
    exports = {4: defaultdict(Counter), 6: defaultdict(Counter)}
    for f in glob.glob(os.path.join(triples_dir, "*.triples")):
        with open(f) as fh:
            for line in fh:
                af, y, x, c = line.split()
                if y == "_":
                    continue
                y, x, c = int(y), int(x), int(c)
                for k in export_classes(y, x, rels, tier1):
                    exports[int(af)][(x, c)][k] += 1
    return exports


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", action="store_true", help="re-extract triples from the bview dumps")
    ap.add_argument("--triples", default=os.path.join(DIR_OUTPUT, "triples"))
    args = ap.parse_args()
    if args.extract:
        extract(args.triples)
    rels = cc.parse_as_rel2(cc.caida_lines(cc.URL_REL.format(d=cc.DEFAULT_DATE)))
    exports = load_exports(args.triples, rels, set(rov_utils.TIER_1_ASNS))
    raw = json.load(open(os.path.join(rov_utils.DIR_DATA, "aspa_real.json")))
    aspa = {int(k): set(v) - {0} for k, v in raw.items()}

    prov, peer = defaultdict(set), defaultdict(set)
    for (a, b), (r, p) in rels.items():
        if r == "p2c":
            prov[b if p == a else a].add(p)
        else:
            peer[a].add(b)
            peer[b].add(a)

    for af in (4, 6):
        ex = exports[af]
        v = lambda x, c: verdict(ex.get((x, c)))  # noqa: E731
        print(f"\n===== IPv{af} =====")
        a_ = Counter(v(x, c) for c, p in aspa.items() if p for x in prov.get(c, set()) - p)
        print("A. CAIDA p2c, provider missing from the customer's ASPA:", dict(a_))
        pairs_b = [(x, c) for c, p in aspa.items() if p for x in peer.get(c, set()) & p]
        print("B. ASPA provider, CAIDA p2p:", dict(Counter(v(x, c) for x, c in pairs_b)))
        print("   of which HE:", dict(Counter(v(x, c) for x, c in pairs_b if x == HE)))
        c_all, c_he, d_ = Counter(), Counter(), Counter()
        for (a, b), (r, p) in rels.items():
            if r == "p2p":
                for x, c in ((a, b), (b, a)):
                    if (x, c) in ex:
                        c_all[v(x, c)] += 1
                        if x == HE:
                            c_he[v(x, c)] += 1
            elif (p, b if p == a else a) in ex:
                d_[v(p, b if p == a else a)] += 1
        print("C. CAIDA p2p links tested:", dict(c_all), " HE as X:", dict(c_he))
        print("D. CAIDA p2c links tested:", dict(d_))

        up = [c for (x, c), k in ex.items() if x == HE and (k["up_strict"] or k["up_caida"])]
        he_cust = {c for c in up if caida_role(rels, c, HE) == "provider"}
        for label, group in (("CAIDA: HE's customer", he_cust), ("CAIDA: HE's peer or no link",
                                                                 set(up) - he_cust)):
            print(f"E. HE exports origin upward, {label} ({len(group)}):",
                  dict(Counter(aspa_outcome(c, HE, aspa) for c in group)))


if __name__ == "__main__":
    main()
