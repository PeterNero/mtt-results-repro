"""Audit Step 5 no-knob/minimal-knob and internal scalar-row execution boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step5_noknobminimalknobaudit_or_internalscalarrowsexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INTERNAL_EXEC = PACKET_DIR / "step5_internal_scalar_row_execution_audit.packet.json"
NOKNOB = PACKET_DIR / "step5_no_knob_value_derivation_audit.packet.json"
MINIMAL = PACKET_DIR / "step5_minimal_universal_parameter_audit.packet.json"
BOUNDARY = PACKET_DIR / "step5_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step5_to_step6_handoff.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step5_NoKnobMinimalKnobAudit_or_InternalScalarRowsExecution_v1.md"

STATUS = (
    "MTT_SELECTED_STEP5_NOKNOBMINIMALKNOBAUDIT_OR_INTERNALSCALARROWSEXECUTION_"
    "CLOSED_AUDIT_NO_INTERNAL_ROWS_NO_MINIMAL_KNOB_SELECTED"
)
NEXT = "MTT_Selected_Step6_MeasuredSMDataComparisonReadiness_or_NoKnobValueGap_v1"


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
    internal = load(INTERNAL_EXEC)
    noknob = load(NOKNOB)
    minimal = load(MINIMAL)
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
    guard(internal, errors, "internal execution", closure=True)
    guard(noknob, errors, "no-knob audit", closure=True)
    guard(minimal, errors, "minimal audit", closure=True)
    guard(boundary, errors, "boundary", closure=False)
    guard(handoff, errors, "handoff", closure=False)

    for key in [
        "source_domain_closed",
        "basis_map_closed",
        "orbit_matrix_packet_closed",
        "direct_emission_attempt_executed",
        "internal_scalar_execution_audited",
    ]:
        expect(internal.get(key) is True, f"internal execution missing: {key}", errors)
    expect(internal.get("full_S2_scalar_execution_ready") is False, "full-S2 execution overready", errors)
    expect(internal.get("selected_universal_parameter_count") == 0, "internal universal parameter overselected", errors)
    expect(internal.get("codomain_scalar_row_count") == 10, "codomain count mismatch", errors)
    expect(internal.get("accepted_internal_scalar_row_count") == 0, "internal scalar rows overaccepted", errors)
    expect(internal.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    expect(internal.get("direct_rows_allowed") is False, "direct rows overallowed", errors)

    expect(noknob.get("kernel_typed") is True, "no-knob kernel not typed", errors)
    expect(noknob.get("Rtheta_readiness") == "8/9", "Rtheta readiness mismatch", errors)
    expect(noknob.get("basis_map_closed") is True, "basis map not closed", errors)
    expect(noknob.get("coefficient_functional_closed") is False, "coefficient functional overclosed", errors)
    expect(noknob.get("accepted_coefficient_row_count") == 0, "accepted coefficient rows overaccepted", errors)
    expect(noknob.get("accepted_internal_value_emission_count") == 0, "accepted internal values overaccepted", errors)
    expect(noknob.get("closed_no_knob_obligation_count") == 0, "no-knob obligations overclosed", errors)
    expect(noknob.get("required_no_knob_obligation_count") == 5, "no-knob obligation count mismatch", errors)
    expect(noknob.get("lambda_H_coefficient_selected") is False, "lambda_H coefficient overselected", errors)
    expect(
        noknob.get("accepted_Yukawa_magnitudes_as_no_knob_predictions") is False,
        "Yukawa magnitudes overaccepted",
        errors,
    )
    expect(noknob.get("full_no_knob_closed") is False, "full no-knob overclosed", errors)
    expect(noknob.get("no_knob_audit_closed") is True, "no-knob audit not closed", errors)

    expect(minimal.get("maximum_live_universal_parameters") == 3, "max universal parameter cap mismatch", errors)
    expect(minimal.get("candidate_class_count") == 5, "candidate class count mismatch", errors)
    expect(minimal.get("selected_candidates_now") == [], "selected candidates should be empty", errors)
    expect(minimal.get("selected_universal_parameter_count") == 0, "minimal universal parameter overselected", errors)
    expect(minimal.get("candidate_specific_source_theorem_present") is False, "source theorem overpresent", errors)
    expect(minimal.get("minimal_universal_parameter_selection_closed") is False, "minimal selection overclosed", errors)
    expect(minimal.get("source_domain_closure_changes_decision") is False, "source domain should not select knob", errors)
    expect(minimal.get("external_replay_policy_ready") is True, "external replay policy not ready", errors)
    expect(minimal.get("external_replay_policy_is_no_knob") is False, "external replay promoted to no-knob", errors)
    expect(minimal.get("external_replay_pack_selected_for_SM_parity") is True, "external replay pack not selected for parity", errors)
    expect(minimal.get("external_replay_pack_selected_for_full_no_knob") is False, "external replay pack overaccepted", errors)
    expect(minimal.get("ordinary_fitted_knobs_forbidden") is True, "ordinary knobs not forbidden", errors)
    expect(minimal.get("allowed_minimal_knob_policy_closed") is True, "minimal audit not closed", errors)
    expect(minimal.get("minimal_knob_selected_now") is False, "minimal knob overselected", errors)

    expect(boundary.get("step5_closed_for_plan_contract") is True, "Step 5 plan contract not closed", errors)
    expect(boundary.get("internal_scalar_row_execution_audited") is True, "internal execution not audited", errors)
    expect(boundary.get("no_knob_audit_closed") is True, "no-knob audit not closed in boundary", errors)
    expect(boundary.get("minimal_knob_policy_audit_closed") is True, "minimal audit not closed in boundary", errors)
    expect(boundary.get("ordinary_fitted_knobs_forbidden") is True, "ordinary knobs not forbidden in boundary", errors)
    expect(boundary.get("selected_universal_parameter_count") == 0, "boundary universal overselected", errors)
    expect(boundary.get("accepted_internal_scalar_row_count") == 0, "boundary scalar rows overaccepted", errors)
    expect(boundary.get("accepted_external_threshold_row_count") == 7, "threshold row count mismatch", errors)
    expect(boundary.get("accepted_external_mass_scheme_row_count") == 3, "mass row count mismatch", errors)
    expect(boundary.get("external_replay_ready_for_step6") is True, "external replay not ready for Step 6", errors)
    expect(boundary.get("internal_no_knob_values_ready_for_step6") is False, "internal no-knob values overready", errors)
    expect(boundary.get("true_SM_equivalence_closed") is False, "boundary true SM overclosed", errors)
    expect(boundary.get("full_no_knob_closed") is False, "boundary full no-knob overclosed", errors)

    expect(handoff.get("completed_step") == 5, "handoff completed step mismatch", errors)
    expect(handoff.get("next_step") == 6, "handoff next step mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    expect(handoff.get("step6_allowed_comparisons", {}).get("admitted_external_replay_rows") is True, "external replay comparison missing", errors)
    expect(
        handoff.get("step6_allowed_comparisons", {}).get("dynamic_first_response_qualitative_matrix_tests") is True,
        "qualitative dynamic comparison missing",
        errors,
    )
    expect(
        handoff.get("step6_allowed_comparisons", {}).get("internal_no_knob_Yukawa_lambdaH_CKM_PMNS_predictions") is False,
        "internal no-knob predictions overallowed",
        errors,
    )
    for key in [
        "accepted_internal_scalar_rows",
        "lambda_H_internal_row",
        "Yukawa_magnitude_internal_rows",
        "CKM_PMNS_value_rows",
        "source_selected_universal_anchor",
    ]:
        expect(handoff.get("step6_must_report_gaps", {}).get(key) is True, f"Step 6 gap missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(handoff.get("do_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step5_closed_for_plan_contract") is True, "candidate Step 5 closure missing", errors)
    expect(decision.get("internal_scalar_row_execution_audited") is True, "candidate internal audit missing", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "candidate scalar rows overaccepted", errors)
    expect(decision.get("lambda_H_row_emitted") is False, "candidate lambda_H overemitted", errors)
    expect(decision.get("no_knob_audit_closed") is True, "candidate no-knob audit missing", errors)
    expect(decision.get("full_no_knob_closed") is False, "candidate full no-knob overclosed", errors)
    expect(decision.get("minimal_knob_policy_audit_closed") is True, "candidate minimal audit missing", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "candidate universal overselected", errors)
    expect(decision.get("ordinary_fitted_knobs_forbidden") is True, "candidate ordinary knobs not forbidden", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "candidate true SM overclosed", errors)
    expect(data.get("step5_contract_closure_claimed") is True, "candidate Step 5 local claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM claim overclosed", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob claim overclosed", errors)

    expect(cert.get("step5_contract_closure_claimed") is True, "certificate Step 5 local claim missing", errors)
    expect(cert.get("accepted_internal_scalar_row_count") == 0, "certificate scalar rows overaccepted", errors)
    expect(cert.get("selected_universal_parameter_count") == 0, "certificate universal overselected", errors)
    expect(cert.get("ordinary_fitted_knobs_forbidden") is True, "certificate ordinary knobs not forbidden", errors)
    expect(cert.get("true_SM_equivalence_claimed") is False, "certificate true SM claim overclosed", errors)
    expect(cert.get("full_no_knob_closure_claimed") is False, "certificate no-knob claim overclosed", errors)

    expect("Step 5 is closed as an audit" in note, "note missing Step 5 audit closure", errors)
    expect("accepted internal scalar rows         : 0" in note, "note missing scalar zero", errors)
    expect("selected universal parameters         : 0" in note, "note missing universal zero", errors)
    expect("ordinary fitted knobs allowed         : false" in note, "note missing fitted knob guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 5 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 5 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
