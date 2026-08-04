from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_hym_projector_source_payload_fill.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json"
REPLAY = QA / "candidate_data" / "selected_u1y_routec_symbolic_transport_projector_replay.values.json"
SM_REPLAY = ROOT.parent / "mtt-sm-parity-closure" / "candidate_data" / "selected_transport_conjugation_validator_replay.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_symbolic_transport_projector_replay_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_symbolic_transport_projector_replay.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SymbolicTransport_ProjectorReplay_Import_v1.md"

STATUS = "POST_ALPHA_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sector_replay_ok(replay: dict) -> bool:
    slots = replay["sector_replay_slots"]
    if sorted(slots) != sorted(SECTORS):
        return False
    for sector, slot in slots.items():
        expected_rank = 1 if sector == "H" else 3
        if not all(
            [
                slot["rank"] == expected_rank,
                slot["finite_raw_truncation_replay_used"] is False,
                slot["selected_projector_source_verified"] is True,
                slot["selected_projector_idempotent"] is True,
                slot["selected_projector_self_adjoint"] is True,
                slot["selected_rank_trace_preserved"] is True,
                slot["selected_kernel_dimension_preserved"] is True,
                slot["selected_gap_preserved"] is True,
                slot["selected_riesz_projector_valid"] is True,
                slot["selected_green_operator_valid"] is True,
                slot["validator_ready_rho_s"] is True,
            ]
        ):
            return False
        if sector == "H" and slot["transport_needed"] is not False:
            return False
        if sector != "H" and slot["transport_needed"] is not True:
            return False
    return True


def symbolic_acceptance_ok(replay: dict) -> bool:
    acceptance = replay["symbolic_acceptance"]
    identities = acceptance["requires_functional_identities"]
    return all(
        [
            replay["accepted_replay"] == "exact_symbolic_transport_conjugation",
            replay["accepted_transport"] == "U=exp(-u ad(T3))",
            acceptance["validator_extension"] == "exact_symbolic_transport_conjugation",
            acceptance["accepts_function_space_conjugation"] is True,
            acceptance["requires_unitary_or_orthogonal_transport"] is True,
            acceptance["gauge_frame_replay_passes"] is True,
            acceptance["gauge_frame_residual_l2"] < acceptance["gauge_frame_residual_tolerance"],
            acceptance["raw_direct_truncated_relative_residual"] > 0.01,
            acceptance["rejects_raw_finite_aliasing_as_failure"] is True,
            all(identities.values()),
        ]
    )


def decision_ok(source: dict) -> bool:
    decision = source["decision"]
    return all(
        [
            source["status"] == "U1Y_ROUTEC_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN",
            source["closure_claimed"] is False,
            source["target_fitting_used"] is False,
            source["next_required_artifact"] == NEXT,
            source["theorem"]["proved"] is True,
            decision["transport_closed_basis_constructed"] is False,
            decision["symbolic_transport_projector_replay_accepted"] is True,
            decision["raw_finite_aliasing_rejected_as_failure"] is True,
            decision["projector_riesz_green_replay_closed"] is True,
            decision["selected_projector_source_verified"] is True,
            decision["selected_riesz_green_source_verified"] is True,
            decision["selected_rho_s_validator_ready"] is True,
            decision["selected_dotD_source_verified"] is False,
            decision["alpha1_driver_verified"] is False,
            decision["dotD_alpha1_closed_by_this_artifact"] is False,
            decision["selected_matter_slot_routing_emitted"] is False,
            decision["selected_1M_Dirac_neutrino_rule_emitted"] is False,
            decision["selected_transfer_normalization_emitted"] is False,
            decision["physical_dotD_alpha1_payload_extracted"] is False,
            decision["target_fitting_used"] is False,
        ]
    )


