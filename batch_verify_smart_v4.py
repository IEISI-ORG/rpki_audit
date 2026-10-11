import argparse
import pandas as pd
import os
import json
import yaml
import time
from datetime import datetime, timezone
import rov_utils
import verify_forensic_path_v2 as forensic

MAX_TARGETS_PER_RUN = 50
DIR_ATLAS_V6 = os.path.join(rov_utils.DIR_ATLAS, "v6")  # outside load_atlas_verdicts' glob


def result_dir(af: int) -> str:
    return DIR_ATLAS_V6 if af == 6 else rov_utils.DIR_ATLAS


def is_fresh(file_path: str) -> bool:
    """True when a cached Atlas result exists and is younger than ATLAS_TTL_DAYS."""
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path) as f:
            ts_str = json.load(f).get('timestamp')
        if not ts_str:
            return False
        age_days = (datetime.now(timezone.utc) - datetime.fromisoformat(ts_str)).total_seconds() / 86400
        return age_days < rov_utils.ATLAS_TTL_DAYS
    except (OSError, ValueError):
        return False


def get_explicit_targets(asns: list[int] | None, cc: str | None, af: int, limit: int) -> list[int]:
    """Targets named on the command line, or a country's networks by cone size.

    Skips ASNs with a fresh result for this address family. Lets small-cone
    networks (e.g. NZ) be tested; get_smart_targets ranks them out of reach.
    """
    if asns:
        candidates = asns
    else:
        df = rov_utils.load_audit_csv()
        df = df[df['cc'] == cc.upper()].copy()
        df['cone'] = pd.to_numeric(df['cone'], errors='coerce').fillna(0).astype(int)
        candidates = [int(a) for a in df.sort_values('cone', ascending=False)['asn']]
    targets = [a for a in candidates if not is_fresh(os.path.join(result_dir(af), f"as_{a}.json"))]
    return targets[:limit]


def get_smart_targets(limit=50) -> list[int]:
    """
    Selects ASNs for re-verification, in priority order:
      1. Stale cached results (TTL expired) — always refresh these first
      2. REGRESSED or CORE: UNPROTECTED with large cones
      3. VULNERABLE / UNRELIABLE with large cones
      4. Large Unverified transit
    Only includes ASNs whose cached result has aged past ATLAS_TTL_DAYS OR
    that have no cached result at all.
    """
    # Stale set from the audit loader (already past TTL)
    _, _, _, stale_asns = rov_utils.load_atlas_verdicts()

    if not os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        print(f"[!] {rov_utils.FILE_AUDIT_FINAL} not found.")
        return sorted(stale_asns)[:limit]

    df = rov_utils.load_audit_csv()
    df['cone'] = pd.to_numeric(df['cone'], errors='coerce').fillna(0).astype(int)

    def get_priority(row):
        v = str(row['verdict']).upper()
        cone = row['cone']
        if "REGRESSED" in v or "UNPROTECTED" in v:
            return 100 + (cone / 1000)
        if "UNRELIABLE" in v or "VULNERABLE" in v:
            return 50 + (cone / 1000)
        if "UNVERIFIED" in v:
            return 10 + (cone / 1000)
        return 0

    df['priority'] = df.apply(get_priority, axis=1)
    candidates = df[df['priority'] > 0].sort_values('priority', ascending=False)

    targets: list[int] = []
    # Stale results always go first
    for asn in stale_asns:
        if len(targets) >= limit:
            break
        targets.append(asn)

    for _, row in candidates.iterrows():
        if len(targets) >= limit:
            break
        asn = int(row['asn'])
        if asn in targets:
            continue
        if not is_fresh(os.path.join(rov_utils.DIR_ATLAS, f"as_{asn}.json")):
            targets.append(asn)

    return targets


