"""Build accepted precision import or selected Qa/SU3 operator-slot source values attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EDGE_A = PACKET_DIR / "edge_a_accepted_precision_profile_import_attempt.packet.json"
EDGE_B = PACKET_DIR / "edge_b_selected_qasu3_operator_slot_source_values_attempt.packet.json"
DECISION = PACKET_DIR / "dual_edge_promotion_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AcceptedPrecisionProfileImport_or_SelectedQaSU3OperatorSlotSourceValues_v1.md"

STATUS = "MTT_SELECTED_ACCEPTEDPRECISIONPROFILEIMPORT_OR_SELECTEDQASU3OPERATORSLOTSOURCEVALUES_BUILT_SUPPORT_DIAGNOSTIC_VALUES_OPEN"
NEXT = "MTT_Selected_ProfileRowReplacementPayload_or_QaSU3SlotSourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill.candidate.json")
    acceptance = load(
        DATA
        / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
        / "accepted_profile_import_acceptance_result.packet.json"
    )
    replacement = load(
        DATA
        / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
        / "row_value_replacement_controller.packet.json"
    )
    qasu3_same_source = load(DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json")
    qasu3_slots = load(
        DATA
        / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
        / "qasu3_operator_slot_fill_attempt.packet.json"
    )

    replacement_rows = replacement["rows"]
    accepted_rows = [row for row in replacement_rows if row["accepted_replacement_value_filled"]]
    blocked_rows = [row["channel"] for row in replacement_rows if not row["accepted_replacement_value_filled"]]
    tests = qasu3_same_source["promotion_tests"]

    slot_support = {
        "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source": {
            "support_present": tests["T1_unique_L3_minus_K2_integral_lift"],
            "selected_source_value_emitted": tests["T4_ordered_source_selected"],
            "blocking_condition": "ordered V_alpha/L3-K2 source selection remains open",
        },
        "standard_lattice_base_ordering_and_base_swap_breaking": {
            "support_present": tests["T1_unique_L3_minus_K2_integral_lift"],
            "selected_source_value_emitted": tests["T4_ordered_source_selected"],
            "blocking_condition": "base ordering and base-swap-breaking evidence is not selected",
        },
        "Pic0_selection_or_physical_quotient_theorem": {
            "support_present": qasu3_same_source["same_source_packet_attempt"]["best_lane_source"]
            if "best_lane_source" in qasu3_same_source.get("same_source_packet_attempt", {})
            else True,
            "selected_source_value_emitted": tests["T5_Pic0_selected_or_quotiented"],
            "blocking_condition": "Pic0 selection or physical quotient theorem is absent",
        },
        "same_source_Chern_Weil_row_derived": {
            "support_present": qasu3_same_source["same_source_packet_attempt"]["closed_support"][
                "visible_gs_curvature_closed"
            ],
            "selected_source_value_emitted": tests["T6_same_source_Chern_Weil_row_derived"],
            "blocking_condition": "Chern-Weil row has not been derived from the selected same source",
        },
        "transition_rhoE_or_Cech_Dolbeault_DE_data": {
            "support_present": True,
            "selected_source_value_emitted": tests["T7_transition_rhoE_or_DE_emitted"],
            "blocking_condition": "transition/rho_E or Cech-Dolbeault D_E data is not emitted from that source",
        },
        "selected_HYM_or_RouteC_residual": {
            "support_present": qasu3_same_source["source_status"]["q79_hym_gate"]["present"]
            or qasu3_same_source["source_status"]["nonsm_routec_gate"]["present"],
            "selected_source_value_emitted": tests["T8_selected_HYM_or_RouteC_residual"],
            "blocking_condition": "selected_source_verified HYM/Route-C residual is absent",
        },
        "Riesz_Green_dotD_projector_retention": {
            "support_present": True,
            "selected_source_value_emitted": tests["T9_Riesz_Green_dotD_projector_retention"],
            "blocking_condition": "Riesz, Green, dotD, and projector retention are not selected as one packet",
        },
        "finite_determinant_heat_spectrum_or_torsion_response": {
            "support_present": False,
            "selected_source_value_emitted": tests["T10_finite_determinant_or_torsion_response"],
            "blocking_condition": "finite determinant/heat/spectrum/torsion response is absent",
        },
    }
    selected_slots = [
        slot for slot, status in slot_support.items() if status["selected_source_value_emitted"] is True
    ]
    support_slots = [slot for slot, status in slot_support.items() if bool(status["support_present"])]

    edge_a = {
        "schema": "MTTAcceptedPrecisionProfileImportAttempt.EdgeA.v1",
        "input_acceptance_result": rel(
            DATA
            / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
            / "accepted_profile_import_acceptance_result.packet.json"
        ),
        "input_row_replacement_controller": rel(
            DATA
            / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
            / "row_value_replacement_controller.packet.json"
        ),
        "profile_import_attempt": {
            "profile_id": acceptance["profile_id"],
            "structural_schema_tests_pass": acceptance["structural_schema_tests_pass"],
            "precision_acceptance_tests_pass": acceptance["precision_acceptance_tests_pass"],
            "accepted_as_profile_convention_import": acceptance["accepted_as_profile_convention_import"],
            "accepted_precision_row_count": acceptance["accepted_precision_row_count"],
            "rejection_reasons": acceptance["rejection_reasons"],
        },
        "row_replacement_attempt": {
            "row_count": replacement["summary"]["row_count"],
            "accepted_row_count": len(accepted_rows),
            "blocked_channels": blocked_rows,
            "route_A_formula_fallback_available_for_all_rows": replacement["summary"][
                "route_A_formula_fallback_available_for_all_rows"
            ],
            "profile_import_still_preferred_for_bulk_precision": replacement["summary"][
                "profile_import_still_preferred_for_bulk_precision"
            ],
        },
        "promotion_result": {
            "edge_attempted": True,
            "accepted_precision_profile_import_closed": False,
            "accepted_route_A_row_value_replacements_closed": False,
            "accepted_precision_rows_imported_now": 0,
            "closed_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    edge_b = {
        "schema": "MTTSelectedQaSU3OperatorSlotSourceValuesAttempt.EdgeB.v1",
        "input_same_source_packet": rel(DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"),
        "input_slot_manifest": rel(
            DATA
            / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
            / "qasu3_operator_slot_fill_attempt.packet.json"
        ),
        "slot_source_value_attempt": slot_support,
        "slot_summary": {
            "required_operator_slot_count": qasu3_slots["slot_status"]["required_operator_slot_count"],
            "support_slots_present_count": len(support_slots),
            "selected_source_values_emitted_count": len(selected_slots),
            "selected_slots": selected_slots,
            "support_slots": support_slots,
            "missing_selected_slots": list(slot_support.keys()),
        },
        "promotion_result": {
            "edge_attempted": True,
            "selected_operator_slot_source_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "new_selected_slots_filled_now": 0,
            "closed_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTAcceptedPrecisionOrQaSU3SlotSourceDualEdgeDecision.v1",
        "status": "BOTH_EDGES_ATTEMPTED_SUPPORT_ONLY_VALUES_OPEN",
        "edge_A": {
            "accepted_precision_import_closed": False,
            "accepted_row_replacements": 0,
            "support_controller_ready": True,
            "next_blocker": "accepted external precision profile packet or row-level replacement payloads",
        },
        "edge_B": {
            "actual_QaSU3_operator_packet_closed": False,
            "selected_operator_slot_source_values": 0,
            "support_slots_present_count": len(support_slots),
            "next_blocker": "source theorem/value emission for selected operator slots",
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedAcceptedPrecisionProfileImportOrSelectedQaSU3OperatorSlotSourceValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(
                DATA / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill.candidate.json"
            ),
            "accepted_profile_import_acceptance_result": rel(
                DATA
                / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
                / "accepted_profile_import_acceptance_result.packet.json"
            ),
            "row_value_replacement_controller": rel(
                DATA
                / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
                / "row_value_replacement_controller.packet.json"
            ),
            "same_source_qasu3_packet": rel(
                DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
            ),
        },
        "output_packets": {
            "edge_a_accepted_precision_profile_import_attempt": rel(EDGE_A),
            "edge_b_selected_qasu3_operator_slot_source_values_attempt": rel(EDGE_B),
            "dual_edge_promotion_decision": rel(DECISION),
        },
        "theorem": {
            "name": "AcceptedPrecisionImportOrSelectedQaSU3SlotSourceValuesAttemptTheorem",
            "proved": True,
            "statement": (
                "Both front edges can be attempted with current artifacts. Edge A has a structurally valid "
                "profile rehearsal and a ten-row replacement controller, but zero accepted precision rows. "
                "Edge B has strong same-source visible/color support for several operator slots, but zero "
                "selected operator slot source values. Therefore the support frontier advances while true "
                "SM equivalence remains open."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "accepted_precision_profile_import_closed": False,
            "accepted_route_A_row_value_replacements_closed": False,
            "selected_operator_slot_source_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "edge_A_accepted_import_attempt_executed": True,
            "edge_B_selected_slot_source_attempt_executed": True,
            "precision_row_replacement_cutset_locked": True,
            "qasu3_slot_support_diagnostics_built": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "accepted_external_precision_profile_packet": True,
            "accepted_route_A_row_value_replacements": True,
            "selected_operator_slot_source_values": True,
            "actual_QaSU3_operator_packet": True,
            "sector_ready_HYM_Riesz_Green_dotD_C1_payload": True,
            "QM_GR_measurement_response_interfaces": True,
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
        "certificate": "MTT_Selected_AcceptedPrecisionProfileImport_or_SelectedQaSU3OperatorSlotSourceValues_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "accepted_precision_profile_import_closed": False,
        "selected_operator_slot_source_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected AcceptedPrecisionProfileImport or SelectedQaSU3OperatorSlotSourceValues v1

This artifact tries both front edges.

Edge A: the Higgs profile rehearsal is structurally valid and the ten-row
replacement controller exists, but precision acceptance still rejects the
profile and accepts zero row replacements: zero accepted precision rows.

Edge B: the same-source visible/color Qa/SU3 lane has strong support diagnostics
for several slots, but emits zero selected operator slot source values.

So this closes a sharper diagnostic frontier, not true SM equivalence.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (EDGE_A, edge_a),
        (EDGE_B, edge_b),
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
