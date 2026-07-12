"""Explore convention and minimal-repair routes for the printed Qa/SU3 HYM connection.

The full-curvature attempt found that the printed A^(0,1) matrix fails the
standard integrability check.  This script tests simple convention changes and
derives the unique B3 coefficient required by integrability once B1 and B2 are
kept as printed.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FULL_ATTEMPT_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_full_left_invariant_curvature_matrix_attempt_certificate.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def printed_matrices(mu: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    s = math.sqrt(mu)
    return (
        np.array([[0.0, 0.0, s], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=float),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-s, 0.0, 0.0]], dtype=float),
        np.array([[0.0, mu, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=float),
    )


def norm_squared(matrix: np.ndarray) -> float:
    return float(np.sum(matrix * matrix))


def matrix_rows(matrix: np.ndarray) -> list[list[float]]:
    return [[float(value) for value in row] for row in matrix]


def convention_scan(mu: float = 1.0) -> list[dict[str, Any]]:
    transforms: dict[str, Callable[[np.ndarray], np.ndarray]] = {
        "as_printed": lambda matrix: matrix,
        "transpose": lambda matrix: matrix.T,
        "negative": lambda matrix: -matrix,
        "negative_transpose": lambda matrix: -matrix.T,
    }
    rows = []
    b1, b2, b3 = printed_matrices(mu)
    for name, transform in transforms.items():
        c1, c2, c3 = transform(b1), transform(b2), transform(b3)
        for structure_sign in (1.0, -1.0):
            for wedge_sign in (1.0, -1.0):
                residual = structure_sign * c3 + wedge_sign * (c1 @ c2 - c2 @ c1)
                rows.append(
                    {
                        "transform": name,
                        "structure_sign": int(structure_sign),
                        "wedge_sign": int(wedge_sign),
                        "residual_norm_squared": norm_squared(residual),
                        "residual_matrix": matrix_rows(residual),
                    }
                )
    return rows


def required_b3_for_integrability(mu: float = 1.0) -> dict[str, Any]:
    b1, b2, printed_b3 = printed_matrices(mu)
    commutator = b1 @ b2 - b2 @ b1
    required_b3 = -commutator
    delta = required_b3 - printed_b3
    return {
        "mu": mu,
        "printed_B3": matrix_rows(printed_b3),
        "commutator_B1B2_minus_B2B1": matrix_rows(commutator),
        "required_B3_standard": matrix_rows(required_b3),
        "required_B3_symbolic": [
            ["mu", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "-mu"],
        ],
        "delta_required_minus_printed": matrix_rows(delta),
        "required_B3_trace": float(np.trace(required_b3)),
        "required_B3_rank": int(np.linalg.matrix_rank(required_b3, tol=1e-12)),
        "printed_to_required_frobenius_distance_squared": norm_squared(delta),
    }


def repaired_curvature_commutator_norm(mu: float) -> float:
    b1, b2, _ = printed_matrices(mu)
    b3 = -(b1 @ b2 - b2 @ b1)
    matrices = [b1, b2, b3]
    total = 0.0
    for b_i in matrices:
        a10_i = -b_i.T
        for b_j in matrices:
            block = a10_i @ b_j - b_j @ a10_i
            total += norm_squared(block)
    return total


def repaired_samples() -> list[dict[str, Any]]:
    samples = []
    for mu in [0.01, 0.1, 0.25, 1.0, 4.0, 16.0]:
        # Required B3 is linear in mu, so this remains a monotone polynomial.
        samples.append(
            {
                "mu": mu,
                "repaired_commutator_curvature_norm": repaired_curvature_commutator_norm(mu),
            }
        )
    return samples


def main() -> int:
    prior = load(FULL_ATTEMPT_CERT)
    scan = convention_scan()
    best = min(scan, key=lambda row: row["residual_norm_squared"])
    output = {
        "certificate": "SelectedQaSU3HYMConnectionErratumOrConventionResolution",
        "status": "QA_SU3_HYM_CONNECTION_CONVENTION_SCAN_DONE_MINIMAL_ERRATUM_IDENTIFIED",
        "input_status": prior["status"],
        "convention_scan": {
            "mu": 1.0,
            "rows": scan,
            "minimum_residual_norm_squared": best["residual_norm_squared"],
            "zero_residual_convention_found": best["residual_norm_squared"] < 1e-12,
            "best_rows": [
                row for row in scan if abs(row["residual_norm_squared"] - best["residual_norm_squared"]) < 1e-12
            ],
        },
        "minimal_standard_repair": required_b3_for_integrability(1.0),
        "repair_status": {
            "keeps_B1_B2_as_printed": True,
            "requires_replacing_printed_B3": True,
            "printed_B3": "mu*E12",
            "integrable_B3_standard": "mu*(E11-E33)",
            "source_support_for_repair": False,
            "reason_source_support_missing": (
                "The corpus prints mu*bar_omega^3 in the (1,2) entry and does "
                "not state the diagonal replacement.  The diagonal B3 is an "
                "erratum candidate, not a source-certified correction."
            ),
        },
        "repaired_branch_diagnostic": {
            "samples": repaired_samples(),
            "selector_warning": (
                "Even the minimal integrability repair does not by itself select "
                "mu; it only restores F^(0,2)=0 under the standard convention."
            ),
        },
        "way_forward": [
            "mark the printed HYM connection as requiring erratum/convention resolution before it can be a proof source",
            "if editing the corpus is allowed, replace or annotate B3 and rerun the curvature/Hessian pipeline",
            "if corpus edits are not allowed, retire this explicit HYM matrix as a closure source and search for another source-certified SU3/Qa operator",
            "keep all previous no-go results, because they rule out constant torsion/OU fixes independently of this erratum",
        ],
        "verdict": {
            "simple_convention_resolves_integrability": False,
            "minimal_algebraic_repair_identified": True,
            "minimal_repair_source_certified": False,
            "mu_selected": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Erratum_Repaired_HYM_Pipeline_or_Source_Retirement_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
