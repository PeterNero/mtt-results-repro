"""Attempt the simplest invariant Dolbeault model for the visible L^2 Ext gate.

The previous source hunt found no selected Cech/Dolbeault packet for
H^1(X,L^2), L=(1,-2,0).  This script tests the smallest possible construction:
a scalar left-invariant (0,1) Dolbeault operator on the Iwasawa anti-holomorphic
basis.  It is useful because it is fully computable, and because it shows why
the next real packet must contain nontrivial transition/automorphy data rather
than only a global invariant scalar potential.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

SOURCE_HUNT = CERTIFICATES / "visible_rank2_l2_cohomology_source_hunt_certificate.json"
L2_GATE = CERTIFICATES / "visible_rank2_l2_ext_h1_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_invariant_dolbeault_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_invariant_dolbeault_attempt_certificate.json"

TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]
TARGET_C2 = [4, 0, 0]

Basis = list[tuple[int, ...]]
Matrix = list[list[Fraction]]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def wedge(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, tuple[int, ...]] | None:
    merged = list(left) + list(right)
    if len(set(merged)) != len(merged):
        return None
    inversions = 0
    for i, value in enumerate(merged):
        for later in merged[i + 1 :]:
            if value > later:
                inversions += 1
    sign = -1 if inversions % 2 else 1
    return sign, tuple(sorted(merged))


def add_form(
    total: dict[tuple[int, ...], Fraction],
    coeff: Fraction,
    form: tuple[int, ...],
) -> None:
    if coeff == 0:
        return
    total[form] = total.get(form, Fraction(0)) + coeff
    if total[form] == 0:
        del total[form]


def dbar_basis_one(index: int) -> dict[tuple[int, ...], Fraction]:
    if index == 3:
        return {(1, 2): Fraction(1)}
    return {}


def dbar(form: tuple[int, ...]) -> dict[tuple[int, ...], Fraction]:
    if not form:
        return {}
    total: dict[tuple[int, ...], Fraction] = {}
    for pos, idx in enumerate(form):
        prefix = form[:pos]
        suffix = form[pos + 1 :]
        deriv_sign = Fraction(-1 if pos % 2 else 1)
        for d_form, coeff in dbar_basis_one(idx).items():
            left = wedge(prefix, d_form)
            if left is None:
                continue
            sign_left, partial = left
            full = wedge(partial, suffix)
            if full is None:
                continue
            sign_full, out_form = full
            add_form(total, deriv_sign * sign_left * sign_full * coeff, out_form)
    return total


def wedge_with_a(form: tuple[int, ...], a1: int, a2: int, a3: int) -> dict[tuple[int, ...], Fraction]:
    total: dict[tuple[int, ...], Fraction] = {}
    for coeff, basis_form in (
        (Fraction(a1), (1,)),
        (Fraction(a2), (2,)),
        (Fraction(a3), (3,)),
    ):
        if coeff == 0:
            continue
        result = wedge(basis_form, form)
        if result is None:
            continue
        sign, out_form = result
        add_form(total, coeff * sign, out_form)
    return total


def d_operator(form: tuple[int, ...], a1: int, a2: int, a3: int) -> dict[tuple[int, ...], Fraction]:
    total = dbar(form)
    for out_form, coeff in wedge_with_a(form, a1, a2, a3).items():
        add_form(total, coeff, out_form)
    return total


def matrix_for_domain(domain: Basis, codomain: Basis, a1: int, a2: int, a3: int) -> Matrix:
    rows = [[Fraction(0) for _ in domain] for _ in codomain]
    row_index = {form: index for index, form in enumerate(codomain)}
    for col, form in enumerate(domain):
        image = d_operator(form, a1, a2, a3)
        for out_form, coeff in image.items():
            rows[row_index[out_form]][col] = coeff
    return rows


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return []
    rows = len(left)
    mids = len(left[0])
    if mids != len(right):
        raise ValueError("shape mismatch")
    cols = len(right[0])
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(mids)) for col in range(cols)]
        for row in range(rows)
    ]


def rank(matrix: Matrix) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or rows[row][col] == 0:
                continue
            factor = rows[row][col]
            rows[row] = [
                rows[row][entry_col] - factor * rows[pivot_row][entry_col]
                for entry_col in range(col_count)
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def matrix_to_json(matrix: Matrix) -> list[list[int | str]]:
    encoded: list[list[int | str]] = []
    for row in matrix:
        out_row: list[int | str] = []
        for value in row:
            out_row.append(value.numerator if value.denominator == 1 else str(value))
        encoded.append(out_row)
    return encoded


def all_zero(matrix: Matrix) -> bool:
    return all(value == 0 for row in matrix for value in row)


def scan_candidate(a1: int, a2: int, a3: int) -> dict[str, Any]:
    c0 = [()]
    c1 = [(1,), (2,), (3,)]
    c2 = [(1, 2), (1, 3), (2, 3)]
    c3 = [(1, 2, 3)]
    d0 = matrix_for_domain(c0, c1, a1, a2, a3)
    d1 = matrix_for_domain(c1, c2, a1, a2, a3)
    d2 = matrix_for_domain(c2, c3, a1, a2, a3)
    d1d0 = matmul(d1, d0)
    d2d1 = matmul(d2, d1)
    integrable = all_zero(d1d0) and all_zero(d2d1)
    rank_d0 = rank(d0)
    rank_d1 = rank(d1)
    dim_ker_d1 = len(c1) - rank_d1
    h1 = dim_ker_d1 - rank_d0
    return {
        "a_vector": [a1, a2, a3],
        "operator": f"D_A = dbar + ({a1})e1 + ({a2})e2 + ({a3})e3 wedge",
        "integrability_condition": "a3=0 for scalar invariant global A",
        "integrable": integrable,
        "d1_d0_zero": all_zero(d1d0),
        "d2_d1_zero": all_zero(d2d1),
        "rank_d0": rank_d0,
        "rank_d1": rank_d1,
        "dim_ker_d1": dim_ker_d1,
        "h1": h1 if integrable else None,
        "topological_c1_vector_abc": [0, 0, 0],
        "matches_target_c1_L_squared": False,
    }


def trivial_fixture_packet() -> dict[str, Any]:
    return {
        "schema": "VisibleRank2L2CohomologyData.v1",
        "status": "COMPLETE",
        "candidate_role": "UNSELECTED_FIXTURE",
        "target": {
            "extension_sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "l_vector_abc": TARGET_L,
            "c1_L_squared_vector_abc": TARGET_L2,
            "c1_L_squared_square_alpha_coeffs": [-16, 0, 0],
            "c2_extension_alpha_coeffs": TARGET_C2,
        },
        "source": {
            "source_kind": "finite_fixture",
            "selected_by_mtt": False,
            "fixture_only": True,
            "source_certificate": "",
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "cochain_complex": {
            "field": "Q",
            "basis_labels_C0": ["1"],
            "basis_labels_C1": ["e1", "e2", "e3"],
            "basis_labels_C2": ["e12", "e13", "e23"],
            "d0": {"matrix": [[0], [0], [0]]},
            "d1": {"matrix": [[0, 0, 1], [0, 0, 0], [0, 0, 0]]},
        },
        "reported_cohomology": {
            "rank_d0": 0,
            "rank_d1": 1,
            "dim_ker_d1": 2,
            "h1": 2,
            "nonzero_extension_class_label": "eta=e1",
            "extension_class_vector_C1": [1, 0, 0],
        },
        "acceptance_tests": {
            "d1_d0_zero": True,
            "h1_positive": True,
            "extension_class_closed": True,
            "extension_class_not_exact": True,
            "derived_without_observed_flavor_inputs": True,
        },
    }


def analyze() -> dict[str, Any]:
    source_hunt = load_json(SOURCE_HUNT)
    l2_gate = load_json(L2_GATE)
    scan = [
        scan_candidate(a1, a2, a3)
        for a1 in (-1, 0, 1)
        for a2 in (-1, 0, 1)
        for a3 in (-1, 0, 1)
    ]
    integrable = [item for item in scan if item["integrable"]]
    positive_h1 = [item for item in integrable if item["h1"] and item["h1"] > 0]
    nontrivial_positive_h1 = [
        item for item in positive_h1 if item["a_vector"] != [0, 0, 0]
    ]
    trivial = next(item for item in scan if item["a_vector"] == [0, 0, 0])
    nonzero_integrable = [item for item in integrable if item["a_vector"] != [0, 0, 0]]

    report = {
        "calculation": "VisibleRank2L2InvariantDolbeaultAttempt",
        "status": "VISIBLE_RANK2_L2_INVARIANT_DOLBEAULT_ATTEMPT_BLOCKED_NEEDS_TRANSITIONS",
        "generated_by": "scripts/attempt_visible_rank2_l2_invariant_dolbeault.py",
        "input_certificates": {
            "visible_rank2_l2_cohomology_source_hunt": SOURCE_HUNT.name,
            "visible_rank2_l2_ext_h1_gate": L2_GATE.name,
        },
        "target": {
            "l_vector_abc": TARGET_L,
            "c1_L_squared_vector_abc": TARGET_L2,
            "c2_extension_alpha_coeffs": TARGET_C2,
        },
        "ansatz": {
            "description": "global scalar left-invariant Dolbeault operator D_A=dbar+A wedge",
            "basis_rules": {
                "dbar_e1": 0,
                "dbar_e2": 0,
                "dbar_e3": "e1 wedge e2",
            },
            "A": "a1*e1+a2*e2+a3*e3 with ai in {-1,0,1}",
            "integrability": "D_A^2=0 iff a3=0",
            "topological_scope": (
                "a global scalar potential on a single smooth trivialization has "
                "c1=0; nonzero c1 requires transition/automorphy data or an "
                "equivalent nontrivial line-bundle representative"
            ),
        },
        "scan_summary": {
            "candidate_count": len(scan),
            "integrable_count": len(integrable),
            "integrable_vectors": [item["a_vector"] for item in integrable],
            "positive_h1_count": len(positive_h1),
            "nontrivial_positive_h1_count": len(nontrivial_positive_h1),
            "nonzero_integrable_h1_values": {
                str(item["a_vector"]): item["h1"] for item in nonzero_integrable
            },
            "trivial_A_h1": trivial["h1"],
            "all_global_scalar_c1_vectors": [[0, 0, 0]],
            "target_c1_L_squared_hit": False,
        },
        "representative_matrices": {
            "trivial_A_d0": [[0], [0], [0]],
            "trivial_A_d1": [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
            "nonzero_integrable_example_A_1_0_0": {
                "d0": matrix_to_json(matrix_for_domain([()], [(1,), (2,), (3,)], 1, 0, 0)),
                "d1": matrix_to_json(
                    matrix_for_domain(
                        [(1,), (2,), (3,)],
                        [(1, 2), (1, 3), (2, 3)],
                        1,
                        0,
                        0,
                    )
                ),
                "h1": next(item for item in scan if item["a_vector"] == [1, 0, 0])["h1"],
            },
        },
        "validator_fixture": {
            "role": "UNSELECTED_FIXTURE",
            "packet": trivial_fixture_packet(),
            "meaning": (
                "The trivial invariant complex can pass finite cochain algebra, "
                "but only as an unselected fixture. It has c1=0, not c1(L^2)=(2,-4,0)."
            ),
        },
        "calculation_results": {
            "source_hunt_blocked_selected_data_absent": source_hunt.get("status")
            == "VISIBLE_RANK2_L2_COHOMOLOGY_SOURCE_HUNT_BLOCKED_SELECTED_DATA_ABSENT",
            "l2_validator_available": l2_gate.get("status")
            == "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN",
            "invariant_scalar_integrability_classified": True,
            "trivial_invariant_complex_has_h1_positive": trivial["h1"] > 0,
            "nontrivial_integrable_invariant_complex_has_h1_positive": bool(
                nontrivial_positive_h1
            ),
            "invariant_global_scalar_ansatz_hits_target_c1_L_squared": False,
            "selected_L2_packet_constructed": False,
        },
        "what_this_closes": {
            "simplest_global_invariant_scalar_dolbeault_route_tested": True,
            "integrability_condition_a3_zero": True,
            "trivial_fixture_h1_positive_but_unselected": True,
            "global_scalar_ansatz_cannot_realize_nonzero_c1_L_squared": True,
            "transition_or_automorphy_data_required": True,
        },
        "still_open": {
            "construct_selected_L2_transition_or_automorphy_data": True,
            "compute_actual_h1_for_nontrivial_L_squared": True,
            "select_nonzero_extension_class": True,
            "prove_non_split_extension_stability": True,
            "prove_HYM_or_Route_C_residual": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_trivial_fixture_is_selected": False,
            "claims_global_scalar_ansatz_hits_target_c1": False,
            "claims_actual_H1_for_L_squared": False,
            "claims_nonzero_Ext_class_selected": False,
            "claims_stability_proved": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The simplest invariant scalar Dolbeault construction does not "
                "close H^1(X,L^2). Integrability forces a3=0. The only positive "
                "h1 case in the scanned global scalar ansatz is the trivial "
                "A=0 complex with h1=2, but that is a c1=0 unselected fixture. "
                "Every nonzero integrable global scalar candidate has h1=0, and "
                "none can realize c1(L^2)=(2,-4,0)."
            ),
            "next_action": (
                "Move from global invariant scalar potentials to a genuine "
                "line-bundle representative: transition/automorphy data or an "
                "equivalent nontrivial Dolbeault operator carrying "
                "c1(L^2)=(2,-4,0)."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2InvariantDolbeaultAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_invariant_dolbeault_attempt.candidate.json",
        "input_certificates": report["input_certificates"],
        "target": report["target"],
        "ansatz": report["ansatz"],
        "scan_summary": report["scan_summary"],
        "representative_matrices": report["representative_matrices"],
        "validator_fixture": report["validator_fixture"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
