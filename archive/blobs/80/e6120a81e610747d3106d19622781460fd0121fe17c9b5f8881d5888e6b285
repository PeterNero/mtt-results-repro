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
    candidate = load_json("candidate_data/selected_postsourcevaluepromotionrows_or_trueprecisionexit.candidate.json")
    cert = load_json("certificates/selected_postsourcevaluepromotionrows_or_trueprecisionexit_certificate.json")
    routea = load_json("certificates/selected_finaldynamicgate_routea_reconciliation_or_valuepromotionnext_certificate.json")
    step24 = load_json("certificates/selected_step24_dynamicgate_reconciliation_or_valuelayercutset_certificate.json")
    value_frontier = load_json("certificates/selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows_certificate.json")
    first_attempt = load_json("certificates/selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution_certificate.json")
    threshold_import = load_json("certificates/selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport_certificate.json")
    value_gate = load_json("certificates/selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure_certificate.json")
    external_packet = load_json("candidate_data/selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport/post_pi_external_source_row_import.packet.json")
    internal_packet = load_json("candidate_data/selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport/internal_threshold_response_functional_row_emission.packet.json")
    readiness_packet = load_json("candidate_data/selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport/step4_value_layer_readiness_after_external_import.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["closure_claimed"] is False, "must not claim full closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")

    source_status = candidate["source_promotion_gate_status"]
    require(routea["older_final_dynamic_gate_consumed_by_later_route_A_source_promotion"] is True, "Route-A reconciliation did not consume old gate")
    require(routea["source_rule_or_galerkin_export_still_active_as_current_blocker"] is False, "old source/Galerkin gate still active")
    require(routea["A_selected_promoted"] is True, "A_selected not promoted")
    require(routea["b_selected_promoted"] is True, "b_selected not promoted")
    require(routea["deltaTheta_C1_promoted"] is True, "deltaTheta_C1 not promoted")
    require(step24["step23_dynamic_workorder_closed_by_later_evidence"] is True, "Step24 dynamic workorder not closed")
    require(step24["selected_primitive_C1_contractions_first_response_layer"] is True, "primitive C1 first response not closed")
    require(source_status["PSM_C1_02_source_rule_or_Galerkin_gate_consumed"] is True, "candidate lost source gate consumption")
    require(source_status["step24_dynamic_bHessian_gate_closed"] is True, "candidate lost Step24 closure")
    require(source_status["route_B_Galerkin_replay_is_not_active_blocker"] is True, "candidate reopens Galerkin replay")

    value_status = candidate["value_layer_status"]
    require(value_frontier["what_closes"]["accepted_value_layer_frontier_frozen"] is True, "value frontier not frozen")
    require(value_frontier["what_closes"]["loop_back_to_dynamic_QaSU3_retired"] is True, "loop-back not retired")
    require(first_attempt["what_closes"]["first_nonlooping_internal_attempt_executed"] is True, "first nonlooping attempt not executed")
    require(first_attempt["what_closes"]["value_functional_gap_identified"] is True, "value functional gap not identified")
    require(value_status["value_layer_required_rows"] == 5, "candidate value-layer required rows not 5")
    require(value_status["value_layer_accepted_source_rows"] == 0, "candidate overclaims accepted value rows")
    require(value_status["source_layer_row_available"] is True, "candidate lost source-layer row")

    external = candidate["threshold_external_replay_import"]
    require(threshold_import["accepted_external_source_row_imported"] is True, "external source row not imported")
    require(threshold_import["accepted_external_threshold_row_count"] == 7, "threshold row count changed")
    require(threshold_import["accepted_external_mass_scheme_row_count"] == 3, "mass-scheme row count changed")
    require(threshold_import["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile theorem not closed")
    require(external_packet["closure_tier"] == "admitted external replay", "external packet tier mismatch")
    require(external_packet["accepted_as_internal_selected_Rtheta_row"] is False, "external packet overclaims internal Rtheta row")
    require(readiness_packet["closed_value_obligation_rows_at_admitted_external_tier"] == 4, "admitted external obligation count changed")
    require(readiness_packet["closed_value_obligation_rows_at_internal_no_knob_tier"] == 0, "internal no-knob obligation count changed")
    require(readiness_packet["readiness_fraction"] == "8/9", "readiness fraction changed")
    require(readiness_packet["only_remaining_readiness_blocker"] == "no_knob_value_derivation", "remaining blocker changed")
    require(external["accepted_external_threshold_row_count"] == 7, "candidate threshold row count mismatch")
    require(external["accepted_external_mass_scheme_row_count"] == 3, "candidate mass-scheme count mismatch")
    require(external["closed_value_obligation_rows_at_admitted_external_tier"] == 4, "candidate external obligation count mismatch")
    require(external["closed_value_obligation_rows_at_internal_no_knob_tier"] == 0, "candidate internal obligation count mismatch")
    require(external["readiness_fraction"] == "8/9", "candidate readiness mismatch")

    decision = candidate["promotion_reexecution_decision"]
    require(value_gate["promoted_route_count"] == 0, "old value gate unexpectedly promoted routes")
    require(value_gate["accepted_true_equivalence_precision_rows"] == 0, "old value gate unexpectedly accepted true rows")
    require(internal_packet["source_domain_closed"] is True, "internal Rtheta source domain not closed")
    require(internal_packet["selected_internal_value_emission_count"] == 0, "internal selected value rows emitted unexpectedly")
    require(internal_packet["accepted_as_internal_selected_Rtheta_row"] is False, "internal packet accepted Rtheta row unexpectedly")
    require(decision["current_support_conditions_satisfied"] == 2, "support condition count mismatch")
    require(decision["promoted_true_precision_route_count"] == 0, "candidate overclaims promoted true precision route")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision rows")
    require(decision["selected_internal_value_emission_count"] == 0, "candidate overclaims internal value emission")
    require(decision["selected_threshold_response_functional_instantiated"] is False, "candidate overclaims threshold functional")
    require(decision["accepted_internal_Rtheta_value_rows"] == 0, "candidate overclaims internal Rtheta rows")

    require(cert["closed_value_obligation_rows_at_admitted_external_tier"] == 4, "certificate external obligation count mismatch")
    require(cert["closed_value_obligation_rows_at_internal_no_knob_tier"] == 0, "certificate internal obligation count mismatch")
    require(cert["readiness_fraction"] == "8/9", "certificate readiness mismatch")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["next_required_artifact"] == candidate["next_attack"]["artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_postsourcevaluepromotionrows_or_trueprecisionexit.candidate.json",
                "status": candidate["status"],
                "source_promotion_gate": "consumed",
                "external_value_lane": "4/5 admitted replay obligations closed",
                "readiness": "8/9",
                "internal_no_knob_rows": 0,
                "accepted_true_equivalence_precision_rows": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected post-source value promotion rows audit passed")


if __name__ == "__main__":
    main()
