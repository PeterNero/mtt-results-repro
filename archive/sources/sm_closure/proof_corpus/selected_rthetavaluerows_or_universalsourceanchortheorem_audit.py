"""Audit R_theta value-row basis map / universal source anchor theorem gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_rthetavaluerows_or_universalsourceanchortheorem.py"

SLUG = "selected_rthetavaluerows_or_universalsourceanchortheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueRows_or_UniversalSourceAnchorTheorem_v1.md"

SPECTRAL_BASIS = PACKET_DIR / "selected_family_spectral_projector_basis.packet.json"
BASIS_MAP = PACKET_DIR / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
INSTANTIATION_UPDATE = PACKET_DIR / "rtheta_instantiation_update_after_basis_map.packet.json"
VALUE_ROW_ATTEMPT = PACKET_DIR / "rtheta_value_row_coefficients_attempt.packet.json"
DECISION = PACKET_DIR / "rtheta_value_rows_or_universal_anchor_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_basis_map.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETAVALUEROWS_OR_UNIVERSALSOURCEANCHORTHEOREM_"
    "BUILT_BASIS_MAP_CLOSED_COEFFICIENTS_OPEN"
)
NEXT = "MTT_Selected_RThetaCoefficientFunctional_or_UniversalAnchorSelection_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    spectral_basis = load(SPECTRAL_BASIS)
    basis_map = load(BASIS_MAP)
    instantiation = load(INSTANTIATION_UPDATE)
    value_attempt = load(VALUE_ROW_ATTEMPT)
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
        spectral_basis.get("status") == "SELECTED_FAMILY_SPECTRAL_PROJECTOR_BASIS_EMITTED",
        "spectral basis status mismatch",
        errors,
    )
    expect(spectral_basis.get("all_sector_projector_bases_closed") is True, "all projector bases must close", errors)
    expect(
        spectral_basis.get("family_label_convention") == "ascending selected H1 eigenvalue",
        "family label convention mismatch",
        errors,
    )
    expect(set(spectral_basis.get("sector_projector_bases", {}).keys()) == {"u", "d", "e", "nuD"}, "sector set mismatch", errors)
    for sector, row in spectral_basis.get("sector_projector_bases", {}).items():
        expect(row.get("spectral_projector_basis_closed") is True, f"{sector} projector basis not closed", errors)
        expect(row.get("eigenvalues") == [-1.367835979172, -0.683917989586, 0.683917989586], f"{sector} eigenvalues mismatch", errors)
        metrics = row.get("projector_metrics", {})
        expect(metrics.get("projector_ranks") == [1, 1, 1], f"{sector} projector ranks mismatch", errors)
        expect(metrics.get("projector_traces") == [1.0, 1.0, 1.0], f"{sector} projector traces mismatch", errors)
        for key in [
            "max_projector_idempotency_error",
            "max_projector_hermitian_error",
            "max_projector_orthogonality_error",
            "completeness_error",
        ]:
            expect(metrics.get(key, 1.0) < 1e-10, f"{sector} {key} too large", errors)
        expect(len(row.get("projectors", [])) == 3, f"{sector} projector count mismatch", errors)
    expect(spectral_basis.get("closure_claimed") is True, "spectral basis local closure must hold", errors)

    expect(
        basis_map.get("status") == "FAMILY_EIGENPROFILE_TO_CHARGED_MAGNITUDE_ROW_BASIS_MAP_CLOSED",
        "basis map status mismatch",
        errors,
    )
    expect(basis_map.get("basis_map_to_sector_scaled_magnitude_rows_closed") is True, "basis map must close", errors)
    expect(basis_map.get("charged_sectors") == ["u", "d", "e"], "charged sector list mismatch", errors)
    expect(basis_map.get("charged_basis_row_count") == 9, "charged basis row count must be 9", errors)
    expect(basis_map.get("required_charged_generation_row_count") == 9, "required charged row count must be 9", errors)
    expect(basis_map.get("coefficient_values_selected") is False, "coefficient values must not be selected", errors)
    expect(
        basis_map.get("generation_resolved_threshold_source_rows_closed") is False,
        "generation threshold rows must remain open",
        errors,
    )
    expect(basis_map.get("accepted_generation_threshold_source_row_count") == 0, "accepted generation rows must remain 0", errors)
    for row in basis_map.get("charged_basis_rows", []):
        expect(row.get("accepted_as_basis_row") is True, f"{row.get('row_id')} basis row not accepted", errors)
        expect(
            row.get("accepted_as_magnitude_value_row") is False,
            f"{row.get('row_id')} magnitude value row overaccepted",
            errors,
        )
        expect(row.get("coefficient_value_selected") is False, f"{row.get('row_id')} coefficient overselected", errors)
    expect(basis_map.get("closure_claimed") is True, "basis map local closure must hold", errors)

    expect(
        instantiation.get("status") == "RTHETA_BASIS_MAP_CLOSED_COEFFICIENT_AND_VALUE_ROWS_OPEN",
        "instantiation update status mismatch",
        errors,
    )
    expect(instantiation.get("retired_failures") == ["basis_map_to_sector_scaled_magnitude_rows"], "wrong retired failure", errors)
    expect(instantiation.get("basis_map_to_sector_scaled_magnitude_rows_closed") is True, "basis map not closed in instantiation", errors)
    expect(instantiation.get("domain_present_count_after_update") == 4, "domain present count must be 4", errors)
    expect(instantiation.get("domain_requirement_count") == 5, "domain requirement count must be 5", errors)
    expect(instantiation.get("codomain_present_required_output_count_after_update") == 1, "codomain present count must remain 1", errors)
    expect(instantiation.get("codomain_required_output_count") == 5, "codomain required count must be 5", errors)
    expect("basis_map_to_sector_scaled_magnitude_rows" not in instantiation.get("remaining_hard_failures", []), "basis map still listed as failure", errors)
    expect(len(instantiation.get("remaining_hard_failures", [])) == 5, "remaining hard failure count must be 5", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "closure_claimed",
    ]:
        expect(instantiation.get(key) is False, f"instantiation {key} must be false", errors)

    expect(
        value_attempt.get("status") == "BASIS_ROWS_CLOSED_COEFFICIENT_VALUES_REJECTED_AS_DIAGNOSTIC",
        "value row attempt status mismatch",
        errors,
    )
    expect(value_attempt.get("diagnostic_coefficient_count") == 9, "diagnostic coefficient count must be 9", errors)
    expect(value_attempt.get("accepted_coefficient_rows") == [], "accepted coefficient rows must be empty", errors)
    expect(value_attempt.get("accepted_coefficient_row_count") == 0, "accepted coefficient count must be 0", errors)
    expect(value_attempt.get("lambda_H_coefficient_selected") is False, "lambda_H coefficient overselected", errors)
    expect(value_attempt.get("sector_scale_only_nogo_preserved") is True, "sector-scale no-go not preserved", errors)
    expect(value_attempt.get("selected_universal_parameter_count") == 0, "selected universal parameter count must be 0", errors)
    expect(value_attempt.get("coefficient_functional_closed") is False, "coefficient functional overclosed", errors)
    for row in value_attempt.get("diagnostic_coefficients", []):
        expect(row.get("accepted_as_selected_coefficient") is False, f"{row.get('coefficient_slot')} overaccepted", errors)
    expect(value_attempt.get("closure_claimed") is False, "value attempt must not claim closure", errors)

    expect(
        decision.get("status") == "BASIS_MAP_CLOSED_COEFFICIENT_FUNCTIONAL_OR_UNIVERSAL_ANCHOR_OPEN",
        "decision status mismatch",
        errors,
    )
    for key in [
        "functional_contract_closed",
        "dynamic_domain_subgate_closed",
        "family_coordinate_subgate_closed",
        "basis_map_to_sector_scaled_magnitude_rows_closed",
    ]:
        expect(decision.get(key) is True, f"decision {key} must be true", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision selected parameter count must be 0", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "decision accepted rows must be 0", errors)
    expect(decision.get("required_charged_generation_row_count") == 9, "decision required rows must be 9", errors)
    for key in [
        "coefficient_functional_closed",
        "minimal_universal_parameter_selection_closed",
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision {key} must be false", errors)

    expect(cutset.get("status") == "NEXT_ATTACK_RTHETA_COEFFICIENT_FUNCTIONAL_OR_UNIVERSAL_ANCHOR", "cutset status mismatch", errors)
    expect(cutset.get("next_required_artifact") == NEXT, "cutset next mismatch", errors)
    expect(len(cutset.get("still_open", [])) == 6, "cutset must list six open targets", errors)
    for value in cutset.get("closed_this_artifact", {}).values():
        expect(value is True, "all cutset local closures must be true", errors)
    expect(cutset.get("closure_claimed") is False, "cutset must not claim closure", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("basis_map_to_sector_scaled_magnitude_rows_closed") is True, "candidate basis map not closed", errors)
    for key in [
        "functional_contract_closed",
        "dynamic_domain_subgate_closed",
        "family_coordinate_subgate_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure {key} must be true", errors)
    expect(closure.get("selected_universal_parameter_count") == 0, "candidate selected parameter count must be 0", errors)
    for key in [
        "coefficient_functional_closed",
        "minimal_universal_parameter_selection_closed",
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure {key} must be false", errors)

    expect("basis map to sector-scaled magnitude rows closed: true" in note, "note basis-map line missing", errors)
    expect("charged basis rows emitted                      : 9/9" in note, "note charged rows line missing", errors)
    expect("coefficient functional closed                   : false" in note, "note coefficient guard missing", errors)

    if errors:
        print("RTheta value-row basis-map audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta value-row basis-map audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
