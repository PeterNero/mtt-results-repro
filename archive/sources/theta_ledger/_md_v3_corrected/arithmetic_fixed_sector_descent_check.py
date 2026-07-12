"""Executable ledger for the arithmetic fixed-sector descent theorem.

This script proves the finite-abelian-group arithmetic used by the proposed
Lens-Nil Z_7 descent theorem, and keeps the MTT-specific assumptions explicit.
It does not pretend to prove the still-open geometric identifications.
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


def char_order(label: int, modulus: int) -> int:
    return modulus // gcd(label, modulus)


def report(name: str, matrix: list[list[int]]) -> tuple[list[int], int]:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("-" * len(name))
    print("matrix rows:", len(matrix))
    print("torsion factors:", factors)
    print("exponent:", exponent(factors) if factors else 1)
    print("free rank:", free_rank)
    if len(matrix) == 2 and len(matrix[0]) == 2:
        print("determinant:", det2(matrix))
    print()
    return factors, free_rank


def main() -> None:
    k_ln = [[2, 1], [1, 4]]
    carry64 = dyadic_carry_matrix(6)
    family3 = [[3]]
    selected448 = block_diag(carry64, k_ln)
    ambient1344 = block_diag(selected448, family3)

    print("Arithmetic fixed-sector descent check")
    print("=====================================")
    print()

    factors_ln, rank_ln = report("Lens-Nil candidate block K_LN", k_ln)
    factors_64, rank_64 = report("six-stage dyadic carry", carry64)
    factors_448, rank_448 = report("selected CP quotient block", selected448)
    factors_1344, rank_1344 = report("ambient block with family Z3", ambient1344)

    assert det2(k_ln) == 7
    assert factors_ln == [7] and rank_ln == 0
    assert factors_64 == [64] and rank_64 == 0
    assert factors_448 == [448] and rank_448 == 0
    assert factors_1344 == [1344] and rank_1344 == 0

    print("Ambient-to-selected character check")
    print("===================================")
    modulus = 1344
    label = 237
    print("ambient modulus:", modulus)
    print("CKM CP label:", label)
    print("gcd(label, modulus):", gcd(label, modulus))
    print("character order:", char_order(label, modulus))
    print("family kernel:", [0, 448, 896])
    print()
    assert char_order(label, modulus) == 448

    print("Gate status")
    print("===========")
    gates = [
        (
            "fixed topological/differential-cohomology sector",
            "CORPUS-SUPPORTED",
            "Strominger selection fixes Chern/gerbe sector",
        ),
        (
            "left-invariant component equations are Diophantine",
            "CORPUS-SUPPORTED",
            "FCC/flux papers include integer flux/holonomy data",
        ),
        (
            "beta_1,beta_3 treated as component lattice, not naive H^4",
            "HANDLED CAUTION",
            "closure check rules out naive de Rham statement",
        ),
        (
            "K_LN has determinant seven and SNF [7]",
            "FORMAL PASS",
            "proved by Smith normal form",
        ),
        (
            "Z64 x Z7 selected quotient has SNF [448]",
            "FORMAL PASS",
            "coprime factors combine cyclically",
        ),
        (
            "ambient Z3 family quotient leaves selected Z448",
            "FORMAL PASS",
            "kernel {0,448,896}",
        ),
        (
            "residual CP labels w,n are dual to the fixed component quotient",
            "OPEN",
            "main Lens-Nil descent lemma",
        ),
        (
            "O(lambda^2 nu^2) curvature terms do not alter integer K_LN",
            "OPEN",
            "integer-block protection lemma",
        ),
        (
            "six dyadic carry rows are derived from recursive shared circle",
            "OPEN",
            "needed for full order-448 proof",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label_text, status, note in gates:
        print(f"{label_text:{width}s}  {status:{status_width}s}  {note}")

    print()
    print("Conclusion")
    print("==========")
    print("The finite arithmetic is now proved conditional on the descent lemmas.")
    print("The remaining work is geometric/arithmetic identification, not numerology.")


if __name__ == "__main__":
    main()

