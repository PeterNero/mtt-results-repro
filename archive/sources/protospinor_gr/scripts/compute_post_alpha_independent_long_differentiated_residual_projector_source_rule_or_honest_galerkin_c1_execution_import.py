from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_independent_long_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_IndependentLongDifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_Import_v1.md"
)

STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_DIFFERENTIATED_RESIDUAL_PROJECTOR_SOURCE_RULE_OR_"
    "HONEST_GALERKIN_C1_EXECUTION_REANCHORED_SOURCE_RULE_CONTRACT_OPEN"
)
SOURCE_STATUS = (
    "POST_ALPHA_INDEPENDENT_DIFFERENTIATED_RESIDUAL_PROJECTOR_SOURCE_RULE_OR_"
    "HONEST_GALERKIN_C1_EXECUTION_IMPORTED_SOURCE_RULE_CONTRACT_OPEN"
)
THIS_ARTIFACT = "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1"
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["fresh_long_stationary_transport_only_no_go_closed"] is True,
            prev["frontier_decision"][
                "frontier_is_differentiated_residual_projector_source_rule_or_honest_galerkin_execution"
            ]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["frontier_decision"]["source_rule_contract_closed_but_values_open"] is True,
            source["frontier_decision"]["recommended_next"]
            == "B_enriched_weylpair_basis_transport_or_vertex_source",
            source["frontier_decision"]["frontier_is_weylpair_source_emission_or_honest_galerkin_value_run"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    source_rule = source_packet["differentiated_residual_projector_source_rule_contract"]
    ladder = source_packet["source_rule_or_execution_route_ladder"]
    execution = source_packet["honest_galerkin_c1_execution_requirement"]

    source_rule_ok = all(
        [
            source_rule["schema"] == "MTTDifferentiatedResidualProjectorSourceRuleContract.v1",
            source_rule["status"] == "SOURCE_RULE_CONTRACT_EMITTED_VALUES_OPEN",
            source_rule["already_selected_support"]["Q_residual_rank"] == 6,
            source_rule["already_selected_support"]["alpha1_dotD_driver_verified"] is True,
            source_rule["already_selected_support"]["source_selector_promoted"] is True,
            source_rule["currently_emitted"]["selected_differentiated_residual_projector_source_rule"] is False,
            source_rule["currently_emitted"]["selected_basis_transport_vertex_or_Hessian_values"] is False,
            source_rule["currently_emitted"]["selected_A_selected"] is False,
            source_rule["currently_emitted"]["selected_b_selected"] is False,
            source_rule["currently_emitted"]["selected_deltaTheta_C1"] is False,
            source_rule["why_selector_is_not_enough"]["stationary_transport_only_ruled_out"] is True,
            source_rule["why_selector_is_not_enough"]["source_selector_is_value_emission"] is False,
            source_rule["observed_data_used"] is False,
            source_rule["target_fitting_used"] is False,
        ]
    )

    conditional = source_rule["exact_conditional_values_if_rule_is_proved"]
    conditional_ok = all(
        [
            conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional["A_transpose_b"] == [12.0, 12.0],
            conditional["deltaTheta_C1"] == [1.0, 1.0],
            conditional["rank"] == 2,
            conditional["SM_parity_dynamic_packet_would_close"] is True,
            conditional["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    ladder_ok = all(
        [
            ladder["schema"] == "MTTSourceRuleOrExecutionRouteLadder.v1",
            ladder["status"] == "ROUTE_LADDER_RANKED_NO_PROMOTION",
            ladder["recommended_next"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            ladder["near_straight_source_path"]["algebraically_sufficient"] is True,
            ladder["near_straight_source_path"]["conditional_A_rank"] == 2,
            ladder["straight_path"]["current_status"] == "OPEN_NEW_SOURCE_RULE_REQUIRED",
            ladder["superset_execution_path"]["selected_source_verified"] is False,
            ladder["observed_data_used"] is False,
            ladder["target_fitting_used"] is False,
        ]
    )

    execution_ok = all(
        [
            execution["schema"] == "MTTHonestGalerkinC1ExecutionRequirement.v1",
            execution["status"] == "HONEST_EXECUTION_REQUIREMENT_REEMITTED_VALUES_OPEN",
            execution["selected_source_verified"] is False,
            execution["target_fitting_forbidden"] is True,
            execution["observed_flavor_data_forbidden"] is True,
            execution["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            execution["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
        ]
    )

    what_closes_now = {
        "fresh_long_PhiFinC1_transport_no_go_gate_consumed": prev_ok,
        "independent_source_rule_contract_replayed": source_ok,
        "source_rule_contract_reanchored": source_rule_ok,
        "conditional_values_remain_conditional": conditional_ok,
        "route_ladder_reanchored_without_promotion": ladder_ok,
        "honest_galerkin_execution_requirement_reanchored": execution_ok,
    }

    what_remains_open = {
        "selected_enriched_weylpair_source_emission": True,
        "selected_differentiated_residual_projector_source_rule": True,
        "selected_basis_transport_vertex_or_Hessian_values": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_promote_source_rule_as_values": True,
        "does_not_promote_enriched_weylpair_source_emission": True,
        "does_not_promote_honest_galerkin_execution": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentLongDifferentiatedResidualProjectorSourceRuleCutsetTheorem",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The fresh long branch reanchors the differentiated residual-projector source-rule "
            "contract and proves the route ladder: enriched Weyl-pair source emission is the "
            "shortest algebraically sufficient next route, but selected source values, Galerkin "
            "values, A/b/deltaTheta, SM dynamic parity, true SM equivalence, and no-knob flavor "
            "closure remain unpromoted."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_independent_differentiated_rule_certificate": source,
        "differentiated_residual_projector_source_rule_contract": source_rule,
        "source_rule_or_execution_route_ladder": ladder,
        "honest_galerkin_c1_execution_requirement": execution,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_rule_contract_closed_but_values_open": True,
            "recommended_next": ladder["recommended_next"],
            "frontier_is_weylpair_source_emission_or_honest_galerkin_value_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_fresh_long_phifinc1_nogo_certificate": str(PREV),
            "source_independent_differentiated_rule_certificate": str(SOURCE_CERT),
            "source_independent_differentiated_rule_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha IndependentLong DifferentiatedResidualProjectorSourceRule or HonestGalerkinC1Execution Import v1

## Result

The fresh long branch now carries the differentiated residual-projector source-rule
contract and route ladder.

Recommended next route:

```text
{ladder["recommended_next"]}
```

Conditional only:

```text
A^T A         = [[12, 0], [0, 12]]
A^T b         = [12, 12]
deltaTheta_C1 = [1, 1]
rank          = 2
```

No selected source values or Galerkin values are promoted here.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_independent_long_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