def find_best_probes_in_cone(target_asn: int, count: int = 5, af: int = 4) -> list[int]:
    """
    Find Atlas probes inside the customer cone of target_asn.

    Uses downstream_graph.json (the phantom-pruned topology) rather than
    the packed ASN data, so the customer set is consistent with the audit.

    Probe preference order:
      1. Single-homed customers (only one provider = the target) — highest
         fidelity; their traffic MUST traverse the target to reach the internet
      2. Multi-homed customers in the direct customer list — usable but the
         off-path guard in analyze_results will discard any probe whose
         traceroute didn't actually traverse the target
      3. Probes inside the target ASN itself (fallback)
    """
    print(f"    - Searching for probes in the customer cone of AS{target_asn}...")

    _, downstream, _ = rov_utils.load_topology()
    # providers_of: customer -> set of its providers
    from collections import defaultdict
    providers_of: dict[int, set] = defaultdict(set)
    for provider, customers in downstream.items():
        for c in customers:
            providers_of[c].add(provider)

    direct_customers = downstream.get(target_asn, [])
    single_homed = [c for c in direct_customers if len(providers_of.get(c, set())) == 1]
    multi_homed  = [c for c in direct_customers if len(providers_of.get(c, set())) > 1]

    found_probes: list[int] = []

    for candidate_list, label in [(single_homed, "single-homed"), (multi_homed, "multi-homed")]:
        for c_asn in candidate_list[:50]:
            if len(found_probes) >= count:
                break
            p_ids = forensic.get_probes(c_asn, count=2, af=af)
            if p_ids:
                found_probes.extend(p_ids)
                print(f"      * {len(p_ids)} probes in AS{c_asn} ({label})")
        if len(found_probes) >= count:
            break

    # Fallback: probes hosted inside the target ASN itself
    if len(found_probes) < count:
        local = forensic.get_probes(target_asn, count=count - len(found_probes), af=af)
        if local:
            found_probes.extend(local)
            print(f"      * {len(local)} probes inside AS{target_asn} (fallback)")

    return found_probes[:count]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=MAX_TARGETS_PER_RUN)
    parser.add_argument("--asns", help="comma-separated ASNs to test instead of smart selection")
    parser.add_argument("--cc", help="test this country's networks (largest cone first)")
    parser.add_argument("--af", type=int, choices=(4, 6), default=4,
                        help="address family; IPv6 results go to data/atlas/v6/")
    args = parser.parse_args()

    if not forensic.ATLAS_API_KEY:
        print("[!] Missing RIPE Atlas API Key in secrets.yaml")
        return

    out_dir = result_dir(args.af)
    os.makedirs(out_dir, exist_ok=True)

    if args.asns or args.cc:
        asns = [int(a.strip().upper().removeprefix("AS")) for a in args.asns.split(",")] if args.asns else None
        targets = get_explicit_targets(asns, args.cc, args.af, args.limit)
    elif args.af == 6:
        print("[!] --af 6 needs --asns or --cc (smart selection is IPv4-audit driven).")
        return
    else:
        targets = get_smart_targets(limit=args.limit)
    if not targets:
        print("[*] No targets need re-verification right now.")
        return

    print(f"[*] {len(targets)} targets selected for re-verification.")

    ip_v = forensic.resolve_ip(forensic.DOMAIN_VALID, af=args.af)
    ip_i = forensic.resolve_ip(forensic.DOMAIN_INVALID, af=args.af)
    if not ip_v or not ip_i:
        print("[!] DNS resolution failed for test domains.")
        return

    for asn in targets:
        print(f"\n>>> Verifying AS{asn}...")
        probes = find_best_probes_in_cone(asn, count=5, af=args.af)
        if not probes:
            print(f"    [!] No usable probes found in cone of AS{asn}. Skipping.")
            continue

        print(f"    - {len(probes)} probes selected.")
        raw_results = forensic.run_forensic_test(asn, probes, ip_v, ip_i, af=args.af)
        if not raw_results:
            print(f"    [!] Forensic test failed for AS{asn}")
            continue

        analysis = forensic.analyze_results(asn, raw_results)
        out_file = os.path.join(out_dir, f"as_{asn}.json")
        with open(out_file, 'w') as f:
            json.dump(analysis, f, indent=2)

        color = "\033[92m" if "SECURE" in analysis['verdict'] else "\033[91m"
        on_path = [p for p in analysis['probe_details']
                   if "Off-Path" not in p['verdict'] and "Down" not in p['verdict']]
        print(f"    - VERDICT: {color}{analysis['verdict']}\033[0m ({analysis['notes']})")
        print(f"    - On-path probes: {len(on_path)} / {analysis['total_probes']}")


if __name__ == "__main__":
    main()
