"""
globalping_report.py — the two Globalping shadow-mode reports (globalping_verify.py
--coverage / --compare). Neither creates a measurement.

  reports/globalping_coverage.md   what Globalping's probes reach, from GET /v1/probes
  reports/globalping_vs_atlas.md   agreement with RIPE Atlas results no more than 7 days
                                   apart, and the pass criteria of plan/globalping_plan.md
                                   section 7 as PASS / NOT YET

Globalping results are not used in verdicts; --compare is the evidence for that decision.
"""
from __future__ import annotations

import bz2
import glob
import json
import logging
import os
import time
from collections import Counter, defaultdict
from datetime import datetime

import globalping_client as gp
import globalping_verify as gv

logger = logging.getLogger(__name__)

MAX_GAP_DAYS = gv.TTL_DAYS
PACIFIC = ("NZ", "FJ", "PG", "SB", "VU", "WS", "TO", "CK", "KI", "TV", "NR", "NU", "FM", "MH", "PW", "MP", "TK",
           "WF", "TL", "GU", "NC", "PF", "AS")
# Plan section 7. A percentage with nothing to count is NOT YET, never a pass.
MIN_SAMPLE, MIN_PER_CLASS = 60, 25
MIN_OVERALL, MIN_SECURE_CONFIRMED, MIN_VULNERABLE_CONFIRMED = 95.0, 90.0, 95.0
MIN_REPEATS, MIN_REPEAT_SAME = 20, 95.0
REPEAT_GAP_HOURS = (12, 48)


def _pct(n: int, d: int) -> str:
    return f"{100 * n / d:.1f}% ({n}/{d})" if d else f"n/a ({n}/{d})"


def _names(paths: gv.Paths) -> dict[int, dict]:
    return {int(k): v for k, v in (gv._read_json(os.path.join(paths.data, "asn_meta.json"), {}) or {}).items()}


# ── Coverage ─────────────────────────────────────────────────────────────────

def load_atlas_probe_asns(paths: gv.Paths) -> tuple[set[int], str]:
    """(ASNs with a connected IPv4 Atlas probe, archive day) from the newest probe archive."""
    files = sorted(glob.glob(os.path.join(paths.atlas, "probes", "*.json.bz2")))
    if not files:
        return set(), "none"
    with bz2.open(files[-1], "rt") as fh:
        data = json.load(fh)
    probes = data.get("objects", data) if isinstance(data, dict) else data
    asns = {int(p["asn_v4"]) for p in probes if p.get("status") == 1 and p.get("asn_v4")}
    return asns, os.path.basename(files[-1]).split(".")[0]


def coverage_stats(probes: list[dict], downstream: dict, meta: dict, atlas_asns: set[int],
                   atlas_results: dict, no_probe_asns: list[int]) -> dict:
    """Counts for the coverage report. Reach rule as find_best_probes_in_cone: target or direct customer."""
    by_asn = gv.probes_by_asn(probes)
    tags = Counter(gv.network_type(p.get("tags") or []) for p in probes)
    dc_only = sum(1 for ps in by_asn.values() if all(gv.network_type(p.get("tags") or []) == "datacenter" for p in ps))
    eyeball = {a: ps for a, ps in by_asn.items() if gv._has_eyeball(ps)}
    transit = [a for a, m in meta.items() if (m.get("cone") or 0) > 0]

    def testable(asn: int, have) -> bool:
        return asn in have or any(c in have for c in downstream.get(asn, []))

    t_gp = {a for a in transit if testable(a, by_asn)}
    t_eye = {a for a in transit if testable(a, eyeball)}
    t_atlas = {a for a in transit if testable(a, atlas_asns)}
    reach = {a: gv.reachable(a, by_asn, downstream) for a in no_probe_asns}
    fresh = {a: r for a, r in atlas_results.items() if gv.age_days(r) <= gv.TTL_DAYS}
    by_class: dict = defaultdict(Counter)
    for a, r in fresh.items():
        by_class[gv.verdict_class(r.get("verdict")) or "INCONCLUSIVE"][gv.reachable(a, by_asn, downstream) or "none"] += 1
    countries = []
    for cc in PACIFIC:
        here = [p for p in probes if (p.get("location") or {}).get("country") == cc]
        asns = {int(p["location"]["asn"]) for p in here if p["location"].get("asn")}
        countries.append({"cc": cc, "meta_asns": sum(1 for m in meta.values() if m.get("cc") == cc),
                          "probes": len(here), "asns": sorted(asns), "new": sorted(asns - atlas_asns)})
    return {"probes": len(probes), "asns": len(by_asn),
            "countries": len({(p.get("location") or {}).get("country") for p in probes}),
            "tags": dict(tags), "dc_only_asns": dc_only, "single_probe_asns": sum(1 for v in by_asn.values() if len(v) == 1),
            "also_atlas": len(set(by_asn) & atlas_asns), "not_atlas": len(set(by_asn) - atlas_asns),
            "transit": len(transit), "t_gp": len(t_gp), "t_eye": len(t_eye), "t_atlas": len(t_atlas),
            "t_both": len(t_gp & t_atlas), "t_gp_only": sorted(t_gp - t_atlas, key=lambda a: -(meta[a].get("cone") or 0)),
            "t_gp_only_eye": len((t_gp - t_atlas) & t_eye), "no_probes": reach, "fresh": {k: dict(v) for k, v in by_class.items()},
            "pacific": countries}


