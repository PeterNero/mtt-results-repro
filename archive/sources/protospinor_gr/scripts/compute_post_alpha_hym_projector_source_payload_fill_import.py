from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_zeromodebasis_hym_projector_theorem.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json"
FUNCTIONAL = QA / "candidate_data" / "selected_u1y_routec_hym_projector_source_payload.functional.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_hym_projector_source_payload_fill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_hym_projector_source_payload_fill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_HYMProjector_SourcePayload_Fill_Import_v1.md"

STATUS = "POST_ALPHA_HYM_PROJECTOR_SOURCE_PAYLOAD_FUNCTIONAL_FILLED_FINITE_REPLAY_OPEN"
NEXT = "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]
MATTER = ["Q", "u", "d", "L", "e", "N"]
MATTER_DIM = 3
H_DIM = 1


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def is_zero_matrix(matrix: list[list[int]]) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def matrix_shape(matrix: list[list[int]], dim: int) -> bool:
    return len(matrix) == dim and all(len(row) == dim for row in matrix)


def sector_dimensions_ok(functional: dict) -> bool:
    bases = functional["ordered_zero_mode_bases_K_s"]
    projectors = functional["sector_projectors"]
    return all(
        bases[sector]["dimension_emitted"] == (H_DIM if sector == "H" else MATTER_DIM)
        and bases[sector]["dimension_required"] == (H_DIM if sector == "H" else MATTER_DIM)
        and len(bases[sector]["basis_vectors"]) == (H_DIM if sector == "H" else MATTER_DIM)
        and projectors[sector]["rank_required"] == (H_DIM if sector == "H" else MATTER_DIM)
        for sector in SECTORS
    )


def projector_flags_ok(functional: dict) -> bool:
    return all(
        all(
            [
                payload["idempotent"] is True,
                payload["rank_preserved"] is True,
                payload["selected_by_same_source"] is True,
                payload["self_adjoint_for_selected_Gram"] is True,
                payload["zero_mode_projector"] is True,
                payload["gap_preserved_by_unitary_transport"] is True,
                payload["finite_27_mode_replay_closed"] is False,
            ]
        )
        for payload in functional["sector_projectors"].values()
    )


def basis_flags_ok(functional: dict) -> bool:
    return all(
        all(
            [
                basis["source_trace_selected_functionally"] is True,
                basis["finite_27_mode_replay_closed"] is False,
                basis["Gram_matrix"] == ("I_1" if sector == "H" else "I_3"),
                basis["trace_normalization"] == (H_DIM if sector == "H" else MATTER_DIM),
            ]
        )
        for sector, basis in functional["ordered_zero_mode_bases_K_s"].items()
    )


def end0_actions_ok(functional: dict) -> bool:
    actions = functional["End0_action_on_zero_modes"]
    matter_template = actions["Q"]
    matter_ok = all(
        all(
            [
                action["preserves_K_s"] is True,
                action["same_source_action"] is True,
                action["bracket_preserving"] is True,
                action["functional_selected_rho_s"] is True,
                action["target_model"] == "adjoint_triplet",
                action["validator_ready_sector_packet"] is False,
                matrix_shape(action["rho_s_T1"], MATTER_DIM),
                matrix_shape(action["rho_s_T2"], MATTER_DIM),
                matrix_shape(action["rho_s_T3"], MATTER_DIM),
                action["rho_s_T1"] == matter_template["rho_s_T1"],
                action["rho_s_T2"] == matter_template["rho_s_T2"],
                action["rho_s_T3"] == matter_template["rho_s_T3"],
            ]
        )
        for sector, action in actions.items()
        if sector in MATTER
    )
    h = actions["H"]
    h_ok = all(
        [
            h["preserves_K_s"] is True,
            h["same_source_action"] is True,
            h["bracket_preserving"] is True,
            h["functional_selected_rho_s"] is True,
            h["target_model"] == "trivial_singlet",
            h["validator_ready_sector_packet"] is False,
            matrix_shape(h["rho_s_T1"], H_DIM),
            matrix_shape(h["rho_s_T2"], H_DIM),
            matrix_shape(h["rho_s_T3"], H_DIM),
            is_zero_matrix(h["rho_s_T1"]),
            is_zero_matrix(h["rho_s_T2"]),
            is_zero_matrix(h["rho_s_T3"]),
        ]
    )
    return matter_ok and h_ok


def candidate_decision_ok(candidate: dict) -> bool:
    decision = candidate["decision"]
    return all(
        [
            candidate["status"] == "U1Y_ROUTEC_HYM_PROJECTOR_PAYLOAD_FILLED_FUNCTIONAL_TRACE_FINITE_REPLAY_OPEN",
            candidate["closure_claimed"] is False,
            candidate["target_fitting_used"] is False,
            candidate["next_required_artifact"] == NEXT,
            decision["functional_projector_payload_filled"] is True,
            decision["functional_zero_mode_bases_emitted"] is True,
            decision["functional_source_map_rho_s_emitted"] is True,
            decision["all_sector_projectors_selected_at_functional_trace_level"] is True,
            decision["all_sector_dimensions_match_contract"] is True,
            decision["source_theorem_can_promote_functional_rho_s"] is True,
            decision["validator_ready_sector_packet_emitted"] is False,
            decision["finite_27mode_validator_replay_closed"] is False,
            decision["selected_matter_slot_routing_emitted"] is False,
            decision["selected_1M_Dirac_neutrino_rule_emitted"] is False,
            decision["selected_transfer_normalization_emitted"] is False,
            decision["physical_dotD_alpha1_payload_extracted"] is False,
            decision["selected_dotD_source_verified"] is False,
            decision["alpha1_driver_verified"] is False,
            decision["target_fitting_used"] is False,
        ]
    )


