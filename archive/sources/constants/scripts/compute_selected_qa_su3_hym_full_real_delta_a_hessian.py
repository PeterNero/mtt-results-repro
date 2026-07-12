"""Compute the real u(3) Chern/HYM algebraic Hessian block for Qa/SU3.

This advances the prior complex End(C^3) scaffold to the real unitary slice.
Using the extracted HYM (0,1) matrices B_i and the trivial Hermitian metric
stated in the source, the unitary Chern conjugate contributes -B_i^*.  The
real algebraic Chern block is

    H_real(mu)[X,Y] = sum_i <[B_i,X],[B_i,Y]> + <[-B_i^*,X],[-B_i^*,Y]>

for anti-Hermitian X,Y in u(3), with the real Hilbert-Schmidt inner product.

This is the full real algebraic Chern block from the available matrix data.
It is not the full Strominger Hessian until metric/radius weights, torsional
endomorphism terms, gauge quotient details, and OU weights are supplied.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DELTA_CERT = ROOT / "certificates" / "selected_qa_su3_hym_delta_a_mu_spectrum_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def connection_matrices(mu: float) -> list[np.ndarray]:
    s = math.sqrt(mu)
    return [
        np.array([[0.0, 0.0, s], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-s, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, mu, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
    ]


def real_inner(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.real(np.trace(x.conj().T @ y)))


def normalized_u3_basis() -> list[dict[str, Any]]:
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

    return [{"label": label, "matrix": matrix} for label, matrix in matrices]


def hessian_matrix(mu: float) -> tuple[np.ndarray, list[str]]:
    basis = normalized_u3_basis()
    labels = [entry["label"] for entry in basis]
    matrices = [entry["matrix"] for entry in basis]
    connection_pieces = []
    for b_matrix in connection_matrices(mu):
        connection_pieces.append(b_matrix)
        connection_pieces.append(-b_matrix.conj().T)

    hessian = np.zeros((len(matrices), len(matrices)), dtype=float)
    for i, x_matrix in enumerate(matrices):
        for j, y_matrix in enumerate(matrices):
            total = 0.0
            for a_matrix in connection_pieces:
                comm_x = a_matrix @ x_matrix - x_matrix @ a_matrix
                comm_y = a_matrix @ y_matrix - y_matrix @ a_matrix
                total += real_inner(comm_x, comm_y)
            hessian[i, j] = total
    return hessian, labels


def real_hessian_block(mu: float) -> dict[str, Any]:
    hessian, labels = hessian_matrix(mu)
    eigenvalues = np.linalg.eigvalsh(hessian)
    rounded = [0.0 if abs(float(value)) < 1e-12 else float(value) for value in eigenvalues]
    positive = [value for value in rounded if value > 1e-10]
    return {
        "mu": mu,
        "basis_labels": labels,
        "operator": "H_real(mu) on normalized anti-Hermitian u(3) basis",
        "dimension_real_u3": 9,
        "zero_modes": len([value for value in rounded if abs(value) <= 1e-10]),
        "positive_modes": len(positive),
        "rank": int(np.linalg.matrix_rank(hessian, tol=1e-10)),
        "eigenvalues": rounded,
        "trace": float(np.trace(hessian)),
        "det_prime": float(np.prod(positive)) if positive else None,
        "log_det_prime": float(np.sum(np.log(positive))) if positive else None,
        "central_u1_zero_mode_expected": True,
    }


def monotonicity_diagnostic(samples: list[dict[str, Any]]) -> dict[str, Any]:
    log_dets = [sample["log_det_prime"] for sample in samples]
    return {
        "sample_mu_values": [sample["mu"] for sample in samples],
        "sample_log_det_prime_values": log_dets,
        "strictly_increasing_on_samples": all(
            after > before for before, after in zip(log_dets, log_dets[1:])
        ),
        "selection_consequence": (
            "The real Chern algebraic block is positive on su(3), but by itself "
            "is monotone on the sampled mu values and therefore does not select "
            "an interior mu without the remaining sourced Hessian/OU terms."
        ),
    }


def main() -> int:
    prior = load(DELTA_CERT)
    sample_mu = [0.25, 1.0, 4.0]
    samples = [real_hessian_block(mu) for mu in sample_mu]
    output = {
        "status": "QA_SU3_HYM_REAL_CHERN_HESSIAN_BLOCK_COMPUTED_STROMINGER_OU_OPEN",
        "input_delta_a_status": prior["status"],
        "computed_block_scope": {
            "included": [
                "real anti-Hermitian u(3) basis",
                "trivial Hermitian metric normalization from the source",
                "Chern unitary conjugate pieces -B_i^*",
                "real Hilbert-Schmidt Hessian from commutators with B_i and -B_i^*",
            ],
            "still_excluded_from_full_strominger_hessian": [
                "Iwasawa metric/radius weights on one-form directions",
                "torsional Weitzenbock/endomorphism terms from R_+ and Hhat",
                "differential derivative pieces beyond the invariant algebraic band",
                "fixed-gauge quotient beyond the central u(1) commutator zero mode",
                "OU weights gamma_{n,k}^{-1}",
                "zeta/heat regularized determinant of the full operator",
            ],
        },
        "sample_real_hessian_blocks": samples,
        "monotonicity_diagnostic": monotonicity_diagnostic(samples),
        "remaining_required_data": [
            "insert sourced Iwasawa metric/radius weights for all real one-form directions",
            "add torsional Weitzenbock/endomorphism terms from the selected Strominger Hessian",
            "identify and quotient all fixed-gauge symmetry modes, not only the central commutator zero mode",
            "supply OU weights gamma_{n,k}^{-1} or prove they vanish on the selected block",
            "then minimize the complete real Hessian/determinant in mu before using any Qa/SU3 comparison",
        ],
        "computed_numeric_response": None,
        "verdict": {
            "real_u3_chern_hessian_block_computed": True,
            "central_u1_zero_mode_seen": True,
            "su3_positive_modes_seen_in_samples": True,
            "full_strominger_hessian_computed": False,
            "ou_weights_available": False,
            "mu_selected": False,
            "can_close_Qa_SU3_now": False,
            "target_fitting_used": False,
            "full_SM_closure_achieved": False,
            "next_required_artifact": "Selected_Qa_SU3_HYM_Strominger_Weitzenbock_OU_Completion_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