def write_coverage(paths: gv.Paths, probes: list[dict] | None = None) -> str:
    probes = probes if probes is not None else gp.fetch_probes(gp.load_token())
    gv.save_probe_list(paths, probes)
    downstream, _ = gv.load_graph(paths)
    meta = _names(paths)
    atlas_asns, archive_day = load_atlas_probe_asns(paths)
    no_probes = sorted(int(a) for a in gv.load_dated(os.path.join(paths.atlas, "no_probes.json")))
    s = coverage_stats(probes, downstream, meta, atlas_asns, gv.load_results(paths.atlas), no_probes)
    name = lambda a: (meta.get(a, {}).get("name") or "")[:32]  # noqa: E731
    inside = [a for a, r in s["no_probes"].items() if r == "inside"]
    cust = [a for a, r in s["no_probes"].items() if r == "customer"]
    lines = [
        "# Globalping probe coverage", "",
        f"Generated {time.strftime('%Y-%m-%d')} by `globalping_verify.py --coverage` from `GET /v1/probes` (no test "
        "cost). Globalping is in shadow mode: its results are not used in verdicts. A probe's AS is Globalping's "
        f"GeoIP reading, not BGP. Atlas side: connected IPv4 probes in the probe archive of {archive_day}.", "",
        "| | |", "|---|---|",
        f"| Probes online | {s['probes']:,} |", f"| ASNs | {s['asns']:,} |", f"| Countries | {s['countries']:,} |",
        f"| Datacenter probes | {s['tags'].get('datacenter', 0):,} |",
        f"| Eyeball probes | {s['tags'].get('eyeball', 0):,} |",
        f"| ASNs with datacenter probes only | {s['dc_only_asns']:,} |",
        f"| ASNs with a single probe | {s['single_probe_asns']:,} |",
        f"| ASNs that also have an Atlas probe | {s['also_atlas']:,} |",
        f"| ASNs with no Atlas probe | {s['not_atlas']:,} |", "",
        "## Transit ASes (cone > 0) testable from a probe inside or in a direct customer", "",
        "| Testable by | ASes |", "|---|---|",
        f"| All transit ASes | {s['transit']:,} |", f"| Atlas | {s['t_atlas']:,} |", f"| Globalping | {s['t_gp']:,} |",
        f"| Globalping, eyeball probes only | {s['t_eye']:,} |", f"| Both | {s['t_both']:,} |",
        f"| Globalping only | {len(s['t_gp_only']):,} ({s['t_gp_only_eye']:,} with eyeball probes) |", "",
        "Largest Globalping-only transit ASes:", "", "| AS | name | cc | cone |", "|---|---|---|---|"]
    lines += [f"| {a} | {name(a)} | {meta[a].get('cc', '')} | {meta[a].get('cone') or 0:,} |" for a in s["t_gp_only"][:20]]
    lines += ["", "## ASes Atlas found without usable probes (`data/atlas/no_probes.json`)", "",
              f"{len(s['no_probes'])} ASNs in the list. Globalping has a probe inside {len(inside)} "
              f"({', '.join(f'{a} {name(a)}' for a in inside) or 'none'}) and in a direct customer of {len(cust)} "
              f"more ({', '.join(f'{a} {name(a)}' for a in cust) or 'none'}).", "",
              f"## Fresh Atlas results (<= {gv.TTL_DAYS} days) Globalping can also test", "",
              "This is the validation sample. SECURE is the scarce class.", "",
              "| Atlas result | probe inside | probe in a direct customer | no probe |", "|---|---|---|---|"]
    for cls in ("SECURE", "VULNERABLE", "INCONCLUSIVE"):
        c = s["fresh"].get(cls, {})
        lines.append(f"| {cls} | {c.get('inside', 0)} | {c.get('customer', 0)} | {c.get('none', 0)} |")
    lines += ["", "## NZ and the Pacific (probes by the probe's country)", "",
              "| cc | ASNs registered there | Globalping probes | Globalping ASNs | of them without an Atlas probe |",
              "|---|---|---|---|---|"]
    for c in s["pacific"]:
        if c["probes"]:
            new = ", ".join(f"{a} {name(a)}" for a in c["new"]) or "0"
            lines.append(f"| {c['cc']} | {c['meta_asns']} | {c['probes']} | {len(c['asns'])} | {new} |")
    lines += ["", "No probes: " + ", ".join(c["cc"] for c in s["pacific"] if not c["probes"]) + ".", ""]
    os.makedirs(paths.reports, exist_ok=True)
    out = os.path.join(paths.reports, "globalping_coverage.md")
    with open(out, "w") as fh:
        fh.write("\n".join(lines))
    logger.info("[+] %s (%d probes, %d ASNs)", out, s["probes"], s["asns"])
    return out


