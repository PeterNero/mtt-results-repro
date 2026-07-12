from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def close(actual: float, expected: float, tol: float = 1e-12) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def main() -> None:
    candidate = load_json("candidate_data/selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit.candidate.json")
    cert = load_json("certificates/selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit_certificate.json")
    rtheta_rule = load_json("certificates/selected_rthetasourceruleemission_or_thresholdmatchingmassschemerows_certificate.json")
    threshold_mass = load_json("certificates/selected_thresholdmatchingrowspostpi_or_massschemesourcerows_certificate.json")
    diagonal_cert = load_json("certificates/selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation_certificate.json")
    threshold_rows = load_json("candidate_data/selected_thresholdmatchingrowspostpi_or_massschemesourcerows/post_pi_admitted_threshold_matching_rows.packet.json")
    mass_rows = load_json("candidate_data/selected_thresholdmatchingrowspostpi_or_massschemesourcerows/post_pi_admitted_mass_scheme_rows.packet.json")
    diagonal = load_json("candidate_data/selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation/accepted_diagonal_profile_theorem_after_external_rows.packet.json")
    readiness = load_json("candidate_data/selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation/rtheta_value_readiness_after_diagonal_theorem.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    require(rtheta_rule["selected_Rtheta_source_rule_functional_mapping_closed"] is True, "Rtheta source-rule mapping not closed")
    require(rtheta_rule["readiness_fraction"] == "5/7", "prior readiness not 5/7")
    require(rtheta_rule["threshold_matching_source_rows_closed"] is False, "prior rule unexpectedly closed threshold rows")
    require(rtheta_rule["mass_scheme_conversion_source_rows_closed"] is False, "prior rule unexpectedly closed mass rows")

    external = candidate["admitted_external_row_exit"]
    require(threshold_mass["threshold_matching_source_rows_closed"] is True, "post-Pi threshold rows not closed")
    require(threshold_mass["mass_scheme_conversion_source_rows_closed"] is True, "post-Pi mass rows not closed")
    require(threshold_mass["closed_at_admitted_external_tier_only"] is True, "post-Pi tier guard missing")
    require(threshold_mass["selected_internal_Rtheta_threshold_mass_derivation_closed"] is False, "post-Pi overcloses internal Rtheta rows")
    require(external["closed"] is True, "external row exit not closed")
    require(external["closure_tier"] == "admitted_external_replay", "wrong closure tier")
    require(external["threshold_matching_source_rows_closed"] is True, "candidate threshold rows not closed")
    require(external["mass_scheme_conversion_source_rows_closed"] is True, "candidate mass rows not closed")
    require(external["accepted_external_threshold_row_count"] == threshold_rows["accepted_admitted_external_threshold_matching_row_count"] == 7, "threshold row count mismatch")
    require(external["accepted_external_mass_scheme_row_count"] == mass_rows["accepted_admitted_external_mass_scheme_row_count"] == 3, "mass row count mismatch")
    require(external["accepted_internal_selected_Rtheta_threshold_mass_row_count"] == 0, "candidate overclaims internal Rtheta rows")
    require(external["selected_internal_Rtheta_threshold_mass_derivation_closed"] is False, "candidate overcloses internal Rtheta derivation")
    require(external["external_rows_used_as_branch_selector"] is False, "external rows used as branch selector")

    profile = candidate["profile_exit"]
    require(diagonal_cert["accepted_diagonal_profile_theorem_closed"] is True, "diagonal theorem not closed")
    require(diagonal_cert["full_covariance_profile_likelihood_closed"] is False, "diagonal cert overcloses full covariance")
    require(diagonal["accepted_diagonal_theorem_closed"] is True, "diagonal packet not closed")
    require(diagonal["full_profile_likelihood_closed"] is False, "diagonal packet overcloses full profile")
    require(profile["accepted_diagonal_profile_theorem_closed"] is True, "candidate lost diagonal closure")
    require(profile["full_profile_likelihood_or_accepted_diagonal_theorem_closed"] is True, "candidate lost profile/diagonal closure")
    require(profile["full_covariance_profile_likelihood_closed"] is False, "candidate overcloses full covariance")
    require(profile["profile_row_count"] == diagonal["profile_row_count"] == 6, "profile row count mismatch")
    require(close(profile["chi2_diagonal"], diagonal["chi2_diagonal"]), "chi2 mismatch")
    require(close(profile["reduced_chi2_diagonal"], diagonal["reduced_chi2_diagonal"]), "reduced chi2 mismatch")
    require(close(profile["max_abs_pull"], diagonal["max_abs_pull"]), "max pull mismatch")

    ready = candidate["readiness_after_import"]
    require(readiness["present_count"] == 8 and readiness["requirement_count"] == 9, "source readiness not 8/9")
    require(ready["post_pi_external_profile_readiness"] == "8/9", "candidate readiness not 8/9")
    require(ready["remaining_blocking_failures"] == ["no_knob_value_derivation"], "remaining blocker mismatch")
    require(ready["accepted_coefficient_value_count"] == 0, "candidate overclaims coefficient values")
    require(ready["accepted_lambda_H_value"] is False, "candidate overclaims lambda_H")
    require(ready["selected_threshold_response_functional_value_instantiated"] is False, "candidate overinstantiates values")
    require(ready["selected_internal_Rtheta_threshold_mass_derivation_closed"] is False, "candidate overcloses internal derivation")
    require(ready["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")
    require(ready["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")
    require(ready["full_no_knob_closed"] is False, "candidate overclaims no-knob")

    decision = candidate["frontier_decision"]
    require(decision["threshold_mass_row_profile_exit_closed_at_admitted_external_tier"] is True, "decision did not close external/profile exit")
    require(decision["internal_no_knob_value_derivation_closed"] is False, "decision overcloses no-knob")
    require(decision["minimal_universal_parameter_policy_needed_if_no_internal_derivation"] is True, "decision lost minimal-parameter policy flag")
    require(decision["current_final_blocker"] == "no_knob_value_derivation", "final blocker changed")

    require(cert["threshold_matching_source_rows_closed"] is True, "certificate threshold rows not closed")
    require(cert["mass_scheme_conversion_source_rows_closed"] is True, "certificate mass rows not closed")
    require(cert["closed_at_admitted_external_tier_only"] is True, "certificate tier guard missing")
    require(cert["accepted_external_threshold_row_count"] == 7, "certificate threshold count mismatch")
    require(cert["accepted_external_mass_scheme_row_count"] == 3, "certificate mass count mismatch")
    require(cert["accepted_internal_selected_Rtheta_threshold_mass_row_count"] == 0, "certificate overclaims internal Rtheta rows")
    require(cert["accepted_diagonal_profile_theorem_closed"] is True, "certificate diagonal closure missing")
    require(cert["full_profile_likelihood_or_accepted_diagonal_theorem_closed"] is True, "certificate profile/diagonal closure missing")
    require(cert["full_covariance_profile_likelihood_closed"] is False, "certificate overcloses full covariance")
    require(cert["post_pi_external_profile_readiness"] == "8/9", "certificate readiness mismatch")
    require(cert["remaining_blocking_failure"] == "no_knob_value_derivation", "certificate final blocker mismatch")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["true_SM_equivalence_closed"] is False, "certificate overclaims true SM")
    require(cert["full_no_knob_closed"] is False, "certificate overclaims no-knob")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit.candidate.json",
                "status": candidate["status"],
                "external_threshold_rows": 7,
                "external_mass_rows": 3,
                "diagonal_profile": "closed",
                "readiness": "8/9",
                "remaining_blocker": "no_knob_value_derivation",
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected threshold/mass profile-exit import audit passed")


if __name__ == "__main__":
    main()
