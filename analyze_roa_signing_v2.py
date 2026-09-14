import pandas as pd
import os
import rov_utils

def analyze():
    print("[*] Loading Data for ROA Signing Report...")
    if not os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        print(f"[!] {rov_utils.FILE_AUDIT_FINAL} not found. Run rov_no_scrape_v22.py first.")
        return

    # 1. Load Audit Results
    df = pd.read_csv(rov_utils.FILE_AUDIT_FINAL, low_memory=False)
    df.set_index('asn', inplace=True)
    
    # 2. Load Signing Stats from Cache
    signing_data = rov_utils.load_signing_stats()
    df['signed_pct'] = df.index.map(signing_data).fillna(0.0)

    # Segmentation
    fully_signed = df[df['signed_pct'] >= 90.0]
    partial_signed = df[(df['signed_pct'] > 0) & (df['signed_pct'] < 90.0)]
    unsigned = df[df['signed_pct'] == 0.0]
    
    df['state'] = df.apply(
        lambda r: rov_utils.classify_signing_rov_state(r['signed_pct'], str(r['verdict'])), axis=1
    )

    print("\n" + "="*80)
    print("GLOBAL ROA SIGNING REPORT")
    print("="*80)

    total = len(df)
    print(f"Total Networks: {total:,}")
    print(f"  - Fully Signed (>90%):  {len(fully_signed):>6,}  ({(len(fully_signed)/total)*100:.1f}%)")
    print(f"  - Partially Signed:     {len(partial_signed):>6,}  ({(len(partial_signed)/total)*100:.1f}%)")
    print(f"  - Totally Unsigned:     {len(unsigned):>6,}  ({(len(unsigned)/total)*100:.1f}%)")

    # Formal ROA-signing x ROV-coverage classification (see
    # rov_utils.classify_signing_rov_state for the full matrix definition).
    print("\n" + "="*80)
    print("ROA SIGNING x ROV COVERAGE CLASSIFICATION")
    print("-" * 80)
    state_order = [
        "FULL ROV COVERAGE", "PARTIALLY SECURE", "SIGNED (NO ROV)",
        "PARTIALLY SIGNED (WEAK)",
        "NOT SIGNED (ROV LOCAL)", "NOT SIGNED (ROV UPSTREAM)", "NOT SIGNED (ROV PARTIAL)",
        "NOT SIGNED (INSECURE)",
    ]
    counts = df['state'].value_counts()
    for state in state_order:
        n = counts.get(state, 0)
        print(f"  {state:<28} {n:>7,}  ({n/total*100:>4.1f}%)")

    # Insight 1: not signed, but the ASN's own prefix protection is moot per
    # definition (an unsigned route is RPKI 'NotFound', never 'Valid', so no
    # ROV anywhere can validate it) — this shows the operational nuance of
    # *why* each one is still unsigned-insecure: doing its own filtering
    # (rare), inheriting filtering from upstream, or neither.
    not_signed_states = ["NOT SIGNED (ROV LOCAL)", "NOT SIGNED (ROV UPSTREAM)", "NOT SIGNED (ROV PARTIAL)"]
    not_signed = df[df['state'].isin(not_signed_states)].sort_values(by='cone', ascending=False)
    print("\n" + "="*80)
    print("NOT SIGNED, BY ROV COVERAGE TYPE")
    print("Own prefix is unsigned — no ROV anywhere can validate it. Shown: whether this")
    print("ASN's own inbound traffic is separately protected by local, upstream, or partial ROV.")
    print("-" * 80)
    print(f"{'ASN':<8} | {'CC':<2} | {'Cone':<8} | {'State':<26} | {'Name'}")
    print("-" * 80)
    for asn, row in not_signed.head(15).iterrows():
        print(f"AS{asn:<6} | {row['cc']:<2} | {int(row['cone']):<8} | {row['state']:<26} | {row['name'][:40]}")

    # Insight 2: signed, but classified with no ROV coverage
    signed_no_rov = df[(df['state'] == "SIGNED (NO ROV)") & (df['signed_pct'] > 95.0)].sort_values(by='cone', ascending=False)
    print("\n" + "="*80)
    print("SIGNED (NO ROV) — Own Routes Signed, Feeds Show Invalid Routes")
    print("-" * 80)
    print(f"{'ASN':<8} | {'CC':<2} | {'Cone':<8} | {'Feeds':<6} | {'Name'}")
    print("-" * 80)
    for asn, row in signed_no_rov.head(15).iterrows():
        ups = f"{row['dirty_feeds']}/{row['total_feeds']}"
        print(f"AS{asn:<6} | {row['cc']:<2} | {int(row['cone']):<8} | {ups:<6} | {row['name'][:40]}")

    print("\n")

if __name__ == "__main__":
    analyze()
