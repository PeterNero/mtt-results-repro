"""Test the algebraic Chern-curvature subblock as a possible mu selector.

The source states that the explicit Iwasawa HYM Chern curvature is nonzero,
type (1,1), and has Tr F_E wedge F_E = 0.  It does not print the complete
curvature matrix.  From the printed connection coefficients we can still
compute the algebraic connection-commutator part of the (1,1) curvature:

    C_ij(mu) = [-B_i^*, B_j]

This is not the full curvature because left-invariant frame derivative /
structure-equation terms may also contribute.  It is, however, the most direct
mu-dependent curvature subblock available from the selected matrix data.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NO_GO_CERT = ROOT / "certificates" / "selected_qa_su3_mu_independent_completion_no_go_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def connection_matrices(mu: float) -> list[np.ndarray]:
    s = math.sqrt(mu)
    return [
        np.array([[0.0, 0.0, s], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-s, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, mu, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
    ]


def frobenius_squared(matrix: np.ndarray) -> float:
    return float(np.real(np.trace(matrix.conj().T @ matrix)))


def curvature_commutator_blocks(mu: float) -> list[dict[str, Any]]:
    blocks = []
    matrices = connection_matrices(mu)
    for i, b_i in enumerate(matrices, start=1):
        a10_i = -b_i.conj().T
        for j, b_j in enumerate(matrices, start=1):
            block = a10_i @ b_j - b_j @ a10_i
            blocks.append(
                {
                    "i": i,
                    "j": j,
                    "frobenius_squared": frobenius_squared(block),
                    "trace": float(np.real(np.trace(block))),
                    "rank": int(np.linalg.matrix_rank(block, tol=1e-12)),
                }
            )
    return blocks


def total_commutator_curvature_norm(mu: float) -> float:
    return sum(block["frobenius_squared"] for block in curvature_commutator_blocks(mu))


def polynomial_value(mu: float) -> float:
    return 2.0 * mu**2 * (mu**2 + mu + 2.0)


def derivative_value(mu: float) -> float:
    return 8.0 * mu**3 + 6.0 * mu**2 + 8.0 * mu


def main() -> int:
    prior = load(NO_GO_CERT)
    sample_mu = [0.01, 0.1, 0.25, 1.0, 4.0, 16.0]
    samples = [
        {
            "mu": mu,
            "total_commutator_curvature_norm": total_commutator_curvature_norm(mu),
            "closed_polynomial_value": polynomial_value(mu),
            "derivative": derivative_value(mu),
            "agrees_with_polynomial": abs(total_commutator_curvature_norm(mu) - polynomial_value(mu))
            < 1e-12,
        }
        for mu in sample_mu
    ]

    output = {
        "certificate": "SelectedQaSU3HYMCurvatureSubblockSelectorTest",
        "status": "QA_SU3_HYM_CURVATURE_COMMUTATOR_SUBBLOCK_COMPUTED_NO_INTERIOR_SELECTOR",
        "input_status": prior["status"],
        "computed_subblock": {
            "definition": "C_ij(mu)=[-B_i^*,B_j] from the printed HYM connection coefficients",
            "scope_warning": (
                "This is the algebraic Chern connection-commutator part, not the "
                "complete left-invariant curvature matrix with derivative and "
                "structure-equation contributions."
            ),
            "sample_blocks_mu_1": curvature_commutator_blocks(1.0),
        },
        "norm_formula": {
            "total_norm": "sum_ij ||[-B_i^*,B_j]||_F^2 = 2*mu^2*(mu^2+mu+2)",
            "derivative": "8*mu^3 + 6*mu^2 + 8*mu",
            "strictly_increasing_for_mu_positive": True,
            "samples": samples,
        },
        "selector_consequence": {
            "commutator_curvature_norm_selects_interior_mu": False,
            "reason": (
                "The available algebraic curvature-strength invariant is strictly "
                "increasing for mu>0, so minimizing it runs to the boundary and "
                "maximizing it runs to infinity unless another selected term competes."
            ),
        },
        "remaining_live_routes": [
            "compute the full left-invariant curvature matrix including d bar_omega^3 and d omega^3 structure terms",
            "derive how Tr F_E wedge F_E = 0 cancels at matrix level and whether a non-norm invariant remains",
            "derive mu-dependent OU eigenvalue weights from the full twisted operator rather than from curvature norm",
            "find a source-stated discrete stability/admissibility condition that fixes mu",
        ],
        "verdict": {
            "curvature_commutator_subblock_computed": True,
            "curvature_commutator_norm_mu_selector": False,
            "full_curvature_matrix_computed": False,
            "full_mu_selection_closed": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Full_Left_Invariant_Curvature_Matrix_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
