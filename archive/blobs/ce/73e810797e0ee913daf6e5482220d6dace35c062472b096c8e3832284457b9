"""Audit Step 9 dynamic Qa/SU3/C1 response promotion frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RETIRED_BLOCKERS = PACKET_DIR / "step9_retired_blockers.packet.json"
C1_SUPPORT_LEDGER = PACKET_DIR / "step9_c1_support_ledger.packet.json"
DYNAMIC_ROUTE_TEST = PACKET_DIR / "step9_dynamic_promotion_route_test.packet.json"
PRECISION_STATUS = PACKET_DIR / "step9_precision_profile_status.packet.json"
CLOSURE_BOUNDARY = PACKET_DIR / "step9_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step9_to_step10_handoff.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step9_DynamicQaSU3C1Response_or_PrecisionProfileCompletion_v1.md"

STATUS = (
    "MTT_SELECTED_STEP9_DYNAMICQASU3C1RESPONSE_OR_PRECISIONPROFILECOMPLETION_"
    "CLOSED_FRONTIER_REDUCTION_SOURCE_RULE_OPEN"
)
NEXT = "MTT_Selected_Step10_PhysicalPhiFinC1SourceRule_or_IndependentGalerkinRows_v1"


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
    retired = load(RETIRED_BLOCKERS)
    c1_support = load(C1_SUPPORT_LEDGER)
    route_test = load(DYNAMIC_ROUTE_TEST)
    precision = load(PRECISION_STATUS)
    boundary = load(CLOSURE_BOUNDARY)
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
    guard(retired, errors, "retired blockers", closure=True)
    guard(c1_support, errors, "C1 support", closure=True)
    guard(route_test, errors, "dynamic route test", closure=True)
    guard(precision, errors, "precision status", closure=True)
    guard(boundary, errors, "closure boundary", closure=False)
    guard(handoff, errors, "handoff", closure=False)

    expect(retired.get("step8_closed_for_plan_contract") is True, "Step 8 not imported closed", errors)
    expect(retired.get("all_operator_source_slots_closed") is True, "operator source slots not closed", errors)
    expect(retired.get("operator_source_slots_closed") == 8, "operator slot count mismatch", errors)
    expect(retired.get("operator_source_slots_remaining") == 0, "operator remaining count mismatch", errors)
    for key in [
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "stationary_projector_source_verified",
        "validator_ready_stationary_rho_s",
        "selected_alpha1_driver_imported",
        "selected_dotD_source_verified_imported",
        "postsource_alpha1_retired",
        "static_matter_routing_closed",
        "retired_from_active_step9_blocker_set",
    ]:
        expect(retired.get(key) is True, f"retired blocker missing: {key}", errors)

    expect(
        c1_support.get("current_primitive_class_promoted_as_valid_C1_observable_layer") is True,
        "primitive C1 support layer not promoted",
        errors,
    )
    expect(
        c1_support.get("current_primitive_class_promoted_as_flavor_closure") is False,
        "primitive scalar layer overpromoted as flavor closure",
        errors,
    )
    expect(
        c1_support.get("higherorder_fullresponse_values_promoted") is False,
        "higher-order values overpromoted",
        errors,
    )
    expect(
        c1_support.get("all_110_value_slots_have_algebraic_candidate_values") is True,
        "formal 110-row replay not retained",
        errors,
    )
    expect(c1_support.get("hessian_b_delta_values_filled") is True, "formal hessian/b/delta fill missing", errors)
    expect(
        c1_support.get("algebraic_values_promoted_as_physical") is False,
        "algebraic values overpromoted as physical",
        errors,
    )
    expect(
        c1_support.get("canonical_residual_projector_promoted_as_unique_mathematical_projector") is True,
        "canonical projector support missing",
        errors,
    )
    expect(
        c1_support.get("PhiFinC1_projector_application_promoted") is False,
        "PhiFinC1 application overpromoted",
        errors,
    )
    expect(
        c1_support.get("algebraic_finite_trace_boundary_cancellation") is True,
        "finite trace boundary support missing",
        errors,
    )
    expect(c1_support.get("physical_action_identity_promoted") is False, "physical action overpromoted", errors)
    expect(c1_support.get("same_source_b_selected_promoted") is False, "b_selected overpromoted", errors)
    expect(c1_support.get("support_layer_closed") is True, "C1 support layer not closed", errors)
    expect(c1_support.get("physical_value_promotion_closed") is False, "physical value layer overclosed", errors)

    expect(
        route_test.get("patched_or_local_principle_sm_parity_support_retained") is True,
        "patched/local support not retained",
        errors,
    )
    expect(
        route_test.get("unpatched_same_branch_PhiFinC1_source_emission_closed") is False,
        "unpatched source emission overclosed",
        errors,
    )
    expect(route_test.get("route_A_source_rule_gap_sharpened") is True, "Route A gap not sharpened", errors)
    expect(route_test.get("route_B_readiness_sidecar_built") is True, "Route B sidecar missing", errors)
    for key in [
        "PSM_C1_01_closed",
        "PSM_C1_04_closed",
        "ROUTE_A_closes_now",
        "ROUTE_B_ready_now",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "selected_C1_response_closed",
        "route_A_minimal_certificate_filled",
        "route_B_run_executed",
    ]:
        expect(route_test.get(key) is False, f"dynamic route overclosed or mismatch: {key}", errors)
    expect(
        route_test.get("physical_action_identity_current_attempt_rejected") is True,
        "current physical action rejection missing",
        errors,
    )
    expect(route_test.get("route_A_minimal_certificate_built") is True, "Route A certificate template missing", errors)
    expect(route_test.get("route_B_run_spec_built") is True, "Route B run spec missing", errors)
    expect(route_test.get("strict_two_lane_validator_still_rejects") is True, "two-lane rejection missing", errors)

    expect(precision.get("partial_precision_values_emitted") is True, "partial precision missing", errors)
    expect(precision.get("minimal_local_QFT_value_suite_filled") is True, "minimal QFT rows missing", errors)
    expect(precision.get("precision_observable_table_closed") is False, "precision table overclosed", errors)
    expect(precision.get("full_precision_observable_value_table_closed") is False, "full profile overclosed", errors)
    expect(
        precision.get("published_or_reconstructed_profile_likelihood_closed") is False,
        "profile likelihood overclosed",
        errors,
    )
    expect(precision.get("accepted_RG_threshold_covariance_closed") is False, "RG covariance overclosed", errors)

    for key in [
        "dotD_alpha1_stationary_projector_retired",
        "source_slot_layer_closed",
        "C1_support_layer_closed",
        "patched_or_local_principle_sm_parity_support_retained",
        "precision_profile_attempt_retained",
        "step9_closed_for_plan_contract",
    ]:
        expect(boundary.get(key) is True, f"boundary missing: {key}", errors)
    for key in [
        "actual_dynamic_QaSU3_operator_packet_closed",
        "selected_C1_response_closed",
        "selected_physical_PhiFinC1_source_rule_closed",
        "independent_Galerkin_row_execution_closed",
        "accepted_RG_threshold_covariance_closed",
        "full_S2_value_emission_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(boundary.get(key) is False, f"boundary overclosed: {key}", errors)

    expect(handoff.get("completed_step") == 9, "handoff completed step mismatch", errors)
    expect(handoff.get("next_step") == 10, "handoff next step mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    for key in [
        "selected_dotD_alpha1_driver",
        "stationary_projector_rho_s",
        "all_eight_operator_source_slots",
        "canonical_residual_projector_as_math_object",
        "formal_110_row_value_replay_as_support",
        "algebraic_trace_boundary_cancellation_as_support",
    ]:
        expect(handoff.get("retired_blockers", {}).get(key) is True, f"handoff retired missing: {key}", errors)
    for key in [
        "route_A_selected_physical_PhiFinC1_source_rule",
        "route_B_independent_selected_Galerkin_or_row_kernel_execution",
    ]:
        expect(handoff.get("step10_must_close_one_of", {}).get(key) is True, f"Step 10 exit missing: {key}", errors)
    for key in [
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
        "full_S2_value_rows",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting",
    ]:
        expect(handoff.get("step10_then_must_emit", {}).get(key) is True, f"Step 10 emission missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(handoff.get("must_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step9_closed_for_plan_contract") is True, "candidate Step 9 closure missing", errors)
    expect(decision.get("dotD_alpha1_stationary_projector_retired") is True, "candidate retired blockers missing", errors)
    expect(decision.get("all_operator_source_slots_closed") is True, "candidate source slots missing", errors)
    expect(decision.get("C1_support_layer_closed") is True, "candidate C1 support missing", errors)
    for key in [
        "route_A_selected_physical_PhiFinC1_source_rule_closed",
        "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "selected_C1_response_closed",
        "full_S2_value_emission_closed",
        "precision_profile_full_closure",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(data.get("step9_contract_closure_claimed") is True, "candidate local Step 9 claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM overclaim", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob overclaim", errors)

    expect(cert.get("step9_contract_closure_claimed") is True, "certificate Step 9 claim missing", errors)
    expect(cert.get("dotD_alpha1_stationary_projector_retired") is True, "certificate retired blockers missing", errors)
    expect(cert.get("all_operator_source_slots_closed") is True, "certificate source slots missing", errors)
    expect(cert.get("C1_support_layer_closed") is True, "certificate C1 support missing", errors)
    for key in [
        "actual_dynamic_QaSU3_operator_packet_closed",
        "selected_C1_response_closed",
        "route_A_selected_physical_PhiFinC1_source_rule_closed",
        "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
    ]:
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("Step 9 is closed as a non-looping frontier reduction" in note, "note missing Step 9 closure", errors)
    expect("actual dynamic Qa/SU3 packet closed       : false" in note, "note missing dynamic guard", errors)
    expect("route A physical Phi_fin^C1 source closed : false" in note, "note missing Route A guard", errors)
    expect("route B independent Galerkin rows closed  : false" in note, "note missing Route B guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 9 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 9 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
