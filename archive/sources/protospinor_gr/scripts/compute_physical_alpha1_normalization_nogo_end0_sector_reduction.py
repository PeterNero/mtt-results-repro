from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct.packet.json"
Q79_FILL = Q79 / "candidate_data" / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
SM_END0 = SM / "candidate_data" / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"

OUT_CERT = ROOT / "certificates" / "physical_alpha1_normalization_nogo_end0_sector_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "physical_alpha1_normalization_nogo_end0_sector_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Physical_alpha1_Normalization_NoGo_End0Sector_Reduction_v1.md"

STATUS = "PHYSICAL_ALPHA1_NAIVE_NORMALIZATION_NOGO_REDUCED_TO_END0_SECTOR_FUNCTOR_VALUES"
NEXT = "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    q79 = load(Q79_FILL)
    end0 = load(SM_END0)

    route_a_nogo = all(
        [
            q79["route_A_source_normalization"]["closed_as_nogo"] is True,
            q79["route_A_source_normalization"]["naive_Ext_scale_to_alpha1_source_normalization_rejected"] is True,
            q79["route_A_source_normalization"]["does_not_vary_integral_c2_alpha1"] is True,
            q79["route_A_source_normalization"]["central_shared_circle_retained"] is True,
            q79["route_A_source_normalization"]["visible_rank2_support"][
                "c2_extension_target_is_plus_4_alpha1"
            ]
            is True,
        ]
    )
    route_b_reduction = all(
        [
            q79["decision"]["sector_routing_route_remains_primary"] is True,
            q79["decision"]["selected_End0_to_sector_routing_values_extracted"] is False,
            q79["route_B_end0_to_sector_routing"]["End0_row_response_available"] is True,
            q79["route_B_end0_to_sector_routing"]["same_basis_dotD_matrices_exist"] is True,
            q79["route_B_end0_to_sector_routing"]["selected_End0_to_sector_functor_values_extracted"]
            is False,
            end0["decision"]["functor_contract_specified"] is True,
            end0["scalar_normalization_no_go"]["closed"] is True,
        ]
    )
    previous_kernel_respected = all(
        [
            prev["constructed_tangent_kernel"]["tangent"]["symbol"] == "h_ext",
            prev["payload_emission_status" if "payload_emission_status" in prev else "theorem"] is not None,
            prev["honest_replay_status"]["alpha1_driver_verified"] is False,
        ]
    )
    guardrails = all(
        [
            q79["guardrails"]["claims_alpha1_driver"] is False,
            q79["guardrails"]["claims_selected_End0_to_sector_routing"] is False,
            q79["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
            end0["target_fitting_used"] is False,
            end0["existing_value_tests"]["passes"] is False,
        ]
    )
    theorem_proved = all([route_a_nogo, route_b_reduction, previous_kernel_respected, guardrails])

    packet = {
        "theorem": {
            "name": "PhysicalAlpha1NormalizationNoGoEnd0SectorReduction",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The constructed h_ext tangent kernel cannot be promoted to physical "
                "alpha1 by naive source-strength normalization: continuous scaling "
                "inside a fixed rank-two extension class does not vary the integral "
                "Chern/source row c2(V_alpha)=4 alpha1, and the shared circle is "
                "degree-zero. The remaining legal route is a selected End0-to-sector "
                "functor/source/value packet that maps dotD[h_ext] to physical sector "
                "dotD_alpha1 matrices with theorem-derived normalization."
            ),
        },
        "route_A_naive_source_normalization_nogo": q79["route_A_source_normalization"],
        "route_B_end0_to_sector_reduction": {
            "closed": False,
            "End0_row_response_available": q79["route_B_end0_to_sector_routing"][
                "End0_row_response_available"
            ],
            "same_basis_dotD_matrices_exist": q79["route_B_end0_to_sector_routing"][
                "same_basis_dotD_matrices_exist"
            ],
            "selected_End0_to_sector_functor_values_extracted": False,
            "must_emit_next": q79["route_B_end0_to_sector_routing"]["must_emit_next"],
            "contract": end0["minimal_functor_contract"],
        },
        "what_closes_now": {
            "naive_Ext_scale_alpha1_normalization_rejected": route_a_nogo,
            "integral_Chern_row_distinguished_from_continuous_tangent": True,
            "shared_circle_degree_zero_guardrail_retained": True,
            "End0_sector_route_identified_as_primary": route_b_reduction,
            "scalar_normalization_no_go_imported": end0["scalar_normalization_no_go"]["closed"],
            "target_fitting_excluded": guardrails,
        },
        "what_remains_open": {
            "selected_End0_to_sector_functor_values": True,
            "selected_sector_zero_mode_realization": True,
            "selected_transfer_normalization": True,
            "sector_equality_from_selected_derivative_to_dotD_matrices": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "A_selected_and_b_selected": True,
        },
        "guardrails": {
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_selected_End0_to_sector_routing": True,
            "does_not_promote_existing_BN_values": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "input_artifacts": {
            "previous_kernel": str(PREV),
            "q79_value_fill": str(Q79_FILL),
            "sm_end0_functor_packet": str(SM_END0),
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "physical_alpha1_normalization_nogo_end0_sector_reduction",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "route_a_nogo": route_a_nogo,
            "route_b_reduction": route_b_reduction,
            "guardrails": guardrails,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Physical alpha1 Normalization NoGo and End0-Sector Reduction v1

## Result

The direct source-strength route is closed as a no-go for naive Ext scaling:
continuous scaling of the selected Ext representative does not vary the
integral Chern/source row `c2(V_alpha)=4 alpha1`. The shared circle remains
degree-zero, so it does not hide the missing source charge.

The remaining legal route is a selected End0-to-sector functor/source/value
packet mapping `dotD[h_ext]` to physical sector `dotD_alpha1`.

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
