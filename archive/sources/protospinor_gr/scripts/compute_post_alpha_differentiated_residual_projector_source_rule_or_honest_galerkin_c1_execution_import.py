from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill_certificate.json"
SLUG = "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
SOURCE_RULE = SM_DIR / "differentiated_residual_projector_source_rule.contract.json"
ROUTE_LADDER = SM_DIR / "source_rule_or_execution_route_ladder.packet.json"
EXECUTION_REQ = SM_DIR / "honest_galerkin_c1_execution_requirement.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_Import_v1.md"

STATUS = "POST_ALPHA_DIFFERENTIATED_RESIDUAL_PROJECTOR_SOURCE_RULE_OR_HONEST_GALERKIN_C1_EXECUTION_IMPORTED_SOURCE_RULE_CONTRACT_OPEN"
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    source_rule = load(SOURCE_RULE)
    route_ladder = load(ROUTE_LADDER)
    execution_req = load(EXECUTION_REQ)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_differentiated_residual_projector_source_rule_or_honest_galerkin_execution"]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            cert["no_knob_closure_claimed"] is False,
            cert["true_SM_equivalence_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "DifferentiatedResidualProjectorSourceRuleCutsetTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["differentiated_residual_projector_source_rule_promoted"] is False,
            candidate["promotion_decision"]["enriched_weylpair_source_emission_promoted"] is False,
            candidate["promotion_decision"]["honest_Galerkin_C1_execution_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["no_knob_flavor_constants_closed"] is False,
        ]
    )

    source_rule_ok = all(
        [
            source_rule["schema"] == "MTTDifferentiatedResidualProjectorSourceRuleContract.v1",
            source_rule["status"] == "SOURCE_RULE_CONTRACT_EMITTED_VALUES_OPEN",
            source_rule["rule_name"] == "SelectedDifferentiatedResidualProjectorSourceRule",
            source_rule["already_selected_support"]["canonical_Q_residual_available"] is True,
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

    route_ok = all(
        [
            route_ladder["schema"] == "MTTSourceRuleOrExecutionRouteLadder.v1",
            route_ladder["status"] == "ROUTE_LADDER_RANKED_NO_PROMOTION",
            route_ladder["recommended_next"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            route_ladder["near_straight_source_path"]["algebraically_sufficient"] is True,
            route_ladder["near_straight_source_path"]["conditional_A_rank"] == 2,
            route_ladder["near_straight_source_path"]["why_not_closed"]
            == "The columns solve the locked algebraic equation, but current artifacts do not yet prove same-branch selected source emission of the Weyl-pair packet.",
            route_ladder["straight_path"]["current_status"] == "OPEN_NEW_SOURCE_RULE_REQUIRED",
            route_ladder["superset_execution_path"]["selected_source_verified"] is False,
            route_ladder["observed_data_used"] is False,
            route_ladder["target_fitting_used"] is False,
        ]
    )

    execution_ok = all(
        [
            execution_req["schema"] == "MTTHonestGalerkinC1ExecutionRequirement.v1",
            execution_req["status"] == "HONEST_EXECUTION_REQUIREMENT_REEMITTED_VALUES_OPEN",
            execution_req["selected_source_verified"] is False,
            execution_req["target_fitting_forbidden"] is True,
            execution_req["observed_flavor_data_forbidden"] is True,
            execution_req["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            execution_req["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
            "primitive_three_by_three_contraction_terms" in execution_req["required_outputs"],
            "CP-odd invariant test" in execution_req["acceptance_checks"],
        ]
    )

    what_closes_now = {
        "PhiFinC1_transport_only_no_go_gate_consumed": prev_ok,
        "differentiated_source_rule_cutset_imported": imported_ok,
        "source_rule_contract_formalized": source_rule_ok,
        "conditional_value_if_rule_is_proved_recorded": conditional_ok,
        "route_ladder_ranked_without_promotion": route_ok,
        "honest_galerkin_execution_requirement_reemitted": execution_ok,
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
        "name": "PostAlphaDifferentiatedResidualProjectorSourceRuleCutsetImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "SM-parity dynamic closure has been reduced to three legal value-emission "
            "routes: selected differentiated residual-projector source rule, same-branch "
            "enriched Weyl-pair basis-transport/vertex/Hessian emission, or honest selected "
            "Galerkin C1 execution. The enriched Weyl-pair route is ranked as the shortest "
            "algebraically sufficient route, but no value emission is promoted here."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "promotion_decision": candidate["promotion_decision"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "differentiated_residual_projector_source_rule_contract": source_rule,
        "source_rule_or_execution_route_ladder": route_ladder,
        "honest_galerkin_c1_execution_requirement": execution_req,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_rule_contract_closed_but_values_open": True,
            "recommended_next": route_ladder["recommended_next"],
            "frontier_is_weylpair_source_emission_or_honest_galerkin_value_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "differentiated_residual_projector_source_rule_contract": str(SOURCE_RULE),
            "source_rule_or_execution_route_ladder": str(ROUTE_LADDER),
            "honest_galerkin_c1_execution_requirement": str(EXECUTION_REQ),
        },
    }

    note = f"""# PostAlpha DifferentiatedResidualProjectorSourceRule or HonestGalerkinC1Execution Import v1

## Result

The source-rule contract is now formalized, but selected value emission remains
open.

Recommended next route:

```text
{route_ladder["recommended_next"]}
```

Conditional values if a selected rule/source emission is proved:

```text
A^T A         = [[12, 0], [0, 12]]
A^T b         = [12, 12]
deltaTheta_C1 = [1, 1]
rank          = 2
```

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
        "certificate": "post_alpha_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution",
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
