"""Compute finite qutrit coupling invariants for the block-factorized route.

The block-factorized packet keeps the Higgs as a trivial rank-one line.  Then a
Yukawa operator Q u H, Q d H, L e H, or L N H can be invariant under the finite
qutrit twist only if the two matter factors are conjugate projective blocks.

This script checks that statement directly by computing fixed subspace
dimensions for V_s tensor V_t, where s,t in Z/3 encode the central qutrit
twist orientation.  The diagonal generators are X tensor X and Z^s tensor Z^t.
"""

from __future__ import annotations

import json
import math
from itertools import product
from typing import Any


Matrix = list[list[complex]]
TOL = 1e-9


def identity(size: int) -> Matrix:
    return [
        [1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]


def clock3(power: int = 1) -> Matrix:
    omega = complex(math.cos(2.0 * math.pi / 3.0), math.sin(2.0 * math.pi / 3.0))
    return [
        [omega ** ((power * idx) % 3) if row == idx else 0.0 + 0.0j for idx in range(3)]
        for row in range(3)
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


def matrix_power(matrix: Matrix, power: int) -> Matrix:
    result = identity(len(matrix))
    for _ in range(power % 3):
        result = matmul(result, matrix)
    return result


def kron(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left) * len(right)
    cols = len(left[0]) * len(right[0])
    out = [[0.0 + 0.0j for _ in range(cols)] for _ in range(rows)]
    for i, left_row in enumerate(left):
        for j, left_value in enumerate(left_row):
            for k, right_row in enumerate(right):
                for ell, right_value in enumerate(right_row):
                    out[i * len(right) + k][j * len(right[0]) + ell] = (
                        left_value * right_value
                    )
    return out


def subtract_identity(matrix: Matrix) -> Matrix:
    out = [row[:] for row in matrix]
    for idx in range(len(out)):
        out[idx][idx] -= 1.0
    return out


def stacked(*matrices: Matrix) -> Matrix:
    out: Matrix = []
    for matrix in matrices:
        out.extend([row[:] for row in matrix])
    return out


def rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank_value = 0
    for col in range(cols):
        pivot = None
        for row in range(rank_value, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank_value], work[pivot] = work[pivot], work[rank_value]
        scale = work[rank_value][col]
        work[rank_value] = [value / scale for value in work[rank_value]]
        for row in range(rows):
            if row == rank_value or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[rank_value][idx]
                for idx in range(cols)
            ]
        rank_value += 1
        if rank_value == cols:
            break
    return rank_value


def fixed_dimension_pair(left_twist: int, right_twist: int) -> int:
    x = shift3()
    z = clock3()
    x_diag = kron(x, x)
    z_diag = kron(matrix_power(z, left_twist), matrix_power(z, right_twist))
    constraints = stacked(subtract_identity(x_diag), subtract_identity(z_diag))
    return 9 - rank(constraints)


def fixed_dimension_triple(a_twist: int, b_twist: int, c_twist: int) -> int:
    x = shift3()
    z = clock3()
    x_diag = kron(kron(x, x), x)
    z_diag = kron(kron(matrix_power(z, a_twist), matrix_power(z, b_twist)), matrix_power(z, c_twist))
    constraints = stacked(subtract_identity(x_diag), subtract_identity(z_diag))
    return 27 - rank(constraints)


def sm_pair_dimensions(assignments: dict[str, int]) -> dict[str, int]:
    pairs = {
        "up": ("Q", "u"),
        "down": ("Q", "d"),
        "charged_lepton": ("L", "e"),
        "dirac_neutrino": ("L", "N"),
    }
    return {
        name: fixed_dimension_pair(assignments[left], assignments[right])
        for name, (left, right) in pairs.items()
    }


def analyze() -> dict[str, Any]:
    pair_table = {
        f"{left}+{right}": fixed_dimension_pair(left, right)
        for left, right in product(range(3), repeat=2)
    }
    triple_table = {
        f"{a}+{b}+{c}": fixed_dimension_triple(a, b, c)
        for a, b, c in product(range(3), repeat=3)
    }
    same_twist = {"Q": 1, "u": 1, "d": 1, "L": 1, "e": 1, "N": 1}
    conjugate_right = {"Q": 1, "u": 2, "d": 2, "L": 1, "e": 2, "N": 2}
    conjugate_left = {"Q": 2, "u": 1, "d": 1, "L": 2, "e": 1, "N": 1}

    allowed_nontrivial_pairs = [
        key for key, value in pair_table.items() if value == 1 and "0" not in key
    ]

    return {
        "calculation": "IwasawaBlockCouplingInvariantAnalysis",
        "pair_fixed_dimensions": pair_table,
        "triple_fixed_dimensions": triple_table,
        "allowed_nontrivial_pair_orientations": allowed_nontrivial_pairs,
        "same_twist_all_family": {
            "assignments": same_twist,
            "sm_yukawa_pair_fixed_dimensions": sm_pair_dimensions(same_twist),
            "all_four_sm_pairs_allowed": all(
                value == 1 for value in sm_pair_dimensions(same_twist).values()
            ),
        },
        "conjugate_right_family": {
            "assignments": conjugate_right,
            "sm_yukawa_pair_fixed_dimensions": sm_pair_dimensions(conjugate_right),
            "all_four_sm_pairs_allowed": all(
                value == 1 for value in sm_pair_dimensions(conjugate_right).values()
            ),
        },
        "conjugate_left_family": {
            "assignments": conjugate_left,
            "sm_yukawa_pair_fixed_dimensions": sm_pair_dimensions(conjugate_left),
            "all_four_sm_pairs_allowed": all(
                value == 1 for value in sm_pair_dimensions(conjugate_left).values()
            ),
        },
        "e6_like_three_same_twists": {
            "orientation": "1+1+1",
            "fixed_dimension": triple_table["1+1+1"],
            "central_orientation_sum_mod3": 0,
        },
        "selection_rule": {
            "trivial_Higgs_line_requires_pair_sum_zero_mod3": True,
            "same_orientation_matter_pair_with_trivial_Higgs_blocked": True,
            "conjugate_matter_pair_with_trivial_Higgs_allowed": True,
            "orientation_assignment_still_selected_open": True,
        },
        "verdict": {
            "finite_coupling_rule_formulated": True,
            "same_twist_all_family_rejected_for_SM_Higgs_line": True,
            "conjugate_orientation_pairing_needed": True,
            "yukawa_magnitudes_computed": False,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
