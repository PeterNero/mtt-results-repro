"""Audit post-Pi threshold matching rows or mass-scheme source rows artifact."""

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
BUILDER = ROOT / "scripts" / "build_selected_thresholdmatchingrowspostpi_or_massschemesourcerows.py"

SLUG = "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1.md"

THRESHOLD_ROWS = PACKET_DIR / "post_pi_admitted_threshold_matching_rows.packet.json"
MASS_ROWS = PACKET_DIR / "post_pi_admitted_mass_scheme_rows.packet.json"
PROMOTION = PACKET_DIR / "external_row_admission_not_rtheta_selection.packet.json"
READINESS = PACKET_DIR / "rtheta_value_readiness_after_external_rows.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_external_threshold_mass_rows.packet.json"

STATUS = (
    "MTT_SELECTED_THRESHOLDMATCHINGROWSPOSTPI_OR_MASSSCHEMESOURCEROWS_"
    "CLOSED_ADMITTED_EXTERNAL_ROWS_PROFILE_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    threshold = load(THRESHOLD_ROWS)
    mass = load(MASS_ROWS)
    promotion = load(PROMOTION)
    readiness = load(READINESS)
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
        threshold.get("status") == "ADMITTED_EXTERNAL_THRESHOLD_MATCHING_ROWS_CLOSED_INTERNAL_RTHETA_OPEN",
        "threshold packet status mismatch",
        errors,
    )
    expect(threshold.get("row_count") == 7, "threshold row count mismatch", errors)
    expect(threshold.get("accepted_admitted_external_threshold_matching_row_count") == 7, "threshold accepted count mismatch", errors)
    expect(threshold.get("accepted_internal_selected_Rtheta_threshold_row_count") == 0, "threshold internal rows overaccepted", errors)
    expect(threshold.get("threshold_matching_source_rows_closed_at_admitted_external_tier") is True, "threshold external tier not closed", errors)
    expect(threshold.get("threshold_matching_source_rows_closed_as_no_knob_Rtheta_derivation") is False, "threshold no-knob overclosed", errors)
    for row in threshold.get("rows", []):
        expect(row.get("accepted_as_admitted_external_threshold_matching_row") is True, f"threshold row not admitted: {row.get('id')}", errors)
        expect(row.get("accepted_as_internal_selected_Rtheta_row") is False, f"threshold row selected internally: {row.get('id')}", errors)
    source_tests = threshold.get("source_closure_tests", {})
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "top_higgs_external_formula_map_import_closed",
        "W_Z_H_external_coordinate_rows_closed",
    ]:
        expect(source_tests.get(key) is True, f"threshold source test missing: {key}", errors)
    expect(source_tests.get("top_higgs_external_formula_map_row_count") == 2, "top/Higgs row count mismatch", errors)
    expect(source_tests.get("W_Z_H_external_coordinate_row_count") == 5, "WZH row count mismatch", errors)

    expect(
        mass.get("status") == "ADMITTED_EXTERNAL_MASS_SCHEME_ROWS_CLOSED_INTERNAL_RTHETA_OPEN",
        "mass packet status mismatch",
        errors,
    )
    expect(mass.get("row_count") == 3, "mass row count mismatch", errors)
    expect(mass.get("accepted_admitted_external_mass_scheme_row_count") == 3, "mass accepted count mismatch", errors)
    expect(mass.get("accepted_internal_selected_Rtheta_mass_scheme_row_count") == 0, "mass internal rows overaccepted", errors)
    expect(mass.get("mass_scheme_conversion_source_rows_closed_at_admitted_external_tier") is True, "mass external tier not closed", errors)
    expect(mass.get("mass_scheme_conversion_source_rows_closed_as_no_knob_Rtheta_derivation") is False, "mass no-knob overclosed", errors)
    for row in mass.get("rows", []):
        expect(row.get("accepted_as_admitted_external_mass_scheme_row") is True, f"mass row not admitted: {row.get('id')}", errors)
        expect(row.get("accepted_as_internal_selected_Rtheta_row") is False, f"mass row selected internally: {row.get('id')}", errors)
    mtests = mass.get("source_closure_tests", {})
    expect(mtests.get("same_branch_scale_scheme_loop_convention_closed") is True, "mass convention source missing", errors)
    expect(mtests.get("all_three_bct_external_mass_scheme_rows_available") is True, "BCT all-three missing", errors)
    expect(mtests.get("accepted_bottom_charm_tau_map_row_count") == 3, "BCT count mismatch", errors)
    expect(mtests.get("fullSM_profile_convention_for_bct_rows_closed") is False, "BCT fullSM profile overclosed", errors)

    expect(
        promotion.get("status") == "EXTERNAL_ROWS_ADMITTED_FOR_REPLAY_NOT_SELECTED_NOKNOB_RTHETA",
        "promotion status mismatch",
        errors,
    )
    expect(promotion.get("accepted_external_threshold_row_count") == 7, "promotion threshold count mismatch", errors)
    expect(promotion.get("accepted_external_mass_scheme_row_count") == 3, "promotion mass count mismatch", errors)
    expect(promotion.get("accepted_internal_selected_Rtheta_row_count") == 0, "promotion internal rows overaccepted", errors)
    guards = promotion.get("guardrails", {})
    for key in [
        "external_rows_used_as_branch_selector",
        "target_fit_after_residuals",
        "full_covariance_profile_likelihood_closed",
        "bct_fullSM_profile_reconciliation_closed",
        "functional_values_instantiated",
    ]:
        expect(guards.get(key) is False, f"promotion guardrail overclosed: {key}", errors)
    expect(promotion.get("closure_claimed") is False, "promotion overclaimed", errors)

    expect(
        readiness.get("status") == "READINESS_ADVANCED_EXTERNAL_ROWS_CLOSED_PROFILE_NOKNOB_OPEN",
        "readiness status mismatch",
        errors,
    )
    expect(readiness.get("previous_present_count") == 5, "previous readiness mismatch", errors)
    expect(readiness.get("present_count") == 7, "readiness did not advance to 7", errors)
    expect(readiness.get("requirement_count") == 9, "readiness requirement mismatch", errors)
    expect(readiness.get("retired_blocking_failures") == [
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
    ], "retired blockers mismatch", errors)
    expect(readiness.get("blocking_failures") == [
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ], "remaining blockers mismatch", errors)
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

    expect(cutset.get("status") == "NEXT_ATTACK_FULL_PROFILE_OR_NOKNOB_VALUE_DERIVATION", "cutset status mismatch", errors)
    closed = cutset.get("closed_now", {})
    for key in [
        "admitted_external_threshold_matching_source_rows",
        "admitted_external_mass_scheme_conversion_source_rows",
        "Rtheta_readiness_present_count_advanced_to_7_of_9",
        "internal_Rtheta_nonselector_boundary_preserved",
    ]:
        expect(closed.get(key) is True, f"cutset closure missing: {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "selected_internal_Rtheta_threshold_mass_derivation",
        "selected_threshold_response_functional_instantiated",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
    ]:
        expect(still.get(key) is True, f"cutset overclosed: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "threshold_matching_source_rows_closed_at_admitted_external_tier",
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier",
    ]:
        expect(closure.get(key) is True, f"candidate closure missing: {key}", errors)
    for key in [
        "selected_internal_Rtheta_threshold_mass_derivation_closed",
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
    expect(cert.get("closed_at_admitted_external_tier_only") is True, "certificate tier guard missing", errors)

    expect("threshold matching rows closed      : true" in note, "note missing threshold closure", errors)
    expect("mass-scheme conversion rows closed  : true" in note, "note missing mass closure", errors)
    expect("Rtheta readiness                    : 7/9" in note, "note missing readiness", errors)
    expect("selected no-knob Rtheta rows        : false" in note, "note missing no-knob guard", errors)

    if errors:
        print("Post-Pi threshold/mass row audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Post-Pi threshold/mass row audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
