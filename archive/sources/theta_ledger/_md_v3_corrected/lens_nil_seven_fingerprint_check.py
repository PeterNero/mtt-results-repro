"""Check the determinant-seven fingerprint in the Lens-Nil coefficients.

The Lens x Nil flux papers compute:

    W1 = 2 lambda^2 R^2,
    W3 = 1 lambda nu R^2,
    A  = 4 lambda^2 + O(lambda^2 nu^2),
    B  = 4 nu^2 + O(lambda^2 nu^2).

The primitive determinant-seven candidate block uses the reduced/leading
integer coefficient pattern

    [[2, 1],
     [1, 4]]

whose determinant is seven and whose Smith normal form is [7].

This script does not claim that the Bianchi equations have already been turned
into Wilson/nil character relations.  It also does not claim that the
O(lambda^2 nu^2) curvature terms are automatically irrelevant.  It verifies
the small integer fingerprint needed for the best Z_7 mechanism and records
the exactness/protection lemma as an open proof obligation.
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


def det2(matrix: list[list[int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("  matrix:", matrix)
    print("  determinant:", det2(matrix) if len(matrix) == 2 and len(matrix[0]) == 2 else "n/a")
    print("  torsion factors:", factors)
    print("  exponent:", exponent(factors) if factors else 1)
    print("  free rank:", free_rank)
    print()


def main() -> None:
    w1_coeff = 2
    w3_coeff = 1
    rplus_coeff = 4

    fingerprint = [
        [w1_coeff, w3_coeff],
        [w3_coeff, rplus_coeff],
    ]

    print("Lens-Nil coefficient fingerprint")
    print("================================")
    print("From the Lens x Nil coefficient appendix:")
    print("  W1 = 2 lambda^2 R^2")
    print("  W3 = 1 lambda nu R^2")
    print("  A  = 4 lambda^2 + O(lambda^2 nu^2)")
    print("  B  = 4 nu^2 + O(lambda^2 nu^2)")
    print("The checked block is the reduced/leading integer fingerprint.")
    print()

    report("primitive coefficient block", fingerprint)

    carry64 = dyadic_carry_matrix(6)
    family3 = [[3]]
    report("dyadic carry plus Lens-Nil fingerprint block", block_diag(carry64, fingerprint))
    report(
        "dyadic carry plus Lens-Nil fingerprint block plus family Z3",
        block_diag(block_diag(carry64, fingerprint), family3),
    )

    print("Interpretive status")
    print("===================")
    print("PASS: the determinant-seven integer fingerprint is present.")
    print("OPEN: derive the map from these Bianchi coefficients to character relations on (w,n).")
    print("OPEN: prove higher-order terms do not alter the fixed-sector integer block.")


if __name__ == "__main__":
    main()
