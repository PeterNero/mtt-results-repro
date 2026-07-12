"""Analyze the finite cocycle behind the Iwasawa projective magnetic carrier.

The projective carrier uses qutrit clock/shift matrices X,Z with

    X Z = omega Z X,  omega^3 = 1.

This script records the associated F_3^2 projective 2-cocycle, checks the
cocycle identity, proves nontriviality through the alternating commutator form,
and identifies the finite Heisenberg central extension.  It is arithmetic
support for the projective route, not selected MTT source data.
"""

from __future__ import annotations

import json
from itertools import product
from typing import Any


P = 3
Element = tuple[int, int]


def mod(value: int) -> int:
    return value % P


def add(left: Element, right: Element) -> Element:
    return (mod(left[0] + right[0]), mod(left[1] + right[1]))


def cocycle(left: Element, right: Element) -> int:
    """Exponent c(left,right) for U_left U_right = omega^c U_{left+right}.

    With U_(a,b)=X^a Z^b and XZ=omega ZX, one has
    Z^b X^a' = omega^(-a' b) X^a' Z^b.
    """

    a_prime, _ = right
    _, b = left
    return mod(-a_prime * b)


def commutator_exponent(left: Element, right: Element) -> int:
    return mod(cocycle(left, right) - cocycle(right, left))


def matrix_rank_mod_p(matrix: list[list[int]]) -> int:
    work = [[mod(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if work[row][col] % P:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, P)
        work[rank] = [mod(inv * value) for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [
                    mod(work[row][idx] - factor * work[rank][idx])
                    for idx in range(cols)
                ]
        rank += 1
    return rank


def heisenberg_mul(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
) -> tuple[int, int, int]:
    base_left = (left[0], left[1])
    base_right = (right[0], right[1])
    summed = add(base_left, base_right)
    return (
        summed[0],
        summed[1],
        mod(left[2] + right[2] + cocycle(base_left, base_right)),
    )


def analyze() -> dict[str, Any]:
    elements = [(a, b) for a, b in product(range(P), repeat=2)]

    cocycle_identity_violations = []
    for x in elements:
        for y in elements:
            for z in elements:
                left = mod(cocycle(x, y) + cocycle(add(x, y), z))
                right = mod(cocycle(y, z) + cocycle(x, add(y, z)))
                if left != right:
                    cocycle_identity_violations.append([x, y, z, left, right])

    commutator_matrix = [
        [commutator_exponent((1, 0), (1, 0)), commutator_exponent((1, 0), (0, 1))],
        [commutator_exponent((0, 1), (1, 0)), commutator_exponent((0, 1), (0, 1))],
    ]
    rank = matrix_rank_mod_p(commutator_matrix)

    heisenberg_elements = [(a, b, c) for a, b, c in product(range(P), repeat=3)]
    identity = (0, 0, 0)
    associativity_violations = []
    for x in heisenberg_elements:
        for y in heisenberg_elements:
            for z in heisenberg_elements:
                if heisenberg_mul(heisenberg_mul(x, y), z) != heisenberg_mul(
                    x, heisenberg_mul(y, z)
                ):
                    associativity_violations.append([x, y, z])

    center = []
    for x in heisenberg_elements:
        if all(
            heisenberg_mul(x, y) == heisenberg_mul(y, x)
            for y in heisenberg_elements
        ):
            center.append(x)

    nonzero_commutators = sorted(
        {
            commutator_exponent(x, y)
            for x in elements
            for y in elements
            if commutator_exponent(x, y) != 0
        }
    )

    return {
        "calculation": "IwasawaProjectiveTwistCocycleAnalysis",
        "base_group": "F_3^2",
        "relation": "X Z = omega Z X",
        "omega_order": 3,
        "cocycle_exponent": "c((a,b),(a',b')) = -a' b mod 3",
        "cocycle_identity_violations": len(cocycle_identity_violations),
        "commutator_exponent": "B((a,b),(a',b')) = a b' - a' b mod 3",
        "commutator_matrix_on_standard_basis": commutator_matrix,
        "commutator_rank_over_F3": rank,
        "nonzero_commutator_exponents": nonzero_commutators,
        "cocycle_nontrivial": rank > 0,
        "commutator_pairing_nondegenerate": rank == 2,
        "central_extension": {
            "name": "finite Heisenberg group H_3",
            "order": len(heisenberg_elements),
            "center_order": len(center),
            "quotient_order": len(heisenberg_elements) // len(center),
            "identity_is_identity": all(
                heisenberg_mul(identity, x) == x and heisenberg_mul(x, identity) == x
                for x in heisenberg_elements
            ),
            "associativity_violations": len(associativity_violations),
        },
        "interpretation": {
            "ordinary_bundle_coboundary_possible": False,
            "reason": "an abelian 2-coboundary has zero alternating commutator, but this form has rank 2",
            "projective_irrep_dimension": 3,
            "candidate_selected_slot": "ambient family-Z3 or gerbe/discrete-torsion twist; not the q79 character itself",
            "does_not_modify_closed_q79_branch": True,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
