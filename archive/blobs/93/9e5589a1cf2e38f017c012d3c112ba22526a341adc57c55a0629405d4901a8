"""Audit sector-scaled eigenprofile threshold rows / Yukawa magnitude source gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.py"

SLUG = "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorScaledEigenprofileThresholdRows_or_YukawaMagnitudeSourceExecution_v1.md"

MODEL_TESTS = PACKET_DIR / "sector_scaled_eigenprofile_model_tests.packet.json"
COEFFICIENT_FRONTIER = PACKET_DIR / "sector_coefficient_frontier.packet.json"
ROW_ATTEMPT = PACKET_DIR / "eigenprofile_threshold_row_acceptance_attempt.packet.json"
DECISION = PACKET_DIR / "sector_scaled_eigenprofile_or_yukawa_magnitude_source_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sector_scaled_eigenprofile.packet.json"

STATUS = (
    "MTT_SELECTED_SECTORSCALEDEIGENPROFILETHRESHOLDROWS_OR_YUKAWAMAGNITUDESOURCEEXECUTION_"
    "BUILT_UNIVERSAL_PROFILE_NOGO_SECTOR_COEFFICIENTS_OPEN"
)
NEXT = "MTT_Selected_HigherResponseSectorCoefficients_or_ThresholdFunctionalSourceRows_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def approx(actual: float, expected: float, tol: float = 1e-9) -> bool:
    return abs(actual - expected) <= tol


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    model_tests = load(MODEL_TESTS)
    coefficient_frontier = load(COEFFICIENT_FRONTIER)
    row_attempt = load(ROW_ATTEMPT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next artifact mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next artifact mismatch", errors)

    for key in [
        "observed_data_used_as_selector",
        "target_fitting_used",
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail {key} must be false", errors)

    expect(
        model_tests.get("status") == "UNIVERSAL_SECTOR_SCALED_EIGENPROFILE_FAILS_MAGNITUDE_ROWS",
        "model test status mismatch",
        errors,
    )
    expect(model_tests.get("theorem", {}).get("proved") is True, "universal profile no-go theorem not proved", errors)
    expect(
        model_tests.get("universal_scaled_profile_can_match_diagnostic_hierarchies") is False,
        "universal scaled profile must fail diagnostic hierarchy test",
        errors,
    )
    expect(approx(model_tests.get("universal_abs_eigenprofile_ratio"), 2.0), "universal ratio must be 2", errors)
    expect(model_tests.get("diagnostic_hierarchy_spread", 0.0) > 80.0, "hierarchy spread too small", errors)
    expected_ratios = {
        "u": 79398.16128964476,
        "d": 918.2600248875669,
        "e": 3477.367910175253,
    }
    for sector, expected_ratio in expected_ratios.items():
        expect(
            approx(model_tests["diagnostic_hierarchy_ratios_not_used_as_selectors"][sector], expected_ratio, 1e-6),
            f"{sector} diagnostic hierarchy ratio mismatch",
            errors,
        )
        scale_result = model_tests["sector_scale_only_results"][sector]
        expect(scale_result.get("accepted_as_source_row") is False, f"{sector} scale result overaccepted", errors)
        expect(
            scale_result.get("relative_residual", 0.0) > 0.9,
            f"{sector} sector-scale residual should be large",
            errors,
        )
        expect(
            approx(scale_result.get("universal_abs_eigenprofile_ratio"), 2.0),
            f"{sector} universal ratio mismatch",
            errors,
        )
        expect(
            model_tests["log_affine_diagnostic_results"][sector].get("accepted_as_source_row") is False,
            f"{sector} log-affine diagnostic overaccepted",
            errors,
        )
        expect(
            model_tests["log_quadratic_diagnostic_exact_coefficients"][sector].get("accepted_as_source_row") is False,
            f"{sector} log-quadratic diagnostic overaccepted",
            errors,
        )
    expect(model_tests.get("observed_data_used_as_selector") is False, "model tests used observed selector", errors)
    expect(model_tests.get("target_fitting_used") is False, "model tests used target fitting", errors)
    expect(model_tests.get("closure_claimed") is True, "model no-go local closure must hold", errors)

    expect(
        coefficient_frontier.get("status") == "SECTOR_COEFFICIENTS_OR_THRESHOLD_FUNCTIONAL_REQUIRED",
        "coefficient frontier status mismatch",
        errors,
    )
    expect(coefficient_frontier.get("family_operator_closed") is True, "family operator must remain closed", errors)
    expect(coefficient_frontier.get("family_eigenbasis_available") is True, "family eigenbasis must be available", errors)
    expect(
        coefficient_frontier.get("universal_family_profile_insufficient") is True,
        "universal profile insufficiency missing",
        errors,
    )
    expect(
        coefficient_frontier.get("vsd02_strict_fill_attempt_currently_accepts_rows") == 0,
        "VSD02 strict fill should accept zero rows",
        errors,
    )
    expect(
        coefficient_frontier.get("vsd02_selected_threshold_response_functional_closed") is False,
        "threshold response functional must remain open",
        errors,
    )
    expect(coefficient_frontier.get("accepted_for_true_precision") is False, "true precision overaccepted", errors)
    expect(
        coefficient_frontier.get("same_branch_scale_scheme_loop_convention_closed") is False,
        "scale/scheme/loop convention must remain open",
        errors,
    )
    expect(coefficient_frontier.get("closure_claimed") is True, "coefficient frontier local closure must hold", errors)

    expect(
        row_attempt.get("status") == "EIGENPROFILE_ROWS_ATTEMPTED_FAMILY_COORDINATE_ONLY",
        "row attempt status mismatch",
        errors,
    )
    expect(row_attempt.get("family_coordinate_rows_available") is True, "family coordinate rows should be available", errors)
    expect(row_attempt.get("sector_scaled_magnitude_rows_emitted") is False, "magnitude rows must not be emitted", errors)
    expect(row_attempt.get("attempted_row_count") == 9, "attempted row count must be 9", errors)
    expect(row_attempt.get("accepted_rows") == [], "accepted rows must be empty", errors)
    expect(row_attempt.get("accepted_row_count") == 0, "accepted row count must be zero", errors)
    expect(row_attempt.get("required_charged_generation_row_count") == 9, "required row count must be nine", errors)
    expect(row_attempt.get("lambda_H_row_required") is True, "lambda_H row must remain required", errors)
    expect(
        row_attempt.get("generation_resolved_threshold_source_rows_closed") is False,
        "generation threshold rows must remain open",
        errors,
    )
    for row in row_attempt.get("attempted_rows", []):
        expect(
            row.get("accepted_as_selected_threshold_source_row") is False,
            f"{row.get('row_id')} overaccepted",
            errors,
        )
    expect(row_attempt.get("closure_claimed") is False, "row attempt must not claim closure", errors)

    expect(
        decision.get("status") == "FAMILY_COORDINATE_CLOSED_SECTOR_MAGNITUDE_SOURCE_OPEN",
        "decision status mismatch",
        errors,
    )
    expect(decision.get("family_resolving_operator_closed") is True, "decision family operator not closed", errors)
    expect(
        decision.get("universal_sector_scaled_eigenprofile_nogo_proved") is True,
        "decision no-go not proved",
        errors,
    )
    expect(decision.get("sector_coefficient_frontier_identified") is True, "sector frontier not identified", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "decision accepted count must be zero", errors)
    expect(decision.get("required_charged_generation_row_count") == 9, "decision required count must be nine", errors)
    for key in [
        "generation_resolved_threshold_source_rows_closed",
        "selected_threshold_response_functional_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision {key} must be false", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_HIGHER_RESPONSE_SECTOR_COEFFICIENTS", "cutset status mismatch", errors)
    expect(cutset.get("next_required_artifact") == NEXT, "cutset next mismatch", errors)
    expect(len(cutset.get("still_open", [])) == 6, "cutset must list six open targets", errors)
    for value in cutset.get("closed_this_artifact", {}).values():
        expect(value is True, "all cutset local closures must be true", errors)
    expect(cutset.get("closure_claimed") is False, "cutset must not claim full closure", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("family_resolving_operator_closed") is True, "candidate family operator not closed", errors)
    expect(
        closure.get("universal_sector_scaled_eigenprofile_nogo_proved") is True,
        "candidate no-go not closed",
        errors,
    )
    expect(
        closure.get("sector_coefficient_frontier_identified") is True,
        "candidate sector frontier not identified",
        errors,
    )
    for key in [
        "generation_resolved_threshold_source_rows_closed",
        "selected_threshold_response_functional_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure {key} must be false", errors)

    expect("universal sector-scaled eigenprofile no-go    : true" in note, "note no-go line missing", errors)
    expect("accepted generation threshold rows            : 0/9" in note, "note accepted-row line missing", errors)

    if errors:
        print("sector-scaled eigenprofile audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("sector-scaled eigenprofile audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
