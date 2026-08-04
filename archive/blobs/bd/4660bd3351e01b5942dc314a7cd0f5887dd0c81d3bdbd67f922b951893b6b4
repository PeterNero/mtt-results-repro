"""Audit the direct H quartic threshold / dynamic Herm(2) radial reduction packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLAR = PACKET_DIR / "sbeta_polar_herm2_reduction.packet.json"
FUNCTIONAL = PACKET_DIR / "h_quartic_threshold_functional_reduction.packet.json"
TRIALS = PACKET_DIR / "current_h_radial_threshold_candidates.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_radial_reduction.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_direct_h_quartic_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_DirectHQuarticThresholdFunctional_or_DynamicHerm2ValueRows_v1.md"
)
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_DIRECTHQUARTICTHRESHOLDFUNCTIONAL_OR_DYNAMICHERM2VALUEROWS_"
    "RADIAL_COLLAPSE_CLOSED_H_SCALAR_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRadialThresholdScalarSource_or_TenKClosure_v1"
SBETA_VALUE = 0.004701083905943647


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    polar = load(POLAR)
    functional = load(FUNCTIONAL)
    trials = load(TRIALS)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("polar", polar),
        ("functional", functional),
        ("trials", trials),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "selected_s_beta_polar_angle_closed",
        "Herm2_radial_collapse_closed",
        "H_scalar_threshold_reduced_to_one_radial_source",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    require(abs(decision["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "decision s_beta")
    for key in [
        "selected_H_radial_threshold_scalar_emitted",
        "selected_H_radial_scale_r_H_emitted",
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "selected_L_rowlocal_Omega_H_lambda",
        "selected_T_scheme_Omega_H_lambda",
        "K_threshold_Omega_H_lambda_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_radial_threshold_source_count"] == 0, "radial count")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(polar["status"] == "SBETA_POLAR_ANGLE_CLOSED_RADIAL_PHASE_OPEN", "polar status")
    require(polar["theorem"]["proved"] is True, "polar theorem")
    inputs = polar["selected_inputs"]
    require(abs(inputs["selected_s_beta"] - SBETA_VALUE) < 1e-18, "polar s_beta")
    require(inputs["projection_measure_equality"] is True, "projection equality")
    require(inputs["no_extra_boundary_source_term"] is True, "no boundary")
    constraints = polar["closed_exact_constraints"]
    require(constraints["Delta_squared"] == "s_beta * r_H^2", "Delta constraint")
    require(constraints["abs_Omega_squared"] == "(1 - s_beta) * r_H^2", "Omega constraint")
    expected_ratio = math.sqrt((1.0 - SBETA_VALUE) / SBETA_VALUE)
    require(
        abs(constraints["abs_Omega_over_abs_Delta"] - expected_ratio) < 1e-15,
        "ratio",
    )
    require(constraints["eigenvalues"] == ["-r_H", "+r_H"], "eigenvalues")
    for key, value in polar["coordinates_still_unselected"].items():
        require(value is None, f"polar overfilled {key}")
    consequence = polar["consequence"]
    require(consequence["scalar_H_K_route_requires_full_three_Herm2_rows"] is False, "scalar not 3-row")
    require(
        consequence["scalar_H_K_route_requires_selected_radial_threshold_scalar_or_direct_K_row"]
        is True,
        "radial scalar consequence",
    )
    require(consequence["full_dynamic_Herm2_route_requires_phase_and_sign"] is True, "phase/sign")
    require(consequence["s_beta_alone_emits_Delta_ReOmega_ImOmega"] is False, "no Herm2 rows")

    require(
        functional["status"] == "H_QUARTIC_THRESHOLD_FUNCTIONAL_REDUCED_TO_RADIAL_SOURCE_SCALAR",
        "functional status",
    )
    require(functional["theorem"]["proved"] is True, "functional theorem")
    equations = functional["closed_source_equations"]
    require(equations["direct_K_row"] == "K_threshold.Omega_H.lambda", "direct K")
    require(
        equations["split_K_row"]
        == "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "split K",
    )
    exits = functional["minimal_legal_exits"]
    require(exits["direct_exit"]["rows_needed"] == 1, "direct rows")
    require(exits["split_exit"]["rows_needed"] == 2, "split rows")
    require(exits["dynamic_Herm2_scalar_exit"]["rows_needed_for_scalar_threshold"] == 1, "radial rows")
    require(exits["full_dynamic_Herm2_exit"]["rows_needed"] == 3, "Herm2 rows")
    for exit_payload in exits.values():
        require(exit_payload["accepted_now"] is False, "exit overaccepted")
    for key, value in functional["not_accepted_as_source_rows"].items():
        require(value is None, f"functional overfilled {key}")

    require(
        trials["status"] == "CURRENT_H_RADIAL_THRESHOLD_CANDIDATES_ZERO_ACCEPTED",
        "trials status",
    )
    require(trials["accepted_radial_threshold_source_count"] == 0, "trial radial count")
    require(trials["accepted_direct_H_K_row_count"] == 0, "trial K count")
    require(len(trials["trials"]) == 7, "trial count")
    for trial in trials["trials"]:
        require(trial["accepted_as_radial_threshold_source"] is False, f"radial accepted {trial['trial_id']}")
        require(trial["accepted_as_K_threshold_Omega_H_lambda"] is False, f"K accepted {trial['trial_id']}")
    for phrase in [
        "treat s_beta as K_threshold.Omega_H.lambda",
        "fix r_H=1 by convention",
        "use D_fin.H as the H radial threshold scalar",
        "use HYM solver norms or residuals as source values",
        "use postcheck target numerators as no-knob source rows",
    ]:
        require(phrase in trials["forbidden_promotions"], f"missing forbidden {phrase}")

    require(
        hk_gate["status"]
        == "H_K_THRESHOLD_GATE_RADIAL_REDUCTION_CLOSED_H_SCALAR_SOURCE_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    require(h_row["s_beta_polar_herm2_reduction_closed"] is True, "H row polar")
    require(h_row["selected_H_radial_threshold_scalar_emitted"] is False, "H radial")
    require(h_row["selected_H_radial_scale_r_H_emitted"] is False, "H r")
    require(h_row["selected_H_phase_sign_rows_emitted"] is False, "H phase")
    require(h_row["direct_K_threshold_Omega_H_lambda_emitted"] is False, "H K")
    cons = hk_gate["conditional_consequent_current"]
    require(cons["ten_K_antecedent_satisfied"] is False, "ten K")
    require(cons["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar")
    require(cons["lambda_H_row_executable"] is False, "lambda executable")
    require(cons["accepted_internal_scalar_value_row_count"] == 0, "internal scalar")

    require(
        cutset["status"] == "NEXT_FRONTIER_H_RADIAL_THRESHOLD_SCALAR_SOURCE_OR_TEN_K_CLOSURE",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "selected s_beta polar angle constraints for Herm(2) H rows",
        "radial collapse theorem for scalar H K-threshold closure",
        "minimal legal exits reduced to direct K, split L/T, or one selected H radial threshold scalar",
        "current radial shortcuts rejected as source rows",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H radial threshold scalar R_H.threshold or equivalent direct K_threshold.Omega_H.lambda",
        "selected H-sector quartic/threshold source functional that emits the radial scalar",
        "Delta/Re(Omega)/Im(Omega) rows if full dynamic Herm(2) closure is required",
        "ten-row K antecedent",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        f"`s_beta={SBETA_VALUE}`",
        "`|Omega|/|Delta|=",
        "selected radial/threshold source scalar",
        "`R_H.threshold`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: selected s_beta polar/radial reduction closed; "
        "H radial threshold scalar and tenth K row remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
