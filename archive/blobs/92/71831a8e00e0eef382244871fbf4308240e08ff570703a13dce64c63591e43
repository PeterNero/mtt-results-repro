"""Search primitive two-row Lens-Nil blocks that derive Z_7 by elimination.

The point is to avoid inserting a row 7w=0 by hand.  A primitive 2x2 integer
relation block

    a w + b n = 0
    c w + d n = 0

has finite quotient of order |ad-bc| when the determinant is nonzero.  If the
entries have gcd 1 and |ad-bc|=7, then the Smith normal form is [7].

Equivalently, eliminating one generator gives:

    (ad-bc) w = 0,
    (ad-bc) n = 0.

So an order-seven row can be a consequence of two small, independent
Lens-Nil/Bianchi/Wilson compatibility rows, not an explicit assumption.
"""

from __future__ import annotations

from functools import reduce
from math import gcd

from candidate_quotient_mechanism_scan import block_diag, dyadic_carry_matrix
from recursive_quotient_snf_template import invariant_factors


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def entry_gcd(matrix: list[list[int]]) -> int:
    out = 0
    for row in matrix:
        for entry in row:
            out = gcd(out, abs(entry))
    return out


def det2(matrix: list[list[int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def row_col_nonzero(matrix: list[list[int]]) -> bool:
    return (
        any(matrix[0])
        and any(matrix[1])
        and any(row[0] for row in matrix)
        and any(row[1] for row in matrix)
    )


def main() -> None:
    primitive_hits: list[list[list[int]]] = []
    positive_hits: list[list[list[int]]] = []

    for a in range(-4, 5):
        for b in range(-4, 5):
            for c in range(-4, 5):
                for d in range(-4, 5):
                    matrix = [[a, b], [c, d]]
                    if not row_col_nonzero(matrix):
                        continue
                    if abs(det2(matrix)) != 7:
                        continue
                    if entry_gcd(matrix) != 1:
                        continue
                    factors, free_rank = invariant_factors(matrix)
                    if factors != [7] or free_rank != 0:
                        continue
                    primitive_hits.append(matrix)
                    if all(entry >= 0 for row in matrix for entry in row):
                        positive_hits.append(matrix)

    primitive_hits.sort(key=lambda m: (max(abs(x) for row in m for x in row), sum(abs(x) for row in m for x in row), m))
    positive_hits.sort(key=lambda m: (max(abs(x) for row in m for x in row), sum(abs(x) for row in m for x in row), m))

    print("Primitive determinant-seven Lens-Nil blocks")
    print("==========================================")
    print(f"primitive hits with entries in [-4,4]: {len(primitive_hits)}")
    print(f"nonnegative primitive hits: {len(positive_hits)}")
    print()

    print("Small nonnegative examples")
    print("==========================")
    for matrix in positive_hits[:12]:
        print(f"{matrix[0]}  {matrix[1]}  det={det2(matrix):2d}")
    print()

    chosen = [[2, 1], [1, 4]]
    factors, free_rank = invariant_factors(chosen)
    print("Chosen primitive block")
    print("======================")
    print("generators: w, n")
    print("relations:")
    print("  2w + n = 0")
    print("   w + 4n = 0")
    print(f"determinant: {det2(chosen)}")
    print("torsion factors:", factors)
    print("exponent:", exponent(factors))
    print("free rank:", free_rank)
    print()
    print("Elimination consequence")
    print("=======================")
    print("4*(2w+n) - 1*(w+4n) = 7w = 0")
    print("-1*(2w+n) + 2*(w+4n) = 7n = 0")
    print()

    carry64 = dyadic_carry_matrix(6)
    family3 = [[3]]
    combined_minimal = block_diag(carry64, chosen)
    combined_ambient = block_diag(combined_minimal, family3)
    for name, matrix in (
        ("dyadic carry plus primitive determinant-seven block", combined_minimal),
        ("dyadic carry plus primitive determinant-seven block plus family Z3", combined_ambient),
    ):
        factors, free_rank = invariant_factors(matrix)
        print(name)
        print("  torsion factors:", factors)
        print("  exponent:", exponent(factors))
        print("  free rank:", free_rank)
        print()

    print("Proof gate")
    print("==========")
    print("Derive two independent MTT Lens-Nil/Wilson rows whose primitive coefficient block has determinant +/-7.")


if __name__ == "__main__":
    main()
