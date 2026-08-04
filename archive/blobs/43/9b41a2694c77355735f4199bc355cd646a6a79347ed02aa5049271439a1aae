"""Audit HRG cross-use prediction validation / strict R_H^RG source theorem packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRGCrossUsePredictionValidation_or_StrictRHRGSourceTheorem_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

CONTROLLED_VALIDATION = BASE / "controlled_hrg_crossuse_prediction_validation.packet.json"
STRICT_REPLAY = BASE / "strict_rhrg_source_theorem_replay.packet.json"
OBLIGATION = BASE / "strict_source_obligation_matrix.packet.json"
CUTSET = BASE / "next_cutset_after_hrg_crossuse_validation.packet.json"

STATUS = (
    "MTT_SELECTED_HRGCROSSUSEPREDICTIONVALIDATION_OR_STRICTRHRGSOURCETHEOREM_"
    "CONTROLLED_CROSSUSE_VALIDATED_STRICT_RHRG_SOURCE_OPEN"
)
NEXT = "MTT_Selected_StrictRHRGSourceConstruction_or_IndependentValidationOracle_v1"
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
    controlled = load(CONTROLLED_VALIDATION)
    strict = load(STRICT_REPLAY)
    obligation = load(OBLIGATION)
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
        "controlled_crossuse_prediction_validated_internally",
        "same_HRG_parameter_reused_without_retuning",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "strict_R_H_RG_source_emitted",
        "strict_RO_value_source_derived",
        "independent_empirical_validation_supplied_here",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(abs(nums["dynamic_C1_HRG_scaled_A00"] - 12.0 * HRG) < 1e-9, "A00")
    require(abs(nums["dynamic_C1_HRG_scaled_b0"] - 12.0 * HRG) < 1e-9, "b0")
    require(abs(nums["dynamic_C1_HRG_scaled_deltaTheta0"] - HRG) < 1e-12, "deltaTheta")
    require(nums["A00_minus_12_HRG"] == 0.0, "A residual")
    require(nums["b0_minus_12_HRG"] == 0.0, "b residual")
    require(nums["deltaTheta0_minus_HRG"] == 0.0, "theta residual")
    require(nums["best_invariant_search_relative_error"] > 0.0, "near miss promoted")
    require(nums["accepted_strict_source_count"] == 0, "strict count")
    require(nums["controlled_prediction_count"] == 3, "prediction count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "theorem_proved",
        "minimal_parameter_tier_claimed",
        "controlled_crossuse_prediction_validated_internally",
        "same_HRG_parameter_reused_without_retuning",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "strict_R_H_RG_source_emitted",
        "strict_RO_value_source_derived",
        "independent_empirical_validation_supplied_here",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_strict_source_count"] == 0, "cert strict count")
    require(cert["controlled_prediction_count"] == 3, "cert prediction count")

    require(
        controlled["status"] == "CONTROLLED_HRG_CROSSUSE_VALIDATION_EXECUTED_INTERNAL_EXACT_EXTERNAL_OPEN",
        "controlled status",
    )
    require(controlled["measured_calibration_used"] is True, "controlled calibration")
    require(controlled["parameter"]["id"] == "UP-RET-OVERLAP.HRG", "controlled id")
    require(abs(controlled["parameter"]["value"] - HRG) < 1e-12, "controlled value")
    require(controlled["parameter"]["declared_once"] is True, "declared once")
    require(controlled["parameter"]["retuned_per_observable"] is False, "retuned")
    require(controlled["parameter"]["source_derived"] is False, "source overclaim")
    require(controlled["parameter"]["controlled_empirical"] is True, "controlled empirical")
    for row in controlled["validated_predictions"]:
        require(row["residual"] == 0.0, f"prediction residual {row['name']}")
    require(controlled["validation_decision"]["controlled_crossuse_prediction_validated_internally"] is True, "validated")
    require(controlled["validation_decision"]["same_HRG_parameter_reused_without_retuning"] is True, "same HRG")
    require(controlled["validation_decision"]["independent_empirical_validation_supplied_here"] is False, "external validation")
    require(controlled["validation_decision"]["accepted_as_strict_no_knob_source"] is False, "strict source overclaim")
    require(controlled["validation_decision"]["counts_for_true_SM_equivalence"] is False, "SM overclaim")
    require_no_selector(controlled, "controlled")

    require(strict["status"] == "STRICT_RHRG_SOURCE_THEOREM_REPLAYED_NOT_EMITTED", "strict status")
    require(strict["theorem"]["proved"] is True, "strict theorem")
    for route in strict["failed_promotion_routes"]:
        require(route["accepted"] is False, f"route accepted {route['route']}")
    for key in [
        "strict_R_H_RG_source_emitted",
        "strict_RO_value_source_derived",
        "selected_large_threshold_RG_transport_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(strict["strict_decision"][key] is False, f"strict false {key}")
    require_no_selector(strict, "strict")

    require(obligation["status"] == "STRICT_RHRG_SOURCE_OBLIGATION_MATRIX_BUILT", "obligation status")
    require("strict numeric HRG source" in obligation["currently_open"], "obligation strict open")
    require("controlled one-parameter HRG cross-use internally validated" in obligation["currently_closed"], "obligation closed")
    require_no_selector(obligation, "obligation")

    require(
        cutset["status"] == "NEXT_FRONTIER_STRICT_RHRG_SOURCE_OR_INDEPENDENT_VALIDATION_ORACLE",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("controlled HRG cross-use validation executed with exact internal residuals" in cutset["closed_here"], "cutset closed")
    require("strict R_H^RG source construction" in cutset["still_open"], "cutset open")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "controlled one-parameter",
        "Strict accepted sources remain `0`",
        "true SM/no-knob equivalence",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: controlled HRG cross-use validates internally with exact residuals; "
        "strict R_H^RG source and independent validation remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
