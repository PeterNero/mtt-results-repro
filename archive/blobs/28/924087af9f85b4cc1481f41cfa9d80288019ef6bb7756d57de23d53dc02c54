"""Audit generation-resolved threshold rows / profile convention closure gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_generationresolvedthresholdsourcerows_or_profileconventionclosure.py"

SLUG = "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_GenerationResolvedThresholdSourceRows_or_ProfileConventionClosure_v1.md"

RECONCILIATION = PACKET_DIR / "stale_dynamic_gap_reconciliation.packet.json"
GEN_SUPPORT = PACKET_DIR / "generation_source_support_recheck.packet.json"
ROW_ATTEMPT = PACKET_DIR / "generation_resolved_threshold_row_attempt.packet.json"
PROFILE = PACKET_DIR / "profile_convention_closure_recheck.packet.json"
DECISION = PACKET_DIR / "generation_rows_or_profile_convention_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_generation_row_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_GENERATIONRESOLVEDTHRESHOLDSOURCEROWS_OR_PROFILECONVENTIONCLOSURE_"
    "BUILT_STALE_DYNAMIC_BLOCKER_RETIRED_GENERATION_ROWS_OPEN"
)
NEXT = "MTT_Selected_FamilyResolvingOperator_or_GenerationThresholdRowsExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    reconciliation = load(RECONCILIATION)
    generation_support = load(GEN_SUPPORT)
    row_attempt = load(ROW_ATTEMPT)
    profile = load(PROFILE)
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
        reconciliation.get("status") == "STALE_DYNAMIC_OPERATOR_PRIMITIVE_BLOCKER_RETIRED",
        "reconciliation status mismatch",
        errors,
    )
    expect(reconciliation.get("later_dynamic_packet_validates") is True, "later dynamic packet must validate", errors)
    expect(len(reconciliation.get("old_errors", [])) >= 4, "old dynamic errors must be recorded", errors)
    expect(
        reconciliation.get("stale_dynamic_errors_retired") is True,
        "stale dynamic errors must be retired",
        errors,
    )
    expect(reconciliation.get("closure_claimed") is True, "reconciliation local closure must hold", errors)

    expect(
        generation_support.get("status") == "GENERATION_STRUCTURE_SUPPORT_PRESENT_MAGNITUDE_ROWS_OPEN",
        "generation support status mismatch",
        errors,
    )
    expect(
        generation_support.get("selected_three_family_structure_declared") is True,
        "three-family source declaration missing",
        errors,
    )
    expect(
        generation_support.get("static_matter_slot_readout_closed") is True,
        "static matter slot readout must be closed",
        errors,
    )
    expect(
        generation_support.get("finite_c1_source_stack_closed") is True,
        "finite C1 source stack must be closed",
        errors,
    )
    row_counts = generation_support.get("formal_row_counts", {})
    expect(row_counts.get("primitive_rows") == 72, "primitive row count mismatch", errors)
    expect(row_counts.get("sector_matrix_rows") == 36, "sector matrix row count mismatch", errors)
    expect(row_counts.get("hessian_source_rows") == 2, "hessian source row count mismatch", errors)
    expect(row_counts.get("total_rows") == 110, "total row count mismatch", errors)
    expect(generation_support.get("generation_support_closed") is True, "generation support must close", errors)
    expect(
        generation_support.get("generation_resolved_magnitude_rows_closed") is False,
        "generation magnitude rows must remain open",
        errors,
    )
    expect(generation_support.get("closure_claimed") is True, "generation support local closure must hold", errors)

    expect(
        row_attempt.get("status") == "GENERATION_RESOLVED_ROWS_ATTEMPTED_DIAGNOSTIC_ONLY",
        "row attempt status mismatch",
        errors,
    )
    expect(row_attempt.get("attempted_row_count") == 9, "attempted row count must be 9", errors)
    expect(row_attempt.get("accepted_rows") == [], "accepted generation rows must be empty", errors)
    expect(row_attempt.get("accepted_row_count") == 0, "accepted generation row count must be zero", errors)
    expect(row_attempt.get("required_charged_generation_row_count") == 9, "required charged row count must be 9", errors)
    expect(row_attempt.get("lambda_H_row_required") is True, "lambda_H row must still be required", errors)
    expect(
        row_attempt.get("generation_resolved_threshold_source_rows_closed") is False,
        "generation threshold source rows must remain open",
        errors,
    )
    for row in row_attempt.get("attempted_rows", []):
        expect(
            row.get("accepted_as_selected_generation_threshold_source_row") is False,
            f"diagnostic row {row.get('row_id')} must not be accepted",
            errors,
        )
    expect(row_attempt.get("closure_claimed") is False, "row attempt must not claim closure", errors)

    expect(
        profile.get("status") == "FIRSTPASS_PROFILE_CONVENTION_AVAILABLE_TRUE_PRECISION_CONVENTION_OPEN",
        "profile status mismatch",
        errors,
    )
    expect(profile.get("accepted_for_SM_parity") is True, "SM parity convention should be accepted", errors)
    expect(profile.get("accepted_for_profile_input") is True, "profile input convention should be accepted", errors)
    expect(profile.get("accepted_for_true_precision") is False, "true precision convention must remain open", errors)
    expect(profile.get("value_profile_execution_layer_closed") is True, "profile execution layer should close", errors)
    expect(profile.get("full_profile_likelihood_closed") is False, "full profile likelihood must remain open", errors)
    expect(
        profile.get("same_branch_scale_scheme_loop_convention_closed") is False,
        "same-branch scale/scheme/loop convention must remain open",
        errors,
    )
    expect(profile.get("closure_claimed") is False, "profile gate must not claim full closure", errors)

    expect(
        decision.get("status") == "DYNAMIC_BLOCKER_RETIRED_GENERATION_ROWS_AND_PROFILE_CONVENTION_OPEN",
        "decision status mismatch",
        errors,
    )
    expect(decision.get("stale_dynamic_operator_primitive_blocker_retired") is True, "stale blocker not retired", errors)
    expect(decision.get("generation_structure_support_closed") is True, "generation support not closed", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "decision accepted count must be 0", errors)
    expect(decision.get("required_charged_generation_row_count") == 9, "decision required count must be 9", errors)
    for key in [
        "generation_resolved_threshold_source_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "full_profile_likelihood_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision {key} must be false", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_FAMILY_RESOLVING_OPERATOR_OR_GENERATION_THRESHOLD_ROWS", "cutset status mismatch", errors)
    expect(cutset.get("next_required_artifact") == NEXT, "cutset next artifact mismatch", errors)
    expect(len(cutset.get("still_open", [])) == 6, "cutset must list six open targets", errors)
    expect(cutset.get("closure_claimed") is False, "cutset must not claim closure", errors)
    for value in cutset.get("closed_this_artifact", {}).values():
        expect(value is True, "all cutset local closures must be true", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("stale_dynamic_operator_primitive_blocker_retired") is True, "candidate stale blocker not retired", errors)
    expect(closure.get("generation_structure_support_closed") is True, "candidate generation support not closed", errors)
    expect(
        closure.get("generation_resolved_threshold_source_rows_closed") is False,
        "candidate generation rows must remain open",
        errors,
    )
    expect(
        closure.get("same_branch_scale_scheme_loop_convention_closed") is False,
        "candidate profile convention must remain open",
        errors,
    )
    expect(
        closure.get("accepted_Yukawa_magnitudes_as_no_knob_predictions") is False,
        "candidate Yukawa no-knob closure must remain false",
        errors,
    )
    expect(closure.get("true_SM_equivalence_closed") is False, "candidate true SM closure must remain false", errors)

    expect("stale dynamic blocker retired        : true" in note, "note stale-blocker line missing", errors)
    expect("accepted generation threshold rows   : 0/9" in note, "note accepted-row line missing", errors)

    if errors:
        print("generation threshold/profile convention audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("generation threshold/profile convention audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
