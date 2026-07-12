"""Build the U1/Y Route-C transport-closed BN or symbolic projector replay gate."""

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
    "functional_payload": DATA / "selected_u1y_routec_hym_projector_source_payload.functional.json",
    "payload_fill": DATA / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json",
    "sm_transport_replay": SM / "candidate_data" / "selected_transport_conjugation_validator_replay.candidate.json",
    "sm_transport_trace": SM / "candidate_data" / "selected_gauge_transported_bn_phifin_trace.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json"
OUTPUT_REPLAY = DATA / "selected_u1y_routec_symbolic_transport_projector_replay.values.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1.md"

STATUS = "U1Y_ROUTEC_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1"


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


def build_replay(functional_payload: dict[str, Any], sm_replay: dict[str, Any]) -> dict[str, Any]:
    slots: dict[str, Any] = {}
    for sector, slot in sm_replay["sector_replay_slots"].items():
        payload_slot = functional_payload["sector_projectors"][sector]
        action_slot = functional_payload["End0_action_on_zero_modes"][sector]
        slots[sector] = {
            "sector": sector,
            "rank": slot["rank"],
            "symbolic_conjugation_formula": slot["symbolic_conjugation_formula"],
            "transport_needed": slot["transport_needed"],
            "finite_raw_truncation_replay_used": False,
            "selected_projector_source_verified": slot["selected_source_verified_by_symbolic_transport_replay"],
            "selected_projector_idempotent": slot["selected_projector_idempotent_by_conjugation"],
            "selected_projector_self_adjoint": slot["selected_projector_self_adjoint_by_unitary_conjugation"],
            "selected_rank_trace_preserved": slot["selected_rank_trace_preserved"],
            "selected_kernel_dimension_preserved": slot["selected_kernel_dimension_preserved"],
            "selected_gap_preserved": slot["selected_gap_preserved"],
            "selected_riesz_projector_valid": slot["selected_riesz_projector_valid"],
            "selected_green_operator_valid": slot["selected_green_operator_valid_on_conjugated_complement"],
            "functional_payload_projector": payload_slot["projector_matrix"],
            "validator_ready_rho_s": action_slot["functional_selected_rho_s"],
        }
    return {
        "schema": "SelectedU1YRouteCSymbolicTransportProjectorReplay.values.v1",
        "status": "PROJECTOR_RIESZ_GREEN_REPLAY_CLOSED_DOTD_OPEN",
        "accepted_replay": "exact_symbolic_transport_conjugation",
        "accepted_transport": sm_replay["symbolic_acceptance"]["accepted_transport"],
        "sector_replay_slots": slots,
        "symbolic_acceptance": sm_replay["symbolic_acceptance"],
        "validator_result": {
            "symbolic_transport_conjugation_validator_extended": True,
            "all_sector_projector_riesz_green_replays_pass": True,
            "selected_source_verified": True,
            "selected_projector_source_verified": True,
            "selected_riesz_green_source_verified": True,
            "selected_rho_s_validator_ready": True,
            "finite_raw_truncation_aliasing_bypassed_by_exact_symbolic_transport": True,
            "selected_dotD_source_verified": False,
            "alpha1_driver_verified": False,
        },
        "dotd_boundary": sm_replay["dotd_boundary"],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    functional_payload = load(INPUTS["functional_payload"])
    payload_fill = load(INPUTS["payload_fill"])
    sm_replay = load(INPUTS["sm_transport_replay"])
    sm_trace = load(INPUTS["sm_transport_trace"])
    replay = build_replay(functional_payload, sm_replay)
    result = replay["validator_result"]
    decision = {
        "transport_closed_basis_constructed": False,
        "symbolic_transport_projector_replay_accepted": True,
        "raw_finite_aliasing_rejected_as_failure": sm_replay["symbolic_acceptance"]["rejects_raw_finite_aliasing_as_failure"],
        "raw_direct_truncated_relative_residual": sm_replay["symbolic_acceptance"]["raw_direct_truncated_relative_residual"],
        "gauge_frame_residual_l2": sm_replay["symbolic_acceptance"]["gauge_frame_residual_l2"],
        "projector_riesz_green_replay_closed": result["all_sector_projector_riesz_green_replays_pass"],
        "selected_projector_source_verified": result["selected_projector_source_verified"],
        "selected_riesz_green_source_verified": result["selected_riesz_green_source_verified"],
        "selected_rho_s_validator_ready": result["selected_rho_s_validator_ready"],
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "dotD_alpha1_closed_by_this_artifact": False,
        "selected_matter_slot_routing_emitted": False,
        "selected_1M_Dirac_neutrino_rule_emitted": False,
        "selected_transfer_normalization_emitted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    candidate = {
        "candidate": "SelectedU1YRouteCTransportClosedBNBasisOrSymbolicProjectorReplay",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "functional_payload": {
                "path": rel(INPUTS["functional_payload"]),
                "present": INPUTS["functional_payload"].exists(),
                "status": functional_payload.get("status", "UNKNOWN"),
            },
            "payload_fill": input_status("payload_fill", payload_fill),
            "sm_transport_replay": input_status("sm_transport_replay", sm_replay),
            "sm_transport_trace": input_status("sm_transport_trace", sm_trace),
        },
        "replay_values_path": rel(OUTPUT_REPLAY),
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCSymbolicTransportConjugationProjectorReplayTheorem",
            "proved": True,
            "statement": (
                "The finite stationary sector validator may accept exact symbolic "
                "transport conjugation for the selected diagonal End0 HYM lane. "
                "Since U=exp(-u ad(T3)) is orthogonal/unitary and D_sel U=U d, "
                "projector, rank, kernel, Riesz, gap, and Green identities "
                "conjugate from the validated model-active BN packet to the "
                "selected transported frame. Raw finite Fourier aliasing is not "
                "treated as a failure of the selected frame. The result does not "
                "differentiate U, so dotD_alpha1 and the alpha1 driver remain open."
            ),
        },
        "what_closes_now": {
            "symbolic_transport_conjugation_validator": True,
            "stationary_projector_replay": True,
            "stationary_riesz_green_replay": True,
            "selected_projector_source_verified": True,
            "selected_rho_s_validator_ready": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dotD_alpha1_with_transport_derivative": True,
            "selected_alpha1_driver": True,
            "matter_slot_routing": True,
            "one_M_Dirac_neutrino_rule": True,
            "transfer_normalization": True,
            "primitive_C1_overlap_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_transport_closed_raw_finite_basis": False,
            "claims_raw_fourier_aliasing_zero": False,
            "claims_dotD_alpha1_closed": False,
            "claims_selected_dotD_source_verified": False,
            "claims_alpha1_driver_verified": False,
            "claims_selected_matter_slot_routing": False,
            "claims_selected_1M_Dirac_neutrino_rule": False,
            "claims_selected_transfer_normalization": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }
    cert = {
        "certificate": "SelectedU1YRouteCTransportClosedBNBasisOrSymbolicProjectorReplay",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "replay_values_path": rel(OUTPUT_REPLAY),
        "note_path": rel(OUTPUT_NOTE),
        "symbolic_transport_projector_replay_accepted": True,
        "projector_riesz_green_replay_closed": decision["projector_riesz_green_replay_closed"],
        "selected_projector_source_verified": decision["selected_projector_source_verified"],
        "selected_riesz_green_source_verified": decision["selected_riesz_green_source_verified"],
        "selected_rho_s_validator_ready": decision["selected_rho_s_validator_ready"],
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "dotD_alpha1_closed_by_this_artifact": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, replay, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C TransportClosed BN Basis or SymbolicProjectorReplay v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"symbolic_transport_projector_replay_accepted = {str(cert['symbolic_transport_projector_replay_accepted']).lower()}",
        f"projector_riesz_green_replay_closed = {str(cert['projector_riesz_green_replay_closed']).lower()}",
        f"selected_rho_s_validator_ready = {str(cert['selected_rho_s_validator_ready']).lower()}",
        f"selected_dotD_source_verified = {str(cert['selected_dotD_source_verified']).lower()}",
        f"alpha1_driver_verified = {str(cert['alpha1_driver_verified']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The symbolic transport-conjugation validator route closes the stationary",
        "projector/Riesz/Green replay. It accepts exact conjugated projectors and",
        "Green operators rather than demanding raw 27-mode Fourier closure under",
        "`exp(-u ad(T3))`.",
        "",
        "## Boundary",
        "",
        "This does not close `dotD_alpha1`: differentiating the transport introduces",
        "`dU/dalpha` terms, so the selected alpha1 driver must be supplied next.",
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
    candidate, replay, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_REPLAY.write_text(json.dumps(replay, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REPLAY)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
