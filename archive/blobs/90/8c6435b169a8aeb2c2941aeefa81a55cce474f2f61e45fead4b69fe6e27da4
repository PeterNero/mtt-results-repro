"""Audit selected dynamic C1 transfer tensor / Galerkin C1 values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_dynamicc1transfertensor_or_galerkinc1values"
SUPPORT = PACKET_DIR / "closed_dynamic_operator_support.packet.json"
TENSOR = PACKET_DIR / "conditional_dynamic_c1_transfer_tensor.packet.json"
FRONTIER = PACKET_DIR / "primitive_tensor_or_galerkin_frontier.packet.json"
CERT = ROOT / "certificates" / "selected_dynamicc1transfertensor_or_galerkinc1values_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicc1transfertensor_or_galerkinc1values.py"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERTENSOR_OR_GALERKINC1VALUES_BUILT_OPERATOR_ALPHA1_CLOSED_PRIMITIVE_TENSOR_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    support = load(SUPPORT)
    tensor = load(TENSOR)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(support["closed_for_frontier"] is True, "operator/alpha1 support not closed")
    static = support["static_source_support"]
    require(static["static_enriched_weylpair_source_provenance_promoted"] is True, "static source not promoted")
    require(static["phase_Z_to"] == ["u", "e"], "phase route mismatch")
    require(static["shift_X_to"] == ["d", "nuD"], "shift route mismatch")
    stationary = support["stationary_operator_support"]
    for key in [
        "selected_projector_source_verified",
        "selected_riesz_green_source_verified",
        "selected_rho_s_validator_ready",
        "selected_source_verified",
        "functional_gauge_transported_trace_proved",
        "symbolic_transport_conjugation_validator_extended",
    ]:
        require(stationary[key] is True, f"stationary support missing: {key}")
    alpha1 = support["alpha1_dotD_support"]
    for key in [
        "alpha1_driver_verified_imported",
        "selected_dotD_source_verified_imported",
        "honest_dotD_alpha1_replay",
        "du_dalpha1_equals_h_ext",
        "attached_to_differentiated_contract_as_driver",
    ]:
        require(alpha1[key] is True, f"alpha1 support missing: {key}")
    require(alpha1["primitive_overlap_values_emitted_by_driver"] is False, "driver overemits primitive values")

    require(tensor["status"] == "CONDITIONAL_TENSOR_NORMAL_FORM_BUILT_NOT_SELECTED", "tensor status mismatch")
    require(tensor["codomain"]["real_dimension"] == 72, "tensor codomain mismatch")
    require(tensor["normal_form_replay"]["rank"] == 2, "rank mismatch")
    require(tensor["normal_form_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(tensor["normal_form_replay"]["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(tensor["normal_form_replay"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    selection = tensor["selection_status"]
    require(selection["conditional_tensor_built"] is True, "conditional tensor not built")
    for key in [
        "selected_dynamic_C1_transfer_tensor_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
    ]:
        require(selection[key] is False, f"tensor overpromoted: {key}")

    require(frontier["transport_only_lane_rejected"] is True, "transport-only lane not rejected")
    require(frontier["transport_only_zero_matrices"] is True, "transport-only zero evidence missing")
    require(frontier["canonical_tensor_selected_by_theorem"] is False, "canonical tensor overselected")
    for route in [
        "route_A_selected_noninvariant_primitive_tensor",
        "route_B_selected_Hessian_or_b_source_vector",
        "route_C_honest_Galerkin_C1_values",
    ]:
        require(frontier["remaining_value_routes"][route]["currently_emitted"] is False, f"route overemitted: {route}")

    for key in [
        "static_source_provenance_retained_closed",
        "stationary_projector_riesz_green_support_retained_closed",
        "alpha1_dotD_driver_retained_closed",
        "transport_only_zero_lane_rejected",
        "conditional_dynamic_C1_transfer_tensor_normal_form_built",
        "dynamic_frontier_reduced_to_primitive_tensor_Hessian_or_Galerkin_values",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_noninvariant_primitive_C1_tensor",
        "selected_primitive_C1_overlap_contractions",
        "selected_Hessian_or_b_source_vector",
        "honest_selected_Galerkin_C1_values",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    require(decision["operator_alpha1_support_closed_for_frontier"] is True, "support decision mismatch")
    for key in [
        "conditional_dynamic_C1_transfer_tensor_selected",
        "selected_noninvariant_primitive_C1_tensor_promoted",
        "selected_Hessian_or_b_source_vector_promoted",
        "honest_Galerkin_C1_values_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "SM_parity_dynamic_packet_closure_claimed",
        "true_SM_equivalence_claimed",
        "no_knob_closure_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
    ]:
        require(data[key] is False, f"candidate overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("The live frontier is now only value emission" in note, "note missing frontier")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