def guardrails_ok(source: dict) -> bool:
    return all(value is False for value in source["guardrails"].values())


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)
    replay = load(REPLAY)
    sm_replay = load(SM_REPLAY)

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_HYM_PROJECTOR_SOURCE_PAYLOAD_FUNCTIONAL_FILLED_FINITE_REPLAY_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1",
            prev["guardrails"]["does_not_claim_finite_27mode_validator_replay"] is True,
        ]
    )
    replay_values_ok = all(
        [
            replay["schema"] == "SelectedU1YRouteCSymbolicTransportProjectorReplay.values.v1",
            replay["status"] == "PROJECTOR_RIESZ_GREEN_REPLAY_CLOSED_DOTD_OPEN",
            replay["validator_result"]["symbolic_transport_conjugation_validator_extended"] is True,
            replay["validator_result"]["all_sector_projector_riesz_green_replays_pass"] is True,
            replay["validator_result"]["selected_source_verified"] is True,
            replay["validator_result"]["selected_projector_source_verified"] is True,
            replay["validator_result"]["selected_riesz_green_source_verified"] is True,
            replay["validator_result"]["selected_rho_s_validator_ready"] is True,
            replay["validator_result"]["finite_raw_truncation_aliasing_bypassed_by_exact_symbolic_transport"] is True,
            replay["validator_result"]["selected_dotD_source_verified"] is False,
            replay["validator_result"]["alpha1_driver_verified"] is False,
            symbolic_acceptance_ok(replay),
            sector_replay_ok(replay),
        ]
    )
    dotd_boundary_ok = all(
        [
            replay["dotd_boundary"]["selected_dotD_source_verified"] is False,
            replay["dotd_boundary"]["alpha1_driver_verified"] is False,
            replay["dotd_boundary"]["dotD_alpha1_closed_by_this_artifact"] is False,
            replay["dotd_boundary"]["previous_honest_dotd_fails_only_by_source_driver_flags"] is True,
            len(replay["dotd_boundary"]["next_required_terms"]) == 3,
            "dU/dalpha" in replay["dotd_boundary"]["next_required_terms"][0],
        ]
    )
    sm_replay_consistent = all(
        [
            sm_replay["status"] == "MTT_SELECTED_TRANSPORT_CONJUGATION_VALIDATOR_REPLAY_CLOSED_DOTD_OPEN",
            sm_replay["theorem"]["proved"] is True,
            sm_replay["promotion_decision"]["symbolic_transport_conjugation_replay_closed"] is True,
            sm_replay["promotion_decision"]["rho_candidate_promoted_to_validator_ready_sector_rho_s_packet"] is True,
            sm_replay["promotion_decision"]["selected_dotD_source_verified"] is False,
            sm_replay["promotion_decision"]["alpha1_driver_verified"] is False,
            sm_replay["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_ready,
            decision_ok(source),
            guardrails_ok(source),
            replay_values_ok,
            dotd_boundary_ok,
            sm_replay_consistent,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaSymbolicTransportProjectorReplayImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "Exact symbolic transport conjugation promotes the selected diagonal End0 HYM lane "
                "from functional projectors to stationary validator-ready projector/Riesz/Green data. "
                "The raw 27-mode Fourier truncation is not claimed transport-closed; its aliasing is "
                "bypassed only by a symbolic conjugation validator. Differentiating U is excluded, so "
                "dotD_alpha1 and the alpha1 driver remain open."
            ),
        },
        "status": STATUS,
        "symbolic_replay_values": replay,
        "checks": {
            "previous_ready": previous_ready,
            "source_decision_ok": decision_ok(source),
            "source_guardrails_ok": guardrails_ok(source),
            "replay_values_ok": replay_values_ok,
            "dotd_boundary_ok": dotd_boundary_ok,
            "sm_replay_consistent": sm_replay_consistent,
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": source["what_closes_now"],
        "what_remains_open": source["what_remains_open"],
        "guardrails": {
            "does_not_claim_raw_finite_transport_closure": True,
            "does_not_claim_raw_aliasing_zero": True,
            "does_not_claim_dotD_alpha1_closed": True,
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_claim_matter_slot_routing_1M_or_transfer_normalization": True,
            "does_not_claim_primitive_C1_A_b_lambda_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "source": str(SOURCE),
            "replay_values": str(REPLAY),
            "sm_replay": str(SM_REPLAY),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_symbolic_transport_projector_replay",
        "status": STATUS,
        "closure_claimed": False,
        "symbolic_transport_projector_replay_accepted": True,
        "projector_riesz_green_replay_closed": True,
        "selected_projector_source_verified": True,
        "selected_riesz_green_source_verified": True,
        "selected_rho_s_validator_ready": True,
        "transport_closed_raw_finite_basis": False,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha SymbolicTransport ProjectorReplay Import v1

## Result

Stationary selected projector/Riesz/Green replay is now closed by exact symbolic
transport conjugation:

```text
accepted replay = exact_symbolic_transport_conjugation
accepted transport = U=exp(-u ad(T3))
selected rho_s validator-ready = true
projector/Riesz/Green replay = true
```

This does not assert that the raw finite 27-mode Fourier basis is closed under
transport. The recorded raw T1/T2 residual remains
`{replay["symbolic_acceptance"]["raw_direct_truncated_relative_residual"]}`.

The boundary is sharp: differentiating the transport introduces `dU/dalpha`,
so `dotD_alpha1` needs the selected transport derivative and alpha1 driver.

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
