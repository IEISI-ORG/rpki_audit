import os
import sys

import pandas as pd
import rov_utils

# Fraction of the previous audit's row count below which a new audit is treated
# as degraded input (e.g. bgp.tools asns.csv missing drops ~30% of ASNs).
MIN_ROW_RATIO = 0.9


def degraded_input_reasons(new_rows: int, rov_tags: int) -> list[str]:
    """Return reasons the new audit looks degraded; empty list means OK to write."""
    reasons = []
    if rov_tags == 0:
        reasons.append("0 bgp.tools ROV tags loaded (fetch failed and no cached copy)")
    if os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        with open(rov_utils.FILE_AUDIT_FINAL) as fh:
            old_rows = sum(1 for _ in fh) - 1
        if old_rows > 0 and new_rows < MIN_ROW_RATIO * old_rows:
            reasons.append(f"{new_rows:,} rows vs {old_rows:,} in the existing audit "
                           f"(< {MIN_ROW_RATIO:.0%})")
    return reasons


def analyze():
    rov_utils.ensure_dirs()
    
    # 1. Load Data
    meta, countries = rov_utils.load_metadata()
    rov_utils.sync_apnic_data(countries)
    rov_set, cf_set, apnic_map = rov_utils.load_security_status()
    rovista_map = rov_utils.sync_rovista()
    atlas_secure, atlas_vulnerable, atlas_raw, atlas_stale = rov_utils.load_atlas_verdicts()
    ts_map = rov_utils.sync_apnic_timeseries(apnic_map, meta)
    
    # 2. Topology
    cones, downstream, upstreams = rov_utils.load_topology()
    if not cones or not upstreams:
        print("[!] Warning: Topology files missing. Run 'do_data_gathering' and 'build_topology_from_go.py' first.")

    print("[4] Generating Global Audit...")
    results = []
    
    # All active/known ASNs
    all_asns = set(meta.keys()) | set(cones.keys()) | set(upstreams.keys())
    
    # Measurement evidence from APNIC; ROVista only if rov_utils.ROVISTA_IN_VERDICTS
    # (off since 2026-10-14, see the ROVista section in CLAUDE.md).
    evidence = {
        asn: rov_utils.verdict_evidence(apnic_map.get(asn, -1), rovista_map.get(asn, -1))
        for asn in all_asns
    }

    # Identify "Safe" ASNs (Passive)
    safe_asns = set()
    for asn in all_asns:
        if (asn in rov_set) or (asn in cf_set) or evidence[asn] == "FILTERING":
            safe_asns.add(asn)

    # Active Overrides (Atlas & Volatility)
    # Atlas VULNERABLE can only downgrade networks with weak current evidence.
    # If a network is confirmed by both bgp.tools ROV tag AND APNIC score >= 60%,
    # the Atlas result is likely a probe-path artefact (probe routed via a
    # different provider that doesn't do ROV) rather than evidence that the
    # target ASN itself doesn't filter.  APNIC carefully selects single-provider
    # probes; our forensic test does not.  ROVista >= 60% counts the same as
    # APNIC, unless the two disagree.
    strong_current_rov = {
        asn for asn in atlas_vulnerable
        if (asn in rov_set or asn in cf_set)
        and evidence[asn] != "DISPUTED"
        and rov_utils.verdict_score(apnic_map.get(asn, -1), rovista_map.get(asn, -1)) >= 60.0
    }
    safe_asns -= (atlas_vulnerable - strong_current_rov)
    safe_asns |= atlas_secure
    
    for asn, (sd, mn, mx, volatile, regression) in ts_map.items():
        if volatile and asn in safe_asns and asn not in rov_set and asn not in cf_set:
            safe_asns.discard(asn)

    for asn in all_asns:
        name = meta.get(asn, {}).get('name', 'Unknown')
        cc = meta.get(asn, {}).get('cc', 'XX')
        cone = cones.get(asn, 0)
        parents = list(upstreams.get(asn, []))
        score = apnic_map.get(asn, -1)
        rovista_score = rovista_map.get(asn, -1)
        is_safe = asn in safe_asns
        
        ts = ts_map.get(asn)
        apnic_stdev, apnic_min90, apnic_max90, volatile, regression = (ts[0], ts[1], ts[2], ts[3], ts[4]) if ts else (-1.0, -1.0, -1.0, False, False)

        dirty_feeds = sum(1 for p in parents if p not in safe_asns)
        total_feeds = len(parents)
        atlas_v = atlas_raw.get(asn, "")
        
        verdict = rov_utils.assign_verdict(
            asn, is_safe, cone, parents, dirty_feeds, volatile, atlas_v
        )
        
        # Highlight Regression in Verdict - simplified label as requested
        # Guard: is_safe=True means the network has strong current ROV evidence
        # (rov_set/cf_set members stay is_safe=True even when volatile, per line 46).
        # CLAUSE.md: REGRESSED does not fire for networks currently classified as safe.
        if regression and not is_safe:
            verdict = "REGRESSED"

        # Fortuitous ROV: stub's APNIC score is consistent with filtering by its
        # upstream, not by the stub itself.  We have no direct evidence (rov_set,
        # cf_set, or Atlas "Target Filtered") that the stub's own routers drop
        # RPKI-invalid routes.  The protection is real but not locally confirmed.
        if (verdict == "STUB: ACTIVE LOCAL ROV"
                and asn not in rov_set
                and asn not in cf_set
                and asn not in atlas_secure):
            verdict = "STUB: FORTUITOUS ROV"

        # Disputed: APNIC and ROVista test the same thing and disagree (one >= 95%,
        # the other < 30%).  Tier 1, hardcoded and conclusive-Atlas verdicts are kept.
        verdict = rov_utils.apply_dispute(verdict, evidence[asn], asn, atlas_v)

        # Inconsistent: network declared ROV intent (bgp.tools rov_set) but the
        # measurements (APNIC/ROVista) show < 30% actual filtering.  Either partial
        # deployment, stale declaration, or ROV misconfigured on a subset of
        # links/routers.  The contradiction is the signal regardless of topology.
        if asn in rov_set and evidence[asn] == "NOT_FILTERING":
            verdict = "INCONSISTENT"

        results.append({
            'asn': asn, 'name': name, 'cc': cc, 'cone': cone,
            'verdict': verdict, 'apnic_score': score, 'rovista_score': rovista_score,
            'dirty_feeds': dirty_feeds, 'total_feeds': total_feeds,
            'atlas_result': atlas_v or '', 
            'apnic_stdev': apnic_stdev, 'apnic_min90': apnic_min90, 'apnic_max90': apnic_max90,
            'regression': regression
        })

    df = pd.DataFrame(results)
    problems = degraded_input_reasons(len(df), len(rov_set))
    if problems:
        # Keep the last good audit: a degraded file would flow into every
        # report and the weekly snapshot commit (as happened 2026-10-11).
        print("\n[!] REFUSING TO WRITE AUDIT — inputs look degraded:")
        for p in problems:
            print(f"    - {p}")
        print(f"    Kept existing {rov_utils.FILE_AUDIT_FINAL}.")
        sys.exit(1)
    df.sort_values(by='cone', ascending=False).to_csv(rov_utils.FILE_AUDIT_FINAL, index=False)
    
    print("\n" + "="*80)
    print(f"AUDIT COMPLETE: {len(df):,} ASNs")
    print(f"File Saved: {rov_utils.FILE_AUDIT_FINAL}")
    print("="*80)

if __name__ == "__main__":
    analyze()
