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
    candidate = load_json("candidate_data/selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission.candidate.json")
    cert = load_json("certificates/selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission_certificate.json")
    fork = load_json("certificates/selected_internalnoknobvaluerows_or_fullcovarianceprofilelikelihoodexecution_certificate.json")
    published = load_json("certificates/selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission_certificate.json")
    external = load_json("certificates/selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof_certificate.json")
    higgs = load_json("certificates/selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure_certificate.json")
    cross_basis = load_json("certificates/selected_crossblockcovariance_or_rthetacoefficientvaluefill_certificate.json")
    cross_values = load_json("certificates/selected_crossblockcovariancevalues_or_rthetacoefficientexecution_certificate.json")
    scalar_functional = load_json("certificates/selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows_certificate.json")
    internal = load_json("certificates/selected_internalrthetavaluederivation_or_minimaluniversalparameterselection_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(fork["two_exit_fork_ready"] is True, "two-exit fork not ready")
    require(fork["exit_A_closed"] is False, "prior fork already closed exit A")
    require(fork["exit_B_closed"] is False, "prior fork already closed exit B")

    require(higgs["accepted_Higgs_decay_covariance_profile_closed"] is True, "Higgs decay covariance not closed")
    require(higgs["first_selected_QaSU3_static_slot_closed"] is True, "first Qa/SU3 static slot not closed")
    require(higgs["full_Higgs_likelihood_profile_closed"] is False, "Higgs likelihood overclosed")
    require(external["external_higgs_decay_covariance_profile_candidate_imported"] is True, "external covariance candidate missing")
    require(external["full_profile_likelihood_function_imported"] is False, "external likelihood unexpectedly imported")
    require(published["external_profile_replay_closed_under_declared_standard"] is True, "published replay boundary not closed")
    require(published["published_or_reconstructed_8x8_profile_likelihood_imported"] is False, "published 8x8 likelihood unexpectedly imported")
    require(published["full_covariance_profile_likelihood_closed"] is False, "published cert overcloses covariance likelihood")

    route_a = candidate["route_A_full_covariance_workspace_attempt"]
    require(route_a["accepted_Higgs_decay_covariance_profile_closed"] is True, "route A lost Higgs covariance")
    require(route_a["first_selected_QaSU3_static_slot_closed"] is True, "route A lost static slot")
    require(route_a["external_higgs_decay_covariance_profile_candidate_imported"] is True, "route A lost external candidate")
    require(route_a["external_profile_replay_closed_under_declared_standard"] is True, "route A lost external replay")
    require(route_a["published_or_reconstructed_8x8_profile_likelihood_imported"] is False, "route A overimports 8x8 likelihood")
    require(route_a["full_profile_likelihood_function_imported"] is False, "route A overimports likelihood function")
    require(route_a["full_Higgs_likelihood_profile_closed"] is False, "route A overcloses Higgs likelihood")
    require(route_a["full_covariance_profile_likelihood_closed"] is False, "route A overcloses full covariance")
    require(route_a["accepted_as_official_profile_workspace"] is False, "route A overaccepts official workspace")
    require(route_a["route_A_closed"] is False, "route A overclosed")

    require(scalar_functional["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True, "scalar source domain not closed")
    require(scalar_functional["ten_scalar_row_codomain_aligned"] is True, "ten scalar codomain not aligned")
    require(scalar_functional["no_knob_numerical_rows_emitted"] is False, "scalar functional overemits rows")
    require(cross_basis["deduplicated_cross_block_covariance_basis_closed"] is True, "cross-block basis not closed")
    require(cross_basis["deduplicated_interim_row_count"] == 19, "cross-block basis row count changed")
    require(cross_basis["Rtheta_coefficient_values_closed"] is False, "cross basis overcloses coefficients")
    require(cross_values["numeric_interim_block_covariance_matrix_closed"] is True, "numeric interim matrix not closed")
    require(cross_values["numeric_cross_block_covariance_values_closed"] is False, "cross values overclose numeric covariance")
    require(cross_values["Rtheta_coefficient_values_closed"] is False, "cross values overclose Rtheta coefficients")
    require(internal["selected_internal_value_emission_count"] == 0, "internal Rtheta overemits values")
    require(internal["accepted_coefficient_value_count"] == 0, "internal Rtheta overaccepts coefficients")
    require(internal["lambda_H_value_execution"] is False, "internal Rtheta overexecutes lambda_H")

    route_b = candidate["route_B_internal_rtheta_value_rows_attempt"]
    require(route_b["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True, "route B lost scalar domain")
    require(route_b["ten_scalar_row_codomain_aligned"] is True, "route B lost scalar codomain")
    require(route_b["deduplicated_cross_block_covariance_basis_closed"] is True, "route B lost covariance basis")
    require(route_b["numeric_interim_block_covariance_matrix_closed"] is True, "route B lost interim matrix")
    require(route_b["deduplicated_interim_row_count"] == 19, "route B row count changed")
    require(route_b["selected_Rtheta_source_rows_closed"] is False, "route B overcloses Rtheta rows")
    require(route_b["Rtheta_coefficient_values_closed"] is False, "route B overcloses coefficient values")
    require(route_b["numeric_cross_block_covariance_values_closed"] is False, "route B overcloses cross values")
    require(route_b["no_knob_numerical_rows_emitted"] is False, "route B overemits no-knob rows")
    require(route_b["selected_internal_value_emission_count"] == 0, "route B overemits internal values")
    require(route_b["accepted_coefficient_value_count"] == 0, "route B overaccepts coefficients")
    require(route_b["accepted_lambda_H_value"] is False, "route B overaccepts lambda_H")
    require(route_b["route_B_closed"] is False, "route B overclosed")

    req = candidate["reduced_payload_requirements"]
    require(req["route_A_missing_payload"] == "accepted_full_likelihood_function_or_official_profile_workspace", "route A missing payload changed")
    require(req["route_B_missing_payload"] == "selected_Rtheta_coefficient_value_rows_or_internal_no_knob_numerical_rows", "route B missing payload changed")
    guards = candidate["guards"]
    require(guards["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(guards["target_fitting_used"] is False, "candidate uses target fitting")
    require(guards["external_rows_count_as_internal_no_knob_source_rows"] is False, "candidate promotes external rows")
    require(guards["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")
    require(guards["full_no_knob_closed"] is False, "candidate overclaims no-knob")

    decision = candidate["decision"]
    require(decision["direct_execution_attempt_closed"] is True, "direct execution attempt not closed")
    require(decision["route_A_closed"] is False, "decision overcloses route A")
    require(decision["route_B_closed"] is False, "decision overcloses route B")
    require(decision["remaining_payload_count"] == 2, "remaining payload count changed")
    require(cert["remaining_payload_count"] == 2, "certificate payload count changed")
    require(cert["true_SM_equivalence_closed"] is False, "certificate overclaims true SM")
    require(cert["full_no_knob_closed"] is False, "certificate overclaims no-knob")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "direct_execution_attempt_closed": True,
                "route_A_closed": cert["route_A_full_covariance_workspace_closed"],
                "route_B_closed": cert["route_B_internal_rtheta_value_rows_closed"],
                "remaining_payload_count": cert["remaining_payload_count"],
                "preferred_next_artifact": cert["preferred_next_artifact"],
            },
            indent=2,
        )
    )
    print("selected full-covariance/internal-Rtheta execution audit passed")


if __name__ == "__main__":
    main()
