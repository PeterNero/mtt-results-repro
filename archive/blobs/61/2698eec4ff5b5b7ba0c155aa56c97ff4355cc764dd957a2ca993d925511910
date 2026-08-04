"""Audit dynamic C1 value-emission attempt / honest Galerkin C1 run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
LANE_A = PACKET_DIR / "lane_a_same_source_value_emission_attempt.packet.json"
LANE_B = PACKET_DIR / "lane_b_honest_galerkin_c1_run_attempt.packet.json"
CUTSET = PACKET_DIR / "strict_value_emission_cutset.packet.json"
CERT = ROOT / "certificates" / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1TransferTensor_ValueEmission_or_HonestGalerkinC1Run_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.py"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERTENSOR_VALUEEMISSION_OR_HONESTGALERKINC1RUN_ATTEMPTED_EXISTING_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    lane_a = load(LANE_A)
    lane_b = load(LANE_B)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(lane_a["status"] == "LANE_A_SAME_SOURCE_DYNAMIC_VALUE_EMISSION_ATTEMPTED_VALUES_OPEN", "lane A status mismatch")
    support = lane_a["closed_support_available"]
    for key in [
        "static_operator_alpha1_support_closed",
        "conditional_transfer_tensor_normal_form_built",
        "transport_only_zero_lane_rejected",
        "stationary_trace_layer_promoted",
        "alpha1_dotD_driver_attached_to_differentiated_contract",
        "linear_algebra_obstruction_removed",
    ]:
        require(support[key] is True, f"lane A support not closed: {key}")
    checked = lane_a["existing_value_sources_checked"]
    require(checked["conditional_tensor_is_reference_not_promotion"]["operator_is_A_selected"] is False, "conditional A overpromoted")
    require(checked["conditional_tensor_is_reference_not_promotion"]["source_vector_is_b_selected"] is False, "conditional b overpromoted")
    for key in [
        "PhiFinC1_identity_promoted_now",
        "primitive_overlap_contractions_promoted",
        "selected_Hessian_bselected_emitted",
        "selected_dynamic_transfer_identity_emitted",
        "current_layer_promoted_as_dynamic_overlap_tensor",
        "current_layer_promoted_as_A_selected",
        "current_layer_promoted_as_b_selected",
    ]:
        require(checked[key] is False, f"lane A value overpromoted: {key}")
    normal = lane_a["conditional_values_preserved_only_as_if_promoted_reference"]
    require(normal["rank"] == 2, "conditional rank mismatch")
    require(abs(normal["condition_number"] - 1.0) <= 1e-12, "conditional condition mismatch")
    require(normal["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional Gram mismatch")
    require(normal["A_transpose_b"] == [12.0, 12.0], "conditional ATb mismatch")
    require(normal["deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")
    require(len(lane_a["missing_for_promotion"]) == 5, "lane A missing list mismatch")
    require(lane_a["can_promote_A_selected_b_selected_deltaTheta_now"] is False, "lane A overpromoted")

    require(lane_b["status"] == "LANE_B_HONEST_GALERKIN_C1_RUN_ATTEMPTED_VALUES_OPEN", "lane B status mismatch")
    require(lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin manifest status mismatch")
    require(lane_b["selected_source_verified"] is False, "Galerkin source oververified")
    require(lane_b["currently_closed"] is False, "Galerkin lane overclosed")
    require(lane_b["can_promote_honest_Galerkin_C1_values_now"] is False, "Galerkin values overpromoted")
    require(lane_b["must_emit_same_coordinate_target"]["total_real_coordinates"] == 72, "Galerkin target dimension mismatch")

    require(cutset["status"] == "STRICT_VALUE_EMISSION_CUTSET_IDENTIFIED_EXISTING_VALUES_OPEN", "cutset status mismatch")
    target = cutset["acceptance_target"]
    for key in [
        "A_selected_72_real_columns_required",
        "b_selected_72_real_source_vector_required",
        "deltaTheta_C1_must_be_solved_from_selected_values",
        "sector_response_matrices_required",
    ]:
        require(target[key] is True, f"target flag missing: {key}")
    facts = cutset["closed_numeric_facts"]
    require(facts["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "cutset ATA mismatch")
    require(facts["A_transpose_b"] == [12.0, 12.0], "cutset ATb mismatch")
    require(facts["deltaTheta_C1"] == [1.0, 1.0], "cutset delta mismatch")
    for key in [
        "A_transpose_A_equals_12I2",
        "A_transpose_b_equals_12_12",
        "deltaTheta_equals_1_1",
        "rank_2_condition_number_1",
    ]:
        require(facts[key] is True, f"closed numeric fact missing: {key}")
    fields = cutset["field_status"]
    require(fields["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "A status mismatch")
    require(fields["b_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "b status mismatch")
    require(fields["deltaTheta_C1"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "delta status mismatch")
    require(fields["sector_response_matrices"] == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE", "sector matrix status mismatch")
    for key in [
        "static_Weyl_pair_source_provenance",
        "stationary_projector_Riesz_Green_support",
        "alpha1_dotD_driver_support",
        "fixed_72_real_coordinate_manifest",
        "rank_2_condition_number_1_conditional_linear_algebra",
        "transport_only_zero_lane_rejection",
    ]:
        require(cutset["closed_not_blockers"][key] is True, f"closed-not-blocker missing: {key}")
    exhausted = cutset["current_acceptance_sources_exhausted"]
    for key in [
        "lane_A_same_source_dynamic_transfer_checked",
        "lane_B_honest_Galerkin_C1_checked",
        "no_current_packet_satisfies_strict_acceptance",
    ]:
        require(exhausted[key] is True, f"exhaustion flag missing: {key}")
    require(cutset["promotion_allowed_now"] is False, "cutset overpromoted")

    for key in [
        "strict_acceptance_target_replayed",
        "lane_A_existing_sources_checked_against_acceptance",
        "lane_B_existing_galerkin_manifest_checked_against_acceptance",
        "closed_support_separated_from_value_emission",
        "minimal_dynamic_value_cutset_identified",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_differentiated_PhiFinC1_source_map",
        "selected_primitive_C1_overlap_contractions",
        "selected_Hessian_or_b_source_vector",
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
    require(decision["value_emission_attempt_completed"] is True, "attempt flag missing")
    for key in [
        "lane_A_same_source_dynamic_transfer_promoted",
        "lane_B_honest_Galerkin_C1_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "sector_response_matrices_claimed",
        "honest_Galerkin_C1_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("remaining object is sharply identified" in note, "note missing cutset explanation")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
