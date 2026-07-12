"""Import visible-operator and Hessian/kernel frontier reductions."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "s3_source_certificate_and_qa_alignment_import_certificate.json"
VISIBLE_GS = SM / "candidate_data" / "selected_visible_green_schwarz_operator_source.candidate.json"
VISIBLE_CW = SM / "candidate_data" / "selected_visible_chern_weil_operator_source.candidate.json"
ROUTEC = SM / "candidate_data" / "selected_routec_hym_operator_pipeline.candidate.json"
QA_REQUEST = QA / "candidate_data" / "central_cocycle_map_source_augmentation_request.candidate.json"
QA_SEARCH = QA / "candidate_data" / "central_cocycle_map_source_search_or_derivation.candidate.json"
QA_INTERFACE = QA / "candidate_data" / "hessian_kernel_central_cocycle_derivation_interface.candidate.json"
QA_FILL = QA / "candidate_data" / "hessian_kernel_central_cocycle_fill_attempt.candidate.json"

OUTPUT_PACKET = DATA / "visible_operator_and_hessian_frontier_import.candidate.json"
OUTPUT_CERT = CERTS / "visible_operator_and_hessian_frontier_import_certificate.json"
OUTPUT_NOTE = CORPUS / "VisibleOperator_and_HessianFrontier_Import_v1.md"

STATUS = "VISIBLE_OPERATOR_HESSIAN_FRONTIER_IMPORTED_SELECTED_VALUES_OPEN"
PREVIOUS_STATUS = "S3_SOURCE_CERTIFICATE_QA_ALIGNMENT_IMPORTED_OPERATOR_RESPONSE_OPEN"
NEXT = "MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Minimal_Hsel_Gret_Source_Request_or_Finite_Galerkin_Candidate_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    visible_gs = load(VISIBLE_GS)
    visible_cw = load(VISIBLE_CW)
    routec = load(ROUTEC)
    qa_request = load(QA_REQUEST)
    qa_search = load(QA_SEARCH)
    qa_interface = load(QA_INTERFACE)
    qa_fill = load(QA_FILL)

    checks = {
        "F0_previous_gate_matches": previous["status"] == PREVIOUS_STATUS,
        "F1_visible_gs_gate_reduces_to_operator_payload": visible_gs["status"]
        == "MTT_SELECTED_VISIBLE_GREEN_SCHWARZ_OPERATOR_SOURCE_GATE_BUILT_OPERATOR_PIPELINE_OPEN"
        and visible_gs["theorem"]["proved"] is True
        and visible_gs["gate_results"]["selected_s3_source_closed"] is True
        and visible_gs["gate_results"]["visible_green_schwarz_curvature_closed"] is True
        and visible_gs["gate_results"]["selected_visible_operator_source_constructed"] is False
        and visible_gs["gate_results"]["selected_D_E_dotD_Riesz_Green_constructed"] is False,
        "F2_visible_cw_reduces_to_same_source_packet": visible_cw["status"]
        == "MTT_SELECTED_VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PACKET"
        and visible_cw["theorem"]["proved"] is True
        and visible_cw["open_gates"]["selected_visible_operator_source_closed"] is False
        and visible_cw["superset_mode"]["primary_path"]["candidate_id"]
        == "rank2_non_split_extension_preferred_L_1_-2_0"
        and visible_cw["superset_mode"]["parallel_repair_path"]["candidate_id"]
        == "direct_route_c_finite_hym_strominger_solve",
        "F3_routec_pipeline_executable_but_unselected": routec["status"]
        == "MTT_SELECTED_ROUTEC_HYM_OPERATOR_PIPELINE_BUILT_SELECTED_VALUES_OPEN"
        and routec["theorem"]["proved"] is True
        and routec["gate_results"]["route_c_scaffold_built"] is True
        and routec["gate_results"]["honest_mesh_metric_sector_pass"] is True
        and routec["gate_results"]["lifted_selected_flags_pipeline_pass"] is True
        and routec["gate_results"]["honest_operator_pipeline_pass"] is False
        and routec["gate_results"]["selected_source_verified"] is False
        and routec["gate_results"]["actual_selected_D_E_dotD_Riesz_Green_supplied"] is False,
        "F4_qa_request_and_search_reduce_to_hessian_kernel": qa_request["status"]
        == "QA_SU3_CENTRAL_COCYCLE_MAP_SOURCE_AUGMENTATION_REQUEST_BUILT_VALUES_OPEN"
        and qa_request["current_result"]["request_built"] is True
        and qa_search["status"]
        == "QA_SU3_CENTRAL_COCYCLE_MAP_SOURCE_SEARCH_DONE_DERIVATION_GATE_BUILT_VALUES_OPEN"
        and qa_search["source_search_result"]["same_branch_hessian_language_found"] is True
        and qa_search["source_search_result"]["actual_selected_H_sel_found"] is False
        and qa_search["source_search_result"]["actual_retarded_kernel_found"] is False
        and qa_search["source_search_result"]["response_payload_found"] is False,
        "F5_qa_hessian_interface_and_fill_blocked_at_selected_values": qa_interface["status"]
        == "QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_DERIVATION_INTERFACE_BUILT_VALUES_OPEN"
        and qa_interface["interface_checks"]["requires_H_sel"] is True
        and qa_interface["interface_checks"]["requires_G_ret"] is True
        and qa_fill["status"]
        == "QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_FILL_ATTEMPT_PARTIAL_TAU_BLOCKED_SELECTED_HESSIAN_KERNEL"
        and qa_fill["fill_result"]["algebraic_Pi_tw_rule_filled"] is True
        and qa_fill["fill_result"]["tau_twist_cancellation_passes"] is True
        and qa_fill["fill_result"]["selected_Qa_SU3_H_sel_matrix_found"] is False
        and qa_fill["fill_result"]["selected_Qa_SU3_G_ret_found"] is False
        and qa_fill["fill_result"]["same_source_response_payload_filled"] is False,
        "F6_no_target_or_closure_overclaim": visible_gs["target_fitting_used"] is False
        and visible_cw["target_fitting_used"] is False
        and routec["target_fitting_used"] is False
        and qa_fill["target_fitting_used"] is False
        and qa_request["closure_claimed"] is False
        and qa_search["closure_claimed"] is False
        and qa_interface["closure_claimed"] is False
        and qa_fill["closure_claimed"] is False,
    }

    return {
        "packet": "VisibleOperator_and_HessianFrontier_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "visible_gs_operator_gate": str(VISIBLE_GS),
            "visible_cw_operator_reduction": str(VISIBLE_CW),
            "routec_hym_pipeline": str(ROUTEC),
            "qa_central_cocycle_request": str(QA_REQUEST),
            "qa_central_cocycle_search": str(QA_SEARCH),
            "qa_hessian_interface": str(QA_INTERFACE),
            "qa_hessian_fill_attempt": str(QA_FILL),
        },
        "theorem": {
            "name": "VisibleOperatorHessianFrontierImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected S3 source and visible Green-Schwarz curvature close the "
                "old support blockers and reduce the visible proof to one same-source "
                "operator packet. The split abelian path is retired; the primary live "
                "source is the non-split rank-two V_alpha extension, with Route-C/HYM "
                "as executable repair. In parallel, Qa/SU3 central-cocycle promotion "
                "is reduced to actual selected H_sel and G_ret data. Algebraic c-charge "
                "tau typing works, but selected Hessian, retarded kernel, admissibility, "
                "and response payloads remain open."
            ),
        },
        "checks": checks,
        "visible_gs_operator_gate": visible_gs,
        "visible_cw_operator_reduction": visible_cw,
        "routec_hym_pipeline": routec,
        "qa_central_cocycle_request": qa_request,
        "qa_central_cocycle_search": qa_search,
        "qa_hessian_interface": qa_interface,
        "qa_hessian_fill_attempt": qa_fill,
        "what_closes_now": {
            "visible_GS_only_straight_path_rejected": True,
            "same_source_operator_payload_contract_built": True,
            "visible_CW_reduced_to_non_split_rank2_or_routec_packet": True,
            "split_line_or_diagonal_cartan_HYM_retired": True,
            "routec_hym_validator_pipeline_built": True,
            "routec_mesh_metric_sector_algebra_passes_honestly": True,
            "qa_central_cocycle_gap_named": True,
            "qa_hessian_kernel_derivation_interface_built": True,
            "qa_algebraic_c_charge_tau_typing_passes": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_visible_bundle_or_sheaf_operator_source": True,
            "non_split_rank2_Valpha_source_packet": True,
            "selected_HYM_or_RouteC_residual": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_zero_mode_projectors": True,
            "primitive_C1_contractions": True,
            "actual_selected_RouteC_HYM_values": True,
            "qa_selected_H_sel_matrix": True,
            "qa_selected_G_ret_kernel": True,
            "qa_tau_extracted_from_H_sel_G_ret": True,
            "qa_same_source_response_payload": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_visible_operator_source": False,
            "claims_selected_routec_values": False,
            "claims_selected_DE_dotD_Riesz_Green": False,
            "claims_qa_selected_Hsel_Gret": False,
            "claims_qa_response_payload": False,
            "claims_A_selected_or_b_selected": False,
            "uses_lifted_selected_flags_as_proof": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
        "parallel_next_required_artifact": PARALLEL_NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "VisibleOperatorHessianFrontierImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
        "parallel_next_required_artifact": packet["parallel_next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# VisibleOperator and HessianFrontier Import v1

Status: `{cert["status"]}`.

The visible-side problem is now reduced to one same-source operator packet.
The selected S3 source and visible Green-Schwarz curvature are closed support;
the split abelian HYM path is retired; the primary live path is the non-split
rank-two `V_alpha` source, with Route-C/HYM as executable repair.

The QA/SU3 central-cocycle problem is reduced to actual selected `H_sel` and
`G_ret` data.  Algebraic `c`-charge tau typing works, but selected Hessian,
retarded kernel, mapped admissibility, and same-source response payloads are
still open.

No observed masses, CKM/PMNS data, benchmark matrices, or target residuals are
used as selectors.

Next artifact: `{cert["next_required_artifact"]}`.
Parallel QA/SU3 artifact: `{cert["parallel_next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