# ── Comparison with Atlas ────────────────────────────────────────────────────

def atlas_adjusted(result: dict) -> str:
    """An Atlas result's verdict with the beacon origin ruled out as the drop point, from its
    stored probe details (the same rule as gv.origin_adjusted)."""
    details = [d for d in result.get("probe_details") or [] if d.get("verdict")]
    if not details:
        return result.get("verdict", "")
    asn = int(result["asn"])
    return gv.aggregate_verdict(dict(Counter(gv.origin_adjusted(asn, d) for d in details)))


def probe_class(verdict: str) -> str | None:
    """What one probe says about the target: VULNERABLE, SECURE, or None (nothing)."""
    if verdict in ("VULNERABLE", "SECURE (Upstream Filtered)"):
        return "VULNERABLE"
    return "SECURE" if verdict == "SECURE (Target Filtered)" else None


def build_pairs(gp_results: dict, atlas_results: dict, max_gap_days: float = MAX_GAP_DAYS) -> list[dict]:
    """One row per AS with both results no more than max_gap_days apart."""
    rows = []
    for asn, g in sorted(gp_results.items()):
        a = atlas_results.get(asn)
        if not a:
            continue
        try:
            gap = abs((datetime.fromisoformat(g["timestamp"]) - datetime.fromisoformat(a["timestamp"])).total_seconds())
        except (KeyError, ValueError, TypeError):
            continue
        if gap > max_gap_days * 86400:
            continue
        rows.append({"asn": asn, "gap_days": gap / 86400, "gp": g, "atlas": a,
                     "gp_class": gv.verdict_class(g["verdict"]), "atlas_class": gv.verdict_class(a["verdict"]),
                     "gp_class_adj": gv.verdict_class(g.get("verdict_origin_adjusted") or g["verdict"]),
                     "atlas_class_adj": gv.verdict_class(atlas_adjusted(a))})
    return rows


