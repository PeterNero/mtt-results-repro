"""Audit threshold-functional source theorem / minimal universal parameter selection gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection.py"

SLUG = "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdFunctionalSourceTheorem_or_MinimalUniversalParameterSelection_v1.md"

STALE_BLOCKER = PACKET_DIR / "stale_rtheta_dynamic_source_blocker_reconciliation.packet.json"
DOMAIN_READINESS = PACKET_DIR / "rtheta_domain_readiness_after_dynamic_family_closure.packet.json"
UNIVERSAL_SELECTION = PACKET_DIR / "minimal_universal_parameter_selection_attempt.packet.json"
INSTANTIATION_UPDATE = PACKET_DIR / "rtheta_instantiation_update_after_dynamic_source_closure.packet.json"
DECISION = PACKET_DIR / "threshold_functional_source_or_minimal_parameter_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_functional_source_gate.packet.json"

STATUS = (
    "MTT_SELECTED_THRESHOLDFUNCTIONALSOURCETHEOREM_OR_MINIMALUNIVERSALPARAMETERSELECTION_"
    "BUILT_DYNAMIC_DOMAIN_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaValueRows_or_UniversalSourceAnchorTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    stale = load(STALE_BLOCKER)
    domain = load(DOMAIN_READINESS)
    universal = load(UNIVERSAL_SELECTION)
    instantiation = load(INSTANTIATION_UPDATE)
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
        stale.get("status") == "STALE_RTHETA_DYNAMIC_SOURCE_BLOCKER_RETIRED",
        "stale blocker status mismatch",
        errors,
    )
    for key in [
        "dynamic_matter_overlap_packet_closed",
        "dynamic_first_response_layer_closed",
        "dynamic_validator_passes",
        "family_resolving_operator_closed",
        "stale_dynamic_source_blocker_retired",
    ]:
        expect(stale.get(key) is True, f"stale reconciliation {key} must be true", errors)
    expect(stale.get("closure_claimed") is True, "stale reconciliation local closure must hold", errors)

    expect(
        domain.get("status") == "RTHETA_DOMAIN_DYNAMIC_FAMILY_SUBGATE_CLOSED_VALUE_BASIS_OPEN",
        "domain status mismatch",
        errors,
    )
    expect(domain.get("domain_requirement_count") == 5, "domain requirement count must be 5", errors)
    expect(domain.get("present_domain_requirement_count") == 3, "domain present count must be 3", errors)
    expect(domain.get("dynamic_domain_subgate_closed") is True, "dynamic domain must close", errors)
    expect(domain.get("family_coordinate_subgate_closed") is True, "family coordinate must close", errors)
    expect(domain.get("basis_map_to_magnitude_rows_closed") is False, "basis map to magnitudes must remain open", errors)
    expect(
        domain.get("same_branch_true_precision_convention_closed") is False,
        "true precision convention must remain open",
        errors,
    )
    requirement_by_id = {row["id"]: row for row in domain.get("domain_requirements", [])}
    expect(
        requirement_by_id["selected_dynamic_operator_packet_or_source_owner_theorem"]["present"] is True,
        "selected dynamic operator requirement should now be present",
        errors,
    )
    expect(
        requirement_by_id["scale_and_scheme_convention_before_observed_value_comparison"]["present"] is False,
        "scale/scheme convention overclosed",
        errors,
    )
    expect(
        requirement_by_id["basis_map_from_MTT_rows_to_SM_value_packet_coordinates"]["present"] is False,
        "basis map to value packet overclosed",
        errors,
    )
    expect(domain.get("closure_claimed") is True, "domain local closure must hold", errors)

    expect(
        universal.get("status") == "NO_UNIVERSAL_PARAMETER_SELECTED_FOR_RTHETA_YUKAWA_WALL",
        "universal selection status mismatch",
        errors,
    )
    expect(universal.get("maximum_live_universal_parameters") == 3, "max universal params mismatch", errors)
    expect(universal.get("selected_parameter_count_before") == 0, "selected params before must be 0", errors)
    expect(universal.get("selected_parameter_count_after") == 0, "selected params after must be 0", errors)
    expect(universal.get("imported_one_universal_primitive_ready") is True, "alpha1 ready primitive should be imported", errors)
    expect(universal.get("provisional_parameter_admitted_now") is False, "provisional parameter overadmitted", errors)
    expect(universal.get("minimal_parameter_yukawa_closure_closed") is False, "minimal parameter closure overclosed", errors)
    expect(len(universal.get("candidate_selection_rows", [])) >= 5, "universal candidate rows missing", errors)
    for row in universal.get("candidate_selection_rows", []):
        expect(row.get("selected_now") is False, f"{row.get('candidate_id')} selected unexpectedly", errors)
        expect(
            row.get("accepted_for_yukawa_wall_now") is False,
            f"{row.get('candidate_id')} accepted for Yukawa wall unexpectedly",
            errors,
        )
    expect(universal.get("closure_claimed") is False, "universal selection must not claim closure", errors)

    expect(
        instantiation.get("status") == "DYNAMIC_DOMAIN_READY_RTHETA_VALUE_ROWS_STILL_OPEN",
        "instantiation update status mismatch",
        errors,
    )
    expect(instantiation.get("functional_contract_closed") is True, "functional contract should be closed", errors)
    expect(instantiation.get("dynamic_domain_subgate_closed") is True, "dynamic domain should be closed", errors)
    expect(instantiation.get("retired_failures") == ["selected_dynamic_operator_source_owner"], "wrong retired failure", errors)
    expect(instantiation.get("domain_present_count_after_update") == 3, "domain present count mismatch", errors)
    expect(instantiation.get("domain_requirement_count") == 5, "domain requirement count mismatch", errors)
    expect(instantiation.get("codomain_present_required_output_count_after_update") == 1, "codomain present count mismatch", errors)
    expect(instantiation.get("codomain_required_output_count") == 5, "codomain required count mismatch", errors)
    expect(instantiation.get("accepted_generation_threshold_source_row_count") == 0, "accepted generation rows must be 0", errors)
    expect(instantiation.get("required_charged_generation_row_count") == 9, "required generation rows must be 9", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "minimal_parameter_yukawa_closure_closed",
        "closure_claimed",
    ]:
        expect(instantiation.get(key) is False, f"instantiation {key} must be false", errors)
    expect(
        "selected_dynamic_operator_source_owner" not in instantiation.get("remaining_hard_failures", []),
        "retired dynamic source blocker still listed as remaining",
        errors,
    )
    expect(len(instantiation.get("remaining_hard_failures", [])) == 6, "remaining hard failure count mismatch", errors)

    expect(
        decision.get("status") == "RTHETA_DYNAMIC_DOMAIN_CLOSED_VALUE_ROWS_AND_PARAMETER_SELECTION_OPEN",
        "decision status mismatch",
        errors,
    )
    for key in [
        "functional_contract_closed",
        "stale_dynamic_source_blocker_retired",
        "dynamic_domain_subgate_closed",
        "family_coordinate_subgate_closed",
        "universal_sector_scaled_eigenprofile_nogo_proved",
    ]:
        expect(decision.get(key) is True, f"decision {key} must be true", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision selected parameter count must be 0", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "decision accepted rows must be 0", errors)
    expect(decision.get("required_charged_generation_row_count") == 9, "decision required rows must be 9", errors)
    for key in [
        "minimal_universal_parameter_selection_closed",
        "selected_threshold_response_functional_instantiated",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "basis_map_to_sector_scaled_magnitude_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision {key} must be false", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_RTHETA_VALUE_ROWS_OR_UNIVERSAL_SOURCE_ANCHOR", "cutset status mismatch", errors)
    expect(cutset.get("next_required_artifact") == NEXT, "cutset next mismatch", errors)
    expect(len(cutset.get("still_open", [])) == 6, "cutset must list six open targets", errors)
    for value in cutset.get("closed_this_artifact", {}).values():
        expect(value is True, "all cutset local closures must be true", errors)
    expect(cutset.get("closure_claimed") is False, "cutset must not claim closure", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "functional_contract_closed",
        "stale_dynamic_source_blocker_retired",
        "dynamic_domain_subgate_closed",
        "family_coordinate_subgate_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure {key} must be true", errors)
    expect(closure.get("selected_universal_parameter_count") == 0, "candidate selected parameter count must be 0", errors)
    for key in [
        "minimal_universal_parameter_selection_closed",
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure {key} must be false", errors)

    expect("stale dynamic-source blocker retired     : true" in note, "note stale blocker line missing", errors)
    expect("R_theta instantiated                     : false" in note, "note instantiation guard missing", errors)
    expect("minimal-parameter Yukawa closure closed  : false" in note, "note minimal parameter guard missing", errors)

    if errors:
        print("threshold-functional source/minimal-parameter audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("threshold-functional source/minimal-parameter audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
