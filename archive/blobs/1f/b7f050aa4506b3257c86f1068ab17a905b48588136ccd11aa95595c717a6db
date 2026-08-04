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
    candidate = load_json("candidate_data/selected_valuesourceanchoremission_or_noknoblimitationtheorem.candidate.json")
    cert = load_json("certificates/selected_valuesourceanchoremission_or_noknoblimitationtheorem_certificate.json")
    anchor = load_json("certificates/selected_valuesourceanchorrows_or_internalnoknobvalueemission_certificate.json")
    threshold_scheme = load_json("certificates/selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution_certificate.json")
    internal_threshold = load_json("certificates/selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision_certificate.json")
    public8x8 = load_json("certificates/selected_public8x8likelihoodsearch_or_routecsourceemissionexecution_certificate.json")
    kernel = load_json("certificates/selected_noknobvaluederivationkernel_or_sourceanchortheorem_certificate.json")
    diagonal = load_json("certificates/selected_thresholdrows_or_diagonalprofilelimitationtheorem_certificate.json")
    likelihood = load_json("certificates/selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission_certificate.json")
    step52 = load_json("certificates/selected_step52_vsd02_strict_value_source_frontier_or_likelihoodworkspace_certificate.json")
    atomic = load_json("certificates/selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "must not claim closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(candidate["theorem"]["proved"] is True, "limitation theorem not proved")
    require(cert["current_inventory_limitation_closed"] is True, "certificate did not close current-inventory limitation")
    require(cert["current_inventory_emits_value_source_anchor_rows"] is False, "certificate overclaims value-source anchor emission")

    inv = candidate["current_selected_source_inventory"]
    require(anchor["internal_Rtheta_dynamic_source_blocker_consumed"] is True, "anchor input lost internal Rtheta source blocker consumption")
    require(anchor["basis_map_to_sector_scaled_magnitude_rows_closed"] is True, "anchor input lost basis map")
    require(anchor["coefficient_domain_readiness_closed"] is True, "anchor input lost coefficient domain readiness")
    require(anchor["Pi_Rtheta_closed"] is True, "anchor input lost Pi_Rtheta")
    require(anchor["selected_dynamic_operator_source_owner_closed"] is True, "anchor input lost source owner")
    require(anchor["strict_accepted_source_row_schema_closed"] is True, "anchor input lost strict row schema")
    require(anchor["no_observed_selector_proof_closed"] is True, "anchor input lost no-observed selector proof")
    require(inv["charged_basis_row_count"] == anchor["charged_basis_row_count"] == 9, "charged basis count changed")
    require(inv["higher_response_codomain_scalar_row_count"] == anchor["higher_response_codomain_scalar_row_count"] == 10, "higher-response codomain count changed")

    attempts = candidate["emission_attempts_already_exhausted_under_current_inventory"]
    require(anchor["candidate_source_rows_tested"] == attempts["strict_value_source_anchor_candidate_rows_tested"] == 6, "strict source-row test count changed")
    require(anchor["atomic_route_count"] == attempts["strict_value_source_anchor_atomic_route_count"] == 3, "strict atomic route count changed")
    require(anchor["accepted_internal_scalar_row_count"] == attempts["strict_value_source_anchor_accepted_internal_rows"] == 0, "strict anchor rows unexpectedly accepted")
    require(step52["candidate_source_rows_tested"] == 6, "step52 source-row count changed")
    require(step52["accepted_vsd02_source_row_count"] == 0, "VSD02 rows unexpectedly accepted")
    require(step52["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta coefficient rows unexpectedly accepted")
    require(step52["accepted_internal_scalar_row_count"] == 0, "internal scalar rows unexpectedly accepted")
    require(atomic["no_observed_selector_proof_closed"] is True, "atomic no-observed selector proof not closed")
    require(atomic["selected_threshold_response_functional_instantiated"] is False, "threshold response functional unexpectedly instantiated")

    require(threshold_scheme["one_to_three_anchor_model_search_executed"] is True, "universal-anchor search not executed")
    require(threshold_scheme["one_to_three_current_source_anchor_sufficient"] is False, "current universal anchor unexpectedly sufficient")
    require(threshold_scheme["accepted_source_anchor_row_count"] == 0, "universal-anchor source rows unexpectedly accepted")
    require(threshold_scheme["accepted_internal_scalar_value_row_count"] == 0, "universal-anchor scalar rows unexpectedly accepted")
    require(internal_threshold["source_selected_execution_workorder_built"] is True, "internal threshold workorder not built")
    require(internal_threshold["internal_threshold_response_value_rows_emitted"] is False, "internal threshold response rows unexpectedly emitted")
    require(internal_threshold["accepted_internal_scalar_value_row_count"] == 0, "internal threshold scalar rows unexpectedly accepted")
    require(kernel["final_no_knob_kernel_typed"] is True, "final no-knob kernel not typed")
    require(kernel["selected_internal_value_emission_count"] == 0, "kernel unexpectedly emits internal values")
    require(public8x8["no_knob_exact_primitive_seed_backimported"] is True, "primitive seed exactness not backimported")
    require(public8x8["public_8x8_likelihood_found"] is False, "public 8x8 likelihood unexpectedly found")
    require(diagonal["firstpass_diagonal_profile_limitation_theorem_closed"] is True, "diagonal limitation theorem not closed")
    require(diagonal["selected_Rtheta_source_rows_closed"] is False, "diagonal theorem unexpectedly closes Rtheta rows")
    require(likelihood["external_profile_replay_closed_under_declared_standard"] is True, "external replay boundary not closed")
    require(likelihood["full_covariance_profile_likelihood_closed"] is False, "full covariance likelihood unexpectedly closed")
    require(likelihood["selected_Rtheta_source_rows_closed"] is False, "likelihood import unexpectedly closes Rtheta rows")

    decision = candidate["limitation_decision"]
    require(decision["current_inventory_emits_value_source_anchor_rows"] is False, "candidate overclaims current inventory emission")
    require(decision["accepted_internal_scalar_rows_after_all_current_attempts"] == 0, "candidate overclaims internal scalar rows")
    require(decision["accepted_Rtheta_source_rows_after_all_current_attempts"] == 0, "candidate overclaims Rtheta source rows")
    require(decision["accepted_threshold_response_source_rows_after_all_current_attempts"] == 0, "candidate overclaims threshold response source rows")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true-equivalence precision rows")
    require(decision["full_no_knob_closed"] is False, "candidate overclaims no-knob closure")
    require(decision["true_SM_equivalence_closed"] is False, "candidate overclaims true SM equivalence")
    require(len(candidate["lawful_exits_after_limitation"]) == cert["lawful_exit_count"] == 3, "lawful exit count changed")
    require(cert["accepted_internal_scalar_rows_after_all_current_attempts"] == 0, "certificate overclaims scalar rows")
    require(cert["accepted_Rtheta_source_rows_after_all_current_attempts"] == 0, "certificate overclaims Rtheta rows")
    require(cert["accepted_threshold_response_source_rows_after_all_current_attempts"] == 0, "certificate overclaims threshold rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_valuesourceanchoremission_or_noknoblimitationtheorem.candidate.json",
                "status": candidate["status"],
                "current_inventory_limitation": "closed",
                "current_inventory_emitted_rows": 0,
                "strict_candidate_rows_tested": 6,
                "atomic_routes": 3,
                "lawful_exits": 3,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected value-source anchor emission or no-knob limitation theorem audit passed")


if __name__ == "__main__":
    main()
