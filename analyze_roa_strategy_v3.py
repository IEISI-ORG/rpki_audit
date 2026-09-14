import pandas as pd
import os
import rov_utils

def analyze():
    print("[*] Loading Data for ROA Strategy Report...")
    if not os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        print(f"[!] {rov_utils.FILE_AUDIT_FINAL} not found. Run rov_no_scrape_v22.py first.")
        return

    # 1. Load Audit Results
    df = rov_utils.load_audit_csv()

    # 2. Load topology and signing stats
    cones, downstream, upstreams = rov_utils.load_topology()
    roa_map = rov_utils.load_signing_stats()
    
    df['signed_pct'] = df['asn'].map(roa_map).fillna(0.0)

    df['state'] = df.apply(
        lambda r: rov_utils.classify_signing_rov_state(r['signed_pct'], str(r['verdict'])), axis=1
    )

    # Insight 1: not signed, by ROV coverage type (see
    # rov_utils.classify_signing_rov_state for the full matrix definition —
    # an unsigned prefix can't be validated by ROV anywhere, local or
    # upstream, so this shows the operational nuance of why each ASN is
    # still unsigned-insecure, not a protection claim).
    print("\n" + "="*95)
    print("1. NOT SIGNED, BY ROV COVERAGE TYPE")
    print("-" * 95)
    print(f"{'ASN':<8} | {'CC':<2} | {'Cone':<8} | {'State':<26} | {'Signed%':<8} | {'Name'}")
    print("-" * 95)

    not_signed_states = ["NOT SIGNED (ROV LOCAL)", "NOT SIGNED (ROV UPSTREAM)", "NOT SIGNED (ROV PARTIAL)"]
    not_signed = df[df['state'].isin(not_signed_states)].sort_values(by='cone', ascending=False)
    for _, r in not_signed.head(15).iterrows():
        print(f"AS{r['asn']:<6} | {r['cc']:<2} | {int(r['cone']):<8} | {r['state']:<26} | \033[91m{r['signed_pct']:>5.1f}%\033[0m  | {r['name'][:45]}")

    # Insight 2: signed, but classified with no ROV coverage
    print("\n" + "="*95)
    print("2. SIGNED (NO ROV)")
    print("-" * 95)
    print(f"{'ASN':<8} | {'CC':<2} | {'Cone':<8} | {'Signed%':<8} | {'Name'}")
    print("-" * 95)

    signed_no_rov = df[(df['state'] == "SIGNED (NO ROV)") & (df['signed_pct'] > 95.0)].sort_values(by='cone', ascending=False)
    for _, r in signed_no_rov.head(15).iterrows():
        print(f"AS{r['asn']:<6} | {r['cc']:<2} | {int(r['cone']):<8} | \033[92m{r['signed_pct']:>5.1f}%\033[0m  | {r['name'][:45]}")

    # Insight 3: Weighted outreach targets
    print("\n" + "="*95)
    print("3. WEIGHTED OUTREACH TARGETS")
    print("   Metric = (Provider Cone Size) * (Count of Unsigned Customers)")
    print("-" * 95)
    print(f"{'ASN':<8} | {'CC':<2} | {'Cone':<8} | {'Unsigned':<8} | {'Impact Score':<14} | {'Name'}")
    print("-" * 95)
    
    providers = df[df['cone'] > 50].copy()
    outreach_list = []
    
    for _, row in providers.iterrows():
        asn = int(row['asn'])
        u_cnt, t_cnt = rov_utils.calculate_cone_health(asn, downstream, roa_map)
        if t_cnt > 0:
            impact_score = int(row['cone']) * u_cnt
            outreach_list.append({
                'asn': asn, 'cc': row['cc'], 'name': row['name'], 'cone': row['cone'],
                'unsigned_customers': u_cnt, 'impact_score': impact_score
            })
            
    outreach_list.sort(key=lambda x: x['impact_score'], reverse=True)
    for item in outreach_list[:25]:
        score_str = f"{item['impact_score']:,}"
        print(f"AS{item['asn']:<6} | {item['cc']:<2} | {int(item['cone']):<8} | {item['unsigned_customers']:<8} | {score_str:<14} | {item['name'][:35]}")

    pd.DataFrame(outreach_list).to_csv("roa_strategy_weighted_v2.csv", index=False)
    print(f"\n[+] Saved strategy to roa_strategy_weighted_v2.csv")

if __name__ == "__main__":
    analyze()
