"""Audit primitive C1 tensor / Hessian source-map or honest Galerkin gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
SOURCE_MAP = PACKET_DIR / "primitive_tensor_hessian_source_map_candidate.packet.json"
SELECTION_KERNEL = PACKET_DIR / "source_map_selection_obligation_kernel.packet.json"
GALERKIN_PACKET = PACKET_DIR / "honest_galerkin_execution_value_slots.packet.json"
CERT = ROOT / "certificates" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.py"

STATUS = "MTT_SELECTED_PRIMITIVEC1TENSOR_HESSIANSOURCEMAP_OR_HONESTGALERKINC1EXECUTION_BUILT_SOURCE_MAP_CANDIDATE_VALUES_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source_map = load(SOURCE_MAP)
    kernel = load(SELECTION_KERNEL)
    galerkin = load(GALERKIN_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(source_map["status"] == "SOURCE_MAP_CANDIDATE_CONSTRUCTED_SELECTION_OPEN", "source map status mismatch")
    support = source_map["closed_support"]
    require(support["strict_72_real_acceptance_target"]["total_real_coordinates"] == 72, "coordinate target mismatch")
    require(support["selected_source_selector_attached"] is True, "source selector not attached")
    require(support["same_branch_source_required"] is True, "same branch flag missing")
    require(support["canonical_Q_residual_available"] is True, "Q_residual missing")
    require(support["Q_residual_rank"] == 6, "Q_residual rank mismatch")
    require(support["projector_idempotence_verified"] is True, "projector idempotence missing")
    require(support["alpha1_dotD_driver_verified"] is True, "alpha1/dotD not attached")
    require(support["static_trace_transfer_normalization_selected"] is True, "trace normalization missing")

    residuals = source_map["candidate_residual_operators"]
    require(residuals["phase_R_Z"]["selected_by_MTT_now"] is False, "phase residual overselected")
    require(residuals["shift_R_X"]["selected_by_MTT_now"] is False, "shift residual overselected")
    require(residuals["phase_R_Z"]["shape"]["residual_norm_sq"] == 4.0, "phase residual norm mismatch")
    require(residuals["shift_R_X"]["shape"]["residual_norm_sq"] == 2.0, "shift residual norm mismatch")
    replay = source_map["residual_completion_replay"]
    require(replay["phase_projection_plus_residual_equals_target"] is True, "phase replay missing")
    require(replay["shift_projection_plus_residual_equals_target"] is True, "shift replay missing")
    require(replay["routed_72_real_completion"]["conditional_b_norm_sq"] == 24.0, "conditional b norm mismatch")
    if_selected = source_map["if_source_map_selected_then"]
    require(if_selected["rank"] == 2, "if-selected rank mismatch")
    require(if_selected["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "if-selected Gram mismatch")
    require(if_selected["A_transpose_b"] == [12.0, 12.0], "if-selected ATb mismatch")
    require(if_selected["deltaTheta_C1"] == [1.0, 1.0], "if-selected delta mismatch")
    require(source_map["selected_by_MTT_now"] is False, "source map overselected")

    require(kernel["status"] == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN", "kernel status mismatch")
    emitted = kernel["currently_emitted"]
    for key in [
        "selected_A_selected",
        "selected_b_selected",
        "selected_basis_transport_vertex_or_Hessian_values",
        "selected_deltaTheta_C1",
        "selected_differentiated_residual_projector_source_rule",
    ]:
        require(emitted[key] is False, f"emitted field overclaimed: {key}")
    current = kernel["minimal_truth_table"]["current_case"]
    require(current["phase_R_Z_selected"] is False, "truth table phase overselected")
    require(current["shift_R_X_selected"] is False, "truth table shift overselected")
    require(current["b_source_emitted"] is False, "truth table b overemitted")
    require(current["A_selected_promotes"] is False, "truth table A overpromoted")
    require(kernel["strict_acceptance_field_status"]["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "strict A status mismatch")
    require(kernel["strict_acceptance_field_status"]["sector_response_matrices"] == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE", "strict sector matrix status mismatch")

    require(galerkin["status"] == "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN", "Galerkin slot status mismatch")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "Galerkin coordinate mismatch")
    require(galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin manifest mismatch")
    require(galerkin["selected_source_verified"] is False, "Galerkin source oververified")
    require(galerkin["can_replace_source_map_now"] is False, "Galerkin replacement overpromoted")

    for key in [
        "primitive_tensor_Hessian_source_map_candidate_constructed",
        "phase_and_shift_residual_operator_shapes_attached",
        "canonical_Q_residual_support_attached",
        "strict_72_real_acceptance_target_attached",
        "selection_truth_table_built",
        "honest_Galerkin_execution_slots_reemitted",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_phase_R_Z_source",
        "selected_shift_R_X_source",
        "selected_Hessian_or_b_source_vector",
        "selected_primitive_C1_tensor_values",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "selected_sector_response_matrices",
        "honest_selected_Galerkin_C1_execution_values",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    require(decision["source_map_candidate_constructed"] is True, "candidate construct flag missing")
    require(decision["source_map_selected_by_MTT_now"] is False, "source map overpromoted")
    for key in [
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "source_map_selected_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "sector_response_matrices_claimed",
        "honest_Galerkin_C1_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("candidate, not a selected value packet" in note, "note missing source-map guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
