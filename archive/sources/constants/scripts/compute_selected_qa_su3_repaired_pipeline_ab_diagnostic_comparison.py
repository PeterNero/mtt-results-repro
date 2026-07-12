"""Diagnostic comparison of two Qa/SU3 HYM repair candidates.

Repair A keeps B1,B2 as printed and replaces B3 by the diagonal integrability
value.  Repair B keeps B1,B3 as printed and moves B2 by one column.  Neither is
source-certified; this script only compares their algebraic consequences.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
GUARD_CERT = ROOT / "certificates" / "selected_qa_su3_hym_erratum_guardrail_deep_scan_certificate.json"
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


def normalized_u3_basis() -> list[tuple[str, np.ndarray]]:
    matrices: list[tuple[str, np.ndarray]] = [
        ("central_i_identity", 1j * np.eye(3) / math.sqrt(3.0)),
        ("cartan_i_lambda3", 1j * np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0)),
        ("cartan_i_lambda8", 1j * np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0)),
    ]
    for a, b, label in [(0, 1, "12"), (0, 2, "13"), (1, 2, "23")]:
        skew_real = np.zeros((3, 3), dtype=complex)
        skew_real[a, b] = 1.0
        skew_real[b, a] = -1.0
        matrices.append((f"skew_real_{label}", skew_real / math.sqrt(2.0)))

        skew_imag = np.zeros((3, 3), dtype=complex)
        skew_imag[a, b] = 1j
        skew_imag[b, a] = 1j
        matrices.append((f"skew_imag_{label}", skew_imag / math.sqrt(2.0)))
    return matrices


def real_inner(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.real(np.trace(x.conj().T @ y)))


def frobenius_squared(matrix: np.ndarray) -> float:
    return float(np.real(np.trace(matrix.conj().T @ matrix)))


def f02_residual(mu: float, variant: str) -> np.ndarray:
    b1, b2, b3 = connection_matrices(mu, variant)
    return b3 + b1 @ b2 - b2 @ b1


def curvature_commutator_norm(mu: float, variant: str) -> float:
    matrices = connection_matrices(mu, variant)
    total = 0.0
    for b_i in matrices:
        a10_i = -b_i.conj().T
        for b_j in matrices:
            block = a10_i @ b_j - b_j @ a10_i
            total += frobenius_squared(block)
    return total


def metric_weights(radius_cert: dict[str, Any]) -> list[float]:
    values = radius_cert["selected_values"]
    r1 = float(values["R_star"])
    r2 = r1
    r3 = float(values["r3"])
    return [1.0 / r1**2, 1.0 / r2**2, 1.0 / r3**2]


def hessian(mu: float, variant: str, weights: list[float]) -> np.ndarray:
    basis = [matrix for _, matrix in normalized_u3_basis()]
    out = np.zeros((len(basis), len(basis)), dtype=float)
    for b_matrix, weight in zip(connection_matrices(mu, variant), weights):
        for a_matrix in (b_matrix, -b_matrix.conj().T):
            for i, x_matrix in enumerate(basis):
                comm_x = a_matrix @ x_matrix - x_matrix @ a_matrix
                for j, y_matrix in enumerate(basis):
                    comm_y = a_matrix @ y_matrix - y_matrix @ a_matrix
                    out[i, j] += weight * real_inner(comm_x, comm_y)
    return out


def sample_variant(variant: str, weights: list[float]) -> dict[str, Any]:
    samples = []
    for mu in [0.25, 1.0, 4.0]:
        h_matrix = hessian(mu, variant, weights)
        eigenvalues = [
            0.0 if abs(float(value)) < 1e-12 else float(value)
            for value in np.linalg.eigvalsh(h_matrix)
        ]
        positive = [value for value in eigenvalues if value > 1e-10]
        samples.append(
            {
                "mu": mu,
                "F02_residual_norm_squared": frobenius_squared(f02_residual(mu, variant)),
                "curvature_commutator_norm": curvature_commutator_norm(mu, variant),
                "hessian_zero_modes": len([value for value in eigenvalues if abs(value) <= 1e-10]),
                "hessian_positive_modes": len(positive),
                "hessian_log_det_prime": float(np.sum(np.log(positive))) if positive else None,
                "hessian_eigenvalues": eigenvalues,
            }
        )
    return {
        "variant": variant,
        "samples": samples,
        "expected_central_zero_only": all(
            sample["hessian_zero_modes"] == 1 and sample["hessian_positive_modes"] == 8
            for sample in samples
        ),
        "integrable_on_samples": all(sample["F02_residual_norm_squared"] <= 1e-12 for sample in samples),
        "hessian_logdet_increasing_on_samples": all(
            after["hessian_log_det_prime"] > before["hessian_log_det_prime"]
            for before, after in zip(samples, samples[1:])
        ),
    }


def main() -> int:
    guard = load(GUARD_CERT)
    radius = load(RADIUS_CERT)
    weights = metric_weights(radius)
    variants = [
        sample_variant("repair_A_diagonal_B3", weights),
        sample_variant("repair_B_move_B2", weights),
    ]
    by_name = {variant["variant"]: variant for variant in variants}
    output = {
        "certificate": "SelectedQaSU3RepairedPipelineABDiagnosticComparison",
        "status": "QA_SU3_REPAIRED_PIPELINE_A_B_DIAGNOSTIC_COMPARISON_DONE_NO_SOURCE_CLOSURE",
        "input_status": {
            "guardrail": guard["status"],
            "selected_radius": radius["status"],
        },
        "repair_definitions": {
            "repair_A_diagonal_B3": "B1=E13, B2=-E31, B3=E11-E33",
            "repair_B_move_B2": "B1=E13, B2=-E32, B3=E12",
        },
        "diagnostics": variants,
        "comparison": {
            "both_restore_integrability_on_samples": all(
                variant["integrable_on_samples"] for variant in variants
            ),
            "repair_A_extra_zero_mode": by_name["repair_A_diagonal_B3"][
                "expected_central_zero_only"
            ]
            is False,
            "repair_B_expected_hessian_rank_pattern": by_name["repair_B_move_B2"][
                "expected_central_zero_only"
            ]
            is True,
            "neither_selects_mu_by_logdet_samples": all(
                variant["hessian_logdet_increasing_on_samples"] for variant in variants
            ),
            "best_diagnostic_candidate": "repair_B_move_B2",
            "reason": (
                "Repair B restores integrability while preserving the one-central-zero/"
                "eight-positive-mode Hessian pattern seen in the original real block. "
                "Repair A restores integrability but introduces an additional zero mode."
            ),
        },
        "not_closed": [
            "neither repair is source-certified",
            "Chern-Weil checks Tr F wedge F = 0 and c3 = 6 were not recomputed from a complete source-certified curvature matrix",
            "both repaired Hessian log-det samples remain monotone and do not select mu",
            "full threshold determinant and BRST quotient remain open",
        ],
        "verdict": {
            "repair_A_viable_diagnostic": False,
            "repair_B_viable_diagnostic": True,
            "repair_B_source_certified": False,
            "mu_selected": False,
            "safe_to_close_Qa_SU3": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Repair_B_Chern_Weil_and_Operator_Test_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
