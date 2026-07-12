"""Build transition-payload or heat-torsion response one-gate attack."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79_ROOT = ROOT.parent / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_transitionpayload_or_heattorsionresponse_onegateattack"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSITION_ATTACK = PACKET_DIR / "selected_transition_payload_attack.packet.json"
PROMOTION_CONTRACT = PACKET_DIR / "transition_payload_promotion_contract.open.json"
HEAT_DEPENDENCY = PACKET_DIR / "heat_torsion_dependency_on_transition_payload.packet.json"
FRONTIER = PACKET_DIR / "one_gate_attack_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TransitionPayload_or_HeatTorsionResponse_OneGateAttack_v1.md"

STATUS = "MTT_SELECTED_TRANSITIONPAYLOAD_OR_HEATTORSIONRESPONSE_ONEGATEATTACK_BUILT_TRANSITION_PAYLOAD_OPEN"
NEXT = "MTT_Selected_TracePayload_or_FullHYMOperatorEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior = load(DATA / "selected_detransition_or_determinanttorsion_twoslotclosingrun" / "post_six_slot_two_gate_frontier.packet.json")
    two_gate_transition = load(
        DATA
        / "selected_detransition_or_determinanttorsion_twoslotclosingrun"
        / "transition_rhoe_or_cech_dolbeault_de_edge_test.packet.json"
    )
    local_de = load(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")
    local_green = load(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json")
    q79_witness = load(Q79_ROOT / "candidate_data" / "q79_typed_monad_cech_or_hym_connection_witness.candidate.json")
    q79_finite = load(Q79_ROOT / "candidate_data" / "q79_selected_finite_connection_solve_execution.candidate.json")
    q79_trace_gap = load(
        Q79_ROOT
        / "candidate_data"
        / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
        / "selected_trace_equality_gap_layer_proof.json"
    )

    selected_attempt = q79_finite["selected_finite_connection_execution_attempt"]
    selected_promotion = selected_attempt["selected_promotion"]
    finite_values = selected_attempt["finite_values_present"]
    cutset = selected_attempt["cutset"]
    trace_contract = q79_finite["selected_trace_or_full_hym_source_contract"]
    witness_payload = q79_witness["minimal_actual_witness_payload"]

    value_shape_complete = all(
        finite_values[key]
        for key in [
            "nonidentity_projective_rhoE",
            "smooth_27_mode_BN",
            "D_E_matrix",
            "Riesz_Green_gap",
            "sector_projectors",
            "dotD_alpha1",
        ]
    )
    local_same_source_formula_ready = (
        local_de["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"]
        and local_green["operator_payload_boundary"]["protected_T3_Riesz_projector_extracted"]
        and local_green["operator_payload_boundary"]["protected_T3_reduced_Green_extracted"]
    )

    route_status = {
        "finite_trace_identification": {
            "available_support": [
                "selected S0 source prefix exists in q79/constants imports",
                "nonidentity projective rho_E candidate is emitted",
                "27-mode D_E/Riesz/Green/dotD value shapes are emitted",
                "q79 selected trace/gap layer is proved at gap scope",
            ],
            "missing": trace_contract["accepted_closing_routes"]["finite_trace_identification"],
            "closed": (
                selected_promotion["rhoE_selected_by_mtt"]
                and selected_promotion["selected_trace_equality"]
                and selected_promotion["selected_gap_error_certificate"]
                and selected_promotion["honest_replay_without_lifted_flags"]
            ),
        },
        "full_HYM_Newton_replay": {
            "available_support": [
                "local diagonal rank-two HYM solve is selected and residual-certified",
                "local End0 D_E formula is extracted",
                "local protected T3 Riesz/Green layer is extracted",
            ],
            "missing": trace_contract["accepted_closing_routes"]["full_HYM_Newton_replay"],
            "closed": (
                local_de["operator_payload_boundary"]["rank2_to_rank3_sector_transfer_values_extracted"]
                and local_de["operator_payload_boundary"]["validator_ready"]
                and local_green["operator_payload_boundary"]["T1_T2_coupled_covariant_Green_extracted"]
                and local_green["operator_payload_boundary"]["rank2_to_rank3_sector_transfer_values_extracted"]
            ),
        },
        "typed_monad_Cech_payload": {
            "available_support": [
                "corpus recovers monad sequence and line-bundle labels",
                "generic constant-map phrase was tested and rejected as a witness",
                "minimal actual typed witness payload is specified",
            ],
            "missing": trace_contract["accepted_closing_routes"]["typed_monad_Cech_payload"],
            "closed": q79_witness["selected_connection_witness_attempt"]["constructs_actual_selected_witness"],
        },
    }
    transition_slot_closes = any(route["closed"] for route in route_status.values())

    transition_attack = {
        "schema": "MTTSelectedTransitionPayloadAttack.v1",
        "slot": "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "status": "TRANSITION_PAYLOAD_ATTACKED_VALUES_PRESENT_SOURCE_TRACE_OPEN",
        "inputs": {
            "two_gate_frontier": rel(DATA / "selected_detransition_or_determinanttorsion_twoslotclosingrun" / "post_six_slot_two_gate_frontier.packet.json"),
            "two_gate_transition_edge": rel(
                DATA
                / "selected_detransition_or_determinanttorsion_twoslotclosingrun"
                / "transition_rhoe_or_cech_dolbeault_de_edge_test.packet.json"
            ),
            "local_diagonal_End0_DE": rel(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"),
            "local_Riesz_Green_dotD": rel(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"),
            "q79_typed_monad_or_HYM_witness": rel(Q79_ROOT / "candidate_data" / "q79_typed_monad_cech_or_hym_connection_witness.candidate.json"),
            "q79_finite_connection_execution": rel(Q79_ROOT / "candidate_data" / "q79_selected_finite_connection_solve_execution.candidate.json"),
            "q79_trace_gap_layer": rel(
                Q79_ROOT
                / "candidate_data"
                / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
                / "selected_trace_equality_gap_layer_proof.json"
            ),
        },
        "support": {
            "prior_has_transition_as_primary_next": prior["recommended_primary_next"]
            == "transition_rhoE_or_Cech_Dolbeault_DE_data",
            "two_gate_transition_slot_open": two_gate_transition["slot_closes"] is False,
            "finite_values_shape_complete": value_shape_complete,
            "local_same_source_formula_ready": local_same_source_formula_ready,
            "q79_gap_layer_proved": q79_trace_gap["gap_layer"]["D_E_honest_replay_passes_after_theorem_derived_source_flags"],
            "q79_gap_layer_scope_only": q79_trace_gap["scope"] == "D_E gap/Riesz/Green layer only",
            "typed_witness_payload_specified": witness_payload["status"] == "OPEN",
        },
        "route_status": route_status,
        "open_cutset": cutset,
        "slot_closes": transition_slot_closes,
        "why_not_closed": (
            "The value shapes are now complete enough for a serious replay target, but no route proves selected "
            "trace equality, selected nonidentity rho_E, selected full operator provenance, or literal typed "
            "Cech/monad transition data. Closing the slot now would relabel diagnostic/model-active values as "
            "selected-source data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_contract = {
        "schema": "MTTTransitionPayloadPromotionContract.v1",
        "status": "OPEN",
        "purpose": "Minimal payload that would close transition_rhoE_or_Cech_Dolbeault_DE_data without lifted flags.",
        "must_emit_one_of": {
            "finite_trace_identification": trace_contract["accepted_closing_routes"]["finite_trace_identification"],
            "full_HYM_Newton_replay": trace_contract["accepted_closing_routes"]["full_HYM_Newton_replay"],
            "typed_monad_Cech_payload": trace_contract["accepted_closing_routes"]["typed_monad_Cech_payload"],
        },
        "must_not_use": trace_contract["must_not_use"],
        "common_validator_outputs": [
            "selected nonidentity rho_E or selected transition/Cech tables",
            "selected sector D_E matrices for Q,u,d,L,e,N,H",
            "selected Riesz/gap and reduced Green on the same finite basis",
            "selected dotD_alpha1 or proof that dotD is outside this slot and already theorem-derived",
            "metric/cocycle compatibility certificate",
            "honest replay without diagnostic selected-flag lifts",
        ],
        "currently_present_but_not_enough": {
            "finite_value_shapes": finite_values,
            "local_D_E_formula": local_de["D_E_direction_payload"],
            "q79_gap_layer": q79_trace_gap["gap_layer"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    heat_dependency = {
        "schema": "MTTHeatTorsionDependencyOnTransitionPayload.v1",
        "slot": "finite_determinant_heat_spectrum_or_torsion_response",
        "status": "HEAT_TORSION_REDUCED_TO_SELECTED_OPERATOR_PAYLOAD_FIRST",
        "dependency": {
            "transition_payload_needed_first": True,
            "reason": (
                "A determinant, heat-kernel table, or torsion response is only proof-usable once the selected "
                "operator and finite basis are fixed. Current determinant/torsion trails are support, but not "
                "the selected HYM/End0 operator response."
            ),
        },
        "minimal_after_transition_payload": [
            "spectrum or heat coefficients of the selected D_E^*D_E/operator block",
            "regularization convention for determinant/torsion",
            "normalization tied to q79/F,m=1 selected source",
            "finite error or truncation bound",
        ],
        "slot_closes": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTOneGateAttackFrontier.v1",
        "status": "PRIMARY_TRANSITION_GATE_ATTACKED_PAYLOAD_OPEN",
        "operator_source_slots_closed": prior["operator_source_slots_closed"],
        "operator_source_slots_remaining": prior["operator_source_slots_remaining"],
        "transition_slot_closes": transition_slot_closes,
        "determinant_torsion_slot_closes": False,
        "remaining_slots": prior["remaining_slots"],
        "best_next_artifact": NEXT,
        "best_next_reason": (
            "All legal transition routes now reduce to selected trace payload or full selected HYM operator "
            "emission. That is narrower than a generic source hunt."
        ),
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTransitionPayloadOrHeatTorsionResponseOneGateAttack",
        "status": STATUS,
        "inputs": transition_attack["inputs"],
        "output_packets": {
            "selected_transition_payload_attack": rel(TRANSITION_ATTACK),
            "transition_payload_promotion_contract": rel(PROMOTION_CONTRACT),
            "heat_torsion_dependency_on_transition_payload": rel(HEAT_DEPENDENCY),
            "one_gate_attack_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "SelectedTransitionPayloadOneGateNormalFormTheorem",
            "proved": True,
            "statement": (
                "The primary remaining transition/D_E slot is reduced to three legal promotion routes: finite "
                "trace identification, full selected HYM/Strominger operator replay, or literal typed monad/Cech "
                "payload. Current artifacts provide value shapes and support for all three, but no route emits "
                "the selected-source payload, so the slot remains open."
            ),
        },
        "what_closes_now": {
            "transition_gate_reduced_to_three_routes": True,
            "finite_value_shapes_imported": value_shape_complete,
            "heat_torsion_deferred_until_operator_payload": True,
            "promotion_contract_emitted": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data": True,
            "finite_determinant_heat_spectrum_or_torsion_response": True,
            "selected_trace_equality": selected_promotion["selected_trace_equality"] is False,
            "rhoE_selected_by_mtt": selected_promotion["rhoE_selected_by_mtt"] is False,
            "selected_full_iwasawa_strominger_operator_formula": cutset["selected_full_iwasawa_strominger_operator_formula"],
            "typed_monad_Cech_payload": not route_status["typed_monad_Cech_payload"]["closed"],
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "operator_source_slots_closed_total": prior["operator_source_slots_closed"],
            "operator_source_slots_remaining": prior["operator_source_slots_remaining"],
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": transition_slot_closes,
            "finite_determinant_heat_spectrum_or_torsion_response_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": transition_slot_closes,
    }

    cert = {
        "certificate": "MTT_Selected_TransitionPayload_or_HeatTorsionResponse_OneGateAttack_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "closed_operator_source_slots_total": prior["operator_source_slots_closed"],
        "operator_source_slots_remaining": prior["operator_source_slots_remaining"],
        "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": transition_slot_closes,
        "finite_determinant_heat_spectrum_or_torsion_response_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected TransitionPayload or HeatTorsionResponse OneGateAttack v1

This artifact attacks the primary remaining gate:
`transition_rhoE_or_Cech_Dolbeault_DE_data`.

The result is not a closure, but the gate is now reduced to three legal routes:

1. finite trace identification
2. full selected HYM/Strominger operator replay
3. literal typed monad/Cech payload

What is present:

- nonidentity projective `rho_E` value shape
- 27-mode `D_E`, Riesz/Green, sector projector, and `dotD` value shapes
- local same-source diagonal End0 formula `D_E=d+ad(du*T3)`
- q79 selected trace/gap layer at gap scope

What is missing:

- selected trace equality
- `rho_E_selected_by_mtt`
- full selected Iwasawa/Strominger operator formula or error bound
- literal typed Cech/monad transition payload
- honest replay without diagnostic lifted selected flags

The determinant / heat / torsion slot is deferred until the selected operator
payload is fixed, because otherwise the spectrum would be attached to a
model-active or off-branch operator rather than the selected HYM/End0 source.

Current count remains six closed operator-source slots and two open slots.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (TRANSITION_ATTACK, transition_attack),
        (PROMOTION_CONTRACT, promotion_contract),
        (HEAT_DEPENDENCY, heat_dependency),
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
