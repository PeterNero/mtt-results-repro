"""Import the End0-to-sector functor value-packet reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

BRIDGE = CERTS / "q79_alpha1_retarded_kernel_formula_nmtt_bridge_certificate.json"
Q79_VALUE_FILL = (
    Q79
    / "certificates"
    / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json"
)

SM_END0_PACKET = SM / "certificates" / "selected_end0_to_sector_functor_source_and_value_packet_certificate.json"
SM_TENSOR = SM / "certificates" / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct_certificate.json"
SM_ADJOINT = SM / "certificates" / "selected_sector_zero_mode_adjointtriplet_realization_theorem_certificate.json"
SM_ACTION_FILL = (
    SM
    / "certificates"
    / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill_certificate.json"
)
SM_SOURCE_ACTION = (
    SM
    / "certificates"
    / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem_certificate.json"
)
SM_SOURCE_PAYLOAD = (
    SM / "certificates" / "selected_sector_zero_mode_source_payload_search_or_emission_attempt_certificate.json"
)
SM_ZERO_MODE_THEOREM = (
    SM / "certificates" / "selected_zero_mode_basis_from_hym_projector_source_theorem_certificate.json"
)
SM_HYM_VALUES = SM / "certificates" / "selected_hym_projector_zeromode_basis_value_emission_certificate.json"
SM_GRAM_TRANSFER = SM / "certificates" / "selected_sectorcharge_gram_transfernormalization_packet_certificate.json"

OUTPUT_PACKET = DATA / "end0_sector_functor_value_packet_reduction.candidate.json"
OUTPUT_CERT = CERTS / "end0_sector_functor_value_packet_reduction_certificate.json"
OUTPUT_NOTE = CORPUS / "End0_SectorFunctor_Value_Packet_Reduction_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    bridge = load(BRIDGE)
    q79_fill = load(Q79_VALUE_FILL)
    end0_packet = load(SM_END0_PACKET)
    tensor = load(SM_TENSOR)
    adjoint = load(SM_ADJOINT)
    action_fill = load(SM_ACTION_FILL)
    source_action = load(SM_SOURCE_ACTION)
    source_payload = load(SM_SOURCE_PAYLOAD)
    zero_mode = load(SM_ZERO_MODE_THEOREM)
    hym_values = load(SM_HYM_VALUES)
    gram_transfer = load(SM_GRAM_TRANSFER)

    reduction_checks = {
        "E0_previous_frontier_is_End0_functor_packet": bridge["verdict"][
            "next_required_artifact"
        ]
        == "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
        "E1_q79_value_fill_names_same_packet": q79_fill["next_required_artifact"]
        == "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
        "E2_sm_attempt_matches_packet_and_rejects_existing_values": end0_packet[
            "certificate"
        ]
        == "MTT_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"
        and not end0_packet["closure_claimed"]
        and not end0_packet["existing_BN_or_compact_values_promoted"]
        and not end0_packet["scalar_normalization_sufficient"],
        "E3_End0_tensor_product_carrier_constructed": tensor[
            "End0_tensor_product_carrier_constructed"
        ]
        and tensor["sector_projectors_constructed"],
        "E4_adjoint_triplet_choice_conditionally_closed": adjoint[
            "theorem_proved"
        ]
        and adjoint["conditional_representation_choice_closed"],
        "E5_canonical_source_map_constructed_but_unselected": source_payload[
            "canonical_source_map_constructed"
        ]
        and not source_payload["selected_source_map_emitted"],
        "E6_zero_mode_bridge_theorem_reduces_to_projector_values": zero_mode[
            "bridge_theorem_proved"
        ]
        and not zero_mode["selected_projector_values_emitted"],
        "E7_model_active_HYM_projector_values_emitted_not_selected": hym_values[
            "finite_projector_values_emitted"
        ]
        and not hym_values["selected_HYM_projector_values_promoted"],
        "E8_gram_transfer_scalar_conditional_after_rho_s": gram_transfer[
            "conditional_gram_transfer_scalar_fixed_after_rho_s"
        ]
        and not gram_transfer["selected_transfer_normalization"],
        "E9_selected_End0_values_not_yet_extracted": not end0_packet[
            "selected_End0_to_sector_functor_values_extracted"
        ],
    }

    theorem_proved = all(reduction_checks.values())

    return {
        "packet": "End0_SectorFunctor_Value_Packet_Reduction_v1",
        "status": "END0_SECTOR_FUNCTOR_PACKET_REDUCED_TO_SELECTED_PROJECTOR_SOURCE_PROMOTION_OPEN",
        "inputs": {
            "q79_bridge": str(BRIDGE.relative_to(ROOT)),
            "q79_value_fill": str(Q79_VALUE_FILL),
            "sm_end0_packet": str(SM_END0_PACKET),
            "sm_tensor_carrier": str(SM_TENSOR),
            "sm_adjoint_triplet": str(SM_ADJOINT),
            "sm_action_fill": str(SM_ACTION_FILL),
            "sm_source_action": str(SM_SOURCE_ACTION),
            "sm_source_payload": str(SM_SOURCE_PAYLOAD),
            "sm_zero_mode_theorem": str(SM_ZERO_MODE_THEOREM),
            "sm_hym_values": str(SM_HYM_VALUES),
            "sm_gram_transfer": str(SM_GRAM_TRANSFER),
        },
        "theorem": {
            "name": "End0SectorFunctorValuePacketReductionTheorem",
            "proved": theorem_proved,
            "statement": (
                "The requested End0-to-sector functor value packet has been "
                "attempted in the SM-parity branch.  Existing B_N and compact "
                "Route-C values cannot be promoted, scalar normalization alone "
                "is insufficient, and the correct carrier is the End0 tensor "
                "product with adjoint-triplet matter sectors and a singlet "
                "Higgs sector.  The remaining blocker is selected source "
                "promotion of zero-mode/HYM projector values, together with "
                "selected matter-slot routing and transfer normalization."
            ),
        },
        "reduction_checks": reduction_checks,
        "closed_support": {
            "End0_tensor_product_carrier": {
                "constructed": tensor["End0_tensor_product_carrier_constructed"],
                "sector_projectors_constructed": tensor["sector_projectors_constructed"],
                "next": tensor["next_required_artifact"],
            },
            "adjoint_triplet_realization": {
                "theorem_proved": adjoint["theorem_proved"],
                "conditional_representation_choice_closed": adjoint[
                    "conditional_representation_choice_closed"
                ],
                "next": adjoint["next_required_artifact"],
            },
            "canonical_source_map": {
                "constructed": source_payload["canonical_source_map_constructed"],
                "selected_source_map_emitted": source_payload["selected_source_map_emitted"],
                "next": source_payload["next_required_artifact"],
            },
            "model_active_projectors": {
                "finite_projector_values_emitted": hym_values[
                    "finite_projector_values_emitted"
                ],
                "selected_HYM_projector_values_promoted": hym_values[
                    "selected_HYM_projector_values_promoted"
                ],
                "next": hym_values["next_required_artifact"],
            },
        },
        "blocked_promotions": {
            "existing_BN_or_compact_values_promoted": end0_packet[
                "existing_BN_or_compact_values_promoted"
            ],
            "selected_End0_to_sector_functor_values_extracted": end0_packet[
                "selected_End0_to_sector_functor_values_extracted"
            ],
            "selected_End0_action_values_filled": action_fill[
                "selected_End0_action_values_filled"
            ],
            "selected_matter_slot_routing_filled": action_fill[
                "selected_matter_slot_routing_filled"
            ],
            "selected_payload_emitted": source_action["selected_payload_emitted"],
            "selected_rho_s_promoted": zero_mode["selected_rho_s_promoted"],
            "selected_transfer_normalization": gram_transfer[
                "selected_transfer_normalization"
            ],
            "alpha1_driver_verified": gram_transfer["alpha1_driver_verified"],
        },
        "frontier_update": {
            "old_next": bridge["verdict"]["next_required_artifact"],
            "sm_packet_status": end0_packet["status"],
            "current_next_primary": hym_values["next_required_artifact"],
            "current_next_parallel": gram_transfer["next_required_artifact"],
            "why": (
                "The End0 functor object is no longer a blank box: the carrier, "
                "conditional adjoint representation, canonical source map, and "
                "model-active HYM projectors are known.  Honest promotion now "
                "requires selected HYM/projector source promotion and the "
                "sector-charge/Gram/transfer-normalization source packet."
            ),
        },
        "guardrails": {
            "does_not_promote_existing_BN_values": True,
            "does_not_claim_selected_projector_values": True,
            "does_not_claim_selected_rho_s": True,
            "does_not_claim_selected_End0_functor_values": True,
            "does_not_claim_selected_transfer_normalization": True,
            "does_not_claim_dotD_or_C1_replay": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The End0-to-sector value packet is reduced to concrete source "
                "promotion gates.  It is not a missing-shape problem anymore: "
                "the End0 tensor carrier and conditional adjoint-triplet sector "
                "representation are in place."
            ),
            "what_remains": (
                "Promote the model-active HYM projector/zero-mode values to "
                "selected values from the same source, and close the selected "
                "sector-charge/Gram/transfer-normalization packet."
            ),
            "next_required_artifacts": [
                hym_values["next_required_artifact"],
                gram_transfer["next_required_artifact"],
            ],
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "End0SectorFunctorValuePacketReduction",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "reduction_checks": packet["reduction_checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# End0 SectorFunctor Value Packet Reduction v1

## Result

Status: `{cert["status"]}`

The requested `Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1`
has now been tested against the SM-parity End0 packet chain.  It does not close
as selected values, but it reduces sharply.

The carrier and representation shape are no longer the main blocker:

- the End0 tensor-product carrier is constructed,
- sector projectors are constructed,
- matter sectors are forced to the adjoint triplet conditionally,
- the Higgs sector is the singlet,
- a canonical source map is constructed,
- model-active HYM projector values are emitted.

The remaining blocker is selected source promotion of those HYM projector and
zero-mode values, plus selected sector-charge/Gram/transfer normalization.

## Reduction Checks

```json
{json.dumps(packet["reduction_checks"], indent=2, sort_keys=True)}
```

## Closed Support

```json
{json.dumps(packet["closed_support"], indent=2, sort_keys=True)}
```

## Blocked Promotions

```json
{json.dumps(packet["blocked_promotions"], indent=2, sort_keys=True)}
```

## Frontier Update

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
