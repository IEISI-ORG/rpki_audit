"""
analyze_nz_project_report.py — New Zealand routing-security project report.

Goes beyond the weekly country deep dive (analyze_country_deep_dive_v2.py NZ):
  1. Verdicts for NZ's largest networks, with APNIC sample counts and the RIPE
     Atlas results (IPv4 and IPv6) behind them.
  2. ROV timeline for the case networks, from the dated APNIC series with the
     APNIC Labs test window (rov_utils.APNIC_EXCLUDED_WINDOWS) masked out.
  3. Coverage: Atlas probes (reports/nz_probe_gap.csv) and APNIC samples.
  4. Method limits, with the numbers that bound each one.

Writes reports/nz_verdicts.csv: one row per NZ network, with the Atlas
measurement IDs, so each verdict can be re-checked on atlas.ripe.net.
"""
import json
import os
from datetime import date, datetime, timedelta, timezone

import pandas as pd

import rov_utils

CC = "NZ"
TOP_N = 20
# Networks whose ROV state changed (or did not) in 2026; see TODO.md.
CASE_ASNS = (9790, 45177, 55850, 4771, 4648, 9500, 4768, 38022)
TIMELINE_LOOKBACK_DAYS = 365
STATE_MIN_RUN = 3  # consecutive reliable points before a state change counts
RECENT_DAYS = 30  # a 'current' APNIC reading older than this is flagged
SIBLINGS_SHOWN = 6
FILTERING_MIN, NOT_FILTERING_MAX = 95.0, 60.0
OUT_CSV = os.path.join("reports", "nz_verdicts.csv")
PROBE_GAP_CSV = os.path.join("reports", "nz_probe_gap.csv")
DIR_ATLAS_V6 = os.path.join(rov_utils.DIR_ATLAS, "v6")


def header(title: str) -> None:
    print("\n" + "=" * 100)
    print(f" {title}")
    print("=" * 100)


def load_atlas(asn: int, af: int) -> dict | None:
    path = os.path.join(DIR_ATLAS_V6 if af == 6 else rov_utils.DIR_ATLAS, f"as_{asn}.json")
    if not os.path.exists(path):
        return None
    try:
        with open(path) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def atlas_age_days(result: dict | None) -> float | None:
    if not result or not result.get("timestamp"):
        return None
    ts = datetime.fromisoformat(result["timestamp"])
    return (datetime.now(timezone.utc) - ts).total_seconds() / 86400


def atlas_label(result: dict | None) -> str:
    if not result:
        return "-"
    age = atlas_age_days(result)
    stale = " (stale)" if age is not None and age > rov_utils.ATLAS_TTL_DAYS else ""
    return f"{result.get('verdict', '?')[:22]}{stale}"


def cached_series(asn: int) -> list:
    """Dated APNIC series from cache only (no network): [] if absent or undated."""
    path = os.path.join(rov_utils.DIR_APNIC_TS, f"{asn}.json")
    try:
        with open(path) as fh:
            raw = json.load(fh)
    except (OSError, ValueError):
        return []
    return raw if rov_utils._ts_cache_is_dated(raw) else []


def reliable_points(raw: list, cc: str) -> list[tuple[str, float, int]]:
    """(date, rate, samples) with n >= the regression threshold, test window removed."""
    return [(r[0], r[1], r[2]) for r in raw
            if r[1] is not None and r[2] >= rov_utils.APNIC_REGRESSION_CURRENT_MIN_SAMPLES
            and not rov_utils._ts_point_excluded(r[0], r[3], cc)]


def state_of(rate: float) -> str:
    if rate >= FILTERING_MIN:
        return "FILTERING"
    if rate < NOT_FILTERING_MAX:
        return "NOT FILTERING"
    return "MIXED"


def timeline(raw: list, cc: str) -> list[tuple[str, str, str]]:
    """State changes (date, from, to) in the lookback window.

    A change counts only once the new state holds for STATE_MIN_RUN reliable
    points, so a one-day dip does not register. Dates are the first day of the run.
    """
    since = (date.today() - timedelta(days=TIMELINE_LOOKBACK_DAYS)).isoformat()
    points = [p for p in reliable_points(raw, cc) if p[0] >= since]
    changes, current, run_state, run_start, run_len = [], None, None, None, 0
    for d, rate, _ in points:
        s = state_of(rate)
        if s == run_state:
            run_len += 1
        else:
            run_state, run_start, run_len = s, d, 1
        if run_len == STATE_MIN_RUN and s != current:
            if current is not None:
                changes.append((run_start, current, s))
            current = s
    return changes


