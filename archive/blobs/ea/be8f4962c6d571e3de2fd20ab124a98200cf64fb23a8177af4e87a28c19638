"""Audit finite H functional candidate or direct Herm(2) row emission run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteHFunctionalCandidate_or_DirectHerm2RowEmissionRun_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

RUN = BASE / "finite_h_functional_candidate_emission_run.packet.json"
DIRECT = BASE / "direct_herm2_rows_after_candidate_run.packet.json"
REDUCTION = BASE / "sbeta_radial_phase_reduction.packet.json"
CUTSET = BASE / "next_cutset_after_finite_h_candidate_run.packet.json"

STATUS = (
    "MTT_SELECTED_FINITEHFUNCTIONALCANDIDATE_OR_DIRECTHERM2ROWEMISSIONRUN_"
    "EXECUTED_SBETA_REDUCTION_ONLY_VALUES_OPEN"
)
NEXT = "MTT_Selected_HRadialScalePhaseSource_or_Herm2HessianRows_v1"
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
    run = load(RUN)
    direct = load(DIRECT)
    reduction = load(REDUCTION)
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
        "finite_H_functional_candidate_run_executed",
        "selected_s_beta_polar_angle_closed",
        "Herm2_radial_collapse_closed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_F_H_functional_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_radial_scale_source_emitted",
        "selected_phase_source_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_logdet_value_executed",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_finite_H_functional_count"] == 0, "accepted F_H")
    require(decision["accepted_H_response_source_row_count"] == 0, "accepted H rows")
    require(decision["accepted_R_H_RG_source_count"] == 0, "accepted RHRG")

    nums = candidate["key_numbers"]
    require(nums["candidate_attempt_count"] == 4, "attempt count")
    require(nums["accepted_finite_H_functional_count"] == 0, "accepted count")
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-15, "s_beta")
    require(nums["required_direct_Herm2_row_or_certificate_count"] == 8, "required rows")
    require(nums["emitted_direct_Herm2_row_or_certificate_count"] == 0, "emitted rows")
    require(nums["selected_K_source_rows"] == 9, "K rows")
    require(nums["selected_K_rows_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "finite_H_functional_candidate_run_executed",
        "selected_s_beta_polar_angle_closed",
        "Herm2_radial_collapse_closed",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "selected_F_H_functional_emitted",
        "selected_radial_scale_source_emitted",
        "selected_phase_source_emitted",
        "direct_Herm2_rows_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_finite_H_functional_count"] == 0, "cert F_H")

    require(run["status"] == "FINITE_H_FUNCTIONAL_CANDIDATE_RUN_EXECUTED_NO_ACCEPTED_FUNCTIONAL", "run status")
    require(run["decision"]["candidate_attempt_count"] == 4, "run count")
    require(run["decision"]["accepted_finite_H_functional_count"] == 0, "run accepted")
    require(run["decision"]["only_s_beta_reduction_available"] is True, "s_beta only")
    for key in [
        "selected_F_H_functional_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_nonzero_tracefree_Herm2_hessian_emitted",
        "finite_exactness_or_residual_certificate_emitted",
    ]:
        require(run["decision"][key] is False, f"run false {key}")
    ids = {attempt["candidate_id"] for attempt in run["candidate_attempts"]}
    for candidate_id in [
        "metric_quotient_functional",
        "finite_projection_sbeta_reduction",
        "direct_hquartic_radial_collapse",
        "hym_section_ring_c2_basis",
    ]:
        require(candidate_id in ids, f"missing attempt {candidate_id}")
    for attempt in run["candidate_attempts"]:
        require(attempt["accepted"] is False, f"attempt accepted {attempt['candidate_id']}")
        require(attempt["rejection_reason"], f"attempt reason {attempt['candidate_id']}")
    require_no_selector(run, "run")

    require(direct["status"] == "DIRECT_HERM2_ROWS_STILL_NULL_AFTER_FINITE_H_CANDIDATE_RUN", "direct status")
    require(direct["decision"]["required_row_or_certificate_count"] == 8, "direct required")
    require(direct["decision"]["emitted_row_or_certificate_count"] == 0, "direct emitted")
    require(direct["decision"]["accepted_row_or_certificate_count"] == 0, "direct accepted")
    for key in [
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
    ]:
        require(direct["decision"][key] is False, f"direct false {key}")
    for row in direct["required_rows"]:
        require(row["emitted"] is False, f"row emitted {row['row_id']}")
        require(row["accepted"] is False, f"row accepted {row['row_id']}")
    require_no_selector(direct, "direct")

    require(reduction["status"] == "SBETA_POLAR_ANGLE_AVAILABLE_RADIAL_PHASE_SOURCE_OPEN", "reduction status")
    support = reduction["available_selected_scalar_support"]
    require(abs(support["selected_s_beta_value"] - S_BETA) < 1e-15, "reduction s_beta")
    require(support["selected_s_beta_polar_angle_closed"] is True, "polar closed")
    require(support["H_scalar_threshold_reduced_to_one_radial_source"] is True, "radial reduced")
    require(support["Herm2_radial_collapse_closed"] is True, "collapse")
    require(reduction["decision"]["s_beta_available"] is True, "s_beta available")
    require(reduction["decision"]["radial_scale_source_emitted"] is False, "radial emitted")
    require(reduction["decision"]["phase_source_emitted"] is False, "phase emitted")
    require(reduction["decision"]["Herm2_values_determined"] is False, "Herm2 determined")
    require("selected radial scale r_H or equivalent threshold scalar" in reduction["missing_for_Herm2_values"], "missing radial")
    require_no_selector(reduction, "reduction")

    require(cutset["status"] == "NEXT_FRONTIER_H_RADIAL_SCALE_PHASE_SOURCE_OR_HERM2_HESSIAN_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("finite H functional candidate emission run executed" in cutset["closed_here"], "cutset closed")
    require("selected radial scale r_H or equivalent threshold scalar" in cutset["still_open"], "cutset radial")
    require("selected Omega phase/sign source" in cutset["still_open"], "cutset phase")
    require_no_selector(cutset, "cutset")

    for phrase in [
        f"s_beta = {S_BETA}",
        "Accepted finite H functionals: `0`",
        "Accepted H-response source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: finite H functional/direct Herm(2) emission run executed; "
        "s_beta reduction is retained, but radial/phase/source rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
