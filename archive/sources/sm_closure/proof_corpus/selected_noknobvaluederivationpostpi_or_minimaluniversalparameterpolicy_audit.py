from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    candidate = load_json("candidate_data/selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy.candidate.json")
    cert = load_json("certificates/selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy_certificate.json")
    profile_exit = load_json("certificates/selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit_certificate.json")
    limitation = load_json("certificates/selected_valuesourceanchoremission_or_noknoblimitationtheorem_certificate.json")
    minimal = load_json("certificates/selected_fullsmminimalparameterledger_or_strictpewsourcetheorem_certificate.json")
    consolidated = load_json("certificates/current_true_sm_closure_consolidated_ledger_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "policy theorem not proved")
    require(candidate["closure_claimed"] is False, "candidate overclaims full closure")
    require(cert["closure_claimed"] is False, "certificate overclaims full closure")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(cert["target_fitting_used"] is False, "target fitting must remain false")
    require(cert["observed_data_used_as_selector"] is False, "observed selector use must remain false")

    require(profile_exit["threshold_matching_source_rows_closed"] is True, "profile exit threshold rows not closed")
    require(profile_exit["mass_scheme_conversion_source_rows_closed"] is True, "profile exit mass rows not closed")
    require(profile_exit["closed_at_admitted_external_tier_only"] is True, "profile exit lost external-tier guard")
    require(profile_exit["accepted_external_threshold_row_count"] == 7, "profile exit threshold count changed")
    require(profile_exit["accepted_external_mass_scheme_row_count"] == 3, "profile exit mass count changed")
    require(profile_exit["accepted_diagonal_profile_theorem_closed"] is True, "profile exit diagonal theorem missing")
    require(profile_exit["post_pi_external_profile_readiness"] == "8/9", "profile exit readiness changed")
    require(profile_exit["selected_internal_Rtheta_threshold_mass_derivation_closed"] is False, "profile exit overcloses internal derivation")
    require(profile_exit["accepted_internal_selected_Rtheta_threshold_mass_row_count"] == 0, "profile exit overclaims internal rows")
    require(profile_exit["selected_threshold_response_functional_value_instantiated"] is False, "profile exit overinstantiates values")
    require(profile_exit["accepted_coefficient_value_count"] == 0, "profile exit overclaims coefficients")
    require(profile_exit["accepted_lambda_H_value"] is False, "profile exit overclaims lambda_H")
    require(profile_exit["accepted_true_equivalence_precision_rows"] == 0, "profile exit overclaims true precision")
    require(profile_exit["full_no_knob_closed"] is False, "profile exit overclaims no-knob")

    post_pi = candidate["post_pi_state"]
    require(post_pi["threshold_matching_source_rows_closed"] is True, "candidate lost threshold row closure")
    require(post_pi["mass_scheme_conversion_source_rows_closed"] is True, "candidate lost mass row closure")
    require(post_pi["closed_at_admitted_external_tier_only"] is True, "candidate lost tier guard")
    require(post_pi["accepted_external_threshold_row_count"] == 7, "candidate threshold count changed")
    require(post_pi["accepted_external_mass_scheme_row_count"] == 3, "candidate mass count changed")
    require(post_pi["accepted_diagonal_profile_theorem_closed"] is True, "candidate lost diagonal theorem")
    require(post_pi["post_pi_external_profile_readiness"] == "8/9", "candidate readiness changed")

    boundary = candidate["internal_no_knob_boundary"]
    require(boundary["selected_internal_Rtheta_threshold_mass_derivation_closed"] is False, "candidate overcloses internal Rtheta derivation")
    require(boundary["accepted_internal_selected_Rtheta_threshold_mass_row_count"] == 0, "candidate overclaims internal threshold/mass rows")
    require(boundary["selected_threshold_response_functional_value_instantiated"] is False, "candidate overinstantiates threshold response values")
    require(boundary["accepted_coefficient_value_count"] == 0, "candidate overclaims coefficient values")
    require(boundary["accepted_lambda_H_value"] is False, "candidate overclaims lambda_H")
    require(boundary["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")
    require(boundary["full_covariance_profile_likelihood_closed"] is False, "candidate overcloses full covariance")
    require(boundary["no_knob_value_derivation_closed"] is False, "candidate overcloses no-knob value derivation")
    require(boundary["full_no_knob_closed"] is False, "candidate overclaims full no-knob")
    require(boundary["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")

    require(limitation["current_inventory_limitation_closed"] is True, "current inventory limitation not closed")
    require(limitation["current_inventory_emits_value_source_anchor_rows"] is False, "current inventory now emits rows unexpectedly")
    require(limitation["accepted_internal_scalar_rows_after_all_current_attempts"] == 0, "limitation overclaims scalar rows")
    require(limitation["accepted_Rtheta_source_rows_after_all_current_attempts"] == 0, "limitation overclaims Rtheta rows")
    require(limitation["accepted_threshold_response_source_rows_after_all_current_attempts"] == 0, "limitation overclaims threshold rows")
    require(limitation["lawful_exit_count"] == 3, "limitation exit count changed")

    policy = candidate["minimal_universal_parameter_policy"]
    require(policy["policy_closed"] is True, "minimal policy not closed")
    require(policy["current_closure_standard"] == "one-shared-physical-primitive SM closure", "policy standard changed")
    require(policy["shared_physical_primitive"] == "P_EW", "shared primitive changed")
    require(policy["shared_physical_primitive_count"] == 1, "shared primitive count changed")
    require(policy["H_specific_parameter_count"] == 0, "H-specific parameter count changed")
    require(policy["lambda_H_independent_parameter_replaced"] is True, "lambda_H replacement lost")
    require(policy["external_threshold_mass_profile_rows_are_replay_tier"] is True, "external rows tier guard lost")
    require(policy["external_rows_count_as_internal_no_knob_source_rows"] is False, "external rows promoted to internal rows")
    require(policy["hidden_per_sector_or_per_row_knobs_allowed"] is False, "hidden knobs allowed")
    require(policy["observed_values_allowed_as_selectors"] is False, "observed selectors allowed")
    require(policy["target_fitting_used"] is False, "policy target fitting changed")

    require(minimal["full_SM_minimal_parameter_ledger_closed"] is True, "minimal parameter ledger not closed")
    require(minimal["P_EW_counted_as_shared_physical_primitive"] is True, "minimal ledger lost P_EW primitive")
    require(minimal["P_EW_parameter_count"] == 1, "minimal ledger P_EW count changed")
    require(minimal["H_specific_parameter_count"] == 0, "minimal ledger H-specific count changed")
    require(minimal["lambda_H_independent_parameter_replaced"] is True, "minimal ledger lambda_H replacement lost")
    require(minimal["full_no_knob_closure_claimed"] is False, "minimal ledger overclaims no-knob")
    require(minimal["true_SM_equivalence_claimed"] is False, "minimal ledger overclaims true SM")

    require(consolidated["threshold_response_first_exit_readiness"] == "8/9", "consolidated readiness not 8/9")
    require(consolidated["threshold_matching_source_rows_closed"] is True, "consolidated threshold rows not closed")
    require(consolidated["mass_scheme_conversion_source_rows_closed"] is True, "consolidated mass rows not closed")
    require(consolidated["closed_at_admitted_external_tier_only"] is True, "consolidated tier guard missing")
    require(consolidated["accepted_internal_selected_Rtheta_threshold_mass_row_count"] == 0, "consolidated overclaims internal rows")
    require(consolidated["full_no_knob_closed"] is False, "consolidated overclaims no-knob")
    # This packet predates the multi-loop precision and observable-functor
    # successors. Its own no-knob boundary remains open, while the consolidated
    # ledger now closes the explicitly weaker one-shared-primitive/profile tier.
    require(consolidated["true_SM_equivalence_closed"] is True, "consolidated successor lost scoped true-SM closure")
    require(
        consolidated["true_SM_equivalence_scope"]
        == "embedded renormalized-SM equivalence at the adopted one-shared-physical-primitive/profile standard",
        "consolidated successor changed closure scope",
    )

    require(cert["minimal_universal_parameter_policy_closed"] is True, "certificate policy not closed")
    require(cert["shared_physical_primitive_count"] == 1, "certificate primitive count changed")
    require(cert["H_specific_parameter_count"] == 0, "certificate H-specific count changed")
    require(cert["external_rows_count_as_internal_no_knob_source_rows"] is False, "certificate promotes external rows")
    require(cert["no_knob_value_derivation_closed"] is False, "certificate overcloses no-knob value derivation")
    require(cert["remaining_blocker"] == "selected_internal_no_knob_value_rows_or_full_covariance_profile_likelihood", "certificate remaining blocker changed")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "policy": "one-shared-physical-primitive",
                "shared_primitive_count": cert["shared_physical_primitive_count"],
                "H_specific_parameter_count": cert["H_specific_parameter_count"],
                "external_profile_readiness": cert["post_pi_external_profile_readiness"],
                "internal_no_knob_rows": cert["accepted_internal_selected_Rtheta_threshold_mass_row_count"],
                "historical_true_precision_rows": cert["accepted_true_equivalence_precision_rows"],
                "current_true_precision_rows": consolidated["accepted_true_equivalence_precision_rows"],
                "scoped_true_SM_equivalence_closed": consolidated["true_SM_equivalence_closed"],
                "remaining_strict_upgrade": "selected_internal_no_knob_value_rows",
            },
            indent=2,
        )
    )
    print("selected no-knob value derivation policy audit passed")


if __name__ == "__main__":
    main()
