"""Audit RO family-selector source theorem and refreshed payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ROFamilySelectorSourceTheorem_or_NonHiggsPredictionMap_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

FAMILY_THEOREM = BASE / "ro_family_selector_source_theorem.packet.json"
FULL_PAYLOAD = BASE / "ro_full_payload_after_family_selector.packet.json"
NONHIGGS_ATTEMPT = BASE / "ro_nonhiggs_prediction_map_attempt_after_selector.packet.json"
UNIVERSAL_GATE = BASE / "ro_universal_admission_gate_after_selector.packet.json"
CUTSET = BASE / "next_cutset_after_ro_family_selector_theorem.packet.json"

STATUS = (
    "MTT_SELECTED_ROFAMILYSELECTORSOURCETHEOREM_OR_NONHIGGSPREDICTIONMAP_"
    "FAMILY_SELECTOR_CLOSED_VALUE_MAP_OPEN"
)
NEXT = "MTT_Selected_ROValueSource_or_NonHiggsMapExecution_v1"
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
    family = load(FAMILY_THEOREM)
    full_payload = load(FULL_PAYLOAD)
    nonhiggs = load(NONHIGGS_ATTEMPT)
    gate = load(UNIVERSAL_GATE)
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
        "RO_family_selector_source_selected",
        "RO_provenance_certificate_closed",
        "UP_RET_OVERLAP_HRG_H_only_empirical",
        "conditional_empirical_H_K_layer_10_of_10",
        "strict_source_tier_9_of_10",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "RO_family_selector_HRG_specialization_selected",
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
    require(nums["source_selected_payload_count"] == 2, "source payload count")
    require(nums["strict_source_payload_count_excluding_provenance"] == 1, "strict source count")
    require(nums["accepted_nonHiggs_map_count"] == 0, "accepted map count")
    require(nums["nonHiggs_prediction_count"] == 0, "prediction count")
    require(nums["charged_strict_Lrowlocal_row_count"] == 9, "charged row count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RO_family_selector_source_selected"] is True, "cert selector")
    require(cert["RO_family_selector_HRG_specialization_selected"] is False, "cert HRG specialization")
    require(cert["RO_value_source_derived"] is False, "cert value")
    require(cert["accepted_nonHiggs_map_count"] == 0, "cert maps")
    require(cert["nonHiggs_prediction_count"] == 0, "cert predictions")
    require(cert["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "cert universal")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no knob")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["observed_data_used_as_selector"] is False, "cert observed selector")
    require(cert["target_fitting_used"] is False, "cert target fitting")

    require(family["id"] == "RO.family_selector", "family id")
    require(family["status"] == "RO_FAMILY_SELECTOR_SOURCE_SELECTED_AS_FAMILY_CLASS", "family status")
    require(family["source_selected"] is True, "family selected")
    require(family["closure_claimed"] is True, "family closure")
    require(family["theorem"]["proved"] is True, "theorem proved")
    require(family["theorem"]["name"] == "ROFamilySelectorSourceTheorem", "theorem name")
    scope = family["selected_scope"]
    require(scope["primitive_class"] == "UP-RET-OVERLAP", "primitive class")
    require(scope["family_class_selected"] is True, "family class selected")
    require(scope["charged_sectors_selected"] == ["u", "d", "e"], "charged sectors")
    require(scope["H_sector_specialization_selected"] is False, "H specialization")
    require(scope["HRG_numeric_value_source_selected"] is False, "HRG source")
    require(scope["nonHiggs_prediction_map_selected"] is False, "nonHiggs map selected")
    support = family["source_support"]
    require(support["same_source_dynamic_packet_validates"] is True, "same-source validates")
    require(support["retarded_overlap_pairing_proved"] is True, "pairing proved")
    require(support["charged_strict_Lrowlocal_row_count"] == 9, "support charged rows")
    require(
        support["selected_retarded_overlap_pairing_status"]
        == "CHARGED_RETARDED_OVERLAP_EQUALS_SELECTED_H1_SPECTRAL_PAIRING",
        "pairing status",
    )
    require(
        support["same_source_dynamic_matter_overlap_status"]
        == "SAME_SOURCE_DYNAMIC_MATTER_OVERLAP_PACKET_VALIDATES",
        "same-source status",
    )
    for phrase in [
        "Family-class selection is not HRG value selection.",
        "Charged retarded-overlap rows do not select the H/lambda threshold multiplier.",
        "No non-Higgs map currently consumes UP-RET-OVERLAP.HRG.",
        "Calibrating HRG on lambda_H still forbids lambda_H prediction credit.",
    ]:
        require(phrase in family["nonpromotion_boundaries"], f"boundary missing {phrase}")

    require(
        full_payload["status"] == "RO_FULL_PAYLOAD_BUILT_FAMILY_SELECTOR_SOURCE_CLOSED_VALUE_MAP_OPEN",
        "full payload status",
    )
    require(full_payload["all_payload_slots_filled"] is True, "slots filled")
    require(full_payload["all_required_payloads_source_selected"] is False, "all source selected")
    require(full_payload["source_selected_payload_count"] == 2, "full source count")
    require(full_payload["strict_source_payload_count_excluding_provenance"] == 1, "full strict count")
    require(full_payload["HRG_numeric_specialization_source_selected"] is False, "full HRG source")
    require(full_payload["nonHiggs_prediction_count"] == 0, "full predictions")
    rows = {row["id"]: row for row in full_payload["payload_rows"]}
    require(rows["RO.family_selector"]["source_selected"] is True, "row selector")
    require(rows["RO.value_source"]["source_selected"] is False, "row value")
    require(rows["RO.H_sector_map"]["source_selected"] is False, "row H")
    require(rows["RO.nonHiggs_sector_map"]["source_selected"] is False, "row nonHiggs")
    require(rows["RO.nonHiggs_prediction_evaluator"]["source_selected"] is False, "row evaluator")
    require(rows["RO.provenance_certificate"]["source_selected"] is True, "row provenance")

    require(
        nonhiggs["status"] == "RO_NONHIGGS_PREDICTION_MAP_REATTEMPTED_AFTER_SELECTOR_ZERO_ACCEPTED",
        "nonHiggs status",
    )
    require(nonhiggs["family_selector_source_selected"] is True, "nonHiggs selector")
    require(nonhiggs["source_selected"] is False, "nonHiggs source")
    require(nonhiggs["tested_map_count"] == 4, "tested maps")
    require(nonhiggs["accepted_crossuse_map_count"] == 0, "accepted maps")
    for row in nonhiggs["map_rows"]:
        require(row["family_selector_available_now"] is True, f"selector available {row['domain']}")
        require(row["same_HRG_primitive_map_available"] is False, f"HRG map {row['domain']}")
        require(row["accepted_as_crossuse_map"] is False, f"accepted {row['domain']}")
        require(row["prediction_emitted_without_retuning"] is False, f"prediction {row['domain']}")
        require("blocking_reason_after_selector" in row, f"after-selector blocker {row['domain']}")
    for key in [
        "accepted_RO_nonHiggs_sector_map",
        "nonHiggs_prediction_emitted",
        "crossuse_prediction_passed",
        "UP_RET_OVERLAP_HRG_universal_admitted",
    ]:
        require(nonhiggs["decision"][key] is False, f"nonHiggs decision {key}")

    require(gate["status"] == "RO_UNIVERSAL_ADMISSION_GATE_FAMILY_SELECTED_HRG_NOT_ADMITTED", "gate status")
    require(gate["family_selector_source_selected"] is True, "gate family")
    require(gate["value_source_derived"] is False, "gate value")
    require(gate["nonHiggs_prediction_emitted"] is False, "gate prediction")
    require(gate["UP_RET_OVERLAP_family_class_selected"] is True, "gate class")
    require(gate["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "gate admitted")
    for phrase in [
        "HRG numeric specialization is calibrated, not source-derived.",
        "No non-Higgs prediction uses the same HRG value without retuning.",
        "The H-sector map remains empirical/conditional rather than strict source.",
    ]:
        require(phrase in gate["admission_failure_reasons"], f"gate reason {phrase}")

    require(cutset["status"] == "NEXT_FRONTIER_RO_VALUE_SOURCE_OR_NONHIGGS_MAP_EXECUTION", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "RO.family_selector source-selected at retarded-overlap family-class level",
        "full RO payload rebuilt after selector theorem",
        "non-Higgs prediction map reattempted after selector theorem",
        "universal admission gate replayed and still rejects HRG",
        "provenance certificate updated after selector theorem",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "source-derived RO.value_source or strict R_H^RG",
        "strict source-selected RO.H_sector_map",
        "accepted RO.nonHiggs_sector_map using HRG specialization",
        "non-Higgs prediction emitted without retuning",
        "universal admission of UP-RET-OVERLAP.HRG",
        "strict selected K_threshold.Omega_H.lambda",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "`RO.family_selector` is now source-selected",
        "family-class level",
        "does **not** select the HRG",
        "`0` accepted maps",
        "`0` predictions",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: RO family selector source theorem closed at family-class level; "
        "HRG value/non-Higgs prediction remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
