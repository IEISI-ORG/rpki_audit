import calendar
import datetime
import os
import pandas as pd
import rov_utils

LOOKBACKS = [("Now", 0), ("3mo", 3), ("6mo", 6), ("12mo", 12), ("24mo", 24)]
TOP_N = 15


def print_header(title: str) -> None:
    print("\n" + "=" * 100)
    print(f" {title}")
    print("=" * 100)


def months_ago(dt: datetime.date, months: int) -> datetime.date:
    """Subtract N calendar months from dt, clamping the day to the target month's length."""
    total = dt.month - 1 - months
    year = dt.year + total // 12
    month = total % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def fetch_all_snapshots() -> dict:
    """Returns {label: {cc: {...}}} for each entry in LOOKBACKS."""
    today = datetime.date.today()
    snapshots = {}
    print("[*] Fetching APNIC Labs ROA-coverage snapshots...")
    for label, months in LOOKBACKS:
        if months == 0:
            data = rov_utils.fetch_apnic_roa_by_country(None)
        else:
            data = rov_utils.fetch_apnic_roa_by_country(months_ago(today, months))
        print(f"    - {label:<5} (reported date {data.get('date', '?')}): "
              f"{len(data) - 1} countries/regions")
        snapshots[label] = data
    return snapshots


def rir_rollup(snapshot: dict, cc_to_rir: dict, stack: str = "v4") -> dict:
    """Aggregate a per-country snapshot to per-RIR totals, weighted by route-object count.

    stack: "v4" (default, keys 'valid'/'total') or "v6" (keys 'v6_valid'/'v6_total').
    """
    valid_key, total_key = ("v6_valid", "v6_total") if stack == "v6" else ("valid", "total")
    totals = {}
    for cc, row in snapshot.items():
        if cc == 'date':
            continue
        rir = cc_to_rir.get(cc)
        if not rir:
            continue
        t = totals.setdefault(rir, {'valid': 0, 'total': 0})
        t['valid'] += row.get(valid_key, 0)
        t['total'] += row.get(total_key, 0)
    for rir, t in totals.items():
        t['valid_pct'] = (t['valid'] / t['total'] * 100) if t['total'] else 0.0
    return totals


