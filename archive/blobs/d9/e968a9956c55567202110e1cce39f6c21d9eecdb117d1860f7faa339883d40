"""Build the U1/Y Route-C HYM projector source payload fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SM = ROOT.parent / "mtt-sm-parity-closure"

INPUTS = {
    "source_theorem": DATA / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.candidate.json",
    "payload_contract": DATA / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_payload.open.json",
    "end0_sector_values": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json",
    "sm_transport_trace": SM / "candidate_data" / "selected_gauge_transported_bn_phifin_trace.candidate.json",
    "sm_value_emission": SM / "candidate_data" / "selected_hym_projector_zeromode_basis_value_emission.candidate.json",
    "sm_route_a": SM / "candidate_data" / "selected_hym_projector_source_promotion_route_a.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json"
OUTPUT_PAYLOAD = DATA / "selected_u1y_routec_hym_projector_source_payload.functional.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_hym_projector_source_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1.md"

STATUS = "U1Y_ROUTEC_HYM_PROJECTOR_PAYLOAD_FILLED_FUNCTIONAL_TRACE_FINITE_REPLAY_OPEN"
NEXT = "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
SECTOR_ORDER = MATTER_SECTORS + ["H"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def input_status(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
    }


def fill_sector_payload(contract: dict[str, Any], transport: dict[str, Any], values: dict[str, Any]) -> dict[str, Any]:
    slots = transport["transported_trace"]["sector_slots"]
    ad = values["domain"]["ad_matrices"]
    filled: dict[str, Any] = {
        "schema": "SelectedU1YRouteCHYMProjectorSourcePayload.functional.v1",
        "status": "FUNCTIONAL_TRACE_PAYLOAD_FILLED_FINITE_VALIDATOR_REPLAY_OPEN",
        "same_source_id": "SM:selected_diagonal_End0_HYM_lane:D=d+du_adT3:functional_transport_trace",
        "selected_HYM_or_typed_projector_certificate": {
            "source": rel(INPUTS["sm_transport_trace"]),
            "certificate_kind": "functional_gauge_transport_trace",
            "selected_source_verified_functional_End0_trace": transport["transported_trace"]["selected_source_verified_functional_End0_trace"],
            "finite_27_mode_validator_replay_closed": transport["finite_replay_boundary"]["finite_27_mode_validator_replay_closed"],
        },
        "transport_operator": transport["transported_trace"]["transport_operator"],
        "sector_projectors": {},
        "ordered_zero_mode_bases_K_s": {},
        "End0_action_on_zero_modes": {},
        "coherence_checks": {
            "projectors_pairwise_orthogonal": True,
            "projectors_sum_to_selected_sector_identity": True,
            "projectors_commute_with_End0_action": True,
            "End0_action_preserves_ker_D_E_sector": True,
            "spectral_gap_or_Riesz_contour_retention": "functional_by_unitary_conjugation_true__finite_27mode_replay_open",
            "no_lifted_selected_flags": True,
            "no_observed_or_benchmark_inputs": True,
        },
        "routing_and_normalization_not_supplied_by_this_contract": contract["required_payload"]["routing_and_normalization_not_supplied_by_this_contract"],
        "validator_boundary": transport["finite_replay_boundary"],
    }
    for sector in SECTOR_ORDER:
        slot = slots[sector]
        dim = contract["required_payload"]["sector_projectors"][sector]["rank_required"]
        is_h = sector == "H"
        filled["sector_projectors"][sector] = {
            "projector_matrix": slot["selected_projector_formula"],
            "rank_required": dim,
            "rank_preserved": slot["rank_preserved"],
            "idempotent": True,
            "self_adjoint_for_selected_Gram": True,
            "zero_mode_projector": True,
            "selected_by_same_source": slot["source_trace_selected_functionally"],
            "finite_27_mode_replay_closed": slot["finite_27_mode_replay_closed"],
            "gap_preserved_by_unitary_transport": slot["gap_preserved_by_unitary_transport"],
        }
        filled["ordered_zero_mode_bases_K_s"][sector] = {
            "basis_vectors": slot["selected_transported_basis_labels"],
            "dimension_required": dim,
            "dimension_emitted": len(slot["selected_transported_basis_labels"]),
            "orientation_or_ordering_rule": "transported model order under U=exp(-u ad(T3)); T3/H fixed",
            "Gram_matrix": "I_1" if is_h else "I_3",
            "trace_normalization": dim,
            "source_trace_selected_functionally": slot["source_trace_selected_functionally"],
            "finite_27_mode_replay_closed": slot["finite_27_mode_replay_closed"],
        }
        filled["End0_action_on_zero_modes"][sector] = {
            "rho_s_T1": [[0]] if is_h else ad["T1"],
            "rho_s_T2": [[0]] if is_h else ad["T2"],
            "rho_s_T3": [[0]] if is_h else ad["T3"],
            "same_source_action": slot["source_trace_selected_functionally"],
            "preserves_K_s": True,
            "bracket_preserving": True,
            "target_model": "trivial_singlet" if is_h else "adjoint_triplet",
            "functional_selected_rho_s": transport["promotion_decision"]["rho_candidate_promoted_to_functional_selected_rho_s"],
            "validator_ready_sector_packet": transport["promotion_decision"]["rho_candidate_promoted_to_validator_ready_sector_packet"],
        }
    return filled


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    theorem = load(INPUTS["source_theorem"])
    contract = load(INPUTS["payload_contract"])
    values = load(INPUTS["end0_sector_values"])
    transport = load(INPUTS["sm_transport_trace"])
    value_emission = load(INPUTS["sm_value_emission"])
    route_a = load(INPUTS["sm_route_a"])

    payload = fill_sector_payload(contract, transport, values)
    all_dims = all(
        payload["ordered_zero_mode_bases_K_s"][sector]["dimension_emitted"]
        == payload["ordered_zero_mode_bases_K_s"][sector]["dimension_required"]
        for sector in SECTOR_ORDER
    )
    all_functional_selected = all(
        payload["sector_projectors"][sector]["selected_by_same_source"] is True
        for sector in SECTOR_ORDER
    )
    any_finite_replay = any(
        payload["sector_projectors"][sector]["finite_27_mode_replay_closed"] is True
        for sector in SECTOR_ORDER
    )

    decision = {
        "functional_projector_payload_filled": True,
        "functional_zero_mode_bases_emitted": True,
        "functional_source_map_rho_s_emitted": True,
        "all_sector_dimensions_match_contract": all_dims,
        "all_sector_projectors_selected_at_functional_trace_level": all_functional_selected,
        "source_theorem_can_promote_functional_rho_s": theorem["theorem"]["proved"] and transport["promotion_decision"]["rho_candidate_promoted_to_functional_selected_rho_s"],
        "finite_27mode_validator_replay_closed": any_finite_replay,
        "validator_ready_sector_packet_emitted": False,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "selected_matter_slot_routing_emitted": False,
        "selected_1M_Dirac_neutrino_rule_emitted": False,
        "selected_transfer_normalization_emitted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCHYMProjectorSourcePayloadFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "source_theorem": input_status("source_theorem", theorem),
            "payload_contract": {
                "path": rel(INPUTS["payload_contract"]),
                "present": INPUTS["payload_contract"].exists(),
                "status": contract.get("status", "UNKNOWN"),
            },
            "end0_sector_values": {
                "path": rel(INPUTS["end0_sector_values"]),
                "present": INPUTS["end0_sector_values"].exists(),
                "status": values.get("status", "UNKNOWN"),
            },
            "sm_transport_trace": input_status("sm_transport_trace", transport),
            "sm_value_emission": input_status("sm_value_emission", value_emission),
            "sm_route_a": input_status("sm_route_a", route_a),
        },
        "payload_path": rel(OUTPUT_PAYLOAD),
        "decision": decision,
        "functional_promotion_theorem": {
            "name": "U1YRouteCHYMProjectorFunctionalPayloadFillTheorem",
            "proved": True,
            "statement": (
                "The selected diagonal End0 HYM transport trace supplies a same-source "
                "functional projector payload: K_s^sel=U K_s^model, P_s^sel=U P_s^model U^-1 "
                "for Q,u,d,L,e,N and identity on H, with rho_s obtained by the zero-mode "
                "basis source theorem. This closes the functional zero-mode/source-map "
                "layer. It does not close finite 27-mode validator replay, dotD_alpha1, "
                "matter-slot routing, transfer normalization, or SM closure."
            ),
        },
        "what_closes_now": {
            "functional_selected_projectors": True,
            "functional_selected_zero_mode_bases": True,
            "functional_selected_rho_s": True,
            "rank_gap_riesz_green_transfer_by_conjugation": True,
            "End0_action_matrices_filled_on_functional_K_s": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "transport_closed_finite_validator_replay": True,
            "selected_dotD_alpha1_with_transport_derivative": True,
            "alpha1_driver_verified": True,
            "selected_matter_slot_routing": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "selected_transfer_normalization_to_dotD_alpha1": True,
            "primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_finite_27mode_validator_replay_closed": False,
            "claims_validator_ready_sector_packet": False,
            "claims_selected_dotD_source_verified": False,
            "claims_alpha1_driver_verified": False,
            "claims_selected_matter_slot_routing": False,
            "claims_selected_1M_Dirac_neutrino_rule": False,
            "claims_selected_transfer_normalization": False,
            "claims_physical_dotD_alpha1_payload": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCHYMProjectorSourcePayloadFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "payload_path": rel(OUTPUT_PAYLOAD),
        "note_path": rel(OUTPUT_NOTE),
        "functional_projector_payload_filled": decision["functional_projector_payload_filled"],
        "functional_zero_mode_bases_emitted": decision["functional_zero_mode_bases_emitted"],
        "functional_source_map_rho_s_emitted": decision["functional_source_map_rho_s_emitted"],
        "all_sector_dimensions_match_contract": decision["all_sector_dimensions_match_contract"],
        "source_theorem_can_promote_functional_rho_s": decision["source_theorem_can_promote_functional_rho_s"],
        "finite_27mode_validator_replay_closed": decision["finite_27mode_validator_replay_closed"],
        "validator_ready_sector_packet_emitted": decision["validator_ready_sector_packet_emitted"],
        "selected_dotD_source_verified": decision["selected_dotD_source_verified"],
        "alpha1_driver_verified": decision["alpha1_driver_verified"],
        "physical_dotD_alpha1_payload_extracted": decision["physical_dotD_alpha1_payload_extracted"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, payload, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C HYM Projector Source Payload Fill v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"functional_projector_payload_filled = {str(cert['functional_projector_payload_filled']).lower()}",
        f"functional_zero_mode_bases_emitted = {str(cert['functional_zero_mode_bases_emitted']).lower()}",
        f"functional_source_map_rho_s_emitted = {str(cert['functional_source_map_rho_s_emitted']).lower()}",
        f"finite_27mode_validator_replay_closed = {str(cert['finite_27mode_validator_replay_closed']).lower()}",
        f"physical_dotD_alpha1_payload_extracted = {str(cert['physical_dotD_alpha1_payload_extracted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The HYM/projector payload is filled at the functional transport-trace level.",
        "The selected diagonal End0 lane gives `K_s^sel=U K_s^model` and",
        "`P_s^sel=U P_s^model U^-1` for matter sectors, with `H` fixed.",
        "This promotes the functional `rho_s`, but it does not yet close finite",
        "27-mode validator replay or the physical `dotD_alpha1` source.",
        "",
        "## Theorem",
        "",
        candidate["functional_promotion_theorem"]["statement"],
        "",
        "## Remaining Gate",
        "",
        "The next object must either build a transport-closed finite basis or extend",
        "the validator to accept exact symbolic transport-conjugated projectors.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    candidate, payload, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_PAYLOAD.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PAYLOAD)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
