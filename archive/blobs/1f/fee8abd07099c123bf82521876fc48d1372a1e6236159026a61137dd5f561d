"""Import Route-C transport source-promotion repair."""

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

PREVIOUS = CERTS / "routec_galerkin_execution_cutset_and_primitive_search_certificate.json"
ROUTE_A = SM / "certificates" / "selected_hym_projector_source_promotion_route_a_certificate.json"
MODEL_EQ = SM / "candidate_data" / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
GAUGE_TRACE = SM / "certificates" / "selected_gauge_transported_bn_phifin_trace_certificate.json"
GAUGE_TRACE_PACKET = SM / "candidate_data" / "selected_gauge_transported_bn_phifin_trace.candidate.json"
TRANSPORT_REPLAY = SM / "certificates" / "selected_transport_conjugation_validator_replay_certificate.json"
TRANSPORT_REPLAY_PACKET = SM / "candidate_data" / "selected_transport_conjugation_validator_replay.candidate.json"
DOTD_TRANSPORT = SM / "certificates" / "selected_dotd_alpha1_transport_derivative_probe_certificate.json"
DOTD_TRANSPORT_PACKET = SM / "candidate_data" / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
ALPHA_NORM = SM / "certificates" / "selected_alpha1_source_strength_normalization_theorem_certificate.json"
ALPHA_VALUE = SM / "certificates" / "selected_alpha1_source_strength_value_emission_attempt_certificate.json"

