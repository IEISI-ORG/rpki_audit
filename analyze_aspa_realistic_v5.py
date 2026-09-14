import pandas as pd
import os
from collections import Counter
import rov_utils


def print_header(title: str) -> None:
    print("\n" + "=" * 95)
    print(f" {title}")
    print("=" * 95)


def is_regular_network(asn: int) -> bool:
    """Exclude Tier 1 cores and non-transit infrastructure (RIRs, root servers, IXP
    route servers) — these don't have meaningful 'upstream' relationships to model."""
    return asn not in rov_utils.TIER_1_ASNS and asn not in rov_utils.NON_TRANSIT_ASNS


def analyze() -> None:
    if not os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        print(f"[!] {rov_utils.FILE_AUDIT_FINAL} not found. Run rov_no_scrape_v22.py first.")
        return

    print("[*] Loading Data...")
    df = pd.read_csv(rov_utils.FILE_AUDIT_FINAL, low_memory=False)
    df['cone'] = pd.to_numeric(df['cone'], errors='coerce').fillna(0).astype(int)
    name_map = df.set_index('asn')['name'].to_dict()
    cone_map = df.set_index('asn')['cone'].to_dict()

    asn_data = rov_utils.load_all_asn_data()
    records: dict[int, list[int]] = {}
    for asn, data in asn_data.items():
        if not is_regular_network(asn):
            continue
        upstreams = [int(u) for u in data.get('upstreams', [])]
        if upstreams:
            records[asn] = upstreams
    print(f"    - Modeled: {len(records):,} 'Regular' Networks")

    # ---------------------------------------------------------
    # 1. COMPLEXITY DISTRIBUTION
    # ---------------------------------------------------------
    print_header("1. ASPA READINESS (Simplicity vs Complexity)")

    total = len(records)
    complexity = Counter(len(ups) for ups in records.values())
    c_simple = complexity[1] + complexity[2]
    c_mod = sum(c for k, c in complexity.items() if 2 < k <= 5)
    c_complex = sum(c for k, c in complexity.items() if k > 5)

    print(f"Total Networks: {total:,}")
    print("-" * 60)
    print(f"  - Trivial (1-2 Providers):   {c_simple:>6,} ({c_simple/total*100:>4.1f}%)")
    print(f"  - Moderate (3-5 Providers):  {c_mod:>6,} ({c_mod/total*100:>4.1f}%)")
    print(f"  - Complex (>5 Providers):    {c_complex:>6,} ({c_complex/total*100:>4.1f}%) -> \033[93mTarget for Engineering Support\033[0m")

    # ---------------------------------------------------------
    # 2. COMPLEXITY GIANTS (Traffic Engineering Heavyweights)
    # ---------------------------------------------------------
    print_header("2. COMPLEXITY GIANTS (Traffic Engineering Heavyweights)")
    print("Networks with >5 Upstreams (Highest Maintenance Burden).")
    print("-" * 90)
    print(f"{'ASN':<8} | {'Providers':<10} | {'Cone':<8} | {'Name'}")
    print("-" * 90)

    complex_list = [
        {'asn': asn, 'count': len(ups), 'cone': cone_map.get(asn, 0), 'name': name_map.get(asn, "Unknown")}
        for asn, ups in records.items() if len(ups) > 5
    ]
    complex_list.sort(key=lambda x: (x['count'], x['cone']), reverse=True)

    for item in complex_list[:50]:
        print(f"AS{item['asn']:<6} | {item['count']:<10} | {item['cone']:<8} | {item['name'][:50]}")

    if complex_list:
        out_df = pd.DataFrame(complex_list)
        filename = "aspa_complexity_list.csv"
        out_df.to_csv(filename, index=False)
        print(f"\n[+] Full list of {len(complex_list)} complex networks saved to '{filename}'")


if __name__ == "__main__":
    analyze()
