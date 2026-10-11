"""
analyze_probe_gap.py — RIPE Atlas probe coverage for one country's networks.

Forensic verification (verify_forensic_path_v2.py) needs a connected probe
inside the target network or its customer cone. This lists the country's
networks with neither, ranked by cone size and then APNIC sample count (a
proxy for eyeball traffic), so probe-hosting outreach goes where it matters.

Usage:
    python3 analyze_probe_gap.py [--cc NZ] [--contacts-out DIR] [--contacts-top N]

--contacts-out writes PeeringDB and RDAP contacts for the top uncovered
networks. Contacts are outreach material: point this outside the repo
(e.g. ~/correspondence/nz/), never at reports/.
"""
import argparse
import csv
import json
import logging
import os
import time

import pandas as pd
import requests

import rov_utils

logger = logging.getLogger(__name__)

URL_ATLAS_PROBES = "https://atlas.ripe.net/api/v2/probes/"
URL_PEERINGDB = "https://www.peeringdb.com/api"
URL_RDAP_AUTNUM = "https://rdap.org/autnum/"
PEERINGDB_DELAY_S = 3.5  # anonymous PeeringDB API allows ~20 requests/minute
DEFAULT_CONTACTS_TOP = 40


def fetch_connected_probes(cc: str) -> list[dict]:
    """All connected (status=1) Atlas probes registered in country cc."""
    probes, url = [], URL_ATLAS_PROBES
    params = {"country_code": cc, "status": 1, "page_size": 500,
              "fields": "id,asn_v4,asn_v6,is_anchor"}
    while url:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        body = resp.json()
        probes.extend(body.get("results", []))
        url, params = body.get("next"), None
    return probes


def latest_apnic_samples(asn: int) -> int:
    """Sample count of the most recent usable APNIC timeseries point (0 if none)."""
    path = os.path.join(rov_utils.DIR_APNIC_TS, f"{asn}.json")
    if not os.path.exists(path):
        return 0
    try:
        with open(path) as fh:
            raw = json.load(fh)
    except (OSError, ValueError):
        return 0
    for row in reversed(raw):
        if isinstance(row, list) and len(row) == 4 and row[1] is not None:
            return int(row[2])
        if isinstance(row, list) and len(row) == 2 and row[0] is not None:
            return int(row[1])
    return 0


def build_coverage(cc_df: pd.DataFrame, probes: list[dict], downstream: dict) -> pd.DataFrame:
    """Per-ASN probe counts inside the network and inside its customer cone."""
    by_v4, by_v6 = {}, {}
    for p in probes:
        if p.get("asn_v4"):
            by_v4[p["asn_v4"]] = by_v4.get(p["asn_v4"], 0) + 1
        if p.get("asn_v6"):
            by_v6[p["asn_v6"]] = by_v6.get(p["asn_v6"], 0) + 1

    rows = []
    for _, r in cc_df.iterrows():
        asn = int(r["asn"])
        cone_v4 = sum(by_v4.get(int(c), 0) for c in downstream.get(asn, []))
        rows.append({
            "asn": asn, "name": r["name"], "verdict": r["verdict"], "cone": int(r["cone"]),
            "probes_v4": by_v4.get(asn, 0), "probes_v6": by_v6.get(asn, 0),
            "probes_v4_in_direct_customers": cone_v4,
            "apnic_samples": latest_apnic_samples(asn),
        })
    out = pd.DataFrame(rows)
    out["covered_v4"] = (out["probes_v4"] + out["probes_v4_in_direct_customers"]) > 0
    return out.sort_values(["covered_v4", "cone", "apnic_samples"], ascending=[True, False, False])


def peeringdb_contacts(asn: int) -> list[dict]:
    """Public PeeringDB points of contact for asn (anonymous API sees public ones only)."""
    resp = requests.get(f"{URL_PEERINGDB}/net", params={"asn": asn, "depth": 2}, timeout=30)
    if resp.status_code == 404:  # network has no PeeringDB record (common for stubs)
        return []
    resp.raise_for_status()
    contacts = []
    for net in resp.json().get("data", []):
        for poc in net.get("poc_set", []):
            if poc.get("email"):
                contacts.append({"source": "peeringdb", "role": poc.get("role", ""),
                                 "name": poc.get("name", ""), "email": poc["email"]})
    return contacts


def rdap_contacts(asn: int) -> list[dict]:
    """Email contacts from RDAP entities (abuse/admin/tech roles) for asn."""
    resp = requests.get(f"{URL_RDAP_AUTNUM}{asn}", timeout=30,
                        headers={"Accept": "application/rdap+json"})
    resp.raise_for_status()
    contacts, stack = [], list(resp.json().get("entities", []))
    while stack:
        ent = stack.pop()
        stack.extend(ent.get("entities", []))
        roles = ",".join(ent.get("roles", []))
        for item in (ent.get("vcardArray") or [None, []])[1]:
            if item[0] == "email":
                contacts.append({"source": "rdap", "role": roles, "name": ent.get("handle", ""),
                                 "email": item[3]})
    return contacts


