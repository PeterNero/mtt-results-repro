"""Attempt the full left-invariant curvature matrix for the Qa/SU3 HYM bundle.

This checks whether the printed (0,1) connection matrix can be used directly
with the printed Iwasawa structure equation to compute the complete Chern
curvature.  The first gate is integrability:

    F^(0,2) = dbar A^(0,1) + A^(0,1) wedge A^(0,1)

The source states dbar_E^2=0.  Using the printed matrix and
dbar(bar_omega^3)=bar_omega^1 wedge bar_omega^2, the residual is nonzero.
Therefore the full curvature matrix is blocked until a source-level convention,
sign, transpose, or missing term is resolved.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CURVATURE_SUBBLOCK_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_hym_curvature_subblock_selector_test_certificate.json"
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


def frobenius_squared(matrix: np.ndarray) -> float:
    return float(np.real(np.trace(matrix.conj().T @ matrix)))


def residual_matrix(mu: float, dbar_omega3_sign: float = 1.0) -> np.ndarray:
    b1, b2, b3 = connection_matrices(mu)
    wedge_commutator = b1 @ b2 - b2 @ b1
    structure_term = dbar_omega3_sign * b3
    return structure_term + wedge_commutator


def matrix_to_real_rows(matrix: np.ndarray) -> list[list[float]]:
    return [[float(np.real(value)) for value in row] for row in matrix]


def sample_residuals() -> list[dict[str, Any]]:
    samples = []
    for mu in [0.25, 1.0, 4.0]:
        matrix = residual_matrix(mu)
        alt_sign_matrix = residual_matrix(mu, dbar_omega3_sign=-1.0)
        samples.append(
            {
                "mu": mu,
                "standard_residual_matrix": matrix_to_real_rows(matrix),
                "standard_residual_frobenius_squared": frobenius_squared(matrix),
                "standard_closed_formula": 3.0 * mu**2,
                "opposite_structure_sign_residual_frobenius_squared": frobenius_squared(
                    alt_sign_matrix
                ),
            }
        )
    return samples


def main() -> int:
    prior = load(CURVATURE_SUBBLOCK_CERT)
    output = {
        "certificate": "SelectedQaSU3FullLeftInvariantCurvatureMatrixAttempt",
        "status": "QA_SU3_FULL_CURVATURE_MATRIX_BLOCKED_BY_PRINTED_INTEGRABILITY_MISMATCH",
        "input_status": prior["status"],
        "source_equations_used": {
            "A01": "A^(0,1)=B1*bar_omega_1+B2*bar_omega_2+B3*bar_omega_3 as printed",
            "structure": "dbar(bar_omega_1)=dbar(bar_omega_2)=0, dbar(bar_omega_3)=bar_omega_1 wedge bar_omega_2",
            "integrability_claim": "source states dbar_E^2=0",
        },
        "computed_integrability_residual": {
            "formula": "F02_bar12 = B3 + (B1*B2 - B2*B1)",
            "symbolic_matrix": [
                ["-mu", "mu", "0"],
                ["0", "0", "0"],
                ["0", "0", "mu"],
            ],
            "frobenius_squared": "3*mu^2",
            "zero_only_at": "mu=0, outside the source branch mu>0",
            "samples": sample_residuals(),
        },
        "interpretation": {
            "standard_formula_consistent_with_printed_source": False,
            "why_blocked": (
                "For mu>0, the printed matrix plus printed Iwasawa structure equation "
                "does not satisfy the standard F^(0,2)=0 integrability check.  Since "
                "the source also claims dbar_E^2=0, the full curvature matrix cannot "
                "be source-certified until the convention or printed matrix is corrected."
            ),
            "possible_resolutions_to_check": [
                "transpose/dual-bundle convention for matrix action",
                "missing diagonal or off-diagonal connection entries",
                "different sign convention for matrix-valued wedge products",
                "different sign in dbar(bar_omega^3)",
                "monad basis contribution not represented by the displayed matrix",
            ],
        },
        "closed_now": [
            "direct full-curvature computation from the printed data is blocked",
            "the obstruction is explicit and reproducible: residual norm 3*mu^2",
            "no target fitting or mu choice can repair integrability for mu>0",
        ],
        "verdict": {
            "full_left_invariant_curvature_matrix_computed": False,
            "printed_data_pass_standard_integrability": False,
            "source_erratum_or_convention_needed": True,
            "mu_selected": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_HYM_Connection_Erratum_or_Convention_Resolution_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
