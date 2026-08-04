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
    candidate = load_json("candidate_data/selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution.candidate.json")
    cert = load_json("certificates/selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution_certificate.json")
    limitation = load_json("certificates/selected_valuesourceanchoremission_or_noknoblimitationtheorem_certificate.json")
    contract = load_json("candidate_data/selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition/selected_threshold_response_functional_contract.packet.json")
    workorder = load_json("candidate_data/selected_vsd02thresholdresponserule_or_externallikelihoodimport/internal_threshold_response_derivation_workorder.packet.json")
    internal_rtheta = load_json("certificates/selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier_certificate.json")
    post_pi = load_json("certificates/selected_postpiconventionsource_or_thresholdfunctionalinstantiation_certificate.json")
    diagonal = load_json("certificates/selected_thresholdrows_or_diagonalprofilelimitationtheorem_certificate.json")
    anchor = load_json("certificates/selected_valuesourceanchorrows_or_internalnoknobvalueemission_certificate.json")
    source_audit = load_json("candidate_data/selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation/accepted_threshold_mass_scheme_source_row_audit.packet.json")
    firstpass = load_json("candidate_data/selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows/firstpass_rtheta_coefficient_values.packet.json")
    promotion = load_json("candidate_data/selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows/selected_rtheta_source_row_promotion_audit.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(limitation["current_inventory_limitation_closed"] is True, "current-inventory limitation not imported")
    require(limitation["lawful_exit_count"] == 3, "lawful exit count changed")

    require(contract["status"] == "SELECTED_THRESHOLD_RESPONSE_FUNCTIONAL_CONTRACT_EMITTED", "threshold response contract missing")
    require(contract["observed_data_used_as_selector"] is False, "contract uses observed selector")
    require(workorder["acceptance_contract"]["values_promotable_now"] is False, "workorder unexpectedly promotes values")
    require(workorder["finite_residual_support"]["all_residuals_finite"] is True, "finite residual support missing")
    require(workorder["finite_residual_support"]["accepted_as_threshold_matching_values"] is False, "workorder overpromotes threshold values")
    require(workorder["finite_residual_support"]["accepted_as_mass_scheme_conversion_values"] is False, "workorder overpromotes mass-scheme values")

    test = candidate["first_exit_acceptance_test"]
    require(test["required_clause_count"] == 7, "required clause count changed")
    require(test["closed_clause_count"] == 4, "closed clause count changed")
    require(test["open_clause_count"] == 3, "open clause count changed")
    require(len(test["closed_clauses"]) == 4, "closed clause list mismatch")
    require(len(test["open_clauses"]) == 3, "open clause list mismatch")
    open_ids = {row["id"] for row in test["open_clauses"]}
    require(open_ids == {
        "selected_threshold_response_functional_source_rule",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
    }, "open clause set changed")

    require(internal_rtheta["source_owner_verified"] is True, "source owner not verified")
    require(internal_rtheta["physical_PhiFinC1_action_source_closed_at_VSD01_source_assembly_scope"] is True, "VSD01 source assembly not closed")
    require(post_pi["same_branch_scale_scheme_loop_convention_closed"] is True, "post-Pi convention source not closed")
    require(post_pi["selected_threshold_response_functional_instantiated"] is False, "post-Pi unexpectedly instantiates threshold functional")
    require(diagonal["firstpass_diagonal_profile_limitation_theorem_closed"] is True, "diagonal limitation not closed")
    require(diagonal["selected_threshold_response_functional_closed"] is False, "diagonal theorem overcloses threshold functional")
    require(anchor["no_observed_selector_proof_closed"] is True, "no-observed-selector guard missing")

    support = candidate["numeric_support_demoted_to_validation"]
    require(firstpass["accepted_as_firstpass_Rtheta_coefficient_values"] is True, "first-pass Rtheta values not closed")
    require(firstpass["accepted_as_selected_Rtheta_coefficient_values"] is False, "first-pass values overpromoted to selected coefficients")
    require(firstpass["accepted_as_selected_threshold_response_functional"] is False, "first-pass values overpromoted to threshold functional")
    require(firstpass["total_dense_coefficient_entries"] == support["firstpass_total_dense_coefficient_entries"] == 82, "dense coefficient count changed")
    require(firstpass["total_nonzero_coefficient_entries"] == support["firstpass_total_nonzero_coefficient_entries"] == 68, "nonzero coefficient count changed")
    require(promotion["promoted_selected_Rtheta_source_row_count"] == 0, "Rtheta source rows overpromoted")
    require(source_audit["accepted_threshold_matching_source_rows"] == [], "threshold matching rows unexpectedly accepted")
    require(source_audit["accepted_mass_scheme_conversion_source_rows"] == [], "mass-scheme rows unexpectedly accepted")
    require(source_audit["promotable_count"] == 0, "source audit unexpectedly promotable")
    require(support["accepted_threshold_matching_source_row_count"] == 0, "candidate overclaims threshold row count")
    require(support["accepted_mass_scheme_conversion_source_row_count"] == 0, "candidate overclaims mass-scheme row count")
    require(support["accepted_internal_scalar_row_count"] == 0, "candidate overclaims scalar rows")
    require(support["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")

    decision = candidate["decision"]
    require(decision["first_lawful_exit_reaudited"] is True, "first exit not reaudited")
    require(decision["first_lawful_exit_closed"] is False, "first exit overclosed")
    require(decision["readiness_fraction"] == "4/7", "readiness fraction changed")
    require(decision["selected_threshold_response_functional_instantiated"] is False, "candidate overcloses threshold functional")
    require(decision["threshold_matching_source_rows_closed"] is False, "candidate overcloses threshold rows")
    require(decision["mass_scheme_conversion_source_rows_closed"] is False, "candidate overcloses mass-scheme rows")
    require(decision["accepted_internal_scalar_rows"] == 0, "candidate overclaims scalar rows")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")
    require(decision["full_no_knob_closed"] is False, "candidate overclaims no-knob")
    require(decision["true_SM_equivalence_closed"] is False, "candidate overclaims true SM equivalence")

    require(cert["first_exit_closed_clause_count"] == 4, "certificate closed clause count changed")
    require(cert["first_exit_open_clause_count"] == 3, "certificate open clause count changed")
    require(cert["readiness_fraction"] == "4/7", "certificate readiness changed")
    require(cert["selected_dynamic_operator_source_owner_closed"] is True, "certificate lost source owner closure")
    require(cert["same_branch_scale_scheme_loop_convention_closed"] is True, "certificate lost convention closure")
    require(cert["diagonal_profile_limitation_closed"] is True, "certificate lost diagonal closure")
    require(cert["no_observed_selector_guard_closed"] is True, "certificate lost no-observed guard")
    require(cert["promoted_selected_Rtheta_source_row_count"] == 0, "certificate overpromotes Rtheta rows")
    require(cert["accepted_threshold_matching_source_row_count"] == 0, "certificate overpromotes threshold rows")
    require(cert["accepted_mass_scheme_conversion_source_row_count"] == 0, "certificate overpromotes mass rows")
    require(cert["accepted_internal_scalar_rows"] == 0, "certificate overclaims scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution.candidate.json",
                "status": candidate["status"],
                "first_exit_readiness": "4/7",
                "closed_clauses": 4,
                "open_clauses": [
                    "selected_threshold_response_functional_source_rule",
                    "threshold_matching_source_rows",
                    "mass_scheme_conversion_source_rows",
                ],
                "accepted_internal_rows": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected threshold-response first-exit re-audit passed")


if __name__ == "__main__":
    main()
