"""Audit higher-response sector coefficients / threshold functional source rows gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.py"

SLUG = "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HigherResponseSectorCoefficients_or_ThresholdFunctionalSourceRows_v1.md"

KNOB_APPLICATION = PACKET_DIR / "minimal_universal_parameter_application_to_yukawa_wall.packet.json"
RESPONSE_FUNCTIONAL_ATTEMPT = PACKET_DIR / "selected_threshold_response_functional_execution_attempt.packet.json"
SECTOR_COEFFICIENT_ATTEMPT = PACKET_DIR / "higher_response_sector_coefficient_source_attempt.packet.json"
DECISION = PACKET_DIR / "higher_response_or_threshold_functional_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higher_response_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_HIGHERRESPONSESECTORCOEFFICIENTS_OR_THRESHOLDFUNCTIONALSOURCEROWS_"
    "BUILT_MINIMAL_PARAMETER_POLICY_APPLIED_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_ThresholdFunctionalSourceTheorem_or_MinimalUniversalParameterSelection_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    knob = load(KNOB_APPLICATION)
    response = load(RESPONSE_FUNCTIONAL_ATTEMPT)
    coefficients = load(SECTOR_COEFFICIENT_ATTEMPT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    for key in [
        "observed_data_used_as_selector",
        "target_fitting_used",
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail {key} must be false", errors)

    expect(
        knob.get("status") == "NO_KNOB_PREFERRED_MINIMAL_UNIVERSAL_PARAMETER_LANES_ALLOWED_NOT_SELECTED",
        "knob application status mismatch",
        errors,
    )
    expect(knob.get("maximum_live_universal_parameters") == 3, "max universal parameters must be 3", errors)
    expect(knob.get("selected_parameter_count_now") == 0, "selected parameter count now must be 0", errors)
    expect(
        knob.get("selected_parameter_count_after_this_artifact") == 0,
        "selected parameter count after artifact must be 0",
        errors,
    )
    expect(knob.get("minimal_universal_parameter_lane_selected_now") is False, "no parameter lane should be selected", errors)
    expect(len(knob.get("knob_lanes", [])) == 4, "must enumerate UP-0 through UP-3", errors)
    for expected_lane, lane in zip(["UP-0", "UP-1", "UP-2", "UP-3"], knob.get("knob_lanes", [])):
        expect(lane.get("lane") == expected_lane, f"lane order mismatch for {expected_lane}", errors)
        expect(lane.get("currently_closes_yukawa_wall") is False, f"{expected_lane} must not close wall now", errors)
    forbidden = knob.get("forbidden_knob_counting", {})
    for key in [
        "ordinary_sector_fits_forbidden",
        "one_knob_per_charged_sector_forbidden_as_source_proof",
        "one_knob_per_generation_forbidden_as_source_proof",
        "diagnostic_log_affine_coefficients_are_not_selected",
        "diagnostic_log_quadratic_coefficients_are_not_selected",
    ]:
        expect(forbidden.get(key) is True, f"forbidden policy missing {key}", errors)
    expect(knob.get("observed_data_used_as_selector") is False, "knob application used observed selector", errors)
    expect(knob.get("target_fitting_used") is False, "knob application used target fitting", errors)
    expect(knob.get("closure_claimed") is True, "knob application local closure must hold", errors)

    expect(
        response.get("status") == "THRESHOLD_RESPONSE_FUNCTIONAL_ATTEMPTED_REQUIRED_OUTPUTS_OPEN",
        "response attempt status mismatch",
        errors,
    )
    expect(response.get("required_output_count") == 5, "response required output count must be 5", errors)
    expect(response.get("present_required_output_count") == 1, "response present output count must be 1", errors)
    expect(response.get("selected_threshold_response_functional_closed") is False, "threshold functional overclosed", errors)
    expect(response.get("accepted_external_likelihood_workspace_closed") is False, "external workspace overclosed", errors)
    expect(response.get("accepted_source_row_count") == 0, "accepted source row count must be 0", errors)
    present = [item for item in response.get("functional_checks", []) if item.get("present_now")]
    expect(len(present) == 1, "exactly one functional check should be present", errors)
    if present:
        expect(
            present[0].get("required_output") == "proof no observed values select the response",
            "wrong present functional check",
            errors,
        )
    expect(response.get("closure_claimed") is False, "response attempt must not claim closure", errors)

    expect(
        coefficients.get("status") == "DIAGNOSTIC_SECTOR_COEFFICIENTS_REJECTED_SELECTED_SOURCE_ROWS_OPEN",
        "coefficient attempt status mismatch",
        errors,
    )
    expect(coefficients.get("family_coordinate_available") is True, "family coordinate must be available", errors)
    expect(coefficients.get("universal_profile_nogo_proved") is True, "universal profile no-go must be proved", errors)
    expect(coefficients.get("candidate_sector_coefficient_row_count") == 6, "candidate coefficient count must be 6", errors)
    expect(coefficients.get("accepted_sector_coefficient_rows") == [], "accepted coefficient rows must be empty", errors)
    expect(coefficients.get("accepted_sector_coefficient_row_count") == 0, "accepted coefficient count must be 0", errors)
    expect(coefficients.get("accepted_generation_threshold_source_row_count") == 0, "accepted generation count must be 0", errors)
    expect(coefficients.get("required_charged_generation_row_count") == 9, "required charged rows must be 9", errors)
    expect(coefficients.get("lambda_H_row_required") is True, "lambda_H row must remain required", errors)
    expect(coefficients.get("ordinary_sector_knobs_rejected") is True, "ordinary sector knobs must be rejected", errors)
    for row in coefficients.get("candidate_sector_coefficient_rows", []):
        expect(
            row.get("accepted_as_selected_sector_coefficients") is False,
            f"{row.get('candidate_id')} overaccepted",
            errors,
        )
    expect(coefficients.get("closure_claimed") is False, "coefficient attempt must not claim closure", errors)

    expect(
        decision.get("status") == "MINIMAL_PARAMETER_POLICY_APPLIED_THRESHOLD_FUNCTIONAL_OPEN",
        "decision status mismatch",
        errors,
    )
    expect(decision.get("no_knob_target_preserved") is True, "no-knob target not preserved", errors)
    expect(decision.get("minimal_universal_parameter_fallback_allowed") is True, "minimal fallback not allowed", errors)
    expect(decision.get("maximum_live_universal_parameters") == 3, "decision max params mismatch", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision selected param count must be 0", errors)
    expect(decision.get("family_resolving_operator_closed") is True, "family operator not closed", errors)
    expect(decision.get("universal_sector_scaled_eigenprofile_nogo_proved") is True, "eigenprofile no-go not proved", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "decision accepted rows must be 0", errors)
    expect(decision.get("required_charged_generation_row_count") == 9, "decision required rows must be 9", errors)
    for key in [
        "higher_response_sector_coefficients_closed",
        "selected_threshold_response_functional_closed",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision {key} must be false", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_THRESHOLD_FUNCTIONAL_SOURCE_THEOREM_OR_UNIVERSAL_PARAMETER_SELECTION",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("next_required_artifact") == NEXT, "cutset next mismatch", errors)
    expect(len(cutset.get("still_open", [])) == 6, "cutset must list six open targets", errors)
    for value in cutset.get("closed_this_artifact", {}).values():
        expect(value is True, "all cutset local closures must be true", errors)
    expect(cutset.get("closure_claimed") is False, "cutset must not claim closure", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("no_knob_target_preserved") is True, "candidate no-knob target not preserved", errors)
    expect(
        closure.get("minimal_universal_parameter_fallback_allowed") is True,
        "candidate minimal fallback not allowed",
        errors,
    )
    expect(closure.get("selected_universal_parameter_count") == 0, "candidate selected params must be 0", errors)
    for key in [
        "higher_response_sector_coefficients_closed",
        "selected_threshold_response_functional_closed",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure {key} must be false", errors)

    expect("no-knob target preserved                    : true" in note, "note no-knob line missing", errors)
    expect("minimal universal parameter fallback allowed: true" in note, "note minimal fallback line missing", errors)
    expect("ordinary fitted sector knobs rejected       : true" in note, "note knob rejection line missing", errors)
    expect("minimal-parameter Yukawa closure closed     : false" in note, "note minimal closure guard missing", errors)

    if errors:
        print("higher-response/threshold-functional audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("higher-response/threshold-functional audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
