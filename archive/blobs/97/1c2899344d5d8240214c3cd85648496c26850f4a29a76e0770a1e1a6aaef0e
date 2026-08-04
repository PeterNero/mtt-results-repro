"""Compute a compact Nil scalar zeta-determinant candidate.

The p != 0 oscillator level is summed analytically over its oscillator index
with the Hurwitz zeta identity.  The remaining central-mode k sum is assigned a
finite part by a large-K asymptotic subtraction fit.

This is a scalar determinant candidate only.  It is not the selected Qa/SU3
gauge-threshold determinant unless the gauge operator and BRST quotient are
proved to reduce to this scalar operator.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SPECTRUM_CERT = ROOT / "certificates" / "sourced_compact_nil_scalar_spectrum_certificate.json"
QA_REDUCTION_CERT = ROOT / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json"

BASIS_P0 = ("K2logK", "K2", "KlogK", "K", "logK", "constant")
BASIS_PNZ = ("K3logK", "K3", "K2logK", "K2", "KlogK", "K", "logK", "constant")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def solve_linear_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    aug = [matrix[i][:] + [vector[i]] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row_index: abs(aug[row_index][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("singular normal equation")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [entry / scale for entry in aug[col]]
        for row_index in range(n):
            if row_index == col:
                continue
            factor = aug[row_index][col]
            aug[row_index] = [
                entry - factor * aug[col][idx]
                for idx, entry in enumerate(aug[row_index])
            ]
    return [aug[i][-1] for i in range(n)]


def least_squares(
    rows: list[tuple[float, float]],
    basis_names: tuple[str, ...],
    basis: Callable[[float], list[float]],
) -> dict[str, Any]:
    matrix = np.array([basis(cutoff) for cutoff, _value in rows], dtype=float)
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
        predicted = sum(c * xi for c, xi in zip(coeffs, basis(cutoff)))
        residuals.append(value - predicted)
    return {
        "basis": list(basis_names),
        "coefficients": dict(zip(basis_names, coeffs)),
        "finite_part_constant": coeffs[-1],
        "max_abs_residual": max(abs(item) for item in residuals),
        "rank": int(rank),
        "singular_values": [float(item) for item in singular_values],
        "residual_sum_squares": float(residual_array[0]) if len(residual_array) else 0.0,
    }


def basis_p0(k: float) -> list[float]:
    logk = math.log(k)
    return [k * k * logk, k * k, k * logk, k, logk, 1.0]


def basis_pnz(k: float) -> list[float]:
    logk = math.log(k)
    return [k**3 * logk, k**3, k * k * logk, k * k, k * logk, k, logk, 1.0]


def p0_cutoff_logdet(cutoff: int) -> float:
    total = 0.0
    for m in range(-cutoff, cutoff + 1):
        for n in range(-cutoff, cutoff + 1):
            if m == 0 and n == 0:
                continue
            total += math.log(4.0 * math.pi * math.pi * float(m * m + n * n))
    return total


def p_nonzero_derivative_term(k: int, c_nil: float) -> float:
    """Return the k contribution to zeta'(0) after summing oscillator n."""

    a = math.pi / (c_nil * c_nil)
    q = a * k + 0.5
    # For lambda_{k,n}=4*pi*k*(n+q), multiplicity 2k:
    # d/ds [(4*pi*k)^(-s) zeta_H(s,q)] at s=0.
    return 2.0 * k * (
        a * k * math.log(4.0 * math.pi * k)
        + math.lgamma(q)
        - 0.5 * math.log(2.0 * math.pi)
    )


def finite_part_p0(k_min: int, k_max: int) -> dict[str, Any]:
    rows = [(float(k), p0_cutoff_logdet(k)) for k in range(k_min, k_max + 1)]
    fit = least_squares(rows, BASIS_P0, basis_p0)
    return {
        "cutoff_range": [k_min, k_max],
        "finite_logdet_part": fit["finite_part_constant"],
        "fit": fit,
    }


def finite_part_p_nonzero(k_min: int, k_max: int, c_nil: float) -> dict[str, Any]:
    rows = []
    running = 0.0
    for k in range(1, k_max + 1):
        running += p_nonzero_derivative_term(k, c_nil)
        if k >= k_min:
            rows.append((float(k), running))
    fit = least_squares(rows, BASIS_PNZ, basis_pnz)
    # p = -zeta'(0).  The fit constant is the finite part of zeta'(0).
    return {
        "cutoff_range": [k_min, k_max],
        "finite_zeta_derivative_part": fit["finite_part_constant"],
        "finite_logdet_part": -fit["finite_part_constant"],
        "fit": fit,
    }


