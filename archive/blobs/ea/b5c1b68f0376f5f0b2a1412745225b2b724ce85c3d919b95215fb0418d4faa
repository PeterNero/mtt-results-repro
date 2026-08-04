"""Audit the H-threshold/RG operator or universal-primitive policy packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hthresholdrgoperator_or_universalprimitivepolicy"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_SEARCH = PACKET_DIR / "strict_h_threshold_rg_operator_source_search.packet.json"
ONE_PRIMITIVE = PACKET_DIR / "existing_one_primitive_reuse_recheck.packet.json"
ADMISSION = PACKET_DIR / "h_threshold_universal_primitive_admission_matrix.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_minimal_parameter_h_gate_execution.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_policy_split.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_policy_split.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HThresholdRGOperator_or_UniversalPrimitivePolicy_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HTHRESHOLDRGOPERATOR_OR_UNIVERSALPRIMITIVEPOLICY_"
    "POLICY_SPLIT_CLOSED_OPERATOR_OPEN"
)
NEXT = "MTT_Selected_HThresholdRGSourceTheorem_or_MinimalPrimitiveCalibrationRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    strict = load(STRICT_SEARCH)
    one = load(ONE_PRIMITIVE)
    admission = load(ADMISSION)
    conditional = load(CONDITIONAL)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("one primitive", one),
        ("admission", admission),
        ("conditional", conditional),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "strict_H_threshold_RG_operator_source_search_closed",
        "existing_one_primitive_reuse_rechecked",
        "H_threshold_universal_primitive_admission_matrix_built",
        "controlled_empirical_H_gate_execution_formula_built",
        "conditional_parameterized_H_gate_executable_if_primitive_admitted",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "strict_H_threshold_RG_operator_emitted",
        "existing_one_primitive_closes_H_threshold",
        "H_threshold_universal_primitive_selected_now",
        "lambda_H_prediction_claim_allowed_if_calibrated_on_lambda_H",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "internal scalar rows")

    nums = data["diagnostic_numbers_not_source"]
    required = nums["required_UP_RET_OVERLAP_HRG_if_calibrated_on_lambda_H"]
    require(required > 100, "required primitive too small")
    require(nums["lambda_if_R_H_RG_equals_1"] < nums["external_lambda_Mt_coordinate"], "R=1 should fail")
    require(
        math.isclose(
            nums["lambda_if_R_H_RG_equals_required_value"],
            nums["external_lambda_Mt_coordinate"],
            rel_tol=0,
            abs_tol=1e-14,
        ),
        "required primitive arithmetic",
    )
    require(abs(nums["residual_at_required_value"]) < 1e-14, "required residual")

    require(
        strict["status"] == "STRICT_H_THRESHOLD_RG_OPERATOR_NOT_EMITTED_CURRENT_SOURCES",
        "strict status",
    )
    require(strict["accepted_current_source_rows"]["selected_R_H_RG"] is False, "strict R overclose")
    require(strict["accepted_current_source_rows"]["selected_K_threshold_Omega_H_lambda"] is False, "strict K overclose")
    require(strict["source_status_imports"]["B43_current_source_nogo_for_strict_vector"] is True, "B43 no-go")
    require(strict["mathematical_impossibility_claimed"] is False, "strict impossibility overclaim")

    require(
        one["status"] == "EXISTING_ONE_PRIMITIVE_REUSE_RECHECKED_H_THRESHOLD_STILL_OPEN",
        "one primitive status",
    )
    bridge = one["existing_primitive_bridge"]
    require(bridge["one_primitive_tier_contract_closed"] is True, "bridge contract")
    require(bridge["one_primitive_value_selected"] is False, "bridge value overselected")
    require(bridge["alpha1_and_weak_mixing_share_same_physical_bridge"] is True, "bridge sharing")
    require(one["decision"]["reuse_existing_one_primitive_as_H_threshold_multiplier"] is False, "hidden H reuse")
    require(one["decision"]["H_gate_closed_by_existing_one_primitive_alone"] is False, "one primitive H overclose")

    require(
        admission["status"] == "H_THRESHOLD_PRIMITIVE_POLICY_MATRIX_BUILT_NONE_SELECTED",
        "admission status",
    )
    require(admission["policy_import"]["maximum_live_universal_parameters"] == 3, "max params")
    require(admission["policy_import"]["selected_parameter_count_now"] == 0, "selected params")
    require(admission["crossuse_import"]["selected_parameter_count_now"] == 0, "crossuse selected")
    candidate = admission["candidate_class_mapping"]["UP_RET_OVERLAP_for_H_threshold"]
    require(candidate["id"] == "UP-RET-OVERLAP", "candidate class")
    require(candidate["required_postcheck_value_if_calibrated_on_lambda_H"] == required, "candidate required")
    lanes = {row["lane"]: row for row in admission["admission_matrix"]}
    require(lanes["strict_source_operator"]["new_universal_parameters"] == 0, "strict lane params")
    require(lanes["strict_source_operator"]["accepted_now"] is False, "strict accepted")
    require(
        lanes["reuse_existing_physical_unit_primitive_only"]["H_gate_effect"]
        == "can support A_EW/mu_match tier but does not emit R_H^RG",
        "reuse lane effect",
    )
    require(lanes["add_H_threshold_universal_primitive"]["new_universal_parameters"] == 1, "H primitive params")
    require(lanes["physical_unit_plus_H_threshold_primitive"]["new_universal_parameters"] == 2, "two primitive params")
    adm_decision = admission["decision"]
    require(adm_decision["selected_H_threshold_primitive_now"] is False, "H primitive selected")
    require(adm_decision["ordinary_H_only_knob_allowed"] is False, "ordinary H knob")
    require(adm_decision["calibrating_H_lambda_makes_H_lambda_a_prediction"] is False, "calibration/prediction")
    require(adm_decision["credible_minimal_parameter_path_exists"] is True, "minimal path")

    require(
        conditional["status"] == "CONTROLLED_EMPIRICAL_H_GATE_EXECUTION_FORMULA_BUILT_NOT_SELECTED",
        "conditional status",
    )
    cal = conditional["calibration_lane"]
    require(cal["primitive_id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(cal["prediction_status_of_lambda_H_if_calibrated_here"] == "calibration_not_prediction", "prediction status")
    require(cal["required_value_from_external_postcheck"] == required, "conditional required")
    post = conditional["execution_postcheck_not_source"]
    require(post["lambda_if_R_H_RG_equals_1"] < post["external_lambda_Mt_coordinate"], "conditional R=1")
    require(abs(post["absolute_residual_at_required_value"]) < 1e-14, "conditional residual")
    effect = conditional["source_row_effect_if_policy_later_admitted"]
    require(effect["conditional_K_threshold_Omega_H_lambda_executable"] is True, "conditional K executable")
    require(effect["strict_selected_K_threshold_Omega_H_lambda_emitted_now"] is False, "strict K emitted")
    require(effect["accepted_selected_K_source_row_count_now"] == 9, "conditional selected K count")
    require(effect["conditional_parameterized_K_row_count"] == 10, "conditional K count")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_POLICY_SPLIT_CLOSED_STRICT_SOURCE_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    for key in [
        "strict_H_threshold_RG_operator_search_closed",
        "existing_one_primitive_reuse_rechecked",
        "H_threshold_universal_primitive_policy_matrix_built",
        "controlled_empirical_H_gate_formula_built",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "strict_H_threshold_RG_operator_emitted",
        "existing_one_primitive_closes_H_threshold",
        "H_threshold_universal_primitive_selected_now",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    conseq = hk_gate["conditional_minimal_parameter_consequent"]
    require(conseq["if_UP_RET_OVERLAP_HRG_admitted_and_calibrated"] is True, "conditional antecedent")
    require(conseq["conditional_parameterized_K_row_count"] == 10, "conditional K")
    require(conseq["lambda_H_prediction_claim_allowed"] is False, "prediction overclaim")
    require(conseq["strict_no_knob_claim_allowed"] is False, "no-knob overclaim")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_HTHRESHOLD_RG_SOURCE_THEOREM_OR_MINIMAL_PRIMITIVE_CALIBRATION_RUN",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "existing one-primitive physical bridge rechecked and refused as hidden H threshold multiplier",
        "H-threshold universal primitive admission matrix built under UP/B23 policy",
        "controlled empirical H-gate execution formula built with exact required value",
        "claim boundary fixed: calibration is not prediction and primitive closure is not no-knob",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H-sector threshold/RG source theorem for R_H^RG",
        "or explicit admission/calibration of UP-RET-OVERLAP.HRG before replay",
        "cross-use prediction audit for any admitted H-threshold primitive",
        "selected K_threshold.Omega_H.lambda at strict source tier",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "strict charged `K_threshold` rows: `9/10`",
        "required `UP-RET-OVERLAP.HRG=",
        "`lambda_H` is not a prediction",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H threshold/RG policy split closed; strict source row remains open; "
        "minimal-parameter calibration lane is exact but not no-knob."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
