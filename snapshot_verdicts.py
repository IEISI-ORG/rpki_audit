"""
snapshot_verdicts.py

Appends one row per day to logs/verdict_counts.csv: verdict classes, evidence
rungs (`decided_by`) and IPv6 classes from the audit CSV, plus the modification
times of the audit and the topology graph. Day-to-day drift in the SECURE count
can then be matched to a topology rebuild or a new evidence rule. A second run on
the same day replaces that day's row. Run by do_reports right after the audit.
"""
import csv
import os
import subprocess
import sys
from collections import Counter
from datetime import date, datetime

import rov_utils

FILE_SNAPSHOT = "logs/verdict_counts.csv"
CLASSES = ("SECURE", "VULNERABLE", "PARTIAL", "UNKNOWN")
RUNGS = ("policy", "atlas", "apnic", "declared", "none")
FIELDS = (
    ["run_date", "audit_mtime", "graph_mtime", "git_head", "rows"]
    + list(CLASSES)
    + ["REGRESSED", "INCONSISTENT"]
    + [f"decided_{r}" for r in RUNGS]
    + ["v6_rows"] + [f"v6_{c}" for c in CLASSES]
    + ["rovista_fresh"]
)


def _mtime(path: str) -> str:
    """Modification time as 'YYYY-MM-DD HH:MM', blank if the file is missing."""
    if not os.path.exists(path):
        return ""
    return datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")


def _git_head() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip()


def count_verdicts(rows: list[dict]) -> dict:
    """Counts for one audit: verdict classes, deciding rungs and IPv6 classes."""
    classes = Counter(rov_utils.classify_verdict(r.get("verdict", "")) for r in rows)
    labels = Counter(r.get("verdict", "") for r in rows)
    rungs = Counter(r.get("decided_by", "") for r in rows)
    v6 = [r["v6_verdict"] for r in rows if r.get("v6_verdict")]
    v6_classes = Counter(rov_utils.classify_verdict(v) for v in v6)
    rovista = sum(1 for r in rows if r.get("rovista_score", "-1") not in ("", "-1", "-1.0"))

    counts = {"rows": len(rows)}
    counts.update({c: classes.get(c, 0) for c in CLASSES})
    counts.update({"REGRESSED": labels.get("REGRESSED", 0),
                   "INCONSISTENT": labels.get("INCONSISTENT", 0)})
    counts.update({f"decided_{r}": rungs.get(r, 0) for r in RUNGS})
    counts["v6_rows"] = len(v6)
    counts.update({f"v6_{c}": v6_classes.get(c, 0) for c in CLASSES})
    counts["rovista_fresh"] = rovista
    return counts


def write_snapshot(row: dict, path: str = FILE_SNAPSHOT) -> None:
    """Add `row` to the snapshot file, replacing any row with the same run_date."""
    kept = []
    if os.path.exists(path):
        with open(path, newline="") as fh:
            kept = [r for r in csv.DictReader(fh) if r.get("run_date") != row["run_date"]]
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(kept + [row], key=lambda r: r["run_date"]))
    os.replace(tmp, path)


def main(audit: str = rov_utils.FILE_AUDIT_FINAL, path: str = FILE_SNAPSHOT,
         today: date | None = None) -> int:
    if not os.path.exists(audit):
        print(f"[!] {audit} not found; no verdict snapshot written")
        return 1
    with open(audit, newline="") as fh:
        rows = list(csv.DictReader(fh))
    row = {"run_date": (today or date.today()).isoformat(),
           "audit_mtime": _mtime(audit),
           "graph_mtime": _mtime(rov_utils.FILE_GRAPH),
           "git_head": _git_head()}
    row.update(count_verdicts(rows))
    write_snapshot(row, path)
    print(f"[+] {path}: {row['run_date']} SECURE {row['SECURE']:,} "
          f"VULNERABLE {row['VULNERABLE']:,} PARTIAL {row['PARTIAL']:,} "
          f"UNKNOWN {row['UNKNOWN']:,} (graph {row['graph_mtime']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
