"""
globalping_verify.py — the Atlas forensic test run from Globalping probes (shadow mode).

NOT USED IN VERDICTS. Results stay under data/globalping/ and in two reports until the
comparison with same-week RIPE Atlas results passes (plan/globalping_plan.md section 7).
Nothing here writes under data/atlas/, and no result carries `non_rov_hops`.

Method, per target AS:
  1. ICMP MTR (3 packets) to Cloudflare's valid beacon address from probes inside the
     target or in a direct customer (data/downstream_graph.json).
  2. The same MTR to the invalid beacon address with `locations` = the first
     measurement's ID, so the same probes answer in the same order.
  3. Results are paired by index, and the probe location records must match.
  4. Reach score = 100 * rcv / total on the hop whose address is the target; 0 when no
     hop is the target. A result that is not `finished` is no data, never "unreachable".
  5. Public hops are mapped with analyze_harvest.as_runs (iptoasn table + PeeringDB IX
     LAN holders). Globalping's own per-hop `asn` is kept as a second signal, and hops
     where the two differ are recorded.
  6. verify_forensic_path_v2._classify_probe classifies each probe, unchanged.

Storage (all under data/globalping/, gitignored):
  probes/<date>.json.gz   the day's /v1/probes list
  raw/<id>.json.gz        each measurement as Globalping returned it
  as_<ASN>.json           Atlas result schema plus source="globalping"
  runs.jsonl              one line per run (for the repeatability check)
  no_probes.json, budget.json

Usage:
  python3 globalping_verify.py                    # shadow run, default selection
  python3 globalping_verify.py --asns 9790,24324  # named targets (run even if fresh)
  python3 globalping_verify.py --cc NZ --limit 10
  python3 globalping_verify.py --dry-run          # show targets and cost, create nothing
  python3 globalping_verify.py --reanalyse        # rebuild as_<ASN>.json from raw files
  python3 globalping_verify.py --coverage         # reports/globalping_coverage.md
  python3 globalping_verify.py --compare          # reports/globalping_vs_atlas.md
"""
from __future__ import annotations

import argparse
import glob
import gzip
import ipaddress
import json
import logging
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone

import requests

import analyze_harvest
import globalping_client as gp
import rov_utils
import verify_forensic_path_v2 as forensic

logger = logging.getLogger(__name__)

SOURCE = "globalping"
BEACON_ORIGIN = forensic.CLOUDFLARE_ASN
MTR_OPTIONS = {"protocol": "ICMP", "packets": 3}
DEFAULT_BUDGET = 200       # tests a night; one test = one probe's result
PROBES_PER_TARGET = 3      # 2 MTRs each, so 6 tests a target
DEFAULT_LIMIT = DEFAULT_BUDGET // (2 * PROBES_PER_TARGET)
TTL_DAYS = rov_utils.ATLAS_TTL_DAYS
WAIT_S = 120
LOCATION_KEYS = ("continent", "region", "country", "state", "city", "asn", "network", "latitude", "longitude")


@dataclass(frozen=True)
class Paths:
    """Where inputs and outputs live. `data` is the repo's data directory."""

    data: str = rov_utils.DIR_DATA
    reports: str = "reports"

    @property
    def gp(self) -> str:
        return os.path.join(self.data, "globalping")

    @property
    def raw(self) -> str:
        return os.path.join(self.gp, "raw")

    @property
    def probes(self) -> str:
        return os.path.join(self.gp, "probes")

    @property
    def atlas(self) -> str:
        return os.path.join(self.data, "atlas")

    @property
    def graph(self) -> str:
        return os.path.join(self.data, "downstream_graph.json")

    def result(self, asn: int) -> str:
        return os.path.join(self.gp, f"as_{asn}.json")


def check_output_dir(paths: Paths) -> None:
    """Refuse an output directory inside data/atlas/: the audit globs that directory."""
    out, atlas = os.path.abspath(paths.gp), os.path.abspath(paths.atlas)
    if out == atlas or out.startswith(atlas + os.sep) or "atlas" in os.path.abspath(paths.data).split(os.sep):
        raise ValueError(f"Globalping output {out} would land under an Atlas directory")


# ── MTR parsing ──────────────────────────────────────────────────────────────

