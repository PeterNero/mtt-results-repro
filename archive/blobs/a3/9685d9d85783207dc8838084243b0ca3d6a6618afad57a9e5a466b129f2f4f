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
    candidate = load_json("candidate_data/selected_rthetarowownerformulavalueemitter_or_officiallikelihoodworkspace.candidate.json")
    cert = load_json("certificates/selected_rthetarowownerformulavalueemitter_or_officiallikelihoodworkspace_certificate.json")
    rows = load_json("certificates/selected_rthetacoefficientsourcerows_or_officiallikelihoodworkspace_certificate.json")
    limitation = load_json("certificates/selected_valuesourceanchoremission_or_noknoblimitationtheorem_certificate.json")
    first_exit = load_json("certificates/selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution_certificate.json")
    value_anchor = load_json("certificates/selected_valuesourceanchorrows_or_internalnoknobvalueemission_certificate.json")
    official = load_json("certificates/selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(rows["ten_row_strict_execution_attempt_closed"] is True, "ten-row precursor not closed")
    require(rows["attempted_slot_count"] == 10, "ten-row slot count changed")
    require(rows["uniform_strict_clause_missing_count"] == 4, "missing clause count changed")
    require(rows["accepted_strict_schema_row_count"] == 0, "ten-row precursor overaccepts rows")
    require(rows["firstpass_replay_values_promoted_to_selected_rows"] is False, "ten-row precursor promotes replay values")

    require(limitation["current_inventory_emits_value_source_anchor_rows"] is False, "limitation overclaims current inventory rows")
    require(limitation["accepted_internal_scalar_rows_after_all_current_attempts"] == 0, "limitation overclaims accepted rows")
    require(value_anchor["accepted_internal_scalar_row_count"] == 0, "value anchor overclaims scalar rows")
    require(first_exit["selected_threshold_response_functional_instantiated"] is False, "first exit overinstantiates functional")
    require(first_exit["accepted_internal_scalar_rows"] == 0, "first exit overaccepts scalar rows")
    require(official["official_likelihood_route_retired_for_now"] is True, "official route not retired")

    factor = candidate["factorization"]
    require(factor["factorization_closed"] is True, "factorization not closed")
    require(factor["missing_clause_instances_before_factorization"] == 40, "missing-clause instance count changed")
    require(factor["attempted_slot_count"] == 10, "factor slot count changed")
    require(factor["missing_clause_count_per_slot"] == 4, "factor missing-per-slot changed")
    require(factor["independent_payload_count_after_factorization"] == 1, "factorization did not collapse to one payload")
    require(factor["factor_object"] == "SelectedRThetaThresholdResponseValueContextEmitter", "factor object changed")
    for clause in [
        "same_branch_source_owner_for_emitted_row",
        "selected_formula_for_emitted_row",
        "selected_numeric_or_exact_value_for_emitted_row",
        "threshold_response_context_for_emitted_row",
        "no_observed_selector_certificate",
    ]:
        require(clause in factor["emitter_contract"], f"emitter contract lost clause: {clause}")

    inventory = candidate["current_inventory_test"]
    require(inventory["current_inventory_emits_emitter"] is False, "current inventory overemits emitter")
    require(inventory["accepted_emitter_count"] == 0, "current inventory overaccepts emitter")
    require(inventory["accepted_strict_schema_row_count"] == 0, "current inventory overaccepts strict rows")
    require(inventory["firstpass_replay_values_promoted_to_selected_rows"] is False, "current inventory promotes replay values")

    workspace = candidate["official_workspace_route"]
    require(workspace["official_likelihood_route_retired_for_now"] is True, "workspace route not retired")
    require(workspace["official_machine_readable_likelihood_imported"] is False, "workspace route overimports likelihood")
    require(workspace["accepted_full_likelihood_function_or_workspace_closed"] is False, "workspace route overcloses")
    require(workspace["route_A_closed"] is False, "workspace route overclosed")

    decision = candidate["decision"]
    require(decision["four_missing_clauses_factorization_closed"] is True, "decision did not close factorization")
    require(decision["route_A_official_workspace_closed"] is False, "decision overcloses route A")
    require(decision["route_B_selected_emitter_closed"] is False, "decision overcloses route B")
    require(decision["remaining_payload_count"] == 2, "decision payload count changed")
    require(cert["next_required_artifact"] == decision["preferred_next_artifact"], "next artifact mismatch")

    require(cert["four_missing_clauses_factorization_closed"] is True, "certificate lost factorization")
    require(cert["missing_clause_instances_before_factorization"] == 40, "certificate missing instance count changed")
    require(cert["independent_payload_count_after_factorization"] == 1, "certificate payload factor count changed")
    require(cert["accepted_emitter_count"] == 0, "certificate overaccepts emitter")
    require(cert["accepted_strict_schema_row_count"] == 0, "certificate overaccepts rows")
    require(cert["true_SM_equivalence_closed"] is False, "certificate overclaims true SM")
    require(cert["full_no_knob_closed"] is False, "certificate overclaims no-knob")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "factorization_closed": cert["four_missing_clauses_factorization_closed"],
                "missing_clause_instances_before_factorization": cert["missing_clause_instances_before_factorization"],
                "independent_payload_count_after_factorization": cert["independent_payload_count_after_factorization"],
                "accepted_emitter_count": cert["accepted_emitter_count"],
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Rtheta row owner/formula/value emitter factorization audit passed")


if __name__ == "__main__":
    main()
