"""Build CONST-HIGGS-01 H7B1J dynamic Hessian or H-sector restriction export."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC_EDGE = BASE / "dynamic_hessian_edge_export_attempt.packet.json"
HSECTOR_EDGE = BASE / "hsector_restriction_edge_export_attempt.packet.json"
COMPACT_WITNESS = BASE / "rejected_compact_h_dotd_numeric_witness.packet.json"
GATE_VALIDATOR = BASE / "strict_msource_gate_validator.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1J_DynamicHessianOrHSectorRestrictionExport_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1J_DYNAMIC_HESSIAN_OR_HSECTOR_RESTRICTION_GATE_BUILT_STRICT_EXPORT_OPEN"


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


def pair_to_complex(value: Any) -> complex:
    if isinstance(value, list) and len(value) == 2 and all(isinstance(v, (int, float)) for v in value):
        return complex(float(value[0]), float(value[1]))
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    raise TypeError(f"cannot parse complex pair: {value!r}")


def complex_to_pair(value: complex) -> list[float]:
    return [value.real, value.imag]


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1i_path = DATA / "const_higgs_01_h7b1i_msource_from_selected_response_prefix.candidate.json"
    h7b1i_functor_path = DATA / "const_higgs_01_h7b1i_msource_from_selected_response_prefix" / "msource_acceptance_functor.packet.json"
    hym_first_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"
    hym_green_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor" / "full_diagonal_end0_green_payload.packet.json"
    rank2_boundary_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor" / "rank2_to_sector_transfer_boundary.packet.json"
    post_hym_path = SM_PARITY_REPO / "candidate_data" / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json"
    projector_progress_path = SM_PARITY_REPO / "candidate_data" / "selected_physicaldotd_sectorrouting_after_hymfirstsolve" / "hym_projector_value_progress_after_first_solve.packet.json"
    projector_kernel_path = SM_PARITY_REPO / "candidate_data" / "selected_physicaldotd_sectorrouting_after_hymfirstsolve" / "selected_projector_source_promotion_kernel.packet.json"
    end0_functor_path = SM_PARITY_REPO / "candidate_data" / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
    compact_dotd_path = SM_PARITY_REPO / "candidate_data" / "selected_routec_strominger_galerkin_solve" / "dotd_response.candidate.json"
    psm_c1_06_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate.candidate.json"
    psm_c1_06_status_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate" / "unpatched_sector_rows_and_replay_independence_status.packet.json"
    psm_c1_06_payload_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate" / "route_b_full_conditional_validator_payload.packet.json"
    psm_c1_06_result_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate" / "route_b_full_conditional_validator_result.packet.json"
    hessian_vector_path = SM_PARITY_REPO / "candidate_data" / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json"
    dynamic_transfer_path = SM_PARITY_REPO / "candidate_data" / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
    dynamic_overlap_path = SM_PARITY_REPO / "candidate_data" / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
    five_clause_path = SM_PARITY_REPO / "candidate_data" / "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset" / "five_clause_source_promotion_attempt.packet.json"

    h7b1i = load(h7b1i_path)
    h7b1i_functor = load(h7b1i_functor_path)
    hym_first = load(hym_first_path)
    hym_green = load(hym_green_path)
    rank2_boundary = load(rank2_boundary_path)
    post_hym = load(post_hym_path)
    projector_progress = load(projector_progress_path)
    projector_kernel = load(projector_kernel_path)
    end0_functor = load(end0_functor_path)
    compact_dotd = load(compact_dotd_path)
    psm_c1_06 = load(psm_c1_06_path)
    psm_c1_06_status = load(psm_c1_06_status_path)
    psm_c1_06_payload = load(psm_c1_06_payload_path)
    psm_c1_06_result = load(psm_c1_06_result_path)
    hessian_vector = load(hessian_vector_path)
    dynamic_transfer = load(dynamic_transfer_path)
    dynamic_overlap = load(dynamic_overlap_path)
    five_clause = load(five_clause_path)

    compact_h = compact_dotd["dotd_response_slots"]["H"]
    z = pair_to_complex(compact_h["dotD_alpha1_matrix"][1][0])
    hermitianized = [
        [0.0, complex_to_pair(z.conjugate() / 2.0)],
        [complex_to_pair(z / 2.0), 0.0],
    ]
    omega_abs_sq = abs(z / 2.0) ** 2
    rejected_s_beta = 0.0 if omega_abs_sq > 0.0 else None

    hessian_clause = five_clause["source_clauses"]["hessian_b_source"]

    dynamic_edge = {
        "schema": "MTTConstHiggs01H7B1JDynamicHessianEdgeExportAttempt.v1",
        "status": "DYNAMIC_HESSIAN_EDGE_ATTEMPT_SUPPORT_STRONG_STRICT_EXPORT_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-A-DYNAMIC-HESSIAN-EXPORT",
        "input_sources": {
            "H7B1I_acceptance_functor": rel(h7b1i_functor_path),
            "PSM_C1_06_candidate": rel(psm_c1_06_path),
            "PSM_C1_06_unpatched_status": rel(psm_c1_06_status_path),
            "PSM_C1_06_conditional_validator_payload": rel(psm_c1_06_payload_path),
            "PSM_C1_06_conditional_validator_result": rel(psm_c1_06_result_path),
            "hessian_source_vector": rel(hessian_vector_path),
            "dynamic_transfer_hessian_bselected": rel(dynamic_transfer_path),
            "dynamic_overlap_hessian_normalization": rel(dynamic_overlap_path),
            "five_clause_source_promotion_attempt": rel(five_clause_path),
        },
        "support_imported": {
            "conditional_RouteB_validator_passes": psm_c1_06["closure_decision"]["conditional_RouteB_validator_passes"],
            "unpatched_RouteB_validator_passes": psm_c1_06["closure_decision"]["unpatched_RouteB_validator_passes"],
            "hessian_source_rows_assembled_from_same_rows_support": psm_c1_06_status["unpatched_support"]["hessian_source_rows_assembled_from_same_rows"],
            "unpatched_actual_row_fill_source_independent": psm_c1_06_status["unpatched_blockers"]["actual_row_fill_source_independent"],
            "unpatched_source_independent_of_residual_projector_replay": psm_c1_06_status["unpatched_blockers"]["source_independent_of_residual_projector_replay"],
            "conditional_independent_hessian_counterterm_source_rows": psm_c1_06_payload["route_B_independent_rowkernel_source"]["independent_hessian_counterterm_source_rows"],
            "conditional_no_residual_projector_replay_or_locked_target_as_source": psm_c1_06_payload["route_B_independent_rowkernel_source"]["no_residual_projector_replay_or_locked_target_as_source"],
            "conditional_validator_result_passes": psm_c1_06_result["passes"],
            "A_transpose_A": hessian_vector["A_transpose_A"],
            "A_transpose_b": hessian_vector["A_transpose_b"],
            "b_norm_sq": hessian_vector["b_norm_sq"],
            "deltaTheta_C1": hessian_vector["deltaTheta_C1"],
            "b_selected_emitted_by_independent_hessian": hessian_vector["b_selected_emitted_by_independent_hessian"],
            "b_selected_replay_available_under_axiom_patch": hessian_vector["b_selected_replay_available_under_axiom_patch"],
            "dynamic_transfer_conditional_gram_exact": dynamic_transfer["what_closes_now"]["conditional_A_transpose_A_Gram_computed"],
            "dynamic_transfer_selected_Hessian_blocks_claimed": dynamic_transfer["selected_Hessian_blocks_claimed"],
            "dynamic_transfer_selected_b_selected_claimed": dynamic_transfer["b_selected_claimed"],
            "dynamic_transfer_selected_identity_claimed": dynamic_transfer["selected_dynamic_transfer_identity_claimed"],
            "dynamic_overlap_selected_Hessian_blocks_emitted": dynamic_overlap["hessian_normalization_route"]["selected_Hessian_blocks_emitted"],
            "dynamic_overlap_selected_b_selected_emitted": dynamic_overlap["hessian_normalization_route"]["selected_b_selected_emitted"],
            "five_clause_values_filled": five_clause["row_values"]["values_filled"],
            "five_clause_values_promoted_as_source": five_clause["row_values"]["values_promoted_as_source"],
        },
        "strict_export_requirements": {
            "same_branch_H_response_or_mass_strain_block": True,
            "theorem_derived_source_emission": True,
            "no_residual_replay_as_source": True,
            "finite_exactness_error_certificate": True,
            "Higgs_two_state_or_Hsector_restriction_target": True,
            "no_observed_Higgs_or_threshold_selector": True,
        },
        "why_current_support_is_not_H_response": {
            "conditional_validator_not_unpatched_export": True,
            "hessian_vector_is_replay_from_residual_projector_contract": hessian_vector["b_selected_emitted_by_independent_hessian"] is False,
            "five_clause_hessian_b_source_emitted": hessian_clause["source_emitted"],
            "five_clause_hessian_b_theorem_derived": hessian_clause["theorem_derived"],
            "five_clause_hessian_b_uses_replay_as_source": hessian_clause["uses_replay_as_source"],
            "dynamic_transfer_selected_Hessian_blocks_emitted": dynamic_transfer["selected_Hessian_blocks_claimed"],
            "dynamic_overlap_selected_Hessian_blocks_emitted": dynamic_overlap["hessian_normalization_route"]["selected_Hessian_blocks_emitted"],
            "c1_rows_live_in_flavor_response_coordinate_system_not_Huv_mass_strain": True,
        },
        "export_decision": {
            "H_response_exported": False,
            "M_source_dynamic_part_exported": False,
            "strict_gate_passes": False,
            "reason": "The C1/Hessian lineage supplies exact conditional and replay support, including A^T A=12 I_2 and A^T b=(12,12), but the unpatched source-emission and replay-independence gates are still open and the rows are not a selected Higgs H_uv mass/strain block.",
        },
        **clean_flags(),
    }

    hsector_edge = {
        "schema": "MTTConstHiggs01H7B1JHSectorRestrictionEdgeExportAttempt.v1",
        "status": "HSECTOR_RESTRICTION_EDGE_ATTEMPT_RANK2_SUPPORT_STRICT_EXPORT_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-B-HSECTOR-RESTRICTION-EXPORT",
        "input_sources": {
            "H7B1I_acceptance_functor": rel(h7b1i_functor_path),
            "HYM_first_solve": rel(hym_first_path),
            "full_diagonal_End0_Green": rel(hym_green_path),
            "rank2_to_sector_transfer_boundary": rel(rank2_boundary_path),
            "physical_dotd_sectorrouting_after_HYM": rel(post_hym_path),
            "projector_progress": rel(projector_progress_path),
            "projector_promotion_kernel": rel(projector_kernel_path),
            "End0_to_sector_functor": rel(end0_functor_path),
            "compact_dotD_response": rel(compact_dotd_path),
        },
        "rank2_and_projector_support_imported": {
            "selected_diagonal_HYM_first_solve_closed": hym_first["closure_decision"]["selected_diagonal_HYM_first_solve_closed"],
            "rank2_End0_payload_closed": hym_first["closure_decision"]["rank2_End0_payload_closed"],
            "rank2_to_sector_transfer_closed": hym_first["closure_decision"]["rank2_to_sector_transfer_closed"],
            "A_HYM_formula_emitted": rank2_boundary["straight_path_progress"]["A_HYM_formula_emitted"],
            "full_diagonal_End0_Green_closed": rank2_boundary["straight_path_progress"]["full_diagonal_End0_Green_closed"],
            "rank2_to_sector_functor_closed": rank2_boundary["rank2_to_sector_functor"]["closed"],
            "physical_dotD_alpha1_emitted": rank2_boundary["rank2_to_sector_functor"]["physical_dotD_alpha1_emitted"],
            "sector_routing_values_emitted": rank2_boundary["rank2_to_sector_functor"]["sector_routing_values_emitted"],
            "finite_model_active_projector_values_emitted": projector_progress["finite_model_active_projector_values_emitted"],
            "selected_HYM_projector_values_promoted": projector_progress["selected_HYM_projector_values_promoted"],
            "PhiFin_selected_trace_emitted": post_hym["closure_decision"]["PhiFin_selected_trace_emitted"],
            "selected_End0_to_sector_routing_values_extracted": post_hym["closure_decision"]["selected_End0_to_sector_routing_values_extracted"],
            "End0_functor_contract_specified": end0_functor["decision"]["functor_contract_specified"],
            "selected_End0_to_sector_functor_values_extracted": end0_functor["decision"]["selected_End0_to_sector_functor_values_extracted"],
            "scalar_normalization_no_go_closed": end0_functor["scalar_normalization_no_go"]["closed"],
            "T1_T2_covariant_Green_closed": hym_green["T1_T2_covariant_Green"]["closed"],
            "offdiagonal_row_model_control_closed": hym_green["offdiagonal_row_model_control"]["closed"],
        },
        "compact_H_slot_support": {
            "dimension": compact_h["dimension"],
            "expected_kernel_dimension": compact_h["expected_kernel_dimension"],
            "kind": compact_h["kind"],
            "dotD_alpha1_matrix": compact_h["dotD_alpha1_matrix"],
            "stiffness_matrix": compact_h["stiffness_matrix"],
            "green_operator_verified": compact_h["green_operator_verified"],
            "horizontal_gauge_verified": compact_h["horizontal_gauge_verified"],
            "selected_dotD_source_verified": compact_h["selected_dotD_source_verified"],
            "alpha1_driver_verified": compact_h["alpha1_driver_verified"],
            "selected_by_mtt": compact_dotd["selected_by_mtt"],
        },
        "zero_cluster_and_H_projector_support": {
            "zero_cluster_indices": projector_progress["zero_cluster"]["indices"],
            "zero_cluster_dimension": projector_progress["zero_cluster"]["dimension"],
            "H_basis_count": projector_progress["sector_rank_summary"]["H"]["basis_count"],
            "H_expected_rank": projector_progress["sector_rank_summary"]["H"]["expected_rank"],
            "H_selected_source_verified": projector_progress["sector_rank_summary"]["H"]["selected_source_verified"],
            "H_value_emitted_as_selected_HYM_projector": projector_progress["sector_rank_summary"]["H"]["value_emitted_as_selected_HYM_projector"],
        },
        "why_current_support_is_not_R_H": {
            "rank2_End0_lane_not_yet_sector_functor": rank2_boundary["rank2_to_sector_functor"]["closed"] is False,
            "finite_projector_values_not_promoted_to_selected": post_hym["closure_decision"]["finite_projector_values_promoted_to_selected"] is False,
            "End0_to_sector_values_not_extracted": end0_functor["decision"]["selected_End0_to_sector_functor_values_extracted"] is False,
            "compact_H_slot_is_single_higgs_carrier": compact_h["kind"] == "single_higgs_carrier",
            "compact_H_slot_flags_are_unselected": compact_h["selected_dotD_source_verified"] is False and compact_h["alpha1_driver_verified"] is False,
            "H_projector_is_rank_one_not_two_Higgs_lift": projector_progress["sector_rank_summary"]["H"]["basis_count"] == 1,
            "rank_two_zero_cluster_support_is_not_a_restriction_map": True,
        },
        "export_decision": {
            "R_H_exported": False,
            "H_sector_restriction_map_exported": False,
            "B_Huv_or_two_column_lift_exported": False,
            "strict_gate_passes": False,
            "reason": "The selected rank-2 End0/HYM lane and compact H-slot values are useful support, but the selected End0-to-sector functor, selected projector promotion, and two-Higgs H_u/H_d^dagger restriction map are not emitted.",
        },
        **clean_flags(),
    }

    compact_witness = {
        "schema": "MTTConstHiggs01H7B1JRejectedCompactHDotDNumericWitness.v1",
        "status": "COMPACT_H_DOTD_NUMERIC_WITNESS_REJECTED_AS_MSOURCE_OR_RH",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-COMPACT-H-DOTD-WITNESS-REJECTION",
        "source": rel(compact_dotd_path),
        "witness_values": {
            "compact_H_dotD_alpha1_matrix": compact_h["dotD_alpha1_matrix"],
            "lower_left_complex_entry_z": complex_to_pair(z),
            "would_be_Hermitian_projection_of_dotD": hermitianized,
            "would_be_Delta_if_promoted": 0.0,
            "would_be_abs_Omega_sq_if_promoted": omega_abs_sq,
            "would_be_s_beta_if_promoted": rejected_s_beta,
        },
        "rejection_checks": {
            "selected_by_mtt": compact_dotd["selected_by_mtt"],
            "selected_dotD_source_verified": compact_h["selected_dotD_source_verified"],
            "alpha1_driver_verified": compact_h["alpha1_driver_verified"],
            "is_dotD_response_not_mass_strain_Hessian": True,
            "is_single_higgs_carrier_not_UV_two_Higgs_lift": compact_h["kind"] == "single_higgs_carrier",
            "Huv_or_Msource_source_emitted": False,
        },
        "promotion_decision": {
            "promote_to_H_response": False,
            "promote_to_R_H": False,
            "promote_to_M_source": False,
            "promote_to_s_beta": False,
            "reason": "The numeric H dotD witness is retained as support only. Hermitianizing an unselected dotD matrix would be an illicit source promotion and would also target the collapsed single-Higgs carrier, not the UV two-Higgs mass/strain block.",
        },
        **clean_flags(),
    }

    gate_validator = {
        "schema": "MTTConstHiggs01H7B1JStrictMSourceGateValidator.v1",
        "status": "STRICT_MSOURCE_GATE_VALIDATOR_FAILS_CURRENT_EXPORT_ATTEMPT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-STRICT-MSOURCE-GATE-VALIDATOR",
        "locked_target": "strict source-owned M_source export feeding H_uv=B_Huv^* M_source B_Huv without measured Higgs/beta/threshold selectors",
        "required_fields": {
            "dynamic_hessian_or_mass_strain_source_owned": dynamic_edge["export_decision"]["H_response_exported"],
            "H_sector_restriction_map_source_owned": hsector_edge["export_decision"]["R_H_exported"],
            "finite_exactness_or_error_certificate": False,
            "not_residual_replay_or_conditional_witness": False,
            "no_observed_selector": True,
            "same_q79_F_m1_branch": True,
        },
        "passes": False,
        "route_results": {
            "H7B1J_A_dynamic_hessian_export": dynamic_edge["export_decision"],
            "H7B1J_B_Hsector_restriction_export": hsector_edge["export_decision"],
            "compact_H_numeric_witness": compact_witness["promotion_decision"],
        },
        "strict_outputs": {
            "H_response": None,
            "R_H": None,
            "M_source": None,
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "superset_strategy": {
            "combining_paths": True,
            "locked_target": "M_source source export",
            "straight_paths_tested": [
                "PSM/C1 dynamic Hessian-source row lineage",
                "selected HYM rank-2 End0 to H-sector routing lineage",
            ],
            "support_paths_retained_without_promotion": [
                "compact H dotD matrix",
                "conditional Route-B validator pass",
                "finite model-active projector values",
                "rank-two T1/T2 Green lane",
            ],
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1JNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1K_PHIFIN_TRACE_OR_END0_HSECTOR_FUNCTOR",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-PHIFIN-MINIMIZER-TRACE-OR-END0-HSECTOR-FUNCTOR",
            "task": "Emit a selected Phi_fin minimizer trace/full HYM-Strominger operator packet that promotes finite projectors and End0-to-sector values, or emit an independent selected Higgs H_uv Hessian/restriction table with exactness.",
        },
        "two_legal_exits": [
            {
                "id": "H7B1K-A",
                "label": "Phi_fin/full operator promotion",
                "must_emit": "selected minimizer trace or full HYM/Strominger operator values promoting P_s, K_s, rho_s, sector dotD, and H-sector restriction values",
            },
            {
                "id": "H7B1K-B",
                "label": "independent Higgs Huv Hessian/restriction table",
                "must_emit": "source-owned H_response and R_H entries for the UV two-Higgs H_u/H_d^dagger block with exactness/error certificate",
            },
        ],
        "do_not_repeat": [
            "Do not hermitianize compact H dotD and call it M_source.",
            "Do not promote conditional Route-B C1 validator success as unpatched Hessian source emission.",
            "Do not promote finite projector values until Phi_fin/full-operator source flags are true.",
            "Do not backsolve from Higgs mass, lambda_H, beta, or threshold residual.",
        ],
        **clean_flags(),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1JDynamicHessianOrHSectorRestrictionExport",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-DYNAMIC-HESSIAN-OR-HSECTOR-RESTRICTION-EXPORT",
        "output_packets": {
            "dynamic_hessian_edge_export_attempt": rel(DYNAMIC_EDGE),
            "hsector_restriction_edge_export_attempt": rel(HSECTOR_EDGE),
            "rejected_compact_h_dotd_numeric_witness": rel(COMPACT_WITNESS),
            "strict_msource_gate_validator": rel(GATE_VALIDATOR),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "H7B1JTwoEdgeMSourceGateAttemptTheorem",
            "proved": True,
            "statement": (
                "The strongest current dynamic-Hessian edge and H-sector-restriction edge do not yet pass the strict M_source gate. "
                "The PSM/C1 row lineage contains exact conditional Hessian support but remains replay/conditional rather than unpatched source emission. "
                "The HYM rank-2 End0 lineage contains a selected diagonal first solve and compact H dotD support, but the End0-to-sector/H-sector restriction values and selected projector promotion remain open. "
                "Therefore H7B1J records a two-edge gate attempt, rejects the compact H dotD shortcut, and reduces the next gate to Phi_fin/full-operator promotion or an independent Higgs Huv Hessian/restriction table."
            ),
        },
        "H7B1I_gate_imported": h7b1i["M_source_acceptance_functor_built"],
        "dynamic_hessian_edge_attempted": True,
        "hsector_restriction_edge_attempted": True,
        "compact_H_numeric_witness_emitted_support_only": True,
        "conditional_RouteB_validator_passes_support_only": psm_c1_06["closure_decision"]["conditional_RouteB_validator_passes"],
        "selected_HYM_rank2_first_solve_imported": hym_first["closure_decision"]["selected_diagonal_HYM_first_solve_closed"],
        "strict_msource_gate_passes": False,
        "H_response_exported": False,
        "R_H_exported": False,
        "M_source_value_emitted": False,
        "B_Huv_value_emitted": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1K_PhiFinMinimizerTraceOrEnd0HSectorFunctor_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1J_DynamicHessianOrHSectorRestrictionExport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "dynamic_hessian_edge_attempted": True,
        "hsector_restriction_edge_attempted": True,
        "compact_H_numeric_witness_emitted_support_only": True,
        "strict_msource_gate_passes": False,
        "H_response_exported": False,
        "R_H_exported": False,
        "M_source_value_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1J Dynamic Hessian Or H-Sector Restriction Export v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1J-DYNAMIC-HESSIAN-OR-HSECTOR-RESTRICTION-EXPORT`

## Result

```text
dynamic Hessian edge attempted            True
H-sector restriction edge attempted       True
compact H numeric witness retained        support only
conditional Route-B validator             support only
selected HYM rank-2 first solve imported  True
strict M_source gate passes               False
H_response / R_H / M_source emitted       False
Huv / Omega / s_beta / lambda_H           False
```

## What We Learned

The C1/Hessian lineage has exact conditional support:

```text
A^T A = 12 I_2
A^T b = (12, 12)
||b||^2 = 24
deltaTheta_C1 = (1, 1)
```

But this is still not unpatched source emission and it is not a selected Higgs
`H_uv` mass/strain Hessian.

The HYM rank-2/End0 lane is also real progress: it emits the selected diagonal
first solve and the `T1/T2` covariant Green lane.  However the selected
End0-to-sector/H-sector restriction values and projector promotion remain open.

## Rejected Shortcut

The compact H-sector dotD witness contains a numeric offdiagonal value, but it
has `selected_dotD_source_verified=false`, `alpha1_driver_verified=false`, and
`selected_by_mtt=false`.  Hermitianizing it would be an illicit source
promotion and would still target the collapsed single-Higgs carrier, not the UV
two-Higgs `H_u/H_d^dagger` mass/strain block.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1K-PHIFIN-MINIMIZER-TRACE-OR-END0-HSECTOR-FUNCTOR`
"""

    for path, payload in [
        (DYNAMIC_EDGE, dynamic_edge),
        (HSECTOR_EDGE, hsector_edge),
        (COMPACT_WITNESS, compact_witness),
        (GATE_VALIDATOR, gate_validator),
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