OUTPUT_PACKET = DATA / "routec_transport_source_promotion_repair.candidate.json"
OUTPUT_CERT = CERTS / "routec_transport_source_promotion_repair_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_Transport_Source_Promotion_Repair_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    route_a = load(ROUTE_A)
    model_eq = load(MODEL_EQ)
    gauge = load(GAUGE_TRACE)
    gauge_packet = load(GAUGE_TRACE_PACKET)
    replay = load(TRANSPORT_REPLAY)
    replay_packet = load(TRANSPORT_REPLAY_PACKET)
    dotd = load(DOTD_TRANSPORT)
    dotd_packet = load(DOTD_TRANSPORT_PACKET)
    alpha_norm = load(ALPHA_NORM)
    alpha_value = load(ALPHA_VALUE)

    checks = {
        "D0_previous_frontier_is_primitive_source_or_basis_emission": previous[
            "frontier_update"
        ]["current_next"]
        == "MTT_Selected_RouteC_Primitive_SourcePromotion_or_BNBasis_Emission_v1",
        "D1_route_A_reduces_source_promotion_to_phifin_trace": route_a[
            "status"
        ]
        == "MTT_SELECTED_HYM_PROJECTOR_SOURCE_PROMOTION_ROUTE_A_REDUCED_TO_PHIFIN_TRACE"
        and route_a["finite_value_side_closed"]
        and route_a["route_A_promotes_now"] is False
        and route_a["source_promotion_closed"] is False
        and route_a["next_required_artifact"]
        == "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1",
        "D2_untransported_model_active_equivalence_rejected": model_eq[
            "status"
        ]
        == "MTT_PHIFIN_BN_MODEL_ACTIVE_EQUIVALENCE_REJECTED_GAUGE_TRANSPORT_TRACE_REQUIRED"
        and model_eq["no_go_theorem"]["proved"]
        and model_eq["promotion_decision"]["exact_model_active_equivalence_rejected"]
        and not model_eq["promotion_decision"]["selected_source_flags_may_be_flipped_now"]
        and model_eq["next_required_artifact"]
        == "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1",
        "D3_gauge_transported_functional_trace_proved_replay_open": gauge[
            "status"
        ]
        == "MTT_SELECTED_GAUGE_TRANSPORTED_BN_PHIFIN_TRACE_PROVED_FINITE_REPLAY_OPEN"
        and gauge["gauge_transported_trace_proved"]
        and gauge["functional_rho_s_promoted"]
        and gauge["finite_validator_replay_closed"] is False
        and gauge["alpha1_driver_verified"] is False
        and gauge_packet["promotion_decision"][
            "selected_source_verified_for_functional_End0_trace"
        ]
        and gauge_packet["finite_replay_boundary"]["finite_27_mode_validator_replay_closed"]
        is False
        and gauge["next_required_artifact"]
        == "MTT_Selected_TransportClosed_BN_Basis_or_ValidatorReplay_v1",
        "D4_symbolic_transport_validator_replay_closes_stationary_source": replay[
            "status"
        ]
        == "MTT_SELECTED_TRANSPORT_CONJUGATION_VALIDATOR_REPLAY_CLOSED_DOTD_OPEN"
        and replay["finite_validator_replay_closed"]
        and replay["selected_source_verified"]
        and replay["selected_rho_s_validator_ready"]
        and replay["selected_dotD_source_verified"] is False
        and replay["alpha1_driver_verified"] is False
        and replay_packet["validator_result"][
            "all_sector_projector_riesz_green_replays_pass"
        ]
        and replay["next_required_artifact"]
        == "MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1",
        "D5_dotd_transport_formula_closes_algebra_driver_open": dotd[
            "status"
        ]
        == "MTT_SELECTED_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_NORMALIZATION_OPEN"
        and dotd["transport_derivative_formula_closed"]
        and dotd["selected_dotD_source_formula_closed"]
        and dotd["selected_dotD_source_verified_by_transport_derivative"]
        and dotd["dotD_validator_full_replay_closed"] is False
        and dotd["alpha1_driver_verified"] is False
        and dotd_packet["validator_boundary"][
            "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
        ]
        and dotd_packet["validator_boundary"]["source_only_fails_only_by_alpha1_driver"]
        and dotd["next_required_artifact"]
        == "MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1",
        "D6_alpha1_normalization_reduces_to_value_or_same_source_packet": alpha_norm[
            "status"
        ]
        == "MTT_SELECTED_ALPHA1_SOURCE_STRENGTH_NORMALIZATION_THEOREM_BUILT_VALUE_OPEN"
        and alpha_norm["alpha1_driver_acceptance_theorem_built"]
        and alpha_norm["conditional_dotd_closure_theorem_built"]
        and alpha_norm["normalization_value_emitted"] is False
        and alpha_norm["alpha1_driver_verified"] is False
        and alpha_norm["next_required_artifact"]
        == "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
        "D7_unit_alpha_candidate_isolated_but_unselected": alpha_value[
            "status"
        ]
        == "MTT_SELECTED_ALPHA1_SOURCE_STRENGTH_VALUE_EMISSION_ATTEMPT_BUILT_VALUE_OPEN"
        and alpha_value["candidate_unit_source_strength_isolated"]
        and alpha_value["conditional_value_candidate"]["lambda_alpha1_candidate"] == 1.0
        and alpha_value["selected_value_emitted"] is False
        and alpha_value["alpha1_driver_verified"] is False,
    }

    return {
        "packet": "RouteC_Transport_Source_Promotion_Repair_v1",
        "status": "ROUTEC_TRANSPORT_SOURCE_PROMOTION_REPAIR_STATIONARY_REPLAY_CLOSED_ALPHA1_DRIVER_OPEN",
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "route_A": str(ROUTE_A),
            "model_active_equivalence": str(MODEL_EQ),
            "gauge_transported_trace": str(GAUGE_TRACE),
            "transport_replay": str(TRANSPORT_REPLAY),
            "dotd_transport": str(DOTD_TRANSPORT),
            "alpha_normalization": str(ALPHA_NORM),
            "alpha_value_attempt": str(ALPHA_VALUE),
        },
        "theorem": {
            "name": "RouteCTransportSourcePromotionRepairTheorem",
            "proved": all(checks.values()),
            "statement": (
                "The primitive source-promotion blocker has a legal transport "
                "repair.  Raw model-active B_N equality is false, but the "
                "gauge-transported Phi_fin trace and symbolic transport "
                "validator replay promote the stationary selected source, "
                "projector, Riesz, and Green identities.  The dynamic dotD "
                "formula is also fixed by transport differentiation, leaving "
                "only the same-branch alpha1 source-strength normalization "
                "needed for honest dotD replay and C1 closure."
            ),
        },
        "checks": checks,
        "closed_stationary_replay": {
            "functional_rho_s_promoted": gauge["functional_rho_s_promoted"],
            "gauge_transported_trace_proved": gauge["gauge_transported_trace_proved"],
            "symbolic_transport_conjugation_validator_extended": replay[
                "symbolic_transport_conjugation_validator_extended"
            ],
            "finite_validator_replay_closed": replay["finite_validator_replay_closed"],
            "selected_source_verified": replay["selected_source_verified"],
            "selected_rho_s_validator_ready": replay["selected_rho_s_validator_ready"],
        },
        "open_dynamic_replay": {
            "selected_dotD_source_formula_closed": dotd[
                "selected_dotD_source_formula_closed"
            ],
            "selected_dotD_source_verified_by_transport_derivative": dotd[
                "selected_dotD_source_verified_by_transport_derivative"
            ],
            "dotD_validator_full_replay_closed": dotd["dotD_validator_full_replay_closed"],
            "alpha1_driver_verified": dotd["alpha1_driver_verified"],
            "unit_lambda_candidate": alpha_value["conditional_value_candidate"][
                "lambda_alpha1_candidate"
            ],
            "unit_candidate_selected": alpha_value["selected_value_emitted"],
        },
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "stationary_replay_next": replay["next_required_artifact"],
            "current_next": "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
            "why": (
                "Transport-conjugation legally promotes the stationary "
                "projector/Riesz/Green/source packet.  The only remaining "
                "source-promotion obstruction for dotD is the selected alpha1 "
                "driver/source-strength normalization."
            ),
        },
        "guardrails": {
            "does_not_promote_raw_untransported_BN_equality": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_honest_dotD_full_replay": True,
            "does_not_claim_nonzero_C1_response": True,
            "does_not_claim_full_SM_or_no_knob_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "Stationary Route-C source promotion is repaired by exact "
                "symbolic transport-conjugation."
            ),
            "what_remains": (
                "Select the alpha1 source-strength value/same-source packet so "
                "the already-derived transport dotD formula can replay honestly."
            ),
            "next_required_artifact": "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCTransportSourcePromotionRepair",
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
    return f"""# RouteC Transport Source Promotion Repair v1

## Result

Status: `{cert["status"]}`

Raw untransported `B_N` equality is rejected.  The legal repair is the
gauge-transported `Phi_fin` trace plus exact symbolic transport-conjugation.
That closes the stationary selected source/projector/Riesz/Green replay, while
`dotD_alpha1` remains dynamic and still requires the selected alpha1
source-strength normalization.

## Checks

```json
{json.dumps(packet["checks"], indent=2, sort_keys=True)}
```

## Closed Stationary Replay

```json
{json.dumps(packet["closed_stationary_replay"], indent=2, sort_keys=True)}
```

## Open Dynamic Replay

```json
{json.dumps(packet["open_dynamic_replay"], indent=2, sort_keys=True)}
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
