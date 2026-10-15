import pandas as pd
import argparse
import os
from collections import Counter
import rov_utils

V6_DIFF_LIMIT = 30

def print_header(title):
    print("\n" + "="*100)
    print(f" {title}")
    print("="*100)

def v6_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Rows with an IPv6 verdict (the audit's v6_* columns, 2026-10-16); empty for older audits."""
    if 'v6_verdict' not in df.columns:
        return df.iloc[0:0]
    return df[df['v6_verdict'].fillna('').astype(str) != '']


def v6_summary(df: pd.DataFrame) -> dict | None:
    """{'networks': n, 'main': Counter(class), 'v6': Counter(class)} over networks with an IPv6
    verdict, so both columns count the same networks; None when the audit has no v6 columns."""
    if 'v6_verdict' not in df.columns:
        return None
    rows = v6_rows(df)
    return {'networks': len(rows),
            'main': Counter(rows['verdict'].map(rov_utils.classify_verdict)),
            'v6': Counter(rows['v6_verdict'].map(rov_utils.classify_verdict))}


def v6_differences(df: pd.DataFrame, limit: int = V6_DIFF_LIMIT) -> pd.DataFrame:
    """Networks whose IPv6 verdict class differs from the main verdict's, largest cone first."""
    rows = v6_rows(df)
    if rows.empty:
        return rows
    changed = rows[rows['verdict'].map(rov_utils.classify_verdict) != rows['v6_verdict'].map(rov_utils.classify_verdict)]
    return changed.sort_values(by='cone', ascending=False).head(limit)


def colour(verdict: str) -> str:
    cat = rov_utils.classify_verdict(verdict)
    return "\033[92m" if cat == "SECURE" else "\033[91m" if cat == "VULNERABLE" else "\033[93m" if cat == "PARTIAL" else "\033[90m"


def analyze_country(target_cc):
    target_cc = target_cc.upper()
    csv_file = rov_utils.FILE_AUDIT_FINAL
    
    if not os.path.exists(csv_file):
        print(f"[!] {csv_file} not found. Run rov_no_scrape_v22.py first.")
        return

    # 1. Load Data
    print(f"[*] Loading Global Audit for {target_cc}...")
    df = rov_utils.load_audit_csv(csv_file)
    country_df = df[df['cc'] == target_cc].copy()
    
    if len(country_df) == 0:
        print(f"[!] No ASNs found for country code '{target_cc}'.")
        return

    country_df['cone'] = pd.to_numeric(country_df['cone'], errors='coerce').fillna(0).astype(int)
    country_df['apnic_score'] = pd.to_numeric(country_df['apnic_score'], errors='coerce').fillna(-1)
    
    # SECTION 1: NATIONAL IMMUNITY STATS
    country_name = rov_utils.cc_to_name(target_cc)
    print_header(f"NATIONAL ROUTING SECURITY: {target_cc} ({country_name})" if country_name != target_cc
                 else f"NATIONAL ROUTING SECURITY: {target_cc}")
    total_asns = len(country_df)
    total_cone = country_df['cone'].sum()
    
    country_df['category'] = country_df['verdict'].apply(rov_utils.classify_verdict)
    
    secure = country_df[country_df['category'] == "SECURE"]
    vuln = country_df[country_df['category'] == "VULNERABLE"]
    
    pct_secure_traffic = (secure['cone'].sum() / total_cone * 100) if total_cone > 0 else 0
    pct_vuln_traffic = (vuln['cone'].sum() / total_cone * 100) if total_cone > 0 else 0
    
    print(f"Total Networks:      {total_asns:,}")
    print(f"Total Cone Gravity:  {total_cone:,}")
    print("-" * 60)
    print(f"\033[92mSECURE (ACTIVE/PASSIVE):\033[0m {len(secure):>5} ({len(secure)/total_asns*100:>4.1f}%) -> Protects {pct_secure_traffic:.1f}% of Traffic")
    print(f"\033[91mVULNERABLE NETWORKS:\033[0m     {len(vuln):>5} ({len(vuln)/total_asns*100:>4.1f}%) -> Exposes  {pct_vuln_traffic:.1f}% of Traffic")
    v6 = v6_summary(country_df)
    if v6 and v6['networks']:
        n = v6['networks']
        print("-" * 60)
        print(f"Seen in IPv6:        {n:,} networks (verdict from IPv6 providers only, column v6_verdict)")
        for cat in ("SECURE", "VULNERABLE"):
            print(f"  {cat:<10} main verdict {v6['main'][cat]:>5} ({v6['main'][cat]/n*100:>4.1f}%)   "
                  f"IPv6 verdict {v6['v6'][cat]:>5} ({v6['v6'][cat]/n*100:>4.1f}%)")
    
    # SECTION 2: THE NATIONAL GIANTS
    print_header(f"THE {target_cc} CORE (Top 20 Networks)")
    has_v6 = 'v6_verdict' in country_df.columns
    v6_head = f" | {'IPv6 Verdict':<30}" if has_v6 else ""
    print(f"{'ASN':<8} | {'Verdict':<30}{v6_head} | {'Cone':<8} | {'APNIC%':<6} | {'Name'}")
    print("-" * (133 if has_v6 else 100))
    
    giants = country_df.sort_values(by='cone', ascending=False).head(20)
    for _, r in giants.iterrows():
        v = r['verdict']
        score = f"{int(r['apnic_score'])}%" if r['apnic_score'] > -1 else "-"
        v6_cell = ""
        if has_v6:
            v6v = r['v6_verdict'] if isinstance(r['v6_verdict'], str) and r['v6_verdict'] else "-"
            v6_cell = f" | {colour(v6v)}{v6v:<30}\033[0m"
        print(f"AS{r['asn']:<6} | {colour(v)}{v:<30}\033[0m{v6_cell} | {r['cone']:<8} | {score:<6} | {r['name'][:40]}")

    # SECTION 3: SUPPLY CHAIN ANALYSIS
    print_header(f"TRANSIT SUPPLY CHAIN (Who provides to {target_cc}?)")
    cc_asns = country_df['asn'].astype(int).tolist()
    upstream_counts = rov_utils.load_upstreams_from_cache(cc_asns)
    
    print(f"{'Rank':<4} | {'Upstream':<8} | {'Dependents':<10} | {'Global Status':<30} | {'Name'}")
    print("-" * 100)
    
    for i, (asn, count) in enumerate(upstream_counts.most_common(20)):
        provider_row = df[df['asn'] == asn]
        if not provider_row.empty:
            r = provider_row.iloc[0]
            v = r['verdict']
            cat = rov_utils.classify_verdict(v)
            color = "\033[92m" if cat == "SECURE" else "\033[91m" if cat == "VULNERABLE" else "\033[90m"
            print(f"#{i+1:<3} | AS{asn:<6} | {count:<10} | {color}{v:<30}\033[0m | {r['name'][:40]}")
        else:
            print(f"#{i+1:<3} | AS{asn:<6} | {count:<10} | {'Unknown (Not in Audit)':<30} | -")

    # SECTION 4: IPv6 DIFFERENCES
    diff = v6_differences(country_df)
    if not diff.empty:
        print_header(f"IPv6 DIFFERENCES ({target_cc} networks whose IPv6 verdict class differs)")
        print("IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).")
        print("E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).")
        print(f"{'ASN':<8} | {'Verdict':<30} | {'IPv6 Verdict':<30} | {'v6 dirty/feeds':<14} | {'Name'}")
        print("-" * 120)
        for _, r in diff.iterrows():
            feeds = f"{int(r['v6_dirty_feeds'])}/{int(r['v6_total_feeds'])}"
            print(f"AS{r['asn']:<6} | {colour(r['verdict'])}{r['verdict']:<30}\033[0m | "
                  f"{colour(r['v6_verdict'])}{r['v6_verdict']:<30}\033[0m | {feeds:<14} | {r['name'][:40]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cc", help="ISO-2 Country Code (e.g. FR, US, AU)")
    args = parser.parse_args()
    analyze_country(args.cc)
