"""Audit visible-operator and Hessian/kernel frontier import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "visible_operator_and_hessian_frontier_import.candidate.json"
CERT = ROOT / "certificates" / "visible_operator_and_hessian_frontier_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "VisibleOperator_and_HessianFrontier_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_visible_operator_and_hessian_frontier.py"

STATUS = "VISIBLE_OPERATOR_HESSIAN_FRONTIER_IMPORTED_SELECTED_VALUES_OPEN"
NEXT = "MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Minimal_Hsel_Gret_Source_Request_or_Finite_Galerkin_Candidate_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["parallel_next_required_artifact"] == PARALLEL_NEXT, "candidate parallel next mismatch")
    require(cert["parallel_next_required_artifact"] == PARALLEL_NEXT, "certificate parallel next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    gs = data["visible_gs_operator_gate"]["gate_results"]
    require(gs["selected_s3_source_closed"] is True, "S3 source not imported closed")
    require(gs["visible_green_schwarz_curvature_closed"] is True, "visible GS curvature not closed")
    require(gs["first_blocking_layer_is_selected_operator_source"] is True, "wrong first blocker")
    for key in [
        "selected_visible_operator_source_constructed",
        "selected_D_E_dotD_Riesz_Green_constructed",
        "coherent_spectral_zero_mode_projectors_constructed",
        "selected_Qa_SU3_packet_closed",
        "sm_parity_closure_claimed",
        "no_knob_closure_claimed",
    ]:
        require(gs[key] is False, f"visible GS overclaimed: {key}")

    cw = data["visible_cw_operator_reduction"]
    require(
        cw["superset_mode"]["primary_path"]["candidate_id"]
        == "rank2_non_split_extension_preferred_L_1_-2_0",
        "wrong visible primary path",
    )
    require(
        cw["superset_mode"]["parallel_repair_path"]["candidate_id"]
        == "direct_route_c_finite_hym_strominger_solve",
        "wrong Route-C repair path",
    )
    require(cw["open_gates"]["selected_visible_operator_source_closed"] is False, "visible source overclosed")

    routec = data["routec_hym_pipeline"]["gate_results"]
    require(routec["route_c_scaffold_built"] is True, "Route-C scaffold missing")
    require(routec["honest_mesh_metric_sector_pass"] is True, "Route-C honest algebra not passing")
    require(routec["lifted_selected_flags_pipeline_pass"] is True, "lifted rehearsal missing")
    for key in [
        "honest_operator_pipeline_pass",
        "selected_source_verified",
        "actual_selected_D_E_dotD_Riesz_Green_supplied",
        "actual_selected_route_c_values_supplied",
        "primitive_C1_contractions_supplied",
        "sm_parity_closure_claimed",
        "no_knob_closure_claimed",
    ]:
        require(routec[key] is False, f"Route-C overclaimed: {key}")

    qa_fill = data["qa_hessian_fill_attempt"]["fill_result"]
    require(qa_fill["algebraic_Pi_tw_rule_filled"] is True, "Pi_tw not filled")
    require(qa_fill["tau_twist_cancellation_passes"] is True, "tau typing does not pass")
    for key in [
        "selected_Qa_SU3_H_sel_matrix_found",
        "selected_Qa_SU3_G_ret_found",
        "tau_extracted_from_H_sel_G_ret",
        "same_source_response_payload_filled",
        "qa_su3_packet_closed",
        "validator_passed",
    ]:
        require(qa_fill[key] is False, f"QA Hessian overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "visible_GS_only_straight_path_rejected",
        "same_source_operator_payload_contract_built",
        "visible_CW_reduced_to_non_split_rank2_or_routec_packet",
        "split_line_or_diagonal_cartan_HYM_retired",
        "routec_hym_validator_pipeline_built",
        "routec_mesh_metric_sector_algebra_passes_honestly",
        "qa_central_cocycle_gap_named",
        "qa_hessian_kernel_derivation_interface_built",
        "qa_algebraic_c_charge_tau_typing_passes",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_visible_operator_source",
        "claims_selected_routec_values",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_qa_selected_Hsel_Gret",
        "claims_qa_response_payload",
        "claims_A_selected_or_b_selected",
        "uses_lifted_selected_flags_as_proof",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("same-source operator packet" in note, "note missing visible frontier")
    require("actual selected `H_sel`" in note, "note missing Hessian frontier")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
