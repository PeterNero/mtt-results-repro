"""Test the sourced co-closed one-form gauge quotient for Qa/SU3 on Nil.

The compact Nil one-form source gives a strong algebraic identity for the
p != 0 co-closed sector:

    Y_+^{k,n} Y_-^{k,n} = M_{k,n+1}^4

where M_{k,n}^2 is the scalar oscillator eigenvalue.  This script computes the
zeta-finite natural quotient terms implied by that identity and compares them
with the already computed Qa/SU3 gauge-quotient gap.

The result is a typed proof attempt, not a closure theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPECTRUM_CERT = ROOT / "certificates" / "sourced_compact_nil_scalar_spectrum_certificate.json"
SCALAR_CERT = ROOT / "certificates" / "compact_nil_scalar_hurwitz_zeta_candidate_certificate.json"
GAP_CERT = ROOT / "certificates" / "selected_qa_su3_gauge_quotient_gap_certificate.json"

BASIS = ("K3logK", "K3", "K2logK", "K2", "KlogK", "K", "logK", "constant")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def basis_values(k: float) -> list[float]:
    logk = math.log(k)
    return [k**3 * logk, k**3, k * k * logk, k * k, k * logk, k, logk, 1.0]


def least_squares(rows: list[tuple[float, float]]) -> dict[str, Any]:
    matrix = np.array([basis_values(cutoff) for cutoff, _value in rows], dtype=float)
    vector = np.array([value for _cutoff, value in rows], dtype=float)
    scales = np.linalg.norm(matrix, axis=0)
    scales[scales == 0.0] = 1.0
    scaled = matrix / scales
    scaled_coeffs, residual_array, rank, singular_values = np.linalg.lstsq(
        scaled,
        vector,
        rcond=None,
    )
    coeffs = (scaled_coeffs / scales).tolist()
    residuals = []
    for cutoff, value in rows:
        predicted = sum(c * xi for c, xi in zip(coeffs, basis_values(cutoff)))
        residuals.append(value - predicted)
    return {
        "basis": list(BASIS),
        "coefficients": dict(zip(BASIS, coeffs)),
        "finite_part_constant": coeffs[-1],
        "max_abs_residual": max(abs(item) for item in residuals),
        "rank": int(rank),
        "singular_values": [float(item) for item in singular_values],
        "residual_sum_squares": float(residual_array[0]) if len(residual_array) else 0.0,
    }


def scalar_zeta_derivative_term(k: int, c_nil: float) -> float:
    a = math.pi / (c_nil * c_nil)
    q = a * k + 0.5
    return 2.0 * k * (
        a * k * math.log(4.0 * math.pi * k)
        + math.lgamma(q)
        - 0.5 * math.log(2.0 * math.pi)
    )


def lowest_scalar_log_term(k: int, c_nil: float) -> float:
    m0 = (2.0 * math.pi * k / c_nil) ** 2 + 2.0 * math.pi * k
    return 2.0 * k * math.log(m0)


def finite_part(
    term: Callable[[int], float],
    k_min: int = 30,
    k_max: int = 120,
) -> dict[str, Any]:
    rows = []
    running = 0.0
    for k in range(1, k_max + 1):
        running += term(k)
        if k >= k_min:
            rows.append((float(k), running))
    fit = least_squares(rows)
    return {
        "cutoff_window": [k_min, k_max],
        "finite_part": fit["finite_part_constant"],
        "fit": fit,
    }


def main() -> int:
    spectrum = load(SPECTRUM_CERT)
    scalar = load(SCALAR_CERT)
    gap = load(GAP_CERT)
    c_nil = float(spectrum["selected_geometry_map"]["r_central"])

    scalar_derivative = finite_part(lambda k: scalar_zeta_derivative_term(k, c_nil))
    scalar_logdet = -float(scalar_derivative["finite_part"])
    lowest_mode_logdet = finite_part(lambda k: lowest_scalar_log_term(k, c_nil))
    lowest = float(lowest_mode_logdet["finite_part"])

    # From Y_+Y_- = M_{n+1}^4, the co-closed p!=0 one-form logdet finite
    # part is 2*(scalar_logdet - lowest_scalar_mode_logdet).
    co_closed_oneform_logdet = 2.0 * (scalar_logdet - lowest)
    oneform_minus_scalar = co_closed_oneform_logdet - scalar_logdet
    half_oneform_minus_scalar = 0.5 * co_closed_oneform_logdet - scalar_logdet
    scalar_minus_half_oneform = scalar_logdet - 0.5 * co_closed_oneform_logdet

    required_gap = float(gap["computed_gap"]["unweighted_Qa_gap"])
    candidates = {
        "co_closed_oneform_logdet": co_closed_oneform_logdet,
        "oneform_minus_scalar": oneform_minus_scalar,
        "half_oneform_minus_scalar": half_oneform_minus_scalar,
        "scalar_minus_half_oneform": scalar_minus_half_oneform,
        "lowest_scalar_mode_logdet": lowest,
    }
    candidate_comparison = {
        name: {
            "value": value,
            "difference_from_required_gap": value - required_gap,
            "absolute_difference_from_required_gap": abs(value - required_gap),
        }
        for name, value in candidates.items()
    }
    best_name = min(
        candidate_comparison,
        key=lambda name: candidate_comparison[name]["absolute_difference_from_required_gap"],
    )

    output = {
        "status": "QA_SU3_COCLOSED_ONEFORM_QUOTIENT_TESTED_NOT_CLOSED",
        "source_data": {
            "oneform_source": "arXiv:1806.05156 co-closed one-form spectrum",
            "identity": "Y_+^{k,n} Y_-^{k,n} = (M_{k,n+1}^2)^2",
            "interpretation": "The p!=0 co-closed one-form determinant is a shifted scalar oscillator determinant.",
            "c_nil": c_nil,
        },
        "finite_parts": {
            "p_nonzero_scalar_logdet": scalar_logdet,
            "lowest_scalar_mode_logdet": lowest,
            "p_nonzero_co_closed_oneform_logdet": co_closed_oneform_logdet,
            "scalar_derivative_fit": scalar_derivative,
            "lowest_mode_fit": lowest_mode_logdet,
        },
        "required_gap": {
            "unweighted_Qa_gap": required_gap,
            "lambda_12_gap": gap["computed_gap"]["lambda_12_gap"],
        },
        "natural_quotient_candidates": candidate_comparison,
        "best_natural_candidate": {
            "name": best_name,
            **candidate_comparison[best_name],
        },
        "regulator_warning": {
            "near_cutoff_artifact_seen": "A direct double-cutoff oneform-minus-scalar estimate can land near the required gap.",
            "reason_rejected": "The double-cutoff estimate uses a different regulator from the scalar Hurwitz finite part and is not stable as a selected zeta quotient.",
        },
        "verdict": {
            "co_closed_oneform_spectrum_used": True,
            "analytic_shift_identity_proved_by_source_formula": True,
            "natural_quotient_candidates_computed": True,
            "any_natural_candidate_matches_gap": candidate_comparison[best_name][
                "absolute_difference_from_required_gap"
            ]
            < 1e-3,
            "selected_Qa_SU3_operator_closed": False,
            "numeric_electroweak_closure_certified": False,
            "next_required_artifact": "Selected_Qa_SU3_Physical_Coherent_Projector_or_Endomorphism_Term_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
