"""Import projector source promotion and dotD transport reduction."""

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

PREVIOUS = CERTS / "end0_sector_functor_value_packet_reduction_certificate.json"
FINITE_PROMOTION = SM / "certificates" / "selected_finite_projector_source_promotion_certificate.json"
GAUGE_TRANSPORT = SM / "certificates" / "selected_gauge_transported_bn_phifin_trace_certificate.json"
TRANSPORT_REPLAY = SM / "certificates" / "selected_transport_conjugation_validator_replay_certificate.json"
DOTD_TRANSPORT = SM / "certificates" / "selected_dotd_alpha1_transport_derivative_probe_certificate.json"
ALPHA1_THEOREM = SM / "certificates" / "selected_alpha1_source_strength_normalization_theorem_certificate.json"
ALPHA1_FILL = SM / "certificates" / "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt_certificate.json"
GRAM_TRANSFER = SM / "certificates" / "selected_sectorcharge_gram_transfernormalization_packet_certificate.json"

OUTPUT_PACKET = DATA / "projector_source_promotion_dotd_transport_reduction.candidate.json"
OUTPUT_CERT = CERTS / "projector_source_promotion_dotd_transport_reduction_certificate.json"
OUTPUT_NOTE = CORPUS / "Projector_Source_Promotion_dotD_Transport_Reduction_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    finite = load(FINITE_PROMOTION)
    gauge = load(GAUGE_TRANSPORT)
    replay = load(TRANSPORT_REPLAY)
    dotd = load(DOTD_TRANSPORT)
    alpha1 = load(ALPHA1_THEOREM)
    fill = load(ALPHA1_FILL)
    gram = load(GRAM_TRANSFER)

    checks = {
        "P0_previous_frontier_was_projector_and_transfer": previous["verdict"][
            "next_required_artifacts"
        ]
        == [
            "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1",
            "MTT_Selected_SectorCharge_or_ZeroModeBasis_SourceEmission_v1",
        ],
        "P1_gauge_transported_trace_proved": gauge["gauge_transported_trace_proved"]
        and gauge["functional_rho_s_promoted"],
        "P2_transport_conjugation_validator_replay_closed": replay[
            "finite_validator_replay_closed"
        ]
        and replay["selected_source_verified"]
        and replay["selected_rho_s_validator_ready"],
        "P3_finite_projector_source_promotion_proved": finite[
            "finite_projector_source_promotion_proved"
        ]
        and finite["selected_projector_source_verified"]
        and finite["transported_packet_promoted"]
        and finite["validator_ready_stationary_rho_s"],
        "P4_raw_untransported_packet_not_promoted": not finite[
            "raw_untransported_packet_promoted"
        ],
        "P5_dotD_transport_derivative_formula_closed": dotd[
            "transport_derivative_formula_closed"
        ]
        and dotd["selected_dotD_source_formula_closed"]
        and dotd["selected_dotD_source_verified_by_transport_derivative"],
        "P6_dotD_full_replay_still_waits_on_driver": not dotd[
            "dotD_validator_full_replay_closed"
        ]
        and not dotd["alpha1_driver_verified"],
        "P7_alpha1_driver_acceptance_theorem_built_value_open": alpha1[
            "alpha1_driver_acceptance_theorem_built"
        ]
        and alpha1["conditional_dotd_closure_theorem_built"]
        and not alpha1["normalization_value_emitted"]
        and not alpha1["alpha1_driver_verified"],
        "P8_transfer_cutset_still_open": fill["minimal_cutset_identified"]
        and not fill["route_A_closed"]
        and not fill["route_B_closed"]
        and not gram["selected_transfer_normalization"],
    }

    theorem_proved = all(checks.values())

    return {
        "packet": "Projector_Source_Promotion_dotD_Transport_Reduction_v1",
        "status": "PROJECTOR_SOURCE_PROMOTION_AND_DOTD_TRANSPORT_CLOSED_ALPHA1_DRIVER_VALUE_OPEN",
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "finite_projector_source_promotion": str(FINITE_PROMOTION),
            "gauge_transported_trace": str(GAUGE_TRANSPORT),
            "transport_conjugation_replay": str(TRANSPORT_REPLAY),
            "dotd_transport_derivative": str(DOTD_TRANSPORT),
            "alpha1_source_strength_theorem": str(ALPHA1_THEOREM),
            "alpha1_sourcestrength_or_transfer_fill": str(ALPHA1_FILL),
            "gram_transfer": str(GRAM_TRANSFER),
        },
        "theorem": {
            "name": "ProjectorSourcePromotionDotDTransportReductionTheorem",
            "proved": theorem_proved,
            "statement": (
                "The selected projector/source promotion gate is closed at the "
                "stationary transported-packet level: gauge-transported Phi_fin, "
                "transport-conjugation validator replay, selected projector "
                "source verification, and validator-ready stationary rho_s are "
                "proved.  The dotD transport derivative/source formula is also "
                "closed.  The remaining blocker is not projector selection or "
                "the dotD formula; it is the selected alpha1 driver/source-strength "
                "or transfer-normalization value needed for honest dotD replay."
            ),
        },
        "checks": checks,
        "closed_now": {
            "gauge_transported_trace": {
                "status": gauge["status"],
                "functional_rho_s_promoted": gauge["functional_rho_s_promoted"],
                "gauge_transported_trace_proved": gauge["gauge_transported_trace_proved"],
            },
            "transport_conjugation_replay": {
                "status": replay["status"],
                "finite_validator_replay_closed": replay["finite_validator_replay_closed"],
                "selected_source_verified": replay["selected_source_verified"],
                "selected_rho_s_validator_ready": replay[
                    "selected_rho_s_validator_ready"
                ],
            },
            "finite_projector_source_promotion": {
                "status": finite["status"],
                "finite_projector_source_promotion_proved": finite[
                    "finite_projector_source_promotion_proved"
                ],
                "selected_projector_source_verified": finite[
                    "selected_projector_source_verified"
                ],
                "transported_packet_promoted": finite["transported_packet_promoted"],
                "validator_ready_stationary_rho_s": finite[
                    "validator_ready_stationary_rho_s"
                ],
            },
            "dotD_transport_derivative": {
                "status": dotd["status"],
                "transport_derivative_formula_closed": dotd[
                    "transport_derivative_formula_closed"
                ],
                "selected_dotD_source_verified_by_transport_derivative": dotd[
                    "selected_dotD_source_verified_by_transport_derivative"
                ],
            },
        },
        "still_open": {
            "raw_untransported_packet_promoted": finite[
                "raw_untransported_packet_promoted"
            ],
            "dotD_validator_full_replay_closed": dotd[
                "dotD_validator_full_replay_closed"
            ],
            "selected_dotD_source_verified_on_finite_promotion_cert": finite[
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified": dotd["alpha1_driver_verified"],
            "normalization_value_emitted": alpha1["normalization_value_emitted"],
            "selected_transfer_normalization": gram["selected_transfer_normalization"],
            "alpha1_source_strength_route_A_closed": fill["route_A_closed"],
            "transfer_normalization_route_B_closed": fill["route_B_closed"],
        },
        "frontier_update": {
            "old_primary_next": previous["frontier_update"]["current_next_primary"],
            "old_parallel_next": previous["frontier_update"]["current_next_parallel"],
            "projector_promotion_next": finite["next_required_artifact"],
            "dotd_transport_next": dotd["next_required_artifact"],
            "current_next": alpha1["next_required_artifact"],
            "parallel_transfer_next": fill["next_required_artifact"],
            "why": (
                "Selected projector/rho_s promotion and the dotD transport "
                "derivative are no longer the main obstruction.  The remaining "
                "non-circular value is the alpha1 driver strength or equivalent "
                "transfer-normalization packet."
            ),
        },
        "guardrails": {
            "does_not_promote_raw_untransported_packet": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_full_dotD_validator_replay": True,
            "does_not_claim_selected_transfer_normalization": True,
            "does_not_claim_C1_response": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The previously open selected HYM/projector source-promotion "
                "gate is imported as closed at stationary transported-packet "
                "scope, and the selected dotD transport derivative/source "
                "formula is imported as closed."
            ),
            "what_remains": (
                "Emit the selected alpha1 source-strength value or equivalent "
                "sector/transfer normalization, then rerun honest dotD and C1 "
                "response without lifted flags."
            ),
            "next_required_artifacts": [
                alpha1["next_required_artifact"],
                fill["next_required_artifact"],
            ],
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "ProjectorSourcePromotionDotDTransportReduction",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Projector Source Promotion dotD Transport Reduction v1

## Result

Status: `{cert["status"]}`

The selected HYM/projector source-promotion gate has moved from open to closed
at stationary transported-packet scope.  The transported `B_N` packet is
promoted, stationary `rho_s` is validator-ready, and the transport-conjugation
validator replay is closed.

The `dotD_alpha1` transport derivative/source formula is also closed.  What
remains open is the selected `alpha1` driver value: a source-strength
normalization or equivalent sector/transfer-normalization value.  Until that is
emitted, honest full `dotD` replay, C1 response, `A_selected`, and `b_selected`
remain open.

## Checks

```json
{json.dumps(packet["checks"], indent=2, sort_keys=True)}
```

## Closed Now

```json
{json.dumps(packet["closed_now"], indent=2, sort_keys=True)}
```

## Still Open

```json
{json.dumps(packet["still_open"], indent=2, sort_keys=True)}
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
