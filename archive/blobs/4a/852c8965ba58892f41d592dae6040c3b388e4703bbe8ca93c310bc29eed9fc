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
    candidate = load_json("candidate_data/selected_internalnoknobvaluerows_or_fullcovarianceprofilelikelihoodexecution.candidate.json")
    cert = load_json("certificates/selected_internalnoknobvaluerows_or_fullcovarianceprofilelikelihoodexecution_certificate.json")
    policy = load_json("certificates/selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy_certificate.json")
    full_cov = load_json("certificates/selected_fullcovarianceprofile_or_selectedrthetasourcerows_certificate.json")
    sidecar = load_json("certificates/selected_covariancesidecarfill_or_rthetasourcerowderivation_certificate.json")
    threshold_cov = load_json("certificates/selected_thresholdmassschemecovariancefill_or_qasu3packetintegration_certificate.json")
    internal_rtheta = load_json("certificates/selected_internalrthetavaluederivation_or_minimaluniversalparameterselection_certificate.json")
    scalar_functional = load_json("certificates/selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(policy["minimal_universal_parameter_policy_closed"] is True, "policy not closed")
    require(policy["post_pi_external_profile_readiness"] == "8/9", "policy readiness changed")
    require(policy["external_rows_count_as_internal_no_knob_source_rows"] is False, "policy promotes external rows")
    require(policy["no_knob_value_derivation_closed"] is False, "policy overcloses no-knob")

    require(full_cov["block_coverage_matrix_closed"] is True, "full covariance block coverage not closed")
    require(full_cov["external_value_layer_broadly_populated"] is True, "external value layer not populated")
    require(full_cov["full_covariance_profile_likelihood_closed"] is False, "full covariance likelihood overclosed")
    require(full_cov["selected_Rtheta_source_rows_closed"] is False, "Rtheta source rows overclosed")
    require(full_cov["true_SM_equivalence_closed"] is False, "full covariance cert overclaims true SM")

    require(sidecar["WZH_interim_covariance_sidecars_closed"] is True, "WZH sidecars not closed")
    require(sidecar["interim_block_diagonal_profile_available"] is True, "interim diagonal profile missing")
    require(sidecar["full_covariance_profile_likelihood_closed"] is False, "sidecar overcloses full covariance")
    require(sidecar["selected_Rtheta_source_rows_closed"] is False, "sidecar overcloses Rtheta rows")

    require(threshold_cov["what_closes"]["threshold_mass_scheme_covariance_contract_built"] is True, "threshold covariance contract missing")
    require(threshold_cov["what_closes"]["source_gate_kept_separate_from_value_transport"] is True, "source/value separation missing")
    require(threshold_cov["what_remains_open"]["profile_likelihood_or_covariance_matrix"] is True, "profile likelihood no longer open")
    require(threshold_cov["what_remains_open"]["threshold_matching_values"] is True, "threshold matching values no longer open")
    require(threshold_cov["what_remains_open"]["mass_scheme_conversion_values"] is True, "mass scheme values no longer open")

    require(internal_rtheta["dynamic_first_response_layer_closed"] is True, "dynamic first response not closed")
    require(internal_rtheta["first_response_only_route_rejected_for_scalar_no_knob_values"] is True, "first response no-go missing")
    require(internal_rtheta["selected_internal_value_emission_count"] == 0, "internal Rtheta overemits values")
    require(internal_rtheta["accepted_coefficient_value_count"] == 0, "internal Rtheta overaccepts coefficients")
    require(internal_rtheta["selected_threshold_response_functional_instantiated"] is False, "internal Rtheta overinstantiates functional")
    require(internal_rtheta["lambda_H_value_execution"] is False, "internal Rtheta overemits lambda_H")
    require(internal_rtheta["no_knob_value_derivation_closed"] is False, "internal Rtheta overcloses no-knob")

    require(scalar_functional["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True, "scalar functional source domain not closed")
    require(scalar_functional["ten_scalar_row_codomain_aligned"] is True, "ten scalar codomain not aligned")
    require(scalar_functional["no_knob_numerical_rows_emitted"] is False, "scalar functional overemits numerical rows")
    require(scalar_functional["accepted_value_layer_closed"] is False, "scalar functional overcloses value layer")

    readiness = candidate["closed_readiness"]
    for key in [
        "minimal_universal_parameter_policy_closed",
        "threshold_matching_source_rows_closed_at_admitted_external_tier",
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier",
        "accepted_diagonal_profile_theorem_closed",
        "block_coverage_matrix_closed",
        "interim_covariance_sidecars_closed",
        "threshold_mass_scheme_covariance_contract_built",
        "selected_Rtheta_scalar_value_functional_source_domain_closed",
        "ten_scalar_row_codomain_aligned",
        "dynamic_first_response_layer_closed",
        "first_response_only_route_rejected_for_scalar_no_knob_values",
    ]:
        require(readiness[key] is True, f"readiness flag missing: {key}")
    require(readiness["post_pi_external_profile_readiness"] == "8/9", "candidate readiness changed")

    exit_a = candidate["exit_A_internal_no_knob_value_rows"]
    require(exit_a["selected_Rtheta_source_rows_closed"] is False, "exit A overcloses Rtheta rows")
    require(exit_a["selected_internal_Rtheta_threshold_mass_derivation_closed"] is False, "exit A overcloses internal derivation")
    require(exit_a["selected_threshold_response_functional_value_instantiated"] is False, "exit A overinstantiates functional")
    require(exit_a["no_knob_numerical_rows_emitted"] is False, "exit A overemits numerical rows")
    require(exit_a["selected_internal_value_emission_count"] == 0, "exit A overemits values")
    require(exit_a["accepted_coefficient_value_count"] == 0, "exit A overaccepts coefficients")
    require(exit_a["accepted_lambda_H_value"] is False, "exit A overaccepts lambda_H")
    require(exit_a["accepted_true_equivalence_precision_rows"] == 0, "exit A overclaims precision rows")

    exit_b = candidate["exit_B_full_covariance_profile_likelihood"]
    require(exit_b["external_value_layer_broadly_populated"] is True, "exit B lost external value layer")
    require(exit_b["interim_block_diagonal_profile_available"] is True, "exit B lost interim profile")
    require(exit_b["WZH_interim_covariance_sidecars_closed"] is True, "exit B lost WZH sidecars")
    require(exit_b["full_covariance_profile_likelihood_closed"] is False, "exit B overcloses covariance likelihood")
    require(exit_b["accepted_as_official_profile_workspace"] is False, "exit B overaccepts official workspace")
    require(exit_b["profile_likelihood_or_covariance_matrix_still_open"] is True, "exit B no longer open")

    guards = candidate["guards"]
    require(guards["external_rows_count_as_internal_no_knob_source_rows"] is False, "candidate promotes external rows")
    require(guards["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(guards["target_fitting_used"] is False, "candidate uses target fitting")
    require(guards["hidden_per_sector_or_per_row_knobs_allowed"] is False, "candidate allows hidden knobs")
    require(guards["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")
    require(guards["full_no_knob_closed"] is False, "candidate overclaims no-knob")

    decision = candidate["decision"]
    require(decision["two_exit_fork_ready"] is True, "two-exit fork not ready")
    require(decision["exit_A_closed"] is False, "decision overcloses exit A")
    require(decision["exit_B_closed"] is False, "decision overcloses exit B")
    require(decision["remaining_exit_count"] == 2, "remaining exit count changed")
    require(cert["two_exit_fork_ready"] is True, "certificate two-exit fork not ready")
    require(cert["remaining_exit_count"] == 2, "certificate exit count changed")
    require(cert["true_SM_equivalence_closed"] is False, "certificate overclaims true SM")
    require(cert["full_no_knob_closed"] is False, "certificate overclaims no-knob")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "two_exit_fork_ready": True,
                "exit_A_internal_rows_closed": cert["exit_A_closed"],
                "exit_B_full_covariance_closed": cert["exit_B_closed"],
                "remaining_exit_count": cert["remaining_exit_count"],
                "preferred_next_artifact": cert["preferred_next_artifact"],
            },
            indent=2,
        )
    )
    print("selected internal no-knob/full-covariance fork audit passed")


if __name__ == "__main__":
    main()
