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
    candidate = load_json("candidate_data/selected_finaldynamicgate_routea_reconciliation_or_valuepromotionnext.candidate.json")
    cert = load_json("certificates/selected_finaldynamicgate_routea_reconciliation_or_valuepromotionnext_certificate.json")
    final_frontier = load_json("certificates/selected_finalprofilelikelihoodordynamicpayloadvalues_certificate.json")
    source_criteria = load_json("certificates/selected_phifinc1sourceemissionorfiniterowindependencetheorem_certificate.json")
    premise_execution = load_json("certificates/selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted_certificate.json")
    gauge_route_a = load_json("certificates/selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution_certificate.json")
    precision_values = load_json("certificates/selected_acceptedprecisionsourcevalues_or_finaltruesmclosure_certificate.json")
    promotion_gate = load_json("certificates/selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")

    require(final_frontier["source_rule_or_galerkin_export_is_only_remaining_dynamic_gate"] is True, "older gate was not the named final dynamic gate")
    require(final_frontier["selected_PhiFinC1_physical_source_emission_theorem_closed"] is False, "older frontier unexpectedly changed")
    require(final_frontier["honest_galerkin_table_exported"] is False, "older frontier unexpectedly exported Galerkin")

    require(source_criteria["route_A_acceptance_criterion_proved"] is True, "Route A criterion not proved")
    require(source_criteria["route_B_acceptance_criterion_proved"] is True, "Route B criterion not proved")
    require(source_criteria["finite_rows_closed_as_replay_postchecks"] is True, "finite rows not demoted to replay postchecks")
    require(source_criteria["source_ownership_boundary_frozen_like_SM_parity"] is True, "source boundary not frozen")

    require(premise_execution["three_field_certificate_is_exact_remaining_route_A"] is True, "three-field Route A target not exact")
    require(premise_execution["untransported_BN_shortcut_rejected_for_source_ownership"] is True, "untransported shortcut not rejected")
    require(premise_execution["gauge_transport_trace_promoted_to_primary_next_target"] is True, "gauge transport not selected as primary")

    require(gauge_route_a["gauge_transported_BN_PhiFin_trace_closed"] is True, "gauge-transported BN/PhiFin trace not closed")
    require(gauge_route_a["Route_A_transport_closed_import_validates"] is True, "Route A transport import not valid")
    require(gauge_route_a["PSM_C1_02_unpatched_source_promotion_closed"] is True, "PSM-C1-02 source promotion not closed")
    require(gauge_route_a["A_selected_promoted"] is True, "A_selected not promoted")
    require(gauge_route_a["b_selected_promoted"] is True, "b_selected not promoted")
    require(gauge_route_a["deltaTheta_C1_promoted"] is True, "deltaTheta_C1 not promoted")
    require(gauge_route_a["narrowed_phifinc1_emission_validator_passes"] is True, "PhiFinC1 emission validator does not pass")
    require(gauge_route_a["psm_c1_02_source_promotion_validator_passes"] is True, "PSM source-promotion validator does not pass")
    require(gauge_route_a["Route_B_independent_rows_required_for_PSM_closure"] is False, "Route B still required for PSM closure")

    decision = candidate["reconciliation_decision"]
    require(decision["older_final_dynamic_gate_consumed_by_later_route_A_source_promotion"] is True, "old gate not consumed")
    require(decision["route_B_independent_galerkin_export_required_for_this_gate"] is False, "Route B wrongly required")
    require(decision["selected_PhiFinC1_physical_source_emission_theorem_closed_at_route_A_source_promotion_scope"] is True, "Route A source theorem not closed at scope")
    require(decision["source_rule_or_galerkin_export_still_active_as_current_blocker"] is False, "old gate still active")
    require(decision["post_source_value_promotion_is_now_the_active_frontier"] is True, "post-source frontier not active")

    not_closed = candidate["what_this_does_not_close"]
    require(not_closed["actual_dynamic_QaSU3_payload_values"] is False, "overclaims dynamic Qa/SU3 payload values")
    require(not_closed["accepted_true_equivalence_precision_rows"] == 0, "overclaims true precision rows")
    require(not_closed["promoted_value_source_routes"] == 0, "overclaims promoted value routes")
    require(not_closed["true_SM_equivalence"] is False, "overclaims true SM")
    require(precision_values["actual_dynamic_QaSU3_operator_packet_closed"] is False, "precision values source unexpectedly closes dynamic payload")
    require(precision_values["accepted_true_equivalence_precision_rows"] == 0, "precision values source unexpectedly closes true-equivalence rows")
    require(promotion_gate["promoted_route_count"] == 0, "promotion gate unexpectedly promoted route")

    require(cert["older_final_dynamic_gate_consumed_by_later_route_A_source_promotion"] is True, "certificate old gate not consumed")
    require(cert["source_rule_or_galerkin_export_still_active_as_current_blocker"] is False, "certificate leaves old gate active")
    require(cert["post_source_value_promotion_is_now_the_active_frontier"] is True, "certificate lost new frontier")
    require(cert["next_required_artifact"] == candidate["new_active_frontier"]["minimal_next_artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_finaldynamicgate_routea_reconciliation_or_valuepromotionnext.candidate.json",
                "status": candidate["status"],
                "old_source_rule_or_galerkin_gate": "consumed by later Route A source promotion",
                "route_B_required_for_this_gate": False,
                "A_b_deltaTheta_promoted": True,
                "current_frontier": "post-source value promotion",
                "accepted_true_equivalence_precision_rows": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected final dynamic gate Route A reconciliation audit passed")


if __name__ == "__main__":
    main()
