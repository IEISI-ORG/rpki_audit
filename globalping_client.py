"""
globalping_client.py — minimal Globalping API client (api.globalping.io, run by jsDelivr).

Globalping works like RIPE Atlas: POST a measurement, then GET it until it finishes.
Used anonymously by default: 250 tests an hour per source IP (shared with every other
anonymous client on this host) and 50 probes per measurement. A test is one probe's
result, not one measurement. An optional `globalping_token` in secrets.yaml is sent as
a Bearer token (500 tests an hour); none is needed.

Client rules from the API spec, all followed here:
  - a descriptive User-Agent and `Accept-Encoding` on every request;
  - at most 2 GETs a second per measurement, and 500 ms between a response and the next
    GET of the same measurement;
  - ETags when polling (`If-None-Match`; a 304 means "unchanged, still running").

Globalping probes have no stable ID: a probe is known only by its location record.
Results are public and kept for about six months, with no guarantee.
"""
from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass
from typing import Any

import requests

logger = logging.getLogger(__name__)

API_BASE = "https://api.globalping.io/v1"
# Generic client name: no personal details go to outside services.
USER_AGENT = "rov-audit-measurement-client"
SECRETS_FILE = "secrets.yaml"
TIMEOUT_S = 30
MIN_POLL_GAP_S = 0.5  # spec: wait 500 ms after a response before the next GET of that measurement


class RateLimited(RuntimeError):
    """Globalping refused a request with HTTP 429 (hourly test limit reached)."""


@dataclass(frozen=True)
class Created:
    """A measurement Globalping accepted."""

    measurement_id: str
    probes_count: int
    rate_limit_remaining: int | None


@dataclass(frozen=True)
class Limits:
    """GET /v1/limits: the allowance for creating measurements (tests per hour)."""

    kind: str  # "ip" (anonymous) or "user" (token)
    limit: int
    remaining: int
    reset_s: int


def load_token(path: str = SECRETS_FILE) -> str | None:
    """`globalping_token` from secrets.yaml, or None (anonymous)."""
    if not os.path.exists(path):
        return None
    try:
        import yaml
        with open(path) as fh:
            token = (yaml.safe_load(fh) or {}).get("globalping_token")
    except (OSError, ValueError, ImportError, AttributeError) as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return None
    return str(token) if token else None


def _headers(token: str | None = None) -> dict[str, str]:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json", "Accept-Encoding": "gzip, br"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _int_header(response: requests.Response, name: str) -> int | None:
    try:
        return int(response.headers.get(name, ""))
    except (TypeError, ValueError):
        return None


def fetch_probes(token: str | None = None) -> list[dict]:
    """Every probe online now, as Globalping lists them (no test cost, no limit)."""
    response = requests.get(f"{API_BASE}/probes", headers=_headers(token), timeout=TIMEOUT_S)
    response.raise_for_status()
    return response.json()


def get_limits(token: str | None = None) -> Limits:
    """The current allowance for creating measurements (no test cost)."""
    response = requests.get(f"{API_BASE}/limits", headers=_headers(token), timeout=TIMEOUT_S)
    response.raise_for_status()
    create = response.json()["rateLimit"]["measurements"]["create"]
    return Limits(str(create.get("type", "")), int(create["limit"]), int(create["remaining"]),
                  int(create.get("reset") or 0))


def create_measurement(target: str, locations: list[dict] | str, mtype: str = "mtr",
                       options: dict | None = None, token: str | None = None) -> Created:
    """Create one measurement to `target`.

    `locations` is a list of location filters, each with its own `limit` (Globalping
    rejects a global `limit` next to per-location ones), or the ID of an earlier
    measurement: the same probes are reused in the same order, and one that has gone
    is reported `offline`. `ipVersion` is never sent: it applies to hostnames only and
    targets here are IP literals.

    Raises:
        RateLimited: on HTTP 429.
        requests.HTTPError: on any other error status.
    """
    body: dict[str, Any] = {"type": mtype, "target": target, "locations": locations}
    if options:
        body["measurementOptions"] = options
    response = requests.post(f"{API_BASE}/measurements", json=body, headers=_headers(token), timeout=TIMEOUT_S)
    if response.status_code == 429:
        raise RateLimited(response.text[:300])
    if response.status_code >= 400:
        raise requests.HTTPError(f"{response.status_code} from Globalping: {response.text[:300]}",
                                 response=response)
    payload = response.json()
    return Created(payload["id"], int(payload.get("probesCount") or 0),
                   _int_header(response, "X-RateLimit-Remaining"))


def fetch_measurement(measurement_id: str, etag: str | None = None,
                      token: str | None = None) -> tuple[dict | None, str | None]:
    """(measurement, etag). The measurement is None on 304 Not Modified (pass the last ETag)."""
    headers = _headers(token)
    if etag:
        headers["If-None-Match"] = etag
    response = requests.get(f"{API_BASE}/measurements/{measurement_id}", headers=headers, timeout=TIMEOUT_S)
    if response.status_code == 304:
        return None, etag
    if response.status_code == 429:
        raise RateLimited(response.text[:300])
    response.raise_for_status()
    return response.json(), response.headers.get("ETag")


def wait_for_all(measurement_ids: list[str], timeout_s: float = 300, poll_s: float = 2.0,
                 token: str | None = None) -> dict[str, dict]:
    """Poll every measurement until it leaves `in-progress` or `timeout_s` passes.

    One GET per measurement per round, rounds at least `poll_s` apart and never closer
    than MIN_POLL_GAP_S to that measurement's last response. A measurement still running
    at the deadline is returned as last seen (its unfinished results carry their own
    `in-progress` status, which callers must treat as no data); one never fetched is
    left out.
    """
    gap = max(poll_s, MIN_POLL_GAP_S)
    pending = list(measurement_ids)
    done: dict[str, dict] = {}
    last_seen: dict[str, dict] = {}
    etags: dict[str, str | None] = {}
    next_ok: dict[str, float] = {}
    deadline = time.monotonic() + timeout_s
    while pending and time.monotonic() < deadline:
        still: list[str] = []
        for measurement_id in pending:
            wait = next_ok.get(measurement_id, 0.0) - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            if time.monotonic() >= deadline:
                still.append(measurement_id)
                continue
            try:
                measurement, etags[measurement_id] = fetch_measurement(
                    measurement_id, etags.get(measurement_id), token)
            except RateLimited:
                raise
            except requests.RequestException as exc:
                logger.warning("Globalping %s poll failed, will retry: %s", measurement_id, exc)
                measurement = None
            next_ok[measurement_id] = time.monotonic() + gap
            if measurement is None:
                still.append(measurement_id)
            elif measurement.get("status") == "in-progress":
                last_seen[measurement_id] = measurement
                still.append(measurement_id)
            else:
                done[measurement_id] = measurement
        pending = still
    if pending:
        logger.warning("Globalping: %d measurement(s) unfinished at timeout", len(pending))
    for measurement_id in pending:
        if measurement_id in last_seen:
            done[measurement_id] = last_seen[measurement_id]
    return done
