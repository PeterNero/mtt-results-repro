"""Build CONST-EW-02 B35 RA-1 derivation attack or RB-2 primitive terms fill."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b35_ra1_derivation_or_rb2_primitive_terms"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RA1 = BASE / "route_a_ra1_derivation_attack_import.packet.json"
RB2 = BASE / "route_b_rb2_primitive_terms_fill_import.packet.json"
ALIGNMENT = BASE / "superset_external_alignment_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b35_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B35_RA1_Derivation_or_RB2_PrimitiveTerms_v1.md"

STATUS = "MTT_CONST_EW_02_B35_RA1_DERIVATION_OR_RB2_PRIMITIVE_TERMS_BUILT"


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

    b34_path = DATA / "const_ew_02_weak_mixing_b34_ra1_or_rb1_input_basis.candidate.json"
    b34_boundary_path = DATA / "const_ew_02_weak_mixing_b34_ra1_or_rb1_input_basis" / "weak_mixing_b34_boundary.packet.json"

    sibling_candidate_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill.candidate.json"
    sibling_ra1_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill" / "route_a_ra1_derivation_attack_with_external_variational_support.packet.json"
    sibling_rb2_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill" / "route_b_rb2_primitive_contraction_terms_fill.packet.json"
    sibling_alignment_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill" / "psm_c1_02_superset_strategy_external_alignment.packet.json"
    sibling_next_path = SM / "candidate_data" / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill" / "next_labeled_workorder.packet.json"

    b34 = load(b34_path)
    b34_boundary = load(b34_boundary_path)
    sibling = load(sibling_candidate_path)
    ra1_src = load(sibling_ra1_path)
    rb2_src = load(sibling_rb2_path)
    alignment_src = load(sibling_alignment_path)
    sibling_next = load(sibling_next_path)

    ra1 = {
        "schema": "MTTConstEW02B35RouteARA1DerivationAttackImport.v1",
        "status": "RA1_REFINED_TO_PHYSICAL_ACTION_EQUALITY_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B35-ROUTEA-RA1-DERIVATION-ATTACK",
        "inputs": {
            "sibling_candidate": rel(sibling_candidate_path),
            "route_a_ra1_derivation_attack": rel(sibling_ra1_path),
        },
        "clause_id": ra1_src["clause_id"],
        "refined_RA1_target": ra1_src["refined_RA1_target"],
        "internal_support": ra1_src["internal_support"],
        "external_alignment": ra1_src["external_alignment"],
        "external_used_as_source_proof": any(item["used_as_source_proof"] for item in ra1_src["external_alignment"]),
        "closed_now": ra1_src["closed_now"],
        "why_still_open": ra1_src["why_still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rb2 = {
        "schema": "MTTConstEW02B35RouteBRB2PrimitiveTermsFillImport.v1",
        "status": "RB2_PRIMITIVE_TERMS_INPUT_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B35-ROUTEB-RB2-PRIMITIVE-TERMS-FILL",
        "inputs": {
            "sibling_candidate": rel(sibling_candidate_path),
            "route_b_rb2_fill": rel(sibling_rb2_path),
        },
        "input_id": rb2_src["input_id"],
        "input_file_exists_now": rb2_src["input_file_exists_now"],
        "filled_input_path": rb2_src["filled_input_path"],
        "primitive_row_count": rb2_src["primitive_row_count"],
        "selected_emitted": rb2_src["selected_emitted"],
        "theorem_derived": rb2_src["theorem_derived"],
        "source_owner_verified": rb2_src["source_owner_verified"],
        "remaining_route_b_input_count_after_rb2": rb2_src["remaining_route_b_input_count_after_rb2"],
        "remaining_route_b_inputs_after_rb2": rb2_src["remaining_route_b_inputs_after_rb2"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    alignment = {
        "schema": "MTTConstEW02B35SupersetExternalAlignmentImport.v1",
        "status": "SUPERSET_PATHS_ALIGNED_NO_EXTERNAL_SOURCE_PROOF_IMPORTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B35-SUPERSET-ALIGNMENT",
        "inputs": {"superset_strategy_external_alignment": rel(sibling_alignment_path)},
        "combined_paths": alignment_src["combined_paths"],
        "external_references": alignment_src["external_references"],
        "locked_target": alignment_src["locked_target"],
        "paths_used_as_knobs": alignment_src["paths_used_as_knobs"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B35Boundary.v1",
        "status": "B35_RB2_INPUT_FILLED_RA1_PHYSICAL_EQUALITY_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B35-BOUNDARY",
        "previous_B34": {
            "candidate": b34["candidate"],
            "status": b34["status"],
            "still_open": b34_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "ROUTE_A_RA1_external_variational_alignment_recorded": sibling["what_closes_now"]["ROUTE_A_RA1_external_variational_alignment_recorded"],
            "ROUTE_A_RA1_refined_to_physical_action_equality": sibling["what_closes_now"]["ROUTE_A_RA1_refined_to_physical_action_equality"],
            "ROUTE_B_RB2_primitive_terms_input_file_filled": sibling["what_closes_now"]["ROUTE_B_RB2_primitive_terms_input_file_filled"],
            "all_72_primitive_support_rows_materialized": sibling["what_closes_now"]["all_72_primitive_support_rows_materialized"],
            "superset_strategy_locked_no_external_source_import": sibling["what_closes_now"]["superset_strategy_locked_no_external_source_import"],
        },
        "still_open": {
            "ROUTE_A_RA1_unpatched_physical_action_equality": True,
            "ROUTE_B_RB2_independent_quadrature_exactness": True,
            "ROUTE_B_RB2_selected_source_promotion": True,
            "ROUTE_B_RB3_hessian_source_vector": True,
            "ROUTE_B_RB4_sector_response_matrices": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B34": {
            "B34": "filled RB-1 input and sharpened RA-1",
            "B35": "fills RB-2 support rows and refines RA-1 to physical action equality",
            "not_repeated": [
                "not another RB-1 basis fill",
                "not using external literature as MTT source proof",
                "not a numerical weak-angle fit",
            ],
        },
        "allowed_claim": "B35 fills RB-2 as 72 primitive support rows and sharpens RA-1 to the physical action equality target.",
        "forbidden_claim": "RA-1 proof, RB-2 selected source promotion, full Route-B export, physical weak-angle closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B35NextWork.v1",
        "status": "NEXT_WORKORDER_RA1_PHYSICAL_ACTION_EQUALITY_OR_RB3_HESSIAN_SOURCE_FILL",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B36-RA1-EQUALITY-OR-RB3-HESSIAN",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B36-ROUTEA-RA1-PHYSICAL-ACTION-EQUALITY",
            "task": sibling_next["primary"]["task"],
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B36-ROUTEB-RB3-HESSIAN-SOURCE-FILL",
            "task": sibling_next["secondary"]["task"],
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB35RA1DerivationOrRB2PrimitiveTerms",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B35-RA1-DERIVATION-OR-RB2-PRIMITIVE-TERMS",
        "output_packets": {
            "route_a_ra1_derivation_attack_import": rel(RA1),
            "route_b_rb2_primitive_terms_fill_import": rel(RB2),
            "superset_external_alignment_import": rel(ALIGNMENT),
            "weak_mixing_b35_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B35RA1DerivationOrRB2PrimitiveTermsTheorem",
            "proved": True,
            "statement": (
                "For the weak-mixing C1 source-promotion packet, Route A RA-1 is refined to the unpatched physical equality S_C1' = C1DefectLeakageFunctional on selected admissible variations, with external Galerkin/Ritz literature used only as methodological alignment. In parallel, Route B RB-2 is filled with all 72 primitive contraction support rows, while selected Galerkin source promotion remains open because the rows are not independent quadrature/source emissions."
            ),
        },
        "RA1_physical_action_equality_proved_now": False,
        "RB2_primitive_terms_input_filled_now": True,
        "RB2_primitive_row_count": rb2_src["primitive_row_count"],
        "RB2_selected_source_promoted_now": False,
        "external_sources_used_as_MTT_source_proof": False,
        "remaining_route_b_input_count_after_rb2": rb2_src["remaining_route_b_input_count_after_rb2"],
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B35_RA1_Derivation_or_RB2_PrimitiveTerms_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "RA1_physical_action_equality_proved_now": False,
        "RB2_primitive_terms_input_filled_now": True,
        "RB2_primitive_row_count": rb2_src["primitive_row_count"],
        "RB2_selected_source_promoted_now": False,
        "external_sources_used_as_MTT_source_proof": False,
        "remaining_route_b_input_count_after_rb2": rb2_src["remaining_route_b_input_count_after_rb2"],
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B35 RA1 Derivation or RB2 Primitive Terms v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B35-RA1-DERIVATION-OR-RB2-PRIMITIVE-TERMS`

## Result

```text
RA-1 physical action equality proved           False
RB-2 primitive terms input filled              True
RB-2 primitive support rows                    {rb2_src["primitive_row_count"]}
RB-2 selected source promotion                 False
remaining Route-B inputs after RB-2            {rb2_src["remaining_route_b_input_count_after_rb2"]}
```

RA-1 is now:

```text
S_C1' = C1DefectLeakageFunctional on selected admissible variations
```

External Galerkin/Ritz references are used only for methodological alignment,
not as MTT source proof.

## Next

`CONST-EW-02 / WEAK-MIXING / B36-RA1-EQUALITY-OR-RB3-HESSIAN`
"""

    for path, payload in [
        (RA1, ra1),
        (RB2, rb2),
        (ALIGNMENT, alignment),
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
