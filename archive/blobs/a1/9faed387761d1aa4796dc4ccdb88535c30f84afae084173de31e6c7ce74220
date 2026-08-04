"""Smith-normal-form templates for possible sevenfold MTT flavor sources.

This script separates actual seven-torsion mechanisms from look-alikes.
It intentionally uses tiny integer matrices: each row is a proposed finite
relation among candidate flavor phase generators.
"""

from __future__ import annotations

from functools import reduce
from math import gcd

from recursive_quotient_snf_template import invariant_factors
from candidate_quotient_mechanism_scan import dyadic_carry_matrix, block_diag


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("  rows:")
    for row in matrix:
        print("   ", row)
    print("  torsion factors:", factors if factors else "none")
    print("  exponent:", exponent(factors) if factors else 1)
    print("  free rank:", free_rank)
    print()


def main() -> None:
    # One generator n. A genuine sevenfold source.
    report("Pure nil/Wilson order-seven row: 7 n = 0", [[7]])

    # Two generators c,n. A monodromy-like identification by itself is not
    # finite; it leaves one free phase direction.
    report("Nil monodromy without terminal closure: n - 7 c = 0", [[-7, 1]])

    # Two generators c,n. Monodromy plus terminal nil closure gives a cyclic
    # order-seven quotient carried by c.
    report(
        "Nil monodromy with terminal nil closure: n=7c, n=0",
        [[-7, 1], [0, 1]],
    )

    # Two generators c,n. Terminal 7n=0 with c identified to n also gives Z7.
    report(
        "Shared-circle/nil lock plus nil seven: c-n=0, 7n=0",
        [[1, -1], [0, 7]],
    )

    # A flux equation that only fixes a ratio of continuous parameters is not
    # a finite quotient unless a compact phase generator is included.
    report(
        "Two independent integer flux labels only: f=0, h=0",
        [[1, 0], [0, 1]],
    )

    # A residual Wilson line of order seven tied to a flux label.
    report(
        "Flux-Wilson congruence: w=f, 7w=0",
        [[1, -1], [0, 7]],
    )

    # Orbifold/discrete gauge row with lens Z3 and sevenfold Wilson line.
    report(
        "Lens family Z3 plus sevenfold Wilson source",
        [[3, 0], [0, 7]],
    )

    # Family Z3 and sevenfold source lock into a cyclic Z21 if the same
    # diagonal phase sees both coprime factors.
    report(
        "Diagonal family-seven lock: 3a-b=0, 7b=0",
        [[3, -1], [0, 7]],
    )

    # Combine the strongest dyadic candidate with several sevenfold templates.
    carry64 = dyadic_carry_matrix(6)
    report(
        "Dyadic carry plus pure nil/Wilson seven",
        block_diag(carry64, [[7]]),
    )
    report(
        "Dyadic carry plus Lens Z3 plus sevenfold Wilson",
        block_diag(carry64, [[3, 0], [0, 7]]),
    )

    # Direct selected CP row. This is valid as a quotient but less explanatory.
    report("Direct diagonal CP row: 448 e = 0", [[448]])

    # Larger recursive carrier with selected order-448 character: ambient
    # quotient Z896 but character 2/896 has order 448.
    report("Larger ambient carrier row: 896 e = 0", [[896]])


if __name__ == "__main__":
    main()
