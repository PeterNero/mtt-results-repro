"""Audit RO value-source / non-Higgs map execution packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rovaluesource_or_nonhiggsmapexecution"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ROValueSource_or_NonHiggsMapExecution_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

VALUE_MATRIX = BASE / "ro_value_source_candidate_matrix.packet.json"
VALUE_EXECUTION = BASE / "ro_value_source_execution.packet.json"
NONHIGGS_REPLAY = BASE / "ro_nonhiggs_same_hrg_map_import_replay.packet.json"
MINIMAL_STATUS = BASE / "ro_minimal_parameter_status_after_value_attempt.packet.json"
PAYLOAD_AFTER = BASE / "ro_payload_after_value_source_execution.packet.json"
CUTSET = BASE / "next_cutset_after_ro_value_source_execution.packet.json"

STATUS = (
    "MTT_SELECTED_ROVALUESOURCE_OR_NONHIGGSMAPEXECUTION_"
    "EXECUTED_VALUE_SOURCE_AND_NONHIGGS_MAPS_OPEN"
)
NEXT = "MTT_Selected_HRGUniversalPrimitiveSourceRule_or_QaSU3RetardedMatchingMap_v1"
HRG = 391.39140285811936


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
    matrix = load(VALUE_MATRIX)
    value = load(VALUE_EXECUTION)
    nonhiggs = load(NONHIGGS_REPLAY)
    minimal = load(MINIMAL_STATUS)
    payload = load(PAYLOAD_AFTER)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    require(candidate["theorem"]["name"] == "ROValueSourceOrNonHiggsMapExecutionTheorem", "theorem name")

    decision = candidate["closure_decision"]
    for key in [
        "RO_family_selector_source_selected",
        "RO_value_source_execution_attempted",
        "adjacent_QaSU3_retarded_response_imported",
        "minimal_parameter_H_layer_executable",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "RO_value_source_derived",
        "strict_R_H_RG_source_emitted",
        "same_HRG_nonHiggs_map_accepted",
        "adjacent_QaSU3_import_promotes_HRG",
        "UP_RET_OVERLAP_HRG_admitted_as_universal",
        "RO_nonHiggs_prediction_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG value")
    require(nums["QaSU3_selected_chi_Qa"] == 1.0, "Qa chi")
    require(nums["RO_value_source_candidate_count"] == 5, "candidate count")
    require(nums["accepted_RO_value_source_count"] == 0, "accepted value count")
    require(nums["same_HRG_nonHiggs_tested_map_count"] == 5, "map count")
    require(nums["accepted_same_HRG_nonHiggs_map_count"] == 0, "accepted map count")
    require(nums["source_selected_payload_count"] == 2, "source payload count")
    require(nums["strict_source_payload_count_excluding_provenance"] == 1, "strict payload count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RO_value_source_execution_attempted"] is True, "cert attempted")
    require(cert["RO_value_source_derived"] is False, "cert derived")
    require(cert["strict_R_H_RG_source_emitted"] is False, "cert strict")
    require(cert["accepted_RO_value_source_count"] == 0, "cert accepted value")
    require(cert["same_HRG_nonHiggs_tested_map_count"] == 5, "cert map count")
    require(cert["accepted_same_HRG_nonHiggs_map_count"] == 0, "cert accepted maps")
    require(cert["adjacent_QaSU3_retarded_response_imported"] is True, "cert Qa")
    require(cert["adjacent_QaSU3_import_promotes_HRG"] is False, "cert Qa promotes")
    require(cert["UP_RET_OVERLAP_HRG_admitted_as_universal"] is False, "cert universal")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no knob")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    require(matrix["status"] == "RO_VALUE_SOURCE_CANDIDATE_MATRIX_EXECUTED_ZERO_ACCEPTED", "matrix status")
    require(matrix["family_selector_source_selected"] is True, "matrix family")
    require(matrix["candidate_count"] == 5, "matrix candidates")
    require(matrix["accepted_source_count"] == 0, "matrix accepted")
    require(matrix["support_import_count"] == 1, "matrix support")
    require(matrix["empirical_payload_count"] == 1, "matrix empirical")
    lanes = {row["lane"]: row for row in matrix["rows"]}
    for lane in [
        "strict_R_H_RG_source_operator",
        "controlled_empirical_H_lambda_calibration",
        "declared_UP_RET_OVERLAP_HRG_universal_parameter",
        "adjacent_QaSU3_selected_retarded_trace_response",
        "same_HRG_nonHiggs_map_execution",
    ]:
        require(lane in lanes, f"missing lane {lane}")
        require(lanes[lane]["accepted_as_RO_value_source"] is False, f"lane accepted {lane}")
        require(lanes[lane]["source_selected"] is False, f"lane source {lane}")
    require(lanes["controlled_empirical_H_lambda_calibration"]["empirical_payload"] is True, "empirical lane")
    require(lanes["controlled_empirical_H_lambda_calibration"]["value"] == HRG, "empirical value")
    qa_lane = lanes["adjacent_QaSU3_selected_retarded_trace_response"]
    require(qa_lane["support_import"] is True, "Qa support")
    require(qa_lane["retarded_response_source_shape_selected"] is True, "Qa source shape")
    require(qa_lane["same_HRG_numeric_specialization"] is False, "Qa HRG")
    require(qa_lane["imported_numeric_value"] == 1.0, "Qa value")
    require(qa_lane["source_status"] == "QA_SU3_SELECTED_FINITE_RESPONSE_FUNCTIONAL_CHI_QA_CLOSED_MEASURED_MATCH_OPEN", "Qa status")

    require(value["id"] == "RO.value_source", "value id")
    require(value["status"] == "RO_VALUE_SOURCE_EXECUTED_ZERO_SOURCE_VALUES_HRG_EMPIRICAL_ONLY", "value status")
    require(value["source_selected"] is False, "value selected")
    require(value["source_value_emitted"] is False, "source emitted")
    require(value["strict_R_H_RG_source_emitted"] is False, "strict emitted")
    require(value["empirical_value_available"] is True, "empirical available")
    require(abs(value["value"]["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "value HRG")
    for key in [
        "RO_value_source_derived",
        "strict_R_H_RG_source_emitted",
        "same_HRG_nonHiggs_map_accepted",
        "adjacent_QaSU3_import_promotes_HRG",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "lambda_H_predicted",
    ]:
        require(value["decision"][key] is False, f"value decision false {key}")
    for key in [
        "adjacent_QaSU3_retarded_response_support_imported",
        "empirical_HRG_value_retained",
        "minimal_parameter_H_layer_retained",
    ]:
        require(value["decision"][key] is True, f"value decision true {key}")

    require(nonhiggs["status"] == "RO_NONHIGGS_SAME_HRG_MAP_IMPORT_REPLAYED_ZERO_ACCEPTED", "nonHiggs status")
    require(nonhiggs["family_selector_source_selected"] is True, "nonHiggs family")
    require(nonhiggs["qa_su3_retarded_response_imported"] is True, "nonHiggs Qa")
    require(nonhiggs["tested_map_count"] == 5, "nonHiggs tested")
    require(nonhiggs["accepted_crossuse_map_count"] == 0, "nonHiggs accepted")
    qa_rows = [row for row in nonhiggs["map_rows"] if row["domain"] == "Qa/SU3 finite response normalization"]
    require(len(qa_rows) == 1, "Qa row count")
    qa_row = qa_rows[0]
    require(qa_row["retarded_overlap_source_shape_selected"] is True, "Qa row source shape")
    require(qa_row["same_HRG_numeric_specialization"] is False, "Qa row HRG")
    require(qa_row["same_HRG_primitive_map_available"] is False, "Qa row primitive")
    require(qa_row["prediction_emitted_without_retuning"] is False, "Qa row prediction")
    require(qa_row["accepted_as_crossuse_map"] is False, "Qa row accepted")
    require(qa_row["imported_numeric_value"] == 1.0, "Qa row value")
    for row in nonhiggs["map_rows"]:
        require(row["accepted_as_crossuse_map"] is False, f"accepted map {row['domain']}")
        require(row["prediction_emitted_without_retuning"] is False, f"prediction {row['domain']}")
    for key in [
        "accepted_RO_nonHiggs_sector_map",
        "nonHiggs_prediction_emitted",
        "crossuse_prediction_passed",
        "UP_RET_OVERLAP_HRG_universal_admitted",
    ]:
        require(nonhiggs["decision"][key] is False, f"nonHiggs decision {key}")

    require(minimal["status"] == "RO_MINIMAL_PARAMETER_STATUS_H_ONLY_EXECUTABLE_NOT_UNIVERSAL", "minimal status")
    require(minimal["parameter_under_test"]["id"] == "UP-RET-OVERLAP.HRG", "minimal id")
    require(minimal["parameter_under_test"]["calibrated_value"] == HRG, "minimal value")
    min_decision = minimal["decision"]
    for key in [
        "one_parameter_layer_executable_for_H",
        "within_maximum_live_universal_parameters",
        "declared_once",
        "not_retuned_per_observable",
    ]:
        require(min_decision[key] is True, f"minimal true {key}")
    for key in [
        "shared_across_two_independent_source_paths",
        "one_calibration_makes_rest_predictions",
        "accepted_as_provisional_universal_parameter_now",
        "accepted_as_no_knob_source_value",
    ]:
        require(min_decision[key] is False, f"minimal false {key}")

    require(payload["status"] == "RO_PAYLOAD_AFTER_VALUE_SOURCE_EXECUTION_VALUE_AND_MAP_OPEN", "payload status")
    require(payload["all_payload_slots_filled"] is True, "payload filled")
    require(payload["all_required_payloads_source_selected"] is False, "payload all selected")
    require(payload["source_selected_payload_count"] == 2, "payload source count")
    require(payload["strict_source_payload_count_excluding_provenance"] == 1, "payload strict count")
    require(payload["HRG_numeric_specialization_source_selected"] is False, "payload HRG source")
    require(payload["accepted_value_source_count"] == 0, "payload value count")
    require(payload["accepted_nonHiggs_map_count"] == 0, "payload map count")
    require(payload["nonHiggs_prediction_count"] == 0, "payload predictions")

    require(cutset["status"] == "NEXT_FRONTIER_HRG_SOURCE_RULE_OR_QASU3_RETARDED_MATCHING_MAP", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "RO.value_source candidate matrix executed",
        "adjacent Qa/SU3 selected retarded-response import classified as support only",
        "non-Higgs same-HRG map replay expanded to five lanes with zero accepted maps",
        "minimal-parameter status fixed as H-only executable but not universal",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "selected HRG numeric source rule from determinant/index/RG transport",
        "typed same-HRG Qa/SU3/electroweak matching map",
        "accepted RO.nonHiggs_sector_map using UP-RET-OVERLAP.HRG",
        "universal admission of UP-RET-OVERLAP.HRG",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "Accepted `RO.value_source` rows: `0`.",
        "Accepted same-HRG non-Higgs maps: `0 / 5`.",
        "chi_Qa = Tr_finite(tau^2) * <Pi_tw, G_ret Pi_tw> = 8 * 1/8 = 1",
        "does not promote `UP-RET-OVERLAP.HRG",
        "The one-parameter H layer is",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: RO value-source execution imported Qa/SU3 support but "
        "accepted 0 value sources and 0 same-HRG non-Higgs maps."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
