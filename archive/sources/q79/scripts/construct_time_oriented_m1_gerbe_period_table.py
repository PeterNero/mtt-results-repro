"""Construct the time-oriented m=1 finite gerbe period table.

The previous certificate fixed the retarded q79/F representative to torsion
label m=1.  This script turns that label into an explicit finite
Deligne/Cech/B-field table on the quotient actually used by the qutrit
projective carrier:

    G = F_3^2,
    B_m((a,b),(c,d)) = -m c b / 3  mod Z.

For m=1 the commutator is the qutrit Fourier/Heisenberg cocycle selected by
the time-oriented q79 branch.  This closes the finite period-table layer only.
It deliberately does not claim full heterotic Bianchi/Freed-Witten/projector
retention or selected D_E/dotD operator data.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE = ROOT / "candidate_data" / "time_oriented_m1_gerbe_period_table.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_gerbe_period_table_certificate.json"
MOD = 3


Element = tuple[int, int]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def add(left: Element, right: Element) -> Element:
    return ((left[0] + right[0]) % MOD, (left[1] + right[1]) % MOD)


def label(element: Element) -> str:
    return f"{element[0]}{element[1]}"


def period_mod3(m: int, left: Element, right: Element) -> int:
    """Return the numerator n in B(left,right)=n/3 mod Z."""
    _a, b = left
    c, _d = right
    return (-m * c * b) % MOD


def delta_mod3(m: int, g: Element, h: Element, k: Element) -> int:
    """Group cohomology coboundary of the 2-cochain, in thirds mod 1."""
    return (
        period_mod3(m, h, k)
        - period_mod3(m, add(g, h), k)
        + period_mod3(m, g, add(h, k))
        - period_mod3(m, g, h)
    ) % MOD


def commutator_mod3(m: int, left: Element, right: Element) -> int:
    return (period_mod3(m, left, right) - period_mod3(m, right, left)) % MOD


def rank_over_f3(matrix: list[list[int]]) -> int:
    work = [[entry % MOD for entry in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if work[row][col] % MOD:
                pivot = row
                break
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inv = pow(work[pivot_row][col], -1, MOD)
        work[pivot_row] = [(value * inv) % MOD for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][col] % MOD == 0:
                continue
            factor = work[row][col]
            work[row] = [
                (work[row][idx] - factor * work[pivot_row][idx]) % MOD
                for idx in range(cols)
            ]
        pivot_row += 1
    return pivot_row


def holonomy_label(value_mod3: int) -> str:
    labels = {0: "1", 1: "zeta_3", 2: "zeta_3^2"}
    return labels[value_mod3 % MOD]


def table_for_label(m: int) -> dict[str, Any]:
    elements = [(a, b) for a, b in product(range(MOD), repeat=2)]
    period_table = {
        f"{label(left)}|{label(right)}": period_mod3(m, left, right)
        for left in elements
        for right in elements
    }
    holonomy_table = {
        key: holonomy_label(value) for key, value in period_table.items()
    }
    deltas = {
        f"{label(g)}|{label(h)}|{label(k)}": delta_mod3(m, g, h, k)
        for g in elements
        for h in elements
        for k in elements
    }
    nonzero_deltas = {key: value for key, value in deltas.items() if value != 0}
    basis = [(1, 0), (0, 1)]
    commutator = [
        [commutator_mod3(m, left, right) for right in basis]
        for left in basis
    ]
    rank = rank_over_f3(commutator)
    normalized = all(
        period_mod3(m, (0, 0), element) == 0
        and period_mod3(m, element, (0, 0)) == 0
        for element in elements
    )
    return {
        "group": {
            "name": "F_3^2",
            "elements": [{"label": label(element), "a": element[0], "b": element[1]} for element in elements],
            "operation": "componentwise addition mod 3",
        },
        "torsion_label_m": m,
        "period_formula": "B_m((a,b),(c,d)) = -m*c*b/3 mod Z",
        "period_table_mod3": period_table,
        "holonomy_table": holonomy_table,
        "coboundary_delta_checked_triples": len(deltas),
        "nonzero_coboundary_deltas_mod3": nonzero_deltas,
        "all_coboundary_deltas_zero": not nonzero_deltas,
        "normalized_two_cocycle": normalized,
        "commutator_matrix_mod3_on_basis_e1_e2": commutator,
        "commutator_rank_over_F3": rank,
        "finite_heisenberg_extension_order": 27 if rank == 2 else 9,
        "ordinary_bundle_coboundary_possible": rank == 0,
        "nontrivial_qutrit_heisenberg_type": rank == 2,
    }


def analyze() -> dict[str, Any]:
    fixed = load_json(CERTIFICATES / "time_oriented_fixed_gerbe_representative_certificate.json")
    selected_type = load_json(CERTIFICATES / "selected_gerbe_fourier_type_theorem_certificate.json")
    holonomy = load_json(CERTIFICATES / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    m1 = table_for_label(1)
    m2 = table_for_label(2)

    fixed_m1 = (
        get(fixed, "calculation_results", "time_oriented_finite_representative_closed") is True
        and get(fixed, "branch_representatives", "time_oriented_q79", "torsion_label_m") == 1
    )
    selected_type_closed = get(
        selected_type,
        "calculation_results",
        "selected_gerbe_fourier_type_closed",
    ) is True
    candidate_map_closed = get(
        holonomy,
        "what_this_closes",
        "candidate_zeta3_holonomy_map",
    ) is True

    expected_commutator = [[0, 1], [2, 0]]
    finite_table_closed = (
        fixed_m1
        and selected_type_closed
        and candidate_map_closed
        and m1["all_coboundary_deltas_zero"] is True
        and m1["normalized_two_cocycle"] is True
        and m1["commutator_matrix_mod3_on_basis_e1_e2"] == expected_commutator
        and m1["ordinary_bundle_coboundary_possible"] is False
    )

    status = (
        "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN"
        if finite_table_closed
        else "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_NOT_CLOSED"
    )

    return {
        "candidate": "TimeOrientedM1GerbePeriodTable",
        "status": status,
        "generated_by": "scripts/construct_time_oriented_m1_gerbe_period_table.py",
        "selected_branch": {
            "q": 79,
            "orientation": "F",
            "torsion_label_m": 1,
            "fixed_by_certificate": "time_oriented_fixed_gerbe_representative_certificate.json",
            "time_oriented_representative_closed": fixed_m1,
        },
        "finite_period_table": m1,
        "antiunitary_conjugate_table_retained": {
            "q": 369,
            "orientation": "F*",
            "torsion_label_m": 2,
            "period_table": m2,
        },
        "input_closure": {
            "selected_gerbe_fourier_type_closed": selected_type_closed,
            "finite_zeta3_holonomy_candidate_map_closed": candidate_map_closed,
            "time_oriented_m1_representative_closed": fixed_m1,
        },
        "calculation_results": {
            "finite_m1_period_table_constructed": finite_table_closed,
            "period_table_is_normalized_two_cocycle": m1["normalized_two_cocycle"],
            "discrete_bianchi_delta_zero": m1["all_coboundary_deltas_zero"],
            "commutator_matrix_matches_qutrit_F_orientation": (
                m1["commutator_matrix_mod3_on_basis_e1_e2"] == expected_commutator
            ),
            "commutator_rank_two": m1["commutator_rank_over_F3"] == 2,
            "ordinary_bundle_coboundary_ruled_out": m1["ordinary_bundle_coboundary_possible"] is False,
            "antiunitary_m2_table_retained": (
                m2["commutator_matrix_mod3_on_basis_e1_e2"] == [[0, 2], [1, 0]]
            ),
        },
        "what_this_closes": {
            "actual_finite_B_field_period_table_on_selected_quotient": finite_table_closed,
            "map_from_m1_period_table_to_zeta3_qutrit_cocycle": finite_table_closed,
            "finite_flat_discrete_bianchi_identity": finite_table_closed,
            "ordinary_bundle_coboundary_escape_for_m1": False,
            "m1_source_is_not_just_a_flag_lift": finite_table_closed,
        },
        "still_open": {
            "full_Deligne_Cech_representative_on_geometric_cover": True,
            "heterotic_Green_Schwarz_embedding_for_selected_twist": True,
            "Freed_Witten_verification_on_selected_cycles": True,
            "twisted_projector_retention_for_visible_sectors": True,
            "visible_SM_bundle_or_sheaf_operator_source": True,
            "repo_level_selected_D_E_dotD_Riesz_Green": True,
            "selected_C1_primitive_contractions": True,
            "Yukawa_magnitudes_and_CKM_angles": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_full_geometric_Deligne_Cech_representative": False,
            "claims_full_heterotic_Green_Schwarz_embedding": False,
            "claims_Freed_Witten_verified": False,
            "claims_twisted_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_selected_visible_operator_source": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected q79/F, m=1 finite gerbe is now an explicit period table "
                "on F_3^2 with zero discrete Bianchi coboundary and the qutrit "
                "Heisenberg commutator. This closes the finite quotient source "
                "table, but not the full geometric operator-source packet."
            )
            if finite_table_closed
            else "The finite m=1 period table did not close.",
            "next_closing_object": (
                "Embed this finite period table into the selected geometric "
                "Deligne/Cech or B-field representative, verify Freed-Witten and "
                "projector retention, then derive selected D_E/dotD/Riesz/Green "
                "operator files from that source."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedM1GerbePeriodTable",
        "status": report["status"],
        "analysis_script": "scripts/construct_time_oriented_m1_gerbe_period_table.py",
        "candidate_data": "candidate_data/time_oriented_m1_gerbe_period_table.candidate.json",
        "selected_branch": report["selected_branch"],
        "input_closure": report["input_closure"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
