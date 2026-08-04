"""Compute the exact remaining requirements for the Qa/SU3 repair fork."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIAG_CERT = ROOT / "certificates" / "selected_qa_su3_repair_chern_weil_operator_diagnostic_certificate.json"
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


def hessian(mu: float, variant: str, weights: list[float]) -> tuple[np.ndarray, list[str]]:
    basis = normalized_u3_basis()
    labels = [label for label, _ in basis]
    matrices = [matrix for _, matrix in basis]
    out = np.zeros((len(basis), len(basis)), dtype=float)
    for b_matrix, weight in zip(connection_matrices(mu, variant), weights):
        for a_matrix in (b_matrix, -b_matrix.conj().T):
            for i, x_matrix in enumerate(matrices):
                comm_x = a_matrix @ x_matrix - x_matrix @ a_matrix
                for j, y_matrix in enumerate(matrices):
                    comm_y = a_matrix @ y_matrix - y_matrix @ a_matrix
                    out[i, j] += weight * real_inner(comm_x, comm_y)
    return out, labels


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


def serialize_real_matrix(matrix: np.ndarray) -> list[list[float]]:
    return [[float(np.real(value)) for value in row] for row in matrix]


def repair_a_extra_null_direction(weights: list[float]) -> dict[str, Any]:
    h_matrix, labels = hessian(1.0, "repair_A_diagonal_B3", weights)
    values, vectors = np.linalg.eigh(h_matrix)
    null_vectors = []
    for value, vector in zip(values, vectors.T):
        if abs(float(value)) <= 1e-10:
            components = [
                {"basis": label, "coefficient": float(coeff)}
                for label, coeff in zip(labels, vector)
                if abs(float(coeff)) > 1e-8
            ]
            null_vectors.append({"eigenvalue": float(value), "components": components})
    noncentral = [entry for entry in null_vectors if len(entry["components"]) != 1]
    return {
        "mu": 1.0,
        "nullity": len(null_vectors),
        "null_vectors": null_vectors,
        "extra_noncentral_nullity": len(noncentral),
        "interpretation": (
            "Repair A can remain viable only if the extra noncentral null "
            "direction is source-certified as a gauge/stabilizer quotient mode."
        ),
    }


def repair_b_required_primitive_correction(weights: list[float]) -> dict[str, Any]:
    samples = []
    for mu in [0.25, 1.0, 4.0]:
        primitive = primitive_contraction(mu, "repair_B_move_B2", weights)
        correction_if_put_in_third_block = -primitive / weights[2]
        samples.append(
            {
                "mu": mu,
                "primitive_obstruction": serialize_real_matrix(primitive),
                "minimal_third_diagonal_block_correction": serialize_real_matrix(
                    correction_if_put_in_third_block
                ),
                "correction_norm_squared": float(
                    np.real(np.trace(correction_if_put_in_third_block.conj().T @ correction_if_put_in_third_block))
                ),
            }
        )
    return {
        "samples": samples,
        "interpretation": (
            "Repair B can remain viable only if the full source-certified "
            "torsion/convention correction contributes exactly this primitive "
            "cancelling traceless diagonal term, or an equivalent weighted "
            "distribution across the three diagonal F11 blocks."
        ),
    }


def main() -> int:
    diag = load(DIAG_CERT)
    radius = load(RADIUS_CERT)
    weights = metric_weights(radius)
    output = {
        "certificate": "SelectedQaSU3RepairForkResolutionRequirements",
        "status": "QA_SU3_REPAIR_FORK_RESOLUTION_REQUIREMENTS_COMPUTED_NO_CLOSURE",
        "input_status": {
            "chern_weil_operator_diagnostic": diag["status"],
            "selected_radius": radius["status"],
        },
        "metric_weights": weights,
        "repair_A_requirement": repair_a_extra_null_direction(weights),
        "repair_B_requirement": repair_b_required_primitive_correction(weights),
        "fork_resolution": {
            "route_A": (
                "Prove the extra noncentral null vector is a legitimate quotient "
                "mode forced by the selected gauge/stabilizer symmetry."
            ),
            "route_B": (
                "Source-certify a full torsion/convention correction whose "
                "primitive contraction cancels the displayed traceless diagonal "
                "obstruction without introducing a fitted coefficient."
            ),
            "forbidden_shortcut": (
                "Do not choose a correction coefficient from the desired Qa/SU3 "
                "threshold value or from the observed electroweak target."
            ),
        },
        "verdict": {
            "route_A_closed": False,
            "route_B_closed": False,
            "fork_resolved": False,
            "safe_to_close_Qa_SU3": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Repair_A_Quotient_Mode_or_Repair_B_Torsion_Source_Test_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
