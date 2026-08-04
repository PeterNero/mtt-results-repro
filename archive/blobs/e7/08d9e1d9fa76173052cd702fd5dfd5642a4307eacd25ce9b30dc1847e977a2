"""Evaluate physical-quotient scheme candidates for stack determinants.

This script tests natural non-fitted transformations of the current stack
determinant candidate table.  It does not select a final scheme.  The point is
to separate useful structural clues from invalid target-fitting.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STACK_TABLE = ROOT / "scripts" / "compute_stack_determinant_candidate_table.py"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


def run_stack_table() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(STACK_TABLE)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def hypercharge_lambda(p_a: float, p_c: float, p_su2: float) -> tuple[float, float]:
    p_y = p_a / 36.0 + p_c / 4.0
    return p_y, p_y - p_su2


def candidate(
    name: str,
    base: dict[str, float],
    target_lambda: float,
    transforms: dict[str, float],
    status: str,
    rationale: str,
) -> dict[str, Any]:
    p_a = transforms.get("p_a", 1.0) * base["p_a"]
    p_c = transforms.get("p_c", 1.0) * base["p_c"]
    p_su2 = transforms.get("p_SU2", 1.0) * base["p_SU2"]
    p_y, lambda_12 = hypercharge_lambda(p_a, p_c, p_su2)
    return {
        "name": name,
        "status": status,
        "rationale": rationale,
        "multipliers": transforms,
        "stack_values": {"p_a": p_a, "p_c": p_c, "p_SU2": p_su2},
        "p_Y": p_y,
        "lambda_12": lambda_12,
        "residual_lambda_12": lambda_12 - target_lambda,
        "absolute_residual_lambda_12": abs(lambda_12 - target_lambda),
    }


def main() -> int:
    stack = run_stack_table()
    c1 = json.loads(C1_CERT.read_text(encoding="utf-8"))
    target_lambda = float(c1["diagnostic_expected"]["lambda_12"])
    base = {
        "p_a": float(stack["candidate_table"]["Qa_SU3_stack"]["value"]),
        "p_c": float(stack["candidate_table"]["Qc_circle_stack"]["value"]),
        "p_SU2": float(stack["candidate_table"]["SU2_stack"]["value"]),
    }

    candidates = [
        candidate(
            "current_proxy_table",
            base,
            target_lambda,
            {"p_a": 1.0, "p_c": 1.0, "p_SU2": 1.0},
            "BASELINE_PROXY_NOT_SELECTED",
            "Current proxy Qa plus exact scalar-proxy Qc/SU2 table.",
        ),
        candidate(
            "uniform_half_determinant_prefactor",
            base,
            target_lambda,
            {"p_a": 0.5, "p_c": 0.5, "p_SU2": 0.5},
            "RULED_OUT_AS_UNIVERSAL_PREFAC",
            "Equal one-loop half determinant prefactor applied to all stack entries.",
        ),
        candidate(
            "uniform_two_physical_polarizations",
            base,
            target_lambda,
            {"p_a": 2.0, "p_c": 2.0, "p_SU2": 2.0},
            "DIAGNOSTIC_NOT_SELECTED",
            "Naive two-polarization multiplier applied uniformly.",
        ),
        candidate(
            "adjoint_dimension_weights",
            base,
            target_lambda,
            {"p_a": 8.0, "p_c": 1.0, "p_SU2": 3.0},
            "DIAGNOSTIC_NOT_SELECTED",
            "Adjoint dimension weights for SU3 and SU2 with abelian factor left at one.",
        ),
        candidate(
            "adjoint_casimir_weights",
            base,
            target_lambda,
            {"p_a": 3.0, "p_c": 1.0, "p_SU2": 2.0},
            "BEST_STRUCTURAL_CLUE_NOT_SELECTED",
            "Adjoint Casimir weights C_A(SU3)=3 and C_A(SU2)=2 with abelian factor left at one.",
        ),
        candidate(
            "formal_de_rham_vector_ghost_on_qc_su2",
            base,
            target_lambda,
            {"p_a": 1.0, "p_c": -0.5, "p_SU2": 0.0},
            "RULED_OUT_FOR_THIS_PROXY_BRANCH",
            "Uses the S1/S2 de Rham vector-ghost bookkeeping for Qc/SU2 while leaving Qa proxy unchanged.",
        ),
    ]

    best = min(candidates, key=lambda item: item["absolute_residual_lambda_12"])
    output = {
        "status": "PHYSICAL_QUOTIENT_SCHEME_CANDIDATES_COMPUTED_NOT_SELECTED",
        "base_stack_values": base,
        "target_witness": {
            "lambda_12": target_lambda,
            "role": "diagnostic only, not input to selection",
        },
        "candidate_results": candidates,
        "best_structural_candidate": best,
        "verdict": {
            "candidate_schemes_evaluated": True,
            "best_candidate_selected_by_corpus": False,
            "numeric_electroweak_closure": False,
            "strongest_clue": (
                "Adjoint Casimir weighting is the nearest non-fitted structural "
                "candidate tested here, but it remains unselected."
            ),
            "next_required_computation": (
                "Derive the physical quotient heat coefficients/index weights "
                "from the selected gauge-threshold operator, rather than choosing "
                "multipliers by target proximity."
            ),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
