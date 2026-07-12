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
    candidate = load_json("candidate_data/selected_acceptedfulllikelihoodfunction_or_rthetacoefficientvaluerows.candidate.json")
    cert = load_json("certificates/selected_acceptedfulllikelihoodfunction_or_rthetacoefficientvaluerows_certificate.json")
    direct = load_json("certificates/selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission_certificate.json")
    ledger = load_json("certificates/current_true_sm_closure_consolidated_ledger_certificate.json")
    firstpass = load_json("certificates/selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows_certificate.json")
    source_owner = load_json("certificates/selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem_certificate.json")
    owner_packet = load_json("certificates/selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction_certificate.json")
    formula = load_json("certificates/selected_rtheta_coefficientformuladerivation_or_selectedownerbridge_certificate.json")
    functional = load_json("certificates/selected_rtheta_coefficientfunctional_or_universalanchorselection_certificate.json")
    likelihood_import = load_json("certificates/selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood_certificate.json")
    likelihood_decision = load_json("certificates/selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(direct["direct_execution_attempt_closed"] is True, "direct execution precursor not closed")
    require(direct["remaining_payload_count"] == 2, "direct execution payload count changed")

    route_a = candidate["route_A_full_likelihood"]
    require(likelihood_import["imported_profile_replay_closed"] is True, "profile replay not closed")
    require(likelihood_import["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overaccepted")
    require(likelihood_import["official_machine_readable_likelihood_imported"] is False, "official machine-readable likelihood imported unexpectedly")
    require(likelihood_decision["official_likelihood_route_retired_for_now"] is True, "official likelihood route not retired")
    require(likelihood_decision["published_profile_replay_retained_for_SM_parity"] is True, "published profile replay not retained")
    require(route_a["imported_profile_replay_closed"] is True, "route A lost profile replay")
    require(route_a["published_profile_replay_retained_for_SM_parity"] is True, "route A lost SM-parity replay")
    require(route_a["official_likelihood_route_retired_for_now"] is True, "route A did not retire official likelihood")
    require(route_a["official_machine_readable_likelihood_imported"] is False, "route A overimports official likelihood")
    require(route_a["accepted_as_official_LHCHXSWG_likelihood"] is False, "route A overaccepts official likelihood")
    require(route_a["accepted_full_likelihood_function_or_workspace_closed"] is False, "route A overcloses likelihood workspace")

    route_b = candidate["route_B_rtheta_coefficients"]
    require(firstpass["firstpass_Rtheta_coefficient_values_closed"] is True, "first-pass Rtheta coefficients not closed")
    require(firstpass["firstpass_composed_BCT_to_Mt_response_closed"] is True, "first-pass response not closed")
    require(firstpass["selected_Rtheta_coefficient_values_closed"] is False, "first-pass cert overcloses selected coefficients")
    require(source_owner["Pi_Rtheta_closed"] is True, "Pi_Rtheta not closed")
    require(source_owner["coefficient_functional_domain_closed"] is True, "coefficient domain not closed")
    require(source_owner["selected_dynamic_operator_source_owner_closed"] is True, "dynamic operator source owner not closed")
    require(owner_packet["row_coefficient_slot_manifest_closed"] is True, "row coefficient manifest not closed")
    require(owner_packet["source_owner_candidate_matrix_closed"] is True, "source owner candidate matrix not closed")
    require(owner_packet["accepted_rtheta_source_owner_count"] == 0, "owner packet overaccepts source owner")
    require(formula["dynamic_precoefficient_formula_basis_closed"] is True, "precoefficient basis not closed")
    require(formula["accepted_coefficient_formula_count"] == 0, "formula overaccepts coefficient formulas")
    require(functional["coefficient_functional_skeleton_closed"] is True, "functional skeleton not closed")
    require(functional["accepted_coefficient_value_count"] == 0, "functional overaccepts coefficient values")
    require(functional["value_evaluator_source_provenance_closed"] is False, "functional overcloses value evaluator provenance")

    require(ledger["selected_dynamic_operator_source_owner_closed"] is True, "ledger lost selected dynamic source owner")
    require(ledger["same_branch_scale_scheme_loop_convention_closed"] is True, "ledger lost same-branch convention")
    require(ledger["threshold_matching_source_rows_closed"] is True, "ledger lost threshold row closure")
    require(ledger["mass_scheme_conversion_source_rows_closed"] is True, "ledger lost mass row closure")
    require(ledger["accepted_diagonal_profile_theorem_closed"] is True, "ledger lost diagonal profile theorem")
    require(ledger["closed_at_admitted_external_tier_only"] is True, "ledger lost admitted-external guard")

    for key in [
        "firstpass_Rtheta_coefficient_values_closed",
        "firstpass_composed_BCT_to_Mt_response_closed",
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
    ]:
        require(route_b[key] is True, f"route B lost closed prerequisite: {key}")
    for key in [
        "selected_Rtheta_source_rows_closed",
        "selected_Rtheta_coefficient_values_closed",
        "selected_threshold_response_functional_instantiated",
        "value_evaluator_source_provenance_closed",
    ]:
        require(route_b[key] is False, f"route B overcloses: {key}")
    require(route_b["accepted_rtheta_source_owner_count"] == 0, "route B overaccepts source owners")
    require(route_b["accepted_coefficient_formula_count"] == 0, "route B overaccepts formulas")
    require(route_b["accepted_coefficient_value_count"] == 0, "route B overaccepts coefficient values")
    require(route_b["selected_internal_value_emission_count"] == 0, "route B overemits internal values")

    blockers = candidate["contracted_blockers"]
    require("selected_dynamic_operator_source_owner" in blockers["old_blockers_now_closed_or_superseded"], "dynamic owner not contracted")
    require("same_branch_scale_scheme_loop_convention" in blockers["old_blockers_now_closed_or_superseded"], "scale convention not contracted")
    require("accepted_full_likelihood_function_or_official_profile_workspace" in blockers["still_open"], "likelihood payload missing")
    require("selected_Rtheta_value_evaluator_source_provenance" in blockers["still_open"], "value evaluator payload missing")
    require("selected_internal_Rtheta_coefficient_value_rows" in blockers["still_open"], "coefficient row payload missing")

    guards = candidate["guards"]
    require(guards["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(guards["target_fitting_used"] is False, "candidate uses target fitting")
    require(guards["external_rows_count_as_internal_no_knob_source_rows"] is False, "candidate promotes external rows")
    require(guards["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")
    require(guards["full_no_knob_closed"] is False, "candidate overclaims no-knob")

    decision = candidate["decision"]
    require(decision["promotion_blocker_contraction_closed"] is True, "promotion contraction not closed")
    require(decision["route_A_closed"] is False, "decision overcloses route A")
    require(decision["route_B_closed"] is False, "decision overcloses route B")
    require(decision["remaining_payload_count"] == 2, "remaining payload count changed")
    require(cert["promotion_blocker_contraction_closed"] is True, "certificate contraction not closed")
    require(cert["remaining_payload_count"] == 2, "certificate payload count changed")
    require(cert["preferred_next_artifact"] == "MTT_Selected_RThetaValueEvaluatorSourceProvenance_or_OfficialLikelihoodWorkspace_v1", "certificate next artifact changed")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "promotion_blocker_contraction_closed": True,
                "route_A_closed": cert["route_A_closed"],
                "route_B_closed": cert["route_B_closed"],
                "remaining_payload_count": cert["remaining_payload_count"],
                "preferred_next_artifact": cert["preferred_next_artifact"],
            },
            indent=2,
        )
    )
    print("selected likelihood/Rtheta coefficient payload audit passed")


if __name__ == "__main__":
    main()
