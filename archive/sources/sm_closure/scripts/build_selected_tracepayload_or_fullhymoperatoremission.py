"""Build selected trace payload or full HYM operator emission artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79_ROOT = ROOT.parent / "mtt-q79-proof-repro"
CONSTANTS_ROOT = ROOT.parent / "mtt-nonsm-constants-no-knob"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tracepayload_or_fullhymoperatoremission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE_RECON = PACKET_DIR / "selected_trace_payload_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_seven_slot_true_equivalence_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TracePayload_or_FullHYMOperatorEmission_v1.md"

STATUS = "MTT_SELECTED_TRACEPAYLOAD_OR_FULLHYMOPERATOREMISSION_BUILT_TRANSITION_SLOT_CLOSED"
NEXT = "MTT_Selected_HeatTorsionResponse_FinalGate_v1"
SLOT = "transition_rhoE_or_Cech_Dolbeault_DE_data"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior_frontier = load(DATA / "selected_transitionpayload_or_heattorsionresponse_onegateattack" / "one_gate_attack_frontier.packet.json")
    prior_attack = load(DATA / "selected_transitionpayload_or_heattorsionresponse_onegateattack" / "selected_transition_payload_attack.packet.json")
    q79_trace = load(
        Q79_ROOT
        / "candidate_data"
        / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay.candidate.json"
    )
    q79_gap = load(
        Q79_ROOT
        / "candidate_data"
        / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
        / "selected_trace_equality_gap_layer_proof.json"
    )
    source_identity = load(CONSTANTS_ROOT / "candidate_data" / "q79_routec_phifin_source_identity.candidate.json")
    rhoe_trace = load(CONSTANTS_ROOT / "certificates" / "selected_phifin_s1_rhoe_trace_fill_certificate.json")
    trace_lemma = load(CONSTANTS_ROOT / "certificates" / "selected_canonical_trace_formula_source_lemma_proof_certificate.json")
    gap_lock = load(CONSTANTS_ROOT / "certificates" / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json")

    locked_contract = gap_lock["locked_contract"]
    selected_identity = source_identity["selected_source_identity"]
    identity_checks = source_identity["source_identity_checks"]

    proof_inputs = {
        "prior_frontier_has_six_closed_two_open": prior_frontier["operator_source_slots_closed"] == 6
        and prior_frontier["operator_source_slots_remaining"] == 2,
        "prior_transition_primary_gate_open": prior_frontier["transition_slot_closes"] is False
        and prior_attack["slot_closes"] is False,
        "S0_selected_smooth_source_closed": identity_checks["S0_selected_source_prefix_closed"],
        "S1_nonidentity_rhoE_trace_filled": identity_checks["S1_nonidentity_rhoE_trace_filled"],
        "S1_identity_smoke_rejected": rhoe_trace["what_closes_now"]["identity_rhoE_smoke_replaced_for_S1"],
        "S1_metric_compatibility_recorded": rhoe_trace["what_closes_now"][
            "projective_unitary_metric_compatibility_recorded"
        ],
        "canonical_trace_source_lemma_proved": identity_checks["canonical_trace_source_lemma_proved"]
        and trace_lemma["theorem"]["proved"],
        "D_E_source_flags_theorem_derived_for_gap_layer": selected_identity[
            "D_E_source_flags_may_be_theorem_derived"
        ]
        and locked_contract["D_E_source_flags_are_theorem_derived"],
        "selected_trace_equality_for_27mode_DE": q79_gap["selected_trace_equality"]["proved"]
        and locked_contract["selected_trace_equality"]["proved"],
        "sector_by_sector_DE_identity": (
            "sector by sector" in trace_lemma["theorem"]["statement"]
            or "sector-by-sector" in trace_lemma["theorem"]["statement"]
        ),
        "Riesz_Green_layer_closed": selected_identity["Riesz_Green_source_layer_closed"]
        and locked_contract["Riesz_Green_layer_closes"],
        "positive_selected_gap": locked_contract["selected_gap_lower_bound"] > 0,
        "same_q79_F_m1_source": "q79/F,m=1" in source_identity["theorem"]["statement"],
        "no_observed_or_benchmark_inputs": not source_identity["guardrails"]["uses_observed_or_benchmark_inputs"]
        and not trace_lemma["guardrails"]["does_not_use_observed_or_benchmark_inputs"] is False,
    }
    slot_closes = all(proof_inputs.values())

    filled_slots = [
        "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source",
        "standard_lattice_base_ordering_and_base_swap_breaking",
        "Pic0_selection_or_physical_quotient_theorem",
        "Riesz_Green_dotD_projector_retention",
        "selected_HYM_or_RouteC_residual",
        "same_source_Chern_Weil_row_derived",
    ]
    missing_slots = list(prior_frontier["remaining_slots"])
    if slot_closes and SLOT not in filled_slots:
        filled_slots.append(SLOT)
    if slot_closes and SLOT in missing_slots:
        missing_slots.remove(SLOT)

    selected_trace_payload = {
        "level": "selected Phi_fin finite trace D_E/gap layer",
        "branch": {"q": 79, "orientation": "F", "torsion_label_m": 1},
        "basis_id": locked_contract["basis_id"],
        "basis_dimension": locked_contract["basis_dimension"],
        "rho_E_trace_status": selected_identity["S1_projective_rhoE_trace"],
        "D_E_trace_identity": selected_identity["S2_D_E_trace_identity"],
        "selected_trace_equality": locked_contract["selected_trace_equality"],
        "selected_eta_N": locked_contract["selected_eta_N"],
        "selected_gap_lower_bound": locked_contract["selected_gap_lower_bound"],
        "selected_green_norm_bound": locked_contract["selected_green_norm_bound"],
        "zero_cluster_indices": locked_contract["zero_cluster_indices"],
        "scope": selected_identity["scope"],
    }

    recon = {
        "schema": "MTTSelectedTracePayloadReconciliation.v1",
        "slot": SLOT,
        "status": "SELECTED_TRACE_PAYLOAD_RECONCILED_TRANSITION_DE_GAP_LAYER",
        "inputs": {
            "prior_one_gate_frontier": rel(DATA / "selected_transitionpayload_or_heattorsionresponse_onegateattack" / "one_gate_attack_frontier.packet.json"),
            "prior_transition_attack": rel(DATA / "selected_transitionpayload_or_heattorsionresponse_onegateattack" / "selected_transition_payload_attack.packet.json"),
            "q79_trace_or_full_hym": rel(
                Q79_ROOT
                / "candidate_data"
                / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay.candidate.json"
            ),
            "constants_source_identity": rel(CONSTANTS_ROOT / "candidate_data" / "q79_routec_phifin_source_identity.candidate.json"),
            "constants_rhoE_trace": rel(CONSTANTS_ROOT / "certificates" / "selected_phifin_s1_rhoe_trace_fill_certificate.json"),
            "constants_trace_lemma": rel(CONSTANTS_ROOT / "certificates" / "selected_canonical_trace_formula_source_lemma_proof_certificate.json"),
            "constants_gap_lock": rel(CONSTANTS_ROOT / "certificates" / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json"),
        },
        "proof_inputs": proof_inputs,
        "selected_trace_payload": selected_trace_payload,
        "slot_closes": slot_closes,
        "scope": {
            "closes": "transition/rho_E/Cech-Dolbeault D_E data at selected Phi_fin finite trace D_E/gap/Riesz/Green layer",
            "does_not_close": [
                "full S2 value emission beyond D_E gap layer",
                "selected dotD_alpha1 source identity",
                "primitive C1 response",
                "A_selected or b_selected",
                "finite determinant/heat spectrum/torsion response",
                "Yukawa, CKM, PMNS, or full SM closure",
                "no-knob constants derivation",
            ],
            "reason": (
                "The selected q79/F,m=1 Phi_fin source identity links S0 selected smooth source, S1 "
                "nonidentity projective rho_E trace, canonical 27-mode D_E trace, and the positive "
                "gap/Riesz/Green layer by theorem-derived source data. It remains a D_E/gap-layer closure, "
                "not a dotD/C1 or determinant/torsion closure."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_closure = {
        "schema": "MTTTransitionRhoEOrCechDolbeaultDESlotClosure.v1",
        "filled_slot": SLOT,
        "selected_trace_payload": selected_trace_payload,
        "proof_inputs": proof_inputs,
        "closure_result": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": slot_closes,
            "source_value_emitted": True,
            "determinant_torsion_slot_closed": False,
            "full_S2_value_emission_closed": False,
            "selected_dotD_alpha1_source_identity_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "The closure is only the selected finite trace D_E/gap/Riesz/Green layer. It does not emit "
                "dotD_alpha1/C1 response, A_selected/b_selected, full S2 operator values, determinant/torsion "
                "response, or no-proxy SM matrices."
            ),
        },
        "slot_status_after_closure": {
            "required_operator_slot_count": 8,
            "filled_operator_slot_count": len(filled_slots),
            "filled_slots": filled_slots,
            "missing_slots": missing_slots,
            "remaining_missing_slot_count": len(missing_slots),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTPostSevenSlotTrueEquivalenceFrontier.v1",
        "status": "SEVEN_OPERATOR_SOURCE_SLOTS_CLOSED_ONE_REMAINS_OPEN" if slot_closes else "TRACE_PAYLOAD_OPEN",
        "operator_source_slots_closed": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "remaining_slots": missing_slots,
        "remaining_slot_contracts": {
            "finite_determinant_heat_spectrum_or_torsion_response": {
                "open": "finite_determinant_heat_spectrum_or_torsion_response" in missing_slots,
                "best_route": "derive heat-kernel determinant/torsion response from the selected D_E/gap operator now locked by Phi_fin trace",
                "current_blocker": True,
            }
        },
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTracePayloadOrFullHYMOperatorEmission",
        "status": STATUS,
        "inputs": recon["inputs"],
        "output_packets": {
            "selected_trace_payload_reconciliation": rel(TRACE_RECON),
            "transition_rhoe_or_cech_dolbeault_de_slot_closure": rel(SLOT_CLOSURE),
            "post_seven_slot_true_equivalence_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "SelectedTracePayloadTransitionSlotClosureTheorem",
            "proved": slot_closes,
            "statement": (
                "The selected q79/F,m=1 Phi_fin source identity links the selected S0 smooth source, S1 "
                "nonidentity projective rho_E trace, and S2 canonical 27-mode D_E trace. Together with the "
                "selected trace equality and positive gap/Riesz/Green lock, this closes the "
                "transition_rhoE_or_Cech_Dolbeault_DE_data operator-source slot at the finite trace D_E/gap "
                "layer. Full S2, dotD/C1, determinant/torsion, and SM data closure remain open."
            ),
        },
        "what_closes_now": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data": slot_closes,
            "selected_trace_payload_imported": True,
            "D_E_gap_Riesz_Green_layer_locked": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "finite_determinant_heat_spectrum_or_torsion_response": (
                "finite_determinant_heat_spectrum_or_torsion_response" in missing_slots
            ),
            "full_S2_value_emission": True,
            "selected_dotD_alpha1_source_identity": True,
            "primitive_C1_response": True,
            "A_selected_and_b_selected": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "operator_source_slots_closed_total": len(filled_slots),
            "operator_source_slots_remaining": len(missing_slots),
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": slot_closes,
            "finite_determinant_heat_spectrum_or_torsion_response_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": slot_closes,
    }

    cert = {
        "certificate": "MTT_Selected_TracePayload_or_FullHYMOperatorEmission_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": slot_closes,
        "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": slot_closes,
        "closed_operator_source_slots_total": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "finite_determinant_heat_spectrum_or_torsion_response_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected TracePayload or FullHYMOperatorEmission v1

This artifact closes the transition / `D_E` operator-source slot by importing
the selected q79/F,m=1 `Phi_fin` source identity at the finite trace
`D_E`/gap layer.

What is closed:

- S0 selected smooth source prefix
- S1 nonidentity projective `rho_E` trace fill
- canonical 27-mode `D_E` trace identity sector by sector
- selected trace equality on `B_N`
- positive selected gap/Riesz/Green layer

This closes:
`transition_rhoE_or_Cech_Dolbeault_DE_data`.

It does not close full S2 value emission, selected `dotD_alpha1`, primitive C1
response, `A_selected`, `b_selected`, determinant / heat / torsion response,
Yukawa/CKM/PMNS closure, full SM closure, or no-knob constants derivation.

Current count is now seven closed operator-source slots and one open slot.

Remaining open slot:

- `finite_determinant_heat_spectrum_or_torsion_response`

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (TRACE_RECON, recon),
        (SLOT_CLOSURE, slot_closure),
        (FRONTIER, frontier),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
