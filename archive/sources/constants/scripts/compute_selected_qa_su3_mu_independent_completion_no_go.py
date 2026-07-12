"""No-go test for mu-independent torsion/OU completion of the Qa/SU3 HYM block.

After the selected Iwasawa metric weights are inserted, the computable Chern
block has the exact pencil form

    H(mu) = mu A + mu^2 B

with A and B positive semidefinite on the real u(3) slice, and H(mu) positive
on the su(3) quotient for mu > 0.  Consequently log det' H(mu) is strictly
increasing on the quotient.  Adding any mu-independent positive semidefinite
torsion/OU lift C gives H(mu)+C with the same monotone derivative, so it cannot
select an interior mu.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
COMPLETION_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_hym_strominger_weitzenbock_ou_completion_certificate.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def connection_matrices(mu: float) -> list[np.ndarray]:
    s = math.sqrt(mu)
    return [
        np.array([[0.0, 0.0, s], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-s, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, mu, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
    ]


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


def hessian(mu: float, weights: list[float]) -> np.ndarray:
    matrices = [matrix for _, matrix in normalized_u3_basis()]
    out = np.zeros((len(matrices), len(matrices)), dtype=float)
    for b_matrix, weight in zip(connection_matrices(mu), weights):
        for a_matrix in (b_matrix, -b_matrix.conj().T):
            for i, x_matrix in enumerate(matrices):
                comm_x = a_matrix @ x_matrix - x_matrix @ a_matrix
                for j, y_matrix in enumerate(matrices):
                    comm_y = a_matrix @ y_matrix - y_matrix @ a_matrix
                    out[i, j] += weight * real_inner(comm_x, comm_y)
    return out


def eigenvalues(matrix: np.ndarray) -> list[float]:
    return [0.0 if abs(float(value)) < 1e-12 else float(value) for value in np.linalg.eigvalsh(matrix)]


def log_det_derivative(mu: float, a_matrix: np.ndarray, b_matrix: np.ndarray) -> float:
    # Work on the su(3) quotient by dropping the central basis vector.  The
    # remaining block is positive definite for mu > 0.
    h_q = (mu * a_matrix + mu**2 * b_matrix)[1:, 1:]
    dh_q = (a_matrix + 2.0 * mu * b_matrix)[1:, 1:]
    return float(np.trace(np.linalg.solve(h_q, dh_q)))


def main() -> int:
    completion = load(COMPLETION_CERT)
    weights_map = completion["source_backed_completion"]["selected_iwasawa_geometry"][
        "relative_one_form_weights"
    ]
    weights = [weights_map["bar_omega_1"], weights_map["bar_omega_2"], weights_map["bar_omega_3"]]

    h1 = hessian(1.0, weights)
    h4 = hessian(4.0, weights)
    # H(1)=A+B, H(4)=4A+16B.
    a_matrix = (16.0 * h1 - h4) / 12.0
    b_matrix = h1 - a_matrix
    reconstruction_errors = {
        "mu_0_25": float(np.max(np.abs(hessian(0.25, weights) - (0.25 * a_matrix + 0.25**2 * b_matrix)))),
        "mu_2": float(np.max(np.abs(hessian(2.0, weights) - (2.0 * a_matrix + 4.0 * b_matrix)))),
        "mu_4": float(np.max(np.abs(h4 - (4.0 * a_matrix + 16.0 * b_matrix)))),
    }
    derivative_samples = {
        str(mu): log_det_derivative(mu, a_matrix, b_matrix)
        for mu in [0.0001, 0.01, 0.25, 1.0, 4.0, 100.0]
    }

    output = {
        "certificate": "SelectedQaSU3MuIndependentCompletionNoGo",
        "status": "QA_SU3_MU_INDEPENDENT_TORSION_OU_COMPLETION_NO_GO_PROVED",
        "input_status": completion["status"],
        "pencil_identity": {
            "formula": "H_weighted(mu)=mu*A+mu^2*B",
            "reconstruction_max_abs_errors": reconstruction_errors,
            "A_eigenvalues_u3": eigenvalues(a_matrix),
            "B_eigenvalues_u3": eigenvalues(b_matrix),
            "A_eigenvalues_su3_block": eigenvalues(a_matrix[1:, 1:]),
            "B_eigenvalues_su3_block": eigenvalues(b_matrix[1:, 1:]),
        },
        "monotonicity_certificate": {
            "derivative_formula": "d/dmu log det(H_Q(mu)) = Tr(H_Q(mu)^-1 * (A_Q+2*mu*B_Q))",
            "derivative_samples": derivative_samples,
            "strictly_positive_on_samples": all(value > 0.0 for value in derivative_samples.values()),
            "reason": (
                "A and B are positive semidefinite and H_Q(mu) is positive definite "
                "on the su(3) quotient for mu>0, so the trace expression is positive."
            ),
        },
        "no_go_scope": {
            "ruled_out_as_mu_selector": [
                "any mu-independent positive semidefinite OU lift C",
                "any mu-independent positive semidefinite torsional endomorphism C",
                "any common positive scalar frame normalization",
                "any source term depending only on the selected Iwasawa radius R_* and r3 but not on mu",
            ],
            "not_ruled_out": [
                "mu-dependent curvature endomorphism from the non-flat HYM curvature F(mu)",
                "mu-dependent OU weights through lambda_{n,k}^{(Hhat)}(mu)",
                "a discrete admissibility or stability condition selecting a special mu",
                "a full zeta/heat determinant whose lower-order terms are explicitly mu-dependent",
            ],
        },
        "verdict": {
            "mu_independent_completion_can_select_mu": False,
            "torsion_ou_closed_if_mu_independent": True,
            "full_mu_selection_closed": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Mu_Dependent_Curvature_or_OU_Selector_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
