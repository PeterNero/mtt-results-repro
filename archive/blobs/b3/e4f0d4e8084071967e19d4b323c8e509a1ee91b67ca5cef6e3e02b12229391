"""Audit HRG consumer value-source / large-threshold transport-map packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRGConsumerValueSource_or_LargeThresholdTransportMap_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

STRICT_REPLAY = BASE / "strict_hrg_value_source_replay_after_dynamic_payload.packet.json"
CONTROLLED_ADMISSION = BASE / "controlled_universal_hrg_parameter_admission.packet.json"
DYNAMIC_C1_MAP = BASE / "dynamic_c1_same_hrg_transport_prediction_map.packet.json"
INVARIANT_SEARCH = BASE / "finite_invariant_hrg_specialization_search.packet.json"
CUTSET = BASE / "next_cutset_after_hrg_consumer_value_source_attack.packet.json"

STATUS = (
    "MTT_SELECTED_HRGCONSUMERVALUESOURCE_OR_LARGETHRESHOLDTRANSPORTMAP_"
    "CONTROLLED_ONE_PARAMETER_TIER_EXECUTED_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGCrossUsePredictionValidation_or_StrictRHRGSourceTheorem_v1"
HRG = 391.39140285811936


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
    strict = load(STRICT_REPLAY)
    controlled = load(CONTROLLED_ADMISSION)
    dynamic = load(DYNAMIC_C1_MAP)
    invariant = load(INVARIANT_SEARCH)
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
        "controlled_RO_value_source_admitted",
        "controlled_dynamic_C1_transport_prediction_map_emitted",
        "UP_RET_OVERLAP_HRG_selected_as_controlled_universal_parameter",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "strict_RO_value_source_derived",
        "strict_R_H_RG_source_emitted",
        "selected_large_threshold_RG_transport_emitted",
        "lambda_H_predicted",
        "finite_invariant_exact_formula_found",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["strict_accepted_RO_value_source_count"] == 0, "strict value count")
    require(decision["strict_same_HRG_nonHiggs_map_count"] == 0, "strict map count")
    require(decision["controlled_RO_value_source_count"] == 1, "controlled value count")
    require(decision["controlled_same_HRG_nonHiggs_map_count"] == 1, "controlled map count")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(nums["strict_accepted_RO_value_source_count"] == 0, "nums strict source")
    require(nums["controlled_RO_value_source_count"] == 1, "nums controlled source")
    require(nums["strict_same_HRG_nonHiggs_map_count"] == 0, "nums strict map")
    require(nums["controlled_same_HRG_nonHiggs_map_count"] == 1, "nums controlled map")
    require(abs(nums["dynamic_C1_HRG_scaled_A00"] - 12.0 * HRG) < 1e-9, "scaled A")
    require(abs(nums["dynamic_C1_HRG_scaled_b0"] - 12.0 * HRG) < 1e-9, "scaled b")
    require(nums["best_invariant_search_relative_error"] > 0.0, "invariant exact overclaim")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "theorem_proved",
        "minimal_parameter_tier_claimed",
        "controlled_RO_value_source_admitted",
        "controlled_dynamic_C1_transport_prediction_map_emitted",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "strict_RO_value_source_derived",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["strict_accepted_RO_value_source_count"] == 0, "cert strict source")
    require(cert["controlled_RO_value_source_count"] == 1, "cert controlled source")
    require(cert["controlled_same_HRG_nonHiggs_map_count"] == 1, "cert controlled map")

    require(
        strict["status"] == "STRICT_HRG_VALUE_SOURCE_REPLAYED_AFTER_DYNAMIC_PAYLOAD_ZERO_ACCEPTED",
        "strict status",
    )
    require(strict["theorem"]["proved"] is True, "strict theorem")
    require(strict["old_rejections_reclassified"]["dynamic_C1_old_missing_payload_reason_retired"] is True, "old blocker")
    require(strict["old_rejections_reclassified"]["dynamic_C1_payload_now_selected"] is True, "dynamic selected")
    require(strict["strict_counts"]["accepted_RO_value_source_count"] == 0, "strict RO count")
    for key in [
        "RO_value_source_derived_strict",
        "strict_R_H_RG_source_emitted",
        "selected_large_threshold_RG_transport_emitted",
        "same_HRG_nonHiggs_map_accepted_strict",
        "strict_no_knob_HRG_source_closed",
    ]:
        require(strict["decision"][key] is False, f"strict decision false {key}")
    require_no_selector(strict, "strict")

    require(
        controlled["status"] == "CONTROLLED_EMPIRICAL_HRG_PARAMETER_ADMITTED_FOR_CROSSUSE_NOT_NOKNOB",
        "controlled status",
    )
    require(controlled["measured_calibration_used"] is True, "controlled calibration")
    primitive = controlled["primitive"]
    require(primitive["id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(abs(primitive["value"] - HRG) < 1e-12, "primitive value")
    require(primitive["declared_once"] is True, "declared once")
    require(primitive["retuned_per_observable"] is False, "retuned")
    require(primitive["new_universal_parameter_count"] == 1, "parameter count")
    require(primitive["source_derived"] is False, "source derived overclaim")
    require(primitive["controlled_empirical"] is True, "controlled empirical")
    require(primitive["lambda_H_prediction_credit_allowed"] is False, "lambda credit")
    require(controlled["legal_boundary"]["RO_value_source_controlled_empirical"] is True, "controlled RO")
    require(controlled["legal_boundary"]["RO_value_source_derived_strict"] is False, "strict RO")
    require(controlled["legal_boundary"]["full_no_knob_closed"] is False, "controlled no-knob")
    require(controlled["decision"]["controlled_RO_value_source_count"] == 1, "controlled count")
    require(controlled["decision"]["strict_source_count_changed"] is False, "strict changed")
    require_no_selector(controlled, "controlled")

    require(dynamic["status"] == "CONTROLLED_SAME_HRG_DYNAMIC_C1_TRANSPORT_MAP_EMITTED", "dynamic status")
    require(dynamic["map"]["parameter_id"] == "UP-RET-OVERLAP.HRG", "dynamic parameter")
    require(dynamic["map"]["same_branch_source_domain"] is True, "same branch")
    require(dynamic["map"]["retuned_for_domain"] is False, "retuned dynamic")
    require(dynamic["input_payload"]["formal_110_total_rows"] == 110, "dynamic rows")
    require(abs(dynamic["predicted_transport_rows"]["HRG_times_A_transpose_A"][0][0] - 12.0 * HRG) < 1e-9, "dynamic A")
    require(abs(dynamic["predicted_transport_rows"]["HRG_times_A_transpose_b"][0] - 12.0 * HRG) < 1e-9, "dynamic b")
    require(dynamic["acceptance"]["accepted_as_controlled_same_HRG_nonHiggs_map"] is True, "dynamic accepted controlled")
    require(dynamic["acceptance"]["accepted_as_strict_no_knob_source_map"] is False, "dynamic strict overclaim")
    require(dynamic["acceptance"]["prediction_emitted_without_retuning"] is True, "dynamic prediction")
    require(dynamic["acceptance"]["independent_empirical_validation_supplied_here"] is False, "dynamic validation")
    require(dynamic["acceptance"]["counts_for_no_knob_derivation"] is False, "dynamic no-knob")
    require_no_selector(dynamic, "dynamic")

    require(
        invariant["status"] == "FINITE_INVARIANT_SEARCH_EXECUTED_NO_EXACT_SELECTED_IDENTITY",
        "invariant status",
    )
    require(invariant["decision"]["exact_selected_formula_found"] is False, "invariant exact")
    require(invariant["decision"]["near_misses_promoted"] is False, "near miss")
    require(invariant["decision"]["strict_HRG_source_theorem_derived"] is False, "strict theorem")
    require(invariant["diagnostics"]["best_candidate_relative_error"] > 0.0, "best exact")
    for row in invariant["candidate_rows"]:
        require(row["accepted_as_source_identity"] is False, f"invariant accepted {row['formula']}")
    require_no_selector(invariant, "invariant")

    require(
        cutset["status"] == "NEXT_FRONTIER_HRG_CROSSUSE_VALIDATION_OR_STRICT_RHRG_SOURCE_THEOREM",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "controlled one-parameter UP-RET-OVERLAP.HRG tier admitted without no-knob credit",
        "typed dynamic-C1 same-HRG transport prediction map emitted without retuning",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed {phrase}")
    for phrase in [
        "strict source-derived R_H^RG or large-threshold transport theorem",
        "independent validation of the dynamic-C1 same-HRG transport prediction",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "Strict Tier",
        "strict accepted RO value sources    0",
        "controlled RO.value_source admitted true",
        "controlled same-HRG maps            1",
        "lambda_H prediction credit          false",
        "No exact selected finite-invariant source identity is found.",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: HRG strict source remains open, but controlled one-parameter "
        "RO.value_source and dynamic-C1 same-HRG transport map are executable."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