def usable(result: dict | None) -> bool:
    """True only for a finished result with hops. `failed`, `offline` and `in-progress` are no data."""
    return isinstance(result, dict) and result.get("status") == "finished" and bool(result.get("hops"))


def mtr_hops(result: dict) -> list[dict]:
    """[{ip, asn: [Globalping's ASNs], total, rcv}] for every hop, silent ones included (ip None)."""
    out = []
    for h in result.get("hops") or []:
        stats = h.get("stats") or {}
        out.append({"ip": h.get("resolvedAddress"), "asn": [int(a) for a in h.get("asn") or []],
                    "total": int(stats.get("total") or 0), "rcv": int(stats.get("rcv") or 0)})
    return out


def _same_ip(a: str, b: str) -> bool:
    try:
        return ipaddress.ip_address(a) == ipaddress.ip_address(b)
    except ValueError:
        return False


def mtr_reach(result: dict | None, target: str) -> float | None:
    """Percent of packets answered by the destination itself; None when the result is no data.

    Taken from the hop whose address is the target, never from path length: an MTR to an
    unreachable address still comes back `finished`, ending in silent hops.
    """
    if not usable(result):
        return None
    score = 0.0
    for h in mtr_hops(result):
        if h["ip"] and h["total"] > 0 and _same_ip(h["ip"], target):
            score = max(score, 100.0 * h["rcv"] / h["total"])
    return score


def public_hop_ips(hops: list[dict]) -> list[str]:
    out = []
    for h in hops:
        try:
            if h["ip"] and ipaddress.ip_address(h["ip"]).is_global:
                out.append(h["ip"])
        except ValueError:
            continue
    return out


def hop_disagreements(hops: list[dict], lookup, ix) -> list[dict]:
    """Public hops where Globalping's ASN (Team Cymru origin) differs from the local mapping
    (IX LAN holder from PeeringDB, else iptoasn). A hop Globalping has no ASN for is not listed."""
    out, seen = [], set()
    by_ip = {h["ip"]: h for h in hops if h["ip"]}
    for ip in public_hop_ips(hops):
        if ip in seen:
            continue
        seen.add(ip)
        theirs = by_ip[ip]["asn"]
        on_ix, holder = ix.lookup(ip) if ix else (False, None)
        ours = holder if on_ix else lookup.asn(ip)
        if theirs and ours not in theirs:
            out.append({"ip": ip, "local": ours, "globalping": theirs, "ix_lan": on_ix})
    return out


# ── Pairing and classification ───────────────────────────────────────────────

def same_probe(a: dict, b: dict) -> bool:
    """Globalping has no probe ID: two results are the same probe when the location records match."""
    return bool(a) and all(a.get(k) == b.get(k) for k in LOCATION_KEYS)


def pair_results(valid_m: dict, invalid_m: dict | None) -> list[dict]:
    """Pair the two measurements' results by index. `unpaired` names the reason when the
    invalid side is missing or comes from a different probe; such a pair is no data."""
    res_v = valid_m.get("results") or []
    res_i = (invalid_m or {}).get("results") or []
    pairs = []
    for i, r in enumerate(res_v):
        probe = r.get("probe") or {}
        other = res_i[i] if i < len(res_i) else None
        reason = None
        if other is None:
            reason = "no invalid result at this index"
        elif not same_probe(probe, other.get("probe") or {}):
            reason = "probe location mismatch"
        pairs.append({"index": i, "probe": probe, "valid": r.get("result") or {},
                      "invalid": (other.get("result") or {}) if other and not reason else None,
                      "unpaired": reason})
    return pairs


def network_type(tags: list[str]) -> str:
    if "eyeball-network" in tags:
        return "eyeball"
    return "datacenter" if "datacenter-network" in tags else "unknown"


def origin_adjusted(asn: int, detail: dict) -> str:
    """The probe verdict with the beacon origin ruled out as the drop point.

    _classify_probe names the first AS of the valid path that the invalid trace didn't
    reach. When that AS is Cloudflare (the origin of both beacons) it cannot be the
    filter: the invalid route ended in the AS before it. If that AS is the target, the
    target is the boundary. Kept beside the unchanged verdict, never instead of it.
    """
    path_i = detail.get("path_i") or []
    if (detail["verdict"] == "SECURE (Upstream Filtered)" and detail.get("boundary_asn") == BEACON_ORIGIN
            and path_i and path_i[-1] == asn):
        return "SECURE (Target Filtered)"
    return detail["verdict"]


