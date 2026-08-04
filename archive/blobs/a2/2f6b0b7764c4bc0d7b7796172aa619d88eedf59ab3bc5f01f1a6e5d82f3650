"""Audit local-QFT precision observable table or Qa/SU3-HYM packet value attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LOCAL_QFT_ATTEMPT = PACKET_DIR / "local_qft_precision_observable_table_attempt.packet.json"
QASU3_ATTEMPT = PACKET_DIR / "qasu3_hym_operator_packet_value_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_value_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LocalQFTPrecisionObservableTable_or_QaSU3HYMOperatorPacket_ValueAttempt_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_LOCALQFTPRECISIONOBSERVABLETABLE_OR_QASU3HYMOPERATORPACKET_VALUEATTEMPT_BUILT_MINIMAL_ROWS_OPEN"
NEXT = "MTT_Selected_PrecisionObservableTable_FullLoopImport_or_QaSU3OperatorSlotFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    local = load(LOCAL_QFT_ATTEMPT)
    qasu3 = load(QASU3_ATTEMPT)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    rows = local["value_rows_emitted"]
    require(rows["representative_tree_level_H_to_ff_rows"] == 5, "unexpected Higgs tree row count")
    require(rows["representative_tree_level_W_to_lnu_rows"] == 3, "unexpected W tree row count")
    require(rows["finite_nonnegative_widths"] is True, "tree widths not finite/nonnegative")
    require(rows["tree_sum_open_H_to_ff_width_GeV"] > 0, "Higgs tree sum not positive")
    require(rows["tree_sum_W_leptonic_width_GeV"] > 0, "W tree sum not positive")

    gate = local["local_qft_gate_update"]
    require(gate["representative_scattering_or_decay_rows_now_filled"] is True, "minimal row subgate not filled")
    require(gate["two_point_functions_or_propagator_normalizations_closed"] is False, "propagator rows overclosed")
    require(gate["ward_anomaly_observable_checks_closed"] is False, "Ward/anomaly rows overclosed")
    require(gate["precision_loop_corrected_observable_table_closed"] is False, "precision table overclosed")
    require(gate["full_profile_likelihood_closed"] is False, "profile likelihood overclosed")
    require(local["precision_acceptance"]["accepted_as_minimal_local_QFT_value_suite"] is True, "minimal suite not accepted")
    require(local["precision_acceptance"]["accepted_as_precision_SM_observable_table"] is False, "tree rows overaccepted as precision")
    require(local["precision_acceptance"]["accepted_for_true_SM_equivalence"] is False, "local route overaccepted")

    support = qasu3["hym_operator_support"]
    require(support["End0_D_E_formula_emitted"] is True, "HYM D_E support missing")
    require(support["protected_T3_lane_closed"] is True, "T3 lane support missing")
    require(support["T1_T2_covariant_Green_closed"] is True, "T1/T2 Green support missing")
    require(support["offdiagonal_row_model_control_closed"] is True, "offdiagonal control missing")
    require(support["validator_ready_sector_payload"] is False, "sector payload overpromoted")
    require(support["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD overpromoted")
    require(support["rank2_to_rank3_sector_transfer_values_extracted"] is False, "sector transfer overpromoted")

    slots = qasu3["operator_slot_attempt"]
    require(slots["required_operator_slot_count"] == 8, "operator slot count changed")
    require(slots["filled_operator_slot_count"] == 0, "operator slots unexpectedly filled")
    require(len(slots["filled_slots"]) == 0, "filled slot list should be empty")
    require(len(slots["missing_slots"]) == 8, "missing slot list should contain all slots")
    require(slots["actual_selected_operator_payload_filled"] is False, "actual operator payload overfilled")
    require(qasu3["promotion_acceptance"]["accepted_as_actual_QaSU3_packet"] is False, "Qa/SU3 overaccepted")
    require(qasu3["promotion_acceptance"]["accepted_for_true_SM_equivalence"] is False, "Qa/SU3 true-equivalence overaccepted")
    require(qasu3["promotion_acceptance"]["accepted_for_no_knob"] is False, "Qa/SU3 no-knob overaccepted")

    require(promotion["status"] == "MINIMAL_LOCAL_QFT_ROWS_FILLED_BOTH_TRUE_EQ_ROUTES_OPEN", "promotion status mismatch")
    require(promotion["route_A"]["minimal_local_QFT_value_suite_filled"] is True, "Route A minimal fill missing")
    require(promotion["route_A"]["precision_observable_table_closed"] is False, "Route A precision overclosed")
    require(promotion["route_B"]["partial_source_plus_HYM_support_combined"] is True, "Route B support combination missing")
    require(promotion["route_B"]["actual_QaSU3_operator_packet_closed"] is False, "Route B packet overclosed")
    require(promotion["SM_parity_closed"] is True, "SM parity reopened")
    require(promotion["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["minimal_local_QFT_value_suite_filled"] is True, "candidate minimal suite missing")
    require(data["closure_decision"]["precision_observable_table_closed"] is False, "candidate precision overclosed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "candidate Qa/SU3 overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["what_closes_now"]["representative_scattering_or_decay_rows_subgate"] is True, "subgate close missing")
    require(data["what_closes_now"]["qasu3_partial_payload_combined_with_hym_support"] is True, "support combination close missing")
    require(data["what_remains_open"]["full_precision_observable_value_table"] is True, "precision table gate missing")
    require(data["what_remains_open"]["actual_QaSU3_operator_packet"] is True, "Qa/SU3 gate missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require("does not promote" in note, "note missing non-promotion guard")
    require("never source selectors" in note, "note missing selector guard")

    for packet in [data, local, qasu3, promotion, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
