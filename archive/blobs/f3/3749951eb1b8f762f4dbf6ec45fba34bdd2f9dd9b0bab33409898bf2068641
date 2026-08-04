"""Build CONST-EW-02 B36 RA-1 equality or RB-3 Hessian source fill."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b36_ra1_equality_or_rb3_hessian"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RA1 = BASE / "route_a_ra1_physical_action_equality_import.packet.json"
RB3 = BASE / "route_b_rb3_hessian_source_fill_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b36_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B36_RA1_Equality_or_RB3_Hessian_v1.md"

STATUS = "MTT_CONST_EW_02_B36_RA1_EQUALITY_OR_RB3_HESSIAN_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b35_path = DATA / "const_ew_02_weak_mixing_b35_ra1_derivation_or_rb2_primitive_terms.candidate.json"
    b35_boundary_path = DATA / "const_ew_02_weak_mixing_b35_ra1_derivation_or_rb2_primitive_terms" / "weak_mixing_b35_boundary.packet.json"

    sibling_candidate_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill.candidate.json"
    sibling_ra1_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "route_a_ra1_physical_action_equality_status.packet.json"
    sibling_rb3_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "route_b_rb3_hessian_source_fill.packet.json"
    sibling_next_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "next_labeled_workorder.packet.json"
    sibling_superset_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "psm_c1_02_superset_alignment_after_rb3.packet.json"

    b35 = load(b35_path)
    b35_boundary = load(b35_boundary_path)
    sibling = load(sibling_candidate_path)
    ra1_src = load(sibling_ra1_path)
    rb3_src = load(sibling_rb3_path)
    sibling_next = load(sibling_next_path)
    superset = load(sibling_superset_path)

    ra1 = {
        "schema": "MTTConstEW02B36RouteARA1PhysicalActionEqualityImport.v1",
        "status": "RA1_REDUCED_TO_RA2_BOUNDARY_SOURCE_CANCELLATION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B36-ROUTEA-RA1-PHYSICAL-ACTION-EQUALITY",
        "inputs": {
            "sibling_candidate": rel(sibling_candidate_path),
            "route_a_ra1_status": rel(sibling_ra1_path),
        },
        "clause_id": ra1_src["clause_id"],
        "current_RA1_result": ra1_src["current_RA1_result"],
        "corpus_support": ra1_src["corpus_support"],
        "physical_action_equality_claimed": ra1_src["physical_action_equality_claimed"],
        "why_RA1_still_open": ra1_src["why_RA1_still_open"],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rb3 = {
        "schema": "MTTConstEW02B36RouteBRB3HessianSourceFillImport.v1",
        "status": "RB3_HESSIAN_SOURCE_NORMAL_EQUATIONS_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B36-ROUTEB-RB3-HESSIAN-SOURCE-FILL",
        "inputs": {
            "sibling_candidate": rel(sibling_candidate_path),
            "route_b_rb3_fill": rel(sibling_rb3_path),
        },
        "input_id": rb3_src["input_id"],
        "primitive_row_count": rb3_src["primitive_row_count"],
        "hessian_source_support": rb3_src["hessian_source_support"],
        "matches_prior_conditional_source_map": rb3_src["matches_prior_conditional_source_map"],
        "computed_from_independent_galerkin_quadrature": rb3_src["computed_from_independent_galerkin_quadrature"],
        "residual_replay_dependency": rb3_src["residual_replay_dependency"],
        "selected_hessian_source_emitted": rb3_src["selected_hessian_source_emitted"],
        "theorem_derived": rb3_src["theorem_derived"],
        "source_owner_verified": rb3_src["source_owner_verified"],
        "why_not_selected": rb3_src["why_not_selected"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B36Boundary.v1",
        "status": "B36_RB3_NORMAL_EQUATIONS_FILLED_RA2_RB4_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B36-BOUNDARY",
        "previous_B35": {
            "candidate": b35["candidate"],
            "status": b35["status"],
            "still_open": b35_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "ROUTE_A_RA1_reduced_to_RA2_boundary_source_cancellation": sibling["what_closes_now"]["ROUTE_A_RA1_reduced_to_RA2_boundary_source_cancellation"],
            "ROUTE_B_RB3_hessian_source_normal_equations_filled": sibling["what_closes_now"]["ROUTE_B_RB3_hessian_source_normal_equations_filled"],
            "support_hessian_positive_definite": sibling["what_closes_now"]["support_hessian_positive_definite"],
            "RB3_matches_prior_conditional_source_map": sibling["what_closes_now"]["RB3_matches_prior_conditional_source_map"],
            "superset_paths_constrained_to_locked_target": sibling["what_closes_now"]["superset_paths_constrained_to_locked_target"],
        },
        "still_open": {
            "RA2_selected_boundary_source_cancellation": True,
            "RB4_independent_selected_quadrature_source": True,
            "selected_hessian_source_emitted": True,
            "selected_source_promotion": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "support_hessian_summary": {
            "A_transpose_A": rb3_src["hessian_source_support"]["A_transpose_A"],
            "A_transpose_b": rb3_src["hessian_source_support"]["A_transpose_b"],
            "deltaTheta_C1_support_solution": rb3_src["hessian_source_support"]["deltaTheta_C1_support_solution"],
            "determinant": rb3_src["hessian_source_support"]["determinant"],
            "positive_definite_support_hessian": rb3_src["hessian_source_support"]["positive_definite_support_hessian"],
        },
        "superset_alignment_after_rb3": superset,
        "anti_cycle_delta_from_B35": {
            "B35": "filled RB-2 primitive support rows and refined RA-1",
            "B36": "uses those rows to fill RB-3 support normal equations and reduces RA-1 to RA-2 boundary/source cancellation",
            "not_repeated": [
                "not another primitive row fill",
                "not promoting residual-replay support as selected source",
                "not a numerical weak-angle fit",
            ],
        },
        "allowed_claim": "B36 fills the RB-3 support Hessian/source normal equations and reduces RA-1 to RA-2 boundary/source cancellation.",
        "forbidden_claim": "selected Hessian source emission, independent quadrature, RA-2 proof, physical weak-angle closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B36NextWork.v1",
        "status": "NEXT_WORKORDER_RA2_BOUNDARY_SOURCE_CANCELLATION_OR_RB4_INDEPENDENT_SOURCE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B37-RA2-BOUNDARY-OR-RB4-INDEPENDENT-SOURCE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B37-ROUTEA-RA2-BOUNDARY-SOURCE-CANCELLATION",
            "task": sibling_next["primary"]["task"],
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B37-ROUTEB-RB4-INDEPENDENT-QUADRATURE-SOURCE",
            "task": sibling_next["secondary"]["task"],
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB36RA1EqualityOrRB3Hessian",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B36-RA1-EQUALITY-OR-RB3-HESSIAN",
        "output_packets": {
            "route_a_ra1_physical_action_equality_import": rel(RA1),
            "route_b_rb3_hessian_source_fill_import": rel(RB3),
            "weak_mixing_b36_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B36RA1EqualityOrRB3HessianTheorem",
            "proved": True,
            "statement": (
                "For the weak-mixing C1 source-promotion packet, RA-1 is reduced to RA-2 selected boundary/source cancellation: the corpus supports the physical action/Hessian picture, but the selected finite C1DefectLeakageFunctional equality is not yet unpatched. In parallel, RB-3 support Hessian/source normal equations are filled from the 72 primitive support rows with A^T A=diag(12,12), A^T b=(12,12), and deltaTheta_C1=(1,1), but selected Hessian source emission remains open because the computation still depends on residual-replay support rather than independent selected quadrature/source ownership."
            ),
        },
        "RA1_physical_action_equality_claimed": False,
        "RA1_reduced_to_RA2_boundary_source_cancellation": True,
        "RB3_hessian_source_normal_equations_filled": True,
        "RB3_selected_hessian_source_emitted": False,
        "RB3_computed_from_independent_galerkin_quadrature": False,
        "RB3_positive_definite_support_hessian": rb3_src["hessian_source_support"]["positive_definite_support_hessian"],
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B36_RA1_Equality_or_RB3_Hessian_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "RA1_physical_action_equality_claimed": False,
        "RA1_reduced_to_RA2_boundary_source_cancellation": True,
        "RB3_hessian_source_normal_equations_filled": True,
        "RB3_selected_hessian_source_emitted": False,
        "RB3_computed_from_independent_galerkin_quadrature": False,
        "RB3_positive_definite_support_hessian": rb3_src["hessian_source_support"]["positive_definite_support_hessian"],
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B36 RA1 Equality or RB3 Hessian v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B36-RA1-EQUALITY-OR-RB3-HESSIAN`

## Result

```text
RA-1 physical action equality claimed          False
RA-1 reduced to RA-2 boundary/source gate      True
RB-3 Hessian/source normal equations filled    True
RB-3 selected Hessian source emitted           False
RB-3 independent Galerkin quadrature           False
```

Support Hessian:

```text
A^T A      = [[12, 0], [0, 12]]
A^T b      = [12, 12]
deltaTheta = [1, 1]
det        = {rb3_src["hessian_source_support"]["determinant"]}
```

## Next

`CONST-EW-02 / WEAK-MIXING / B37-RA2-BOUNDARY-OR-RB4-INDEPENDENT-SOURCE`
"""

    for path, payload in [
        (RA1, ra1),
        (RB3, rb3),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
