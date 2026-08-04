"""Audit Step56 diagonal-profile import / no-knob frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step56_diagonalprofile_import_or_noknob_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE_IMPORT = PACKET_DIR / "step56_diagonal_profile_import.packet.json"
VALUE_RECHECK = PACKET_DIR / "step56_value_readiness_recheck_after_profile.packet.json"
CUTSET = PACKET_DIR / "step56_next_noknob_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step56_DiagonalProfileImport_or_NoKnobFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP56_DIAGONAL_PROFILE_IMPORTED_NOKNOB_VALUE_DERIVATION_OPEN"
NEXT = "MTT_Selected_NoKnobValueDerivationPostPi_or_MinimalUniversalParameterPolicy_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE_IMPORT)
    values = load(VALUE_RECHECK)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step56 theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for packet in [data, profile, values, cutset, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(profile["accepted_diagonal_profile_theorem_closed"] is True, "diagonal theorem not imported")
    require(
        profile["full_profile_likelihood_or_accepted_diagonal_theorem_closed"] is True,
        "profile/diagonal requirement not closed",
    )
    require(profile["full_covariance_profile_likelihood_closed"] is False, "full covariance overclosed")
    require(profile["profile_row_count"] == 6, "profile row count mismatch")
    require(profile["reduced_chi2_diagonal"] < 1.001, "diagonal reduced chi2 mismatch")
    require(profile["max_abs_pull"] < 2.22, "diagonal max pull mismatch")
    require(profile["full_covariance_gap_preserved"] is True, "full covariance gap not preserved")

    require(values["previous_present_count"] == 7, "previous readiness mismatch")
    require(values["present_count"] == 8, "readiness present mismatch")
    require(values["requirement_count"] == 9, "readiness requirement mismatch")
    require(
        values["retired_blocking_failure"] == "full_profile_likelihood_or_accepted_diagonal_theorem",
        "wrong retired blocker",
    )
    require(values["blocking_failures"] == ["no_knob_value_derivation"], "remaining blocker mismatch")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        require(values[key] is False, f"value recheck overclosed: {key}")
    require(values["accepted_coefficient_value_count"] == 0, "coefficient values overaccepted")
    require(values["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")

    closed = cutset["closed_now"]
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows_at_admitted_external_tier",
        "mass_scheme_conversion_source_rows_at_admitted_external_tier",
        "accepted_diagonal_profile_theorem",
        "Rtheta_readiness_present_count_advanced_to_8_of_9",
    ]:
        require(closed[key] is True, f"cutset closure missing: {key}")
    still = cutset["still_open"]
    for key in [
        "no_knob_value_derivation",
        "selected_internal_Rtheta_threshold_mass_derivation",
        "selected_threshold_response_functional_instantiated",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(still[key] is True, f"cutset overclosed: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    decision = data["closure_decision"]
    for key in [
        "accepted_diagonal_profile_theorem_closed",
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
        require(cert[key] is True, f"certificate closure missing: {key}")
    for key in [
        "full_covariance_profile_likelihood_closed",
        "no_knob_value_derivation_closed",
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["Rtheta_readiness_present_count"] == 8, "candidate readiness mismatch")
    require(decision["Rtheta_readiness_requirement_count"] == 9, "candidate requirement mismatch")
    require(decision["only_remaining_readiness_blocker"] == "no_knob_value_derivation", "wrong remaining blocker")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "internal Rtheta rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "internal scalar rows overaccepted")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "accepted diagonal theorem closed       : true",
        "full correlated covariance closed      : false",
        "Rtheta readiness                       : 8/9",
        "only remaining readiness blocker       : no_knob_value_derivation",
        "selected internal Rtheta rows          : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
