"""Audit charm CRunDec input policy or R_theta mass-scheme derivation artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_charmcrundecinputpolicy_or_rthetamassschemederivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SWEEP = PACKET_DIR / "charm_crundec_input_policy_sweep.packet.json"
SENSITIVITY = PACKET_DIR / "bct_profile_sensitivity_to_charm_policy.packet.json"
SELECTION_GATE = PACKET_DIR / "charm_policy_selection_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charm_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CharmCRunDecInputPolicy_or_RThetaMassSchemeDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CHARMCRUNDECINPUTPOLICY_OR_RTHETAMASSSCHEMEDERIVATION_"
    "BUILT_POLICY_SWEEP_NO_SELECTED_REPAIR"
)
NEXT = "MTT_Selected_CharmTableSubstitution_or_SelectedRThetaRowsDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float, expected: float, tol: float = 1e-12) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    sweep = load(SWEEP)
    sensitivity = load(SENSITIVITY)
    gate = load(SELECTION_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
        require(cert[key] is False, f"certificate guardrail overclaimed: {key}")

    require(sweep["status"] == "CHARM_CRUNDEC_POLICY_SWEEP_BUILT_NO_EXACT_REPAIR", "sweep status mismatch")
    require(sweep["grid"]["row_count"] == 750, "sweep row count changed")
    require(sweep["best_grid_row_selected"] is False, "best grid row selected")
    best = sweep["best_grid_row_by_abs_residual"]
    require(close(best["running_mass_MZ_GeV"], 0.6719738598372106), "best grid mass changed")
    require(close(best["z_to_HuangZhou_EFT"], 2.442992213178366), "best grid z changed")
    require(best["alpha_s_MZ"] == 0.1185, "best alpha changed")
    require(best["mc_mc_GeV"] == 1.27, "best mc changed")
    require(best["bottom_threshold_GeV"] == 4.8, "best threshold changed")
    require(best["loop_order"] == 5, "best loop changed")
    require(close(sweep["current_repo_charm_row"]["z_to_HuangZhou_EFT"], 2.8458915935487368), "current z changed")
    require(close(sweep["huang_zhou_input_like_probes"]["alpha_s_0p1179_mc_1p27_mbth_4p8_loop4"]["z_to_HuangZhou_EFT"], 2.946349287499459), "HZ-ish loop4 z changed")
    require(close(sweep["huang_zhou_input_like_probes"]["alpha_s_0p1179_mc_1p27_mbth_4p8_loop5"]["z_to_HuangZhou_EFT"], 2.780653970852618), "HZ-ish loop5 z changed")
    require("target fitting" in sweep["why_not_selected"], "sweep target-fit guard missing")
    require(sweep["closure_claimed"] is True, "sweep should close locally")

    require(
        sensitivity["status"] == "PROFILE_SENSITIVITY_TO_CHARM_POLICY_COMPUTED_SELECTION_OPEN",
        "sensitivity status mismatch",
    )
    profiles = sensitivity["profiles"]
    require(close(profiles["current_repo_policy"]["chi_square_survival_probability_df3"], 0.02386956100195133), "current p changed")
    require(close(profiles["best_grid_row"]["chi_square_survival_probability_df3"], 0.07280094084234212), "best-grid p changed")
    require(close(profiles["external_table_substitution"]["chi_square_survival_probability_df3"], 0.999993614860048), "table-substitution p changed")
    require(profiles["current_repo_policy"]["passes_95pct_profile_gate"] is False, "current policy gate changed")
    require(profiles["best_grid_row"]["passes_95pct_profile_gate"] is True, "best grid gate changed")
    require(profiles["external_table_substitution"]["passes_95pct_profile_gate"] is True, "table substitution gate changed")
    require(sensitivity["profile_pass_possible_in_grid"] is True, "grid pass possibility missing")
    require(sensitivity["profile_pass_possible_by_table_substitution"] is True, "table pass possibility missing")
    require(sensitivity["profile_pass_selected_now"] is False, "profile pass selected")
    require("Neither choice is selected" in sensitivity["selection_guard"], "selection guard missing")
    require(sensitivity["closure_claimed"] is True, "sensitivity should close locally")

    require(gate["status"] == "CHARM_POLICY_REPAIR_CANDIDATES_IDENTIFIED_NONE_SELECTED", "gate status mismatch")
    require(gate["best_grid_policy_would_pass_95pct_profile"] is True, "best-grid gate flag missing")
    require(gate["huang_zhou_table_substitution_would_pass_95pct_profile"] is True, "table gate flag missing")
    require(gate["accepted_repair_now"] is False, "repair accepted too early")
    require(gate["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta derivation overclosed")
    require(gate["minimal_internal_missing_object"] == "SelectedRouteCStromingerGalerkinResidualSolve", "wrong missing object")
    require(len(gate["required_for_acceptance"]) == 3, "acceptance requirements changed")
    require(gate["closure_claimed"] is False, "gate overclosed")

    require(cutset["status"] == "NEXT_DECIDE_TABLE_SUBSTITUTION_OR_SELECTED_RTHETA_ROWS", "cutset status mismatch")
    for key in [
        "charm_CRunDec_input_policy_sweep",
        "BCT_profile_sensitivity_to_charm_policy",
        "passing_policy_candidates_identified",
        "no_hidden_fit_guard_enforced",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "selected_charm_policy_repair",
        "selected_Rtheta_mass_scheme_derivation",
        "BCT_profile_95pct_closure",
        "W_Z_H_electroweak_matching_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["charm_CRunDec_input_policy_sweep_closed"] is True, "candidate sweep flag missing")
    require(closure["profile_pass_possible_in_grid"] is True, "candidate grid pass flag missing")
    require(closure["profile_pass_possible_by_table_substitution"] is True, "candidate table pass flag missing")
    for key in [
        "selected_charm_policy_repair_closed",
        "BCT_profile_95pct_closure_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("best grid selected                : false" in note, "note missing best-grid guard")
    require("selected Rtheta rows closed       : false" in note, "note missing Rtheta guard")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
