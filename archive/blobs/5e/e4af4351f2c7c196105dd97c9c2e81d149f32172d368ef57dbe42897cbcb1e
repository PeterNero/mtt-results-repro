"""Audit retarded-overlap family selector / HRG source payload fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RetardedOverlapFamilySelector_or_HRGSourcePayloadFill_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

RO_SELECTOR = BASE / "ro_family_selector.packet.json"
RO_VALUE = BASE / "ro_value_source.packet.json"
RO_H_MAP = BASE / "ro_h_sector_map.packet.json"
RO_NONHIGGS_MAP = BASE / "ro_nonhiggs_sector_map.packet.json"
RO_EVALUATOR = BASE / "ro_nonhiggs_prediction_evaluator.packet.json"
RO_PROVENANCE = BASE / "ro_provenance_certificate.packet.json"
FILL_MATRIX = BASE / "ro_payload_fill_matrix.packet.json"
CUTSET = BASE / "next_cutset_after_ro_payload_fill.packet.json"

STATUS = (
    "MTT_SELECTED_RETARDEDOVERLAPFAMILYSELECTOR_OR_HRGSOURCEPAYLOADFILL_"
    "PAYLOADS_FILLED_SOURCE_SELECTOR_OPEN"
)
NEXT = "MTT_Selected_ROFamilySelectorSourceTheorem_or_NonHiggsPredictionMap_v1"
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
    selector = load(RO_SELECTOR)
    value = load(RO_VALUE)
    h_map = load(RO_H_MAP)
    nonhiggs = load(RO_NONHIGGS_MAP)
    evaluator = load(RO_EVALUATOR)
    provenance = load(RO_PROVENANCE)
    matrix = load(FILL_MATRIX)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")

    decision = candidate["closure_decision"]
    for key in [
        "all_six_RO_payload_slots_filled",
        "RO_provenance_certificate_closed",
        "UP_RET_OVERLAP_HRG_H_only_empirical",
        "conditional_empirical_H_K_layer_10_of_10",
        "strict_source_tier_9_of_10",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "RO_family_selector_source_selected",
        "RO_value_source_derived",
        "RO_H_sector_map_strict_source_selected",
        "RO_nonHiggs_sector_map_accepted",
        "RO_nonHiggs_prediction_emitted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG value")
    require(nums["payload_slots_required"] == 6, "required slots")
    require(nums["payload_slots_filled"] == 6, "filled slots")
    require(nums["source_selected_payload_count"] == 1, "source selected count")
    require(nums["strict_source_payload_count_excluding_provenance"] == 0, "strict source count")
    require(nums["nonHiggs_prediction_count"] == 0, "prediction count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RO_payload_slots_filled"] == 6, "cert slots")
    require(cert["RO_provenance_certificate_closed"] is True, "cert provenance")
    require(cert["strict_source_payload_count_excluding_provenance"] == 0, "cert strict count")
    require(cert["nonHiggs_prediction_count"] == 0, "cert predictions")
    require(cert["H_only_empirical_layer_retained"] is True, "cert H only")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no knob")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    require(selector["id"] == "RO.family_selector", "selector id")
    require(selector["status"] == "RO_FAMILY_SELECTOR_TYPED_SHELL_FILLED_NOT_SELECTED", "selector status")
    require(selector["payload_kind"] == "typed_shell", "selector kind")
    require(selector["source_selected"] is False, "selector selected")
    require(selector["candidate_selector"]["primitive_class"] == "UP-RET-OVERLAP", "selector class")
    require(selector["candidate_selector"]["specialization"] == "UP-RET-OVERLAP.HRG", "selector specialization")
    require(selector["policy_basis"]["UP_RET_OVERLAP_selected_now"] is False, "selector policy")

    require(value["id"] == "RO.value_source", "value id")
    require(value["status"] == "RO_VALUE_SOURCE_EMPIRICAL_VALUE_FILLED_SOURCE_VALUE_OPEN", "value status")
    require(value["source_selected"] is False, "value selected")
    require(value["empirical_value_available"] is True, "value empirical")
    require(abs(value["value"]["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "value HRG")
    require(value["source_value_emitted"] is False, "source value")
    require(value["strict_R_H_RG_source_emitted"] is False, "strict value")
    require(value["claim_boundary"]["lambda_H_calibrated"] is True, "lambda calibrated")
    require(value["claim_boundary"]["lambda_H_predicted"] is False, "lambda predicted")
    require(value["claim_boundary"]["strict_no_knob_closure_claimed"] is False, "value no knob")

    require(h_map["id"] == "RO.H_sector_map", "H map id")
    require(h_map["status"] == "RO_H_SECTOR_MAP_EMPIRICAL_FILLED_STRICT_SOURCE_OPEN", "H map status")
    require(h_map["source_selected"] is False, "H map selected")
    require(h_map["controlled_empirical_map_filled"] is True, "H map filled")
    require(h_map["strict_H_sector_map_emitted"] is False, "H map strict")
    require(h_map["primitive"]["selected_as_strict_source_parameter"] is False, "H primitive strict")
    require(h_map["gate_effect"]["conditional_parameterized_K_row_count"] == 10, "H K count")
    require(h_map["gate_effect"]["H_lambda_calibrated_not_predicted"] is True, "H lambda")
    require(h_map["gate_effect"]["strict_K_threshold_Omega_H_lambda_emitted"] is False, "H strict K")

    require(nonhiggs["id"] == "RO.nonHiggs_sector_map", "nonHiggs id")
    require(nonhiggs["status"] == "RO_NONHIGGS_SECTOR_MAP_EXECUTED_ZERO_ACCEPTED_MAPS", "nonHiggs status")
    require(nonhiggs["source_selected"] is False, "nonHiggs selected")
    require(nonhiggs["tested_map_count"] == 4, "nonHiggs tested")
    require(nonhiggs["accepted_crossuse_map_count"] == 0, "nonHiggs accepted")
    for row in nonhiggs["map_rows"]:
        require(row["accepted_as_crossuse_map"] is False, f"accepted map {row['domain']}")
        require(row["same_HRG_primitive_map_available"] is False, f"HRG map {row['domain']}")
        require(row["prediction_emitted_without_retuning"] is False, f"prediction {row['domain']}")

    require(evaluator["id"] == "RO.nonHiggs_prediction_evaluator", "evaluator id")
    require(evaluator["status"] == "RO_NONHIGGS_PREDICTION_EVALUATOR_BUILT_ZERO_PREDICTIONS", "evaluator status")
    require(evaluator["source_selected"] is False, "evaluator selected")
    require(evaluator["evaluator_contract"]["must_use_same_HRG_value"] is True, "same HRG")
    require(evaluator["evaluator_contract"]["must_not_recalibrate_on_nonHiggs_target"] is True, "no retune")
    require(evaluator["evaluator_contract"]["lambda_H_forbidden_as_prediction_credit"] is True, "lambda credit")
    require(evaluator["execution_result"]["accepted_nonHiggs_sector_map_count"] == 0, "eval map count")
    require(evaluator["execution_result"]["prediction_count"] == 0, "eval predictions")
    require(evaluator["execution_result"]["crossuse_prediction_passed"] is False, "eval crossuse")
    require(evaluator["execution_result"]["universal_primitive_admitted"] is False, "eval universal")

    require(provenance["id"] == "RO.provenance_certificate", "provenance id")
    require(
        provenance["status"] == "RO_PROVENANCE_CERTIFICATE_CLOSED_FOR_CURRENT_PAYLOAD_FILL",
        "provenance status",
    )
    require(provenance["source_selected"] is True, "provenance selected")
    for key in [
        "calibration/prediction separation",
        "H-only empirical classification",
        "charged-row HRG multiplier prohibition",
        "non-Higgs map count and zero-prediction decision",
        "strict no-knob and true-SM overclaim guard",
    ]:
        require(key in provenance["certificate_closes"], f"provenance close {key}")
    for pid in [
        "RO.family_selector",
        "RO.value_source",
        "RO.H_sector_map",
        "RO.nonHiggs_sector_map",
        "RO.nonHiggs_prediction_evaluator",
        "RO.provenance_certificate",
    ]:
        require(pid in provenance["provenance_ledger"], f"ledger missing {pid}")

    require(matrix["status"] == "RO_PAYLOAD_FILL_MATRIX_BUILT_PROVENANCE_ONLY_SOURCE_SELECTED", "matrix status")
    require(matrix["required_payload_count"] == 6, "matrix required")
    require(matrix["filled_payload_count"] == 6, "matrix filled")
    require(matrix["missing_from_manifest"] == [], "matrix missing")
    require(matrix["source_selected_payload_count"] == 1, "matrix selected")
    require(matrix["strict_source_payload_count_excluding_provenance"] == 0, "matrix strict")
    gate = matrix["gate_decision"]
    require(gate["all_payload_slots_filled_with_current_objects"] is True, "gate filled")
    for key in [
        "all_required_payloads_source_selected",
        "HRG_universal_admitted",
        "strict_H_K_row_closed",
        "nonHiggs_prediction_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(gate[key] is False, f"gate false {key}")

    require(
        cutset["status"] == "NEXT_FRONTIER_RO_FAMILY_SELECTOR_SOURCE_THEOREM_OR_NONHIGGS_MAP",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "all six RO payload slots filled with current strongest objects",
        "RO.provenance_certificate closed for current payload boundary",
        "RO.H_sector_map filled at controlled empirical tier",
        "RO.value_source filled as calibrated value with source gap",
        "RO.nonHiggs_sector_map and evaluator executed with zero accepted predictions",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "source-selected RO.family_selector",
        "source-derived RO.value_source or strict R_H^RG",
        "accepted RO.nonHiggs_sector_map",
        "non-Higgs prediction emitted without retuning",
        "strict selected K_threshold.Omega_H.lambda",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "`RO.family_selector`: typed shell filled, not source-selected.",
        "`RO.value_source`: empirical calibrated value filled",
        "`RO.nonHiggs_sector_map`: executed, `0` accepted maps.",
        "`RO.nonHiggs_prediction_evaluator`: built, `0` predictions.",
        "`RO.provenance_certificate`: closed for the current payload boundary.",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: all six RO payload slots filled; provenance closed; "
        "selector/value/non-Higgs prediction remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
