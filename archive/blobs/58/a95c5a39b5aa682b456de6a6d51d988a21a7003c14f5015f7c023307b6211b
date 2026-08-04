"""Audit strict R_H^RG source construction / independent validation oracle packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictrhrgsourceconstruction_or_independentvalidationoracle"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictRHRGSourceConstruction_or_IndependentValidationOracle_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

GATE_EXECUTION = BASE / "strict_rhrg_source_gate_execution.packet.json"
ORACLE_RANK = BASE / "independent_validation_oracle_rank_test.packet.json"
INVARIANT_REPLAY = BASE / "expanded_finite_invariant_source_search_replay.packet.json"
CUTSET = BASE / "next_cutset_after_strict_rhrg_oracle_execution.packet.json"

STATUS = (
    "MTT_SELECTED_STRICTRHRGSOURCECONSTRUCTION_OR_INDEPENDENTVALIDATIONORACLE_"
    "EXECUTED_STRICT_SOURCE_AND_ORACLE_OPEN"
)
NEXT = "MTT_Selected_RHRGDeterminantIndexCandidate_or_ExternalValidationTarget_v1"
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
    gates = load(GATE_EXECUTION)
    oracle = load(ORACLE_RANK)
    invariant = load(INVARIANT_REPLAY)
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
    require(decision["controlled_internal_validation_remains_valid"] is True, "controlled still valid")
    for key in [
        "strict_R_H_RG_source_constructed",
        "all_strict_R_H_RG_gates_satisfied",
        "independent_validation_oracle_emitted",
        "expanded_invariant_exact_identity_found",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(nums["controlled_validation_row_count"] == 3, "row count")
    require(nums["independent_validation_rank"] == 0, "independent rank")
    require(nums["row_family_rank_after_dividing_by_HRG"] == 1, "row family rank")
    require(nums["accepted_strict_source_count"] == 0, "strict count")
    require(nums["best_expanded_invariant_relative_error"] > 0.0, "invariant exact overclaim")
    require(nums["previous_best_invariant_relative_error"] > 0.0, "previous invariant")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "theorem_proved",
        "minimal_parameter_tier_claimed",
        "controlled_internal_validation_remains_valid",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "strict_R_H_RG_source_constructed",
        "all_strict_R_H_RG_gates_satisfied",
        "independent_validation_oracle_emitted",
        "expanded_invariant_exact_identity_found",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_strict_source_count"] == 0, "cert strict count")
    require(cert["independent_validation_rank"] == 0, "cert rank")

    require(gates["status"] == "STRICT_RHRG_SOURCE_GATES_EXECUTED_NOT_ALL_SATISFIED", "gates status")
    require(gates["decision"]["strict_R_H_RG_source_constructed"] is False, "gates source")
    require(gates["decision"]["all_strict_gates_satisfied"] is False, "gates all")
    require(gates["decision"]["controlled_parameter_tier_available"] is True, "gates controlled")
    require(gates["decision"]["strict_no_knob_credit_allowed"] is False, "gates no-knob")
    require(gates["gate_results"]["selected_matching_scale_mu_match"] is False, "mu_match")
    require(gates["gate_results"]["selected_H_sector_threshold_RG_operator_R_H_RG"] is False, "R_H")
    require(gates["gate_results"]["selected_K_threshold_Omega_H_lambda"] is False, "K_H")
    require(gates["gate_results"]["same_branch_scheme_alignment_with_Omega_H_lambda"] is True, "scheme")
    require_no_selector(gates, "gates")

    require(
        oracle["status"] == "INDEPENDENT_VALIDATION_ORACLE_TEST_EXECUTED_DEPENDENT_ROWS_ONLY",
        "oracle status",
    )
    require(oracle["rank_result"]["declared_HRG_parameter_rank"] == 1, "declared rank")
    require(oracle["rank_result"]["independent_validation_rank"] == 0, "independent rank")
    require(oracle["rank_result"]["row_family_rank_after_dividing_by_HRG"] == 1, "row family rank")
    require(oracle["decision"]["independent_validation_oracle_emitted"] is False, "oracle emitted")
    require(oracle["decision"]["controlled_internal_validation_remains_valid"] is True, "oracle controlled")
    require(oracle["decision"]["counts_for_true_SM_equivalence"] is False, "oracle SM")
    require_no_selector(oracle, "oracle")

    require(
        invariant["status"] == "EXPANDED_FINITE_INVARIANT_REPLAY_EXECUTED_NO_SELECTED_EXACT_IDENTITY",
        "invariant status",
    )
    require(invariant["diagnostic_target_scan_used"] is True, "diagnostic scan")
    require(invariant["decision"]["exact_selected_identity_found"] is False, "invariant exact")
    require(invariant["decision"]["near_miss_promoted"] is False, "near miss")
    require(invariant["decision"]["strict_R_H_RG_source_constructed"] is False, "invariant source")
    for row in invariant["candidate_rows"]:
        require(row["accepted_as_source_identity"] is False, f"invariant accepted {row['formula']}")
    require_no_selector(invariant, "invariant")

    require(
        cutset["status"] == "NEXT_FRONTIER_RHRG_DETERMINANT_INDEX_OR_EXTERNAL_VALIDATION_TARGET",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("strict R_H^RG acceptance contract executed gate-by-gate" in cutset["closed_here"], "cutset closed")
    require("selected determinant/index/RG candidate for R_H^RG" in cutset["still_open"], "cutset open")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "strict accepted source count: `0`",
        "independent validation rank: `0`",
        "Next artifact",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: strict R_H^RG gates and independent oracle test executed; "
        "controlled HRG remains valid but no strict/no-knob promotion is emitted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
