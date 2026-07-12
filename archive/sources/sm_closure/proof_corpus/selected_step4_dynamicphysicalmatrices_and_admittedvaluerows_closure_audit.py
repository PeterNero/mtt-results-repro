"""Audit Step 4 dynamic-matrix and admitted-value-row closure boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step4_dynamicphysicalmatrices_and_admittedvaluerows_closure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DYNAMIC = PACKET_DIR / "step4_dynamic_physical_matrix_contract.packet.json"
VALUES = PACKET_DIR / "step4_admitted_value_row_contract.packet.json"
BOUNDARY = PACKET_DIR / "step4_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step4_to_step5_handoff.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step4_DynamicPhysicalMatrices_and_AdmittedValueRows_Closure_v1.md"

STATUS = (
    "MTT_SELECTED_STEP4_DYNAMICPHYSICALMATRICES_AND_ADMITTEDVALUEROWS_CLOSURE_"
    "CLOSED_ADMITTED_REPLAY_INTERNAL_NOKNOB_HANDOFF"
)
NEXT = "MTT_Selected_Step5_NoKnobMinimalKnobAudit_or_InternalScalarRowsExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    dynamic = load(DYNAMIC)
    values = load(VALUES)
    boundary = load(BOUNDARY)
    handoff = load(HANDOFF)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(dynamic, errors, "dynamic contract", closure=True)
    guard(values, errors, "value contract", closure=True)
    guard(boundary, errors, "boundary", closure=False)
    guard(handoff, errors, "handoff", closure=False)

    for key in [
        "stale_phifin_matter_slot_blockers_retired_by_later_u10_artifact",
        "static_matter_slot_source_closed",
        "dynamic_frontier_reduced_after_static_sector_closure",
        "same_source_dynamic_matter_overlap_packet_closed",
        "selected_dynamic_overlap_tensor_promoted",
        "selected_A_selected_b_selected_preserved",
        "dynamic_QaSU3_first_response_layer_closed",
        "VSD01_source_assembly_subgate_closed",
        "VSD01_dynamic_overlap_subgate_closed",
        "physical_PhiFinC1_action_source",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "formal_110_row_assembly",
        "all_72_primitive_rows_exact",
        "dynamic_physical_matrix_contract_closed",
    ]:
        expect(dynamic.get(key) is True, f"dynamic contract missing: {key}", errors)

    for key in [
        "external_import_lane_closed_at_admitted_replay_tier",
        "accepted_diagonal_profile_theorem_closed",
        "kernel_readiness",
        "admitted_value_row_contract_closed",
    ]:
        expect(values.get(key) is True, f"value contract missing: {key}", errors)
    expect(values.get("accepted_external_threshold_row_count") == 7, "threshold row count mismatch", errors)
    expect(values.get("accepted_external_mass_scheme_row_count") == 3, "mass row count mismatch", errors)
    expect(values.get("internal_selected_Rtheta_value_row_emitted") is False, "internal Rtheta row overemitted", errors)
    expect(values.get("accepted_internal_scalar_row_count") == 0, "internal scalar rows overaccepted", errors)
    expect(values.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    expect(values.get("kernel_readiness_fraction") == "8/9", "kernel readiness mismatch", errors)
    expect(values.get("selected_universal_parameter_count") == 0, "universal parameter overselected", errors)
    expect(values.get("internal_no_knob_value_rows_closed") is False, "internal no-knob overclosed", errors)

    expect(boundary.get("step4_closed_for_plan_contract") is True, "Step 4 plan contract not closed", errors)
    expect(boundary.get("step4_dynamic_physical_matrices_closed") is True, "Step 4 dynamic matrices not closed", errors)
    expect(boundary.get("step4_accepted_admitted_value_rows_closed") is True, "Step 4 admitted rows not closed", errors)
    for key in [
        "step4_internal_no_knob_value_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(boundary.get(key) is False, f"boundary overclosed: {key}", errors)

    expect(handoff.get("completed_step") == 4, "handoff completed step mismatch", errors)
    expect(handoff.get("next_step") == 5, "handoff next step mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    for key in [
        "internal_Rtheta_scalar_rows",
        "lambda_H_row",
        "accepted_Yukawa_magnitudes",
        "CKM_PMNS_value_closure",
        "candidate_specific_universal_source_anchor",
        "minimal_knob_policy_if_no_internal_derivation",
    ]:
        expect(handoff.get("step5_live_questions", {}).get(key) is True, f"Step 5 live question missing: {key}", errors)
    for key in [
        "Phi_fin_transport_replay",
        "static_U10_Ubar5_1M_matter_slot_readout",
        "A_selected_b_selected_deltaTheta_C1_first_response",
        "post_pi_admitted_external_threshold_mass_scheme_rows",
    ]:
        expect(handoff.get("do_not_reopen_as_step4_blockers", {}).get(key) is True, f"do-not-reopen flag missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step4_closed_for_plan_contract") is True, "candidate Step 4 closure missing", errors)
    expect(decision.get("step4_dynamic_physical_matrices_closed") is True, "candidate dynamic closure missing", errors)
    expect(decision.get("step4_accepted_admitted_value_rows_closed") is True, "candidate admitted rows missing", errors)
    expect(decision.get("step4_internal_no_knob_value_rows_closed") is False, "candidate internal no-knob overclosed", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "candidate internal scalars overaccepted", errors)
    expect(decision.get("accepted_external_threshold_row_count") == 7, "candidate threshold count mismatch", errors)
    expect(decision.get("accepted_external_mass_scheme_row_count") == 3, "candidate mass count mismatch", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "candidate true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "candidate no-knob overclosed", errors)
    expect(data.get("step4_contract_closure_claimed") is True, "candidate Step 4 local claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM claim overclosed", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate full no-knob claim overclosed", errors)

    expect(cert.get("step4_contract_closure_claimed") is True, "certificate Step 4 local claim missing", errors)
    expect(cert.get("step4_internal_no_knob_value_rows_closed") is False, "certificate internal no-knob overclosed", errors)
    expect("Step 4 is closed at the plan-contract tier" in note, "note missing Step 4 closure", errors)
    expect("internal no-knob value rows closed      : false" in note, "note missing no-knob guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 4 closure audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 4 closure audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
