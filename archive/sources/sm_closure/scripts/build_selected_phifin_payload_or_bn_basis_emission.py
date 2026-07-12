"""Build the selected Phi_fin payload or B_N basis emission contract.

This locks the remaining primitive-emission work at field level.  It does not
claim the selected payload or basis has been emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"

PREVIOUS = DATA / "selected_routec_source_provenance_or_basis_certificate.candidate.json"
FIRST_RUN = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"
PHIFIN = DATA / "finite_emission_morphism_phifin.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"

OUT_DATA = DATA / "selected_phifin_payload_or_bn_basis_emission.candidate.json"
OUT_CERT = CERTS / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
OUT_NOTE = CORPUS / "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1.md"
CONTRACT_DIR = DATA / "selected_phifin_payload_or_bn_basis_emission"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def true_map(keys: list[str]) -> dict[str, bool]:
    return {key: True for key in keys}


def build_phifin_contract(phifin: dict[str, Any], alpha: dict[str, Any]) -> dict[str, Any]:
    required_outputs = list(phifin["phifin_schema"]["required_outputs"])
    alpha_required = list(alpha["next_blocker"]["must_supply"])
    selected_flags = [
        "route_c_residual.selected_source_verified",
        "operator_slots[*].selected_source_verified",
        "spectral_slots[*].selected_source_verified",
        "green_slots[*].selected_source_verified",
        "dotd_response_slots[*].selected_dotD_source_verified",
        "dotd_response_slots[*].alpha1_driver_verified",
    ]
    validation_files = [
        "route_c_residual.candidate.json",
        "rhoE_mesh.candidate.json",
        "rhoE_metric.candidate.json",
        "sector_maps.candidate.json",
        "de_action.candidate.json",
        "riesz_gap.candidate.json",
        "reduced_green.candidate.json",
        "dotd_response.candidate.json",
        "spectral_galerkin_data.candidate.json",
        "c1_primitive_contractions.candidate.json",
    ]
    return {
        "schema": "MTTSelectedPhiFinPayloadEmissionContract.v1",
        "status": "OPEN_SELECTED_VALUES_NOT_EMITTED",
        "domain": phifin["phifin_schema"]["domain"],
        "codomain_files": validation_files,
        "required_outputs": required_outputs,
        "alpha1_required_outputs": alpha_required,
        "flags_that_must_be_theorem_derived": selected_flags,
        "minimum_selected_payload_fields": {
            "selected_source_certificate": None,
            "rho_E_transition_data": None,
            "Hermitian_metric": None,
            "connection_A_star": None,
            "sector_projectors": None,
            "D_E_action_slots": None,
            "Riesz_projectors_and_gap": None,
            "reduced_Green_operators": None,
            "dotD_alpha1_matrices": None,
            "horizontal_responses": None,
            "finite_C1_Hessian_source": None,
            "primitive_C1_contractions": None,
            "spectral_error_budget": None,
        },
        "current_status": {
            "support_shapes_present": alpha["payload_summary"]["all_support_shapes_present"],
            "selected_values_emitted": alpha["payload_summary"]["all_selected_values_emitted"],
            "selected_flags": phifin["phifin_schema"]["selected_flags"],
        },
        "promotion_rule": "All fields must be emitted from the selected q79/F,m=1 Strominger/HYM minimizer, not from lifted smoke flags.",
        "forbidden_shortcuts": [
            "lift selected flags by hand",
            "reuse identity rho_E smoke as selected data",
            "choose entries from observed masses, CKM/PMNS, or benchmark matrices",
            "treat residual zero in smoke fixtures as source selection",
        ],
    }


def build_bn_contract() -> dict[str, Any]:
    basis = load_json(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json")
    protocol = load_json(Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json")
    deck = load_json(Q79_CERTS / "iwasawa_standard_lattice_deck_scaffold_certificate.json")
    spectral = load_json(Q79_CERTS / "iwasawa_spectral_galerkin_data.template.json")
    zero_mode = load_json(Q79_CERTS / "selected_zero_mode_basis_dotd_interface_certificate.json")
    required_fields = [
        "selected_deck_or_equivalent_cover",
        "scalar_basis_functions_phi_m",
        "deck_or_periodic_constraints",
        "bundle_transition_or_equivariance_matrices",
        "metric_volume_quadrature",
        "selected_D_E_action_on_basis",
        "Gram_matrix_entries",
        "stiffness_matrix_entries",
        "generalized_eigenpairs",
        "Riesz_projectors",
        "reduced_Green_operators",
        "gap_error_certificate",
        "ordered_zero_mode_bases_Q_u_d_L_e_N_H",
        "dotD_alpha1_in_same_basis",
    ]
    return {
        "schema": "MTTSelectedBNBasisEmissionContract.v1",
        "status": "OPEN_SELECTED_BASIS_NOT_EMITTED",
        "basis_skeleton_status": basis["status"],
        "deck_scaffold_status": deck["status"],
        "closed_support": {
            "form_fiber_tensor_bookkeeping": basis["closed_decisions"]["form_fiber_tensor_bookkeeping_closed"],
            "candidate_deck_generators": deck["what_this_closes"]["explicit_candidate_deck_generators"],
            "fundamental_gluing_laws": deck["what_this_closes"]["fundamental_gluing_laws_formulated"],
            "matrix_protocol_formulated": protocol["verdict"]["closes_execution_protocol"],
            "zero_mode_dotD_interface_formulated": zero_mode["status"] == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN",
        },
        "required_fields": true_map(required_fields),
        "required_basis_checks": protocol["finite_basis_protocol"]["basis_checks"],
        "required_success_gates": spectral["success_gates"],
        "current_open_fields": {
            **basis["still_missing_for_actual_B_N"],
            **deck["still_open"],
            **protocol["values_still_open"],
        },
        "minimum_basis_payload_fields": {
            "basis_id": None,
            "selected_deck_certificate": None,
            "scalar_basis": None,
            "bundle_equivariance": None,
            "quadrature_rule": None,
            "gram_matrix": None,
            "stiffness_matrix": None,
            "operator_action_matrices": None,
            "eigenpairs": None,
            "gap_error_budget": None,
            "sector_zero_mode_bases": None,
        },
        "forbidden_shortcuts": [
            "use torus Fourier modes without nonabelian deck check",
            "use invariant subspace as the selected non-invariant basis",
            "use scalar central-circle Fourier modes as untwisted zero modes",
            "choose basis to fit observed masses or mixings",
        ],
    }


def build_candidate() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    first = load_json(FIRST_RUN)
    phifin = load_json(PHIFIN)
    alpha = load_json(PHIFIN_ALPHA1)
    phifin_contract = build_phifin_contract(phifin, alpha)
    bn_contract = build_bn_contract()

    phifin_path = CONTRACT_DIR / "selected_phifin_payload.emission_contract.json"
    bn_path = CONTRACT_DIR / "selected_bn_basis.emission_contract.json"
    write_json(phifin_path, phifin_contract)
    write_json(bn_path, bn_contract)

    remaining_parts = {
        "R1_selected_source_certificate": "must identify the selected q79/F,m=1 Strominger/HYM minimizer and justify all selected-source flags",
        "R2_selected_rhoE_metric_connection": "must emit rho_E, Hermitian metric, connection A*, and sector projectors",
        "R3_selected_operator_spectral_data": "must emit D_E, Riesz projectors, gaps, reduced Green operators, and dotD_alpha1",
        "R4_selected_basis_data": "must emit quotient/deck-valid B_N, quadrature, Gram/stiffness matrices, and eigenpairs",
        "R5_selected_C1_response": "must emit finite Hessian source, horizontal responses, and primitive C1 contractions",
        "R6_replay_without_lifted_flags": "must rerun validators on honest manifest and promotion gate without formal-lift flags",
    }
    dependency_order = [
        "R1_selected_source_certificate",
        "R2_selected_rhoE_metric_connection",
        "R4_selected_basis_data",
        "R3_selected_operator_spectral_data",
        "R5_selected_C1_response",
        "R6_replay_without_lifted_flags",
    ]
    closure_vector = {key: False for key in remaining_parts}
    support_vector = {
        "formal_lift_algebra_passes": first["validation"]["formal_lift_lower_validators_all_pass"],
        "phifin_contract_written": phifin_path.exists(),
        "bn_contract_written": bn_path.exists(),
        "remaining_parts_ordered": True,
        "no_target_fitting": True,
    }
    return {
        "candidate": "MTTSelectedPhiFinPayloadOrBNBasisEmission",
        "status": "MTT_SELECTED_PHIFIN_OR_BN_EMISSION_CONTRACTS_LOCKED_VALUES_OPEN",
        "inputs": {
            "previous": rel(PREVIOUS),
            "first_run": rel(FIRST_RUN),
            "phifin": rel(PHIFIN),
            "phifin_alpha1": rel(PHIFIN_ALPHA1),
        },
        "contracts": {
            "selected_phifin_payload": rel(phifin_path),
            "selected_bn_basis": rel(bn_path),
        },
        "superset_mode": {
            "classification": "DUAL_PRIMITIVE_EMISSION_CONTRACT",
            "straight_path": {
                "classification": "NOT_CLOSED",
                "reason": "Current artifacts write contracts and support data but do not emit selected values.",
            },
            "superset_convergence": {
                "classification": "FIELD_LEVEL_REMAINING_PARTS_LOCKED",
                "locked_target": "honest selected Route-C manifest without lifted flags",
                "support": support_vector,
            },
            "superset_repair": {
                "classification": "EMIT_ONE_OR_BOTH_PRIMITIVES",
                "options": ["selected Phi_fin payload", "selected B_N basis certificate"],
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "remaining_parts": remaining_parts,
        "dependency_order": dependency_order,
        "closure_vector": closure_vector,
        "support_vector": support_vector,
        "what_closes_now": {
            "selected_phifin_payload_contract_written": phifin_path.exists(),
            "selected_bn_basis_contract_written": bn_path.exists(),
            "remaining_parts_field_locked": True,
            "dependency_order_locked": True,
            "honest_replay_target_locked": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            **{key: True for key in remaining_parts},
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedPhiFinOrBNEmissionContractTheorem",
            "proved": True,
            "statement": (
                "The remaining Route-C closure parts are locked at field level.  A selected Phi_fin payload contract and a selected B_N "
                "basis contract are written, with dependency order and replay target fixed.  No selected values are emitted yet; the next "
                "step must fill R1-R6 from MTT-selected data and replay the validators without lifted flags."
            ),
        },
        "previous_gate_closed": previous["calculation"]["support_closed"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1",
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "MTTSelectedPhiFinPayloadOrBNBasisEmission",
        "status": candidate["status"],
        "candidate_path": rel(OUT_DATA),
        "note_path": rel(OUT_NOTE),
        "contracts": candidate["contracts"],
        "closure_vector": candidate["closure_vector"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "primary_next_artifact": candidate["next_required_artifact"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    parts = "\n".join(f"- `{key}`: {value}" for key, value in candidate["remaining_parts"].items())
    order = "\n".join(f"{idx + 1}. `{key}`" for idx, key in enumerate(candidate["dependency_order"]))
    return f"""# MTT Selected Phi_fin Payload or B_N Basis Emission

Status: `{candidate['status']}`.

This locks down the remaining parts at field level.

## Contracts

- selected Phi_fin payload: `{candidate['contracts']['selected_phifin_payload']}`
- selected B_N basis: `{candidate['contracts']['selected_bn_basis']}`

## Remaining Parts

{parts}

## Dependency Order

{order}

## Result

The contracts are written and the honest replay target is locked.  No selected
values are emitted yet.  The next step must fill either the selected `Phi_fin`
payload or the selected quotient/deck-valid `B_N` basis, then replay the
Route-C manifest without lifted flags.

Next artifact: `{candidate['next_required_artifact']}`.
"""


def main() -> int:
    candidate = build_candidate()
    cert = build_certificate(candidate)
    write_json(OUT_DATA, candidate)
    write_json(OUT_CERT, cert)
    OUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps({"candidate": rel(OUT_DATA), "status": candidate["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
