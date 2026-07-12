"""Audit selected HRG primitive cross-use prediction audit/source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRGPrimitiveCrossUsePredictionAudit_or_SourceTheoremAttempt_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

STRICT = BASE / "strict_hrg_source_theorem_reattempt.packet.json"
CROSSUSE = BASE / "hrg_crossuse_prediction_audit_execution.packet.json"
TARGETS = BASE / "hrg_nonhiggs_target_matrix.packet.json"
POLICY = BASE / "hrg_primitive_policy_decision_after_crossuse.packet.json"
HK_GATE = BASE / "hk_threshold_gate_after_hrg_crossuse_audit.packet.json"
CUTSET = BASE / "next_cutset_after_hrg_crossuse_audit.packet.json"

STATUS = (
    "MTT_SELECTED_HRGPRIMITIVECROSSUSEPREDICTIONAUDIT_OR_SOURCETHEOREMATTEMPT_"
    "EXECUTED_NO_CROSSUSE_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGNonHiggsRetardedOverlapMap_or_StrictSourceTheorem_v1"
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
    strict = load(STRICT)
    crossuse = load(CROSSUSE)
    targets = load(TARGETS)
    policy = load(POLICY)
    hk_gate = load(HK_GATE)
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
        "crossuse_prediction_audit_executed",
        "strict_HRG_source_theorem_reattempted",
        "UP_RET_OVERLAP_HRG_H_only_empirical",
        "conditional_empirical_H_K_layer_10_of_10",
        "strict_source_tier_9_of_10",
        "lambda_H_calibrated",
    ]:
        require(decision[key] is True, f"decision true missing {key}")
    for key in [
        "crossuse_prediction_audit_passed",
        "strict_HRG_source_theorem_emitted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false missing {key}")
    require(decision["accepted_nonhiggs_prediction_target_count"] == 0, "accepted target count")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG value")
    require(nums["accepted_nonhiggs_prediction_target_count"] == 0, "num accepted targets")
    require(nums["tested_nonhiggs_target_count"] == 3, "num tested targets")
    require(nums["controlled_empirical_conditional_K_row_count"] == 10, "empirical K count")
    require(nums["strict_accepted_selected_K_source_row_count"] == 9, "strict K count")

    require(cert["status"] == STATUS, "certificate status")
    require(cert["crossuse_prediction_audit_passed"] is False, "cert crossuse")
    require(cert["strict_HRG_source_emitted"] is False, "cert strict source")
    require(cert["H_only_empirical_layer_retained"] is True, "cert H-only")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    require(strict["status"] == "STRICT_HRG_SOURCE_THEOREM_REATTEMPTED_NOT_EMITTED", "strict status")
    strict_result = strict["result"]
    for key in [
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda_emitted",
        "same_branch_H_sector_determinant_or_index_emitted",
        "selected_matching_surface_mu_match_emitted",
        "mathematical_impossibility_claimed",
    ]:
        require(strict_result[key] is False, f"strict result {key}")

    require(crossuse["status"] == "HRG_CROSSUSE_PREDICTION_AUDIT_EXECUTED_FAILED", "crossuse status")
    audit = crossuse["audit_result"]
    require(audit["crossuse_prediction_audit_executed"] is True, "audit executed")
    require(audit["crossuse_prediction_audit_passed"] is False, "audit passed")
    require(audit["accepted_prediction_target_count"] == 0, "audit target count")
    require(audit["H_only_fit_quarantined"] is True, "audit quarantine")
    require(audit["universal_primitive_admitted"] is False, "audit universal")
    require(audit["strict_no_knob_status_upgraded"] is False, "audit no-knob")
    scope = crossuse["calibration_scope"]
    require(scope["forbidden_prediction_credit"] == "lambda_H(M_t)", "forbidden credit")
    require(scope["lambda_H_predicted"] is False, "lambda prediction")

    require(targets["status"] == "HRG_NONHIGGS_TARGET_MATRIX_EXECUTED_ZERO_ACCEPTED_TARGETS", "targets status")
    require(targets["tested_target_count"] == 3, "tested count")
    require(targets["accepted_prediction_target_count"] == 0, "accepted count")
    target_names = [row["target"] for row in targets["target_results"]]
    for target in [
        "non-Higgs threshold/RG observable",
        "weak-mixing or alpha-sector consistency",
        "charged scalar threshold/prefactor rows",
    ]:
        require(target in target_names, f"target missing {target}")
    for row in targets["target_results"]:
        require(row["same_primitive_source_map_available"] is False, f"map overemitted {row['target']}")
        require(row["predicted_value_emitted_without_retuning"] is False, f"prediction overemitted {row['target']}")
        require(row["passes_crossuse"] is False, f"crossuse overpassed {row['target']}")

    require(policy["status"] == "HRG_PRIMITIVE_CLASSIFIED_H_ONLY_EMPIRICAL_NOT_UNIVERSAL", "policy status")
    require(abs(policy["calibrated_value"] - HRG) < 1e-12, "policy value")
    policy_decision = policy["policy_decision"]
    require(policy_decision["H_only_measured_parameter_interface_ready"] is True, "H-only interface")
    require(policy_decision["universal_parameter_admitted"] is False, "policy universal")
    require(policy_decision["no_knob_parameter_derived"] is False, "policy no-knob")
    require(policy_decision["requires_nonhiggs_map_or_strict_source_theorem"] is True, "policy next")
    for forbidden in [
        "strict no-knob K_threshold.Omega_H.lambda source row",
        "lambda_H prediction claim",
        "universal parameter credibility upgrade",
        "non-Higgs prediction credit",
    ]:
        require(forbidden in policy["forbidden_current_use"], f"forbidden missing {forbidden}")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_EMPIRICAL_10_OF_10_STRICT_9_OF_10_CROSSUSE_FAILED",
        "H K status",
    )
    empirical = hk_gate["controlled_empirical_tier"]
    require(empirical["conditional_parameterized_K_row_count"] == 10, "empirical K")
    require(empirical["crossuse_prediction_audit_required"] is False, "audit still required")
    require(empirical["crossuse_prediction_audit_executed"] is True, "audit not executed")
    require(empirical["crossuse_prediction_audit_passed"] is False, "audit passed in gate")
    require(empirical["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "gate universal")
    require(empirical["UP_RET_OVERLAP_HRG_H_only_empirical"] is True, "gate H-only")
    require(hk_gate["strict_source_tier"]["accepted_selected_K_source_row_count"] == 9, "gate strict K")

    require(cutset["status"] == "NEXT_FRONTIER_HRG_NONHIGGS_MAP_OR_STRICT_SOURCE_THEOREM", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "HRG cross-use prediction audit executed",
        "zero non-Higgs prediction targets accepted",
        "HRG primitive classified as H-only empirical calibration unless upgraded",
        "strict HRG source theorem reattempted and still not emitted",
        "conditional empirical H K layer remains 10/10 but quarantined",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "strict selected R_H^RG source theorem",
        "strict selected K_threshold.Omega_H.lambda",
        "non-Higgs retarded-overlap source map using UP-RET-OVERLAP.HRG",
        "universal primitive credibility upgrade for HRG",
        "lambda_H prediction without calibration",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "Cross-use prediction audit: executed.",
        "Accepted non-Higgs prediction targets: `0 / 3`.",
        "Strict selected `R_H^RG` source theorem: reattempted, still not emitted.",
        "Controlled empirical H K layer: still conditional `10/10`.",
        "Strict source tier: still `9/10`.",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: HRG cross-use audit executed with zero accepted non-Higgs "
        "prediction targets; strict source remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
