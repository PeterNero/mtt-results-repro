"""Audit charm table substitution or selected Rtheta rows decision artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUBSTITUTION = PACKET_DIR / "charm_table_substitution_decision.packet.json"
EMPIRICAL_PROFILE = PACKET_DIR / "bct_empirical_table_substituted_profile.packet.json"
RTHETA_DECISION = PACKET_DIR / "selected_rtheta_rows_decision_after_table_substitution.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charm_table_substitution.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CharmTableSubstitution_or_SelectedRThetaRowsDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CHARMTABLESUBSTITUTION_OR_SELECTEDRTHETAROWSDECISION_"
    "BUILT_EMPIRICAL_PROFILE_CLOSED_SOURCE_RTHETA_OPEN"
)
NEXT = "MTT_Selected_WZHElectroweakRows_or_SelectedRThetaMassSchemeDerivation_v1"


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
    substitution = load(SUBSTITUTION)
    empirical = load(EMPIRICAL_PROFILE)
    rtheta = load(RTHETA_DECISION)
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

    require(
        substitution["status"] == "HUANG_ZHOU_CHARM_TABLE_SUBSTITUTION_ACCEPTED_AS_EMPIRICAL_PROFILE_ROW",
        "substitution status mismatch",
    )
    decision = substitution["decision"]
    require(decision["accept_charm_table_substitution_for_empirical_profile"] is True, "substitution not accepted")
    require(decision["substituted_row_id"] == "charm_MSbar_native_scale_transport", "wrong substituted row")
    require(close(decision["substituted_mass_MZ_GeV"], 0.628), "substituted charm mass changed")
    require(close(decision["substituted_uncertainty_GeV"], 0.018), "substituted charm sigma changed")
    require(decision["resulting_charm_z"] == 0.0, "substituted charm z changed")
    scope = substitution["scope"]
    require(scope["closes_empirical_BCT_profile_layer"] is True, "empirical layer not closed")
    for key in [
        "replaces_CRunDec_replay_row_as_source",
        "selects_CRunDec_input_policy",
        "selects_Rtheta_mass_scheme_rows",
        "claims_no_knob_derivation",
    ]:
        require(scope[key] is False, f"scope overclaimed: {key}")
    require(substitution["closure_claimed"] is True, "substitution should close locally")

    require(
        empirical["status"] == "BCT_EMPIRICAL_TABLE_SUBSTITUTED_PROFILE_PASSES_95PCT_GATE",
        "empirical profile status mismatch",
    )
    require(close(empirical["correlated_chi_square"], 0.0008323513815455399), "empirical chi-square changed")
    require(close(empirical["chi_square_survival_probability_df3"], 0.999993614860048), "empirical p-value changed")
    require(empirical["passes_95pct_profile_gate"] is True, "empirical 95 gate not closed")
    require(empirical["passes_99pct_profile_gate"] is True, "empirical 99 gate not closed")
    require(empirical["empirical_profile_closure_claimed"] is True, "empirical closure missing")
    require(empirical["source_or_Rtheta_closure_claimed"] is False, "source/Rtheta closure overclaimed")
    require(empirical["z_residuals"]["charm_MSbar_native_scale_transport"] == 0.0, "charm z not substituted")
    require(close(empirical["z_residuals"]["bottom_MSbar_native_scale_transport"], -0.026803001937948125), "bottom z changed")
    require(empirical["z_residuals"]["tau_pole_rest_to_running_lepton"] == 0.0, "tau z changed")
    require(empirical["closure_claimed"] is True, "empirical packet should close locally")

    require(
        rtheta["status"] == "EMPIRICAL_PROFILE_CLOSED_SELECTED_RTHETA_ROWS_STILL_OPEN",
        "Rtheta decision status mismatch",
    )
    require(rtheta["empirical_profile_closed"] is True, "Rtheta decision missing empirical closure")
    require(rtheta["external_rows_available"] is True, "Rtheta decision missing external rows")
    require(rtheta["accepted_Rtheta_source_row_count"] == 0, "Rtheta rows overaccepted")
    require(rtheta["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta derivation overclosed")
    require(rtheta["minimal_internal_missing_object"] == "SelectedRouteCStromingerGalerkinResidualSolve", "wrong missing object")
    require(rtheta["closure_claimed"] is False, "Rtheta decision overclosed")

    require(cutset["status"] == "NEXT_ATTACK_WZH_ELECTROWEAK_ROWS_OR_SELECTED_RTHETA_DERIVATION", "cutset status mismatch")
    for key in [
        "charm_table_substitution_empirical_profile_decision",
        "BCT_empirical_profile_95pct_closure",
        "BCT_external_row_availability",
        "table_substitution_scope_guard",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "BCT_source_or_no_knob_profile_closure",
        "selected_Rtheta_mass_scheme_derivation",
        "selected_CRunDec_charm_input_policy",
        "W_Z_H_electroweak_matching_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["BCT_empirical_profile_95pct_closure_closed"] is True, "candidate empirical closure missing")
    require(close(closure["BCT_empirical_profile_survival_probability"], 0.999993614860048), "candidate p changed")
    require(closure["charm_table_substitution_accepted_as_empirical_profile"] is True, "candidate substitution missing")
    for key in [
        "BCT_source_or_no_knob_profile_closure_closed",
        "selected_CRunDec_charm_input_policy_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("BCT empirical 95 pct closure   : true" in note, "note missing empirical closure")
    require("selected Rtheta rows closed    : false" in note, "note missing Rtheta guard")
    require("full no-knob closure           : false" in note, "note missing no-knob guard")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