def repeatability(runs: list[dict]) -> tuple[int, int]:
    """(targets re-run 12-48 h apart with a conclusive verdict both times, of them with the same class)."""
    by_asn: dict = defaultdict(list)
    for r in runs:
        try:
            by_asn[int(r["asn"])].append((datetime.fromisoformat(r["timestamp"]), gv.verdict_class(r["verdict"])))
        except (KeyError, ValueError, TypeError):
            continue
    n = same = 0
    lo, hi = (h * 3600 for h in REPEAT_GAP_HOURS)
    for seq in by_asn.values():
        seq.sort(key=lambda x: x[0])
        for (t1, c1), (t2, c2) in zip(seq, seq[1:]):
            if c1 and c2 and lo <= (t2 - t1).total_seconds() <= hi:
                n += 1
                same += c1 == c2
                break
    return n, same


def evaluate(pairs: list[dict], repeats: tuple[int, int], suffix: str = "") -> list[dict]:
    """The section 7 criteria on ASes conclusive on both sides. suffix "_adj" uses the
    origin-adjusted verdicts. Each row: name, need, got, ok."""
    g, a = "gp_class" + suffix, "atlas_class" + suffix
    both = [p for p in pairs if p[g] and p[a]]
    n = len(both)
    n_sec = sum(1 for p in both if p[a] == "SECURE")
    n_vul = n - n_sec
    agree = sum(1 for p in both if p[g] == p[a])
    gp_sec = [p for p in both if p[g] == "SECURE"]
    gp_vul = [p for p in both if p[g] == "VULNERABLE"]
    sec_ok = sum(1 for p in gp_sec if p[a] == "SECURE")
    vul_ok = sum(1 for p in gp_vul if p[a] == "VULNERABLE")
    rep_n, rep_same = repeats

    def share(k: int, d: int, need: float) -> bool:
        return d > 0 and 100 * k / d >= need

    return [
        {"name": "Sample", "need": f">= {MIN_SAMPLE} ASes, >= {MIN_PER_CLASS} Atlas-SECURE and >= {MIN_PER_CLASS} "
                                   "Atlas-VULNERABLE",
         "got": f"{n} ASes: {n_sec} Atlas-SECURE, {n_vul} Atlas-VULNERABLE",
         "ok": n >= MIN_SAMPLE and n_sec >= MIN_PER_CLASS and n_vul >= MIN_PER_CLASS},
        {"name": "Overall agreement", "need": f">= {MIN_OVERALL:.0f}%", "got": _pct(agree, n),
         "ok": share(agree, n, MIN_OVERALL)},
        {"name": "Globalping SECURE confirmed by Atlas", "need": f">= {MIN_SECURE_CONFIRMED:.0f}%",
         "got": _pct(sec_ok, len(gp_sec)), "ok": share(sec_ok, len(gp_sec), MIN_SECURE_CONFIRMED)},
        {"name": "Globalping VULNERABLE confirmed by Atlas", "need": f">= {MIN_VULNERABLE_CONFIRMED:.0f}%",
         "got": _pct(vul_ok, len(gp_vul)), "ok": share(vul_ok, len(gp_vul), MIN_VULNERABLE_CONFIRMED)},
        {"name": "Repeatability", "need": f">= {MIN_REPEATS} targets re-run 24 h later, >= {MIN_REPEAT_SAME:.0f}% same",
         "got": _pct(rep_same, rep_n), "ok": rep_n >= MIN_REPEATS and share(rep_same, rep_n, MIN_REPEAT_SAME)},
    ]


def passed(criteria: list[dict]) -> bool:
    return all(c["ok"] for c in criteria)


def probe_split(pairs: list[dict]) -> dict:
    """Per (network type, relation): probes, no data, off-path, conclusive, agreeing with Atlas's AS verdict."""
    out: dict = defaultdict(Counter)
    for p in pairs:
        for d in p["gp"].get("probe_details") or []:
            row = out[(d.get("network_type", "unknown"), d.get("relation", "other"))]
            row["probes"] += 1
            row["no_data"] += bool(d.get("no_data"))
            row["off_path"] += "Off-Path" in d["verdict"]
            cls = probe_class(d["verdict"])
            if cls and p["atlas_class"]:
                row["conclusive"] += 1
                row["agree"] += cls == p["atlas_class"]
    return out


