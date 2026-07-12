"""Audit H-sector determinant/RG operator definition or target-independent validation run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HSectorDeterminantRGOperatorDefinition_or_TargetIndependentValidationRun_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

OPERATOR_DEF = BASE / "hsector_determinant_rg_operator_definition.packet.json"
SLOT_EXECUTION = BASE / "hsector_determinant_rg_slot_execution.packet.json"
VALIDATION_RUN = BASE / "target_independent_validation_run.packet.json"
CUTSET = BASE / "next_cutset_after_hsector_determinant_rg_definition.packet.json"

STATUS = (
    "MTT_SELECTED_HSECTORDETERMINANTRGOPERATORDEFINITION_OR_TARGETINDEPENDENTVALIDATIONRUN_"
    "OPERATOR_CONTRACT_DEFINED_VALUE_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_HSectorLogDeterminantKernel_or_SelectedHResponseSpectrum_v1"
HRG = 391.39140285811936
S_BETA = 0.004701083905943647


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    operator_def = load(OPERATOR_DEF)
    slots = load(SLOT_EXECUTION)
    validation = load(VALIDATION_RUN)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["minimal_parameter_tier_claimed"] is True, "minimal tier")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "operator_contract_defined",
        "domain_contract_executable",
        "selected_geometry_domain_slots_closed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "logdet_kernel_executable_now",
        "operator_value_emitted",
        "R_H_RG_selected",
        "target_independent_validation_run_executed",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_R_H_RG_source_count"] == 0, "accepted source count")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG_diagnostic_only"] - HRG) < 1e-12, "HRG")
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-18, "s_beta")
    require(nums["closed_geometry_domain_slot_count"] == nums["geometry_domain_slot_count"], "geometry slots")
    require(nums["missing_value_slot_count"] == nums["value_slot_count"], "value slots")
    require(nums["accepted_R_H_RG_source_count"] == 0, "source count")
    require(nums["accepted_validation_target_count"] == 0, "validation count")
    require(nums["accepted_selected_K_source_row_count"] == 9, "K count")
    require(nums["selected_K_threshold_row_count_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "theorem_proved",
        "minimal_parameter_tier_claimed",
        "operator_contract_defined",
        "domain_contract_executable",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "logdet_kernel_executable_now",
        "operator_value_emitted",
        "R_H_RG_selected",
        "target_independent_validation_run_executed",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_R_H_RG_source_count"] == 0, "cert source count")

    require(operator_def["status"] == "HSECTOR_DETERMINANT_RG_OPERATOR_CONTRACT_DEFINED", "operator status")
    require(operator_def["operator"]["id"] == "R_H^RG(mu_match -> M_t)", "operator id")
    require("logdet_zeta" in operator_def["operator"]["value_rule"], "logdet rule")
    require(operator_def["definition_decision"]["operator_contract_defined"] is True, "operator defined")
    require(operator_def["definition_decision"]["operator_value_emitted"] is False, "operator value")
    require(operator_def["definition_decision"]["R_H_RG_selected"] is False, "operator selected")
    require(operator_def["definition_decision"]["counts_for_no_knob_closure"] is False, "operator no-knob")
    for value in operator_def["selected_inputs_available"].values():
        require(value is True, "selected input missing")
    for value in operator_def["missing_value_inputs"].values():
        require(value is True, "missing value slot overclosed")
    require_no_selector(operator_def, "operator")

    require(slots["status"] == "HSECTOR_DETERMINANT_RG_SLOTS_EXECUTED_VALUE_SPECTRUM_OPEN", "slot status")
    require(slots["slot_table"]["geometry_domain_slots_closed"] == slots["slot_table"]["geometry_domain_slot_count"], "slot geometry")
    require(slots["slot_table"]["value_slots_missing"] == slots["slot_table"]["value_slot_count"], "slot values")
    require(abs(slots["diagnostic_target_value_not_used"] - HRG) < 1e-12, "slot HRG")
    require(slots["execution_decision"]["domain_contract_executable"] is True, "slot domain")
    require(slots["execution_decision"]["logdet_kernel_executable_now"] is False, "slot logdet")
    require(slots["execution_decision"]["target_independent_numeric_validation_executable_now"] is False, "slot validation")
    require(slots["execution_decision"]["strict_R_H_RG_source_constructed"] is False, "slot source")
    require(slots["execution_decision"]["accepted_R_H_RG_source_count"] == 0, "slot count")
    require_no_selector(slots, "slots")

    require(validation["status"] == "TARGET_INDEPENDENT_VALIDATION_NOT_RUN_SOURCE_OPERATOR_OPEN", "validation status")
    require(validation["firstpass_RG_support_classification"]["accepted_for_SM_parity"] is True, "SM parity RG")
    require(validation["firstpass_RG_support_classification"]["accepted_for_true_precision_equivalence"] is False, "precision RG")
    require(validation["firstpass_RG_support_classification"]["accepted_as_no_knob_R_H_RG_source"] is False, "RG source")
    require(validation["validation_targets"]["candidate_target_count"] == 0, "target candidates")
    require(validation["validation_targets"]["accepted_target_count"] == 0, "target accepted")
    require(validation["decision"]["validation_run_executed"] is False, "validation executed")
    require(validation["decision"]["validation_run_blocked_by_missing_source_operator"] is True, "validation blocker")
    require(validation["decision"]["external_targets_imported"] is False, "external targets")
    require_no_selector(validation, "validation")

    require(cutset["status"] == "NEXT_FRONTIER_HSECTOR_LOGDETERMINANT_KERNEL_OR_SELECTED_H_RESPONSE_SPECTRUM", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("H-sector determinant/RG operator contract defined" in cutset["closed_here"], "cutset closed")
    require("selected H_response or F_H second-variation spectrum on B_Huv" in cutset["still_open"], "cutset open")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "operator contract",
        "logdet kernel executable now: `false`",
        "accepted `R_H^RG` source count: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H-sector determinant/RG operator contract is defined; "
        "H_response/logdet value execution and validation remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
