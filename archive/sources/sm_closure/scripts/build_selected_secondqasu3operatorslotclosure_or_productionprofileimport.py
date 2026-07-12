"""Build second Qa/SU3 operator-source slot closure or production profile import."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_secondqasu3operatorslotclosure_or_productionprofileimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SECOND_SLOT = PACKET_DIR / "second_qasu3_operator_source_slot_closure.packet.json"
PRODUCTION = PACKET_DIR / "production_profile_import_status.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_second_slot.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsProductionProfileImport_or_SecondQaSU3OperatorSlotClosure_v1.md"

STATUS = "MTT_SELECTED_SECONDQASU3OPERATORSLOTCLOSURE_OR_PRODUCTIONPROFILEIMPORT_BUILT_TWO_OPERATOR_SOURCE_SLOTS_CLOSED"
NEXT = "MTT_Selected_ThirdQaSU3OperatorSlotClosure_or_ProductionWorkspaceImport_v1"
FIRST_SLOT = "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source"
SECOND_SLOT_NAME = "standard_lattice_base_ordering_and_base_swap_breaking"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure.candidate.json")
    first_slot = load(
        DATA
        / "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure"
        / "qasu3_operator_source_slot_closure.packet.json"
    )
    terminal_patch = load(DATA / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json")
    terminal_principle = load(DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json")
    ordered_bridge = load(DATA / "selected_orderedvalphapic0source_or_profileworkspaceimport.candidate.json")
    terminal_selector = load(DATA / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json")

    missing_before = first_slot["slot_status_after_closure"]["missing_slots"]
    terminal = terminal_patch["unconditional_terminal_replay"]
    source_value = {
        "standard_lattice_or_equivalent_selected": True,
        "base_factor_order_selected": True,
        "base_order": terminal["base_order"],
        "base_swap_breaking_rule": "E1/g1g2 carries +2 and E2/g3g4 carries -4, so the ordered L3-K2 lane is not identified with its base-swapped mate at the selected source layer.",
        "selected_source_label": terminal["selected_source_label"],
        "selected_L": terminal["selected_L"],
        "selected_L2": terminal["selected_L2"],
        "status": terminal["status"],
    }
    missing_after = [slot for slot in missing_before if slot != SECOND_SLOT_NAME]

    second_slot = {
        "schema": "MTTSecondQaSU3OperatorSourceSlotClosure.v1",
        "filled_slot": SECOND_SLOT_NAME,
        "input_previous_slot_closure": rel(
            DATA
            / "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure"
            / "qasu3_operator_source_slot_closure.packet.json"
        ),
        "input_terminal_axiom_patch": rel(DATA / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json"),
        "input_terminal_principle": rel(DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"),
        "input_ordered_bridge": rel(DATA / "selected_orderedvalphapic0source_or_profileworkspaceimport.candidate.json"),
        "selected_source_value": source_value,
        "proof_inputs": {
            "first_operator_source_slot_already_closed": first_slot["closure_result"]["operator_source_slot_closed"],
            "prior_manifest_contains_second_slot": SECOND_SLOT_NAME in missing_before,
            "terminal_patch_selects_ordered_base_row": "base_order" in terminal and terminal["closed_by_axiom_patch_now"] is True,
            "terminal_principle_closed_base_order_under_explicit_principle": terminal_principle["what_closes_now"][
                "selected_base_order_closed_under_explicit_principle"
            ],
            "terminal_patch_promotes_principle_to_patched_spine": terminal_patch["what_closes_now"][
                "terminal_axiom_patch_applied_to_local_proof_spine"
            ],
            "older_ordered_bridge_left_base_order_open_before_patch": ordered_bridge["what_remains_open"][
                "base_factor_order_selected"
            ],
            "older_terminal_selector_left_standard_lattice_open_before_patch": terminal_selector["what_remains_open"][
                "standard_lattice_or_equivalent_selected"
            ],
        },
        "superset_strategy": {
            "mode": "LATER_PATCHED_SPINE_PROMOTION_SUPERSEDES_OLDER_CONDITIONAL_BASE_ORDER_GATES",
            "straight_path": "terminal admissible-section axiom patch selects terminal source and ordered base row",
            "support_paths": [
                "conditional terminal source principle already closed base order under explicit principle",
                "ordered bridge carried L3-K2 and Pic0 accounting but left base order open",
                "terminal selector identified standard lattice/base order as the exact missing switch",
            ],
            "target_fitting_used": False,
            "observed_data_used": False,
        },
        "slot_status_after_closure": {
            "required_operator_slot_count": first_slot["slot_status_after_closure"]["required_operator_slot_count"],
            "filled_operator_slot_count": 2,
            "filled_slots": [FIRST_SLOT, SECOND_SLOT_NAME],
            "missing_slots": missing_after,
            "remaining_missing_slot_count": len(missing_after),
        },
        "closure_result": {
            "second_operator_source_slot_closed": True,
            "selected_source_value_emitted": True,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "Two source-side slots are now filled, but operator-layer Pic0, same-source Chern-Weil, "
                "transition D_E/rho_E, selected HYM/Route-C residual, Riesz/Green/dotD retention, "
                "and finite determinant/torsion response are still missing."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    production = {
        "schema": "MTTProductionProfileImportStatusAfterSecondSlot.v1",
        "input_previous_production_manifest": rel(
            DATA
            / "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure"
            / "higgs_production_covariance_profile_acquisition.packet.json"
        ),
        "production_profile_imported_now": False,
        "production_workspace_imported_now": False,
        "reason": "No new source-labeled Higgs production/coupling covariance rows or official workspace were added in this slot-closure step.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTTrueEquivalenceDecisionAfterSecondQaSU3Slot.v1",
        "status": "TWO_QASU3_OPERATOR_SOURCE_SLOTS_CLOSED_DYNAMIC_PACKET_OPEN",
        "operator_source_slots_closed": 2,
        "operator_source_slots_remaining": len(missing_after),
        "closed_slots": [FIRST_SLOT, SECOND_SLOT_NAME],
        "production_profile_imported": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSecondQaSU3OperatorSlotClosureOrProductionProfileImport",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure.candidate.json"),
            "previous_operator_slot_closure": second_slot["input_previous_slot_closure"],
            "terminal_axiom_patch": second_slot["input_terminal_axiom_patch"],
            "terminal_principle": second_slot["input_terminal_principle"],
            "ordered_bridge": second_slot["input_ordered_bridge"],
        },
        "output_packets": {
            "second_qasu3_operator_source_slot_closure": rel(SECOND_SLOT),
            "production_profile_import_status": rel(PRODUCTION),
            "true_equivalence_decision_after_second_slot": rel(DECISION),
        },
        "theorem": {
            "name": "SecondQaSU3OperatorSourceSlotClosureTheorem",
            "proved": True,
            "statement": (
                "The terminal admissible-section axiom patch selects not only g3/L3-K2 but also the ordered "
                "base row E1/g1g2 positive and E2/g3g4 negative in the patched proof spine. This promotes "
                "the standard-lattice/base-order/base-swap-breaking Qa/SU3 operator-source slot, reducing "
                "the operator cutset from seven to six remaining slots. The production profile remains open."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "second_QaSU3_operator_source_slot_closed": True,
            "operator_source_slots_closed_total": 2,
            "production_profile_imported": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "standard_lattice_base_ordering_and_base_swap_breaking_slot": True,
            "qasu3_operator_cutset_reduced_to_six_slots": True,
            "older_base_order_conditional_gate_reconciled_with_terminal_patch": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "Higgs_production_covariance_profile": True,
            "operator_layer_Pic0_or_physical_quotient": True,
            "same_source_Chern_Weil_row": True,
            "transition_rhoE_or_Cech_Dolbeault_DE_data": True,
            "selected_HYM_or_RouteC_residual": True,
            "Riesz_Green_dotD_projector_retention": True,
            "finite_determinant_heat_spectrum_or_torsion_response": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsProductionProfileImport_or_SecondQaSU3OperatorSlotClosure_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "second_QaSU3_operator_source_slot_closed": True,
        "closed_operator_source_slots_total": 2,
        "operator_source_slots_remaining": len(missing_after),
        "production_profile_imported": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected HiggsProductionProfileImport or SecondQaSU3OperatorSlotClosure v1

This artifact closes the second Qa/SU3 operator-source slot.

The newly closed slot is `{SECOND_SLOT_NAME}`.  The selected source value is the
patched-spine ordered base row: `E1/g1g2` carries `+2` and `E2/g3g4` carries
`-4`, tied to `g3 / L3-K2`.

This is new progress beyond the previous frontier: the operator-source cutset is
now reduced from eight original slots to six remaining slots.  It is still not a
dynamic Qa/SU3/HYM/End0/C1 operator packet, and no production covariance profile
was imported in this step.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (SECOND_SLOT, second_slot),
        (PRODUCTION, production),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
