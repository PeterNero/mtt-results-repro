"""Audit the selected Qa/SU3 gauge-quotient gap calculation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_gauge_quotient_gap_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Gauge_Quotient_Gap_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_gauge_quotient_gap.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    computed = run_script()
    gap = computed["computed_gap"]
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "QA_SU3_GAUGE_QUOTIENT_GAP_COMPUTED_OPERATOR_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate gap",
            abs(gap["unweighted_Qa_gap"] - cert["computed_gap"]["unweighted_Qa_gap"]) < 1e-12
            and abs(gap["lambda_12_gap"] - cert["computed_gap"]["lambda_12_gap"]) < 1e-12,
            gap,
        )
    )
    failures.append(
        not report(
            "gap is small and positive",
            0.79 < gap["unweighted_Qa_gap"] < 0.80
            and 0.06 < gap["lambda_12_gap"] < 0.07,
            gap,
        )
    )
    failures.append(
        not report(
            "gap is not selected as a fitted correction",
            computed["verdict"]["gap_computed"] is True
            and computed["verdict"]["gap_selected"] is False
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False
            and computed["verdict"]["numeric_electroweak_closure_certified"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records forbidden shortcuts",
            "not a counterterm" in note
            and "Selected_Qa_SU3_Gauge_Block_Quotient_Operator_v1" in note
            and "0.7944423933963232" in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 gauge-quotient gap audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
