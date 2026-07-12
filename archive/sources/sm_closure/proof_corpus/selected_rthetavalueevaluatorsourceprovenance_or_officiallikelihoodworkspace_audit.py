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
    candidate = load_json("candidate_data/selected_rthetavalueevaluatorsourceprovenance_or_officiallikelihoodworkspace.candidate.json")
    cert = load_json("certificates/selected_rthetavalueevaluatorsourceprovenance_or_officiallikelihoodworkspace_certificate.json")
    contracted = load_json("certificates/selected_acceptedfulllikelihoodfunction_or_rthetacoefficientvaluerows_certificate.json")
    direct = load_json("certificates/selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission_certificate.json")
    functional = load_json("certificates/selected_rtheta_coefficientfunctional_or_universalanchorselection_certificate.json")
    owner_packet = load_json("certificates/selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction_certificate.json")
    formula = load_json("certificates/selected_rtheta_coefficientformuladerivation_or_selectedownerbridge_certificate.json")
    execution = load_json("certificates/selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_certificate.json")
    official_decision = load_json("certificates/selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision_certificate.json")
    official_import = load_json("certificates/selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(contracted["promotion_blocker_contraction_closed"] is True, "contracted precursor not closed")
    require(direct["direct_execution_attempt_closed"] is True, "direct execution precursor not closed")
    require(contracted["remaining_payload_count"] == 2, "contracted precursor payload count changed")

    schema = candidate["strict_row_schema"]
    require(schema["schema"] == "RThetaCoefficientSourceRow.v1", "strict row schema name changed")
    require(schema["schema_closed"] is True, "strict row schema not closed")
    require(len(schema["required_clauses"]) == 9, "strict row schema clause count changed")
    for required in [
        "selected_source_owner_certificate",
        "selected_coefficient_formula_certificate",
        "emitted_coefficient_value",
        "Pi_Rtheta_projector_compatibility",
        "no_observed_value_or_target_residual_selector",
    ]:
        require(required in schema["required_clauses"], f"strict row schema lost clause: {required}")

    route_a = candidate["route_A_official_likelihood"]
    require(official_decision["official_likelihood_route_retired_for_now"] is True, "official likelihood route not retired")
    require(official_import["official_machine_readable_likelihood_imported"] is False, "official likelihood imported unexpectedly")
    require(official_import["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overaccepted")
    require(route_a["official_likelihood_route_retired_for_now"] is True, "route A not retired")
    require(route_a["official_machine_readable_likelihood_imported"] is False, "route A overimports official likelihood")
    require(route_a["accepted_full_likelihood_function_or_workspace_closed"] is False, "route A overcloses workspace")
    require(route_a["route_A_closed"] is False, "route A overclosed")

    route_b = candidate["route_B_rtheta_value_evaluator"]
    for key in [
        "Pi_Rtheta_closed",
        "coefficient_functional_domain_closed",
        "selected_dynamic_operator_source_owner_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "threshold_matching_source_rows_closed_at_admitted_external_tier",
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier",
        "accepted_diagonal_profile_theorem_closed",
        "row_coefficient_slot_manifest_closed",
        "source_owner_candidate_matrix_closed",
        "dynamic_precoefficient_formula_basis_closed",
        "coefficient_functional_skeleton_closed",
        "firstpass_Rtheta_coefficient_values_closed",
        "firstpass_composed_BCT_to_Mt_response_closed",
        "strict_Rtheta_coefficient_source_row_schema_closed",
    ]:
        require(route_b[key] is True, f"route B lost closed prerequisite: {key}")

    require(execution["Pi_Rtheta_closed"] is True, "execution precursor lost Pi_Rtheta")
    require(execution["selected_dynamic_operator_source_owner_closed"] is True, "execution precursor lost source owner")
    require(functional["coefficient_functional_skeleton_closed"] is True, "functional skeleton not closed")
    require(owner_packet["row_coefficient_slot_manifest_closed"] is True, "row manifest not closed")
    require(owner_packet["source_owner_candidate_matrix_closed"] is True, "source owner matrix not closed")
    require(formula["dynamic_precoefficient_formula_basis_closed"] is True, "precoefficient basis not closed")

    for key in [
        "selected_Rtheta_source_rows_closed",
        "selected_Rtheta_coefficient_values_closed",
        "selected_threshold_response_functional_instantiated",
        "value_evaluator_source_provenance_closed",
        "route_B_closed",
    ]:
        require(route_b[key] is False, f"route B overcloses: {key}")
    require(route_b["accepted_rtheta_source_owner_count"] == 0, "route B overaccepts source owners")
    require(route_b["accepted_coefficient_formula_count"] == 0, "route B overaccepts formulas")
    require(route_b["accepted_coefficient_value_count"] == 0, "route B overaccepts values")
    require(route_b["accepted_strict_schema_row_count"] == 0, "route B overaccepts strict schema rows")
    require(route_b["selected_internal_value_emission_count"] == 0, "route B overemits values")

    cutset = candidate["cutset"]
    require(cutset["cutset_closed"] is True, "cutset not closed")
    require("Pi_Rtheta" in cutset["old_reopen_targets_rejected"], "cutset reopens Pi_Rtheta")
    require("coefficient functional domain" in cutset["old_reopen_targets_rejected"], "cutset reopens coefficient domain")
    require("one or more selected RThetaCoefficientSourceRow.v1 rows" in cutset["remaining_atomic_payloads"], "strict row payload missing")
    require("or an official machine-readable full likelihood/profile workspace" in cutset["remaining_atomic_payloads"], "official workspace payload missing")

    guards = candidate["guards"]
    require(guards["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(guards["target_fitting_used"] is False, "candidate uses target fitting")
    require(guards["external_rows_count_as_internal_no_knob_source_rows"] is False, "candidate promotes external rows")
    require(guards["official_workspace_used"] is False, "candidate uses official workspace despite absence")
    require(guards["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")
    require(guards["full_no_knob_closed"] is False, "candidate overclaims no-knob")

    decision = candidate["decision"]
    require(decision["strict_schema_and_cutset_closed"] is True, "decision did not close schema/cutset")
    require(decision["route_A_closed"] is False, "decision overcloses route A")
    require(decision["route_B_closed"] is False, "decision overcloses route B")
    require(decision["remaining_payload_count"] == 2, "remaining payload count changed")
    require(decision["preferred_next_artifact"] == cert["next_required_artifact"], "next artifact mismatch")

    for key in [
        "strict_Rtheta_coefficient_source_row_schema_closed",
        "source_provenance_cutset_closed",
        "Pi_Rtheta_closed",
        "coefficient_functional_domain_closed",
        "row_coefficient_slot_manifest_closed",
        "source_owner_candidate_matrix_closed",
        "dynamic_precoefficient_formula_basis_closed",
        "coefficient_functional_skeleton_closed",
    ]:
        require(cert[key] is True, f"certificate lost closed field: {key}")
    for key in [
        "selected_Rtheta_source_rows_closed",
        "selected_Rtheta_coefficient_values_closed",
        "selected_threshold_response_functional_instantiated",
        "value_evaluator_source_provenance_closed",
        "accepted_full_likelihood_function_or_workspace_closed",
        "route_A_closed",
        "route_B_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses: {key}")
    require(cert["accepted_strict_schema_row_count"] == 0, "certificate overaccepts strict schema rows")
    require(cert["remaining_payload_count"] == 2, "certificate payload count changed")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "strict_schema_and_cutset_closed": True,
                "accepted_strict_schema_row_count": cert["accepted_strict_schema_row_count"],
                "route_A_closed": cert["route_A_closed"],
                "route_B_closed": cert["route_B_closed"],
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Rtheta value-evaluator source provenance cutset audit passed")


if __name__ == "__main__":
    main()
