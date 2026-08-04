"""Audit flavor-operator value use / CKM-PMNS orientation bridge."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
CSK_SOURCE = DATA / SLUG / "strict_csk_source_theorem_attempt.packet.json"
REDUCTION = DATA / SLUG / "csk_reduction_recheck.packet.json"
ORIENTATION = DATA / SLUG / "flavor_operator_ckmpmns_orientation_bridge.packet.json"
PRECISION = DATA / SLUG / "flavor_higgs_threshold_precision_integration_status.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_flavor_operator_orientation_bridge.packet.json"
NOTE = CORPUS / "MTT_Selected_FlavorOperatorValueUse_or_CKMPMNSOrientationBridge_v1.md"

STATUS = (
    "MTT_SELECTED_FLAVOROPERATORVALUEUSE_OR_CKMPMNSORIENTATIONBRIDGE_"
    "BUILT_OPERATOR_USE_BRIDGE_STRICT_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_CKMPMNSOrientationSourceOperator_or_FlavorPrecisionIntegration_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    csk_source = load(CSK_SOURCE)
    reduction = load(REDUCTION)
    orientation = load(ORIENTATION)
    precision = load(PRECISION)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "FlavorOperatorUseAndOrientationBridgeTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["flavor_operator_policy_value_use_closed"] is True
    assert decision["policy_csk_source_value_row_count"] == 9
    assert decision["strict_selected_csk_source_row_count"] == 0
    assert decision["strict_csk_source_theorem_closed"] is False
    assert decision["coefficient_reduction_below_nine_closed"] is False
    assert decision["coefficient_matrix_full_rank"] is True
    assert decision["CKM_PMNS_orientation_bridge_executable"] is True
    assert decision["qualitative_CP_bridge_closed"] is True
    assert decision["selected_CKM_PMNS_orientation_source_closed"] is False
    assert decision["measured_CKM_PMNS_phase_values_derived"] is False
    assert decision["h_lambda_minimal_one_primitive_integrated"] is True
    assert decision["precision_profile_integrated"] is True
    assert decision["accepted_true_equivalence_rows"] == 0
    assert decision["full_true_SM_equivalence_closed"] is False
    assert decision["full_no_knob_closed"] is False

    assert csk_source["policy_source_value_row_count"] == 9
    assert csk_source["strict_selected_no_knob_source_row_count"] == 0
    assert csk_source["selected_source_theorem_closed"] is False

    assert reduction["coefficient_matrix_rank"] == 3
    assert reduction["coefficient_matrix_full_rank"] is True
    assert reduction["reduction_below_nine_closed"] is False
    assert reduction["minimal_current_flavor_policy_slots"] == 9
    assert all(test["closes"] is False for test in reduction["tested_reductions"])

    assert orientation["bridge_ready"] is True
    assert orientation["diagonal_magnitude_operator"]["row_count"] == 9
    assert orientation["diagonal_magnitude_operator"]["strict_selected_no_knob_source_row_count"] == 0
    assert orientation["CKM_bridge"]["operator_use_closed"] is True
    assert orientation["CKM_bridge"]["selected_orientation_source_closed"] is False
    assert orientation["CKM_bridge"]["unitarity_max_residual"] < 1e-12
    assert orientation["PMNS_bridge"]["operator_use_closed"] is True
    assert orientation["PMNS_bridge"]["selected_orientation_source_closed"] is False
    assert orientation["PMNS_bridge"]["unitarity_max_residual"] < 1e-12
    assert orientation["dynamic_cp_support"]["qualitative_cp_orientation_bridge_closed"] is True
    assert orientation["dynamic_cp_support"]["measured_CKM_PMNS_phase_values_derived"] is False
    assert orientation["observed_data_used_as_selector"] is False
    assert orientation["target_fitting_used"] is False

    assert precision["h_lambda_lane"]["H_specific_parameter_count"] == 0
    assert precision["h_lambda_lane"]["P_EW_counted_as_shared_physical_primitive"] is True
    assert precision["minimal_parameter_ledger"]["charged_yukawa_counted_as_measured_replay"] == 9
    assert precision["precision_frontier"]["accepted_true_equivalence_rows"] == 0
    assert precision["precision_frontier"]["true_SM_equivalence_closed"] is False
    assert precision["full_true_SM_equivalence_closed"] is False

    assert next_packet["next_required_artifact"] == NEXT
    assert "strict selected c_{s,k} source theorem or independently selected lower-dimensional flavor source" in next_packet[
        "remaining_source_rows"
    ]

    assert cert["status"] == STATUS
    assert cert["policy_csk_source_value_row_count"] == 9
    assert cert["strict_selected_csk_source_row_count"] == 0
    assert cert["coefficient_matrix_full_rank"] is True
    assert cert["CKM_PMNS_orientation_bridge_executable"] is True
    assert cert["qualitative_CP_bridge_closed"] is True
    assert cert["selected_CKM_PMNS_orientation_source_closed"] is False
    assert cert["accepted_true_equivalence_rows"] == 0
    assert cert["full_true_SM_equivalence_closed"] is False
    assert cert["observed_data_used_as_selector"] is False
    assert NEXT in note
    assert "FlavorOperatorUseAndOrientationBridgeTheorem" in note
    print("flavor-operator value use / CKM-PMNS orientation bridge audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