def write_contacts(gap: pd.DataFrame, out_dir: str, cc: str, top: int) -> str:
    """Fetch contacts for the top uncovered networks and write them to out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{cc.lower()}_probe_gap_contacts.csv")
    targets = gap[~gap["covered_v4"]].head(top)
    with open(path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["asn", "network", "cone", "apnic_samples",
                                                "source", "role", "name", "email"])
        writer.writeheader()
        for i, (_, r) in enumerate(targets.iterrows(), 1):
            contacts = []
            for fetch in (peeringdb_contacts, rdap_contacts):
                try:
                    contacts.extend(fetch(int(r["asn"])))
                except (requests.RequestException, ValueError) as e:
                    logger.warning("AS%s %s failed: %s", r["asn"], fetch.__name__, e)
            seen = set()
            for c in contacts:
                if c["email"].lower() in seen:
                    continue
                seen.add(c["email"].lower())
                writer.writerow({"asn": r["asn"], "network": r["name"], "cone": r["cone"],
                                 "apnic_samples": r["apnic_samples"], **c})
            print(f"    - [{i}/{len(targets)}] AS{r['asn']}: {len(seen)} contacts")
            time.sleep(PEERINGDB_DELAY_S)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--cc", default="NZ")
    parser.add_argument("--contacts-out", help="directory for the contacts CSV (outside the repo)")
    parser.add_argument("--contacts-top", type=int, default=DEFAULT_CONTACTS_TOP)
    args = parser.parse_args()
    cc = args.cc.upper()
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    df = rov_utils.load_audit_csv()
    cc_df = df[df["cc"] == cc].copy()
    cc_df["cone"] = pd.to_numeric(cc_df["cone"], errors="coerce").fillna(0).astype(int)
    _, downstream, _ = rov_utils.load_topology()

    print(f"[*] Fetching connected RIPE Atlas probes for {cc}...")
    probes = fetch_connected_probes(cc)
    gap = build_coverage(cc_df, probes, downstream)

    v4_asns = {p["asn_v4"] for p in probes if p.get("asn_v4")}
    v6_asns = {p["asn_v6"] for p in probes if p.get("asn_v6")}
    in_audit = set(cc_df["asn"].astype(int))
    print("\n" + "=" * 100)
    print(f" RIPE ATLAS PROBE COVERAGE: {cc} ({rov_utils.cc_to_name(cc)})")
    print("=" * 100)
    print(f"Connected probes:              {len(probes)}")
    print(f"Distinct IPv4 / IPv6 ASNs:     {len(v4_asns)} / {len(v6_asns)}")
    print(f"Networks in audit:             {len(cc_df)}")
    print(f"  with a probe inside (v4):    {(gap['probes_v4'] > 0).sum()}")
    print(f"  with a probe inside (v6):    {(gap['probes_v6'] > 0).sum()}")
    print(f"  testable via direct customer:{(gap['covered_v4'] & (gap['probes_v4'] == 0)).sum():>5}")
    print(f"  NOT testable (IPv4):         {(~gap['covered_v4']).sum()}")
    print(f"Probe ASNs not in {cc} audit:   {len(v4_asns - in_audit)} "
          "(probe registered in country, network registered elsewhere)")

    print("\n" + "=" * 100)
    print(" TOP 30 UNTESTABLE NETWORKS (no IPv4 probe inside or in a direct customer)")
    print("=" * 100)
    print(f"{'ASN':<10} | {'Cone':>5} | {'APNIC n':>8} | {'Verdict':<30} | Name")
    print("-" * 100)
    for _, r in gap[~gap["covered_v4"]].head(30).iterrows():
        print(f"AS{r['asn']:<8} | {r['cone']:>5} | {r['apnic_samples']:>8} | "
              f"{str(r['verdict'])[:30]:<30} | {str(r['name'])[:35]}")

    out_csv = os.path.join("reports", f"{cc.lower()}_probe_gap.csv")
    gap.to_csv(out_csv, index=False)
    print(f"\n[*] Full table: {out_csv}")

    if args.contacts_out:
        print(f"\n[*] Fetching contacts for the top {args.contacts_top} untestable networks...")
        path = write_contacts(gap, os.path.expanduser(args.contacts_out), cc, args.contacts_top)
        print(f"[*] Contacts written to {path}")


if __name__ == "__main__":
    main()
