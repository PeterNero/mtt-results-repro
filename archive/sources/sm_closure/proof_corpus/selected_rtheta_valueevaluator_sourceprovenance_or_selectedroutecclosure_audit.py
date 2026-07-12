"""Audit R_theta value-evaluator source-provenance / selected Route-C closure attempt."""

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
BUILDER = (
    ROOT
    / "scripts"
    / "build_selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure.py"
)

SLUG = "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueEvaluatorSourceProvenance_or_SelectedRouteCClosure_v1.md"

ALPHA1_IMPORT = PACKET_DIR / "rtheta_alpha1_dotd_provenance_import.packet.json"
READINESS = PACKET_DIR / "rtheta_value_evaluator_readiness_after_alpha1_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_alpha1_import.packet.json"
SELECTED_ROUTE_C = PACKET_DIR / "selected_routec_closure_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_value_evaluator_source_provenance.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_VALUEEVALUATORSOURCEPROVENANCE_OR_SELECTEDROUTECCLOSURE_"
    "IMPORTED_ALPHA1_DOTD_PI_OPEN"
)
NEXT = "MTT_Selected_RThetaPiKernel_from_SelectedHYMConnection_or_BNBasisEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    alpha = load(ALPHA1_IMPORT)
    readiness = load(READINESS)
    pi = load(PI_RECHECK)
    routec = load(SELECTED_ROUTE_C)
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

    expect(
        alpha.get("status") == "THEOREM_DERIVED_ALPHA1_DOTD_REPLAY_IMPORTED_FOR_RTHETA",
        "alpha import status mismatch",
        errors,
    )
    for key in [
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "honest_dotD_alpha1_replay",
        "du_dalpha1_equals_h_ext",
        "accepted_for_rtheta_evaluator_readiness",
    ]:
        expect(alpha.get(key) is True, f"alpha import missing: {key}", errors)
    expect(alpha.get("lambda_alpha1") == 1.0, "lambda_alpha1 mismatch", errors)
    expect(alpha.get("N_alpha1_h_ext") == 1.0, "N_alpha1 mismatch", errors)
    expect(alpha.get("tangent_residual_l2") == 0.0, "alpha residual mismatch", errors)
    expect("theta_coeff values" in alpha.get("does_not_emit", []), "alpha import must not emit theta coefficients", errors)
    expect("lambda_H" in alpha.get("does_not_emit", []), "alpha import must not emit lambda_H", errors)
    expect(alpha.get("closure_claimed") is True, "alpha local import should close", errors)

    expect(
        readiness.get("status") == "RTHETA_VALUE_EVALUATOR_READINESS_ALPHA1_IMPORTED_DE_GREEN_OPEN",
        "readiness status mismatch",
        errors,
    )
    expect(readiness.get("previous_readiness_present_count") == 4, "previous readiness count mismatch", errors)
    expect(readiness.get("readiness_present_count") == 5, "readiness did not advance to 5", errors)
    expect(readiness.get("readiness_required_count") == 7, "readiness required count mismatch", errors)
    expect(
        readiness.get("still_open_rows") == [
            "coherent_spectral_projector_retention",
            "selected_DE_Riesz_Green_dotD",
        ],
        "readiness open rows mismatch",
        errors,
    )
    expect(readiness.get("closed_now", {}).get("honest_dotD_replay_without_lifted_flags") is True, "dotD row not closed", errors)
    dotd_rows = [row for row in readiness.get("readiness_rows", []) if row.get("id") == "honest_dotD_replay_without_lifted_flags"]
    expect(len(dotd_rows) == 1, "dotD readiness row missing", errors)
    if dotd_rows:
        row = dotd_rows[0]
        expect(row.get("present_before_alpha1_import") is False, "dotD row should be false before import", errors)
        expect(row.get("present") is True, "dotD row should be true after import", errors)
    for key in [
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "closure_claimed",
    ]:
        expect(readiness.get(key) is False, f"readiness overclosed: {key}", errors)
    expect(readiness.get("accepted_coefficient_value_count") == 0, "readiness accepted coefficient values", errors)

    expect(
        pi.get("status") == "PI_RTHETA_RECHECKED_ALPHA1_NOT_ACTIVE_DE_GREEN_BASIS_OPEN",
        "Pi recheck status mismatch",
        errors,
    )
    expect(pi.get("alpha1_dotD_blocker_retired") is True, "alpha1 blocker not retired in Pi recheck", errors)
    expect(pi.get("Pi_Rtheta_closed") is False, "Pi_Rtheta overclosed", errors)
    expect(pi.get("accepted_coefficient_value_count") == 0, "Pi recheck accepted coefficient values", errors)
    tests = pi.get("component_tests_after_import", {})
    for key in [
        "static_block_projectors_available",
        "q79_polarization_available",
        "sector_projector_matrices_available",
        "stationary_projector_source_verified",
        "honest_dotD_alpha1_replay_imported",
    ]:
        expect(tests.get(key) is True, f"Pi component should be true: {key}", errors)
    for key in [
        "coherent_spectral_projectors_available",
        "selected_DE_Riesz_Green_available",
        "selected_HYM_connection_representative_available",
        "selected_finite_basis_quadrature_error_contract_available",
    ]:
        expect(tests.get(key) is False, f"Pi component overclosed: {key}", errors)
    expect(
        pi.get("minimal_missing_primitives") == [
            "gauge_fixed_selected_HYM_connection_representative",
            "selected_finite_basis_quadrature_error_contract",
            "selected_D_E_Riesz_Green_from_connection",
            "coherent_spectral_zero_mode_projector_retention",
        ],
        "Pi missing primitive list mismatch",
        errors,
    )
    expect("honest_dotD_replay_without_lifted_flags" in pi.get("no_longer_active_blockers", []), "retired dotD blocker missing", errors)
    expect(pi.get("closure_claimed") is False, "Pi recheck overclaimed", errors)

    expect(
        routec.get("status") == "SELECTED_ROUTEC_CLOSURE_ADVANCED_ALPHA1_IMPORTED_SOURCE_VALUES_OPEN",
        "Route-C status mismatch",
        errors,
    )
    progress = routec.get("source_provenance_progress", {})
    expect(progress.get("alpha1_dotD_source_provenance") is True, "Route-C alpha1 progress missing", errors)
    for key in [
        "HYM_connection_representative",
        "quotient_valid_B_N_basis",
        "selected_DE_Riesz_Green",
        "coherent_spectral_projectors",
        "primitive_C1_contractions",
    ]:
        expect(progress.get(key) is False, f"Route-C progress overclosed: {key}", errors)
    for key in [
        "formal_lift_accepted_as_proof",
        "proof_promotion_allowed",
        "selected_routec_closed",
        "selected_value_evaluator_closed",
        "closure_claimed",
    ]:
        expect(routec.get(key) is False, f"Route-C overclosed: {key}", errors)
    expect(routec.get("formal_lift_lower_validators_all_pass") is True, "formal-lift lower validators missing", errors)
    expect(routec.get("formal_lift_promotion_passes") is True, "formal-lift diagnostic missing", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_PI_RTHETA_FROM_SELECTED_HYM_CONNECTION_OR_BN_BASIS_EMISSION",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    for value in cutset.get("closed_now", {}).values():
        expect(value is True, "all cutset closures should be true", errors)
    expect(cutset.get("still_open") == pi.get("minimal_missing_primitives"), "cutset open list mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("value_evaluator_readiness_present_count") == 5, "candidate readiness count mismatch", errors)
    expect(closure.get("value_evaluator_readiness_required_count") == 7, "candidate required count mismatch", errors)
    expect(closure.get("alpha1_dotd_provenance_imported") is True, "candidate alpha import missing", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficient values", errors)
    for key in [
        "Pi_Rtheta_closed",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not recorded", errors)
    expect(cert.get("value_evaluator_readiness_present_count") == 5, "certificate readiness count mismatch", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "certificate accepted values mismatch", errors)

    expect("alpha1/dotD provenance imported       : true" in note, "note missing alpha import", errors)
    expect("value evaluator readiness             : 5/7" in note, "note missing 5/7 readiness", errors)
    expect("Pi_Rtheta closed                      : false" in note, "note missing Pi guard", errors)
    expect("accepted coefficient values           : 0" in note, "note missing zero values guard", errors)

    if errors:
        print("RTheta value-evaluator source-provenance audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta value-evaluator source-provenance audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
