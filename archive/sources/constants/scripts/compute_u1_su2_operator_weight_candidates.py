"""Evaluate non-fitted U1/SU2 gauge-threshold operator/weight candidates.

This script does not select the final electroweak threshold operator.  It
uses the exact scalar-proxy U1 circle and SU2 sphere finite parts as inputs
and compares several source-motivated operator/weight transforms against the
diagnostic C1 target.

Near numerical agreement is reported only as a diagnostic.  It is not a
prediction unless the operator and weights are independently selected.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


def run_circle_sphere() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(CIRCLE_SPHERE)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def delta_g(v1_tilde: float, lambda_12: float) -> float:
    return v1_tilde * lambda_12 / (4.0 * math.pi)


def weighted_candidate(
    name: str,
    u1_piece: float,
    su2_piece: float,
    target_lambda: float,
    v1_tilde: float,
    u1_weight: float,
    su2_weight: float,
    status: str,
    rationale: str,
) -> dict[str, Any]:
    lambda_12 = u1_weight * u1_piece - su2_weight * su2_piece
    return {
        "name": name,
        "status": status,
        "rationale": rationale,
        "operator_model": "weighted exact scalar-proxy determinant",
        "weights": {"U1": u1_weight, "SU2": su2_weight},
        "lambda_12": lambda_12,
        "Delta_G_12": delta_g(v1_tilde, lambda_12),
        "residual_lambda_12": lambda_12 - target_lambda,
        "absolute_residual_lambda_12": abs(lambda_12 - target_lambda),
    }


def vector_ghost_de_rham_candidate(
    u1_piece: float,
    target_lambda: float,
    v1_tilde: float,
) -> dict[str, Any]:
    # For de Rham Hodge spectra on S1, det' Delta_1 = det' Delta_0.
    # For S2, the non-harmonic Hodge one-form determinant is two scalar
    # copies.  The formal gauge-fixed combination 1/2 log det Delta_1
    # - log det Delta_0 therefore gives -1/2 scalar on S1 and 0 on S2.
    lambda_12 = -0.5 * u1_piece
    return {
        "name": "formal_de_rham_vector_ghost",
        "status": "EXPLORATORY_OPERATOR_LOGIC_NOT_SELECTED",
        "rationale": (
            "Gauge-fixed de Rham determinant bookkeeping check; useful as an "
            "operator sanity test, but not selected as the MTT threshold "
            "operator."
        ),
        "operator_model": "1/2 log det Delta_1 - log det Delta_0",
        "weights": {"U1_effective_scalar_piece": -0.5, "SU2_effective_scalar_piece": 0.0},
        "lambda_12": lambda_12,
        "Delta_G_12": delta_g(v1_tilde, lambda_12),
        "residual_lambda_12": lambda_12 - target_lambda,
        "absolute_residual_lambda_12": abs(lambda_12 - target_lambda),
    }


def rational_scan(
    u1_piece: float,
    su2_piece: float,
    target_lambda: float,
    max_denominator: int = 12,
    top_k: int = 8,
) -> list[dict[str, Any]]:
    rationals = sorted(
        {
            Fraction(n, d)
            for d in range(1, max_denominator + 1)
            for n in range(0, 2 * max_denominator + 1)
            if Fraction(n, d) <= 2
        }
    )
    rows: list[tuple[float, Fraction, Fraction, float]] = []
    for u1_weight in rationals:
        for su2_weight in rationals:
            lambda_12 = float(u1_weight) * u1_piece - float(su2_weight) * su2_piece
            rows.append((abs(lambda_12 - target_lambda), u1_weight, su2_weight, lambda_12))
    rows.sort(key=lambda row: row[0])
    return [
        {
            "U1": f"{u1_weight.numerator}/{u1_weight.denominator}",
            "SU2": f"{su2_weight.numerator}/{su2_weight.denominator}",
            "lambda_12": lambda_12,
            "absolute_residual_lambda_12": residual,
        }
        for residual, u1_weight, su2_weight, lambda_12 in rows[:top_k]
    ]


def main() -> int:
    pieces = run_circle_sphere()
    c1 = json.loads(C1_CERT.read_text(encoding="utf-8"))
    u1 = float(pieces["finite_parts"]["U1_circle"])
    su2 = float(pieces["finite_parts"]["SU2_effective_sphere"])
    target_lambda = float(c1["diagnostic_expected"]["lambda_12"])
    v1_tilde = float(c1["selected_values"]["v1_tilde"])

    candidates = [
        weighted_candidate(
            "scalar_unit_weights",
            u1,
            su2,
            target_lambda,
            v1_tilde,
            1.0,
            1.0,
            "EXACT_PROXY_CLOSED_NOT_FINAL",
            "Exact U1/SU2 scalar zeta pieces with unit diagnostic weights.",
        ),
        weighted_candidate(
            "one_loop_half_scalar",
            u1,
            su2,
            target_lambda,
            v1_tilde,
            0.5,
            0.5,
            "STANDARD_PREFAC_CHECK_NOT_SELECTED",
            "Formal half-determinant prefactor applied equally to both scalar proxy pieces.",
        ),
        weighted_candidate(
            "gut_hypercharge_three_fifths_u1",
            u1,
            su2,
            target_lambda,
            v1_tilde,
            3.0 / 5.0,
            1.0,
            "SOURCE_MOTIVATED_NORMALIZATION_NOT_SELECTED_HERE",
            "Common GUT hypercharge normalization check; admissible only if selected by the MTT branch.",
        ),
        weighted_candidate(
            "two_thirds_u1_diagnostic",
            u1,
            su2,
            target_lambda,
            v1_tilde,
            2.0 / 3.0,
            1.0,
            "NEAR_HIT_DIAGNOSTIC_NOT_A_PROOF",
            "Simple rational U1 suppression close to the target; currently lacks an independent source theorem.",
        ),
        vector_ghost_de_rham_candidate(u1, target_lambda, v1_tilde),
    ]

    required_u1_weight_with_su2_unit = (target_lambda + su2) / u1
    required_su2_weight_with_u1_unit = (u1 - target_lambda) / su2

    output = {
        "status": "U1_SU2_OPERATOR_WEIGHT_CANDIDATE_GATE_BUILT_NOT_CLOSED",
        "input_finite_parts": {
            "U1_circle": u1,
            "SU2_effective_sphere": su2,
            "scalar_unit_lambda_12": u1 - su2,
        },
        "target_witness": {
            "lambda_12": target_lambda,
            "Delta_G_12": float(c1["diagnostic_expected"]["Delta_G_12"]),
            "role": "diagnostic witness only, not an input to selection",
        },
        "candidate_results": candidates,
        "reverse_engineered_weights_forbidden_as_proof": {
            "required_U1_weight_if_SU2_weight_is_1": required_u1_weight_with_su2_unit,
            "required_SU2_weight_if_U1_weight_is_1": required_su2_weight_with_u1_unit,
            "reason": "These are solved from the diagnostic target and are forbidden as no-knob selection data.",
        },
        "small_rational_scan_for_diagnostics_only": rational_scan(u1, su2, target_lambda),
        "verdict": {
            "operator_weight_gate_built": True,
            "scalar_proxy_overshoot_explained": True,
            "near_hit_is_not_closure": True,
            "numeric_electroweak_closure": False,
            "next_required_computation": (
                "Source-certify the U1/SU2 gauge-threshold operator and "
                "topology/index weights before comparing to the electroweak target."
            ),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
