"""
atlas_harvest.py — download other people's public RIPE Atlas measurements towards the
RPKI beacons, so their per-probe results can be compared with the audit at no credit cost.

Targets (2026-10-14): Cloudflare's invalid beacon addresses (103.21.244.9 behind
invalid.rpki.isbgpsafeyet.com; 103.21.244.19, ROVista's target), the RIPE NCC RIS
beacons (93.175.147.1 invalid, 93.175.146.1 valid) and their IPv6 counterparts.
Our own measurements (forensic engine, nz_beacon_baseline, one-off checks) are skipped.

Stopped measurements are fetched once; ongoing ones are re-fetched for the last
HARVEST_WINDOW_DAYS. Results: data/atlas/harvest/<msm_id>.json.gz plus index.json.
No API key, no credits.

Usage: python3 atlas_harvest.py [--targets ip,ip,...]
"""
import argparse
import gzip
import json
import os
import re
import time
from datetime import datetime, timedelta, timezone

import requests

import rov_utils

ATLAS_API = "https://atlas.ripe.net/api/v2"
TARGETS = ["103.21.244.9", "103.21.244.19", "93.175.147.1", "93.175.146.1",
           "2606:4700:7000::6715:f409", "2001:7fb:fd03::1", "2001:7fb:fd02::1"]
DIR_HARVEST = os.path.join(rov_utils.DIR_ATLAS, "harvest")
HARVEST_WINDOW_DAYS = 30
OURS = re.compile(r"^(RPKI (In)?[Vv]alid (Ping|Trace)|rpki_audit|RIS beacon .*rpki_audit)")
SKIP_STATUS = {"Failed", "No suitable probes", "Denied", "Scheduled", "Specified"}


def is_ours(description: str | None) -> bool:
    return bool(description) and bool(OURS.match(description))


def plan_downloads(measurements: list[dict], have: set[int]) -> list[tuple[dict, bool]]:
    """[(measurement, windowed)] to fetch: third-party, not failed; stopped ones only once."""
    plan = []
    for m in measurements:
        status = m.get("status", {}).get("name")
        if is_ours(m.get("description")) or status in SKIP_STATUS:
            continue
        if status == "Ongoing":
            plan.append((m, True))
        elif m["id"] not in have:
            plan.append((m, False))
    return plan


def list_measurements(target: str) -> list[dict]:
    fields = "id,description,type,af,status,participant_count,start_time,stop_time,interval,target"
    url = f"{ATLAS_API}/measurements/?target={target}&page_size=500&fields={fields}"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page.get("results", [])
        url = page.get("next")
    return out


def fetch_results(m: dict, windowed: bool) -> list:
    url = f"{ATLAS_API}/measurements/{m['id']}/results/?format=json"
    if windowed:
        start = int((datetime.now(timezone.utc) - timedelta(days=HARVEST_WINDOW_DAYS)).timestamp())
        url += f"&start={start}"
    resp = requests.get(url, timeout=600)
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", help="comma-separated target addresses")
    args = ap.parse_args()
    targets = args.targets.split(",") if args.targets else TARGETS
    os.makedirs(DIR_HARVEST, exist_ok=True)
    index_path = os.path.join(DIR_HARVEST, "index.json")
    index = json.load(open(index_path)) if os.path.exists(index_path) else {}
    have = {int(k) for k, v in index.items() if v.get("results") is not None}

    seen: dict[int, dict] = {}
    for t in targets:
        for m in list_measurements(t):
            seen.setdefault(m["id"], m)
        print(f"[*] {t}: {len(seen)} measurements listed so far")
    plan = plan_downloads(list(seen.values()), have)
    print(f"[*] {len(plan)} to download ({sum(w for _, w in plan)} ongoing, windowed)")

    for i, (m, windowed) in enumerate(plan, 1):
        try:
            res = fetch_results(m, windowed)
        except (requests.RequestException, ValueError) as e:
            print(f"    [!] {m['id']}: {e}")
            continue
        with gzip.open(os.path.join(DIR_HARVEST, f"{m['id']}.json.gz"), "wt") as f:
            json.dump(res, f)
        index[str(m["id"])] = {**m, "results": len(res), "windowed": windowed,
                               "fetched": datetime.now(timezone.utc).isoformat()}
        if i % 25 == 0 or i == len(plan):
            with open(index_path, "w") as f:
                json.dump(index, f, indent=1)
            print(f"    - {i}/{len(plan)} fetched")
        time.sleep(1)
    with open(index_path, "w") as f:
        json.dump(index, f, indent=1)
    print(f"[+] {index_path}: {len(index)} measurements")


if __name__ == "__main__":
    main()
