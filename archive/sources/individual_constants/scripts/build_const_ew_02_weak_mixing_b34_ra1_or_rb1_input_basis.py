"""Build CONST-EW-02 B34 Route-A RA-1 or Route-B RB-1 input-basis artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b34_ra1_or_rb1_input_basis"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RA1 = BASE / "route_a_ra1_physical_c1_variation_import.packet.json"
RB1 = BASE / "route_b_rb1_zero_mode_basis_input_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b34_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B34_RA1_or_RB1_InputBasis_v1.md"

STATUS = "MTT_CONST_EW_02_B34_RA1_OR_RB1_INPUT_BASIS_BUILT"


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

    b33_path = DATA / "const_ew_02_weak_mixing_b33_selected_source_promotion_packet.candidate.json"
    b33_boundary_path = DATA / "const_ew_02_weak_mixing_b33_selected_source_promotion_packet" / "weak_mixing_b33_boundary.packet.json"

    sibling_candidate_path = SM / "candidate_data" / "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill.candidate.json"
    sibling_ra1_path = SM / "candidate_data" / "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill" / "route_a_ra1_physical_c1_variation_principle_attempt.packet.json"
    sibling_rb1_path = SM / "candidate_data" / "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill" / "route_b_rb1_zero_mode_basis_input_fill.packet.json"
    sibling_decision_path = SM / "candidate_data" / "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill" / "psm_c1_02_ra1_rb1_decision.packet.json"
    sibling_next_path = SM / "candidate_data" / "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill" / "next_labeled_workorder.packet.json"
    hym_basis_path = SM / "candidate_data" / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"

    b33 = load(b33_path)
    b33_boundary = load(b33_boundary_path)
    sibling = load(sibling_candidate_path)
    ra1_src = load(sibling_ra1_path)
    rb1_src = load(sibling_rb1_path)
    decision_src = load(sibling_decision_path)
    sibling_next = load(sibling_next_path)
    hym_basis = load(hym_basis_path)

    ra1 = {
        "schema": "MTTConstEW02B34RouteARA1Import.v1",
        "status": "RA1_SUPPORT_IDENTIFIED_UNPATCHED_DERIVATION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-RA1-PHYSICAL-C1-VARIATION",
        "inputs": {
            "sibling_candidate": rel(sibling_candidate_path),
            "route_a_ra1_attempt": rel(sibling_ra1_path),
        },
        "clause_id": ra1_src["clause_id"],
        "minimal_statement": ra1_src["minimal_statement"],
        "support_available": ra1_src["support_available"],
        "closed_now": ra1_src["closed_now"],
        "conditional_witness_value": ra1_src["conditional_witness_value"],
        "why_not_proved": ra1_src["why_not_proved"],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rb1 = {
        "schema": "MTTConstEW02B34RouteBRB1Import.v1",
        "status": "RB1_ZERO_MODE_BASIS_INPUT_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B34-ROUTEB-SELECTED-ZERO-MODE-BASIS",
        "inputs": {
            "sibling_candidate": rel(sibling_candidate_path),
            "route_b_rb1_fill": rel(sibling_rb1_path),
            "hym_basis_bridge": rel(hym_basis_path),
        },
        "input_id": rb1_src["input_id"],
        "input_file_exists_now": rb1_src["input_file_exists_now"],
        "basis_dimension": rb1_src["basis_dimension"],
        "filled_input_path": rb1_src["filled_input_path"],
        "selected_emitted": rb1_src["selected_emitted"],
        "theorem_derived": rb1_src["theorem_derived"],
        "source_owner_verified": rb1_src["source_owner_verified"],
        "remaining_route_b_input_count_after_rb1": rb1_src["remaining_route_b_input_count_after_rb1"],
        "remaining_route_b_inputs": rb1_src["remaining_route_b_inputs"],
        "hym_projector_bridge": {
            "bridge_theorem_proved": hym_basis["theorem"]["bridge_theorem_proved"],
            "selected_values_emitted": hym_basis["theorem"]["selected_values_emitted"],
            "promotion_reason_not_now": hym_basis["promotion_decision"]["reason_not_promoted_now"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B34Boundary.v1",
        "status": "B34_RB1_INPUT_FILLED_RA1_AND_SOURCE_PROMOTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B34-BOUNDARY",
        "previous_B33": {
            "candidate": b33["candidate"],
            "status": b33["status"],
            "still_open": b33_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "ROUTE_A_RA1_support_matrix_recorded": sibling["what_closes_now"]["ROUTE_A_RA1_support_matrix_recorded"],
            "ROUTE_B_RB1_zero_mode_basis_input_file_filled": sibling["what_closes_now"]["ROUTE_B_RB1_zero_mode_basis_input_file_filled"],
            "RB1_selected_source_promotion_guarded_open": sibling["what_closes_now"]["RB1_selected_source_promotion_guarded_open"],
            "superset_strategy_locked_to_same_target": sibling["what_closes_now"]["superset_strategy_locked_to_same_target"],
        },
        "still_open": {
            "ROUTE_A_RA1_unpatched_physical_C1_variation_derivation": True,
            "ROUTE_B_RB1_selected_HYM_projector_basis_value_emission": True,
            "ROUTE_B_RB2_primitive_contraction_terms": True,
            "ROUTE_B_RB3_hessian_source_vector": True,
            "ROUTE_B_RB4_sector_response_matrices": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "superset_strategy": decision_src["superset_strategy"],
        "anti_cycle_delta_from_B33": {
            "B33": "constructed the nine-field source packet and named Route-A/Route-B exits",
            "B34": "fills the first Route-B input at support level and records RA-1 as the active unpatched action-derivation gap",
            "not_repeated": [
                "not another source-promotion packet rebuild",
                "not a patched/local-axiom closure claim",
                "not a numerical weak-angle fit",
            ],
        },
        "allowed_claim": "B34 fills RB-1 as a support-level zero-mode basis input and sharpens RA-1 to the unpatched physical C1 variation derivation.",
        "forbidden_claim": "RA-1 proof, RB-1 source promotion, full Route-B export, physical weak-angle closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B34NextWork.v1",
        "status": "NEXT_WORKORDER_RA1_DERIVATION_ATTACK_OR_RB2_PRIMITIVE_TERMS_FILL",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B35-RA1-DERIVATION-OR-RB2-PRIMITIVE-TERMS",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B35-ROUTEA-RA1-DERIVATION-ATTACK",
            "task": sibling_next["primary"]["task"],
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B35-ROUTEB-RB2-PRIMITIVE-TERMS-FILL",
            "task": sibling_next["secondary"]["task"],
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB34RA1OrRB1InputBasis",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-CLAUSE1-OR-ROUTEB-INPUT-BASIS",
        "output_packets": {
            "route_a_ra1_physical_c1_variation_import": rel(RA1),
            "route_b_rb1_zero_mode_basis_input_import": rel(RB1),
            "weak_mixing_b34_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B34RA1OrRB1InputBasisTheorem",
            "proved": True,
            "statement": (
                "For the weak-mixing C1 source-promotion packet, Route A RA-1 remains open because current support does not derive the physical C1 variation principle from unpatched MTT/Theta/Strominger action. In parallel, Route B RB-1 is filled as a support-level zero-mode basis input for honest Galerkin execution, but selected source promotion remains open until same-branch HYM projector basis values are emitted."
            ),
        },
        "RA1_closed_now": False,
        "RB1_input_filled_now": True,
        "RB1_selected_source_promoted_now": False,
        "remaining_route_b_input_count_after_rb1": rb1_src["remaining_route_b_input_count_after_rb1"],
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B34_RA1_or_RB1_InputBasis_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "RA1_closed_now": False,
        "RB1_input_filled_now": True,
        "RB1_selected_source_promoted_now": False,
        "remaining_route_b_input_count_after_rb1": rb1_src["remaining_route_b_input_count_after_rb1"],
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B34 RA1 or RB1 Input Basis v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B34-ROUTEA-CLAUSE1-OR-ROUTEB-INPUT-BASIS`

## Result

```text
RA-1 physical C1 variation principle closed       False
RB-1 zero-mode basis input file filled            True
RB-1 selected source promotion                    False
remaining Route-B inputs after RB-1               {rb1_src["remaining_route_b_input_count_after_rb1"]}
```

RA-1 is now the unpatched physical action equality problem:

```text
{ra1_src["minimal_statement"]}
```

RB-1 is useful support, but the selected HYM projector basis value emission is
still open, so this is not full source promotion.

## Next

`CONST-EW-02 / WEAK-MIXING / B35-RA1-DERIVATION-OR-RB2-PRIMITIVE-TERMS`
"""

    for path, payload in [
        (RA1, ra1),
        (RB1, rb1),
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
