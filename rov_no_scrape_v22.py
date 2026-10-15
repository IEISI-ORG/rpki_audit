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
    # IPv6-only graph (2026-10-16): HE gives its peers IPv6 transit, so a network's IPv6 providers can
    # differ from the main graph's. Judged with the same pipeline into the v6_* columns; the main
    # verdict is unchanged (Terry's choice). Blank for ASes not in the IPv6 graph.
    downstream_v6, upstreams_v6 = rov_utils.load_graph(rov_utils.FILE_GRAPH_V6)
    v6_asns = set(upstreams_v6) | set(downstream_v6)
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
        ts = ts_map.get(asn)
        apnic_stdev, apnic_min90, apnic_max90, volatile, regression = (ts[0], ts[1], ts[2], ts[3], ts[4]) if ts else (-1.0, -1.0, -1.0, False, False)

        total_feeds = len(parents)
        atlas_v = atlas_raw.get(asn, "")
        st, decided_by = status[asn]
        ctx = dict(safe_asns=safe_asns, cone=cone, volatile=volatile, atlas_v=atlas_v,
                   in_bgp=asn in bgp_asns, evidence=evidence[asn], status=st, decided_by=decided_by,
                   regression=regression, rov_set=rov_set, cf_set=cf_set, atlas_secure=atlas_secure)
        # assign_verdict, then STUB: FORTUITOUS ROV, DISPUTED, and last REGRESSED / INCONSISTENT
        # from the evidence ladder (a tag shields from neither); see rov_utils.audit_verdict.
        verdict, dirty_feeds = rov_utils.audit_verdict(asn, parents, **ctx)
        if asn in v6_asns:
            parents_v6 = upstreams_v6.get(asn, set())
            v6_verdict, v6_dirty = rov_utils.audit_verdict(asn, parents_v6, **ctx)
            v6_total = len(parents_v6)
        else:
            v6_verdict, v6_dirty, v6_total = "", "", ""

        results.append({
            'asn': asn, 'name': name, 'cc': cc, 'cone': cone,
            'verdict': verdict, 'decided_by': decided_by, 'apnic_score': score, 'rovista_score': rovista_score,
            'dirty_feeds': dirty_feeds, 'total_feeds': total_feeds,
            'atlas_result': atlas_v or '', 
            'apnic_stdev': apnic_stdev, 'apnic_min90': apnic_min90, 'apnic_max90': apnic_max90,
            'regression': regression,
            'v6_dirty_feeds': v6_dirty, 'v6_total_feeds': v6_total, 'v6_verdict': v6_verdict,
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
