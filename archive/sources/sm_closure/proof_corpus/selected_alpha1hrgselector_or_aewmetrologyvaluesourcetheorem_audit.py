"""Audit alpha1-HRG selector / A_EW value-source theorem packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1HRGSelector_or_AEWMetrologyValueSourceTheorem_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

ALPHA_PACKET = BASE / "alpha1_hrg_selector_promotion_attempt.packet.json"
AEW_PACKET = BASE / "aew_metrology_value_source_attempt.packet.json"
DUAL_PACKET = BASE / "dual_route_residual_lock.packet.json"
CUTSET_PACKET = BASE / "next_cutset_after_alpha1_aew_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_ALPHA1HRGSELECTOR_OR_AEWMETROLOGYVALUESOURCETHEOREM_"
    "ATTEMPTED_EXACT_DEFICIT_LOCKED_SOURCE_OPEN"
)
NEXT = "MTT_Selected_DynamicPhiFinC1Payload_or_LargeThresholdHRGConsumerMap_v1"
S_BETA = 0.004701083905943647
AEW = 0.0685013467625
LAMBDA_DTERM = 0.00032203057880065373
LAMBDA_MT = 0.12604
HRG = 391.39140285811936
REQ_AEW = 26.810838207045368
H_EXT_L2 = 0.03961411527057935
H_EXT_RESIDUAL_L2 = 6.751979459438445e-13


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    alpha = load(ALPHA_PACKET)
    aew = load(AEW_PACKET)
    dual = load(DUAL_PACKET)
    cutset = load(CUTSET_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate theorem closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")
    require(
        candidate["theorem"]["name"] == "Alpha1HRGSelectorOrAEWMetrologyValueSourceTheorem",
        "candidate theorem name",
    )
    require(candidate["theorem"]["proved"] is True, "candidate theorem proved")

    decision = candidate["closure_decision"]
    for key in [
        "alpha1_HRG_selector_attempt_closed",
        "AEW_value_source_attempt_closed",
        "dual_route_exact_deficit_locked",
        "conditional_lambda_alpha1_candidate_isolated",
        "alpha_source_strength_prioritized",
        "same_branch_alpha1_derivative_closed_by_latest_bridge",
        "honest_dotd_validator_replay_closed_by_latest_bridge",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_alpha_source_strength_value_emitted",
        "selected_transfer_normalization_emitted",
        "typed_BN_retarded_alpha1_derivative_emitted",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "primitive_C1_contractions_emitted",
        "A_selected_emitted",
        "b_selected_emitted",
        "typed_consumer_map_to_HRG_emitted",
        "selected_A_EW_value_emitted",
        "selected_mu_match_value_emitted",
        "selected_threshold_RG_transport_emitted",
        "selected_large_threshold_factor_emitted",
        "same_HRG_nonHiggs_prediction_emitted",
        "burden_equivalence_accepted_as_source",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_HRG_selector_count"] == 0, "accepted HRG selectors")
    require(decision["accepted_AEW_source_count"] == 0, "accepted A_EW sources")

    nums = candidate["key_numbers"]
    require(abs(nums["s_beta"] - S_BETA) < 1e-18, "s_beta")
    require(abs(nums["A_EW_Mt_external"] - AEW) < 1e-15, "A_EW")
    require(abs(nums["lambda_Dterm_Mt_external_AEW_times_selected_sbeta"] - LAMBDA_DTERM) < 1e-18, "lambda dterm")
    require(abs(nums["lambda_Mt_external_coordinate"] - LAMBDA_MT) < 1e-15, "lambda Mt")
    require(abs(nums["computed_HRG_burden"] - HRG) < 1e-12, "computed HRG")
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(nums["burden_equivalence_residual"] == 0.0, "burden residual")
    require(abs(nums["required_A_EW_to_match_external_lambda_Mt"] - REQ_AEW) < 1e-12, "required A_EW")
    require(abs(nums["direct_required_A_EW_lambda_over_s_beta"] - REQ_AEW) < 1e-12, "direct required A_EW")
    require(nums["direct_required_A_EW_residual"] == 0.0, "direct required residual")
    require(abs(nums["required_A_EW_over_external_A_EW"] - HRG) < 1e-12, "required/external ratio")
    require(nums["required_A_EW_over_external_A_EW_minus_HRG_abs"] == 0.0, "required/external HRG residual")
    require(abs(nums["lambda_replay_from_external_AEW_s_beta_HRG"] - LAMBDA_MT) < 1e-15, "lambda replay")
    require(nums["lambda_replay_residual"] == 0.0, "lambda replay residual")
    require(nums["lambda_alpha1_candidate"] == 1.0, "lambda alpha1")
    require(nums["latest_bridge_lambda_alpha1"] == 1.0, "bridge lambda alpha1")
    require(nums["latest_bridge_N_alpha1_h_ext"] == 1.0, "bridge N alpha1")
    require(nums["latest_bridge_alpha1_driver_verified"] is True, "bridge alpha1 driver")
    require(nums["latest_bridge_selected_dotD_source_verified"] is True, "bridge dotD source")
    require(nums["latest_bridge_honest_dotd_validator_exit_code"] == 0, "bridge dotD exit")
    require(abs(nums["h_ext_l2"] - H_EXT_L2) < 1e-18, "h ext L2")
    require(abs(nums["h_ext_residual_l2"] - H_EXT_RESIDUAL_L2) < 1e-24, "h ext residual")
    require(nums["dynamic_phi_fin_c1_payload_selected"] is False, "dynamic payload")
    require(nums["primitive_C1_contractions_emitted"] is False, "primitive contractions")
    require(nums["A_selected_claimed"] is False, "A_selected")
    require(nums["b_selected_claimed"] is False, "b_selected")
    require(nums["same_source_packet_selected_fields"] == 0, "same-source selected fields")
    require(nums["same_source_packet_required_fields"] == 7, "same-source required fields")
    require(nums["accepted_external_wzh_coordinate_rows"] == 5, "WZH rows")
    require(nums["accepted_selected_Rtheta_source_rows"] == 0, "Rtheta rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "alpha1_HRG_selector_attempt_closed",
        "AEW_value_source_attempt_closed",
        "dual_route_exact_deficit_locked",
        "conditional_lambda_alpha1_candidate_isolated",
        "same_branch_alpha1_derivative_closed_by_latest_bridge",
        "honest_dotd_validator_replay_closed_by_latest_bridge",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "selected_alpha_source_strength_value_emitted",
        "selected_transfer_normalization_emitted",
        "typed_BN_retarded_alpha1_derivative_emitted",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "primitive_C1_contractions_emitted",
        "A_selected_emitted",
        "b_selected_emitted",
        "typed_consumer_map_to_HRG_emitted",
        "selected_A_EW_value_emitted",
        "selected_mu_match_value_emitted",
        "selected_threshold_RG_transport_emitted",
        "selected_large_threshold_factor_emitted",
        "same_HRG_nonHiggs_prediction_emitted",
        "burden_equivalence_accepted_as_source",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(alpha["status"] == "ALPHA1_HRG_SELECTOR_PROMOTION_ATTEMPTED_SOURCE_VALUE_OPEN", "alpha status")
    require(alpha["theorem"]["name"] == "Alpha1HRGSelectorPromotionAttemptTheorem", "alpha theorem")
    require(alpha["acceptance_predicate"]["satisfied_now"] is False, "alpha predicate")
    alpha_decision = alpha["decision"]
    require(alpha_decision["alpha1_HRG_selector_attempt_closed"] is True, "alpha attempt")
    require(alpha_decision["alpha_source_strength_prioritized"] is True, "alpha priority")
    require(alpha_decision["conditional_lambda_alpha1_candidate_isolated"] is True, "alpha candidate")
    require(
        alpha_decision["same_branch_alpha1_derivative_closed_by_latest_bridge"] is True,
        "alpha bridge",
    )
    require(
        alpha_decision["honest_dotd_validator_replay_closed_by_latest_bridge"] is True,
        "dotD bridge",
    )
    for key in [
        "selected_alpha_source_strength_value_emitted",
        "selected_transfer_normalization_emitted",
        "typed_BN_retarded_alpha1_derivative_emitted",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "primitive_C1_contractions_emitted",
        "A_selected_emitted",
        "b_selected_emitted",
        "typed_consumer_map_to_HRG_emitted",
        "same_HRG_nonHiggs_prediction_emitted",
        "accepted_as_HRG_selector",
    ]:
        require(alpha_decision[key] is False, f"alpha false {key}")
    bridge = alpha["latest_bridge_replay"]
    require(bridge["same_branch_alpha1_derivative_selected_emitted"] is True, "bridge derivative")
    require(bridge["du_dalpha1_equals_h_ext"] is True, "bridge du/dalpha")
    require(bridge["lambda_alpha1"] == 1.0, "bridge lambda")
    require(bridge["N_alpha1_h_ext"] == 1.0, "bridge norm")
    require(bridge["alpha1_driver_verified"] is True, "bridge alpha driver")
    require(bridge["selected_dotD_source_verified"] is True, "bridge dotD source")
    require(bridge["honest_dotd_validator_exit_code"] == 0, "bridge validator")
    require(bridge["dynamic_phi_fin_c1_payload_selected"] is False, "bridge payload")
    require(bridge["primitive_C1_contractions_emitted"] is False, "bridge primitive")
    require(bridge["A_selected_claimed"] is False, "bridge A")
    require(bridge["b_selected_claimed"] is False, "bridge b")
    require(alpha["conditional_alpha_value"]["lambda_alpha1_candidate"] == 1.0, "alpha lambda")
    require(alpha["route_replay"]["route_A_unit_source_strength_coordinate"]["local_transport_formula_closes"] is True, "route A local")
    require(alpha["route_replay"]["route_A_unit_source_strength_coordinate"]["emitted_as_selected"] is False, "route A emitted")
    require(alpha["route_replay"]["route_B_same_source_packet_or_transfer_normalization"]["selected_fields"] == 0, "route B selected")
    require(alpha["route_replay"]["route_B_same_source_packet_or_transfer_normalization"]["required_fields"] == 7, "route B required")
    require(alpha["route_replay"]["route_C_retarded_overlap_kernel_transfer"]["ckm_retarded_kernel_pattern_available"] is True, "route C support")
    require(alpha["route_replay"]["route_C_retarded_overlap_kernel_transfer"]["selected_BN_tangent_or_retarded_kernel"] is False, "route C selected")
    require(alpha["source_identity_lanes"]["lane_A_same_source_identity_verdict"] == "OPEN", "lane A")
    require(alpha["source_identity_lanes"]["lane_B_typed_retarded_kernel_verdict"] == "OPEN", "lane B")

    require(aew["status"] == "AEW_METROLOGY_VALUE_SOURCE_ATTEMPTED_EXTERNAL_ONLY_SOURCE_OPEN", "A_EW status")
    require(aew["theorem"]["name"] == "AEWMetrologyValueSourceAttemptTheorem", "A_EW theorem")
    aew_decision = aew["decision"]
    require(aew_decision["aew_metrology_value_source_attempt_closed"] is True, "A_EW attempt")
    for key in [
        "selected_A_EW_value_emitted",
        "selected_mu_match_value_emitted",
        "selected_threshold_RG_transport_emitted",
        "external_coordinate_replay_promoted_to_source",
        "selected_large_threshold_factor_emitted",
        "accepted_as_A_EW_value_source",
    ]:
        require(aew_decision[key] is False, f"A_EW false {key}")
    require(aew_decision["selected_metrology_source_slot_count"] == 0, "A_EW source slots")
    require(aew["external_coordinate_summary"]["accepted_external_wzh_coordinate_rows"] == 5, "A_EW WZH")
    require(aew["external_coordinate_summary"]["accepted_selected_Rtheta_source_rows"] == 0, "A_EW Rtheta")
    require(abs(aew["required_source_values"]["required_A_EW_over_external_A_EW"] - HRG) < 1e-12, "A_EW HRG")
    require(aew["required_source_values"]["required_A_EW_over_external_A_EW_minus_HRG_abs"] == 0.0, "A_EW HRG residual")

    require(dual["status"] == "DUAL_ROUTE_EXACT_DEFICIT_LOCKED_TO_HRG_SIZED_SOURCE_OBJECT", "dual status")
    require(dual["theorem"]["name"] == "DualRouteExactDeficitLockTheorem", "dual theorem")
    equalities = dual["equalities"]
    require(abs(equalities["lambda_Mt_over_A_EW_s_beta"] - HRG) < 1e-12, "dual ratio")
    require(equalities["HRG_burden_residual"] == 0.0, "dual HRG residual")
    require(equalities["lambda_replay_residual"] == 0.0, "dual lambda residual")
    require(abs(equalities["required_A_EW_over_external_A_EW"] - HRG) < 1e-12, "dual required/external")
    require(equalities["required_A_EW_over_external_A_EW_minus_HRG_abs"] == 0.0, "dual required residual")
    require(dual["interpretation"]["not_a_plain_AEW_gauge_row"] is True, "dual not plain")
    require(dual["interpretation"]["not_accepted_from_external_lambda_Mt"] is True, "dual no external")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_DYNAMIC_PHIFIN_C1_PAYLOAD_OR_LARGE_THRESHOLD_HRG_CONSUMER_MAP",
        "cutset",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "alpha/source-strength HRG selector promotion route executed",
        "latest visible/Route-C bridge imported as closing same-branch alpha1 derivative and honest dotD replay",
        "A_EW metrology value-source route executed with zero selected source slots",
        "exact HRG-sized deficit locked as one large-threshold/source object",
        "external lambda_Mt barred from source selection",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "selected dynamic Phi_fin C1 payload values",
        "selected primitive C1 contractions",
        "A_selected and b_selected value payload",
        "typed B_N retarded alpha1 derivative",
        "typed consumer map from alpha/BN source data to UP_RET_OVERLAP.HRG",
        "selected A_EW gauge/action normalization or large threshold/RG transport",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "What Just Locked",
        "required/external A_EW    = 391.39140285811936",
        "Alpha1 HRG Selector",
        "alpha1 driver verified    = True",
        "dynamic Phi_fin/C1 payload= False",
        "A_EW Value Source",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: alpha1-HRG and A_EW source routes executed; exact HRG-sized "
        "deficit locked as a source obligation without promoting external lambda_Mt."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
