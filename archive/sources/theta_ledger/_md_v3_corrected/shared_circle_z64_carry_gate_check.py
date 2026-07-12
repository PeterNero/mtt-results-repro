"""Gate check for the shared-circle Z64 dyadic carry theorem.

This script separates three things that are easy to blur:

1. six independent binary memories: Z_2^6, exponent 2;
2. one six-stage dyadic carry chain: Z_64, exponent 64;
3. the MTT corpus evidence needed to justify the carry rows.

Only item 2 gives the dyadic order needed for the order-448 CP character.
The spectral projector now derives the D2 tower for the selected tower
operator.  The remaining proof task is to identify the actual MTT flavor
operator with that tower operator and bound the correction.
"""

from __future__ import annotations

from functools import reduce
from math import gcd

from candidate_quotient_mechanism_scan import dyadic_carry_matrix
from recursive_quotient_snf_template import invariant_factors


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def diag(entries: list[int]) -> list[list[int]]:
    return [[entry if i == j else 0 for j, entry in enumerate(entries)] for i, entry in enumerate(entries)]


def chain_without_terminal(levels: int) -> list[list[int]]:
    rows: list[list[int]] = []
    for i in range(levels - 1):
        row = [0] * levels
        row[i] = 2
        row[i + 1] = -1
        rows.append(row)
    return rows


def report(name: str, matrix: list[list[int]]) -> tuple[list[int], int]:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("-" * len(name))
    print("rows:", len(matrix), "cols:", len(matrix[0]) if matrix else 0)
    print("torsion factors:", factors)
    print("exponent:", exponent(factors) if factors else 1)
    print("free rank:", free_rank)
    print()
    return factors, free_rank


def main() -> None:
    independent_bits = diag([2] * 6)
    partial_chain = chain_without_terminal(6)
    carry64 = dyadic_carry_matrix(6)
    direct64 = [[64]]

    print("Shared-circle Z64 carry gate check")
    print("==================================")
    print()

    factors_bits, rank_bits = report("six independent binary memories", independent_bits)
    factors_partial, rank_partial = report("shared-circle carry without terminal closure", partial_chain)
    factors_carry, rank_carry = report("six-stage shared-circle carry", carry64)
    factors_direct, rank_direct = report("direct selected Z64 row", direct64)

    assert factors_bits == [2, 2, 2, 2, 2, 2] and rank_bits == 0
    assert exponent(factors_bits) == 2
    assert factors_partial == [] and rank_partial == 1
    assert factors_carry == [64] and rank_carry == 0
    assert factors_direct == [64] and rank_direct == 0

    print("Gate status")
    print("===========")
    gates = [
        (
            "shared central circle exists",
            "CORPUS-SUPPORTED",
            "central-circle paper and Book",
        ),
        (
            "family Z3 holonomy on central circle exists",
            "CORPUS-SUPPORTED",
            "central-circle flavor appendix",
        ),
        (
            "central-circle phases contribute to CP",
            "CORPUS-SUPPORTED",
            "Yukawa/phase discussion",
        ),
        (
            "proto-spinor supplies structural Z2 memory",
            "CORPUS-SUPPORTED",
            "spinorial return/triadic carrier clues",
        ),
        (
            "six independent Z2 memories give Z64",
            "FAIL",
            "exponent is only 2",
        ),
        (
            "six carry rows plus terminal closure give Z64",
            "FORMAL PASS",
            "SNF [64]",
        ),
        (
            "six-level dyadic refinement tower gives rows",
            "PROVED",
            "row-origin theorem",
        ),
        (
            "spectral P_fl derives the D2 tower",
            "PROVED-SPECTRAL",
            "concrete L_fl,MTT block still needed",
        ),
        (
            "operator-identification stability criterion",
            "PROVED",
            "small-correction theorem for alpha L_tower + E",
        ),
        (
            "extract concrete L_fl,MTT block and norm bound",
            "OPEN",
            "need projector/Wilson/proto-spinor calculation",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
