"""Audit Step 6 measured-SM comparison readiness and no-knob gap boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step6_measuredsmcomparisonreadiness_or_noknobvaluegap"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
COMPARISON = PACKET_DIR / "step6_admitted_comparison_material.packet.json"
GAPS = PACKET_DIR / "step6_no_knob_value_gap_register.packet.json"
READINESS = PACKET_DIR / "step6_true_equivalence_readiness.packet.json"
BOUNDARY = PACKET_DIR / "step6_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step6_to_step7_handoff.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step6_MeasuredSMComparisonReadiness_or_NoKnobValueGap_v1.md"

STATUS = (
    "MTT_SELECTED_STEP6_MEASUREDSMCOMPARISONREADINESS_OR_NOKNOBVALUEGAP_"
    "CLOSED_READINESS_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_Step7_CommonRGCovarianceObservableSuite_or_FinalTrueSMEquivalenceGate_v1"


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
    comparison = load(COMPARISON)
    gaps = load(GAPS)
    readiness = load(READINESS)
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
    guard(comparison, errors, "comparison", closure=True)
    guard(gaps, errors, "gaps", closure=True)
    guard(readiness, errors, "readiness", closure=True)
    guard(boundary, errors, "boundary", closure=False)
    guard(handoff, errors, "handoff", closure=False)

    allowed = comparison.get("allowed_comparison_lanes", {})
    expect(allowed.get("admitted_external_replay_rows") is True, "external replay comparison not allowed", errors)
    expect(
        allowed.get("dynamic_first_response_qualitative_matrix_tests") is True,
        "dynamic qualitative comparison not allowed",
        errors,
    )
    expect(
        allowed.get("internal_no_knob_Yukawa_lambdaH_CKM_PMNS_predictions") is False,
        "internal no-knob predictions overallowed",
        errors,
    )
    expect(comparison.get("measured_comparison_readiness_closed") is True, "comparison readiness not closed", errors)
    external = comparison.get("admitted_external_replay", {})
    expect(external.get("external_import_lane_closed_at_admitted_replay_tier") is True, "external lane not ready", errors)
    expect(external.get("accepted_external_threshold_row_count") == 7, "threshold row count mismatch", errors)
    expect(external.get("accepted_external_mass_scheme_row_count") == 3, "mass scheme row count mismatch", errors)
    expect(external.get("accepted_diagonal_profile_theorem_closed") is True, "diagonal profile missing", errors)
    expect(external.get("is_no_knob_source") is False, "external replay promoted to no-knob", errors)
    native = comparison.get("native_measured_replay", {})
    expect(native.get("native_replay_closure_claimed") is True, "native replay not claimed", errors)
    expect(native.get("closed_row_count") == 6, "native replay row count mismatch", errors)
    expect(native.get("is_downstream_comparison_only") is True, "native replay not downstream-only", errors)
    dynamic = comparison.get("dynamic_qualitative_support", {})
    expect(dynamic.get("first_response_layer_closed") is True, "dynamic first response not closed", errors)
    expect(dynamic.get("qualitative_test_count") == 4, "qualitative test count mismatch", errors)
    expect(dynamic.get("not_a_precision_value_packet") is True, "dynamic support promoted to precision values", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(comparison.get("forbidden_selector_uses", {}).get(key) is True, f"selector guard missing: {key}", errors)

    expect(gaps.get("gap_count") == 5, "no-knob gap count mismatch", errors)
    for key in [
        "accepted_internal_scalar_rows",
        "lambda_H_internal_row",
        "Yukawa_magnitude_internal_rows",
        "CKM_PMNS_value_rows",
        "source_selected_universal_anchor",
    ]:
        expect(gaps.get("gaps", {}).get(key) is True, f"gap missing: {key}", errors)
    expect(gaps.get("accepted_internal_scalar_row_count") == 0, "gap scalar rows overaccepted", errors)
    expect(gaps.get("selected_universal_parameter_count") == 0, "gap universal parameter overselected", errors)
    expect(gaps.get("internal_no_knob_values_ready_for_comparison") is False, "internal no-knob values overready", errors)
    expect(
        gaps.get("internal_no_knob_Yukawa_lambdaH_CKM_PMNS_predictions_allowed") is False,
        "internal no-knob predictions allowed",
        errors,
    )
    expect(gaps.get("no_knob_gap_blocks_full_SM_equivalence") is True, "gap does not block full equivalence", errors)
    expect(gaps.get("ordinary_fitted_knobs_forbidden") is True, "ordinary fitted knobs not forbidden", errors)

    expect(readiness.get("native_published_parameter_replay_ready") is True, "native replay not ready", errors)
    expect(readiness.get("admitted_external_replay_ready") is True, "external replay not ready", errors)
    expect(
        readiness.get("dynamic_first_response_qualitative_tests_ready") is True,
        "dynamic qualitative readiness missing",
        errors,
    )
    expect(readiness.get("common_rg_true_equivalence_ready") is False, "common RG overready", errors)
    expect(readiness.get("common_rg_open_row_count") == 8, "common RG open row count mismatch", errors)
    expect(readiness.get("selected_SM_packet_final_certificate_ready") is False, "SM packet certificate overready", errors)
    expect(readiness.get("true_SM_equivalence_closed") is False, "true SM overclosed", errors)
    expect(readiness.get("full_no_knob_closed") is False, "full no-knob overclosed", errors)

    for key in [
        "measured_comparison_readiness_closed",
        "no_knob_value_gap_reported",
        "admitted_external_replay_ready",
        "native_measured_replay_ready",
        "dynamic_qualitative_support_ready",
        "step6_closed_for_plan_contract",
    ]:
        expect(boundary.get(key) is True, f"boundary missing: {key}", errors)
    expect(boundary.get("accepted_internal_scalar_row_count") == 0, "boundary scalar rows overaccepted", errors)
    expect(boundary.get("selected_universal_parameter_count") == 0, "boundary universal overselected", errors)
    expect(boundary.get("common_rg_true_equivalence_ready") is False, "boundary common RG overready", errors)
    expect(boundary.get("true_SM_equivalence_closed") is False, "boundary true SM overclosed", errors)
    expect(boundary.get("full_no_knob_closed") is False, "boundary no-knob overclosed", errors)

    expect(handoff.get("completed_step") == 6, "handoff completed step mismatch", errors)
    expect(handoff.get("next_step") == 7, "handoff next step mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    expect(len(handoff.get("step7_must_close", {})) == 9, "Step 7 blocker count mismatch", errors)
    for key in [
        "admitted_external_replay_rows_as_comparison_data",
        "native_measured_replay_rows_as_downstream_slots",
        "dynamic_first_response_qualitative_tests",
    ]:
        expect(handoff.get("step7_may_use", {}).get(key) is True, f"Step 7 allowed use missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(handoff.get("step7_must_not_use_as_selectors", {}).get(key) is True, f"Step 7 selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step6_closed_for_plan_contract") is True, "candidate Step 6 closure missing", errors)
    expect(decision.get("measured_comparison_readiness_closed") is True, "candidate readiness missing", errors)
    expect(decision.get("no_knob_value_gap_reported") is True, "candidate gap report missing", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "candidate scalar rows overaccepted", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "candidate universal overselected", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "candidate true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "candidate no-knob overclosed", errors)
    expect(data.get("step6_contract_closure_claimed") is True, "candidate Step 6 local claim missing", errors)
    expect(data.get("native_replay_closure_claimed") is True, "candidate native replay claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM claim overclosed", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob claim overclosed", errors)

    expect(cert.get("step6_contract_closure_claimed") is True, "certificate Step 6 local claim missing", errors)
    expect(cert.get("measured_comparison_readiness_closed") is True, "certificate readiness missing", errors)
    expect(cert.get("no_knob_value_gap_reported") is True, "certificate gap report missing", errors)
    expect(cert.get("accepted_internal_scalar_row_count") == 0, "certificate scalar rows overaccepted", errors)
    expect(cert.get("selected_universal_parameter_count") == 0, "certificate universal overselected", errors)
    expect(cert.get("native_replay_closure_claimed") is True, "certificate native replay claim missing", errors)
    expect(cert.get("true_SM_equivalence_claimed") is False, "certificate true SM claim overclosed", errors)
    expect(cert.get("full_no_knob_closure_claimed") is False, "certificate no-knob claim overclosed", errors)

    expect("Step 6 is closed as measured-comparison readiness" in note, "note missing Step 6 closure", errors)
    expect("accepted internal scalar rows         : 0" in note, "note missing scalar zero", errors)
    expect("selected universal parameters         : 0" in note, "note missing universal zero", errors)
    expect("true SM equivalence closed            : false" in note, "note missing true SM guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 6 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 6 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