def first_state(raw: list, cc: str) -> str | None:
    since = (date.today() - timedelta(days=TIMELINE_LOOKBACK_DAYS)).isoformat()
    points = [p for p in reliable_points(raw, cc) if p[0] >= since]
    return state_of(points[0][1]) if points else None


def latest_point(raw: list, cc: str) -> tuple[str, float, int] | None:
    pts = reliable_points(raw, cc)
    return pts[-1] if pts else None


def probe_notes(asn: int, result: dict, orgs: dict) -> list[str]:
    """Per-probe outcome counts plus sibling observations the aggregate verdict hides.

    Siblings (same CAIDA organisation) are not part of the target for the
    forensic method, so a probe routed through a sibling counts as off-path and
    a filtering boundary at a sibling counts as "pre-target". Both are flagged.
    """
    details = result.get("probe_details", [])
    if not details:
        return ["no probe returned results (measurements ran, see msm IDs)"]
    org = orgs.get(asn, (None, ""))[0]
    siblings = {a for a, (o, _) in orgs.items() if org and o == org} - {asn}
    counts: dict[str, int] = {}
    for d in details:
        counts[d["verdict"]] = counts.get(d["verdict"], 0) + 1
    notes = ["; ".join(f"{n} x {v}" for v, n in sorted(counts.items()))]
    for d in details:
        via = [a for a in d.get("path_v") or [] if a in siblings]
        if "Off-Path" in d["verdict"] and via:
            notes.append(f"probe {d['probe_id']}: routed via sibling AS{via[0]}, counted off-path")
        if d.get("boundary_asn") in siblings:
            notes.append(f"probe {d['probe_id']}: invalid dropped at sibling AS{d['boundary_asn']} "
                         f"({d['verdict']})")
        if "Off-Path" in d["verdict"] and not (d.get("path_v") or [])[:-1]:
            notes.append(f"probe {d['probe_id']}: no resolvable hop before the destination AS "
                         "(probe's own AS not on the path)")
    return notes


def path_adjacency_check(asns: list[int], downstream: dict) -> tuple[int, int]:
    """(adjacencies with an inferred provider-customer link, total adjacencies)
    across the valid-path traceroutes of the given ASNs' Atlas results."""
    links = {(int(p), int(c)) for p, cs in downstream.items() for c in cs}
    known = total = 0
    for asn in asns:
        for af in (4, 6):
            result = load_atlas(asn, af) or {}
            for probe in result.get("probe_details", []):
                path = probe.get("path_v") or []
                for a, b in zip(path, path[1:]):
                    total += 1
                    known += (a, b) in links or (b, a) in links
    return known, total


