"""Build CONST-HIGGS-01 H7B1I M_source from selected response prefix."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PREFIX_IMPORT = BASE / "selected_response_prefix_import.packet.json"
FUNCTOR = BASE / "msource_acceptance_functor.packet.json"
CURRENT_ATTEMPT = BASE / "current_msource_export_attempt.packet.json"
OBSTRUCTION = BASE / "dynamic_hessian_obstruction_theorem.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1I_MSourceFromSelectedResponsePrefix_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1I_MSOURCE_RESPONSE_PREFIX_CONTRACT_BUILT_VALUE_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1g_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource.candidate.json"
    h7b1g_msource_request_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "msource_minimal_operator_payload_request.packet.json"
    h7b1h_path = DATA / "const_higgs_01_h7b1h_nearhit_source_export_audit.candidate.json"
    trace_payload_path = SM_PARITY_REPO / "candidate_data" / "selected_tracepayload_or_fullhymoperatoremission.candidate.json"
    trace_reconciliation_path = SM_PARITY_REPO / "candidate_data" / "selected_tracepayload_or_fullhymoperatoremission" / "selected_trace_payload_reconciliation.packet.json"
    transition_closure_path = SM_PARITY_REPO / "candidate_data" / "selected_tracepayload_or_fullhymoperatoremission" / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
    transition_attack_path = SM_PARITY_REPO / "candidate_data" / "selected_transitionpayload_or_heattorsionresponse_onegateattack" / "selected_transition_payload_attack.packet.json"
    transition_contract_path = SM_PARITY_REPO / "candidate_data" / "selected_transitionpayload_or_heattorsionresponse_onegateattack" / "transition_payload_promotion_contract.open.json"
    finite_emission_path = SM_PARITY_REPO / "candidate_data" / "finite_emission_morphism_phifin.candidate.json"
    visible_cw_path = SM_PARITY_REPO / "candidate_data" / "selected_visible_chern_weil_operator_source.candidate.json"
    dotd_c1_path = Q79_REPO / "candidate_data" / "q79_selected_dotd_alpha1_c1_response_emission.candidate.json"
    c1_reduction_path = Q79_REPO / "certificates" / "c1_finite_response_matrix_reduction_certificate.json"

    h7b1g = load(h7b1g_path)
    h7b1g_msource_request = load(h7b1g_msource_request_path)
    h7b1h = load(h7b1h_path)
    trace_payload = load(trace_payload_path)
    trace_reconciliation = load(trace_reconciliation_path)
    transition_closure = load(transition_closure_path)
    transition_attack = load(transition_attack_path)
    transition_contract = load(transition_contract_path)
    finite_emission = load(finite_emission_path)
    visible_cw = load(visible_cw_path)
    dotd_c1 = load(dotd_c1_path)
    c1_reduction = load(c1_reduction_path)

    selected_trace_payload = trace_reconciliation["selected_trace_payload"]
    transition_result = transition_closure["closure_result"]
    c1_required = c1_reduction["values_still_required"]
    dotd_frontier = dotd_c1["dotd_alpha1_frontier"]
    c1_contract_not_closed = dotd_c1["c1_response_emission_contract"]["not_closed"]

    prefix_import = {
        "schema": "MTTConstHiggs01H7B1ISelectedResponsePrefixImport.v1",
        "status": "SELECTED_RESPONSE_PREFIX_IMPORTED_DYNAMIC_MSOURCE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-SELECTED-RESPONSE-PREFIX-IMPORT",
        "input_sources": {
            "H7B1G_M_source_request": rel(h7b1g_msource_request_path),
            "H7B1H_route_decision": rel(h7b1h_path),
            "selected_trace_payload": rel(trace_payload_path),
            "selected_trace_payload_reconciliation": rel(trace_reconciliation_path),
            "transition_slot_closure": rel(transition_closure_path),
            "finite_emission_morphism": rel(finite_emission_path),
            "visible_chern_weil_operator_source": rel(visible_cw_path),
            "q79_dotd_c1_response": rel(dotd_c1_path),
            "c1_finite_response_matrix_reduction": rel(c1_reduction_path),
        },
        "selected_static_prefix": {
            "branch": selected_trace_payload["branch"],
            "basis_id": selected_trace_payload["basis_id"],
            "basis_dimension": selected_trace_payload["basis_dimension"],
            "selected_eta_N": selected_trace_payload["selected_eta_N"],
            "selected_gap_lower_bound": selected_trace_payload["selected_gap_lower_bound"],
            "selected_green_norm_bound": selected_trace_payload["selected_green_norm_bound"],
            "zero_cluster_indices": selected_trace_payload["zero_cluster_indices"],
            "H_sector_trace_identity": selected_trace_payload["selected_trace_equality"]["H_sector"],
            "transition_slot_closed": transition_result["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"],
            "source_value_emitted_for_DE_gap_layer": transition_result["source_value_emitted"],
        },
        "dynamic_parts_still_open": {
            "selected_dotD_alpha1_source_identity_closed": transition_result["selected_dotD_alpha1_source_identity_closed"],
            "actual_dynamic_QaSU3_operator_packet_closed": transition_result["actual_dynamic_QaSU3_operator_packet_closed"],
            "full_S2_value_emission_closed": transition_result["full_S2_value_emission_closed"],
            "determinant_torsion_slot_closed": transition_result["determinant_torsion_slot_closed"],
            "finite_determinant_heat_spectrum_or_torsion_response": trace_payload["what_remains_open"]["finite_determinant_heat_spectrum_or_torsion_response"],
            "primitive_C1_response": trace_payload["what_remains_open"]["primitive_C1_response"],
            "A_selected_and_b_selected": trace_payload["what_remains_open"]["A_selected_and_b_selected"],
        },
        "value_emitted": False,
        **clean_flags(),
    }

    functor = {
        "schema": "MTTConstHiggs01H7B1IMSourceAcceptanceFunctor.v1",
        "status": "MSOURCE_ACCEPTANCE_FUNCTOR_BUILT_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-MSOURCE-ACCEPTANCE-FUNCTOR",
        "finite_source_space": {
            "branch": selected_trace_payload["branch"],
            "basis_id": selected_trace_payload["basis_id"],
            "basis_dimension": selected_trace_payload["basis_dimension"],
            "same_source_required": True,
        },
        "formal_construction_when_payload_exists": {
            "response_hessian": "H_response = Hess_response restricted to the selected finite source space",
            "H_sector_restriction": "R_H: selected finite source space -> selected H-sector response subspace",
            "Hermitian_projection": "M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2",
            "Huv_link": "H_uv = B_Huv^* M_source B_Huv, only after B_Huv is separately emitted",
        },
        "acceptance_requirements": [
            "selected tangent or retarded derivative source for q79/F,m=1",
            "same-branch alpha1/response driver with honest no-lift replay",
            "finite Hess_Xi or mass/strain block on the selected source space",
            "H-sector restriction map onto the response subspace, not only the collapsed H line",
            "Hermiticity check M_source^*=M_source in the selected source metric",
            "finite exactness/error certificate for H_response and R_H",
            "proof that no observed Higgs, beta, mass, Yukawa, or threshold target selects any entry",
        ],
        "what_current_prefix_supplies": {
            "selected_DE_gap_Riesz_Green_layer": True,
            "selected_trace_equality_for_27mode_DE": selected_trace_payload["selected_trace_equality"]["proved"],
            "H_sector_rank_two_zero_cluster_support": selected_trace_payload["selected_trace_equality"]["H_sector"],
            "selected_green_norm_bound": selected_trace_payload["selected_green_norm_bound"],
            "same_basis_dotD_value_matrices_available_as_support": dotd_frontier["closed_finite_prefix"]["dotD_alpha1_value_matrices_emitted"],
        },
        "what_current_prefix_does_not_supply": {
            "selected_tangent_or_retarded_derivative_source": dotd_c1["selected_tangent_or_retarded_kernel_obstruction"]["source_driver_requirements"]["R4_selected_alpha1_deformation_parameter"] is False,
            "same_branch_alpha1_driver_theorem": dotd_frontier["remaining_gates"]["same_branch_alpha1_driver_theorem"],
            "honest_dotD_replay_without_lifted_flags": dotd_c1["selected_tangent_or_retarded_kernel_obstruction"]["source_driver_requirements"]["R6_honest_dotD_replay_without_lifted_flags"] is False,
            "full_lower_order_Hess_Xi_blocks": c1_required["full_lower_order_Hess_Xi_blocks"],
            "selected_deltaTheta_C1_solution": c1_required["selected_deltaTheta_C1_solution"],
            "sector_dotD_Q_u_d_L_e_N_H": c1_required["sector_dotD_Q_u_d_L_e_N_H"],
            "sector_zero_mode_bases_Q_u_d_L_e_N_H": c1_required["sector_zero_mode_bases_Q_u_d_L_e_N_H"],
            "primitive_3x3_contraction_terms_for_each_sector": c1_required["primitive_3x3_contraction_terms_for_each_sector"],
            "H_sector_Hermitian_mass_strain_restriction": True,
        },
        "M_source_value_emitted": False,
        **clean_flags(),
    }

    current_attempt = {
        "schema": "MTTConstHiggs01H7B1ICurrentMSourceExportAttempt.v1",
        "status": "CURRENT_MSOURCE_EXPORT_ATTEMPT_BLOCKED_BY_DYNAMIC_HESSIAN_AND_RESTRICTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-CURRENT-MSOURCE-EXPORT-ATTEMPT",
        "attempted_export": {
            "candidate_formula": functor["formal_construction_when_payload_exists"]["Hermitian_projection"],
            "source_space": functor["finite_source_space"],
            "available_prefix_is_sufficient_for_contract": True,
            "available_prefix_is_sufficient_for_values": False,
        },
        "strict_missing_fields": {
            "selected_tangent_or_retarded_derivative_source": True,
            "same_branch_alpha1_response_driver": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "finite_Hess_Xi_or_mass_strain_block": True,
            "H_sector_restriction_map": True,
            "Hermitian_M_source_entries": True,
            "exactness_certificate": True,
        },
        "computed_values": {
            "M_source": None,
            "H_response": None,
            "R_H": None,
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    obstruction = {
        "schema": "MTTConstHiggs01H7B1IDynamicHessianObstructionTheorem.v1",
        "status": "DYNAMIC_HESSIAN_OBSTRUCTION_PROVED_MSOURCE_VALUE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-DYNAMIC-HESSIAN-OBSTRUCTION",
        "theorem": {
            "name": "H7B1IDynamicHessianNotImpliedByTraceGapTheorem",
            "proved": True,
            "statement": (
                "The selected Phi_fin trace payload closes the finite D_E/gap/Riesz/Green layer and supplies H-sector zero-cluster support, but this does not determine a dynamic Hermitian mass/strain operator M_source. "
                "M_source requires a selected response Hessian or mass/strain block plus an H-sector restriction map from the same source. Current dotD/C1 artifacts leave the selected tangent, same-branch driver, lower-order Hess_Xi blocks, zero-mode responses, primitive contractions, and H-sector Hermitian restriction open. Therefore H7B1I builds the M_source acceptance functor but emits no M_source value."
            ),
        },
        "proof_steps": [
            "The trace payload identifies D_E and its gap/Riesz/Green data at a stationary finite trace layer.",
            "A stationary trace/gap layer is quadratic spectral support; it is not a response Hessian for the Higgs mass/strain splitting.",
            "The C1 finite-response reduction explicitly leaves evaluated source vector, deltaTheta_C1, lower-order Hess_Xi blocks, sector dotD, zero modes, and primitive contractions open.",
            "Without H_response and R_H, the Hermitian projection formula for M_source has no entries to evaluate.",
            "Since H_uv also requires B_Huv, no Omega, s_beta, lambda_H, or strict Higgs closure follows from this prefix.",
        ],
        "countermodel_boundary": {
            "same_static_trace_gap_data": True,
            "vary_dynamic_H_response": True,
            "M_source_changes": True,
            "stationary_DE_gap_layer_unchanged": True,
            "therefore_static_prefix_underdetermines_M_source": True,
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1INextWork.v1",
        "status": "NEXT_WORKORDER_H7B1J_DYNAMIC_HESSIAN_OR_HSECTOR_RESTRICTION_EXPORT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-DYNAMIC-HESSIAN-OR-HSECTOR-RESTRICTION-EXPORT",
            "task": "Try to emit either the selected response Hessian/mass-strain block H_response or the selected H-sector restriction map R_H from the same q79/F,m=1 source.",
        },
        "two_subroutes": [
            {
                "id": "H7B1J-A",
                "label": "dynamic Hessian export",
                "must_emit": "finite Hess_Xi or mass/strain block with selected tangent/driver and no lifted flags",
            },
            {
                "id": "H7B1J-B",
                "label": "H-sector restriction export",
                "must_emit": "R_H mapping the selected finite source space into the H-sector response subspace, compatible with the rank-two zero-cluster support",
            },
        ],
        "do_not_repeat": [
            "Do not relabel D_E/gap/Riesz/Green support as M_source.",
            "Do not relabel rank-one H projector or zero-cluster support as B_Huv.",
            "Do not backsolve from Higgs mass, lambda_H, beta, or threshold residual.",
        ],
        **clean_flags(),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1IMSourceFromSelectedResponsePrefix",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-MSOURCE-FROM-SELECTED-RESPONSE-PREFIX",
        "output_packets": {
            "selected_response_prefix_import": rel(PREFIX_IMPORT),
            "msource_acceptance_functor": rel(FUNCTOR),
            "current_msource_export_attempt": rel(CURRENT_ATTEMPT),
            "dynamic_hessian_obstruction_theorem": rel(OBSTRUCTION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": obstruction["theorem"],
        "H7B1G_contract_imported": h7b1g["both_payloads_required_for_Huv"],
        "H7B1H_msource_first_route_imported": h7b1h["selected_next_route"] == "M_source_first",
        "selected_response_prefix_imported": True,
        "selected_DE_gap_Riesz_Green_layer_closed": True,
        "H_sector_rank_two_zero_cluster_support_imported": True,
        "M_source_acceptance_functor_built": True,
        "dynamic_hessian_obstruction_proved": True,
        "M_source_value_emitted": False,
        "B_Huv_value_emitted": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1J_DynamicHessianOrHSectorRestrictionExport_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1I_MSourceFromSelectedResponsePrefix_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_response_prefix_imported": True,
        "selected_DE_gap_Riesz_Green_layer_closed": True,
        "H_sector_rank_two_zero_cluster_support_imported": True,
        "M_source_acceptance_functor_built": True,
        "dynamic_hessian_obstruction_proved": True,
        "M_source_value_emitted": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1I MSource From Selected Response Prefix v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1I-MSOURCE-FROM-SELECTED-RESPONSE-PREFIX`

## Result

```text
selected response prefix imported          True
selected D_E/gap/Riesz/Green layer closed  True
H-sector rank-two zero-cluster support     True
M_source acceptance functor built          True
M_source value emitted                     False
H_uv / Omega / s_beta / lambda_H           False
strict no-knob Higgs closure               False
```

## Construction Contract

If the dynamic payload is later emitted, the accepted source operator is:

```text
H_response = Hess_response restricted to the selected finite source space
M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2
H_uv = B_Huv^* M_source B_Huv
```

Here `R_H` is the same-source H-sector restriction map.  `B_Huv` is still a
separate payload; it is not needed to verify `M_source`, but it is required to
compute `H_uv`.

## Why No Value Yet

The selected trace payload closes only the stationary finite trace
`D_E/gap/Riesz/Green` layer.  It does not emit the selected tangent/response
driver, finite dynamic Hessian/mass-strain block, H-sector restriction map, or
Hermitian `M_source` entries.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-DYNAMIC-HESSIAN-OR-HSECTOR-RESTRICTION-EXPORT`
"""

    for path, payload in [
        (PREFIX_IMPORT, prefix_import),
        (FUNCTOR, functor),
        (CURRENT_ATTEMPT, current_attempt),
        (OBSTRUCTION, obstruction),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
