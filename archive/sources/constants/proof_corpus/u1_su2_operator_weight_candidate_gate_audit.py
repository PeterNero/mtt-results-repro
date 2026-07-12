"""Audit the U1/SU2 operator-weight candidate gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "u1_su2_operator_weight_candidate_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "U1_SU2_Operator_Weight_Candidate_Gate_v1.md"
SCRIPT = REPO / "scripts" / "compute_u1_su2_operator_weight_candidates.py"


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
            cert["status"] == "U1_SU2_OPERATOR_WEIGHT_CANDIDATE_GATE_BUILT_NOT_CLOSED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate scalar split",
            approx(
                computed["input_finite_parts"]["scalar_unit_lambda_12"],
                cert["input_finite_parts"]["scalar_unit_lambda_12"],
            ),
            computed["input_finite_parts"],
        )
    )

    by_name = {row["name"]: row for row in computed["candidate_results"]}
    failures.append(
        not report(
            "scalar unit overshoots",
            by_name["scalar_unit_weights"]["residual_lambda_12"] > 0.8,
            by_name["scalar_unit_weights"],
        )
    )
    failures.append(
        not report(
            "half determinant undershoots",
            by_name["one_loop_half_scalar"]["residual_lambda_12"] < -0.6,
            by_name["one_loop_half_scalar"],
        )
    )
    failures.append(
        not report(
            "GUT 3/5 check not exact",
            0.12 < by_name["gut_hypercharge_three_fifths_u1"]["absolute_residual_lambda_12"] < 0.14,
            by_name["gut_hypercharge_three_fifths_u1"],
        )
    )
    failures.append(
        not report(
            "2/3 near hit is explicitly non-proof",
            by_name["two_thirds_u1_diagnostic"]["absolute_residual_lambda_12"] < 0.04
            and by_name["two_thirds_u1_diagnostic"]["status"] == "NEAR_HIT_DIAGNOSTIC_NOT_A_PROOF",
            by_name["two_thirds_u1_diagnostic"],
        )
    )
    failures.append(
        not report(
            "de Rham vector ghost check rejected",
            by_name["formal_de_rham_vector_ghost"]["lambda_12"] < 0
            and by_name["formal_de_rham_vector_ghost"]["status"] == "EXPLORATORY_OPERATOR_LOGIC_NOT_SELECTED",
            by_name["formal_de_rham_vector_ghost"],
        )
    )
    failures.append(
        not report(
            "reverse engineered weights forbidden",
            computed["reverse_engineered_weights_forbidden_as_proof"][
                "required_U1_weight_if_SU2_weight_is_1"
            ]
            > 0.65
            and computed["reverse_engineered_weights_forbidden_as_proof"][
                "required_SU2_weight_if_U1_weight_is_1"
            ]
            < 0
            and "forbidden" in computed["reverse_engineered_weights_forbidden_as_proof"]["reason"],
            computed["reverse_engineered_weights_forbidden_as_proof"],
        )
    )
    failures.append(
        not report(
            "note names the correct next gate",
            "Selected_U1_SU2_Gauge_Threshold_Operator_and_Weights_v1" in note
            and "source-certifies the operator and weights" in note
            and "not selected" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and computed["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        )
    )

    print("\nU1/SU2 operator-weight candidate gate audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
