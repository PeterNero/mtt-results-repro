"""Minimality checks for the six-stage Z64 carry block.

The Z64 carry matrix has five carry rows and one terminal closure row:

    2x_i - x_{i+1} = 0, i=0,...,4
    2x_5 = 0.

This script tests which parts are essential.  Removing any row destroys the
finite Z64 conclusion.  Changing the terminal multiplier m gives order 32*m
after the five carry rows, so m=2 is the minimal terminal closure producing
exactly Z64.
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


def carry_with_terminal(levels: int, terminal: int) -> list[list[int]]:
    rows: list[list[int]] = []
    for i in range(levels - 1):
        row = [0] * levels
        row[i] = 2
        row[i + 1] = -1
        rows.append(row)
    final = [0] * levels
    final[-1] = terminal
    rows.append(final)
    return rows


def remove_row(matrix: list[list[int]], index: int) -> list[list[int]]:
    return [row for i, row in enumerate(matrix) if i != index]


def row_name(index: int) -> str:
    if index < 5:
        return f"carry row {index}: 2x_{index}-x_{index + 1}=0"
    return "terminal row: 2x_5=0"


def report(name: str, matrix: list[list[int]]) -> tuple[list[int], int]:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("-" * len(name))
    print("torsion factors:", factors)
    print("exponent:", exponent(factors) if factors else 1)
    print("free rank:", free_rank)
    print()
    return factors, free_rank


def main() -> None:
    carry = dyadic_carry_matrix(6)

    print("Z64 carry minimality check")
    print("==========================")
    print()

    factors, free_rank = report("full six-stage carry", carry)
    assert factors == [64] and free_rank == 0

    print("Remove-one-row test")
    print("===================")
    for index in range(len(carry)):
        reduced = remove_row(carry, index)
        row_factors, row_rank = invariant_factors(reduced)
        row_exp = exponent(row_factors) if row_factors else 1
        print(f"remove {row_name(index):34s} -> factors={row_factors}, exponent={row_exp}, free_rank={row_rank}")
        assert not (row_factors == [64] and row_rank == 0)
    print()

    print("Terminal multiplier test")
    print("========================")
    for terminal in range(1, 9):
        matrix = carry_with_terminal(6, terminal)
        term_factors, term_rank = invariant_factors(matrix)
        term_exp = exponent(term_factors) if term_factors else 1
        print(f"terminal {terminal}*x_5=0 -> factors={term_factors}, exponent={term_exp}, free_rank={term_rank}")
        assert term_rank == 0
        assert term_exp == 32 * terminal
    print()

    print("Interpretation")
    print("==============")
    print("All five carry rows are needed to tie the six memories into one cyclic chain.")
    print("A terminal closure is needed to make the quotient finite.")
    print("The minimal exact terminal closure giving Z64 is 2x_5=0.")


if __name__ == "__main__":
    main()
