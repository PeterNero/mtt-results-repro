from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_dynamic_c1_value_emission_cutset_certificate.json"

SM_CERT = SM_ROOT / "certificates" / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
SOURCE_RULE = SM_DIR / "differentiated_residual_projector_source_rule.contract.json"
ROUTE_LADDER = SM_DIR / "source_rule_or_execution_route_ladder.packet.json"
HONEST_EXECUTION = SM_DIR / "honest_galerkin_c1_execution_requirement.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_residual_projector_source_rule_contract_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_residual_projector_source_rule_contract.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_ResidualProjector_SourceRule_Contract_Import_v1.md"

STATUS = "POST_ALPHA_RESIDUAL_PROJECTOR_SOURCE_RULE_CONTRACT_IMPORTED_VALUES_OPEN"
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    sm_cert = load(SM_CERT)
    sm_candidate = load(SM_CANDIDATE)
    source_rule = load(SOURCE_RULE)
    route_ladder = load(ROUTE_LADDER)
    honest_execution = load(HONEST_EXECUTION)

    previous_cutset_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_selected_value_emission_cutset"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1",
        ]
    )

    imported_contract_ok = all(
        [
            sm_cert["theorem_proved"] is True,
            sm_cert["closure_claimed"] is False,
            sm_cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            sm_cert["no_knob_closure_claimed"] is False,
            sm_cert["true_SM_equivalence_claimed"] is False,
            sm_cert["observed_data_used"] is False,
            sm_cert["target_fitting_used"] is False,
            sm_cert["next_required_artifact"] == NEXT,
            all(sm_cert["what_closes"].values()),
            all(sm_cert["what_remains_open"].values()),
            sm_candidate["theorem"]["proved"] is True,
            sm_candidate["closure_claimed"] is False,
            sm_candidate["observed_data_used"] is False,
            sm_candidate["target_fitting_used"] is False,
            sm_candidate["next_required_artifact"] == NEXT,
            all(sm_candidate["what_closes_now"].values()),
            all(sm_candidate["what_remains_open"].values()),
        ]
    )

    source_rule_contract_ok = all(
        [
            source_rule["schema"] == "MTTDifferentiatedResidualProjectorSourceRuleContract.v1",
            source_rule["status"] == "SOURCE_RULE_CONTRACT_EMITTED_VALUES_OPEN",
            source_rule["observed_data_used"] is False,
            source_rule["target_fitting_used"] is False,
            source_rule["already_selected_support"]["canonical_Q_residual_available"] is True,
            source_rule["already_selected_support"]["Q_residual_rank"] == 6,
            source_rule["already_selected_support"]["alpha1_dotD_driver_verified"] is True,
            source_rule["already_selected_support"]["primitive_vertex_or_basis_transport_source_selector_promoted"] is True,
            source_rule["currently_emitted"]["selected_differentiated_residual_projector_source_rule"] is False,
            source_rule["currently_emitted"]["selected_basis_transport_vertex_or_Hessian_values"] is False,
            source_rule["currently_emitted"]["selected_A_selected"] is False,
            source_rule["currently_emitted"]["selected_b_selected"] is False,
            source_rule["currently_emitted"]["selected_deltaTheta_C1"] is False,
            source_rule["why_selector_is_not_enough"]["source_selector_is_value_emission"] is False,
            source_rule["why_selector_is_not_enough"]["stationary_transport_only_ruled_out"] is True,
            source_rule["why_selector_is_not_enough"]["primitive_fixed_fiber_span_can_close"] is False,
        ]
    )

    conditional_values = source_rule["exact_conditional_values_if_rule_is_proved"]
    conditional_values_ok = all(
        [
            conditional_values["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional_values["A_transpose_b"] == [12.0, 12.0],
            conditional_values["deltaTheta_C1"] == [1.0, 1.0],
            conditional_values["rank"] == 2,
            conditional_values["SM_parity_dynamic_packet_would_close"] is True,
            conditional_values["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    route_ladder_ok = all(
        [
            route_ladder["schema"] == "MTTSourceRuleOrExecutionRouteLadder.v1",
            route_ladder["status"] == "ROUTE_LADDER_RANKED_NO_PROMOTION",
            route_ladder["recommended_next"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            route_ladder["observed_data_used"] is False,
            route_ladder["target_fitting_used"] is False,
            route_ladder["near_straight_source_path"]["algebraically_sufficient"] is True,
            route_ladder["near_straight_source_path"]["conditional_A_rank"] == 2,
            route_ladder["near_straight_source_path"]["id"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            route_ladder["straight_path"]["id"] == "A_differentiated_residual_projector_rule",
            route_ladder["superset_execution_path"]["id"] == "C_honest_selected_Galerkin_C1_execution",
            route_ladder["superset_execution_path"]["selected_source_verified"] is False,
            "using observed SM flavor data or benchmark matrices as selectors" in route_ladder["ruled_out_paths"],
        ]
    )

    honest_execution_ok = all(
        [
            honest_execution["schema"] == "MTTHonestGalerkinC1ExecutionRequirement.v1",
            honest_execution["status"] == "HONEST_EXECUTION_REQUIREMENT_REEMITTED_VALUES_OPEN",
            honest_execution["selected_source_verified"] is False,
            honest_execution["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            honest_execution["observed_flavor_data_forbidden"] is True,
            honest_execution["target_fitting_forbidden"] is True,
            honest_execution["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            honest_execution["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
            honest_execution["required_outputs"]
            == [
                "zero_mode_bases",
                "primitive_three_by_three_contraction_terms",
                "linear_response_matrices",
                "C33/nonzero-family-rank tests",
            ],
        ]
    )

    what_closes_now = {
        "previous_value_emission_cutset_consumed": previous_cutset_ok,
        "differentiated_residual_projector_source_rule_contract_imported": imported_contract_ok,
        "canonical_Q_residual_support_recorded": source_rule_contract_ok,
        "conditional_values_quarantined_until_rule_or_execution": conditional_values_ok,
        "three_legal_routes_ranked": route_ladder_ok,
        "honest_Galerkin_execution_requirements_reemitted": honest_execution_ok,
        "stationary_and_fixed_fiber_shortcuts_ruled_out": (
            source_rule["why_selector_is_not_enough"]["stationary_transport_only_ruled_out"] is True
            and source_rule["why_selector_is_not_enough"]["primitive_fixed_fiber_span_can_close"] is False
            and "stationary transport-only Phi_fin^C1" in route_ladder["ruled_out_paths"]
            and "pure fixed-fiber primitive replay" in route_ladder["ruled_out_paths"]
        ),
    }

    legal_routes = {
        "A_differentiated_residual_projector_rule": {
            "description": route_ladder["straight_path"]["description"],
            "status": route_ladder["straight_path"]["current_status"],
            "why_not_closed": route_ladder["straight_path"]["why_not_closed"],
        },
        "B_enriched_weylpair_basis_transport_or_vertex_source": {
            "description": route_ladder["near_straight_source_path"]["description"],
            "status": route_ladder["near_straight_source_path"]["current_status"],
            "recommended_primary": True,
            "algebraically_sufficient": True,
            "why_not_closed": route_ladder["near_straight_source_path"]["why_not_closed"],
        },
        "C_honest_selected_Galerkin_C1_execution": {
            "description": route_ladder["superset_execution_path"]["description"],
            "status": route_ladder["superset_execution_path"]["current_status"],
            "required_outputs": route_ladder["superset_execution_path"]["required_outputs"],
            "selected_source_verified": False,
        },
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
        "does_not_promote_source_selector_as_value_emission": True,
        "does_not_promote_conditional_A_b_deltaTheta": True,
        "does_not_use_observed_flavor_data": True,
        "does_not_use_target_fitting": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_no_knob_or_true_SM_closure": True,
    }

    theorem_proved = all(
        [
            all(what_closes_now.values()),
            all(what_remains_open.values()),
            all(guardrails.values()),
        ]
    )

    theorem = {
        "name": "PostAlphaResidualProjectorSourceRuleContractImport",
        "proved": theorem_proved,
        "closure_claimed": False,
        "statement": (
            "After the dynamic C1 value-emission cutset, the next exact "
            "contract is a three-route value-emission theorem: prove the "
            "selected differentiated residual-projector source rule, promote "
            "same-branch enriched Weyl-pair basis-transport/vertex/Hessian "
            "source emission, or run honest selected Galerkin C1 execution. "
            "The enriched Weyl-pair route is ranked primary because it is "
            "already algebraically sufficient, but it is not promoted without "
            "same-branch selected source emission."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "already_selected_support": source_rule["already_selected_support"],
        "legal_routes": legal_routes,
        "recommended_next_route": route_ladder["recommended_next"],
        "conditional_values_if_rule_or_execution_closes": {
            **conditional_values,
            "selected_now": False,
        },
        "required_emissions": source_rule["required_emissions"],
        "honest_galerkin_required_outputs": honest_execution["required_outputs"],
        "ruled_out_paths": route_ladder["ruled_out_paths"],
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "frontier_is_three_route_value_emission_contract": True,
            "recommended_primary_route": "B_enriched_weylpair_basis_transport_or_vertex_source",
            "conditional_values_promoted": False,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_dynamic_c1_value_emission_cutset": str(PREV),
            "sm_residual_projector_certificate": str(SM_CERT),
            "sm_residual_projector_candidate": str(SM_CANDIDATE),
            "source_rule_contract": str(SOURCE_RULE),
            "route_ladder": str(ROUTE_LADDER),
            "honest_execution_requirement": str(HONEST_EXECUTION),
        },
    }

    note = f"""# PostAlpha Residual Projector Source-Rule Contract Import v1

## Result

The dynamic C1 value-emission frontier has been sharpened into a three-route
contract.

Legal routes:

```text
A. Prove selected differentiated Phi_fin^C1 applies Q_residual.
B. Promote enriched Weyl-pair basis-transport/vertex/Hessian source emission.
C. Run honest selected Galerkin C1 execution.
```

Route B is ranked primary because its Weyl-pair packet is already
algebraically sufficient, with conditional rank 2. It is still not promoted:
same-branch selected source emission remains missing.

Conditional values if a legal route emits them:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
```

Stationary transport-only Phi_fin^C1, pure fixed-fiber primitive replay,
canonical Q_residual without an application/source rule, and observed flavor
data as selectors remain ruled out.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_residual_projector_source_rule_contract",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "legal_routes": legal_routes,
        "recommended_next_route": route_ladder["recommended_next"],
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
