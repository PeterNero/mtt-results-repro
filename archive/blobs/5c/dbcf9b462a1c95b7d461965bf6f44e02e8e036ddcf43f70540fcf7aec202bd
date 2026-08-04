"""Analyze a discrete gerbe/B-field holonomy model for the qutrit twist.

This supplies the missing *candidate* map:

    flat Z_3 B-field/discrete-torsion holonomy -> qutrit zeta_3 cocycle.

It does not prove MTT selection.  The output is a finite exact calculation
showing that the central cocycle used by the projective magnetic carrier is the
holonomy of a flat torsion two-form on F_3^2, with zero discrete Bianchi
residual in this finite model.
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
    return mod(left[0] + right[0]), mod(left[1] + right[1])


def b_field_period(left: Element, right: Element) -> int:
    """Integer numerator for B(left,right) in (1/3)Z/Z.

    With U_(a,b)=X^a Z^b and XZ=omega ZX, the multiplication cocycle is
    c((a,b),(a',b'))=-a' b mod 3.  This is the flat torsion B-holonomy used
    here.
    """

    a_prime, _ = right
    _, b = left
    return mod(-a_prime * b)


def coboundary_2(left: Element, middle: Element, right: Element) -> int:
    return mod(
        b_field_period(middle, right)
        - b_field_period(add(left, middle), right)
        + b_field_period(left, add(middle, right))
        - b_field_period(left, middle)
    )


def alternating_form(left: Element, right: Element) -> int:
    return mod(b_field_period(left, right) - b_field_period(right, left))


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


def phase_label(exponent: int) -> str:
    return f"zeta_3^{mod(exponent)}"


def table(elements: list[Element]) -> dict[str, dict[str, str]]:
    return {
        str(left): {
            str(right): phase_label(b_field_period(left, right))
            for right in elements
        }
        for left in elements
    }


def analyze() -> dict[str, Any]:
    elements = [(a, b) for a, b in product(range(P), repeat=2)]
    identity = (0, 0)

    bianchi_violations = []
    for left in elements:
        for middle in elements:
            for right in elements:
                residual = coboundary_2(left, middle, right)
                if residual != 0:
                    bianchi_violations.append([left, middle, right, residual])

    normalized = all(
        b_field_period(identity, element) == 0
        and b_field_period(element, identity) == 0
        for element in elements
    )
    commutator_matrix = [
        [alternating_form((1, 0), (1, 0)), alternating_form((1, 0), (0, 1))],
        [alternating_form((0, 1), (1, 0)), alternating_form((0, 1), (0, 1))],
    ]
    commutator_rank = matrix_rank_mod_p(commutator_matrix)
    elementary_square_holonomies = {
        "X_then_Z": phase_label(b_field_period((1, 0), (0, 1))),
        "Z_then_X": phase_label(b_field_period((0, 1), (1, 0))),
        "corner_ratio_XZ_vs_ZX": phase_label(
            alternating_form((1, 0), (0, 1))
        ),
        "corner_ratio_ZX_vs_XZ": phase_label(
            alternating_form((0, 1), (1, 0))
        ),
    }

    return {
        "calculation": "IwasawaDiscreteGerbeHolonomyCandidate",
        "status": "CANDIDATE_MAP_CLOSED_SELECTION_OPEN",
        "finite_base": "F_3^2",
        "flat_torsion_B_period": "B((a,b),(a',b')) = -a' b / 3 mod Z",
        "holonomy_formula": "Hol_B(x,y)=exp(2*pi*i*(-a' b)/3)",
        "normalized_cocycle": normalized,
        "discrete_bianchi_residual_count": len(bianchi_violations),
        "discrete_bianchi_residual_zero": len(bianchi_violations) == 0,
        "commutator_matrix_on_standard_basis": commutator_matrix,
        "commutator_rank_over_F3": commutator_rank,
        "nontrivial_discrete_torsion": commutator_rank == 2,
        "elementary_square_holonomies": elementary_square_holonomies,
        "sample_holonomy_table": table(elements),
        "matches_qutrit_projective_cocycle": True,
        "selection_status": {
            "selected_by_mtt": False,
            "fixed_differential_cohomology_class_for_this_twist": False,
            "green_schwarz_bianchi_for_full_heterotic_background": "not checked by this finite flat model",
            "freed_witten_for_selected_cycles": "not checked by this finite flat model",
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
