"""Audit R_theta value evaluator execution or threshold-response instantiation packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.py"

SLUG = "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueEvaluatorExecution_or_ThresholdResponseInstantiation_v1.md"

SOURCE_OWNER = PACKET_DIR / "rtheta_value_evaluator_source_owner_update.packet.json"
INSTANTIATION_AUDIT = PACKET_DIR / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
EXECUTION_GATE = PACKET_DIR / "rtheta_value_evaluator_execution_gate.packet.json"
VALUE_RECHECK = PACKET_DIR / "rtheta_coefficient_value_recheck_after_pi_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_value_evaluator_recheck.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_VALUEEVALUATOREXECUTION_OR_THRESHOLDRESPONSEINSTANTIATION_"
    "CLOSED_PI_SOURCE_OWNER_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaThresholdRows_or_ProfileConventionSourceClosure_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    source_owner = load(SOURCE_OWNER)
    instantiation = load(INSTANTIATION_AUDIT)
    execution = load(EXECUTION_GATE)
    value = load(VALUE_RECHECK)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail overclaimed: {key}", errors)

    expect(source_owner.get("status") == "PI_BACKED_DYNAMIC_SOURCE_OWNER_CLOSED", "source owner status mismatch", errors)
    for key in [
        "Pi_Rtheta_closed",
        "selected_dynamic_operator_source_owner_closed",
        "coefficient_functional_domain_closed",
        "source_normalized_projection_weights_closed",
        "closure_claimed",
    ]:
        expect(source_owner.get(key) is True, f"source-owner field should be true: {key}", errors)
    expect(source_owner.get("magnitude_bearing_projection_weights_closed") is False, "magnitude weights overclosed", errors)
    expect(source_owner.get("retired_old_failure") == "selected_dynamic_operator_source_owner", "wrong retired failure", errors)

    expect(
        instantiation.get("status") == "PI_SOURCE_OWNER_CLOSED_THRESHOLD_RESPONSE_NOT_INSTANTIATED",
        "instantiation status mismatch",
        errors,
    )
    expect(instantiation.get("accepted_threshold_response_functional_instantiated") is False, "threshold response overinstantiated", errors)
    expect("selected_dynamic_operator_source_owner" in instantiation.get("retired_failures_since_previous", []), "dynamic owner not retired", errors)
    requirements = {item["id"]: item for item in instantiation.get("requirements", [])}
    for key in [
        "selected_dynamic_operator_source_owner",
        "Pi_Rtheta_projection_kernel",
        "coefficient_functional_skeleton",
        "source_normalized_sector_projection_weights",
    ]:
        expect(requirements.get(key, {}).get("present") is True, f"requirement should be present: {key}", errors)
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]:
        expect(requirements.get(key, {}).get("present") is False, f"requirement overclosed: {key}", errors)
        expect(key in instantiation.get("blocking_failures", []), f"missing blocker: {key}", errors)

    expect(
        execution.get("status") == "VALUE_EVALUATOR_DOMAIN_CLOSED_EXECUTION_BLOCKED_BY_THRESHOLD_ROWS",
        "execution gate status mismatch",
        errors,
    )
    for key in [
        "Pi_Rtheta_closed",
        "selected_dynamic_operator_source_owner_closed",
        "coefficient_functional_skeleton_closed",
        "threshold_response_contract_closed",
        "source_normalized_projection_weights_closed",
    ]:
        expect(execution.get(key) is True, f"execution gate should be true: {key}", errors)
    for key in [
        "magnitude_bearing_projection_weights_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "closure_claimed",
    ]:
        expect(execution.get(key) is False, f"execution gate overclosed: {key}", errors)
    expect(execution.get("accepted_coefficient_value_count") == 0, "execution accepted coefficients", errors)

    expect(value.get("status") == "PI_CLOSED_COEFFICIENT_VALUES_STILL_REJECTED", "value recheck status mismatch", errors)
    expect(value.get("Pi_Rtheta_closed") is True, "value recheck missing Pi closure", errors)
    for key in [
        "selected_value_evaluator_closed",
        "lambda_H_value_selected",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(value.get(key) is False, f"value recheck overclosed: {key}", errors)
    expect(value.get("accepted_coefficient_value_count") == 0, "value recheck accepted coefficients", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_THRESHOLD_ROWS_OR_PROFILE_CONVENTION_SOURCE_CLOSURE",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closed_now", {}).get("Pi_Rtheta") is True, "cutset missing Pi closure", errors)
    expect(cutset.get("closed_now", {}).get("selected_dynamic_operator_source_owner") is True, "cutset missing source-owner closure", errors)
    expect(cutset.get("still_open") == instantiation.get("blocking_failures"), "cutset blocker list mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "Pi_Rtheta_closed",
        "selected_dynamic_operator_source_owner_closed",
        "coefficient_functional_domain_closed",
        "source_normalized_projection_weights_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure should be true: {key}", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)
    expect(cert.get("selected_dynamic_operator_source_owner_closed") is True, "cert source owner mismatch", errors)
    expect(cert.get("selected_threshold_response_functional_instantiated") is False, "cert threshold overclosed", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "cert accepted coefficients", errors)

    expect("Pi_Rtheta closed                              : true" in note, "note missing Pi closure", errors)
    expect("selected dynamic operator source owner closed: true" in note, "note missing source-owner closure", errors)
    expect("threshold response instantiated              : false" in note, "note missing threshold guard", errors)
    expect("accepted coefficient values                   : 0" in note, "note missing zero-value guard", errors)

    if errors:
        print("RTheta value-evaluator audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta value-evaluator audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
