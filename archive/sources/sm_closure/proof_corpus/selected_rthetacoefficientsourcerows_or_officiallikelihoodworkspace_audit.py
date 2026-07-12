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
    candidate = load_json("candidate_data/selected_rthetacoefficientsourcerows_or_officiallikelihoodworkspace.candidate.json")
    cert = load_json("certificates/selected_rthetacoefficientsourcerows_or_officiallikelihoodworkspace_certificate.json")
    cutset = load_json("certificates/selected_rthetavalueevaluatorsourceprovenance_or_officiallikelihoodworkspace_certificate.json")
    firstpass = load_json("candidate_data/selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows/firstpass_rtheta_coefficient_values.packet.json")
    manifest = load_json("candidate_data/selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction/rtheta_row_coefficient_slot_manifest.packet.json")
    source_owner = load_json("candidate_data/selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction/rtheta_source_owner_candidate_matrix.packet.json")
    formula = load_json("candidate_data/selected_rtheta_coefficientformuladerivation_or_selectedownerbridge/rtheta_slot_projection_feasibility.packet.json")
    pi = load_json("candidate_data/selected_rtheta_primitivec1overlap_or_pinoneedtheorem/pi_rtheta_recheck_after_primitive_c1_import.packet.json")
    execution_gate = load_json("candidate_data/selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation/rtheta_value_evaluator_execution_gate.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(cutset["strict_Rtheta_coefficient_source_row_schema_closed"] is True, "strict schema precursor not closed")
    require(cutset["accepted_strict_schema_row_count"] == 0, "cutset overaccepted rows")
    require(firstpass["accepted_as_firstpass_Rtheta_coefficient_values"] is True, "first-pass values not available")
    require(firstpass["accepted_as_selected_Rtheta_coefficient_values"] is False, "first-pass values overpromoted")
    require(manifest["manifest_closed"] is True, "slot manifest not closed")
    require(manifest["slot_count"] == 10, "slot count changed")
    require(source_owner["accepted_rtheta_source_owner_count"] == 0, "source owner overaccepted")
    require(formula["accepted_coefficient_formula_count"] == 0, "formula overaccepted")
    require(pi["Pi_Rtheta_closed"] is True, "latest Pi_Rtheta not closed")
    require(execution_gate["Pi_Rtheta_closed"] is True, "execution gate lost Pi")
    require(execution_gate["selected_threshold_response_functional_instantiated"] is False, "threshold response overinstantiated")

    schema = candidate["schema_execution"]
    require(schema["schema"] == "RThetaCoefficientSourceRow.v1", "schema name changed")
    require(schema["attempted_slot_count"] == 10, "attempted slot count changed")
    require(schema["accepted_strict_schema_row_count"] == 0, "schema overaccepts rows")
    require(schema["strict_acceptance_clause_count"] == 9, "clause count changed")
    require(schema["uniform_pass_count"] == 5, "uniform pass count changed")
    require(schema["uniform_missing_count"] == 4, "uniform missing count changed")
    for missing in [
        "selected_source_owner_certificate",
        "selected_coefficient_formula_certificate",
        "emitted_selected_coefficient_value",
        "selected_threshold_response_functional_or_equivalent_value_context",
    ]:
        require(missing in schema["strict_clauses_missing_uniformly"], f"missing clause not recorded: {missing}")

    rows = candidate["row_attempts"]
    require(len(rows) == 10, "row attempt count changed")
    require({row["slot_id"] for row in rows} == {slot["slot_id"] for slot in manifest["coefficient_slots"]}, "row attempts do not match manifest")
    for row in rows:
        require(row["firstpass_value_support_available"] is True, f"{row['slot_id']} lost first-pass support")
        require(row["strict_clause_pass_count"] == 5, f"{row['slot_id']} pass count changed")
        require(row["strict_clause_missing_count"] == 4, f"{row['slot_id']} missing count changed")
        require(row["accepted_as_strict_RThetaCoefficientSourceRow"] is False, f"{row['slot_id']} overaccepted")

    dynamic_support_count = sum(1 for row in rows if row["dynamic_precoefficient_support_available"])
    require(dynamic_support_count == 8, "dynamic precoefficient support count changed")

    route_a = candidate["route_A_official_likelihood"]
    require(route_a["official_likelihood_route_retired_for_now"] is True, "official likelihood not retired")
    require(route_a["official_machine_readable_likelihood_imported"] is False, "official likelihood overimported")
    require(route_a["accepted_full_likelihood_function_or_workspace_closed"] is False, "official workspace overclosed")
    require(route_a["route_A_closed"] is False, "route A overclosed")

    route_b = candidate["route_B_strict_rows"]
    for key in [
        "Pi_Rtheta_closed",
        "coefficient_functional_domain_closed",
        "selected_dynamic_operator_source_owner_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "strict_Rtheta_coefficient_source_row_schema_closed",
        "ten_slot_execution_attempted",
        "firstpass_value_support_available",
    ]:
        require(route_b[key] is True, f"route B lost support: {key}")
    for key in [
        "selected_Rtheta_source_rows_closed",
        "selected_Rtheta_coefficient_values_closed",
        "selected_threshold_response_functional_instantiated",
        "value_evaluator_source_provenance_closed",
        "route_B_closed",
    ]:
        require(route_b[key] is False, f"route B overcloses: {key}")
    require(route_b["accepted_strict_schema_row_count"] == 0, "route B overaccepts rows")

    guards = candidate["guards"]
    require(guards["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(guards["target_fitting_used"] is False, "candidate uses target fitting")
    require(guards["firstpass_replay_values_promoted_to_selected_rows"] is False, "candidate promotes first-pass replay")
    require(guards["external_rows_count_as_internal_no_knob_source_rows"] is False, "candidate promotes external rows")
    require(guards["true_SM_equivalence_closed"] is False, "candidate overclaims true SM")
    require(guards["full_no_knob_closed"] is False, "candidate overclaims no-knob")

    decision = candidate["decision"]
    require(decision["ten_row_strict_execution_attempt_closed"] is True, "decision did not close execution attempt")
    require(decision["route_A_closed"] is False, "decision overcloses route A")
    require(decision["route_B_closed"] is False, "decision overcloses route B")
    require(decision["remaining_payload_count"] == 2, "decision payload count changed")
    require(cert["next_required_artifact"] == decision["preferred_next_artifact"], "next artifact mismatch")

    require(cert["attempted_slot_count"] == 10, "certificate attempted count changed")
    require(cert["uniform_strict_clause_pass_count"] == 5, "certificate pass count changed")
    require(cert["uniform_strict_clause_missing_count"] == 4, "certificate missing count changed")
    require(cert["accepted_strict_schema_row_count"] == 0, "certificate overaccepts strict rows")
    require(cert["firstpass_replay_values_promoted_to_selected_rows"] is False, "certificate promotes first-pass replay")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "attempted_slot_count": cert["attempted_slot_count"],
                "accepted_strict_schema_row_count": cert["accepted_strict_schema_row_count"],
                "uniform_clause_score": f"{cert['uniform_strict_clause_pass_count']}/{cert['strict_acceptance_clause_count']}",
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Rtheta coefficient source-row execution audit passed")


if __name__ == "__main__":
    main()
