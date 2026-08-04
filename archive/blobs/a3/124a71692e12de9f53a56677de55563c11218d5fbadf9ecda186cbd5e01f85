"""Audit post-Pi full-profile/diagonal theorem or no-knob value derivation artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation.py"

SLUG = "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1.md"

DIAGONAL = PACKET_DIR / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
FULL_GATE = PACKET_DIR / "full_covariance_profile_gate_after_diagonal_acceptance.packet.json"
READINESS = PACKET_DIR / "rtheta_value_readiness_after_diagonal_theorem.packet.json"
NOKNOB = PACKET_DIR / "no_knob_value_derivation_recheck_after_profile.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_diagonal_profile_acceptance.packet.json"

STATUS = (
    "MTT_SELECTED_FULLPROFILEORDIAGONALTHEOREMPOSTPI_OR_NOKNOBVALUEDERIVATION_"
    "CLOSED_ACCEPTED_DIAGONAL_PROFILE_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_NoKnobValueDerivationPostPi_or_MinimalUniversalParameterPolicy_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def close(actual: float, expected: float, tol: float = 1e-12) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    diagonal = load(DIAGONAL)
    full_gate = load(FULL_GATE)
    readiness = load(READINESS)
    noknob = load(NOKNOB)
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
        expect(cert.get(key) is False, f"certificate guardrail overclaimed: {key}", errors)

    expect(
        diagonal.get("status") == "ACCEPTED_DIAGONAL_PROFILE_THEOREM_CLOSED_FULL_COVARIANCE_OPEN",
        "diagonal status mismatch",
        errors,
    )
    tests = diagonal.get("acceptance_tests", {})
    for key in [
        "post_pi_convention_source_closed",
        "admitted_external_threshold_rows_closed",
        "admitted_external_mass_scheme_rows_closed",
        "diagonal_profile_executed",
        "passes_coarse_diagonal_profile",
        "diagonal_uncertainty_sidecar_available",
    ]:
        expect(tests.get(key) is True, f"diagonal acceptance test missing: {key}", errors)
    expect(tests.get("correlations_included") is False, "diagonal correlations overclaimed", errors)
    expect(tests.get("full_covariance_profile_likelihood_closed") is False, "diagonal full covariance overclaimed", errors)
    expect(diagonal.get("profile_row_count") == 6, "diagonal profile row count mismatch", errors)
    expect(close(diagonal.get("chi2_diagonal"), 6.00319217893227), "diagonal chi2 mismatch", errors)
    expect(diagonal.get("degrees_of_freedom") == 6, "diagonal dof mismatch", errors)
    expect(close(diagonal.get("reduced_chi2_diagonal"), 1.000532029822045), "diagonal reduced chi2 mismatch", errors)
    expect(diagonal.get("max_abs_pull") < 2.22, "diagonal max pull too large", errors)
    expect(diagonal.get("accepted_diagonal_theorem_closed") is True, "diagonal theorem not closed", errors)
    expect(diagonal.get("full_profile_likelihood_closed") is False, "full profile overclosed", errors)
    expect(diagonal.get("closure_claimed") is True, "diagonal local closure missing", errors)

    expect(
        full_gate.get("status") == "FULL_COVARIANCE_PROFILE_STILL_OPEN_ACCEPTED_DIAGONAL_THEOREM_AVAILABLE",
        "full gate status mismatch",
        errors,
    )
    expect(full_gate.get("accepted_diagonal_theorem_closed") is True, "full gate missing diagonal theorem", errors)
    expect(full_gate.get("full_covariance_profile_likelihood_closed") is False, "full covariance overclosed", errors)
    expect(full_gate.get("can_claim_full_correlated_profile") is False, "full correlated profile overclaimed", errors)
    expect(len(full_gate.get("missing_covariance_objects", [])) >= 5, "missing covariance objects not preserved", errors)
    expect(full_gate.get("closure_claimed") is False, "full gate overclaimed", errors)

    expect(
        readiness.get("status") == "READINESS_ADVANCED_DIAGONAL_THEOREM_CLOSED_NOKNOB_OPEN",
        "readiness status mismatch",
        errors,
    )
    expect(readiness.get("previous_present_count") == 7, "previous readiness mismatch", errors)
    expect(readiness.get("present_count") == 8, "readiness did not advance to 8", errors)
    expect(readiness.get("requirement_count") == 9, "readiness requirement mismatch", errors)
    expect(
        readiness.get("retired_blocking_failure") == "full_profile_likelihood_or_accepted_diagonal_theorem",
        "wrong retired blocker",
        errors,
    )
    expect(readiness.get("blocking_failures") == ["no_knob_value_derivation"], "remaining blockers mismatch", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(readiness.get(key) is False, f"readiness overclosed: {key}", errors)
    expect(readiness.get("accepted_coefficient_value_count") == 0, "readiness accepted coefficients", errors)

    expect(
        noknob.get("status") == "NOKNOB_VALUE_DERIVATION_STILL_OPEN_EXTERNAL_REPLAY_READY",
        "no-knob status mismatch",
        errors,
    )
    expect(noknob.get("closed_obligation_count_under_no_knob") == 0, "no-knob obligations overclosed", errors)
    expect(noknob.get("external_replay_rows_available", {}).get("accepted_diagonal_theorem") is True, "external replay diagonal missing", errors)
    expect(noknob.get("no_knob_value_derivation_closed") is False, "no-knob overclosed", errors)
    expect(noknob.get("minimal_universal_parameter_policy_needed_if_no_internal_derivation") is True, "minimal-parameter route not flagged", errors)
    expect(noknob.get("selected_universal_parameter_count") == 0, "selected universal parameters overclaimed", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_NOKNOB_VALUE_DERIVATION_OR_MINIMAL_UNIVERSAL_PARAMETER", "cutset status mismatch", errors)
    closed = cutset.get("closed_now", {})
    for key in [
        "accepted_diagonal_profile_theorem",
        "full_profile_or_accepted_diagonal_requirement",
        "Rtheta_readiness_present_count_advanced_to_8_of_9",
        "full_covariance_profile_gap_preserved",
    ]:
        expect(closed.get(key) is True, f"cutset closure missing: {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "no_knob_value_derivation",
        "selected_internal_Rtheta_threshold_mass_derivation",
        "selected_threshold_response_functional_instantiated",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        expect(still.get(key) is True, f"cutset overclosed: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "accepted_diagonal_profile_theorem_closed",
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure missing: {key}", errors)
    for key in [
        "full_covariance_profile_likelihood_closed",
        "no_knob_value_derivation_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "selected_value_evaluator_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)

    expect("accepted diagonal theorem closed       : true" in note, "note missing diagonal closure", errors)
    expect("full correlated covariance closed      : false" in note, "note missing covariance guard", errors)
    expect("Rtheta readiness                       : 8/9" in note, "note missing readiness", errors)
    expect("no-knob value derivation closed        : false" in note, "note missing no-knob guard", errors)

    if errors:
        print("Post-Pi diagonal/no-knob audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Post-Pi diagonal/no-knob audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
