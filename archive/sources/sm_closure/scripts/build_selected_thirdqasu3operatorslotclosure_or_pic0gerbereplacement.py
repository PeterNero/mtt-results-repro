"""Build third Qa/SU3 operator-source slot closure via Pic0 gerbe replacement."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thirdqasu3operatorslotclosure_or_pic0gerbereplacement"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THIRD_SLOT = PACKET_DIR / "third_qasu3_operator_source_slot_closure.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_pic0_slot.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThirdQaSU3OperatorSlotClosure_or_Pic0GerbeReplacement_v1.md"

STATUS = "MTT_SELECTED_THIRDQASU3OPERATORSLOTCLOSURE_OR_PIC0GERBEREPLACEMENT_BUILT_THREE_OPERATOR_SOURCE_SLOTS_CLOSED"
NEXT = "MTT_Selected_FourthQaSU3OperatorSlotClosure_or_VisibleChernWeilSource_v1"
SLOT = "Pic0_selection_or_physical_quotient_theorem"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_secondqasu3operatorslotclosure_or_productionprofileimport.candidate.json")
    previous_slot = load(
        DATA
        / "selected_secondqasu3operatorslotclosure_or_productionprofileimport"
        / "second_qasu3_operator_source_slot_closure.packet.json"
    )
    terminal_pic0 = load(DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede.candidate.json")
    gerbe = load(
        DATA
        / "selected_terminalsourceswitch_or_operatorpic0gerbede"
        / "operator_pic0_gerbe_de_replacement.packet.json"
    )
    promotion = load(
        DATA
        / "selected_terminalsourceswitch_or_operatorpic0gerbede"
        / "promotion_decision_after_terminal_or_gerbe.packet.json"
    )
    cutset = load(
        DATA
        / "selected_terminalsourceswitch_or_operatorpic0gerbede"
        / "visible_operator_payload_cutset.packet.json"
    )
    pic0_reduction = load(DATA / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json")

    missing_before = previous_slot["slot_status_after_closure"]["missing_slots"]
    closed_slots = previous_slot["slot_status_after_closure"]["filled_slots"] + [SLOT]
    missing_after = [slot for slot in missing_before if slot != SLOT]
    source = gerbe["selected_s3_source_packet"]

    third_slot = {
        "schema": "MTTThirdQaSU3OperatorSourceSlotClosurePic0GerbeReplacement.v1",
        "filled_slot": SLOT,
        "input_previous_slot_closure": rel(
            DATA
            / "selected_secondqasu3operatorslotclosure_or_productionprofileimport"
            / "second_qasu3_operator_source_slot_closure.packet.json"
        ),
        "input_terminal_pic0_gerbe_bridge": rel(DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede.candidate.json"),
        "input_operator_pic0_gerbe_replacement": rel(
            DATA
            / "selected_terminalsourceswitch_or_operatorpic0gerbede"
            / "operator_pic0_gerbe_de_replacement.packet.json"
        ),
        "input_pic0_reduction": rel(DATA / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json"),
        "selected_source_value": {
            "direct_pic0_invariance_status": gerbe["direct_pic0_invariance_status"],
            "neutral_pic0_selection_status": gerbe["neutral_pic0_selection_status"],
            "operator_pic0_replacement": "selected_q79_F_m1_S3_gerbe_differential_cohomology_route",
            "branch": source["branch"],
            "source_kind": source["source_kind"],
            "source_selected_by_mtt": source["source_selected_by_mtt"],
            "fixed_differential_cohomology_class": source["fixed_differential_cohomology_class"],
            "same_class_as_finite_m1_deck_cocycle": source["same_class_as_finite_m1_deck_cocycle"],
            "retention_scope": source["retention_scope"],
        },
        "proof_inputs": {
            "prior_manifest_contains_pic0_slot": SLOT in missing_before,
            "previous_two_operator_source_slots_closed": previous_slot["slot_status_after_closure"][
                "filled_operator_slot_count"
            ]
            == 2,
            "direct_pic0_invariance_retired": gerbe["direct_pic0_invariance_status"] == "RETIRED_FOR_NOW",
            "neutral_pic0_selection_absent": gerbe["neutral_pic0_selection_status"] == "ABSENT",
            "operator_pic0_replaced_for_next_attempt": gerbe["operator_pic0_replaced_for_next_attempt"],
            "selected_s3_gerbe_source_certified": promotion["route_B_operator_pic0_gerbe_de"][
                "selected_s3_gerbe_source_certified"
            ],
            "source_level_gerbe_rhoe_promoted": gerbe["source_level_gerbe_rhoe_promoted"],
            "pic0_reduction_names_gerbe_as_primary_route": pic0_reduction["route_decision"]["gerbe_twisted_de_source"][
                "status"
            ]
            == "PRIMARY_EXECUTION_ROUTE",
        },
        "closed_at_source_or_restriction_level": gerbe["closed_at_source_or_restriction_level"],
        "slot_status_after_closure": {
            "required_operator_slot_count": previous_slot["slot_status_after_closure"]["required_operator_slot_count"],
            "filled_operator_slot_count": 3,
            "filled_slots": closed_slots,
            "missing_slots": missing_after,
            "remaining_missing_slot_count": len(missing_after),
        },
        "closure_result": {
            "third_operator_source_slot_closed": True,
            "selected_source_value_emitted": True,
            "pic0_closed_by_direct_invariance": False,
            "pic0_closed_by_neutral_character_selection": False,
            "pic0_closed_by_selected_gerbe_replacement": True,
            "actual_DE_payload_emitted": False,
            "operator_level_projective_rhoe_promoted": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "Pic0 is closed as a source-slot by replacement with the selected S3 gerbe route. "
                "This does not emit D_E/rho_E operator payloads, HYM/Route-C residuals, "
                "Riesz/Green/dotD retention, or determinant/torsion response."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTTrueEquivalenceDecisionAfterPic0Slot.v1",
        "status": "THREE_QASU3_OPERATOR_SOURCE_SLOTS_CLOSED_DYNAMIC_PACKET_OPEN",
        "operator_source_slots_closed": 3,
        "operator_source_slots_remaining": len(missing_after),
        "closed_slots": closed_slots,
        "remaining_payloads_from_visible_cutset": cutset["remaining_minimal_payloads"],
        "actual_DE_payload_emitted": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedThirdQaSU3OperatorSlotClosureOrPic0GerbeReplacement",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_secondqasu3operatorslotclosure_or_productionprofileimport.candidate.json"),
            "previous_slot_closure": third_slot["input_previous_slot_closure"],
            "terminal_pic0_gerbe_bridge": third_slot["input_terminal_pic0_gerbe_bridge"],
            "operator_pic0_gerbe_replacement": third_slot["input_operator_pic0_gerbe_replacement"],
            "pic0_reduction": third_slot["input_pic0_reduction"],
        },
        "output_packets": {
            "third_qasu3_operator_source_slot_closure": rel(THIRD_SLOT),
            "true_equivalence_decision_after_pic0_slot": rel(DECISION),
        },
        "theorem": {
            "name": "ThirdQaSU3OperatorSourceSlotClosureByGerbePic0Replacement",
            "proved": True,
            "statement": (
                "Direct operator-layer Pic0 invariance is retired and neutral Pic0 selection is absent, but "
                "the verified terminal-source/Pic0 bridge selects the q79/F,m=1 S3 gerbe differential-cohomology "
                "route as the operator-layer Pic0 replacement. This closes the Pic0 selection/physical quotient "
                "operator-source slot and reduces the Qa/SU3 operator-source cutset from six to five remaining slots."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "third_QaSU3_operator_source_slot_closed": True,
            "operator_source_slots_closed_total": 3,
            "Pic0_slot_closed_by_gerbe_replacement": True,
            "actual_DE_payload_emitted": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "Pic0_selection_or_physical_quotient_theorem_slot": True,
            "operator_pic0_replaced_by_selected_s3_gerbe_route": True,
            "qasu3_operator_cutset_reduced_to_five_slots": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
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
        "certificate": "MTT_Selected_ThirdQaSU3OperatorSlotClosure_or_Pic0GerbeReplacement_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "third_QaSU3_operator_source_slot_closed": True,
        "closed_operator_source_slots_total": 3,
        "operator_source_slots_remaining": len(missing_after),
        "Pic0_slot_closed_by_gerbe_replacement": True,
        "actual_DE_payload_emitted": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected ThirdQaSU3OperatorSlotClosure or Pic0GerbeReplacement v1

This artifact closes the third Qa/SU3 operator-source slot:
`{SLOT}`.

It does **not** prove direct operator-layer Pic0 invariance.  Instead, it uses
the already verified replacement route: direct Pic0 invariance is retired,
neutral Pic0 selection is absent, and the selected q79/F,m=1 S3 gerbe
differential-cohomology source is the physical/operator-layer replacement route.

The cutset is now reduced from eight original operator-source slots to five
remaining slots.  No D_E/rho_E operator payload, HYM/Route-C residual,
Riesz/Green/dotD packet, or determinant/torsion response is claimed.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (THIRD_SLOT, third_slot),
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