def classify(asn: int, pair: dict, target_v: str, target_i: str, lookup, ix,
             customers: frozenset = frozenset()) -> dict:
    """One probe's detail record: _classify_probe's output plus Globalping provenance."""
    probe, res_v, res_i = pair["probe"], pair["valid"], pair["invalid"]
    no_data = pair["unpaired"]
    if not no_data and not usable(res_v):
        no_data = f"valid result {res_v.get('status', 'missing')}"
    if not no_data and not usable(res_i):
        no_data = f"invalid result {(res_i or {}).get('status', 'missing')}"
    hops_v = mtr_hops(res_v) if usable(res_v) else []
    hops_i = mtr_hops(res_i) if usable(res_i) else []
    if not no_data and not any(h["rcv"] for h in hops_i):
        # Not even the probe's gateway answered: the probe measured nothing. An empty invalid
        # path would otherwise read SECURE (Target Filtered) for a probe inside the target.
        no_data = "invalid result has no answering hop"
    runs_v = analyze_harvest.as_runs(public_hop_ips(hops_v), lookup, ix)
    runs_i = analyze_harvest.as_runs(public_hop_ips(hops_i), lookup, ix)
    score_v = mtr_reach(res_v, target_v)
    score_i = mtr_reach(res_i, target_i)
    if no_data:
        # No data on either side is never evidence: a zero valid score makes the classifier
        # return INCONCLUSIVE (Probe Down) whatever the paths say.
        detail = forensic._classify_probe(asn, pair["index"], [], [], 0.0, 0.0)
    else:
        detail = forensic._classify_probe(asn, pair["index"], [a for a, _ in runs_v], [a for a, _ in runs_i],
                                          score_v, score_i)
    detail.pop("non_rov_hops", None)  # known false entries on the Atlas side; never written here
    tags = list(probe.get("tags") or [])
    probe_asn = probe.get("asn")
    target_hops = sum(n for a, n in runs_v if a == asn)
    path_v = [a for a, _ in runs_v]
    detail.update({
        "result_index": pair["index"],
        "probe": {k: probe.get(k) for k in LOCATION_KEYS},
        "tags": tags,
        "network_type": network_type(tags),
        "relation": "in-target" if probe_asn == asn else "customer" if probe_asn in customers else "other",
        "no_data": no_data,
        "score_v": score_v,
        "score_i": score_i,
        "hops_v": [[h["ip"], h["asn"], h["rcv"], h["total"]] for h in hops_v],
        "hops_i": [[h["ip"], h["asn"], h["rcv"], h["total"]] for h in hops_i],
        # The probe's AS is a GeoIP guess: it counts only when a hop maps to it.
        "probe_asn_on_path": probe_asn in path_v,
        "target_hops_v": target_hops,
        # One hop in the target's space between two other ASes may be a border-router address.
        "weak_on_path": target_hops == 1 and bool(path_v) and path_v[0] != asn,
        "hop_asn_disagreements": hop_disagreements(hops_v + hops_i, lookup, ix),
        "origin_boundary": detail.get("boundary_asn") == BEACON_ORIGIN,
        # No public hop on the invalid trace: the boundary is inferred from the valid path alone.
        "empty_invalid_path": not no_data and not runs_i,
    })
    detail["verdict_origin_adjusted"] = origin_adjusted(asn, detail)
    return detail


def aggregate_verdict(counts: dict) -> str:
    """AS-level verdict from per-probe verdict counts; same precedence as forensic.analyze_results."""
    non_rov = counts.get("VULNERABLE", 0) + counts.get("SECURE (Upstream Filtered)", 0)
    secure = counts.get("SECURE (Target Filtered)", 0)
    if non_rov:
        return "VULNERABLE (Partial Deployment)" if secure else "VULNERABLE"
    if secure:
        return "SECURE (Verified Active)"
    return "INCONCLUSIVE (Divergent)" if counts.get("VULNERABLE (Bypass Route)", 0) else "INCONCLUSIVE"


