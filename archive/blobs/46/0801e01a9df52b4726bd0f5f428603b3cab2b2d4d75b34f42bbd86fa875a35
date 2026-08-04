"""Audit phase-lane curvature source-relation skeleton."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phaselanecurvaturesourcerelation_or_sevenparameteryukawareduction"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SKELETON = PACKET_DIR / "phase_lane_curvature_source_skeleton.packet.json"
EXECUTION = PACKET_DIR / "seven_parameter_reduction_execution.packet.json"
OBLIGATION = PACKET_DIR / "residual_exactness_obligation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhaseLaneCurvatureSourceRelation_or_SevenParameterYukawaReduction_v1.md"

STATUS = "MTT_SELECTED_PHASELANECURVATURESOURCERELATION_OR_SEVENPARAMETERYUKAWAREDUCTION_BUILT_SKELETON_RESIDUAL_OPEN"
NEXT = "MTT_Selected_PhaseLaneCurvatureResidualExactness_or_SourceCorrectionRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    skeleton = load(SKELETON)
    execution = load(EXECUTION)
    obligation = load(OBLIGATION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is True, "candidate fitted guard")
    require(data["target_fitting_used"] is True, "candidate target fitting")

    require(data["theorem"]["name"] == "PhaseLaneCurvatureSourceRelationSkeletonTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "skeleton theorem not proved")

    status = data["source_theorem_status"]
    require(status["source_relation_skeleton_constructed"] is True, "skeleton not constructed")
    require(status["gamma_source_row_accepted"] is False, "gamma overaccepted")
    require(status["three_over_eleven_source_ratio_accepted"] is False, "ratio overaccepted")
    require(status["residual_exactness_closed"] is False, "residual overclosed")
    require(status["exact_seven_parameter_reduction_closed"] is False, "exact reduction overclosed")
    require(status["accepted_no_knob_yukawa_rows"] == 0, "no-knob rows overaccepted")

    relation = skeleton["relation"]
    require(relation["operator_form"] == "log|Y_s(g)| = a_s + b_s F_g + gamma * chi_s * F_g^2", "operator form")
    require(relation["chi_phase_packet_I_plus_Z"] == 1, "phase chi")
    require(relation["chi_shift_packet_I_plus_X"] == "3/11", "shift chi")
    require(relation["sector_lane_map"] == {"u": "phase_packet_I_plus_Z", "e": "phase_packet_I_plus_Z", "d": "shift_packet_I_plus_X"}, "lane map")
    require(len(relation["parameter_slots"]) == 7, "parameter slot count")
    require(relation["source_reduction_if_exact"] == "9 coefficient rows -> 7 coefficient rows", "reduction text")

    closed = skeleton["closed_source_side_support"]
    for key in [
        "family_spectrum_closed",
        "family_basis_nonsingular",
        "phase_shift_lane_routing_closed",
        "step68_theta_exponent_rows_closed",
        "small_rational_curvature_clue_retained",
    ]:
        require(closed[key] is True, f"closed support missing {key}")
    require(closed["theta_rows_target_fitting_used"] is False, "theta rows target fitting")
    require(closed["theta_rows_observed_data_used_as_selector"] is False, "theta rows observed selector")

    open_clauses = skeleton["open_source_clauses"]
    require(set(open_clauses) == {"gamma_source_row", "three_over_eleven_source_ratio", "residual_exactness_or_correction_rows"}, "open clauses")
    guard = skeleton["guardrails"]
    require(guard["observed_data_used_to_fit_gamma_and_affine_rows"] is True, "skeleton fitted guard")
    require(guard["accepted_as_selected_source_theorem"] is False, "skeleton source overclaimed")
    require(guard["accepted_no_knob_yukawa_rows"] == 0, "skeleton no-knob rows")
    require(guard["exact_reduction_closed"] is False, "skeleton exact overclosed")

    require(execution["status"] == "SEVEN_PARAMETER_REDUCTION_EXECUTED_AS_FITTED_SKELETON_RESIDUAL_OPEN", "execution status")
    require(execution["ratio_c2_d_to_phase_gamma"] == 3.0 / 11.0, "execution ratio")
    require(len(execution["fitted_parameters"]) == 7, "execution fitted param count")
    require(abs(execution["fitted_parameters"]["gamma"] - data["key_numbers"]["fitted_gamma"]) < 1.0e-15, "gamma mismatch")
    require(execution["max_abs_log_residual"] > 0, "residual should be nonzero")
    require(execution["max_abs_log_residual"] < 0.002, "residual too large")
    require(execution["worst_multiplicative_yukawa_error"] < 1.002, "fitted clue too weak")
    require(execution["accepted_as_exact_source_reduction"] is False, "execution overaccepted")
    require(execution["observed_data_used_as_selector"] is True, "execution observed selector")
    require(execution["target_fitting_used"] is True, "execution target fitting")

    require(obligation["status"] == "RESIDUAL_EXACTNESS_OPEN", "obligation status")
    require(obligation["residual_rank"] == 1, "residual rank")
    require(obligation["residual_frobenius_norm"] > 0, "residual norm zero")
    for row_sum in obligation["residual_row_sums"]:
        require(abs(row_sum) < 1.0e-12, "row residual not centered")
    require(len(obligation["legal_closure_routes"]) == 3, "legal routes")
    require(len(obligation["forbidden_closure_routes"]) == 3, "forbidden routes")

    closure = data["closure_decision"]
    require(closure["seven_parameter_curvature_skeleton_closed"] is True, "closure skeleton")
    require(closure["strict_selected_source_relation_closed"] is False, "closure strict overclosed")
    require(closure["strict_no_knob_flavor_closure"] is False, "closure flavor overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "closure true SM overclosed")
    require(closure["full_no_knob_closed"] is False, "closure no-knob overclosed")

    require(cert["skeleton_theorem_proved"] is True, "cert skeleton")
    require(cert["source_theorem_proved"] is False, "cert source overproved")
    require(cert["gamma_source_row_accepted"] is False, "cert gamma")
    require(cert["three_over_eleven_source_ratio_accepted"] is False, "cert ratio")
    require(cert["residual_exactness_closed"] is False, "cert residual")
    require(cert["accepted_no_knob_yukawa_rows"] == 0, "cert no-knob rows")

    for phrase in [
        "seven-parameter curvature skeleton",
        "`chi_d = 3/11`",
        "max log residual",
        "residual is nonzero",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