def _probe_line(d: dict) -> str:
    where = f"{d.get('probe', {}).get('city')}, {d.get('probe', {}).get('country')} AS{d.get('probe', {}).get('asn')}"
    extra = f"; no data: {d['no_data']}" if d.get("no_data") else ""
    flag = " (drop point named as AS13335)" if d.get("origin_boundary") else ""
    return (f"    - probe {d.get('result_index')} ({where}, {d.get('network_type')}, {d.get('relation')}): "
            f"{d['verdict']}{flag}; valid path {d.get('path_v')}, invalid path {d.get('path_i')}{extra}")


def render_compare(pairs: list[dict], runs: list[dict], names: dict, n_gp: int) -> tuple[str, dict]:
    repeats = repeatability(runs)
    crit, crit_adj = evaluate(pairs, repeats), evaluate(pairs, repeats, "_adj")
    ok, ok_adj = passed(crit), passed(crit_adj)
    word = lambda b: "PASS" if b else "NOT YET"  # noqa: E731
    both = [p for p in pairs if p["gp_class"] and p["atlas_class"]]
    disagree = [p for p in both if p["gp_class"] != p["atlas_class"]]
    disagree_adj = [p for p in pairs if p["gp_class_adj"] and p["atlas_class_adj"]
                    and p["gp_class_adj"] != p["atlas_class_adj"]]
    matrix = Counter((p["gp_class"] or "INCONCLUSIVE", p["atlas_class"] or "INCONCLUSIVE") for p in pairs)
    hop_diff = Counter()
    hops_checked = 0
    for p in pairs:
        for d in p["gp"].get("probe_details") or []:
            hops_checked += len({h[0] for h in (d.get("hops_v") or []) + (d.get("hops_i") or []) if h[0] and h[1]})
            for x in d.get("hop_asn_disagreements") or []:
                hop_diff[(x["local"], tuple(x["globalping"]), x["ix_lan"])] += 1
    lines = [
        "# Globalping vs RIPE Atlas", "",
        f"Generated {time.strftime('%Y-%m-%d')} by `globalping_verify.py --compare`. Globalping is in shadow mode: "
        "its results are **not used in verdicts**. This report decides whether they may be "
        "(`plan/globalping_plan.md` section 7).", "",
        f"**Result: {word(ok)}** (verdicts as `_classify_probe` gives them). With the beacon origin ruled out as a "
        f"drop point on both sides: {word(ok_adj)}.", "",
        f"{n_gp} Globalping results; {len(pairs)} have an Atlas result no more than {MAX_GAP_DAYS} days apart; "
        f"{len(both)} are conclusive on both sides; {len(both) - len(disagree)} agree.", "",
        "## Pass criteria", "",
        "| Criterion | Threshold | As classified | | Origin ruled out | |", "|---|---|---|---|---|---|"]
    for c, c2 in zip(crit, crit_adj):
        lines.append(f"| {c['name']} | {c['need']} | {c['got']} | {word(c['ok'])} | {c2['got']} | {word(c2['ok'])} |")
    lines += ["",
              "\"Origin ruled out\": `_classify_probe` names the first AS of the valid path that the invalid trace did "
              "not reach as the drop point. When that AS is Cloudflare (AS13335, the origin of both beacons) and the "
              "invalid trace ended inside the target, the probe is read as SECURE (Upstream Filtered), which counts "
              "against the target. The second pair of columns reads those probes as SECURE (Target Filtered), on the "
              "Atlas side too. Which reading is right is an open decision (TODO.md).", "",
              "## Globalping against Atlas, AS level", "",
              "| Globalping \\ Atlas | SECURE | VULNERABLE | INCONCLUSIVE |", "|---|---|---|---|"]
    for g in ("SECURE", "VULNERABLE", "INCONCLUSIVE"):
        lines.append(f"| {g} | " + " | ".join(str(matrix[(g, a)]) for a in ("SECURE", "VULNERABLE", "INCONCLUSIVE")) + " |")
    lines += ["", "## By probe type", "",
              "Each Globalping probe against the Atlas verdict for the AS. A probe is conclusive when it reads "
              "VULNERABLE, SECURE (Target Filtered) or SECURE (Upstream Filtered).", "",
              "| Network | Probe is | probes | no data | off-path | conclusive | agree with Atlas |",
              "|---|---|---|---|---|---|---|"]
    for (ntype, rel), r in sorted(probe_split(pairs).items()):
        lines.append(f"| {ntype} | {rel} | {r['probes']} | {r['no_data']} | {r['off_path']} | {r['conclusive']} | "
                     f"{_pct(r['agree'], r['conclusive'])} |")
    lines += ["", "## Disagreements", "",
              f"{len(disagree)} as classified; {len(disagree_adj)} with the origin ruled out "
              f"({', '.join(str(p['asn']) for p in disagree_adj) or 'none'}). Each one needs reading at trace level: "
              "Globalping fault, Atlas fault, or a real difference. Globalping measurements: "
              "`https://api.globalping.io/v1/measurements/<id>`; Atlas: `https://atlas.ripe.net/measurements/<id>/`.", ""]
    for p in disagree:
        g, a = p["gp"], p["atlas"]
        ids = a.get("measurement_ids") or {}
        lines += [f"- **AS{p['asn']} {(names.get(p['asn'], {}).get('name') or '')[:40]}** "
                  f"({p['gap_days']:.1f} days apart)",
                  f"  - Atlas: {a['verdict']} ({a['timestamp'][:10]}; origin ruled out: {atlas_adjusted(a)}); "
                  f"trace_valid {ids.get('trace_valid')}, trace_invalid {ids.get('trace_invalid')}; "
                  f"probe verdicts {a.get('verdict_counts')}",
                  f"  - Globalping: {g['verdict']} ({g['timestamp'][:10]}; origin ruled out: "
                  f"{g.get('verdict_origin_adjusted')}); mtr_valid {g['measurement_ids'].get('mtr_valid')}, "
                  f"mtr_invalid {g['measurement_ids'].get('mtr_invalid')}"]
        lines += [_probe_line(d) for d in g.get("probe_details") or []]
    lines += ["", "## Hop ASNs: Globalping's against the local mapping", "",
              f"{hops_checked:,} public hops carried a Globalping ASN; {sum(hop_diff.values())} differed from the "
              "local mapping (PeeringDB IX LAN holder, else iptoasn).", ""]
    if hop_diff:
        lines += ["| local | Globalping | on an IX LAN | hops |", "|---|---|---|---|"]
        lines += [f"| {loc} | {', '.join(map(str, theirs))} | {'yes' if on_ix else 'no'} | {n} |"
                  for (loc, theirs, on_ix), n in hop_diff.most_common(25)]
    lines.append("")
    summary = {"pass": ok, "pass_adjusted": ok_adj, "criteria": crit, "criteria_adjusted": crit_adj,
               "results": n_gp, "pairs": len(pairs), "both_conclusive": len(both),
               "disagreements": [p["asn"] for p in disagree], "disagreements_adjusted": [p["asn"] for p in disagree_adj]}
    return "\n".join(lines), summary


def load_runs(paths: gv.Paths) -> list[dict]:
    runs = []
    try:
        with open(os.path.join(paths.gp, "runs.jsonl")) as fh:
            for line in fh:
                try:
                    runs.append(json.loads(line))
                except ValueError:
                    continue
    except OSError:
        pass
    return runs


def write_compare(paths: gv.Paths) -> dict | None:
    gp_results = gv.load_results(paths.gp)
    pairs = build_pairs(gp_results, gv.load_results(paths.atlas))
    text, summary = render_compare(pairs, load_runs(paths), _names(paths), len(gp_results))
    os.makedirs(paths.reports, exist_ok=True)
    out = os.path.join(paths.reports, "globalping_vs_atlas.md")
    with open(out, "w") as fh:
        fh.write(text)
    logger.info("[+] %s", out)
    for label, key, crit in (("As classified", "pass", "criteria"), ("Origin ruled out", "pass_adjusted", "criteria_adjusted")):
        logger.info("%s: %s", label, "PASS" if summary[key] else "NOT YET")
        for c in summary[crit]:
            logger.info("    %-7s %-42s %s (need %s)", "PASS" if c["ok"] else "NOT YET", c["name"], c["got"], c["need"])
    return summary
