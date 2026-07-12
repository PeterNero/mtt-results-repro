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
    candidate = load_json("candidate_data/selected_valuesourceanchorrows_or_internalnoknobvalueemission.candidate.json")
    cert = load_json("certificates/selected_valuesourceanchorrows_or_internalnoknobvalueemission_certificate.json")
    internal_rtheta = load_json("certificates/selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier_certificate.json")
    basis = load_json("certificates/selected_rthetavaluerows_or_universalsourceanchortheorem_certificate.json")
    coeff = load_json("certificates/selected_rtheta_coefficientfunctional_or_universalanchorselection_certificate.json")
    evaluator = load_json("certificates/selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_certificate.json")
    step52 = load_json("certificates/selected_step52_vsd02_strict_value_source_frontier_or_likelihoodworkspace_certificate.json")
    vsd02_rule = load_json("certificates/selected_vsd02thresholdresponserule_or_externallikelihoodimport_certificate.json")
    vsd02_fill = load_json("certificates/selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation_certificate.json")
    rtheta_vsd02 = load_json("candidate_data/selected_rtheta_vsd02strictreplay_or_responsefunctionalroute.candidate.json")
    atomic = load_json("certificates/selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition_certificate.json")
    likelihood = load_json("certificates/selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["closure_claimed"] is False, "must not claim closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")

    domain = candidate["domain_and_contract_closed"]
    require(internal_rtheta["physical_PhiFinC1_action_source_closed_at_VSD01_source_assembly_scope"] is True, "internal Rtheta VSD01 action source not closed")
    require(internal_rtheta["all_72_row_values_exact"] is True, "internal Rtheta VSD01 72 rows not exact")
    require(internal_rtheta["internal_Rtheta_scalar_rows_accepted"] == 0, "internal Rtheta VSD01 overclaims scalar rows")
    require(basis["basis_map_to_sector_scaled_magnitude_rows_closed"] is True, "Rtheta basis map not closed")
    require(basis["charged_basis_row_count"] == 9, "charged basis row count changed")
    require(basis["required_charged_generation_row_count"] == 9, "required charged rows changed")
    require(coeff["coefficient_functional_skeleton_closed"] is True, "coefficient skeleton not closed")
    require(coeff["domain_readiness_closed"] is True, "coefficient domain readiness not closed")
    require(coeff["domain_present_count_after_update"] == coeff["domain_requirement_count"] == 5, "coefficient domain not 5/5")
    require(evaluator["Pi_Rtheta_closed"] is True, "Pi_Rtheta not closed")
    require(evaluator["selected_dynamic_operator_source_owner_closed"] is True, "dynamic operator source owner not closed")
    require(step52["strict_accepted_source_row_schema_closed"] is True, "strict accepted-source schema not closed")
    require(atomic["no_observed_selector_proof_closed"] is True, "no observed selector proof not closed")
    require(domain["internal_Rtheta_dynamic_source_blocker_consumed"] is True, "candidate lost internal Rtheta source-blocker consumption")
    require(domain["basis_map_to_sector_scaled_magnitude_rows_closed"] is True, "candidate lost basis map")
    require(domain["charged_basis_row_count"] == 9, "candidate charged row count mismatch")
    require(domain["higher_response_codomain_scalar_row_count"] == 10, "candidate codomain row count mismatch")
    require(domain["coefficient_domain_present_count"] == domain["coefficient_domain_requirement_count"] == 5, "candidate coefficient domain mismatch")
    require(domain["Pi_Rtheta_closed"] is True, "candidate lost Pi_Rtheta")
    require(domain["strict_accepted_source_row_schema_closed"] is True, "candidate lost strict schema")

    attempt = candidate["strict_value_source_anchor_attempt"]
    require(step52["candidate_source_rows_tested"] == 6, "candidate source row test count changed")
    require(len(rtheta_vsd02["atomic_routes"]) == 3, "atomic route count changed")
    require(step52["accepted_vsd02_source_row_count"] == 0, "VSD02 rows unexpectedly accepted")
    require(step52["accepted_internal_Rtheta_coefficient_row_count"] == 0, "internal Rtheta coefficients unexpectedly accepted")
    require(step52["accepted_internal_scalar_row_count"] == 0, "internal scalar rows unexpectedly accepted")
    require(step52["selected_lambda_H_row_closed"] is False, "lambda_H row unexpectedly closed")
    require(step52["selected_threshold_response_functional_closed"] is False, "threshold response functional unexpectedly closed")
    require(vsd02_rule["what_closes"]["row_route_classification"] is True, "row route classification not closed")
    require(vsd02_fill["what_closes"]["all_current_candidates_tested_against_schema"] is True, "current candidates not tested")
    require(vsd02_fill["what_closes"]["strict_accepted_source_row_schema"] is True, "fill did not retain strict schema")
    require(attempt["candidate_source_rows_tested"] == 6, "candidate attempt source row count mismatch")
    require(attempt["atomic_route_count"] == 3, "candidate atomic route count mismatch")
    require(attempt["accepted_vsd02_source_row_count"] == 0, "candidate overclaims VSD02 rows")
    require(attempt["accepted_internal_Rtheta_coefficient_row_count"] == 0, "candidate overclaims Rtheta coefficients")
    require(attempt["accepted_internal_scalar_row_count"] == 0, "candidate overclaims scalar rows")
    require(attempt["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")

    external = candidate["external_profile_boundary"]
    require(likelihood["external_profile_replay_closed_under_declared_standard"] is True, "external replay boundary not closed")
    require(likelihood["published_or_reconstructed_8x8_profile_likelihood_imported"] is False, "8x8 likelihood unexpectedly imported")
    require(likelihood["full_covariance_profile_likelihood_closed"] is False, "full covariance likelihood unexpectedly closed")
    require(likelihood["selected_Rtheta_source_rows_closed"] is False, "selected Rtheta rows unexpectedly closed")
    require(external["external_profile_replay_closed_under_declared_standard"] is True, "candidate lost external replay support")
    require(external["full_covariance_profile_likelihood_closed"] is False, "candidate overclaims full likelihood")
    require(external["selected_Rtheta_source_rows_closed"] is False, "candidate overclaims selected Rtheta rows")

    require(cert["candidate_source_rows_tested"] == 6, "certificate source row count mismatch")
    require(cert["atomic_route_count"] == 3, "certificate atomic route count mismatch")
    require(cert["accepted_internal_scalar_row_count"] == 0, "certificate overclaims scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_valuesourceanchorrows_or_internalnoknobvalueemission.candidate.json",
                "status": candidate["status"],
                "domain_contract": "closed",
                "charged_basis_rows": 9,
                "higher_response_codomain_rows": 10,
                "candidate_source_rows_tested": 6,
                "atomic_routes": 3,
                "accepted_internal_rows": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected value-source anchor rows audit passed")


if __name__ == "__main__":
    main()