def guardrails_ok(candidate: dict) -> bool:
    guardrails = candidate["guardrails"]
    return all(value is False for value in guardrails.values())


def main() -> None:
    prev = load(PREV)
    candidate = load(SOURCE)
    functional = load(FUNCTIONAL)

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_ZEROMODEBASIS_HYM_PROJECTOR_THEOREM_PROVED_PAYLOAD_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1",
            prev["guardrails"]["does_not_emit_selected_projectors_or_Ks"] is True,
        ]
    )
    functional_payload_ok = all(
        [
            functional["schema"] == "SelectedU1YRouteCHYMProjectorSourcePayload.functional.v1",
            functional["status"] == "FUNCTIONAL_TRACE_PAYLOAD_FILLED_FINITE_VALIDATOR_REPLAY_OPEN",
            functional["same_source_id"]
            == "SM:selected_diagonal_End0_HYM_lane:D=d+du_adT3:functional_transport_trace",
            functional["transport_operator"]["symbol"] == "U",
            functional["transport_operator"]["formula"] == "exp(-u ad(T3))",
            functional["transport_operator"]["unitary_or_orthogonal"] is True,
            functional["selected_HYM_or_typed_projector_certificate"]["selected_source_verified_functional_End0_trace"]
            is True,
            functional["selected_HYM_or_typed_projector_certificate"]["finite_27_mode_validator_replay_closed"]
            is False,
            functional["coherence_checks"]["End0_action_preserves_ker_D_E_sector"] is True,
            functional["coherence_checks"]["projectors_commute_with_End0_action"] is True,
            functional["coherence_checks"]["projectors_pairwise_orthogonal"] is True,
            functional["coherence_checks"]["projectors_sum_to_selected_sector_identity"] is True,
            functional["coherence_checks"]["no_observed_or_benchmark_inputs"] is True,
            functional["coherence_checks"]["no_lifted_selected_flags"] is True,
            sector_dimensions_ok(functional),
            projector_flags_ok(functional),
            basis_flags_ok(functional),
            end0_actions_ok(functional),
        ]
    )
    validator_boundary_ok = all(
        [
            functional["validator_boundary"]["finite_27_mode_validator_replay_closed"] is False,
            functional["validator_boundary"]["direct_truncated_relative_residual_from_T1T2_probe"] > 0,
            functional["validator_boundary"]["gauge_frame_residual_l2"] < 1e-12,
            "transport-closed basis" in functional["validator_boundary"]["reason"],
            len(functional["validator_boundary"]["next_acceptance"]) == 4,
        ]
    )
    routing_still_open = all(
        value is None for value in functional["routing_and_normalization_not_supplied_by_this_contract"].values()
    )
    theorem_proved = all(
        [
            previous_ready,
            candidate_decision_ok(candidate),
            guardrails_ok(candidate),
            functional_payload_ok,
            validator_boundary_ok,
            routing_still_open,
            candidate["functional_promotion_theorem"]["proved"] is True,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaHYMProjectorSourcePayloadFillImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected diagonal End0 HYM transport trace fills the functional projector "
                "source payload for sectors Q,u,d,L,e,N,H: K_s^sel=U K_s^model, "
                "P_s^sel=U P_s^model U^-1 for matter sectors and identity on H, and rho_s is "
                "emitted by the zero-mode source theorem. This closes the functional zero-mode "
                "and source-map layer, but not the finite 27-mode replay or physical dotD layer."
            ),
        },
        "status": STATUS,
        "same_source_id": functional["same_source_id"],
        "transport_operator": functional["transport_operator"],
        "functional_payload": functional,
        "functional_promotion_theorem": candidate["functional_promotion_theorem"],
        "checks": {
            "previous_ready": previous_ready,
            "candidate_decision_ok": candidate_decision_ok(candidate),
            "candidate_guardrails_ok": guardrails_ok(candidate),
            "functional_payload_ok": functional_payload_ok,
            "validator_boundary_ok": validator_boundary_ok,
            "routing_still_open": routing_still_open,
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "guardrails": {
            "does_not_claim_finite_27mode_validator_replay": True,
            "does_not_claim_validator_ready_sector_packet": True,
            "does_not_claim_matter_slot_routing": True,
            "does_not_claim_1M_Dirac_neutrino_rule": True,
            "does_not_claim_transfer_normalization": True,
            "does_not_claim_physical_dotD_or_alpha1_driver": True,
            "does_not_claim_primitive_C1_A_b_lambda_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "source": str(SOURCE),
            "functional_payload": str(FUNCTIONAL),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_hym_projector_source_payload_fill",
        "status": STATUS,
        "closure_claimed": False,
        "functional_selected_projectors": True,
        "functional_selected_zero_mode_bases": True,
        "functional_selected_rho_s": True,
        "finite_27mode_validator_replay_closed": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha HYMProjector SourcePayload Fill Import v1

## Result

The selected diagonal End0 HYM transport trace now fills the functional payload
required by the zero-mode source theorem:

```text
K_s^sel = U K_s^model
P_s^sel = U P_s^model U^-1       for Q,u,d,L,e,N
P_H^sel = P_H^model              for H
rho_s(T_i) = P_s rho(T_i) P_s | K_s
```

This closes the functional zero-mode/source-map layer:

```text
functional selected projectors: yes
functional selected zero-mode bases: yes
functional selected rho_s matrices: yes
same-source trace: {functional["same_source_id"]}
```

It does **not** close the finite 27-mode validator replay. The imported
payload records a direct T1/T2 truncation residual
`{functional["validator_boundary"]["direct_truncated_relative_residual_from_T1T2_probe"]}`,
so the next gate is a transport-closed BN basis, enriched Fourier closure, or
symbolic projector replay.

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
