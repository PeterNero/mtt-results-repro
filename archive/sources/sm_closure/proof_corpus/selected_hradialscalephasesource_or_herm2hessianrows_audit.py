"""Audit H radial-scale/phase source or Herm(2) Hessian rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialscalephasesource_or_herm2hessianrows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRadialScalePhaseSource_or_Herm2HessianRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

SOURCE_SPLIT = BASE / "h_radial_scale_source_split.packet.json"
POLAR = BASE / "herm2_polar_reconstruction_law.packet.json"
CONTROLLED = BASE / "controlled_parameter_radial_lane.packet.json"
CUTSET = BASE / "next_cutset_after_hradial_phase_source.packet.json"

STATUS = (
    "MTT_SELECTED_HRADIALSCALEPHASESOURCE_OR_HERM2HESSIANROWS_"
    "RADIAL_ROUTE_SPLIT_PHASE_TRACE_OPEN"
)
NEXT = "MTT_Selected_Herm2PolarSourceCompletion_or_HResponseRows_v1"
S_BETA = 0.004701083905943647
UP_HRG = 391.39140285811936
LOG_UP_HRG = 5.969708089616292


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
    split = load(SOURCE_SPLIT)
    polar = load(POLAR)
    controlled = load(CONTROLLED)
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
        "radial_source_route_split_closed",
        "Herm2_polar_reconstruction_law_closed",
        "controlled_radial_calibration_available",
        "lambda_H_calibrated_in_controlled_lane",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "strict_radial_scale_source_emitted",
        "selected_Delta_sign_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "same_source_certificates_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_H_response_source_row_count"] == 0, "H rows")
    require(decision["accepted_R_H_RG_source_count"] == 0, "RHRG rows")

    nums = candidate["key_numbers"]
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-15, "s_beta")
    require(abs(nums["UP_RET_OVERLAP_HRG_controlled_calibration"] - UP_HRG) < 1e-12, "UP HRG")
    require(abs(nums["log_UP_RET_OVERLAP_HRG"] - LOG_UP_HRG) < 1e-12, "log UP")
    require(nums["strict_selected_K_source_rows"] == 9, "K rows")
    require(nums["strict_selected_K_rows_required"] == 10, "K required")
    require(nums["accepted_H_response_source_row_count"] == 0, "num H rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "num RHRG")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "radial_source_route_split_closed",
        "Herm2_polar_reconstruction_law_closed",
        "controlled_radial_calibration_available",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "strict_radial_scale_source_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "direct_Herm2_rows_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_H_response_source_row_count"] == 0, "cert H rows")
    require(cert["accepted_R_H_RG_source_count"] == 0, "cert RHRG")

    require(split["status"] == "RADIAL_SOURCE_REDUCED_TO_EW_BOUNDARY_OR_H_THRESHOLD_RG", "split status")
    require(abs(split["selected_angle_support"]["s_beta"] - S_BETA) < 1e-15, "split s_beta")
    require(split["selected_angle_support"]["selected_s_beta_polar_angle_closed"] is True, "angle")
    require(split["selected_angle_support"]["Herm2_radial_collapse_closed"] is True, "collapse")
    strict = split["strict_no_knob_radial_routes"]
    require(strict["Dterm_EW_boundary_route"]["reduced"] is True, "Dterm reduced")
    require(strict["Dterm_EW_boundary_route"]["selected_A_EW_emitted"] is False, "A_EW overclosed")
    require(strict["Dterm_EW_boundary_route"]["K_threshold_Omega_H_lambda_emitted"] is False, "K overclosed")
    require(strict["intrinsic_H_quartic_or_large_threshold_RG_route"]["A_EW_source_tier_gate_closed"] is True, "tier")
    require(strict["intrinsic_H_quartic_or_large_threshold_RG_route"]["direct_intrinsic_H_quartic_K_row_emitted"] is False, "intrinsic K")
    require(strict["strict_R_H_RG_operator_route"]["strict_H_threshold_RG_operator_source_search_closed"] is True, "source search")
    require(strict["strict_R_H_RG_operator_route"]["strict_H_threshold_RG_operator_emitted"] is False, "strict R")
    require(split["decision"]["radial_source_route_split_closed"] is True, "split closed")
    require(split["decision"]["strict_radial_scale_source_emitted"] is False, "strict radial")
    require(split["decision"]["controlled_radial_calibration_available"] is True, "controlled radial")
    require(split["decision"]["strict_Herm2_rows_determined"] is False, "strict Herm2")
    require_no_selector(split, "split")

    require(polar["status"] == "HERMITIAN_TRACEFREE_POLAR_LAW_CLOSED_VALUES_CONDITIONAL", "polar status")
    require(abs(polar["known_inputs"]["s_beta"] - S_BETA) < 1e-15, "polar s_beta")
    for key in ["radial_scale", "Delta_sign", "Omega_phase", "trace_center", "source_certificates"]:
        require(key in polar["required_new_sources"], f"polar source {key}")
    formulas = polar["conditional_reconstruction"]
    require(formulas["Delta"] == "sigma_D * r_H * sqrt(s_beta)", "Delta formula")
    require("cos(phi_Omega)" in formulas["Re_Omega"], "Re formula")
    require("sin(phi_Omega)" in formulas["Im_Omega"], "Im formula")
    require(formulas["Huu"] == "m0 + Delta", "Huu formula")
    require(formulas["Hdd"] == "m0 - Delta", "Hdd formula")
    require(polar["decision"]["polar_reconstruction_law_closed"] is True, "polar closed")
    for key in [
        "Delta_row_emitted",
        "Re_Omega_row_emitted",
        "Im_Omega_row_emitted",
        "Huu_Hud_Hdd_emitted",
        "trace_center_source_emitted",
        "phase_source_emitted",
    ]:
        require(polar["decision"][key] is False, f"polar false {key}")
    require_no_selector(polar, "polar")

    require(controlled["status"] == "CONTROLLED_RADIAL_LANE_AVAILABLE_NOT_STRICT_SOURCE", "controlled status")
    param = controlled["controlled_parameter"]
    require(param["name"] == "UP_RET_OVERLAP_HRG", "param name")
    require(abs(param["value"] - UP_HRG) < 1e-12, "param value")
    require(abs(param["log_value"] - LOG_UP_HRG) < 1e-12, "param log")
    require(param["lambda_H_calibrated"] is True, "lambda calibrated")
    require(param["lambda_H_predicted"] is False, "lambda predicted")
    boundary = controlled["strict_boundary"]
    require(boundary["strict_H_threshold_RG_source_theorem_attempted"] is True, "strict attempted")
    require(boundary["strict_H_threshold_RG_operator_emitted"] is False, "strict emitted")
    require(boundary["crossuse_prediction_audit_passed"] is False, "crossuse")
    require(boundary["strict_accepted_selected_K_source_row_count"] == 9, "strict K")
    require(boundary["strict_selected_K_threshold_row_count_required"] == 10, "strict K req")
    require(controlled["decision"]["minimal_parameter_H_layer_available"] is True, "min layer")
    require(controlled["decision"]["usable_for_SM_parity_calibration"] is True, "SM parity")
    require(controlled["decision"]["usable_for_no_knob_prediction"] is False, "no knob")
    require(controlled["decision"]["can_emit_strict_Herm2_rows"] is False, "Herm2 strict")
    require(controlled["decision"]["can_emit_controlled_radial_placeholder"] is True, "placeholder")
    require_no_selector(controlled, "controlled")

    require(cutset["status"] == "NEXT_FRONTIER_HERM2_POLAR_SOURCE_COMPLETION_OR_HRESPONSE_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("Herm(2) polar reconstruction law from s_beta, radial scale, phase, sign, and trace source" in cutset["closed_here"], "cutset closed")
    for phrase in [
        "strict selected radial scale source",
        "selected Delta sign/source orientation",
        "selected Omega phase in H_uv basis",
        "trace-center m0 source or quotient trace-free normalization theorem",
        "direct H-response rows Huu,Hud,Hdd",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        f"s_beta = {S_BETA}",
        f"UP_RET_OVERLAP_HRG = {UP_HRG}",
        "Delta    = sigma_D * r_H * sqrt(s_beta)",
        "Accepted H-response source rows: `0`",
        "Strict radial scale source emitted: `False`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H radial source split and Herm(2) polar law are closed; "
        "strict radial/phase/trace source rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
