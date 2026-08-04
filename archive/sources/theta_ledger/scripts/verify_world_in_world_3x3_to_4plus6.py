#!/usr/bin/env python3
"""Exact checks for the world-in-world 3x3 to 4+6 reconciliation."""

from __future__ import annotations

import json
from fractions import Fraction


Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: list[list[int]]) -> Matrix:
    return tuple(tuple(Fraction(value) for value in row) for row in rows)


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(3)) for i in range(3)
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(3)) for i in range(3)
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(3)), Fraction(0))
            for j in range(3)
        )
        for i in range(3)
    )


def transpose(value: Matrix) -> Matrix:
    return tuple(tuple(value[j][i] for j in range(3)) for i in range(3))


def frobenius(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        (left[i][j] * right[i][j] for i in range(3) for j in range(3)),
        Fraction(0),
    )


def flatten(value: Matrix) -> list[Fraction]:
    return [value[i][j] for i in range(3) for j in range(3)]


def vector_rank(vectors: list[list[Fraction]]) -> int:
    if not vectors:
        return 0
    work = [row[:] for row in vectors]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column] != 0), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [entry / pivot_value for entry in work[rank]]
        for row in range(rows):
            if row == rank or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][index] - factor * work[rank][index]
                for index in range(columns)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def matrix_rank(value: Matrix) -> int:
    return vector_rank([list(row) for row in value])


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


ZERO = matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
IDENTITY = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

E12 = matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
E13 = matrix([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
E21 = transpose(E12)
E23 = matrix([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
E31 = transpose(E13)
E32 = transpose(E23)

SKEW = [subtract(E12, E21), subtract(E13, E31), subtract(E23, E32)]
SCALAR = [IDENTITY]
DIAGONAL_TRACELESS = [
    matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
]
SYMMETRIC_OFF_DIAGONAL = [add(E12, E21), add(E13, E31), add(E23, E32)]

DIAGONAL = [
    matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
    matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]]),
]
NIL = [E12, E23, E13]

P1 = matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
P2 = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
P3 = IDENTITY
TRACE_LINE = tuple(tuple(Fraction(1, 3) for _ in range(3)) for _ in range(3))
TRACE_ZERO = subtract(IDENTITY, TRACE_LINE)


def blocks_are_orthogonal(blocks: list[list[Matrix]]) -> bool:
    for left_index, left in enumerate(blocks):
        for right in blocks[left_index + 1 :]:
            if any(frobenius(a, b) != 0 for a in left for b in right):
                return False
    return True


def main() -> None:
    polar_blocks = [SKEW, SCALAR, DIAGONAL_TRACELESS, SYMMETRIC_OFF_DIAGONAL]
    polar_basis = [item for block in polar_blocks for item in block]
    iwasawa_basis = SKEW + DIAGONAL + NIL

    checks = {
        "dimension_identity": 1 + 9 == (1 + 3) + (1 + 2 + 3) == 10,
        "polar_basis_rank": vector_rank([flatten(item) for item in polar_basis]) == 9,
        "polar_block_dimensions": [len(block) for block in polar_blocks]
        == [3, 1, 2, 3],
        "polar_blocks_frobenius_orthogonal": blocks_are_orthogonal(polar_blocks),
        "iwasawa_lie_algebra_basis_rank": vector_rank(
            [flatten(item) for item in iwasawa_basis]
        )
        == 9,
        "nil_bracket_xy_is_z": commutator(E12, E23) == E13,
        "nil_bracket_xz_zero": commutator(E12, E13) == ZERO,
        "nil_bracket_yz_zero": commutator(E23, E13) == ZERO,
        "conditional_flag_witness_ranks_are_1_2_3": [
            matrix_rank(P1),
            matrix_rank(P2),
            matrix_rank(P3),
        ]
        == [1, 2, 3],
        "conditional_flag_witness_is_nested": multiply(P1, P2) == P1
        and multiply(P2, P1) == P1
        and multiply(P2, P3) == P2
        and multiply(P3, P2) == P2,
        "trace_line_projector_rank_one": matrix_rank(TRACE_LINE) == 1
        and multiply(TRACE_LINE, TRACE_LINE) == TRACE_LINE,
        "trace_zero_projector_rank_two": matrix_rank(TRACE_ZERO) == 2
        and multiply(TRACE_ZERO, TRACE_ZERO) == TRACE_ZERO,
        "trace_split_is_orthogonal_and_complete": multiply(TRACE_LINE, TRACE_ZERO)
        == ZERO
        and add(TRACE_LINE, TRACE_ZERO) == IDENTITY,
    }

    result = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "exact_checks": checks,
        "proved_scope": {
            "world_in_world_matrix_components": 9,
            "orientation_components": 3,
            "strain_components": 6,
            "polar_symmetric_block_dimensions": [1, 2, 3],
            "conditional_complete_flag_witness_ranks": [1, 2, 3],
            "q79_compatible_trace_split_ranks": [1, 2, 3],
            "nil_lie_algebra": "three-dimensional Heisenberg",
        },
        "not_proved_by_this_certificate": {
            "physical_space_from_SO3_parameters": True,
            "central_scalar_compactifies_to_shared_circle": True,
            "rank_two_sector_globalizes_to_Lens_3_1": True,
            "same_circle_is_shared_by_lens_nil_and_time": True,
            "local_carrier_globalizes_to_q79_Fu_Yau_X6": True,
            "rank_count_alone_sources_a_nested_complete_flag": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
