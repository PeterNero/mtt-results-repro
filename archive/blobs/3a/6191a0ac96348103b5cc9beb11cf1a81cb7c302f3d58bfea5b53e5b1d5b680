"""Analyze block-factorized options for the qutrit projective twist.

The previous fill attempt found that the irreducible qutrit clock/shift
carrier has no rank-one invariant Higgs projector.  This script checks whether
the obvious repair, adding a trivial Higgs line, preserves scalar projective
gluing.  It does not: diag(X,1), diag(Z,1) has a rank-one invariant line, but
its corner ratio is diag(omega I_3,1), not a scalar.

Therefore the honest continuation is not a naive rank-four direct sum.  It is a
block-factorized schema: the qutrit twist may live in an ambient family-Z3 or
twisted-boundary factor while the Higgs carrier is validated separately.
"""

from __future__ import annotations

import json
import math
from typing import Any


Matrix = list[list[complex]]
TOL = 1e-9


def identity(size: int) -> Matrix:
    return [
        [1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]


def clock3() -> Matrix:
    omega = complex(math.cos(2.0 * math.pi / 3.0), math.sin(2.0 * math.pi / 3.0))
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, omega, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, omega**2],
    ]


def shift3() -> Matrix:
    return [
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
    ]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[row][idx] * right[idx][col] for idx in range(len(right)))
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def adjoint(matrix: Matrix) -> Matrix:
    return [
        [matrix[col][row].conjugate() for col in range(len(matrix))]
        for row in range(len(matrix[0]))
    ]


def block_diag(left: Matrix, right: Matrix) -> Matrix:
    size_left = len(left)
    size_right = len(right)
    out = [[0.0 + 0.0j for _ in range(size_left + size_right)] for _ in range(size_left + size_right)]
    for row in range(size_left):
        for col in range(size_left):
            out[row][col] = left[row][col]
    for row in range(size_right):
        for col in range(size_right):
            out[size_left + row][size_left + col] = right[row][col]
    return out


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    return max(
        abs(left[row][col] - right[row][col])
        for row in range(len(left))
        for col in range(len(left[0]))
    )


def scalar_central_error(matrix: Matrix) -> tuple[complex, float]:
    size = len(matrix)
    scalar = sum(matrix[idx][idx] for idx in range(size)) / size
    scalar_matrix = [
        [scalar if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]
    return scalar, max_abs_diff(matrix, scalar_matrix)


def projector_last_line(size: int) -> Matrix:
    out = [[0.0 + 0.0j for _ in range(size)] for _ in range(size)]
    out[size - 1][size - 1] = 1.0 + 0.0j
    return out


def commutes(left: Matrix, right: Matrix) -> bool:
    return max_abs_diff(matmul(left, right), matmul(right, left)) <= TOL


def phase_label(value: complex) -> str:
    if abs(value) <= TOL:
        return "zero"
    unit = value / abs(value)
    angle = math.atan2(unit.imag, unit.real)
    if angle < 0:
        angle += 2.0 * math.pi
    index = round(3.0 * angle / (2.0 * math.pi)) % 3
    root = complex(math.cos(2.0 * math.pi * index / 3.0), math.sin(2.0 * math.pi * index / 3.0))
    if abs(unit - root) <= 1e-6:
        return f"zeta_3^{index}"
    return f"angle={angle:.12f}"


def analyze() -> dict[str, Any]:
    x3 = shift3()
    z3 = clock3()
    ratio3 = matmul(matmul(x3, z3), adjoint(matmul(z3, x3)))
    scalar3, central_error3 = scalar_central_error(ratio3)

    x4 = block_diag(x3, identity(1))
    z4 = block_diag(z3, identity(1))
    ratio4 = matmul(matmul(x4, z4), adjoint(matmul(z4, x4)))
    scalar4, central_error4 = scalar_central_error(ratio4)
    h_projector = projector_last_line(4)

    return {
        "calculation": "IwasawaBlockFactorizedTwistRouteAnalysis",
        "rank3_family_block": {
            "corner_ratio_scalar_label": phase_label(scalar3),
            "centrality_error": central_error3,
            "single_scalar_projective_gluing": central_error3 <= TOL,
            "rank_one_projector_available": False,
            "reason": "irreducible qutrit clock/shift carrier has commutant C*I_3",
        },
        "naive_rank4_direct_sum": {
            "carrier": "diag(X,1), diag(Z,1)",
            "rank_one_H_projector_commutes_with_X4": commutes(h_projector, x4),
            "rank_one_H_projector_commutes_with_Z4": commutes(h_projector, z4),
            "rank_one_H_projector_available": commutes(h_projector, x4)
            and commutes(h_projector, z4),
            "corner_ratio_diagonal_labels": ["zeta_3^1", "zeta_3^1", "zeta_3^1", "zeta_3^0"],
            "best_scalar_average_label": phase_label(scalar4),
            "centrality_error": central_error4,
            "single_scalar_projective_gluing": central_error4 <= TOL,
            "verdict": "rank-one H line exists, but scalar projective gluing fails on the combined rank-four carrier",
        },
        "honest_route": {
            "block_factorized_schema_needed": True,
            "family_twist_block": "rank-three qutrit projective family/twisted-boundary carrier",
            "higgs_block": "separate selected Higgs carrier with ordinary rank-one projector",
            "single_carrier_shortcut_allowed": False,
            "requires_new_validator_schema": True,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