def main() -> None:
    df = rov_utils.load_audit_csv()
    nz = df[df["cc"] == CC].copy()
    nz["cone"] = pd.to_numeric(nz["cone"], errors="coerce").fillna(0).astype(int)
    nz["apnic_score"] = pd.to_numeric(nz["apnic_score"], errors="coerce")
    nz = nz.sort_values("cone", ascending=False)
    _, downstream, _ = rov_utils.load_topology()
    orgs = rov_utils.load_as_orgs()
    audit_date = datetime.fromtimestamp(os.path.getmtime(rov_utils.FILE_AUDIT_FINAL)).date()

    header(f"NEW ZEALAND ROUTING SECURITY — PROJECT REPORT ({date.today().isoformat()})")
    print(f"Audit file:        {rov_utils.FILE_AUDIT_FINAL} (written {audit_date})")
    print(f"NZ networks:       {len(nz):,}")
    for first, last, ccs, reason in rov_utils.APNIC_EXCLUDED_WINDOWS:
        if CC in ccs:
            print(f"APNIC excluded:    {first} to {last} ({reason}); a daily reading is dropped")
            print("                   when its rolling window overlaps these dates.")

    # ── 1. Verdict summary ──────────────────────────────────────────────────
    header("1. VERDICTS")
    nz["bucket"] = nz["verdict"].map(rov_utils.classify_verdict)
    total_cone = max(nz["cone"].sum(), 1)
    for bucket, g in nz.groupby("bucket"):
        print(f"{bucket:<12} {len(g):>4} networks ({len(g) / len(nz):5.1%}) | "
              f"{g['cone'].sum() / total_cone:5.1%} of NZ cone gravity")
    print("\nBy verdict label:")
    for verdict, n in nz["verdict"].value_counts().items():
        print(f"  {verdict:<36} {n:>4}")

    # ── 2. Top networks ────────────────────────────────────────────────────
    header(f"2. NZ TOP {TOP_N} NETWORKS BY CUSTOMER CONE")
    print(f"{'ASN':<9} | {'Name':<26} | {'Verdict':<27} | {'Cone':>5} | {'APNIC%':>6} | "
          f"{'n':>6} | {'Atlas v4':<24} | Atlas v6")
    print("-" * 140)
    for _, r in nz.head(TOP_N).iterrows():
        asn = int(r["asn"])
        lp = latest_point(cached_series(asn), CC)
        rate = f"{lp[1]:.0f}" if lp else ("-" if r["apnic_score"] < 0 else f"{r['apnic_score']:.0f}")
        n = f"{lp[2]:,}" if lp else "-"
        print(f"AS{asn:<7} | {str(r['name'])[:26]:<26} | {str(r['verdict'])[:27]:<27} | "
              f"{r['cone']:>5} | {rate:>6} | {n:>6} | {atlas_label(load_atlas(asn, 4)):<24} | "
              f"{atlas_label(load_atlas(asn, 6))}")
    print("\nAPNIC% and n: most recent daily reading with n >= "
          f"{rov_utils.APNIC_REGRESSION_CURRENT_MIN_SAMPLES} samples, test window excluded.")

    # ── 2b. Atlas detail ───────────────────────────────────────────────────
    header("2b. RIPE ATLAS DETAIL (per-probe outcomes for NZ networks with an Atlas result)")
    for _, r in nz.iterrows():
        asn = int(r["asn"])
        for af in (4, 6):
            res = load_atlas(asn, af)
            if not res or (not res.get("probe_details") and not res.get("measurement_ids")):
                continue  # untested, or a pre-2026-10-11 result without per-probe detail
            ids = " ".join(str(v) for v in (res.get("measurement_ids") or {}).values() if v)
            print(f"AS{asn:<7} IPv{af} {str(r['name'])[:28]:<28} {res.get('verdict')} "
                  f"({str(res.get('timestamp', ''))[:10]}) msm: {ids or '-'}")
            for note in probe_notes(asn, res, orgs):
                print(f"{'':>14}{note}")

    # ── 3. Case timeline ───────────────────────────────────────────────────
    header(f"3. ROV TIMELINE, LAST {TIMELINE_LOOKBACK_DAYS} DAYS (APNIC, test window masked)")
    print(f"States: FILTERING >= {FILTERING_MIN:.0f}%, NOT FILTERING < {NOT_FILTERING_MAX:.0f}%, "
          f"else MIXED; a change needs {STATE_MIN_RUN} consecutive readings.\n")
    for asn in CASE_ASNS:
        raw = rov_utils._fetch_apnic_ts_rates(asn, CC)
        row = nz[nz["asn"] == asn]
        name = str(row["name"].iloc[0]) if len(row) else orgs.get(asn, ("", "?"))[1]
        if not rov_utils._ts_cache_is_dated(raw):
            print(f"AS{asn:<7} {name[:30]:<30} no dated APNIC series")
            continue
        changes, start = timeline(raw, CC), first_state(raw, CC)
        lp = latest_point(raw, CC)
        old = " — OLD READING" if lp and lp[0] < (date.today() - timedelta(days=RECENT_DAYS)).isoformat() else ""
        now = (f"now {state_of(lp[1])} ({lp[1]:.0f}%, n={lp[2]:,}, {lp[0]}{old})"
               if lp else "no reliable recent reading")
        print(f"AS{asn:<7} {name[:30]:<30} started {start or '?'}; {now}")
        for d, a, b in changes:
            print(f"{'':>40}{d}: {a} -> {b}")
        v4 = load_atlas(asn, 4)
        if v4:
            print(f"{'':>40}Atlas v4: {v4.get('verdict')} ({str(v4.get('timestamp', ''))[:10]})")
    print("\nChange dates are the first day the new state held. Readings whose window overlaps the")
    print("test window are masked, so a change during 5-24 Aug (7-day window) shows as the first")
    print("unmasked day; confirm such dates with Atlas.")
    print("\nAPNIC measures what users of the network see: filtering inherited from an upstream")
    print("counts the same as local ROV. The Atlas verdicts above test the network itself.")

    # ── 4. Coverage ────────────────────────────────────────────────────────
    header("4. MEASUREMENT COVERAGE")
    if os.path.exists(PROBE_GAP_CSV):
        gap = pd.read_csv(PROBE_GAP_CSV, keep_default_na=False, na_values=[""])
        print(f"RIPE Atlas (from {PROBE_GAP_CSV}):")
        print(f"  probe inside network (IPv4 / IPv6): {(gap['probes_v4'] > 0).sum()} / "
              f"{(gap['probes_v6'] > 0).sum()} of {len(gap)}")
        print(f"  testable via a direct customer:     "
              f"{(gap['covered_v4'] & (gap['probes_v4'] == 0)).sum()}")
        print(f"  not testable over IPv4:             {(~gap['covered_v4']).sum()}")
    else:
        print(f"RIPE Atlas: run analyze_probe_gap.py first ({PROBE_GAP_CSV} missing).")
    scored = nz[nz["apnic_score"] >= 0]
    recent_cutoff = (date.today() - timedelta(days=RECENT_DAYS)).isoformat()
    latest = [latest_point(rov_utils._fetch_apnic_ts_rates(int(a), CC), CC) for a in scored["asn"]]
    recent = sum(1 for p in latest if p and p[0] >= recent_cutoff)
    print("\nAPNIC Labs:")
    print(f"  any APNIC score:                    {len(scored)} of {len(nz)}")
    print(f"  reading with n>=100 in last {RECENT_DAYS} days: {recent} of {len(nz)}")
    print("  APNIC samples come from ad impressions, so networks with few end users")
    print("  (research, enterprise, wholesale transit) get few or no readings.")
    sparse = nz[nz["apnic_score"] < 0].head(10)
    if len(sparse):
        print("  Largest networks with no APNIC score: "
              + ", ".join(f"AS{int(a)} {str(n)[:20]}" for a, n in zip(sparse["asn"], sparse["name"])))

    # ── 5. Method limits ───────────────────────────────────────────────────
    header("5. METHOD LIMITS")
    sib_groups: dict[str, list[int]] = {}
    for a in nz["asn"].astype(int):
        if a in orgs:
            sib_groups.setdefault(orgs[a][0], []).append(a)
    multi = {o: sorted(a) for o, a in sib_groups.items() if len(a) > 1}
    print("Siblings: the topology treats each AS separately. CAIDA AS-to-organisation data puts")
    print(f"{sum(len(v) for v in multi.values())} NZ ASes in {len(multi)} multi-AS organisations, including:")
    top_multi = sorted(multi.items(), key=lambda kv: -nz[nz["asn"].isin(kv[1])]["cone"].sum())[:8]
    for org, asns in top_multi:
        shown = ", ".join(f"AS{a}" for a in asns[:SIBLINGS_SHOWN])
        more = f" (+{len(asns) - SIBLINGS_SHOWN} more)" if len(asns) > SIBLINGS_SHOWN else ""
        print(f"  {orgs[asns[0]][1][:40]:<40} {shown}{more}")
    known, total = path_adjacency_check([int(a) for a in nz["asn"]], downstream)
    pct = f"{known / total:.0%}" if total else "n/a"
    print(f"\nInferred topology: of {total} AS adjacencies on NZ Atlas valid-path traceroutes,")
    print(f"{known} ({pct}) match an inferred provider-customer link. The rest are peering, IXP")
    print("or links the valley-free inference missed; customer cones are built only from inferred links.")
    print("\nIPv6: forensic tests can now run over IPv6 (batch_verify_smart_v4.py --af 6);")
    print("networks without an IPv6 Atlas result above are IPv4-tested only.")
    print("\nCustomer routes: the isbgpsafeyet beacon is reached via peers and transit. No test here")
    print("shows whether a network applies ROV to routes learned from its own customers.")

    # ── 6. Verdict CSV ─────────────────────────────────────────────────────
    rows = []
    for _, r in nz.iterrows():
        asn = int(r["asn"])
        lp = latest_point(cached_series(asn), CC)
        row = {"asn": asn, "name": r["name"], "org": orgs.get(asn, ("", ""))[1],
               "verdict": r["verdict"], "cone": r["cone"],
               "apnic_score_country_page": r["apnic_score"],
               "apnic_rate": lp[1] if lp else None, "apnic_samples": lp[2] if lp else None,
               "apnic_date": lp[0] if lp else None}
        for af in (4, 6):
            res = load_atlas(asn, af) or {}
            row[f"atlas_v{af}_verdict"] = res.get("verdict")
            row[f"atlas_v{af}_date"] = str(res.get("timestamp", ""))[:10] or None
            ids = res.get("measurement_ids") or {}
            row[f"atlas_v{af}_msm_ids"] = " ".join(str(v) for v in ids.values() if v) or None
            row[f"atlas_v{af}_probe_ids"] = " ".join(map(str, res.get("probe_ids", []))) or None
        rows.append(row)
    pd.DataFrame(rows).to_csv(OUT_CSV, index=False)
    print(f"\n[*] Per-network verdicts: {OUT_CSV} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
