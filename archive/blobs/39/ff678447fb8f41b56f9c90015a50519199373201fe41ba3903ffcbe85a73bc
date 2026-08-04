"""Audit the selected gauge-threshold heat-kernel theorem reduction."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_gauge_threshold_operator_heat_kernel_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Gauge_Threshold_Operator_Heat_Kernel_Theorem_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_gauge_threshold_operator_heat_kernel_theorem.py"


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
            cert["status"] == "GAUGE_THRESHOLD_OPERATOR_HEAT_KERNEL_THEOREM_REDUCED_NOT_PROVED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate candidate",
            approx(
                computed["current_numeric_candidate"]["heat_weighted_lambda_12"],
                cert["current_numeric_candidate"]["heat_weighted_lambda_12"],
            )
            and approx(
                computed["current_numeric_candidate"]["heat_weighted_Delta_G_12"],
                cert["current_numeric_candidate"]["heat_weighted_Delta_G_12"],
            ),
            computed["current_numeric_candidate"],
        )
    )
    failures.append(
        not report(
            "four theorem obligations are exposed",
            set(computed["obligations"]) == {
                "O1_selected_gauge_threshold_operator",
                "O2_heat_trace_index_weights",
                "O3_finite_stack_determinants",
                "O4_retarded_kernel_c1_normalization",
            },
            list(computed["obligations"]),
        )
    )
    failures.append(
        not report(
            "operator theorem remains open",
            computed["verdict"]["operator_theorem_closed"] is False
            and computed["verdict"]["gauge_factor_resolved_operator_selected"] is False
            and computed["verdict"]["finite_stack_determinants_selected"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "Casimir coefficient branch remains conditional",
            computed["obligations"]["O2_heat_trace_index_weights"]["current_status"] == "CONDITIONAL_CANDIDATE"
            and computed["verdict"]["casimir_coefficients_derived_from_operator"] is False,
            computed["obligations"]["O2_heat_trace_index_weights"],
        )
    )
    failures.append(
        not report(
            "note names constructive next block artifact",
            "Selected_Qa_Qc_SU2_Gauge_Threshold_Operator_Blocks_v1" in note
            and "D_Qa" in note
            and "D_Qc" in note
            and "D_SU2" in note
            and "not proved" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "no new no-knob prediction claimed",
            cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )

    print("\nSelected gauge-threshold heat-kernel theorem audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