def verdict_class(verdict: str | None) -> str | None:
    """SECURE / VULNERABLE / None (inconclusive), as rov_utils.load_atlas_verdicts reads a verdict."""
    v = (verdict or "").upper()
    if "VULNERABLE" in v or v == "SECURE (UPSTREAM FILTERED)":
        return "VULNERABLE"
    return "SECURE" if "SECURE" in v else None


def _count(details: list[dict], key: str) -> dict:
    counts: dict = {}
    for d in details:
        counts[d[key]] = counts.get(d[key], 0) + 1
    return counts


def iso_utc(ts: str | None) -> str:
    """Globalping's `2026-11-28T00:57:57.717Z` as an ISO string Python 3.10 can parse."""
    if not ts:
        return datetime.now(timezone.utc).isoformat()
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).isoformat()


def analyze_target(asn: int, valid_m: dict, invalid_m: dict | None, lookup, ix,
                   customers: frozenset = frozenset()) -> dict:
    """The result file for one target: Atlas result schema, `source: globalping`, no `non_rov_hops`."""
    target_v = valid_m.get("target")
    target_i = (invalid_m or {}).get("target")
    details = [classify(asn, p, target_v, target_i, lookup, ix, customers)
               for p in pair_results(valid_m, invalid_m)]
    counts = _count(details, "verdict")
    verdict = aggregate_verdict(counts)
    on_path = [d for d in details if "Off-Path" not in d["verdict"] and "Down" not in d["verdict"]]
    rep = next((d for d in on_path if d["verdict"].startswith("SECURE (Target")), on_path[0] if on_path else {})
    reasons = sorted({d["no_data"] or d["verdict"] for d in details if "INCONCLUSIVE" in d["verdict"]})
    return {
        "asn": asn,
        "source": SOURCE,
        "af": 4,
        "measurement_ids": {"mtr_valid": valid_m.get("id"), "mtr_invalid": (invalid_m or {}).get("id")},
        "targets": {"valid": target_v, "invalid": target_i},
        "probe_ids": [d["result_index"] for d in details],  # result indexes: Globalping has no probe IDs
        "verdict": verdict,
        "verdict_origin_adjusted": aggregate_verdict(_count(details, "verdict_origin_adjusted")),
        "notes": (f"{len(on_path)} of {len(details)} probes on path. "
                  f"Inconclusive: {reasons}" if reasons else f"{len(on_path)} of {len(details)} probes on path."),
        "n_vulnerable": counts.get("VULNERABLE", 0),
        "n_secure_local": counts.get("SECURE (Target Filtered)", 0),
        "n_bypass": counts.get("VULNERABLE (Bypass Route)", 0),
        "n_upstream_filtered": counts.get("SECURE (Upstream Filtered)", 0),
        "verdict_counts": counts,
        "filter_boundary": rep.get("boundary_asn"),
        "successful_probes": len(on_path),
        "total_probes": len(details),
        "probe_details": details,
        "timestamp": iso_utc(valid_m.get("createdAt")),
    }


# ── Files ────────────────────────────────────────────────────────────────────

def _write_json(path: str, obj, **kwargs) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh, **kwargs)
    os.replace(tmp, path)


