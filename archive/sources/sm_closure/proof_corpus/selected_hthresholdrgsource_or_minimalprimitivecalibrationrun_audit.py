"""Audit the H-threshold/RG source attempt or minimal-primitive calibration run."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_ATTEMPT = PACKET_DIR / "strict_h_threshold_rg_source_theorem_attempt.packet.json"
CALIBRATION = PACKET_DIR / "minimal_primitive_calibration_run.packet.json"
EMPIRICAL_GATE = PACKET_DIR / "controlled_empirical_h_k_gate.packet.json"
CROSSUSE = PACKET_DIR / "crossuse_prediction_audit_workorder.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_calibration_run.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_calibration_run.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HThresholdRGSource_or_MinimalPrimitiveCalibrationRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HTHRESHOLDRGSOURCE_OR_MINIMALPRIMITIVECALIBRATIONRUN_"
    "CALIBRATION_LAYER_CLOSED_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGPrimitiveCrossUsePredictionAudit_or_SourceTheoremAttempt_v1"


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
    strict = load(STRICT_ATTEMPT)
    calibration = load(CALIBRATION)
    empirical = load(EMPIRICAL_GATE)
    crossuse = load(CROSSUSE)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict attempt", strict),
        ("calibration", calibration),
        ("empirical gate", empirical),
        ("crossuse", crossuse),
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
    require(data["minimal_parameter_H_calibration_layer_claimed"] is True, "minimal H layer")

    decision = data["closure_decision"]
    for key in [
        "strict_H_threshold_RG_source_theorem_attempted",
        "UP_RET_OVERLAP_HRG_calibration_run_built",
        "UP_RET_OVERLAP_HRG_admitted_empirical_layer",
        "lambda_H_calibrated",
        "controlled_empirical_H_K_layer_built",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "strict_H_threshold_RG_operator_emitted",
        "UP_RET_OVERLAP_HRG_selected_strict_source",
        "lambda_H_predicted",
        "strict_ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "crossuse_prediction_audit_passed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["controlled_empirical_conditional_K_row_count"] == 10, "empirical K count")
    require(decision["strict_accepted_selected_K_source_row_count"] == 9, "strict K count")
    require(decision["strict_selected_K_threshold_row_count_required"] == 10, "strict required")

    nums = data["calibration_numbers"]
    require(nums["UP_RET_OVERLAP_HRG"] > 100, "HRG too small")
    require(nums["lambda_if_R_H_RG_equals_1"] < nums["external_lambda_Mt_coordinate"], "R=1 should fail")
    require(
        math.isclose(
            nums["lambda_if_R_H_RG_equals_required_value"],
            nums["external_lambda_Mt_coordinate"],
            rel_tol=0,
            abs_tol=1e-14,
        ),
        "calibration arithmetic",
    )
    require(abs(nums["residual"]) < 1e-14, "calibration residual")

    require(
        strict["status"] == "STRICT_H_THRESHOLD_RG_SOURCE_THEOREM_ATTEMPTED_NOT_EMITTED",
        "strict status",
    )
    attempt = strict["attempt_result"]
    for key in [
        "selected_R_H_RG_emitted",
        "selected_A_EW_emitted",
        "selected_mu_match_emitted",
        "selected_K_threshold_Omega_H_lambda_emitted",
        "mathematical_impossibility_claimed",
    ]:
        require(attempt[key] is False, f"strict attempt overclosed {key}")

    require(
        calibration["status"] == "UP_RET_OVERLAP_HRG_CALIBRATED_EMPIRICAL_LAYER_NOT_PREDICTION",
        "calibration status",
    )
    primitive = calibration["primitive"]
    require(primitive["id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(primitive["new_universal_parameter_count_in_this_layer"] == 1, "primitive count")
    require(primitive["selected_as_strict_source_parameter"] is False, "primitive strict source")
    require(primitive["admitted_as_controlled_empirical_parameter"] is True, "primitive empirical")
    protocol = calibration["calibration_protocol"]
    require(protocol["calibrating_observable"] == "lambda_H(M_t)", "calibrating observable")
    require(protocol["calibrating_observable_prediction_claim_allowed"] is False, "prediction claim")
    require(protocol["measured_calibration_used"] is True, "measured calibration")
    require(protocol["observed_data_used_as_source_selector"] is False, "source selector")
    require(protocol["retuning_per_observable_allowed"] is False, "retuning")
    boundary = calibration["claim_boundary"]
    require(boundary["strict_no_knob_closure_claimed"] is False, "calibration no-knob")
    require(boundary["lambda_H_predicted"] is False, "lambda predicted")
    require(boundary["lambda_H_calibrated"] is True, "lambda calibrated")
    require(boundary["minimal_parameter_H_layer_closed"] is True, "minimal H layer closed")
    require(boundary["full_SM_closure_claimed"] is False, "full SM overclaim")

    require(
        empirical["status"] == "CONTROLLED_EMPIRICAL_H_K_GATE_CONDITIONAL_10_OF_10_STRICT_9_OF_10",
        "empirical status",
    )
    strict_tier = empirical["strict_source_tier"]
    require(strict_tier["accepted_selected_K_source_row_count"] == 9, "empirical strict K count")
    require(strict_tier["K_threshold_Omega_H_lambda_emitted"] is False, "empirical strict K")
    require(strict_tier["ten_K_antecedent_satisfied"] is False, "empirical ten K")
    empirical_tier = empirical["controlled_empirical_tier"]
    require(empirical_tier["UP_RET_OVERLAP_HRG_admitted_as_calibrated_parameter"] is True, "empirical primitive")
    require(empirical_tier["conditional_parameterized_K_row_count"] == 10, "empirical conditional K")
    require(empirical_tier["H_lambda_calibrated_not_predicted"] is True, "empirical prediction boundary")

    require(
        crossuse["status"] == "CROSSUSE_PREDICTION_AUDIT_REQUIRED_FOR_HRG_PRIMITIVE",
        "crossuse status",
    )
    tested = crossuse["calibrated_primitive_under_test"]
    require(tested["id"] == "UP-RET-OVERLAP.HRG", "crossuse primitive")
    require(tested["calibrated_value"] == nums["UP_RET_OVERLAP_HRG"], "crossuse value")
    require(tested["forbidden_prediction_credit"] == "lambda_H(M_t)", "forbidden credit")
    require(len(crossuse["required_prediction_set_before_credibility_upgrade"]) >= 3, "prediction set")
    cross_decision = crossuse["credibility_decision"]
    require(cross_decision["crossuse_prediction_audit_passed_now"] is False, "crossuse passed")
    require(cross_decision["H_only_fit_quarantined"] is True, "H-only quarantine")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_STRICT_9_OF_10_EMPIRICAL_H_LAYER_BUILT",
        "H K status",
    )
    require(hk_gate["strict_source_tier"]["accepted_selected_K_source_row_count"] == 9, "H K strict")
    require(hk_gate["controlled_empirical_tier"]["conditional_parameterized_K_row_count"] == 10, "H K empirical")
    require(hk_gate["controlled_empirical_tier"]["H_lambda_calibrated_not_predicted"] is True, "H K prediction")
    require(hk_gate["controlled_empirical_tier"]["full_SM_closure_claimed"] is False, "H K full SM")
    h_row = hk_gate["H_row"]
    require(h_row["strict_H_threshold_RG_source_theorem_attempted"] is True, "H row strict attempt")
    require(h_row["strict_H_threshold_RG_operator_emitted"] is False, "H row strict operator")
    require(h_row["UP_RET_OVERLAP_HRG_calibration_run_built"] is True, "H row calibration")
    require(h_row["UP_RET_OVERLAP_HRG_selected_strict_source"] is False, "H row strict primitive")
    require(h_row["controlled_empirical_H_layer_built"] is True, "H row empirical layer")

    require(
        cutset["status"] == "NEXT_FRONTIER_HRG_CROSSUSE_PREDICTION_AUDIT_OR_SOURCE_THEOREM",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "strict R_H^RG source theorem attempted and still not emitted",
        "UP-RET-OVERLAP.HRG calibrated exactly at controlled empirical tier",
        "controlled empirical H K layer built as conditional 10/10",
        "lambda_H prediction credit explicitly forbidden for the calibration observable",
        "cross-use prediction audit workorder built",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "strict selected R_H^RG source theorem",
        "strict selected K_threshold.Omega_H.lambda",
        "cross-use prediction audit for UP-RET-OVERLAP.HRG",
        "non-Higgs threshold/RG source map using the same calibrated primitive",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "controlled empirical H calibration layer: built",
        "conditional empirical H K layer is now `10/10`",
        "strict source tier remains `9/10`",
        "`lambda_H` is calibration, not prediction",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: minimal H-threshold calibration layer built; strict no-knob H source "
        "and cross-use prediction audit remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
