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
    bgp_asns = rov_utils.load_bgp_asns()
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

    # One ladder decides whether each network filters (rov_utils.filtering_status, 2026-10-15):
    # policy > Atlas > measurement > declared (tag, isbgpsafeyet) > unknown. Customers' dirty-feed
    # counts and each network's own label both read it; UNKNOWN counts as dirty.
    status = {}
    for asn in all_asns:
        ts = ts_map.get(asn)
        status[asn] = rov_utils.filtering_status(
            asn, atlas_secure=atlas_secure, atlas_vulnerable=atlas_vulnerable,
            evidence=evidence[asn], volatile=bool(ts and ts[3]), regression=bool(ts and ts[4]),
            rov_set=rov_set, cf_set=cf_set)
    safe_asns = {asn for asn, (st, _) in status.items() if st == "FILTERING"}

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
            asn, is_safe, cone, parents, dirty_feeds, volatile, atlas_v, in_bgp=asn in bgp_asns
        )
        
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

        # REGRESSED (dropped over 1 year, not filtering now) and, last, INCONSISTENT (tagged, but
        # Atlas or the measurement says it doesn't filter: partial deployment, stale declaration
        # or misconfiguration). Both come from the ladder; a tag shields from neither.
        st, decided_by = status[asn]
        verdict = rov_utils.evidence_overrides(verdict, status=st, decided_by=decided_by,
                                               tagged=asn in rov_set, regression=regression)

        results.append({
            'asn': asn, 'name': name, 'cc': cc, 'cone': cone,
            'verdict': verdict, 'decided_by': decided_by, 'apnic_score': score, 'rovista_score': rovista_score,
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
