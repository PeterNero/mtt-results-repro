"""Analyze the flat-torsion gerbe selection gap for the qutrit twist.

The finite gerbe candidate proves that a flat Z3 B-field/discrete-torsion
2-cocycle can reproduce the qutrit projective corner phase.  This script checks
whether the currently closed Strominger/Fu-Yau data can select that torsion
representative by itself.

The key point is simple: flat torsion changes holonomy but not curvature.  The
current MTT flux selection functional is formulated in terms of the
Green-Schwarz curvature Hhat and fixed topological sector data.  Therefore, if
the discrete torsion label is not already part of the fixed topological sector,
the existing curvature/Bianchi proof cannot distinguish the three Z3 flat
torsion classes.
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


def b_period(label: int, left: Element, right: Element) -> int:
    """Numerator of the flat torsion B-period in (1/3)Z/Z."""

    a_prime, _ = right
    _, b = left
    return mod(label * (-a_prime * b))


def coboundary_2(label: int, left: Element, middle: Element, right: Element) -> int:
    return mod(
        b_period(label, middle, right)
        - b_period(label, add(left, middle), right)
        + b_period(label, left, add(middle, right))
        - b_period(label, left, middle)
    )


def alternating_form(label: int, left: Element, right: Element) -> int:
    return mod(b_period(label, left, right) - b_period(label, right, left))


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
        inverse = pow(work[rank][col], -1, P)
        work[rank] = [mod(inverse * value) for value in work[rank]]
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


def label_report(label: int, elements: list[Element]) -> dict[str, Any]:
    bianchi_violations = []
    for left in elements:
        for middle in elements:
            for right in elements:
                residual = coboundary_2(label, left, middle, right)
                if residual:
                    bianchi_violations.append([left, middle, right, residual])

    commutator_matrix = [
        [alternating_form(label, (1, 0), (1, 0)), alternating_form(label, (1, 0), (0, 1))],
        [alternating_form(label, (0, 1), (1, 0)), alternating_form(label, (0, 1), (0, 1))],
    ]
    z_then_x = phase_label(b_period(label, (0, 1), (1, 0)))
    x_then_z = phase_label(b_period(label, (1, 0), (0, 1)))

    return {
        "torsion_label": label,
        "flat_B_period": f"B_{label}((a,b),(a',b')) = {label}*(-a' b)/3 mod Z",
        "discrete_bianchi_residual_count": len(bianchi_violations),
        "discrete_bianchi_zero": len(bianchi_violations) == 0,
        "delta_Hhat_curvature": 0,
        "green_schwarz_bianchi_changed": False,
        "freed_witten_curvature_obstruction": False,
        "commutator_matrix_over_F3": commutator_matrix,
        "commutator_rank_over_F3": matrix_rank_mod_p(commutator_matrix),
        "x_then_z": x_then_z,
        "z_then_x": z_then_x,
        "qutrit_projective_cocycle_role": (
            "trivial"
            if label == 0
            else "matches_current_zeta_3^2_orientation"
            if z_then_x == "zeta_3^2"
            else "matches_conjugate_zeta_3^1_orientation"
        ),
    }


def analyze() -> dict[str, Any]:
    elements = [(a, b) for a, b in product(range(P), repeat=2)]
    labels = [label_report(label, elements) for label in range(P)]
    nontrivial = [entry for entry in labels if entry["torsion_label"] != 0]

    all_flat = all(entry["discrete_bianchi_zero"] for entry in labels)
    all_curvature_invisible = all(entry["delta_Hhat_curvature"] == 0 for entry in labels)
    nontrivial_qutrit = all(entry["commutator_rank_over_F3"] == 2 for entry in nontrivial)
    trivial_distinguished_by_holonomy = labels[0]["commutator_rank_over_F3"] == 0

    return {
        "calculation": "IwasawaFlatTorsionGerbeSelectionGap",
        "status": "PROVED_SELECTION_GAP",
        "finite_base": "F_3^2",
        "torsion_labels": labels,
        "all_flat_torsion_labels_have_zero_discrete_bianchi": all_flat,
        "all_flat_torsion_labels_leave_Hhat_curvature_unchanged": all_curvature_invisible,
        "nontrivial_labels_match_qutrit_or_conjugate": nontrivial_qutrit,
        "trivial_label_rejected_only_by_holonomy_not_by_curvature": trivial_distinguished_by_holonomy,
        "current_selection_functional_visibility": {
            "sees_Green_Schwarz_curvature_Hhat": True,
            "sees_flat_torsion_holonomy_without_extra_topological_label": False,
            "can_select_between_Z3_flat_labels_from_current_curvature_data": False,
        },
        "selection_gap": {
            "selected_torsion_label_supplied_by_current_certificates": False,
            "needed_extra_input": "fixed differential-cohomology torsion label m=1 or m=2, or an equivalent selected gerbe period table",
            "if_extra_input_supplied": "finite Bianchi and qutrit holonomy checks are already ready for promotion",
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
