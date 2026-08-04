"""Audit post-Pi convention source or threshold-functional instantiation artifact."""

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
BUILDER = ROOT / "scripts" / "build_selected_postpiconventionsource_or_thresholdfunctionalinstantiation.py"

SLUG = "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostPiConventionSource_or_ThresholdFunctionalInstantiation_v1.md"

CONVENTION = PACKET_DIR / "post_pi_same_branch_convention_source_contract.packet.json"
FUNCTIONAL = PACKET_DIR / "threshold_functional_instantiation_recheck_after_convention.packet.json"
ROW_MATRIX = PACKET_DIR / "threshold_row_source_attack_matrix.packet.json"
READINESS = PACKET_DIR / "rtheta_value_readiness_after_convention_source.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_post_pi_convention_source.packet.json"

STATUS = (
    "MTT_SELECTED_POSTPICONVENTIONSOURCE_OR_THRESHOLDFUNCTIONALINSTANTIATION_"
    "CLOSED_CONVENTION_SOURCE_THRESHOLD_VALUES_OPEN"
)
NEXT = "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1"
REMAINING_BLOCKERS = [
    "threshold_matching_source_rows",
    "mass_scheme_conversion_source_rows",
    "no_knob_value_derivation",
    "full_profile_likelihood_or_accepted_diagonal_theorem",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    convention = load(CONVENTION)
    functional = load(FUNCTIONAL)
    row_matrix = load(ROW_MATRIX)
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
        convention.get("status") == "SAME_BRANCH_SCALE_SCHEME_LOOP_CONVENTION_SOURCE_CLOSED_VALUES_OPEN",
        "convention status mismatch",
        errors,
    )
    expect(convention.get("target_scale") == "M_Z", "target scale mismatch", errors)
    expect(convention.get("target_scheme") == "MSbar", "target scheme mismatch", errors)
    owner = convention.get("same_branch_owner_evidence", {})
    for key in [
        "Pi_Rtheta_closed",
        "VSD01_source_assembly_subgate_closed",
        "dynamic_matter_overlap_first_response_closed",
        "coefficient_functional_domain_closed",
        "source_normalized_projection_weights_closed",
        "post_pi_frontier_synchronized",
    ]:
        expect(owner.get(key) is True, f"owner evidence missing: {key}", errors)
    repaired = convention.get("old_rejection_repaired", {})
    for key in [
        "source_ownership_was_open_before",
        "post_pi_source_owner_now_closed",
        "post_pi_assembly_now_closed",
        "external_benchmarks_remain_downstream_only",
        "finite_residuals_remain_requirements_not_fits",
    ]:
        expect(repaired.get(key) is True, f"old rejection not repaired/preserved: {key}", errors)
    expect(convention.get("same_branch_scale_scheme_loop_convention_closed") is True, "convention not closed", errors)
    for key in [
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "selected_threshold_response_functional_instantiated",
    ]:
        expect(convention.get(key) is False, f"convention overclosed: {key}", errors)
    expect(convention.get("accepted_coefficient_value_count") == 0, "convention accepted coefficients", errors)
    for source in convention.get("external_primary_source_inspiration", []):
        expect(source.get("used_as_selector") is False, f"external source used as selector: {source}", errors)

    expect(
        functional.get("status") == "CONVENTION_SOURCE_CLOSED_FUNCTIONAL_VALUES_STILL_OPEN",
        "functional status mismatch",
        errors,
    )
    domain = functional.get("contract_domain_ready_after_post_pi", {})
    for key in [
        "Pi_Rtheta_closed",
        "coefficient_functional_domain_closed",
        "source_normalized_projection_weights_closed",
        "same_branch_scale_scheme_loop_convention_closed",
    ]:
        expect(domain.get(key) is True, f"functional domain not ready: {key}", errors)
    missing = functional.get("still_missing_for_value_instantiation", {})
    for key in [
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "magnitude_bearing_projection_weights",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "no_knob_value_derivation",
    ]:
        expect(missing.get(key) is True, f"functional missing value overclosed: {key}", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "selected_value_evaluator_closed",
        "true_SM_equivalence_closed",
        "closure_claimed",
    ]:
        expect(functional.get(key) is False, f"functional overclaimed: {key}", errors)
    expect(functional.get("accepted_coefficient_value_count") == 0, "functional accepted coefficients", errors)

    expect(row_matrix.get("status") == "ROW_ATTACK_MATRIX_BUILT_NO_VALUES_ACCEPTED", "row matrix status mismatch", errors)
    expect(row_matrix.get("accepted_row_group_count") == 0, "row groups overaccepted", errors)
    expect(len(row_matrix.get("row_groups", [])) == 4, "row group count mismatch", errors)
    for group in row_matrix.get("row_groups", []):
        expect(group.get("accepted_now") is False, f"row group overaccepted: {group.get('id')}", errors)
    expect(row_matrix.get("closure_claimed") is False, "row matrix overclaimed", errors)

    expect(
        readiness.get("status") == "READINESS_ADVANCED_CONVENTION_CLOSED_VALUE_ROWS_OPEN",
        "readiness status mismatch",
        errors,
    )
    expect(readiness.get("previous_present_count") == 4, "previous readiness mismatch", errors)
    expect(readiness.get("present_count") == 5, "readiness did not advance to 5", errors)
    expect(readiness.get("requirement_count") == 9, "readiness requirement mismatch", errors)
    expect(readiness.get("retired_blocking_failure") == "same_branch_scale_scheme_loop_convention", "wrong retired blocker", errors)
    expect(readiness.get("blocking_failures") == REMAINING_BLOCKERS, "remaining blockers mismatch", errors)
    expect(readiness.get("accepted_coefficient_value_count") == 0, "readiness accepted coefficients", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "closure_claimed",
    ]:
        expect(readiness.get(key) is False, f"readiness overclaimed: {key}", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_THRESHOLD_MATCHING_AND_MASS_SCHEME_ROWS", "cutset status mismatch", errors)
    closed = cutset.get("closed_now", {})
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "post_pi_formal_convention_source_contract",
        "MZ_MSbar_loop_threshold_mass_scheme_policy_attached",
        "external_primary_source_requirements_catalogued_as_nonselectors",
        "Rtheta_readiness_present_count_advanced_to_5_of_9",
    ]:
        expect(closed.get(key) is True, f"cutset missing closure: {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "magnitude_bearing_projection_weights",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
    ]:
        expect(still.get(key) is True, f"cutset overclosed: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "post_pi_formal_convention_source_contract_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure missing: {key}", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "magnitude_bearing_projection_weights_closed",
        "accepted_lambda_H_value",
        "selected_value_evaluator_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)
    expect(cert.get("same_branch_scale_scheme_loop_convention_closed") is True, "certificate convention missing", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "certificate accepted coefficients", errors)

    expect("same-branch convention source closed       : true" in note, "note missing convention closure", errors)
    expect("Rtheta readiness                           : 5/9" in note, "note missing readiness", errors)
    expect("accepted coefficient values                : 0" in note, "note missing coefficient guard", errors)

    if errors:
        print("Post-Pi convention-source audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Post-Pi convention-source audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
