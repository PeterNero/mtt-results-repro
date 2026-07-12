"""Audit selected family-resolving operator / generation threshold row execution gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_familyresolvingoperator_or_generationthresholdrowsexecution.py"

SLUG = "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FamilyResolvingOperator_or_GenerationThresholdRowsExecution_v1.md"

STALE_RECONCILIATION = PACKET_DIR / "stale_routec_operator_nogo_reconciliation.packet.json"
SPECTRUM = PACKET_DIR / "selected_first_response_family_spectrum.packet.json"
MAG_OBSTRUCTION = PACKET_DIR / "magnitude_threshold_row_obstruction_after_family_resolution.packet.json"
DECISION = PACKET_DIR / "family_resolving_operator_or_generation_threshold_rows_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_family_resolving_operator.packet.json"

STATUS = (
    "MTT_SELECTED_FAMILYRESOLVINGOPERATOR_OR_GENERATIONTHRESHOLDROWSEXECUTION_"
    "BUILT_FAMILY_OPERATOR_CLOSED_MAGNITUDE_ROWS_OPEN"
)
NEXT = "MTT_Selected_SectorScaledEigenprofileThresholdRows_or_YukawaMagnitudeSourceExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    stale = load(STALE_RECONCILIATION)
    spectrum = load(SPECTRUM)
    obstruction = load(MAG_OBSTRUCTION)
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
        stale.get("status") == "STALE_ROUTEC_SCAFFOLD_NOGO_RETIRED_FOR_FIRST_RESPONSE_DYNAMIC_LAYER",
        "stale reconciliation status mismatch",
        errors,
    )
    expect(stale.get("old_selected_emitted_count") == 0, "old Route-C no-go selected count must be zero", errors)
    expect(stale.get("old_required_field_count") == 7, "old Route-C no-go required count must be seven", errors)
    expect(stale.get("later_dynamic_validator_passes") is True, "later dynamic validator must pass", errors)
    expect(stale.get("later_dynamic_packet_closed") is True, "later dynamic packet must close", errors)
    expect(stale.get("later_qasu3_first_response_closed") is True, "later QaSU3 first response must close", errors)
    expect(stale.get("vsd01_dynamic_tensor_subgate_closed") is True, "VSD01 dynamic tensor subgate must close", errors)
    expect(
        stale.get("stale_first_response_absence_blocker_retired") is True,
        "stale first-response absence blocker must be retired",
        errors,
    )
    expect(stale.get("magnitude_value_closure_retired") is False, "magnitude closure must not be retired", errors)
    expect(stale.get("closure_claimed") is True, "stale reconciliation local closure must hold", errors)

    expect(
        spectrum.get("status") == "SELECTED_FIRST_RESPONSE_OPERATOR_HAS_NONDEGENERATE_FAMILY_SPECTRUM",
        "spectrum status mismatch",
        errors,
    )
    expect(spectrum.get("family_resolving_operator_closed") is True, "family operator must close", errors)
    expect(spectrum.get("all_sectors_family_resolved") is True, "all sectors must be family resolved", errors)
    expect(spectrum.get("universal_spectrum_across_sectors") is True, "spectrum must be universal across sectors", errors)
    expect(spectrum.get("generation_magnitude_rows_emitted") is False, "magnitude rows must not be emitted", errors)
    expect(set(spectrum.get("sector_results", {}).keys()) == {"u", "d", "e", "nuD"}, "sector set mismatch", errors)
    expected_eigenvalues = [-1.367835979172, -0.683917989586, 0.683917989586]
    for sector, result in spectrum.get("sector_results", {}).items():
        expect(result.get("correction_dY_rank") == 3, f"{sector} dY rank mismatch", errors)
        expect(result.get("first_hermitian_response_rank") == 3, f"{sector} H1 rank mismatch", errors)
        expect(result.get("traceless_rank") == 3, f"{sector} traceless rank mismatch", errors)
        expect(result.get("distinct_eigenvalue_count") == 3, f"{sector} distinct eigenvalue count mismatch", errors)
        expect(result.get("family_labels_resolved") is True, f"{sector} family labels not resolved", errors)
        expect(result.get("selected_by_MTT") is True, f"{sector} not selected by MTT", errors)
        expect(result.get("hermitian_error_max_abs") == 0.0, f"{sector} Hermitian error nonzero", errors)
        expect(result.get("eigenvalues") == expected_eigenvalues, f"{sector} eigenvalues mismatch", errors)
        expect(result.get("min_spectral_gap", 0.0) > 0.6, f"{sector} spectral gap too small", errors)
    expect(spectrum.get("closure_claimed") is True, "spectrum local closure must hold", errors)

    expect(
        obstruction.get("status") == "FAMILY_LABELS_RESOLVED_MAGNITUDE_ROWS_STILL_NOT_EMITTED",
        "obstruction status mismatch",
        errors,
    )
    expect(obstruction.get("family_operator_closed") is True, "obstruction should inherit family closure", errors)
    expect(
        obstruction.get("universal_spectrum_across_sectors") is True,
        "obstruction should record universal spectrum",
        errors,
    )
    expect(obstruction.get("first_response_abs_eigenvalue_ratio") == 2.0, "first-response ratio mismatch", errors)
    expect(obstruction.get("accepted_generation_threshold_source_rows") == [], "accepted rows must be empty", errors)
    expect(obstruction.get("accepted_generation_threshold_source_row_count") == 0, "accepted row count must be zero", errors)
    expect(obstruction.get("required_charged_generation_row_count") == 9, "required row count must be nine", errors)
    expect(obstruction.get("lambda_H_row_required") is True, "lambda_H row must still be required", errors)
    expect(
        obstruction.get("generation_resolved_threshold_source_rows_closed") is False,
        "generation threshold rows must remain open",
        errors,
    )
    expect(
        obstruction.get("diagnostic_hierarchy_spread", 0.0) > 80.0,
        "diagnostic hierarchy spread should remain recorded",
        errors,
    )
    expect(obstruction.get("closure_claimed") is False, "obstruction must not claim closure", errors)

    expect(
        decision.get("status") == "FAMILY_RESOLVING_OPERATOR_CLOSED_GENERATION_MAGNITUDE_THRESHOLD_ROWS_OPEN",
        "decision status mismatch",
        errors,
    )
    expect(decision.get("family_resolving_operator_closed") is True, "decision family operator must close", errors)
    expect(decision.get("all_sectors_family_resolved") is True, "decision all sectors resolved mismatch", errors)
    expect(decision.get("universal_spectrum_across_sectors") is True, "decision universal spectrum mismatch", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "decision accepted count must be zero", errors)
    expect(decision.get("required_charged_generation_row_count") == 9, "decision required count must be nine", errors)
    for key in [
        "generation_resolved_threshold_source_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision {key} must be false", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_SECTOR_SCALED_EIGENPROFILE_THRESHOLD_ROWS", "cutset status mismatch", errors)
    expect(cutset.get("next_required_artifact") == NEXT, "cutset next mismatch", errors)
    expect(len(cutset.get("still_open", [])) == 6, "cutset must list six open targets", errors)
    expect(cutset.get("closure_claimed") is False, "cutset must not claim closure", errors)
    for value in cutset.get("closed_this_artifact", {}).values():
        expect(value is True, "all cutset local closures must be true", errors)

    closure = candidate.get("closure_decision", {})
    expect(
        closure.get("stale_first_response_absence_blocker_retired") is True,
        "candidate stale blocker not retired",
        errors,
    )
    expect(closure.get("family_resolving_operator_closed") is True, "candidate family operator not closed", errors)
    expect(
        closure.get("generation_resolved_threshold_source_rows_closed") is False,
        "candidate generation rows must remain open",
        errors,
    )
    expect(
        closure.get("accepted_Yukawa_magnitudes_as_no_knob_predictions") is False,
        "candidate Yukawa magnitudes must remain open",
        errors,
    )
    expect(closure.get("true_SM_equivalence_closed") is False, "candidate true SM must remain open", errors)

    expect("family-resolving operator closed             : true" in note, "note family closure line missing", errors)
    expect("accepted generation threshold rows           : 0/9" in note, "note accepted-row line missing", errors)

    if errors:
        print("family-resolving operator audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("family-resolving operator audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
