"""Build the U1/Y Route-C dotD alpha1 transport derivative and driver gate."""

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
    "symbolic_replay": DATA / "selected_u1y_routec_symbolic_transport_projector_replay.values.json",
    "transport_replay_gate": DATA / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json",
    "hym_projector_payload": DATA / "selected_u1y_routec_hym_projector_source_payload.functional.json",
    "sm_dotd_transport_probe": SM / "candidate_data" / "selected_dotd_alpha1_transport_derivative_probe.candidate.json",
    "sm_alpha1_source_strength_theorem": SM / "candidate_data" / "selected_alpha1_source_strength_normalization_theorem.candidate.json",
    "sm_source_origin_alpha1_driver": SM / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_u1y_routec_alpha1_source_strength_value_contract.open.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1.md"

STATUS = "U1Y_ROUTEC_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_VALUE_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1"


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


def build_contract(sm_norm: dict[str, Any], sm_origin: dict[str, Any]) -> dict[str, Any]:
    criterion = sm_norm["acceptance_criterion"]
    unified = sm_origin["unified_payload_contract"]
    return {
        "schema": "SelectedU1YRouteCAlpha1SourceStrengthValueContract.open.v1",
        "status": "OPEN_SOURCE_STRENGTH_VALUE_REQUIRED",
        "name": "Selected_U1Y_RouteC_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
        "purpose": "derive alpha1_driver_verified without lifted flags",
        "required_value": {
            "same_source_id": None,
            "selected_source_strength_coordinate_alpha1": None,
            "du_dalpha1_equals_h_ext": None,
            "h_ext_zero_mean_HYM_row_gauge": None,
            "source_strength_normalization_value": None,
            "normalization_fixed_by": "selected Phi_fin/Strominger/HYM source, not measured data",
            "selected_transfer_normalization_to_existing_dotD_matrices": None,
            "honest_dotD_validator_replay": None,
        },
        "must_emit": criterion["must_emit"],
        "forbidden_shortcuts": criterion["forbidden_shortcuts"],
        "unified_same_source_payload": {
            "domain": unified["domain"],
            "codomain": unified["codomain"],
            "must_commute_with": unified["must_commute_with"],
            "must_emit": unified["must_emit"],
            "acceptance": unified["acceptance"],
        },
        "validator_flags_that_become_true_only_after_value": [
            "selected_dotD_source_verified",
            "alpha1_driver_verified",
            "selected_transfer_normalization_verified",
            "honest_dotD_validator_replay",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    symbolic = load(INPUTS["symbolic_replay"])
    replay_gate = load(INPUTS["transport_replay_gate"])
    payload = load(INPUTS["hym_projector_payload"])
    sm_probe = load(INPUTS["sm_dotd_transport_probe"])
    sm_norm = load(INPUTS["sm_alpha1_source_strength_theorem"])
    sm_origin = load(INPUTS["sm_source_origin_alpha1_driver"])

    contract = build_contract(sm_norm, sm_origin)
    formula = sm_probe["transport_derivative_formula"]
    validator = sm_probe["validator_boundary"]
    current = sm_norm["current_status"]
    evidence = sm_norm["current_evidence"]

    decision = {
        "transport_derivative_formula_closed": sm_probe["theorem"]["proved"],
        "selected_dotD_source_formula_closed": sm_probe["promotion_decision"]["selected_dotD_source_formula_closed"],
        "selected_dotD_source_verified_by_transport_derivative": sm_probe["promotion_decision"]["selected_dotD_source_verified_by_transport_derivative"],
        "projector_riesz_green_replay_closed": symbolic["validator_result"]["all_sector_projector_riesz_green_replays_pass"],
        "validator_ready_rho_s_closed": symbolic["validator_result"]["selected_rho_s_validator_ready"],
        "dotD_matrices_pass_if_driver_theorem_supplied": evidence["dotd_matrices_pass_if_driver_theorem_supplied"],
        "source_only_fails_only_by_alpha1_driver": validator["source_only_fails_only_by_alpha1_driver"],
        "alpha1_driver_acceptance_theorem_proved": sm_norm["theorem"]["proved"],
        "source_strength_value_contract_created": True,
        "normalization_value_emitted_now": current["normalization_value_emitted_now"],
        "alpha1_driver_verified_now": current["alpha1_driver_verified_now"],
        "honest_dotD_validator_closed_now": current["honest_dotd_validator_closed_now"],
        "selected_transfer_normalization_closed": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "selected_matter_slot_routing_emitted": False,
        "selected_1M_Dirac_neutrino_rule_emitted": False,
        "primitive_C1_values_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCdotDAlpha1TransportDerivativeAndDriver",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "symbolic_replay": {"path": rel(INPUTS["symbolic_replay"]), "present": True, "status": symbolic.get("status")},
            "transport_replay_gate": input_status("transport_replay_gate", replay_gate),
            "hym_projector_payload": {"path": rel(INPUTS["hym_projector_payload"]), "present": True, "status": payload.get("status")},
            "sm_dotd_transport_probe": input_status("sm_dotd_transport_probe", sm_probe),
            "sm_alpha1_source_strength_theorem": input_status("sm_alpha1_source_strength_theorem", sm_norm),
            "sm_source_origin_alpha1_driver": input_status("sm_source_origin_alpha1_driver", sm_origin),
        },
        "source_strength_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "transport_derivative_payload": {
            "U": formula["U"],
            "dU_dalpha": formula["dU_dalpha"],
            "h_symbol": formula["h_symbol"],
            "dotD_h": formula["dotD_h"],
            "identity": formula["identity"],
            "response": formula["response"],
            "horizontal_gauge_requires": formula["horizontal_gauge_requires"],
            "h_ext_mean_abs": formula["h_ext_mean_abs"],
            "h_ext_residual_l2": sm_probe["driver_audit"]["h_ext_residual_l2"],
        },
        "validator_replay_boundary": {
            "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived": validator["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"],
            "source_only_fails_only_by_alpha1_driver": validator["source_only_fails_only_by_alpha1_driver"],
            "source_only_validation": validator["source_only_validation"],
            "full_flag_validation": validator["full_flag_validation"],
            "promote_full_flags_now": validator["promote_full_flags_now"],
        },
        "theorem": {
            "name": "U1YRouteCdotDAlpha1TransportDerivativeAndDriverCriterion",
            "proved": True,
            "statement": (
                "The selected transported zero-mode packet has a closed dotD source "
                "formula: for U=exp(-u ad(T3)), dU/dalpha=-(du/dalpha)ad(T3)U "
                "and dotD_h=(dh)ad(T3). Together with the symbolic projector/Riesz/Green "
                "replay, this proves the local dotD algebra and identifies the only "
                "remaining flag: a same-branch alpha1 source-strength value proving "
                "du/dalpha1=h_ext in the selected zero-mean HYM row gauge. Until that "
                "value is emitted, alpha1_driver_verified and honest dotD replay remain open."
            ),
        },
        "what_closes_now": {
            "dU_dalpha_formula": True,
            "dotD_h_formula": True,
            "selected_dotD_source_algebra": True,
            "honest_replay_reduced_to_alpha1_driver_value": True,
            "source_strength_value_contract": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "emit_selected_source_strength_normalization_value": True,
            "selected_transfer_normalization_to_existing_dotD_matrices": True,
            "honest_dotD_validator_replay_without_lifted_alpha1_flag": True,
            "matter_slot_routing": True,
            "one_M_Dirac_neutrino_rule": True,
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
            "claims_alpha1_driver_verified": False,
            "claims_honest_dotD_validator_closed": False,
            "claims_source_strength_value_emitted": False,
            "claims_selected_transfer_normalization": False,
            "claims_physical_dotD_alpha1_payload": False,
            "claims_selected_matter_slot_routing": False,
            "claims_selected_1M_Dirac_neutrino_rule": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_full_flag_probe_as_proof": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCdotDAlpha1TransportDerivativeAndDriver",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "source_strength_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "transport_derivative_formula_closed": decision["transport_derivative_formula_closed"],
        "selected_dotD_source_formula_closed": decision["selected_dotD_source_formula_closed"],
        "projector_riesz_green_replay_closed": decision["projector_riesz_green_replay_closed"],
        "validator_ready_rho_s_closed": decision["validator_ready_rho_s_closed"],
        "source_strength_value_contract_created": True,
        "normalization_value_emitted_now": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, contract, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C dotD alpha1 TransportDerivative and Driver v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"transport_derivative_formula_closed = {str(cert['transport_derivative_formula_closed']).lower()}",
        f"selected_dotD_source_formula_closed = {str(cert['selected_dotD_source_formula_closed']).lower()}",
        f"source_strength_value_contract_created = {str(cert['source_strength_value_contract_created']).lower()}",
        f"alpha1_driver_verified_now = {str(cert['alpha1_driver_verified_now']).lower()}",
        f"honest_dotD_validator_closed_now = {str(cert['honest_dotD_validator_closed_now']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This constructs the object needed to close `dotD_alpha1`: the transport",
        "derivative formula plus a source-strength value contract. The algebra is",
        "closed, but the physical driver value is still open.",
        "",
        "## Formula",
        "",
        "```text",
        "U = exp(-u ad(T3))",
        "dU/dalpha = -(du/dalpha) ad(T3) U",
        "dotD_h = (dh) ad(T3)",
        "D_sel(delta psi) + dotD_h psi_sel = 0",
        "```",
        "",
        "## Closing Requirement",
        "",
        "Emit a same-branch source-strength normalization proving",
        "`du/dalpha1 = h_ext` in the selected zero-mean HYM row gauge. Only then",
        "`alpha1_driver_verified` can become true and the honest dotD validator can",
        "replay without lifted flags.",
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
    candidate, contract, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
