"""Audit the current stack determinant candidate table."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "stack_determinant_candidate_table_certificate.json"
NOTE = REPO / "proof_corpus" / "Stack_Determinant_Candidate_Table_v1.md"
SCRIPT = REPO / "scripts" / "compute_stack_determinant_candidate_table.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


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
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "STACK_DETERMINANT_CANDIDATE_TABLE_BUILT_QA_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate",
            approx(
                computed["hypercharge_accounting"]["weak_split"]["lambda_12"],
                cert["hypercharge_accounting"]["lambda_12"],
            )
            and approx(
                computed["diagnostic_comparison"]["required_Qa_if_Qc_and_SU2_candidates_are_kept"],
                cert["diagnostic_comparison"]["required_Qa_if_Qc_and_SU2_candidates_are_kept"],
            ),
            computed["diagnostic_comparison"],
        )
    )
    failures.append(
        not report(
            "Qa remains proxy",
            computed["candidate_table"]["Qa_SU3_stack"]["status"] == "PROXY_FINITE_PART_NOT_SELECTED"
            and computed["verdict"]["Qa_selected_determinant_closed"] is False,
            computed["candidate_table"]["Qa_SU3_stack"],
        )
    )
    failures.append(
        not report(
            "candidate undershoots diagnostic",
            computed["diagnostic_comparison"]["residual_lambda_12"] < -0.7,
            computed["diagnostic_comparison"],
        )
    )
    failures.append(
        not report(
            "required Qa gap is large",
            computed["diagnostic_comparison"]["required_Qa_minus_proxy_Qa"] > 28.0,
            computed["diagnostic_comparison"],
        )
    )
    failures.append(
        not report(
            "note records remaining determinant replacements",
            "replace the proxy p_a" in note
            and "physical quotient/projector" in note
            and "topology/index weights" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )

    print("\nStack determinant candidate table audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
