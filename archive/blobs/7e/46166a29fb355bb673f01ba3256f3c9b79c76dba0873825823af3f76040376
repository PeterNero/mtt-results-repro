from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_finite_hym_de_gap_promotion.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_dotd_source_end0_routing_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_dotd_source_end0_routing_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_dotD_Source_End0Routing_Reduction_v1.md"

STATUS = "POST_ALPHA_DOTD_SOURCE_REDUCED_END0_ROUTING_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)

    previous_gap_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_FINITE_HYM_DE_GAP_PROMOTED_DOTD_SOURCE_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1",
            prev["what_closes_now"]["DE_action_closed_for_gap_layer"] is True,
            prev["what_remains_open"]["selected_dotD_alpha1_source"] is True,
            all(prev["guardrails"].values()),
        ]
    )
    reduction_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["status"] == "U1Y_ROUTEC_DOTD_ALPHA1_SOURCENORM_NOGO_END0SECTOR_FUNCTOR_VALUES_OPEN",
            source["decision"]["naive_source_normalization_rejected"] is True,
            source["decision"]["End0_sector_route_primary"] is True,
            source["decision"]["selected_Ext_density_scale_tangent_closed_in_SM_support"] is True,
            source["decision"]["shared_circle_guardrail_retained"] is True,
            source["decision"]["same_basis_dotD_matrices_exist_conditionally"] is True,
            source["decision"]["honest_bn_validator_fails_only_by_source_flags"] is True,
            source["decision"]["dotD_alpha1_source_closed"] is False,
            source["decision"]["physical_dotD_alpha1_payload_extracted"] is False,
            source["decision"]["selected_End0_to_sector_functor_values_extracted"] is False,
            source["decision"]["selected_transfer_normalization_closed"] is False,
            source["decision"]["primitive_C1_values_computed"] is False,
            source["decision"]["A_selected_or_b_selected_emitted"] is False,
            source["decision"]["lambda_12_computable"] is False,
            source["decision"]["target_fitting_used"] is False,
            source["next_required_artifact"] == NEXT,
        ]
    )
    contract_open = all(
        [
            source["contract"]["status"] == "OPEN_SELECTED_END0_TO_SECTOR_FUNCTOR_VALUES_REQUIRED",
            source["contract"]["branch"]["q"] == 79,
            source["contract"]["branch"]["orientation"] == "F",
            source["contract"]["branch"]["torsion_label_m"] == 1,
            source["contract"]["domain"]["basis"] == ["T1", "T2", "T3"],
            source["contract"]["domain"]["current_supported_lane"] == "T3",
            source["contract"]["codomain"]["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3",
            all(value is None for value in source["contract"]["values"].values()),
            "selected_dotD_source_verified" in source["contract"]["validator_flags_that_must_be_theorem_derived"],
            "alpha1_driver_verified" in source["contract"]["validator_flags_that_must_be_theorem_derived"],
            "selected_transfer_normalization_verified"
            in source["contract"]["validator_flags_that_must_be_theorem_derived"],
        ]
    )
    route_a_nogo_valid = all(
        [
            source["route_A_source_normalization_nogo"]["closed_as_nogo"] is True,
            source["route_A_source_normalization_nogo"]["naive_Ext_scale_to_alpha1_source_normalization_rejected"]
            is True,
            source["route_A_source_normalization_nogo"]["does_not_vary_integral_c2_alpha1"] is True,
            source["route_A_source_normalization_nogo"]["central_shared_circle_retained"] is True,
            source["route_A_source_normalization_nogo"]["selected_source_strength_coordinate_absent"] is True,
            source["route_A_source_normalization_nogo"]["topological_support_present"] is True,
            source["route_A_source_normalization_nogo"]["visible_rank2_support"][
                "c2_extension_target_is_plus_4_alpha1"
            ]
            is True,
            source["route_A_source_normalization_nogo"]["visible_rank2_support"]["central_shared_circle_trivial"]
            is True,
        ]
    )
    route_b_open_valid = all(
        [
            source["route_B_end0_to_sector_routing"]["closed"] is False,
            source["route_B_end0_to_sector_routing"]["End0_row_response_available"] is True,
            source["route_B_end0_to_sector_routing"]["same_basis_dotD_matrices_exist"] is True,
            source["route_B_end0_to_sector_routing"]["conditional_weyl_transfer_exact"] is True,
            source["route_B_end0_to_sector_routing"]["su5_e6_structural_partition_available"] is True,
            source["route_B_end0_to_sector_routing"]["honest_bn_validator_fails_only_by_source_flags"] is True,
            source["route_B_end0_to_sector_routing"]["selected_End0_direction_support"] == "T3",
            source["route_B_end0_to_sector_routing"]["selected_End0_to_sector_functor_values_extracted"] is False,
            source["route_B_end0_to_sector_routing"]["selected_sector_routing_closed"] is False,
            source["route_B_end0_to_sector_routing"]["selected_transfer_normalization_closed"] is False,
            source["route_B_end0_to_sector_routing"]["physical_dotD_alpha1_payload_extracted"] is False,
            source["route_B_end0_to_sector_routing"]["values_promoted"] is False,
        ]
    )
    guardrails_ok = all(
        [
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_selected_dotD_source"] is False,
            source["guardrails"]["claims_alpha1_driver"] is False,
            source["guardrails"]["claims_selected_End0_to_sector_routing"] is False,
            source["guardrails"]["claims_selected_transfer_normalization"] is False,
            source["guardrails"]["claims_physical_alpha1_value_extracted"] is False,
            source["guardrails"]["claims_primitive_C1_values_computed"] is False,
            source["guardrails"]["claims_A_selected_or_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_full_sm_closure"] is False,
            source["guardrails"]["promotes_diagnostic_lift_as_proof"] is False,
            source["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_gap_ready,
            reduction_valid,
            contract_open,
            route_a_nogo_valid,
            route_b_open_valid,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaDotDSourceEnd0RoutingReductionImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The dotD_alpha1 source route is reduced to a selected End0-to-sector "
                "functor source-and-value packet. The naive identification of continuous "
                "Ext-density scaling with alpha1 source normalization is rejected because "
                "it does not vary the integral Chern/source row, and the shared circle remains "
                "degree-zero. Existing same-basis dotD/projector data are compatible support "
                "only until routing and transfer normalization are theorem-derived."
            ),
        },
        "status": STATUS,
        "contract": source["contract"],
        "route_A_source_normalization_nogo": source["route_A_source_normalization_nogo"],
        "route_B_end0_to_sector_routing": source["route_B_end0_to_sector_routing"],
        "checks": {
            "previous_gap_ready": previous_gap_ready,
            "reduction_valid": reduction_valid,
            "contract_open": contract_open,
            "route_a_nogo_valid": route_a_nogo_valid,
            "route_b_open_valid": route_b_open_valid,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": source["what_closes_now"],
        "what_remains_open": source["what_remains_open"],
        "guardrails": {
            "does_not_claim_dotD_source_or_alpha1_driver": True,
            "does_not_claim_selected_End0_sector_routing": True,
            "does_not_claim_transfer_normalization": True,
            "does_not_claim_primitive_C1_A_b_lambda_or_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "shared_circle_degree_zero_guardrail_retained": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "source": str(SOURCE),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_dotd_source_end0_routing_reduction",
        "status": STATUS,
        "closure_claimed": False,
        "dotD_alpha1_source_closed": False,
        "selected_End0_to_sector_functor_values_extracted": False,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha dotD Source End0Routing Reduction v1

## Result

The `dotD_alpha1` source route is reduced to selected End0-to-sector functor
values. The naive route is closed as a no-go:

```text
Ext-density scale is continuous inside a fixed rank-two extension class
c2(V_alpha)=4 alpha1 is integral Chern/source data
continuous Ext scaling does not vary the integral source row
shared circle remains degree-zero/trivial
```

The live route is now the End0-to-sector packet with `T1,T2,T3` domain basis,
current support in the `T3` lane, sector projectors, routing, and transfer
normalization still required.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
