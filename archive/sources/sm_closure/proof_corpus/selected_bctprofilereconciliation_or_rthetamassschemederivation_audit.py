"""Audit BCT profile reconciliation or R_theta mass-scheme derivation artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bctprofilereconciliation_or_rthetamassschemederivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EFT_PROFILE = PACKET_DIR / "bct_correlated_eft_profile.packet.json"
FULLSM_PROFILE = PACKET_DIR / "bct_correlated_fullsm_profile.packet.json"
RTHETA_GAP = PACKET_DIR / "rtheta_mass_scheme_derivation_gap_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_profile.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BCTProfileReconciliation_or_RThetaMassSchemeDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BCTPROFILERECONCILIATION_OR_RTHETAMASSSCHEMEDERIVATION_"
    "BUILT_CORRELATED_PROFILE_BORDERLINE_RTHETA_OPEN"
)
NEXT = "MTT_Selected_CharmCRunDecInputPolicy_or_RThetaMassSchemeDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float, expected: float, tol: float = 1e-12) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def require_profile_common(profile: dict) -> None:
    require(profile["schema"] == "MTTBCTCorrelatedProfile.v1", "wrong profile schema")
    require(profile["degrees_of_freedom"] == 3, "wrong profile dof")
    require(profile["profile_closure_claimed"] is False, "profile closure overclaimed")
    require(profile["observed_data_used_as_selector"] is False, "observed selector used")
    require(profile["target_fitting_used"] is False, "target fitting used")
    require(profile["closure_claimed"] is True, "profile packet should close locally")
    require(profile["correlation_matrix_determinant"] > 0.8, "bad correlation determinant")
    require(
        profile["row_order"]
        == [
            "bottom_MSbar_native_scale_transport",
            "charm_MSbar_native_scale_transport",
            "tau_pole_rest_to_running_lepton",
        ],
        "wrong profile row order",
    )


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    eft = load(EFT_PROFILE)
    fullsm = load(FULLSM_PROFILE)
    rtheta = load(RTHETA_GAP)
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

    require_profile_common(eft)
    require(eft["status"] == "BCT_EFT_CORRELATED_PROFILE_COMPUTED_BORDERLINE_NOT_CLOSED", "EFT status mismatch")
    require(eft["table_key"] == "EFT_QCDxQED_5q3l_MZ", "EFT table key mismatch")
    require(close(eft["diagonal_chi_square"], 8.099817363144254), "EFT diagonal chi-square changed")
    require(close(eft["correlated_chi_square"], 9.449973148192832), "EFT correlated chi-square changed")
    require(close(eft["chi_square_survival_probability_df3"], 0.02386956100195133), "EFT p-value changed")
    require(eft["passes_95pct_profile_gate"] is False, "EFT 95pct gate changed")
    require(eft["passes_99pct_profile_gate"] is True, "EFT 99pct gate changed")
    require(eft["correlation_matrix"] == [[1.0, 0.37, -0.002], [0.37, 1.0, -0.0017], [-0.002, -0.0017, 1.0]], "EFT correlations changed")
    require(close(eft["z_residuals"]["charm_MSbar_native_scale_transport"], 2.8458915935487368), "EFT charm z changed")

    require_profile_common(fullsm)
    require(
        fullsm["status"] == "BCT_FULLSM_CORRELATED_PROFILE_COMPUTED_REJECTED_FOR_CURRENT_EXTERNAL_ROWS",
        "full-SM status mismatch",
    )
    require(fullsm["table_key"] == "FullSM_6q3l_MZ", "full-SM table key mismatch")
    require(close(fullsm["diagonal_chi_square"], 4554.958103075176), "full-SM diagonal chi-square changed")
    require(close(fullsm["correlated_chi_square"], 4571.749371583484), "full-SM correlated chi-square changed")
    require(fullsm["chi_square_survival_probability_df3"] == 0.0, "full-SM p-value changed")
    require(fullsm["passes_95pct_profile_gate"] is False, "full-SM 95pct gate changed")
    require(fullsm["passes_99pct_profile_gate"] is False, "full-SM 99pct gate changed")
    require(fullsm["correlation_matrix"] == [[1.0, 0.37, -0.023], [0.37, 1.0, -0.029], [-0.023, -0.029, 1.0]], "full-SM correlations changed")
    require(close(fullsm["z_residuals"]["tau_pole_rest_to_running_lepton"], 67.39285714285694), "full-SM tau z changed")

    require(
        rtheta["status"] == "EXTERNAL_PROFILE_COMPUTED_SELECTED_RTHETA_DERIVATION_STILL_OPEN",
        "Rtheta status mismatch",
    )
    require(rtheta["external_rows_available"] is True, "external rows not available in Rtheta recheck")
    require(rtheta["accepted_Rtheta_source_row_count"] == 0, "Rtheta source rows overaccepted")
    require(rtheta["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta derivation overclosed")
    require(rtheta["minimal_internal_missing_object"] == "SelectedRouteCStromingerGalerkinResidualSolve", "wrong Rtheta missing object")
    require(rtheta["external_profile_may_validate_Rtheta"] is True, "Rtheta validation relation missing")
    require(rtheta["external_profile_selects_Rtheta"] is False, "external profile selects Rtheta")
    require(rtheta["closure_claimed"] is False, "Rtheta gap overclosed")

    require(cutset["status"] == "NEXT_ATTACK_CHARM_INPUT_POLICY_OR_SELECTED_RTHETA_ROWS", "cutset status mismatch")
    for key in [
        "BCT_correlated_EFT_profile_computed",
        "BCT_correlated_fullSM_profile_computed",
        "fullSM_current_external_profile_rejected",
        "Rtheta_nonselector_gap_rechecked",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "BCT_profile_95pct_closure",
        "charm_CRunDec_input_policy_reconciliation",
        "selected_Rtheta_mass_scheme_derivation",
        "W_Z_H_electroweak_matching_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["accepted_bottom_charm_tau_map_row_count"] == 3, "candidate row count mismatch")
    require(closure["all_three_bct_external_mass_scheme_rows_available"] is True, "candidate all-three missing")
    require(closure["BCT_correlated_EFT_profile_computed"] is True, "candidate EFT profile missing")
    require(closure["BCT_EFT_profile_passes_95pct_gate"] is False, "candidate EFT 95 gate changed")
    require(closure["BCT_EFT_profile_passes_99pct_gate"] is True, "candidate EFT 99 gate changed")
    require(closure["BCT_fullSM_profile_passes_95pct_gate"] is False, "candidate full-SM gate changed")
    for key in [
        "BCT_profile_95pct_closure_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("EFT passes 95 pct profile gate  : false" in note, "note missing 95 gate")
    require("selected Rtheta rows closed     : false" in note, "note missing Rtheta guard")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
