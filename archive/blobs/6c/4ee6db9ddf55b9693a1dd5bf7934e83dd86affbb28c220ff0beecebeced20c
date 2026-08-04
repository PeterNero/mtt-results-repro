"""Small Smith-normal-form invariant calculator for recursive quotient tests.

This avoids external dependencies.  It computes torsion invariant factors from
determinantal divisors, which is practical for the small relation matrices used
in the flavor-holonomy quotient notes.

Rows are integer relations; columns are carrier generators.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd


def det_int(matrix: list[list[int]]) -> int:
    """Exact determinant by fraction Gaussian elimination."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    sign = 1
    for i in range(n):
        pivot = None
        for r in range(i, n):
            if a[r][i] != 0:
                pivot = r
                break
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            sign *= -1
        p = a[i][i]
        det *= p
        for r in range(i + 1, n):
            factor = a[r][i] / p
            for c in range(i, n):
                a[r][c] -= factor * a[i][c]
    out = det * sign
    if out.denominator != 1:
        raise ArithmeticError("nonintegral determinant from integer matrix")
    return int(out)


def rank_q(matrix: list[list[int]]) -> int:
    """Rank over Q."""
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if a[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col] != 0:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def gcd_of_minors(matrix: list[list[int]], k: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    g = 0
    for rs in combinations(range(rows), k):
        for cs in combinations(range(cols), k):
            minor = [[matrix[r][c] for c in cs] for r in rs]
            g = gcd(g, abs(det_int(minor)))
    return g


def invariant_factors(matrix: list[list[int]]) -> tuple[list[int], int]:
    """Return nontrivial torsion factors and free rank of Z^cols / rows(matrix)."""
    if not matrix:
        return [], 0
    cols = len(matrix[0])
    rank = rank_q(matrix)
    divisors = [1]
    for k in range(1, rank + 1):
        divisors.append(gcd_of_minors(matrix, k))
    factors = []
    for k in range(1, rank + 1):
        if divisors[k - 1] == 0:
            raise ArithmeticError("bad determinantal divisor")
        factor = divisors[k] // divisors[k - 1]
        if factor > 1:
            factors.append(factor)
    return factors, cols - rank


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("  torsion factors:", factors if factors else "none")
    print("  free rank:", free_rank)
    print()


def main() -> None:
    # Generators:
    # e_c, e_l, e_n, e_12, e_23, e_31

    bare_lens_phase_sum = [
        [0, 3, 0, 0, 0, 0],  # 3 e_l = 0
        [0, 0, 0, 1, 1, 1],  # e_12 + e_23 + e_31 = 0
    ]
    report("Bare terminal lens torsion plus phase sum", bare_lens_phase_sum)

    shared_lens_a1 = [
        [-1, 1, 0, 0, 0, 0],  # e_l = e_c
        [0, 3, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
    ]
    report("Shared circle with e_l = e_c, plus lens torsion", shared_lens_a1)

    shared_lens_a7 = [
        [-7, 1, 0, 0, 0, 0],  # e_l = 7 e_c
        [0, 3, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
    ]
    report("Toy shared circle with e_l = 7 e_c, plus lens torsion", shared_lens_a7)

    # Toy only: this demonstrates what a derived order-448 relation would look
    # like algebraically.  It is not an MTT derivation.
    toy_448_relation = [
        [448, 0, 0, 0, 0, 0],  # 448 e_c = 0
        [0, 0, 0, 1, 1, 1],
    ]
    report("Toy shared-circle Z_448 relation, not derived", toy_448_relation)

    toy_64_x_7 = [
        [64, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
    ]
    report("Toy product quotient Z_64 x Z_7, not derived", toy_64_x_7)


if __name__ == "__main__":
    main()