def _read_json(path: str, default):
    try:
        with open(path) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def _safe_id(measurement_id) -> str:
    """Measurement IDs come from the API and become file names: letters, digits, - and _ only."""
    if not isinstance(measurement_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", measurement_id):
        raise ValueError(f"unexpected measurement id {measurement_id!r}")
    return measurement_id


def save_raw(paths: Paths, measurement: dict) -> None:
    _safe_id(measurement.get("id"))
    os.makedirs(paths.raw, exist_ok=True)
    with gzip.open(os.path.join(paths.raw, f"{measurement['id']}.json.gz"), "wt") as fh:
        json.dump(measurement, fh)


def load_raw(paths: Paths, measurement_id: str | None) -> dict | None:
    if not measurement_id:
        return None
    _safe_id(measurement_id)
    try:
        with gzip.open(os.path.join(paths.raw, f"{measurement_id}.json.gz"), "rt") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def save_probe_list(paths: Paths, probes: list[dict], today: date | None = None) -> str:
    """Keep one probe list a day: a probe is only its location record, so the list is the provenance."""
    os.makedirs(paths.probes, exist_ok=True)
    path = os.path.join(paths.probes, f"{(today or date.today()).isoformat()}.json.gz")
    if not os.path.exists(path):
        with gzip.open(path, "wt") as fh:
            json.dump(probes, fh)
    return path


def load_results(directory: str) -> dict[int, dict]:
    """{asn: result} from as_<ASN>.json files that carry a verdict and a timestamp."""
    out = {}
    for path in glob.glob(os.path.join(directory, "as_*.json")):
        d = _read_json(path, None)
        if isinstance(d, dict) and d.get("verdict") and d.get("timestamp") and d.get("asn") is not None:
            out[int(d["asn"])] = d
    return out


def age_days(result: dict, now: datetime | None = None) -> float:
    now = now or datetime.now(timezone.utc)
    try:
        return (now - datetime.fromisoformat(result["timestamp"])).total_seconds() / 86400
    except (KeyError, ValueError, TypeError):
        return float("inf")


def write_result(paths: Paths, result: dict) -> str:
    check_output_dir(paths)
    if "non_rov_hops" in result or any("non_rov_hops" in d for d in result["probe_details"]):
        raise ValueError("Globalping results must not carry non_rov_hops")
    os.makedirs(paths.gp, exist_ok=True)
    _write_json(paths.result(result["asn"]), result, indent=1)
    return paths.result(result["asn"])


def append_run(paths: Paths, result: dict) -> None:
    with open(os.path.join(paths.gp, "runs.jsonl"), "a") as fh:
        fh.write(json.dumps({k: result[k] for k in ("asn", "timestamp", "verdict", "verdict_origin_adjusted",
                                                    "measurement_ids", "successful_probes")}) + "\n")


def load_dated(path: str, today: date | None = None) -> dict[str, str]:
    """{key: ISO date} entries younger than TTL_DAYS (no_probes.json)."""
    today = today or date.today()
    out = {}
    for k, d in (_read_json(path, {}) or {}).items():
        try:
            if (today - date.fromisoformat(d)).days < TTL_DAYS:
                out[k] = d
        except (TypeError, ValueError):
            continue
    return out


def record_no_probes(paths: Paths, asn: int, today: date | None = None) -> None:
    path = os.path.join(paths.gp, "no_probes.json")
    entries = load_dated(path, today)
    entries[str(asn)] = (today or date.today()).isoformat()
    os.makedirs(paths.gp, exist_ok=True)
    _write_json(path, entries, indent=1, sort_keys=True)


# ── Budget ───────────────────────────────────────────────────────────────────

class Budget:
    """Tests left tonight: the smaller of the nightly budget (less what today's earlier runs
    spent) and what the API says remains. Updated from X-RateLimit-Remaining after each POST."""

    def __init__(self, nightly: int, spent_today: int, api_remaining: int):
        self.allowed = max(0, nightly - spent_today)
        self.api_remaining = api_remaining
        self.spent = 0

    def start_ok(self) -> bool:
        """The run starts only when the API allowance covers the whole of tonight's budget."""
        return self.allowed > 0 and self.api_remaining >= self.allowed

    def can_afford(self, tests: int) -> bool:
        return self.spent + tests <= self.allowed and tests <= self.api_remaining

    def charge(self, tests: int, header_remaining: int | None) -> None:
        self.spent += tests
        self.api_remaining = header_remaining if header_remaining is not None else self.api_remaining - tests


def spent_today(paths: Paths, today: date | None = None) -> int:
    return int((_read_json(os.path.join(paths.gp, "budget.json"), {}) or {}).get((today or date.today()).isoformat(), 0))


def record_spent(paths: Paths, tests: int, today: date | None = None) -> None:
    today = today or date.today()
    path = os.path.join(paths.gp, "budget.json")
    cutoff = (today - timedelta(days=30)).isoformat()
    book = {d: n for d, n in (_read_json(path, {}) or {}).items() if d >= cutoff}
    book[today.isoformat()] = int(book.get(today.isoformat(), 0)) + tests
    os.makedirs(paths.gp, exist_ok=True)
    _write_json(path, book, indent=1, sort_keys=True)


# ── Targets and probes ───────────────────────────────────────────────────────

def probes_by_asn(probes: list[dict]) -> dict[int, list[dict]]:
    out: dict[int, list[dict]] = defaultdict(list)
    for p in probes:
        asn = (p.get("location") or {}).get("asn")
        if asn:
            out[int(asn)].append(p)
    return dict(out)


def load_graph(paths: Paths) -> tuple[dict[int, list[int]], dict[int, set[int]]]:
    """(downstream {provider: [customers]}, providers_of {customer: {providers}})."""
    downstream = {int(k): [int(c) for c in v] for k, v in (_read_json(paths.graph, {}) or {}).items()}
    providers_of: dict[int, set[int]] = defaultdict(set)
    for provider, customers in downstream.items():
        for c in customers:
            providers_of[c].add(provider)
    return downstream, providers_of


def _has_eyeball(probes: list[dict]) -> bool:
    return any("eyeball-network" in (p.get("tags") or []) for p in probes)


def probe_locations(target: int, by_asn: dict, downstream: dict, providers_of: dict,
                    count: int = PROBES_PER_TARGET) -> list[dict]:
    """Globalping `locations` for a target, at most `count` probes.

    Order: single-homed direct customers (their traffic must cross the target), then probes
    inside the target, then multi-homed direct customers (the off-path gate discards those
    that route around it). Customers with an eyeball probe go first. One probe per customer AS.
    """
    customers = [c for c in downstream.get(target, []) if c in by_asn and c != target]

    def ranked(group: list[int]) -> list[int]:
        return sorted(group, key=lambda c: (not _has_eyeball(by_asn[c]), c))

    single = ranked([c for c in customers if len(providers_of.get(c, ())) == 1])
    multi = ranked([c for c in customers if len(providers_of.get(c, ())) > 1])
    locations: list[dict] = []
    left = count
    for c in single[:left]:
        locations.append({"asn": c, "limit": 1})
    left = count - len(locations)
    if left and target in by_asn:
        n = min(left, len(by_asn[target]))
        locations.append({"asn": target, "limit": n})
        left -= n
    for c in multi[:left]:
        locations.append({"asn": c, "limit": 1})
    return locations


def reachable(target: int, by_asn: dict, downstream: dict) -> str | None:
    """"inside", "customer" or None: where Globalping has a probe for this target."""
    if target in by_asn:
        return "inside"
    return "customer" if any(c in by_asn for c in downstream.get(target, [])) else None


def select_targets(atlas: dict[int, dict], by_asn: dict, downstream: dict, skip: set[int],
                   limit: int, now: datetime | None = None) -> list[int]:
    """Shadow-mode targets: ASes with a conclusive Atlas result no older than TTL_DAYS and a
    Globalping probe inside or in a direct customer. SECURE first (the scarce class), then
    VULNERABLE; newest Atlas result first within each, so the two tests are close in time."""
    ranked = []
    for asn, result in atlas.items():
        cls = verdict_class(result.get("verdict"))
        age = age_days(result, now)
        if cls and age <= TTL_DAYS and asn not in skip and asn != BEACON_ORIGIN and reachable(asn, by_asn, downstream):
            ranked.append((cls != "SECURE", age, asn))
    return [asn for _, _, asn in sorted(ranked)[:limit]]


def country_targets(cc: str, limit: int, skip: set[int]) -> list[int]:
    import pandas as pd
    df = rov_utils.load_audit_csv()
    df = df[df["cc"] == cc.upper()]
    cone = pd.to_numeric(df["cone"], errors="coerce").fillna(0)
    order = df.assign(cone=cone).sort_values("cone", ascending=False)["asn"]
    return [int(a) for a in order if int(a) not in skip][:limit]


# ── Run ──────────────────────────────────────────────────────────────────────

def measure_target(asn: int, locations: list[dict], ip_v: str, ip_i: str, budget: Budget,
                   paths: Paths, token: str | None = None, client=gp) -> tuple[dict, dict | None] | None:
    """Create and collect the valid MTR, then the invalid one from the same probes.

    Returns (valid, invalid) measurements, or None when no probe matched (HTTP 422).
    Raises gp.RateLimited on a 429 so the caller stops the run, and requests.HTTPError
    when the valid measurement is refused for another reason.
    """
    try:
        created = client.create_measurement(ip_v, locations, "mtr", MTR_OPTIONS, token)
    except requests.HTTPError as exc:
        if getattr(exc.response, "status_code", None) == 422:  # no probe matched the locations
            return None
        raise
    budget.charge(created.probes_count, created.rate_limit_remaining)
    valid = client.wait_for_all([created.measurement_id], WAIT_S, token=token).get(created.measurement_id)
    if not valid:
        raise requests.HTTPError(f"measurement {created.measurement_id} could not be fetched")
    save_raw(paths, valid)
    reached = any((mtr_reach(r.get("result"), ip_v) or 0.0) >= 50.0 for r in valid.get("results") or [])
    if valid.get("status") != "finished" or not reached or not budget.can_afford(created.probes_count):
        return valid, None  # no probe reached the valid beacon: an invalid test would tell nothing
    try:
        again = client.create_measurement(ip_i, created.measurement_id, "mtr", MTR_OPTIONS, token)
    except requests.HTTPError as exc:
        logger.info("    [!] AS%s invalid measurement refused: %s", asn, exc)
        return valid, None
    budget.charge(again.probes_count, again.rate_limit_remaining)
    invalid = client.wait_for_all([again.measurement_id], WAIT_S, token=token).get(again.measurement_id)
    if invalid:
        save_raw(paths, invalid)
    return valid, invalid


def choose_targets(args, paths: Paths, by_asn: dict, downstream: dict) -> list[int]:
    # A result without an invalid measurement tested nothing, so it does not hold the target back.
    fresh = {a for a, r in load_results(paths.gp).items()
             if age_days(r) < TTL_DAYS and (r.get("measurement_ids") or {}).get("mtr_invalid")}
    if args.asns:
        return [int(a.strip().upper().removeprefix("AS")) for a in args.asns.split(",") if a.strip()][:args.limit]
    skip = fresh | {int(a) for a in load_dated(os.path.join(paths.gp, "no_probes.json"))}
    if args.cc:
        return country_targets(args.cc, args.limit, skip)
    return select_targets(load_results(paths.atlas), by_asn, downstream, skip, args.limit)


def run(args, paths: Paths, client=gp) -> int:
    check_output_dir(paths)
    token = client.load_token()
    probes = client.fetch_probes(token)
    by_asn = probes_by_asn(probes)
    downstream, providers_of = load_graph(paths)
    targets = choose_targets(args, paths, by_asn, downstream)
    plan = [(asn, probe_locations(asn, by_asn, downstream, providers_of)) for asn in targets]
    cost = sum(2 * sum(loc["limit"] for loc in locs) for _, locs in plan)
    logger.info("[*] Globalping shadow run: %d targets, up to %d tests (budget %d). Not used in verdicts.",
                len(plan), cost, args.budget)
    if args.dry_run:
        for asn, locs in plan:
            logger.info("    AS%s  %s", asn, locs or "no probes")
        return 0
    save_probe_list(paths, probes)
    limits = client.get_limits(token)
    budget = Budget(args.budget, spent_today(paths), limits.remaining)
    if not budget.start_ok():
        logger.info("[!] Not starting: %d tests remain this hour (%s limit %d), tonight's budget is %d.",
                    limits.remaining, limits.kind, limits.limit, budget.allowed)
        return 0
    ip_v = forensic.resolve_ip(forensic.DOMAIN_VALID)
    ip_i = forensic.resolve_ip(forensic.DOMAIN_INVALID)
    if not ip_v or not ip_i:
        logger.info("[!] DNS resolution failed for the beacon names.")
        return 1
    lookup = analyze_harvest.load_ip2asn(os.path.join(paths.atlas, "ip2asn", "ip2asn-combined.tsv.gz"))
    ix = analyze_harvest.load_ix(os.path.join(paths.atlas, "peeringdb"))[0]
    done = 0
    try:
        for asn, locations in plan:
            if not locations:
                record_no_probes(paths, asn)
                continue
            need = 2 * sum(loc["limit"] for loc in locations)
            if not budget.can_afford(need):
                logger.info("[*] Budget reached (%d spent, %d left this hour); stopping.",
                            budget.spent, budget.api_remaining)
                break
            try:
                measured = measure_target(asn, locations, ip_v, ip_i, budget, paths, token, client)
            except requests.RequestException as exc:
                # A POST that timed out may still have been accepted: count its tests.
                if isinstance(exc, requests.Timeout):
                    budget.charge(need // 2, None)
                logger.info("    [!] AS%s skipped: %s", asn, exc)
                continue
            if not measured:
                record_no_probes(paths, asn)
                continue
            result = analyze_target(asn, measured[0], measured[1], lookup, ix, frozenset(downstream.get(asn, [])))
            write_result(paths, result)
            append_run(paths, result)
            done += 1
            logger.info("    AS%-7s %-32s adjusted: %-28s on-path %d/%d  ids %s %s", asn, result["verdict"],
                        result["verdict_origin_adjusted"], result["successful_probes"], result["total_probes"],
                        result["measurement_ids"]["mtr_valid"], result["measurement_ids"]["mtr_invalid"])
    except gp.RateLimited as exc:
        logger.info("[!] HTTP 429 from Globalping; stopping the run. %s", exc)
    finally:
        if budget.spent:
            record_spent(paths, budget.spent)
    logger.info("[+] %d targets measured, %d tests spent, %d left this hour.", done, budget.spent,
                budget.api_remaining)
    return 0


def reanalyse(paths: Paths) -> int:
    """Rebuild every as_<ASN>.json from the raw measurements it names. No requests."""
    check_output_dir(paths)
    lookup = analyze_harvest.load_ip2asn(os.path.join(paths.atlas, "ip2asn", "ip2asn-combined.tsv.gz"))
    ix = analyze_harvest.load_ix(os.path.join(paths.atlas, "peeringdb"))[0]
    downstream, _ = load_graph(paths)
    n = 0
    for asn, old in sorted(load_results(paths.gp).items()):
        ids = old.get("measurement_ids") or {}
        valid = load_raw(paths, ids.get("mtr_valid"))
        if not valid:
            logger.info("    AS%s: raw valid measurement missing, left as is", asn)
            continue
        new = analyze_target(asn, valid, load_raw(paths, ids.get("mtr_invalid")), lookup, ix,
                             frozenset(downstream.get(asn, [])))
        write_result(paths, new)
        n += 1
        if new["verdict"] != old["verdict"]:
            logger.info("    AS%s: %s -> %s", asn, old["verdict"], new["verdict"])
    logger.info("[+] Re-analysed %d results in %s", n, paths.gp)
    return 0


def main(argv: list[str] | None = None, client=gp) -> int:
    parser = argparse.ArgumentParser(description="Globalping ROV test, shadow mode (not used in verdicts).")
    parser.add_argument("--asns", help="comma-separated ASNs to test (run even with a fresh result)")
    parser.add_argument("--cc", help="test this country's networks, largest cone first")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="most targets in one run")
    parser.add_argument("--budget", type=int, default=DEFAULT_BUDGET, help="most tests a night (default 200)")
    parser.add_argument("--dry-run", action="store_true", help="show targets and cost; create nothing")
    parser.add_argument("--reanalyse", action="store_true", help="rebuild result files from raw measurements")
    parser.add_argument("--coverage", action="store_true", help="write reports/globalping_coverage.md")
    parser.add_argument("--compare", action="store_true", help="write reports/globalping_vs_atlas.md")
    parser.add_argument("--data-dir", default=rov_utils.DIR_DATA, help="data directory (default: data)")
    parser.add_argument("--reports-dir", default="reports")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    paths = Paths(args.data_dir, args.reports_dir)
    if args.coverage or args.compare:
        import globalping_report
        if args.coverage:
            globalping_report.write_coverage(paths)
        if args.compare:
            return 0 if globalping_report.write_compare(paths) is not None else 1
        return 0
    if args.reanalyse:
        return reanalyse(paths)
    return run(args, paths, client)


if __name__ == "__main__":
    sys.exit(main())
