"""Arithmetic descent check for the Mukai Z_7 replacement route.

The old Lens-Nil source and the new Mukai source share the same integer block

    K = [[2, 1],
         [1, 4]]

but their geometric status is different.  The Lens-Nil coefficient derivation
is blocked by exterior-calculus consistency.  The Mukai route realizes the same
block as a positive charge-pairing matrix in the algebraic Mukai lattice.

This script keeps the finite arithmetic separate from the geometric gates:

    Z_64 x Z_7 ~= Z_448
    Z_64 x Z_7 x Z_3 ~= Z_1344
    quotient by the family Z_3 leaves the selected order-448 character.
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
    k_mukai = [[2, 1], [1, 4]]
    carry64 = dyadic_carry_matrix(6)
    family3 = [[3]]
    selected448 = block_diag(carry64, k_mukai)
    ambient1344 = block_diag(selected448, family3)

    print("Mukai fixed-sector descent check")
    print("================================")
    print()

    factors_7, rank_7 = report("Mukai positive charge block K_Mukai", k_mukai)
    factors_64, rank_64 = report("six-stage dyadic carry", carry64)
    factors_448, rank_448 = report("selected CP quotient block", selected448)
    factors_1344, rank_1344 = report("ambient block with family Z3", ambient1344)

    assert det2(k_mukai) == 7
    assert factors_7 == [7] and rank_7 == 0
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
            "Mukai charge block has determinant seven and SNF [7]",
            "PASS",
            "explicit positive primitive Mukai vectors",
        ),
        (
            "Z64 x Z7 selected quotient has SNF [448]",
            "PASS",
            "coprime invariant factors combine cyclically",
        ),
        (
            "ambient Z3 family quotient leaves selected Z448",
            "PASS",
            "kernel {0,448,896}",
        ),
        (
            "stable sheaf/bundle realization",
            "PROVED/OPTIONAL",
            "stable sheaves proved; local-freeness is only a stronger route",
        ),
        (
            "CP labels equal Hom(coker K_Mukai,U(1))",
            "PROVED",
            "finite-character identification for selected A_P",
        ),
        (
            "MTT fixed-sector selection",
            "CLOSED-CHARGE",
            "Bianchi-compatible Fu-Yau/Mukai charge sector now supplied",
        ),
        (
            "Fu-Yau anomaly/topological completion",
            "CLOSED-CHARGE",
            "closed by the Fu-Yau/Mukai charge-sector certificate",
        ),
        (
            "six dyadic carry rows supplied by exact branch",
            "CLOSED-EXACT",
            "Z64 exact certificate supplies A64; recursive derivation is optional",
        ),
    ]
    width = max(len(label_text) for label_text, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label_text, status, note in gates:
        print(f"{label_text:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
