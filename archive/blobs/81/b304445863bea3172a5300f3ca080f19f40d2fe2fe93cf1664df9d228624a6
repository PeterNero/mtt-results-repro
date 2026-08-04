"""Build value attempt for local-QFT precision table or Qa/SU3-HYM operator packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_QFT_ATTEMPT = PACKET_DIR / "local_qft_precision_observable_table_attempt.packet.json"
QASU3_ATTEMPT = PACKET_DIR / "qasu3_hym_operator_packet_value_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_value_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LocalQFTPrecisionObservableTable_or_QaSU3HYMOperatorPacket_ValueAttempt_v1.md"

STATUS = "MTT_SELECTED_LOCALQFTPRECISIONOBSERVABLETABLE_OR_QASU3HYMOPERATORPACKET_VALUEATTEMPT_BUILT_MINIMAL_ROWS_OPEN"
NEXT = "MTT_Selected_PrecisionObservableTable_FullLoopImport_or_QaSU3OperatorSlotFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    current = load(DATA / "selected_precisionprofileloopvalues_or_actualqasu3operatorpayload_currentexecution.candidate.json")
    local_gate = load(
        DATA
        / "selected_correlatedprofilevalues_or_localqftobservablevalues"
        / "local_qft_observable_value_gate.packet.json"
    )
    tree_rows = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "representative_tree_level_decay_observable_rows.packet.json"
    )
    qasu3_payload = load(
        DATA
        / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
        / "qasu3_candidate_payload_fill_attempt.packet.json"
    )
    hym_green = load(
        DATA
        / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
        / "full_diagonal_end0_green_payload.packet.json"
    )

    h_rows = tree_rows["higgs_fermion_decay_rows"]
    w_rows = tree_rows["w_leptonic_decay_rows"]
    qasu3_slots = qasu3_payload["operator_payload_slots"]
    filled_slots = [key for key, value in qasu3_slots.items() if value is True]
    missing_slots = [key for key, value in qasu3_slots.items() if value is False]

    local_qft_attempt = {
        "schema": "MTTLocalQFTPrecisionObservableTableAttempt.v1",
        "input_gate": rel(
            DATA
            / "selected_correlatedprofilevalues_or_localqftobservablevalues"
            / "local_qft_observable_value_gate.packet.json"
        ),
        "input_tree_rows": rel(
            DATA
            / "selected_precisionqftobservablerows_or_actualqasu3packet"
            / "representative_tree_level_decay_observable_rows.packet.json"
        ),
        "value_rows_emitted": {
            "representative_tree_level_H_to_ff_rows": len(h_rows),
            "representative_tree_level_W_to_lnu_rows": len(w_rows),
            "finite_nonnegative_widths": tree_rows["summary"]["all_widths_finite_nonnegative"],
            "tree_sum_open_H_to_ff_width_GeV": tree_rows["summary"]["tree_sum_open_H_to_ff_width_GeV"],
            "tree_sum_W_leptonic_width_GeV": tree_rows["summary"]["tree_sum_W_leptonic_width_GeV"],
        },
        "local_qft_gate_update": {
            "representative_scattering_or_decay_rows_now_filled": True,
            "two_point_functions_or_propagator_normalizations_closed": False,
            "ward_anomaly_observable_checks_closed": False,
            "precision_loop_corrected_observable_table_closed": False,
            "full_profile_likelihood_closed": False,
        },
        "precision_acceptance": {
            "accepted_as_minimal_local_QFT_value_suite": True,
            "accepted_as_precision_SM_observable_table": False,
            "accepted_for_true_SM_equivalence": False,
            "why_not_precision": tree_rows["why_not_precision"],
        },
        "required_next_values": [
            "two-point functions or propagator normalizations",
            "Ward/anomaly observable checks",
            "loop-corrected local-QFT correlator/S-matrix/decay rows",
            "published or reconstructed profile likelihood values",
            "multi-loop threshold and scheme-convention table",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3_attempt = {
        "schema": "MTTQaSU3HYMOperatorPacketValueAttempt.v1",
        "input_partial_payload": rel(
            DATA
            / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
            / "qasu3_candidate_payload_fill_attempt.packet.json"
        ),
        "input_hym_green_payload": rel(
            DATA
            / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
            / "full_diagonal_end0_green_payload.packet.json"
        ),
        "partial_source_payload": qasu3_payload["partial_payload_fields"],
        "hym_operator_support": {
            "End0_D_E_formula_emitted": hym_green["End0_D_E_formula"]["emitted"],
            "protected_T3_lane_closed": hym_green["protected_T3_lane"]["closed"],
            "T1_T2_covariant_Green_closed": hym_green["T1_T2_covariant_Green"]["closed"],
            "offdiagonal_row_model_control_closed": hym_green["offdiagonal_row_model_control"]["closed"],
            "validator_ready_sector_payload": hym_green["operator_payload_boundary"][
                "validator_ready_sector_payload"
            ],
            "physical_dotD_alpha1_payload_extracted": hym_green["operator_payload_boundary"][
                "physical_dotD_alpha1_payload_extracted"
            ],
            "rank2_to_rank3_sector_transfer_values_extracted": hym_green["operator_payload_boundary"][
                "rank2_to_rank3_sector_transfer_values_extracted"
            ],
        },
        "operator_slot_attempt": {
            "required_operator_slot_count": qasu3_payload["required_operator_slot_count"],
            "filled_operator_slot_count": qasu3_payload["filled_operator_slot_count"],
            "filled_slots": filled_slots,
            "missing_slots": missing_slots,
            "actual_selected_operator_payload_filled": qasu3_payload[
                "actual_selected_operator_payload_filled"
            ],
        },
        "promotion_acceptance": {
            "accepted_as_actual_QaSU3_packet": False,
            "accepted_for_true_SM_equivalence": False,
            "accepted_for_no_knob": False,
            "reason": (
                "The value attempt combines the best partial visible/color source payload with diagonal "
                "End0 HYM Green support. It still lacks all required selected operator slots and is not "
                "sector-ready."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTLocalQFTOrQaSU3ValueAttemptPromotionDecision.v1",
        "status": "MINIMAL_LOCAL_QFT_ROWS_FILLED_BOTH_TRUE_EQ_ROUTES_OPEN",
        "route_A": {
            "minimal_local_QFT_value_suite_filled": True,
            "precision_observable_table_closed": False,
            "true_SM_equivalence_closed": False,
            "next_blocker": "full precision loop/profile observable table",
        },
        "route_B": {
            "partial_source_plus_HYM_support_combined": True,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "next_blocker": "fill selected operator slots and sector-ready HYM/Riesz/Green/dotD/C1 payload",
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedLocalQFTPrecisionObservableTableOrQaSU3HYMOperatorPacketValueAttempt",
        "status": STATUS,
        "inputs": {
            "current_execution": rel(
                DATA / "selected_precisionprofileloopvalues_or_actualqasu3operatorpayload_currentexecution.candidate.json"
            ),
            "local_qft_gate": rel(
                DATA
                / "selected_correlatedprofilevalues_or_localqftobservablevalues"
                / "local_qft_observable_value_gate.packet.json"
            ),
            "representative_tree_rows": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
            "qasu3_partial_payload": rel(
                DATA
                / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
                / "qasu3_candidate_payload_fill_attempt.packet.json"
            ),
            "hym_green_payload": rel(
                DATA
                / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
                / "full_diagonal_end0_green_payload.packet.json"
            ),
        },
        "output_packets": {
            "local_qft_precision_observable_table_attempt": rel(LOCAL_QFT_ATTEMPT),
            "qasu3_hym_operator_packet_value_attempt": rel(QASU3_ATTEMPT),
            "promotion_decision_after_value_attempt": rel(PROMOTION),
        },
        "theorem": {
            "name": "LocalQFTValueAttemptOrQaSU3OperatorPacketAttemptTheorem",
            "proved": True,
            "statement": (
                "The current artifacts fill a minimal local-QFT representative decay-row suite and combine "
                "the best partial Qa/SU3 visible/color source payload with diagonal HYM Green support. "
                "This closes only the minimal representative-row subgate. It does not emit a full precision "
                "observable/profile table or an actual selected sector-ready Qa/SU3-HYM operator packet."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "minimal_local_QFT_value_suite_filled": True,
            "precision_observable_table_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "representative_scattering_or_decay_rows_subgate": True,
            "qasu3_partial_payload_combined_with_hym_support": True,
            "precision_route_blocker_sharpened": True,
            "operator_route_blocker_sharpened": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "full_precision_observable_value_table": True,
            "published_or_reconstructed_profile_likelihood": True,
            "two_point_or_propagator_normalization_rows": True,
            "ward_anomaly_observable_checks": True,
            "actual_QaSU3_operator_packet": True,
            "selected_operator_slots": True,
            "sector_ready_HYM_Riesz_Green_dotD_C1_payload": True,
            "QM_GR_measurement_response_interfaces": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": current["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_LocalQFTPrecisionObservableTable_or_QaSU3HYMOperatorPacket_ValueAttempt_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "minimal_local_QFT_value_suite_filled": True,
        "precision_observable_table_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected LocalQFTPrecisionObservableTable or QaSU3HYMOperatorPacket ValueAttempt v1

This artifact attempts both legal true-equivalence exits.

Route A now fills the minimal representative local-QFT decay-row subgate using
the already emitted tree-level H->ff and W->lnu rows.  It does not promote these
rows to a full precision observable/profile table.

Route B combines the best partial same-source Qa/SU3 visible/color payload with
diagonal End0 HYM/Riesz/Green support.  It does not promote an actual selected
Qa/SU3-HYM operator packet because the selected operator slots and sector-ready
dynamic payload remain open.

Observed constants remain downstream replay inputs only, never source selectors.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (LOCAL_QFT_ATTEMPT, local_qft_attempt),
        (QASU3_ATTEMPT, qasu3_attempt),
        (PROMOTION, promotion),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
