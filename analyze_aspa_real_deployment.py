import os
import pandas as pd
import rov_utils

HIGH_ROA_THRESHOLD = 90.0   # % ROA signing to count as "ROA hygiene" for readiness
READY_MIN_CONE = 100        # cone floor for "giant" in the readiness cross-check


def print_header(title: str) -> None:
    print("\n" + "=" * 100)
    print(f" {title}")
    print("=" * 100)


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    return len(a & b) / len(union) if union else 0.0


def analyze() -> None:
    if not os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        print(f"[!] {rov_utils.FILE_AUDIT_FINAL} not found. Run rov_no_scrape_v22.py first.")
        return

    print("[*] Loading Data...")
    df = pd.read_csv(rov_utils.FILE_AUDIT_FINAL, low_memory=False)
    df['cone'] = pd.to_numeric(df['cone'], errors='coerce').fillna(0).astype(int)
    verdict_map = df.set_index('asn')['verdict'].to_dict()
    name_map = df.set_index('asn')['name'].to_dict()
    cc_map = df.set_index('asn')['cc'].to_dict()
    cone_map = df.set_index('asn')['cone'].to_dict()

    asn_data = rov_utils.load_all_asn_data()
    roa_map = {asn: d.get('roa_signed_pct', 0.0) for asn, d in asn_data.items()}

    _, _, upstreams = rov_utils.load_topology()
    cc_to_rir = rov_utils.load_cc_to_rir()

    print("[*] Fetching real ASPA objects from console.rpki-client.org...")
    real_aspa = rov_utils.fetch_real_aspa_deployment()
    if not real_aspa:
        print("[!] No real ASPA data retrieved — aborting.")
        return
    print(f"    - {len(real_aspa):,} ASNs have a real, published ASPA object")

    # ------------------------------------------------------------------
    # SECTION 1: Global adoption
    # ------------------------------------------------------------------
    print_header("1. REAL ASPA ADOPTION (Ground Truth, not a Model)")
    total_asns = len(df)
    total_with_upstreams = len(upstreams)
    adopters = len(real_aspa)
    print(f"Total audited ASNs:                     {total_asns:,}")
    print(f"ASNs with an inferred upstream (customers): {total_with_upstreams:,}")
    print(f"ASNs with a real published ASPA object:  {adopters:,} "
          f"({adopters/total_asns*100:.2f}% of all ASNs, "
          f"{adopters/total_with_upstreams*100:.2f}% of ASNs with a provider to declare)")
    avg_providers = sum(len(p) for p in real_aspa.values()) / adopters
    max_providers = max(len(p) for p in real_aspa.values())
    print(f"Average declared providers per ASPA record: {avg_providers:.2f} (max {max_providers})")

    # ------------------------------------------------------------------
    # SECTION 2: Cross-check against the "Ready-to-Sign Giants" readiness model
    # ------------------------------------------------------------------
    print_header("2. MODEL vs REALITY — 'Ready-to-Sign Giants'")
    print(f"Giants (cone > {READY_MIN_CONE}) with 100% ROA hygiene and 100% secure upstreams "
          f"(per analyze_aspa_readiness_v2.py's criteria):")

    ready, ready_signed, ready_unsigned = [], [], []
    for asn, ups in upstreams.items():
        if cone_map.get(asn, 0) <= READY_MIN_CONE or not ups:
            continue
        secure_ups = sum(1 for u in ups if rov_utils.is_secure(str(verdict_map.get(u, ""))))
        if secure_ups == len(ups) and roa_map.get(asn, 0.0) >= HIGH_ROA_THRESHOLD:
            ready.append(asn)
            (ready_signed if asn in real_aspa else ready_unsigned).append(asn)

    if ready:
        print(f"  Ready-to-sign giants:     {len(ready):,}")
        print(f"  ...who HAVE signed ASPA:  {len(ready_signed):,} ({len(ready_signed)/len(ready)*100:.1f}%)")
        print(f"  ...who HAVEN'T yet:       {len(ready_unsigned):,} ({len(ready_unsigned)/len(ready)*100:.1f}%)")
        print("\n  Top 10 ready-but-unsigned (by cone, actionable outreach targets):")
        top_unsigned = sorted(ready_unsigned, key=lambda a: cone_map.get(a, 0), reverse=True)[:10]
        for asn in top_unsigned:
            print(f"    AS{asn:<6} | cone {cone_map.get(asn, 0):<7,} | {name_map.get(asn, 'Unknown')[:50]}")
    else:
        print("  [!] No ASNs met the readiness criteria.")

    # ------------------------------------------------------------------
    # SECTION 3: Topology validation — declared vs inferred provider sets
    # ------------------------------------------------------------------
    print_header("3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams")
    print("For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:")

    comparable = []
    for asn, declared in real_aspa.items():
        inferred = upstreams.get(asn)
        if not inferred:
            continue
        d_set, i_set = set(declared), set(inferred)
        comparable.append({
            'asn': asn, 'jaccard': jaccard(d_set, i_set),
            'declared': d_set, 'inferred': i_set,
        })

    if comparable:
        scores = [c['jaccard'] for c in comparable]
        exact = sum(1 for s in scores if s == 1.0)
        print(f"  ASNs comparable (both declared and inferred data exist): {len(comparable):,}")
        print(f"  Exact match (Jaccard = 1.0):    {exact:,} ({exact/len(comparable)*100:.1f}%)")
        print(f"  Mean Jaccard overlap:           {sum(scores)/len(scores):.3f}")
        print(f"  Median Jaccard overlap:         {sorted(scores)[len(scores)//2]:.3f}")

        print("\n  Biggest mismatches (declared vs inferred providers disagree most):")
        worst = sorted(comparable, key=lambda c: c['jaccard'])[:10]
        for c in worst:
            asn = c['asn']
            print(f"    AS{asn:<6} | {name_map.get(asn, 'Unknown')[:35]:<35} | Jaccard {c['jaccard']:.2f} | "
                  f"declared={sorted(c['declared'])} inferred={sorted(c['inferred'])}")
    else:
        print("  [!] No overlap between real ASPA adopters and our inferred-upstream set.")

    # ------------------------------------------------------------------
    # SECTION 4: Real adopters by RIR + top adopters by cone
    # ------------------------------------------------------------------
    print_header("4. REAL ADOPTERS BY RIR")
    rir_counts: dict[str, int] = {}
    for asn in real_aspa:
        rir = cc_to_rir.get(cc_map.get(asn, ''))
        if rir:
            rir_counts[rir] = rir_counts.get(rir, 0) + 1
    for rir, n in sorted(rir_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {rir:<10} | {n:>5,} adopters")

    print_header("TOP 15 REAL ASPA ADOPTERS BY CONE SIZE")
    print(f"{'ASN':<8} | {'CC':<2} | {'Cone':<8} | {'Verdict':<20} | {'Name'}")
    print("-" * 90)
    top_adopters = sorted(real_aspa.keys(), key=lambda a: cone_map.get(a, 0), reverse=True)[:15]
    for asn in top_adopters:
        v = str(verdict_map.get(asn, 'UNKNOWN'))
        print(f"AS{asn:<6} | {cc_map.get(asn, '??'):<2} | {cone_map.get(asn, 0):<8,} | {v[:20]:<20} | {name_map.get(asn, 'Unknown')[:40]}")

    # ------------------------------------------------------------------
    # Save full cross-reference CSV
    # ------------------------------------------------------------------
    rows = []
    for asn in set(df['asn']) | set(real_aspa.keys()):
        declared = real_aspa.get(asn)
        inferred = upstreams.get(asn)
        rows.append({
            'asn': asn,
            'name': name_map.get(asn, 'Unknown'),
            'cc': cc_map.get(asn, ''),
            'rir': cc_to_rir.get(cc_map.get(asn, ''), ''),
            'cone': cone_map.get(asn, 0),
            'verdict': verdict_map.get(asn, ''),
            'has_real_aspa': asn in real_aspa,
            'declared_providers': ';'.join(str(p) for p in declared) if declared else '',
            'inferred_upstreams': ';'.join(str(u) for u in inferred) if inferred else '',
            'jaccard_overlap': jaccard(set(declared), set(inferred)) if declared and inferred else None,
        })
    pd.DataFrame(rows).to_csv("aspa_real_vs_model.csv", index=False)
    print(f"\n[+] Full cross-reference saved to aspa_real_vs_model.csv")


if __name__ == "__main__":
    analyze()
