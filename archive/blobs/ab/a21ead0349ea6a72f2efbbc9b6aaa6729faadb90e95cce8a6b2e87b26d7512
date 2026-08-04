"""Audit Step 12 pre-residual source-ownership clause proof ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step12_preresidualsourceownership_or_newrowsourceids"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PLAN_POSITION = PACKET_DIR / "step12_plan_position.packet.json"
NORMAL_FORM = PACKET_DIR / "step12_preresidual_normal_form_and_source_test.packet.json"
KERNEL_REDUCTION = PACKET_DIR / "step12_source_owner_kernel_reduction.packet.json"
NEW_ROWS = PACKET_DIR / "step12_new_row_source_ids_attempt.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step12_to_step13_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step12_PreResidualSourceOwnershipClauseProof_or_NewRowSourceEmission_v1.md"

STATUS = (
    "MTT_SELECTED_STEP12_PRERESIDUALSOURCEOWNERSHIP_OR_NEWROWSOURCEIDS_"
    "CLOSED_NORMAL_FORM_SOURCE_TEST_ACTIONKERNEL_OPEN"
)
NEXT = "MTT_Selected_Step13_PhysicalActionKernelFields_or_IndependentRowSourceIDs_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    plan = load(PLAN_POSITION)
    normal = load(NORMAL_FORM)
    kernel = load(KERNEL_REDUCTION)
    rows = load(NEW_ROWS)
    workorder = load(NEXT_WORKORDER)
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
    guard(plan, errors, "plan", closure=True)
    guard(normal, errors, "normal form", closure=True)
    guard(kernel, errors, "kernel reduction", closure=True)
    guard(rows, errors, "new rows", closure=True)
    guard(workorder, errors, "workorder", closure=False)

    expect(plan.get("active_step") == 12, "active step mismatch", errors)
    expect(plan.get("active_target", {}).get("primary") == "prove source ownership of pre-residual R_Z/R_X variation operators", "active primary target mismatch", errors)
    for step in ["step13", "step14", "step15", "step16"]:
        expect(step in plan.get("remaining_steps_after_12", {}), f"remaining step missing: {step}", errors)

    expect(normal.get("source_level_weyl_carrier_selected") is True, "Weyl carrier not selected", errors)
    expect(normal.get("static_source_selector_selected") is True, "static source selector missing", errors)
    expect(normal.get("R_Z", {}).get("coefficient_count") == 6, "R_Z coefficient count mismatch", errors)
    expect(normal.get("R_X", {}).get("coefficient_count") == 3, "R_X coefficient count mismatch", errors)
    expect(abs(normal.get("R_Z", {}).get("norm_sq") - 4.0) < 1e-12, "R_Z norm mismatch", errors)
    expect(abs(normal.get("R_X", {}).get("norm_sq") - 2.0) < 1e-12, "R_X norm mismatch", errors)
    expect(normal.get("R_Z", {}).get("reconstruction_error_norm_sq") < 1e-24, "R_Z reconstruction too large", errors)
    expect(normal.get("R_X", {}).get("reconstruction_error_norm_sq") < 1e-24, "R_X reconstruction too large", errors)
    expect(normal.get("operator_discovery_problem_closed") is True, "operator discovery not closed", errors)
    expect(normal.get("pre_residual_source_ordering_normal_form_closed") is True, "normal form not closed", errors)
    expect(normal.get("residual_projector_replay_used_as_source") is False, "residual replay used as source", errors)
    for key in [
        "physical_action_equals_c1_defect_functional",
        "physical_boundary_source_terms_vanish",
        "same_source_rz_rx_bselected_emitted",
        "physical_selection_validator_passes",
        "pre_residual_RZ_RX_source_ownership_closed",
    ]:
        expect(normal.get(key) is False, f"normal form overclosed: {key}", errors)

    expect(kernel.get("source_kernel_current_validator_returncode") == 1, "source kernel validator should reject", errors)
    expect(
        set(kernel.get("source_kernel_missing_fields", []))
        == {"selected_variation_functional", "same_source_hessian", "sector_functor", "independence_certificate"},
        "source kernel missing fields mismatch",
        errors,
    )
    expect(kernel.get("routec_validator_ok") is False, "Route C validator overaccepted", errors)
    conditional = kernel.get("routec_conditional_witness_if_principle_inserted_or_derived", {})
    for key in ["selected_variation_functional", "same_source_hessian", "sector_functor", "independence_certificate"]:
        expect(conditional.get(key) is True, f"conditional witness missing: {key}", errors)
        expect(kernel.get(f"{key}_proved_now") is False, f"kernel field overproved: {key}", errors)
    expect(kernel.get("source_owner_kernel_proved_now") is False, "source owner kernel overproved", errors)
    expect(kernel.get("dynamic_owner_closed_fields", {}).get("admissible_c1_variation_space") is True, "dynamic owner variation space missing", errors)
    expect(kernel.get("dynamic_owner_closed_fields", {}).get("source_owner_id") is True, "dynamic owner id missing", errors)
    expect(kernel.get("dynamic_owner_closed_fields", {}).get("independence_guard") is True, "dynamic owner independence guard missing", errors)
    for key in ["phase_R_Z_source", "shift_R_X_source", "b_selected_source", "sector_row_assembly"]:
        expect(kernel.get("dynamic_owner_open_fields", {}).get(key) is False, f"dynamic owner field overclosed: {key}", errors)

    expect(rows.get("independent_connection_export_schema_built") is True, "connection export schema missing", errors)
    expect(rows.get("connection_export_tables_present_count") == 5, "connection table count mismatch", errors)
    expect(rows.get("new_independent_110_row_source_export_emitted") is False, "new 110-row export overemitted", errors)
    expect(rows.get("new_row_source_ids_emitted") is False, "new row source ids overemitted", errors)

    expect(workorder.get("completed_step") == 12, "workorder completed step mismatch", errors)
    expect(workorder.get("next_step") == 13, "workorder next step mismatch", errors)
    expect(workorder.get("next_required_artifact") == NEXT, "workorder next mismatch", errors)
    for key in [
        "derive_selected_variation_functional",
        "derive_physical_action_equals_c1_defect_functional",
        "derive_physical_boundary_source_vanishing",
        "emit_independent_row_source_ids",
    ]:
        expect(workorder.get("step13_must_close_one_of", {}).get(key) is True, f"Step 13 target missing: {key}", errors)
    for key in [
        "RZ_RX_normal_form_discovery",
        "exact_72_row_value_replay",
        "shape_routing_as_source_selection",
        "premise_free_symbolic_source_stack_as_final_theorem",
    ]:
        expect(workorder.get("step13_must_not_repeat", {}).get(key) is True, f"anti-repeat missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(workorder.get("must_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    for key in [
        "step12_closed_for_plan_contract",
        "RZ_RX_operator_discovery_closed",
        "pre_residual_normal_form_closed",
    ]:
        expect(decision.get(key) is True, f"candidate closed field missing: {key}", errors)
    for key in [
        "residual_projector_replay_used_as_source",
        "pre_residual_RZ_RX_source_ownership_closed",
        "selected_variation_functional_proved_now",
        "same_source_hessian_b_proved_now",
        "sector_functor_proved_now",
        "independence_certificate_proved_now",
        "new_independent_110_row_source_export_emitted",
        "SelectedFiniteC1SourceIdentityTheorem_proved",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(data.get("step12_contract_closure_claimed") is True, "candidate Step 12 claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM overclaim", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob overclaim", errors)

    expect(cert.get("RZ_RX_operator_discovery_closed") is True, "certificate discovery closure missing", errors)
    expect(cert.get("pre_residual_normal_form_closed") is True, "certificate normal form missing", errors)
    expect(cert.get("pre_residual_RZ_RX_source_ownership_closed") is False, "certificate source ownership overclosed", errors)
    expect(cert.get("SelectedFiniteC1SourceIdentityTheorem_proved") is False, "certificate theorem overproved", errors)

    expect("Step 12   : current pre-residual source-ownership reduction" in note, "note missing Step 12 plan", errors)
    expect("pre-residual R_Z/R_X source ownership    : false" in note, "note missing source ownership guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 12 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 12 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
