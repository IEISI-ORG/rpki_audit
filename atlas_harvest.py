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

At most MAX_PER_RUN (500) measurements per run, not-yet-fetched ones first, so a daily run works
through the backlog. Each response is read in chunks and abandoned above MAX_RESPONSE_BYTES
(recorded as skipped, not retried): on 2026-10-15 a one-off, one-probe measurement (185673939)
returned ~4.3 GB, which the old code read whole into memory during the host's first memory
near-miss that morning. Run it alone and capped (systemd-run MemoryMax), per CLAUDE.md.

Usage: python3 atlas_harvest.py [--targets ip,ip,...] [--max N]
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
MAX_PER_RUN = 500
MAX_RESPONSE_BYTES = 100_000_000   # largest saved so far: 3.4 MB gzipped
OURS = re.compile(r"^(RPKI (In)?[Vv]alid (Ping|Trace)|rpki_audit|RIS beacon .*rpki_audit)")
SKIP_STATUS = {"Failed", "No suitable probes", "Denied", "Scheduled", "Specified"}


def is_ours(description: str | None) -> bool:
    return bool(description) and bool(OURS.match(description))


class ResponseTooLarge(ValueError):
    pass


def plan_downloads(measurements: list[dict], have: set[int], skip: set[int] = frozenset(),
                   limit: int = MAX_PER_RUN) -> list[tuple[dict, bool]]:
    """[(measurement, windowed)] to fetch, at most limit: third-party, not failed, not skipped
    before; stopped ones only once. Not-yet-fetched stopped ones come before ongoing re-fetches."""
    new, ongoing = [], []
    for m in measurements:
        status = m.get("status", {}).get("name")
        if is_ours(m.get("description")) or status in SKIP_STATUS or m["id"] in skip:
            continue
        if status == "Ongoing":
            ongoing.append((m, True))
        elif m["id"] not in have:
            new.append((m, False))
    return (new + ongoing)[:limit]


def read_capped(chunks, cap: int = MAX_RESPONSE_BYTES) -> bytes:
    """Join response chunks; raise ResponseTooLarge as soon as more than cap bytes arrive."""
    buf, n = [], 0
    for c in chunks:
        n += len(c)
        if n > cap:
            raise ResponseTooLarge(f"response over {cap:,} bytes")
        buf.append(c)
    return b"".join(buf)


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
    with requests.get(url, timeout=600, stream=True) as resp:
        resp.raise_for_status()
        return json.loads(read_capped(resp.iter_content(chunk_size=1 << 20)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", help="comma-separated target addresses")
    ap.add_argument("--max", type=int, default=MAX_PER_RUN, help="measurements to fetch this run")
    args = ap.parse_args()
    targets = args.targets.split(",") if args.targets else TARGETS
    os.makedirs(DIR_HARVEST, exist_ok=True)
    index_path = os.path.join(DIR_HARVEST, "index.json")
    index = json.load(open(index_path)) if os.path.exists(index_path) else {}
    have = {int(k) for k, v in index.items() if v.get("results") is not None}
    skip = {int(k) for k, v in index.items() if v.get("skipped")}

    seen: dict[int, dict] = {}
    for t in targets:
        for m in list_measurements(t):
            seen.setdefault(m["id"], m)
        print(f"[*] {t}: {len(seen)} measurements listed so far")
    plan = plan_downloads(list(seen.values()), have, skip, limit=args.max)
    print(f"[*] {len(plan)} to download this run (limit {args.max}; "
          f"{sum(w for _, w in plan)} ongoing, windowed)")

    for i, (m, windowed) in enumerate(plan, 1):
        try:
            res = fetch_results(m, windowed)
        except ResponseTooLarge as e:
            print(f"    [!] {m['id']}: {e}; skipped for good")
            index[str(m["id"])] = {**m, "results": None, "skipped": str(e),
                                   "fetched": datetime.now(timezone.utc).isoformat()}
            continue
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
