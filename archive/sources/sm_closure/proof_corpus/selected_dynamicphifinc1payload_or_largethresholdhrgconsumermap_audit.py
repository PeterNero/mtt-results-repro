"""Audit dynamic Phi_fin/C1 payload or large-threshold HRG consumer-map packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicPhiFinC1Payload_or_LargeThresholdHRGConsumerMap_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

DYNAMIC_GATE = BASE / "dynamic_phifinc1_final_gate_reconciliation.packet.json"
HRG_CONSUMER = BASE / "large_threshold_hrg_consumer_map_gate.packet.json"
AXIOM_BOUNDARY = BASE / "local_axiom_vs_unpatched_boundary.packet.json"
CUTSET = BASE / "next_cutset_after_dynamic_payload_hrg_consumer.packet.json"

STATUS = (
    "MTT_SELECTED_DYNAMICPHIFINC1PAYLOAD_OR_LARGETHRESHOLDHRGCONSUMERMAP_"
    "RECONCILED_VALUES_READY_SOURCE_RULE_OPEN"
)
NEXT = "MTT_Selected_UnpatchedPhiFinC1SourceRule_or_HonestGalerkinTables_to_HRGConsumerMap_v1"
HRG = 391.39140285811936
REQ_AEW = 391.39140285811936


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    dynamic = load(DYNAMIC_GATE)
    hrg = load(HRG_CONSUMER)
    boundary = load(AXIOM_BOUNDARY)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate theorem closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["theorem"]["name"] == "DynamicPhiFinC1PayloadOrLargeThresholdHRGConsumerMapTheorem", "theorem")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "dynamic_gate_reconciled",
        "alpha1_and_dotd_replay_retired",
        "exact_dynamic_values_ready",
        "local_axiom_conditional_dynamic_C1_closure_available",
        "HRG_consumer_map_gate_built",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "strict_unpatched_dynamic_C1_closed",
        "source_rule_proved_unpatched",
        "honest_galerkin_c1_tables_exported",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
        "typed_HRG_consumer_map_emitted",
        "selected_AEW_large_threshold_transport_available_for_consumer",
        "same_HRG_nonHiggs_prediction_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(abs(nums["computed_HRG_burden"] - HRG) < 1e-12, "computed HRG")
    require(abs(nums["required_A_EW_over_external_A_EW"] - REQ_AEW) < 1e-12, "required A_EW ratio")
    require(nums["required_A_EW_over_external_A_EW_minus_HRG_abs"] == 0.0, "HRG residual")
    require(nums["lambda_replay_residual"] == 0.0, "lambda replay residual")
    require(nums["dynamic_payload_row_count"] == 9, "dynamic row count")
    require(nums["accepted_dynamic_payload_row_count"] == 0, "accepted dynamic row count")
    require(nums["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A")
    require(nums["A_transpose_b"] == [12.0, 12.0], "A^T b")
    require(nums["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta")
    require(nums["rank"] == 2, "rank")
    require(nums["conditional_b_norm_sq"] == 24.0, "b norm")
    require(nums["phase_R_Z_residual_norm_sq"] == 4.0, "phase residual")
    require(nums["shift_R_X_residual_norm_sq"] == 2.0, "shift residual")
    require(nums["total_residual_norm_sq_four_sectors"] == 12.0, "total residual")
    require(nums["lane_B_missing_output_count"] == 4, "Lane B missing count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "dynamic_gate_reconciled",
        "exact_dynamic_values_ready",
        "local_axiom_conditional_dynamic_C1_closure_available",
        "HRG_consumer_map_gate_built",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "strict_unpatched_dynamic_C1_closed",
        "source_rule_proved_unpatched",
        "honest_galerkin_c1_tables_exported",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "typed_HRG_consumer_map_emitted",
        "same_HRG_nonHiggs_prediction_emitted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(dynamic["status"] == "DYNAMIC_PHIFINC1_VALUES_READY_STRICT_SOURCE_RULE_OPEN", "dynamic status")
    require(dynamic["theorem"]["proved"] is True, "dynamic theorem")
    require(dynamic["decision"]["dynamic_gate_reconciled"] is True, "dynamic reconciled")
    require(dynamic["decision"]["alpha1_and_dotd_replay_retired"] is True, "alpha/dotD retired")
    require(dynamic["decision"]["exact_dynamic_values_ready"] is True, "values ready")
    for key in [
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "source_rule_proved_unpatched",
        "honest_galerkin_c1_tables_exported",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
    ]:
        require(dynamic["decision"][key] is False, f"dynamic false {key}")
    require(dynamic["strict_source_status"]["dynamic_values_ready"] is True, "strict values ready")
    require(dynamic["strict_source_status"]["source_rule_proved"] is False, "strict source rule")
    require(dynamic["strict_source_status"]["honest_galerkin_table_exported"] is False, "strict Galerkin")
    require(dynamic["strict_source_status"]["dynamic_payload_rows_accepted"] == 0, "dynamic accepted rows")
    require(dynamic["strict_source_status"]["dynamic_payload_rows_in_inventory"] == 9, "dynamic inventory")
    require(dynamic["exact_values_ready"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "dynamic A^T A")
    require(dynamic["exact_values_ready"]["deltaTheta_C1"] == [1.0, 1.0], "dynamic delta")
    require(dynamic["ready_value_table"]["phase_R_Z"]["selected_now"] is False, "phase selected")
    require(dynamic["ready_value_table"]["shift_R_X"]["selected_now"] is False, "shift selected")
    require(dynamic["ready_value_table"]["phase_R_Z"]["residual_norm_sq"] == 4.0, "phase residual dynamic")
    require(dynamic["ready_value_table"]["shift_R_X"]["residual_norm_sq"] == 2.0, "shift residual dynamic")
    require_no_selector(dynamic, "dynamic")

    require(hrg["status"] == "HRG_CONSUMER_MAP_GATE_TYPED_SOURCE_OPEN", "HRG status")
    require(hrg["theorem"]["proved"] is True, "HRG theorem")
    require(hrg["acceptance_predicate"]["satisfied_now"] is False, "HRG predicate")
    require(abs(hrg["exact_deficit_equalities"]["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG exact")
    require(hrg["exact_deficit_equalities"]["required_A_EW_over_external_A_EW_minus_HRG_abs"] == 0.0, "HRG exact residual")
    for key in [
        "exact_HRG_deficit_locked",
    ]:
        require(hrg["decision"][key] is True, f"HRG true {key}")
    for key in [
        "selected_dynamic_payload_available_for_consumer",
        "selected_AEW_large_threshold_transport_available_for_consumer",
        "typed_HRG_consumer_map_emitted",
        "same_HRG_nonHiggs_prediction_emitted",
        "external_lambda_Mt_used_as_selector",
        "accepted_as_source",
    ]:
        require(hrg["decision"][key] is False, f"HRG false {key}")
    require(hrg["decision"]["accepted_HRG_selector_count"] == 0, "HRG accepted selector count")
    require(hrg["decision"]["accepted_AEW_source_count"] == 0, "HRG accepted A_EW count")
    require_no_selector(hrg, "HRG")

    require(boundary["status"] == "LOCAL_AXIOM_CONDITIONAL_DYNAMIC_C1_CLOSED_UNPATCHED_EXIT_OPEN", "boundary status")
    require(boundary["theorem"]["proved"] is True, "boundary theorem")
    require(boundary["patched_lane"]["local_source_axiom_accepted"] is True, "local axiom accepted")
    require(boundary["patched_lane"]["patched_dynamic_C1_packet_closed"] is True, "patched closed")
    require(boundary["patched_lane"]["scientific_status"] == "axiom-conditional closure", "patched status")
    require(boundary["unpatched_lane"]["unpatched_dynamic_C1_closed"] is False, "unpatched closed")
    require(boundary["unpatched_lane"]["source_rule_derived_unpatched"] is False, "source rule derived")
    require(boundary["unpatched_lane"]["honest_galerkin_table_exported"] is False, "Galerkin exported")
    require(boundary["unpatched_lane"]["lane_A_source_rule_passes_now"] is False, "lane A passes")
    require(boundary["unpatched_lane"]["lane_B_galerkin_passes_now"] is False, "lane B passes")
    require(len(boundary["unpatched_lane"]["lane_B_missing_outputs"]) == 4, "Lane B missing outputs")
    require(boundary["decision"]["local_axiom_conditional_dynamic_C1_closure_available"] is True, "boundary conditional")
    for key in [
        "local_axiom_promoted_to_strict_no_knob",
        "unpatched_source_rule_derived_now",
        "honest_selected_galerkin_tables_exported_now",
        "strict_dynamic_payload_selected_now",
    ]:
        require(boundary["decision"][key] is False, f"boundary false {key}")
    require_no_selector(boundary, "boundary")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_UNPATCHED_PHIFINC1_SOURCE_RULE_OR_GALERKIN_TABLES_TO_HRG_CONSUMER",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "dynamic Phi_fin/C1 final value gate reconciled with exact R_Z/R_X candidate values",
        "local axiom conditional dynamic C1 closure separated from strict unpatched closure",
        "HRG-sized deficit attached to typed consumer-map acceptance predicate",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "derive DifferentiatedPhiFinC1ResidualProjectorApplicationRule unpatched",
        "or export honest selected Galerkin C1 tables in fixed 72-real coordinates",
        "emit typed HRG consumer/source map from selected payload to UP_RET_OVERLAP.HRG",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "Dynamic Payload Gate",
        "dynamic values ready             true",
        "A^T A                            [[12.0, 0.0], [0.0, 12.0]]",
        "local axiom conditional closure  True",
        "HRG Consumer Gate",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: dynamic Phi_fin/C1 values are ready but strict source rule/Galerkin "
        "export and typed HRG consumer map remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
