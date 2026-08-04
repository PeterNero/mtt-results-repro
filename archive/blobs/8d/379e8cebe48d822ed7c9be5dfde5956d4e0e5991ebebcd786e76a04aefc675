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
    candidate = load_json("candidate_data/selected_rthetasourceruleemission_or_thresholdmatchingmassschemerows.candidate.json")
    cert = load_json("certificates/selected_rthetasourceruleemission_or_thresholdmatchingmassschemerows_certificate.json")
    previous = load_json("certificates/selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution_certificate.json")
    contract = load_json("candidate_data/selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition/selected_threshold_response_functional_contract.packet.json")
    internal_rtheta = load_json("certificates/selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier_certificate.json")
    post_pi = load_json("certificates/selected_postpiconventionsource_or_thresholdfunctionalinstantiation_certificate.json")
    diagonal = load_json("certificates/selected_thresholdrows_or_diagonalprofilelimitationtheorem_certificate.json")
    anchor = load_json("certificates/selected_valuesourceanchorrows_or_internalnoknobvalueemission_certificate.json")
    source_audit = load_json("candidate_data/selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation/accepted_threshold_mass_scheme_source_row_audit.packet.json")
    firstpass = load_json("candidate_data/selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows/firstpass_rtheta_coefficient_values.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(previous["readiness_fraction"] == "4/7", "previous first-exit readiness changed")
    require(previous["first_exit_open_clause_count"] == 3, "previous first-exit open count changed")

    rule = candidate["selected_rtheta_source_rule"]
    require(contract["status"] == "SELECTED_THRESHOLD_RESPONSE_FUNCTIONAL_CONTRACT_EMITTED", "contract not emitted")
    require(rule["status"] == "SELECTED_RTHETA_SOURCE_RULE_FUNCTIONAL_MAPPING_EMITTED_VALUES_OPEN", "rule status mismatch")
    require(rule["selected_before_observed_comparison"] is True, "rule not selected before observed comparison")
    require("typed selected source-rule functional mapping" in rule["does_emit_now"], "rule does not emit functional mapping")
    for forbidden in [
        "threshold matching numeric source rows",
        "mass-scheme conversion numeric source rows",
        "selected Rtheta coefficient values",
        "lambda_H value row",
        "true-equivalence precision rows",
    ]:
        require(forbidden in rule["does_not_emit_now"], f"rule does not guard forbidden emission: {forbidden}")

    require(internal_rtheta["source_owner_verified"] is True, "source owner not verified")
    require(internal_rtheta["physical_PhiFinC1_action_source_closed_at_VSD01_source_assembly_scope"] is True, "VSD01 source assembly not closed")
    require(post_pi["same_branch_scale_scheme_loop_convention_closed"] is True, "post-Pi convention not closed")
    require(post_pi["selected_threshold_response_functional_instantiated"] is False, "post-Pi overinstantiates value functional")
    require(diagonal["firstpass_diagonal_profile_limitation_theorem_closed"] is True, "diagonal limitation not closed")
    require(diagonal["selected_threshold_response_functional_closed"] is False, "diagonal theorem overcloses value functional")
    require(anchor["no_observed_selector_proof_closed"] is True, "no-observed selector guard missing")

    readiness = candidate["first_exit_readiness_after_source_rule"]
    require(readiness["required_clause_count"] == 7, "required clause count changed")
    require(readiness["closed_clause_count"] == 5, "closed clause count not advanced to 5")
    require(readiness["open_clause_count"] == 2, "open clause count not reduced to 2")
    require(readiness["readiness_fraction"] == "5/7", "readiness fraction not 5/7")
    require("selected_threshold_response_functional_source_rule" in readiness["closed_clauses"], "source-rule clause not closed")
    require(readiness["open_clauses"] == ["threshold_matching_source_rows", "mass_scheme_conversion_source_rows"], "open clauses mismatch")

    values = candidate["value_row_status"]
    require(firstpass["accepted_as_firstpass_Rtheta_coefficient_values"] is True, "first-pass coefficients not closed")
    require(firstpass["accepted_as_selected_Rtheta_coefficient_values"] is False, "first-pass coefficients overpromoted")
    require(firstpass["total_dense_coefficient_entries"] == values["firstpass_total_dense_coefficient_entries"] == 82, "dense coefficient count changed")
    require(firstpass["total_nonzero_coefficient_entries"] == values["firstpass_total_nonzero_coefficient_entries"] == 68, "nonzero coefficient count changed")
    require(source_audit["accepted_threshold_matching_source_rows"] == [], "threshold rows unexpectedly accepted")
    require(source_audit["accepted_mass_scheme_conversion_source_rows"] == [], "mass-scheme rows unexpectedly accepted")
    require(source_audit["promotable_count"] == 0, "source audit unexpectedly promotable")
    require(values["selected_threshold_response_functional_source_rule_closed"] is True, "value status lost source-rule closure")
    require(values["selected_threshold_response_functional_value_instantiated"] is False, "value functional overinstantiated")
    require(values["threshold_matching_source_rows_closed"] is False, "threshold rows overclosed")
    require(values["mass_scheme_conversion_source_rows_closed"] is False, "mass-scheme rows overclosed")
    require(values["promoted_selected_Rtheta_source_row_count"] == 0, "Rtheta source rows overpromoted")
    require(values["accepted_threshold_matching_source_row_count"] == 0, "threshold row count overclaimed")
    require(values["accepted_mass_scheme_conversion_source_row_count"] == 0, "mass-scheme row count overclaimed")
    require(values["accepted_internal_scalar_rows"] == 0, "internal scalar rows overclaimed")
    require(values["accepted_true_equivalence_precision_rows"] == 0, "true precision rows overclaimed")
    require(values["full_no_knob_closed"] is False, "no-knob overclosed")
    require(values["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(cert["selected_Rtheta_source_rule_functional_mapping_closed"] is True, "certificate lost source-rule mapping")
    require(cert["selected_threshold_response_functional_source_rule_closed"] is True, "certificate lost threshold source rule")
    require(cert["selected_threshold_response_functional_value_instantiated"] is False, "certificate overinstantiates value functional")
    require(cert["first_exit_closed_clause_count"] == 5, "certificate closed clause count mismatch")
    require(cert["first_exit_open_clause_count"] == 2, "certificate open clause count mismatch")
    require(cert["readiness_fraction"] == "5/7", "certificate readiness mismatch")
    require(cert["threshold_matching_source_rows_closed"] is False, "certificate overcloses threshold rows")
    require(cert["mass_scheme_conversion_source_rows_closed"] is False, "certificate overcloses mass rows")
    require(cert["accepted_threshold_matching_source_row_count"] == 0, "certificate threshold count overclaimed")
    require(cert["accepted_mass_scheme_conversion_source_row_count"] == 0, "certificate mass count overclaimed")
    require(cert["accepted_internal_scalar_rows"] == 0, "certificate scalar rows overclaimed")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate true precision overclaimed")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_rthetasourceruleemission_or_thresholdmatchingmassschemerows.candidate.json",
                "status": candidate["status"],
                "first_exit_readiness": "5/7",
                "source_rule_mapping": "closed",
                "open_clauses": readiness["open_clauses"],
                "accepted_value_rows": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Rtheta source-rule emission audit passed")


if __name__ == "__main__":
    main()