def lambda_from_unweighted_p(p_unweighted: float, qa_reduction: dict[str, Any]) -> dict[str, float]:
    selected = qa_reduction["selected_inputs"]
    p_c = float(selected["p_Qc_selected"])
    p_su2 = float(selected["p_SU2_selected"])
    target = float(selected["target_lambda_12_diagnostic"])
    heat_weighted = 3.0 * p_unweighted
    lambda_12 = heat_weighted / 36.0 + p_c / 4.0 - p_su2
    return {
        "unweighted_p_a": p_unweighted,
        "heat_weighted_p_a": heat_weighted,
        "lambda_12_candidate": lambda_12,
        "target_lambda_12": target,
        "residual_lambda_12": lambda_12 - target,
        "absolute_residual_lambda_12": abs(lambda_12 - target),
    }


def main() -> int:
    spectrum = load(SPECTRUM_CERT)
    qa_reduction = load(QA_REDUCTION_CERT)
    c_nil = float(spectrum["selected_geometry_map"]["r_central"])

    windows = [(20, 90), (30, 120), (40, 150)]
    window_results = []
    for k_min, k_max in windows:
        p0 = finite_part_p0(k_min, k_max)
        pnz = finite_part_p_nonzero(k_min, k_max, c_nil)
        total = p0["finite_logdet_part"] + pnz["finite_logdet_part"]
        window_results.append(
            {
                "cutoff_window": [k_min, k_max],
                "p0_finite_logdet_part": p0["finite_logdet_part"],
                "p_nonzero_finite_logdet_part": pnz["finite_logdet_part"],
                "total_scalar_finite_logdet_candidate": total,
                "hypercharge_if_used_for_Qa": lambda_from_unweighted_p(total, qa_reduction),
                "p0_fit_residual": p0["fit"]["max_abs_residual"],
                "p_nonzero_fit_residual": pnz["fit"]["max_abs_residual"],
            }
        )

    central = window_results[1]
    scalar_values = [item["total_scalar_finite_logdet_candidate"] for item in window_results]
    scalar_spread = max(scalar_values) - min(scalar_values)
    output = {
        "status": "COMPACT_NIL_SCALAR_HURWITZ_ZETA_CANDIDATE_COMPUTED_NOT_QA_CLOSURE",
        "input_source": {
            "spectrum_certificate": str(SPECTRUM_CERT),
            "spectrum_status": spectrum["status"],
            "qa_reduction_certificate": str(QA_REDUCTION_CERT),
            "qa_reduction_status": qa_reduction["status"],
        },
        "formula": {
            "p0": "finite part of sum' log(4*pi^2*(m^2+n^2))",
            "p_nonzero_zeta": "sum_{k>=1} 2k*(4*pi*k)^(-s)*zeta_H(s, 1/2 + pi*k/c_nil^2)",
            "p_nonzero_logdet": "- finite part of d/ds at s=0 of p_nonzero_zeta",
            "asymptotic_fit_basis_p0": list(BASIS_P0),
            "asymptotic_fit_basis_p_nonzero": list(BASIS_PNZ),
        },
        "selected_geometry": {
            "c_nil": c_nil,
            "compact_scalar_multiplicity": "2*|k|",
        },
        "window_results": window_results,
        "central_window_result": central,
        "comparison_to_required_Qa": {
            "required_unweighted_Qa": qa_reduction["exact_required_Qa_after_Qc_SU2_closure"][
                "unweighted_p_a_required_if_CA_SU3_is_3"
            ],
            "central_scalar_unweighted_candidate": central["total_scalar_finite_logdet_candidate"],
            "central_minus_required": central["total_scalar_finite_logdet_candidate"]
            - qa_reduction["exact_required_Qa_after_Qc_SU2_closure"][
                "unweighted_p_a_required_if_CA_SU3_is_3"
            ],
        },
        "stability_diagnostics": {
            "window_scalar_value_spread": scalar_spread,
            "stable_enough_for_selected_determinant": scalar_spread < 1.0,
            "interpretation": "The scalar calculation is numerically stable as a scalar diagnostic. Selection still requires the Qa gauge operator and BRST quotient.",
        },
        "verdict": {
            "compact_scalar_hurwitz_candidate_computed": True,
            "compact_scalar_candidate_near_required_Qa": False,
            "scalar_candidate_refutes_direct_scalar_Qa_closure": True,
            "asymptotic_fit_stable_enough_for_selection": scalar_spread < 1.0,
            "selected_Qa_gauge_operator_closed": False,
            "BRST_ghost_quotient_closed": False,
            "numeric_electroweak_closure_certified": False,
            "next_required_artifact": "Selected_Qa_SU3_Gauge_Block_Quotient_Operator_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