def analyze() -> None:
    if not os.path.exists(rov_utils.FILE_AUDIT_FINAL):
        print(f"[!] {rov_utils.FILE_AUDIT_FINAL} not found. Run rov_no_scrape_v22.py first.")
        return

    cc_to_rir = rov_utils.load_cc_to_rir()
    if not cc_to_rir:
        print(f"[!] {rov_utils.FILE_CC_TO_RIR} not found or empty. Cannot compute RIR rollups.")
        return

    df = rov_utils.load_audit_csv()
    asn_count_by_cc = df['cc'].value_counts().to_dict()
    asn_count_by_rir = {}
    for cc, n in asn_count_by_cc.items():
        rir = cc_to_rir.get(cc)
        if rir:
            asn_count_by_rir[rir] = asn_count_by_rir.get(rir, 0) + n

    snapshots = fetch_all_snapshots()
    labels = [lbl for lbl, _ in LOOKBACKS]

    # RIR rollups computed first — the global total is derived from these rather
    # than APNIC's own 'XA' (World) row, which is absent from their historical
    # format for older dates (confirmed missing for the 24-month-ago snapshot).
    rir_rollups = {label: rir_rollup(snapshots[label], cc_to_rir) for label in labels}
    rir_rollups_v6 = {label: rir_rollup(snapshots[label], cc_to_rir, stack="v6") for label in labels}
    all_rirs = sorted({r for label in labels for r in rir_rollups[label]})

    # ------------------------------------------------------------------
    # SECTION 1: Global (World) trend — IPv4 and IPv6 side by side
    # ------------------------------------------------------------------
    for stack_name, rollups in (("IPv4", rir_rollups), ("IPv6", rir_rollups_v6)):
        print_header(f"GLOBAL ROA COVERAGE TREND ({stack_name} Route Objects, % Valid)")
        print(f"{'Period':<8} | {'Reported Date':<14} | {'% Valid':<8} | {'Total Route Objects'}")
        print("-" * 60)
        for label in labels:
            snap = snapshots[label]
            world_valid = sum(t['valid'] for t in rollups[label].values())
            world_total = sum(t['total'] for t in rollups[label].values())
            world_pct = (world_valid / world_total * 100) if world_total else 0.0
            print(f"{label:<8} | {snap.get('date', '?'):<14} | {world_pct:>6.1f}% | {world_total:>10,}")

    print("\nNOTE: IPv4 and IPv6 are reported separately because they are measured\n"
          "separately by APNIC and can diverge significantly per network — do not\n"
          "average or add them into one 'global ROA coverage' number.")

    # ------------------------------------------------------------------
    # SECTION 2: RIR-level trend (weighted by route-object count) + current ASN counts
    # ------------------------------------------------------------------
    print_header("RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)")
    header = f"{'RIR':<10} | {'ASNs (now)':<10} | " + " | ".join(f"{lbl:>7}" for lbl in labels)
    print(header)
    print("-" * len(header))
    for rir in all_rirs:
        row = f"{rir:<10} | {asn_count_by_rir.get(rir, 0):<10,} | "
        row += " | ".join(f"{rir_rollups[lbl].get(rir, {}).get('valid_pct', 0):>6.1f}%" for lbl in labels)
        print(row)

    print_header("RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)")
    print(header)
    print("-" * len(header))
    for rir in all_rirs:
        row = f"{rir:<10} | {asn_count_by_rir.get(rir, 0):<10,} | "
        row += " | ".join(f"{rir_rollups_v6[lbl].get(rir, {}).get('valid_pct', 0):>6.1f}%" for lbl in labels)
        print(row)

    # ------------------------------------------------------------------
    # SECTION 3: Per-country deltas — symmetric improvers/decliners
    # ------------------------------------------------------------------
    now_snap = snapshots["Now"]
    rows = []
    for cc, row in now_snap.items():
        if cc == 'date' or not cc_to_rir.get(cc):
            continue
        entry = {'cc': cc, 'rir': cc_to_rir[cc], 'asn_count': asn_count_by_cc.get(cc, 0),
                  'valid_pct_now': row['valid_pct'], 'total_now': row['total'],
                  'valid_pct_now_v6': row.get('v6_valid_pct'), 'total_now_v6': row.get('v6_total')}
        for label in labels[1:]:
            past = snapshots[label].get(cc)
            entry[f'valid_pct_{label}'] = past['valid_pct'] if past else None
            entry[f'delta_{label}'] = round(row['valid_pct'] - past['valid_pct'], 1) if past else None
            past_v6_pct = past.get('v6_valid_pct') if past else None
            entry[f'valid_pct_{label}_v6'] = past_v6_pct
            entry[f'delta_{label}_v6'] = (
                round(row.get('v6_valid_pct', 0) - past_v6_pct, 1)
                if past and past_v6_pct is not None and row.get('v6_valid_pct') is not None else None
            )
        rows.append(entry)

    trend_df = pd.DataFrame(rows)
    trend_df.to_csv("roa_signing_trends.csv", index=False)
    print(f"\n[+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv")

    for stack_suffix, stack_label, now_col in (("", "IPv4", "valid_pct_now"), ("_v6", "IPv6", "valid_pct_now_v6")):
        for window in ("3mo", "6mo", "12mo", "24mo"):
            col = f'delta_{window}{stack_suffix}'
            valid_rows = trend_df.dropna(subset=[col])
            # Ignore tiny route-object counts — a handful of routes swinging 0%->100%
            # is noise, not a real national trend.
            total_col = 'total_now' if not stack_suffix else 'total_now_v6'
            valid_rows = valid_rows[valid_rows[total_col] >= 20]

            improvers = valid_rows.sort_values(by=col, ascending=False).head(TOP_N)
            decliners = valid_rows.sort_values(by=col, ascending=True).head(TOP_N)

            print_header(f"BIGGEST MOVERS — {window} WINDOW ({stack_label}, % Valid, ROA coverage)")
            print(f"{'CC':<4} | {'Country':<20} | {'RIR':<8} | {'ASNs':<6} | {'Now':<7} | {window:<7} | {'Delta'}")
            print("-" * 85)
            print("Improvers:")
            for _, r in improvers.iterrows():
                print(f"{r['cc']:<4} | {rov_utils.cc_to_name(r['cc'])[:20]:<20} | {r['rir']:<8} | {r['asn_count']:<6.0f} | "
                      f"{r[now_col]:>5.1f}% | {r[f'valid_pct_{window}{stack_suffix}']:>5.1f}% | {r[col]:>+6.1f}pp")
            print("Decliners:")
            for _, r in decliners.iterrows():
                print(f"{r['cc']:<4} | {rov_utils.cc_to_name(r['cc'])[:20]:<20} | {r['rir']:<8} | {r['asn_count']:<6.0f} | "
                      f"{r[now_col]:>5.1f}% | {r[f'valid_pct_{window}{stack_suffix}']:>5.1f}% | {r[col]:>+6.1f}pp")

    # ------------------------------------------------------------------
    # SECTION 4: Named callout — China (the case that prompted this check-up)
    # ------------------------------------------------------------------
    print_header("SPOTLIGHT: CHINA (CN)")
    cn_row = trend_df[trend_df['cc'] == 'CN']
    if not cn_row.empty:
        r = cn_row.iloc[0]
        print(f"ASNs: {r['asn_count']:.0f}  |  RIR: {r['rir']}")
        print("IPv4:")
        for label in labels:
            pct = r['valid_pct_now'] if label == 'Now' else r.get(f'valid_pct_{label}')
            print(f"  {label:<5}: {pct:.1f}% of IPv4 route objects covered by a valid ROA" if pct is not None
                  else f"  {label:<5}: no data")
        print("IPv6:")
        for label in labels:
            pct = r['valid_pct_now_v6'] if label == 'Now' else r.get(f'valid_pct_{label}_v6')
            print(f"  {label:<5}: {pct:.1f}% of IPv6 route objects covered by a valid ROA" if pct is not None
                  else f"  {label:<5}: no data")
    else:
        print("[!] No data available for CN.")


if __name__ == "__main__":
    analyze()
