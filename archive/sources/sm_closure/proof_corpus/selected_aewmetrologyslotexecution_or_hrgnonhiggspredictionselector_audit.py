"""Audit A_EW metrology-slot execution / HRG non-Higgs selector packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AEWMetrologySlotExecution_or_HRGNonHiggsPredictionSelector_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

AEW_EXECUTION = BASE / "aew_metrology_slot_execution.packet.json"
BURDEN = BASE / "aew_hrg_burden_equivalence_diagnostic.packet.json"
HRG_SELECTOR = BASE / "hrg_nonhiggs_prediction_selector_execution.packet.json"
NEXT_PRIORITY = BASE / "next_priority_after_dual_execution.packet.json"
CUTSET = BASE / "next_cutset_after_aew_hrg_selector_execution.packet.json"

STATUS = (
    "MTT_SELECTED_AEWMETROLOGYSLOTEXECUTION_OR_HRGNONHIGGSPREDICTIONSELECTOR_"
    "EXECUTED_ZERO_SOURCE_VALUES_ALPHA_SELECTOR_PRIORITIZED"
)
NEXT = "MTT_Selected_Alpha1HRGSelector_or_AEWMetrologyValueSourceTheorem_v1"
S_BETA = 0.004701083905943647
AEW = 0.0685013467625
LAMBDA_DTERM = 0.00032203057880065373
LAMBDA_MT = 0.12604
HRG = 391.39140285811936
REQ_AEW = 26.810838207045368


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
    aew = load(AEW_EXECUTION)
    burden = load(BURDEN)
    hrg_selector = load(HRG_SELECTOR)
    next_priority = load(NEXT_PRIORITY)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")
    require(
        candidate["theorem"]["name"] == "AEWMetrologySlotExecutionOrHRGNonHiggsPredictionSelectorTheorem",
        "theorem name",
    )
    require(candidate["theorem"]["proved"] is True, "theorem proved")

    decision = candidate["closure_decision"]
    for key in [
        "AEW_metrology_slot_execution_closed",
        "external_WZH_rows_available",
        "AEW_HRG_burden_equivalence_diagnostic_built",
        "HRG_nonHiggs_prediction_selector_execution_closed",
        "alpha_source_strength_prioritized",
        "dynamic_C1_retained_as_second_selector",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_A_EW_value_emitted",
        "selected_mu_match_value_emitted",
        "selected_threshold_RG_transport_emitted",
        "external_WZH_rows_promoted_to_source",
        "burden_equivalence_accepted_as_source",
        "same_HRG_nonHiggs_prediction_emitted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "K_threshold_Omega_H_lambda_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["selected_metrology_source_slot_count"] == 0, "metrology source slots")
    require(decision["eligible_HRG_selector_count"] == 2, "eligible selectors")
    require(decision["accepted_HRG_selector_count"] == 0, "accepted selectors")

    nums = candidate["key_numbers"]
    require(abs(nums["s_beta"] - S_BETA) < 1e-18, "s_beta")
    require(abs(nums["A_EW_Mt_external"] - AEW) < 1e-15, "A_EW")
    require(abs(nums["A_EW_recomputed_from_g2_gY"] - AEW) < 1e-15, "A_EW recompute")
    require(nums["A_EW_recompute_residual"] == 0.0, "A_EW residual")
    require(abs(nums["lambda_Dterm_Mt_external_AEW_times_selected_sbeta"] - LAMBDA_DTERM) < 1e-18, "lambda dterm")
    require(abs(nums["lambda_Mt_external_coordinate"] - LAMBDA_MT) < 1e-15, "lambda Mt")
    require(abs(nums["computed_HRG_burden"] - HRG) < 1e-12, "computed HRG")
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(nums["burden_equivalence_residual"] == 0.0, "burden residual")
    require(abs(nums["required_A_EW_to_match_external_lambda_Mt"] - REQ_AEW) < 1e-12, "required A_EW")
    require(nums["accepted_external_wzh_coordinate_rows"] == 5, "WZH rows")
    require(nums["accepted_selected_Rtheta_source_rows"] == 0, "Rtheta rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "AEW_metrology_slot_execution_closed",
        "external_WZH_rows_available",
        "AEW_HRG_burden_equivalence_diagnostic_built",
        "HRG_nonHiggs_prediction_selector_execution_closed",
        "alpha_source_strength_prioritized",
        "dynamic_C1_retained_as_second_selector",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "selected_A_EW_value_emitted",
        "selected_mu_match_value_emitted",
        "selected_threshold_RG_transport_emitted",
        "external_WZH_rows_promoted_to_source",
        "burden_equivalence_accepted_as_source",
        "same_HRG_nonHiggs_prediction_emitted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "K_threshold_Omega_H_lambda_emitted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["selected_metrology_source_slot_count"] == 0, "cert metrology slots")
    require(cert["eligible_HRG_selector_count"] == 2, "cert eligible selectors")
    require(cert["accepted_HRG_selector_count"] == 0, "cert accepted selectors")

    require(aew["status"] == "AEW_METROLOGY_SLOT_EXECUTED_ZERO_SELECTED_SOURCE_VALUES", "A_EW status")
    require(aew["decision"]["AEW_metrology_slot_execution_closed"] is True, "A_EW closed")
    require(aew["decision"]["selected_metrology_source_slot_count"] == 0, "A_EW slot count")
    require(aew["decision"]["external_WZH_rows_available"] is True, "WZH available")
    require(aew["decision"]["external_WZH_rows_promoted_to_source"] is False, "WZH source")
    require(aew["decision"]["K_threshold_Omega_H_lambda_emitted"] is False, "K row")
    require(len(aew["executed_slots"]) == 3, "executed slots")
    for row in aew["executed_slots"]:
        require(row["executed"] is True, f"slot executed {row['slot']}")
        require(row["selected_source_value_emitted"] is False, f"slot selected {row['slot']}")
        require(row["accepted_as_source"] is False, f"slot source {row['slot']}")
    require(aew["external_coordinate_rows"]["accepted_external_wzh_coordinate_row_count"] == 5, "WZH accepted")
    require(aew["external_coordinate_rows"]["accepted_selected_Rtheta_source_row_count"] == 0, "WZH source rows")

    require(burden["status"] == "AEW_HRG_BURDEN_EQUIVALENCE_DIAGNOSTIC_BUILT_NOT_SOURCE", "burden status")
    vals = burden["values"]
    require(abs(vals["computed_HRG_burden"] - HRG) < 1e-12, "burden HRG")
    require(abs(vals["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "burden UP")
    require(vals["ratio_residual"] == 0.0, "burden residual")
    require(burden["interpretation"]["accepted_as_source_row"] is False, "burden source")
    require(burden["interpretation"]["accepted_as_nonHiggs_prediction"] is False, "burden prediction")

    require(hrg_selector["status"] == "HRG_NONHIGGS_SELECTOR_EXECUTED_ALPHA_PRIORITY_ZERO_ACCEPTED", "selector status")
    sel_decision = hrg_selector["decision"]
    require(sel_decision["HRG_nonHiggs_prediction_selector_execution_closed"] is True, "selector closed")
    require(sel_decision["eligible_selector_count"] == 2, "selector eligible")
    require(sel_decision["accepted_selector_count"] == 0, "selector accepted")
    require(sel_decision["alpha_source_strength_prioritized"] is True, "alpha priority")
    require(sel_decision["dynamic_C1_retained_as_second_selector"] is True, "dynamic fallback")
    require(sel_decision["charged_threshold_rows_rejected_as_selector"] is True, "charged rejected")
    require(sel_decision["generic_nonHiggs_threshold_rejected_until_typed_consumer_exists"] is True, "generic rejected")
    require(sel_decision["RO_value_source_selected"] is False, "RO value")
    require(sel_decision["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "universal HRG")
    require(sel_decision["same_HRG_nonHiggs_prediction_emitted"] is False, "same HRG prediction")
    selector_rows = {row["selector"]: row for row in hrg_selector["selector_rows"]}
    require(selector_rows["alpha_source_strength"]["priority"] == 1, "alpha priority row")
    require(selector_rows["alpha_source_strength"]["eligible_as_nonHiggs_prediction_selector"] is True, "alpha eligible")
    require(selector_rows["alpha_source_strength"]["accepted_now"] is False, "alpha accepted")
    require(selector_rows["dynamic_C1_overlap_value_tensor"]["priority"] == 2, "dynamic priority row")
    require(selector_rows["dynamic_C1_overlap_value_tensor"]["eligible_as_nonHiggs_prediction_selector"] is True, "dynamic eligible")
    require(selector_rows["dynamic_C1_overlap_value_tensor"]["accepted_now"] is False, "dynamic accepted")
    require(selector_rows["charged_scalar_threshold_rows"]["eligible_as_nonHiggs_prediction_selector"] is False, "charged eligible")
    require(selector_rows["generic_nonHiggs_threshold_RG"]["eligible_as_nonHiggs_prediction_selector"] is False, "generic eligible")

    require(next_priority["status"] == "NEXT_PRIORITY_ALPHA1_HRG_SELECTOR_OR_AEW_METROLOGY_VALUE_SOURCE", "priority")
    require(next_priority["decision"]["next_required_artifact"] == NEXT, "priority next")
    require(next_priority["decision"]["alpha1_selector_chosen_as_primary_next"] is True, "priority alpha")
    require(next_priority["decision"]["aew_value_source_retained_parallel"] is True, "priority aew")
    require(next_priority["decision"]["dynamic_C1_selector_retained_fallback"] is True, "priority dynamic")

    require(cutset["status"] == "NEXT_FRONTIER_ALPHA1_HRG_SELECTOR_OR_AEW_METROLOGY_VALUE_SOURCE", "cutset")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "A_EW metrology slots executed against current WZH/external and source tiers",
        "A_EW/HRG diagnostic burden equivalence recorded",
        "alpha/source-strength selected as primary next HRG non-Higgs selector lane",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "selected A_EW source value",
        "selected alpha1 source-strength normalization value or typed BN retarded derivative",
        "same-HRG alpha/source-strength prediction without retuning",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "A_EW Slot Execution",
        "Burden Equivalence Diagnostic",
        "lambda_Mt / (A_EW*s_beta) = 391.39140285811936",
        "1. alpha/source-strength",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: A_EW slots executed with zero selected source values; "
        "HRG burden diagnostic matches exactly; alpha/source-strength is the primary selector."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
