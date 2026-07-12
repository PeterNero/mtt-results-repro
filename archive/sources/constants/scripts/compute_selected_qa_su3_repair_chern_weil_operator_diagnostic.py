"""Compare repaired Qa/SU3 HYM candidates against Chern-Weil diagnostics.

The previous gate found two algebraic repairs for the printed connection.
This script tests their next consequences without treating either repair as
source-certified.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AB_CERT = ROOT / "certificates" / "selected_qa_su3_repaired_pipeline_ab_diagnostic_comparison_certificate.json"
RADIUS_CERT = ROOT / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def elementary(row: int, col: int) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    matrix[row - 1, col - 1] = 1.0
    return matrix


def connection_matrices(mu: float, variant: str) -> list[np.ndarray]:
    s = math.sqrt(mu)
    if variant == "repair_A_diagonal_B3":
        return [
            s * elementary(1, 3),
            -s * elementary(3, 1),
            mu * (elementary(1, 1) - elementary(3, 3)),
        ]
    if variant == "repair_B_move_B2":
        return [
            s * elementary(1, 3),
            -s * elementary(3, 2),
            mu * elementary(1, 2),
        ]
    raise ValueError(f"unknown variant: {variant}")


def metric_weights(radius_cert: dict[str, Any]) -> list[float]:
    values = radius_cert["selected_values"]
    r1 = float(values["R_star"])
    r2 = r1
    r3 = float(values["r3"])
    return [1.0 / r1**2, 1.0 / r2**2, 1.0 / r3**2]


def frobenius_squared(matrix: np.ndarray) -> float:
    return float(np.real(np.trace(matrix.conj().T @ matrix)))


def f02_residual(mu: float, variant: str) -> np.ndarray:
    b1, b2, b3 = connection_matrices(mu, variant)
    return b3 + b1 @ b2 - b2 @ b1


def f11_blocks(mu: float, variant: str) -> list[list[np.ndarray]]:
    matrices = connection_matrices(mu, variant)
    blocks = []
    for b_i in matrices:
        row = []
        a10_i = -b_i.conj().T
        for b_j in matrices:
            row.append(a10_i @ b_j - b_j @ a10_i)
        blocks.append(row)
    return blocks


def primitive_contraction(mu: float, variant: str, weights: list[float]) -> np.ndarray:
    blocks = f11_blocks(mu, variant)
    total = np.zeros((3, 3), dtype=complex)
    for i, weight in enumerate(weights):
        total += weight * blocks[i][i]
    return total


def wedge_sign(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, tuple[int, ...]] | None:
    if set(left).intersection(right):
        return None
    merged = list(left) + list(right)
    inversions = 0
    for i, a in enumerate(merged):
        for b in merged[i + 1 :]:
            if a > b:
                inversions += 1
    return (-1 if inversions % 2 else 1), tuple(sorted(merged))


def matrix_form_f11(mu: float, variant: str) -> dict[tuple[int, int], np.ndarray]:
    blocks = f11_blocks(mu, variant)
    terms: dict[tuple[int, int], np.ndarray] = {}
    for i in range(3):
        for j in range(3):
            terms[(i, 3 + j)] = blocks[i][j]
    return terms


def wedge_power_trace_coefficients(
    terms: dict[tuple[int, ...], np.ndarray], power: int
) -> dict[tuple[int, ...], complex]:
    current: dict[tuple[int, ...], np.ndarray] = {(): np.eye(3, dtype=complex)}
    for _ in range(power):
        nxt: dict[tuple[int, ...], np.ndarray] = {}
        for left_form, left_matrix in current.items():
            for right_form, right_matrix in terms.items():
                wedge = wedge_sign(left_form, right_form)
                if wedge is None:
                    continue
                sign, form = wedge
                nxt[form] = nxt.get(form, np.zeros((3, 3), dtype=complex)) + sign * (
                    left_matrix @ right_matrix
                )
        current = nxt
    return {form: complex(np.trace(matrix)) for form, matrix in current.items()}


def trace_norm_squared(coefficients: dict[tuple[int, ...], complex]) -> float:
    return float(sum(abs(value) ** 2 for value in coefficients.values()))


def serialize_matrix(matrix: np.ndarray) -> list[list[float]]:
    return [[float(np.real(value)) for value in row] for row in matrix]


def sample_variant(variant: str, weights: list[float]) -> dict[str, Any]:
    samples = []
    for mu in [0.25, 1.0, 4.0]:
        terms = matrix_form_f11(mu, variant)
        trace_f = {form: complex(np.trace(matrix)) for form, matrix in terms.items()}
        trace_f2 = wedge_power_trace_coefficients(terms, 2)
        trace_f3 = wedge_power_trace_coefficients(terms, 3)
        primitive = primitive_contraction(mu, variant, weights)
        top_form = tuple(range(6))
        samples.append(
            {
                "mu": mu,
                "F02_residual_norm_squared": frobenius_squared(f02_residual(mu, variant)),
                "primitive_contraction": serialize_matrix(primitive),
                "primitive_contraction_norm_squared": frobenius_squared(primitive),
                "trace_F_norm_squared": trace_norm_squared(trace_f),
                "trace_F2_norm_squared": trace_norm_squared(trace_f2),
                "trace_F3_top_coefficient_real": float(np.real(trace_f3.get(top_form, 0.0))),
                "trace_F3_top_coefficient_imag": float(np.imag(trace_f3.get(top_form, 0.0))),
                "trace_F3_norm_squared": trace_norm_squared(trace_f3),
            }
        )
    return {
        "variant": variant,
        "samples": samples,
        "integrable_on_samples": all(sample["F02_residual_norm_squared"] <= 1e-12 for sample in samples),
        "primitive_on_samples": all(
            sample["primitive_contraction_norm_squared"] <= 1e-12 for sample in samples
        ),
        "trace_F_zero_on_samples": all(sample["trace_F_norm_squared"] <= 1e-12 for sample in samples),
        "trace_F2_zero_on_samples": all(sample["trace_F2_norm_squared"] <= 1e-12 for sample in samples),
        "trace_F3_nonzero_on_samples": any(
            sample["trace_F3_norm_squared"] > 1e-12 for sample in samples
        ),
    }


def main() -> int:
    ab = load(AB_CERT)
    radius = load(RADIUS_CERT)
    weights = metric_weights(radius)
    variants = [
        sample_variant("repair_A_diagonal_B3", weights),
        sample_variant("repair_B_move_B2", weights),
    ]
    by_name = {variant["variant"]: variant for variant in variants}
    output = {
        "certificate": "SelectedQaSU3RepairChernWeilOperatorDiagnostic",
        "status": "QA_SU3_REPAIR_CHERN_WEIL_OPERATOR_DIAGNOSTIC_SPLIT_NO_CLOSURE",
        "input_status": {
            "ab_diagnostic": ab["status"],
            "selected_radius": radius["status"],
        },
        "scope": {
            "included": [
                "standard left-invariant F02 integrability residual",
                "F11 commutator blocks [-B_i^*, B_j]",
                "selected Iwasawa metric-weighted primitive contraction",
                "algebraic trace F, trace F wedge F, and trace F wedge F wedge F coefficients",
            ],
            "not_included": [
                "source-certified erratum text",
                "torsional R_+ derivative corrections",
                "full BRST gauge-fixed determinant",
                "normalization from the published c3 convention",
            ],
        },
        "metric_weights": weights,
        "diagnostics": variants,
        "comparison": {
            "repair_A_integrable_and_primitive": by_name["repair_A_diagonal_B3"][
                "integrable_on_samples"
            ]
            and by_name["repair_A_diagonal_B3"]["primitive_on_samples"],
            "repair_A_hessian_rank_problem_from_prior_gate": True,
            "repair_B_integrable": by_name["repair_B_move_B2"]["integrable_on_samples"],
            "repair_B_primitive_obstructed": not by_name["repair_B_move_B2"][
                "primitive_on_samples"
            ],
            "repair_B_hessian_rank_good_from_prior_gate": True,
            "split_conclusion": (
                "The candidates trade strengths: Repair A passes the algebraic "
                "integrability/primitivity diagnostic but had an extra Hessian "
                "zero mode; Repair B preserves Hessian rank but fails the naive "
                "metric-weighted HYM primitive contraction."
            ),
        },
        "verdict": {
            "repair_A_closed": False,
            "repair_B_closed": False,
            "source_certified_repair_found": False,
            "safe_to_close_Qa_SU3": False,
            "mu_selected": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Source_Certified_Connection_or_Full_Torsion_Primitive_Correction_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
