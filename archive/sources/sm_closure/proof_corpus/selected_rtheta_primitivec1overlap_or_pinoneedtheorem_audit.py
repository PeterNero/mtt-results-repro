"""Audit R_theta primitive-C1 overlap import or Pi no-need theorem packet."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_primitivec1overlap_or_pinoneedtheorem.py"

SLUG = "selected_rtheta_primitivec1overlap_or_pinoneedtheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaPrimitiveC1Overlap_or_PiNoNeedTheorem_v1.md"

PRIMITIVE_IMPORT = PACKET_DIR / "rtheta_primitive_c1_overlap_import.packet.json"
DEPENDENCY_AUDIT = PACKET_DIR / "pi_rtheta_dependency_audit_after_primitive_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_primitive_c1_import.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_pi_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_pi_closure.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_PRIMITIVEC1OVERLAP_OR_PINONEEDTHEOREM_"
    "IMPORTED_PRIMITIVE_C1_PI_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaValueEvaluatorExecution_or_ThresholdResponseInstantiation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    primitive = load(PRIMITIVE_IMPORT)
    dependency = load(DEPENDENCY_AUDIT)
    pi = load(PI_RECHECK)
    value = load(VALUE_GATE)
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
        primitive.get("status") == "PRIMITIVE_C1_OVERLAP_IMPORTED_FROM_SAME_SOURCE_DYNAMIC_PACKET",
        "primitive import status mismatch",
        errors,
    )
    expect(primitive.get("route") == "direct primitive C1 overlap import, not no-need theorem", "wrong primitive route", errors)
    for key in [
        "primitive_C1_overlap_contractions_closed",
        "primitive_C1_or_no_need_gate_closed",
        "closure_claimed",
    ]:
        expect(primitive.get(key) is True, f"primitive import did not close: {key}", errors)
    expect(primitive.get("primitive_C1_no_need_theorem_closed") is False, "no-need theorem overclaimed", errors)
    expect(primitive.get("selected_first_response_layer_only") is True, "first-response guard missing", errors)
    same_source = primitive.get("same_source_flags", {})
    for key in ["selected_emitted", "same_source", "theorem_derived"]:
        expect(same_source.get(key) is True, f"primitive same-source flag missing: {key}", errors)
    for item in [
        "theta_coeff numeric values",
        "lambda_H",
        "Yukawa magnitudes",
        "true SM equivalence",
        "full no-knob closure",
    ]:
        expect(item in primitive.get("does_not_emit", []), f"primitive import overemits or omits guard: {item}", errors)

    expect(
        dependency.get("status") == "PI_RTHETA_DEPENDENCIES_ALL_PRESENT_VALUE_EVALUATOR_SEPARATE",
        "dependency audit status mismatch",
        errors,
    )
    for key, value_now in dependency.get("dependency_classes", {}).items():
        expect(value_now is True, f"dependency not closed: {key}", errors)
    expect(
        dependency.get("coefficient_functional_skeleton_closed") is True,
        "coefficient skeleton not closed in dependency audit",
        errors,
    )
    expect(
        "selected threshold response functional instantiated"
        in dependency.get("value_evaluator_separate_requirements", []),
        "threshold response not separated",
        errors,
    )

    expect(
        pi.get("status") == "PI_RTHETA_RECHECKED_PRIMITIVE_C1_IMPORTED_CLOSED",
        "Pi recheck status mismatch",
        errors,
    )
    expect(
        pi.get("retired_missing_primitives")
        == ["primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta"],
        "retired primitive mismatch",
        errors,
    )
    expect(pi.get("new_minimal_missing_primitives") == [], "Pi still has missing primitives", errors)
    tests = pi.get("component_tests_after_primitive_c1_import", {})
    for key in [
        "coherent_spectral_projectors_available",
        "rank2_to_sector_transfer_values_available",
        "selected_DE_Riesz_Green_available",
        "selected_sector_B_N_basis_quadrature_error_contract_available",
        "validator_ready_sector_payload_available",
        "selected_dotD_alpha1_imported_crossrepo",
        "selected_dotD_transport_derivative_local_to_transported_packet",
        "selected_dotD_alpha1_driver_normalization_available",
        "selected_matter_slot_routing_available",
        "selected_static_matter_slot_readout_available",
        "primitive_C1_overlap_or_no_need_available",
        "selected_primitive_C1_overlap_contractions_available",
        "selected_dynamic_matter_overlap_packet_validates",
    ]:
        expect(tests.get(key) is True, f"Pi component should be true: {key}", errors)
    expect(pi.get("Pi_Rtheta_closed") is True, "Pi_Rtheta not closed", errors)
    expect(pi.get("accepted_coefficient_value_count") == 0, "Pi accepted coefficient values", errors)
    expect(pi.get("closure_claimed") is True, "Pi local closure not claimed", errors)

    expect(
        value.get("status") == "RTHETA_PI_CLOSED_VALUES_STILL_REJECTED_THRESHOLD_RESPONSE_OPEN",
        "value gate status mismatch",
        errors,
    )
    expect(value.get("Pi_Rtheta_closed") is True, "value gate missing Pi closure", errors)
    expect(value.get("coefficient_functional_skeleton_closed") is True, "value gate missing skeleton", errors)
    for key in [
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "profile_response_closed",
        "Yukawa_magnitudes_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(value.get(key) is False, f"value gate overclosed: {key}", errors)
    expect(value.get("accepted_coefficient_value_count") == 0, "value gate accepted coefficients", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_RTHETA_VALUE_EVALUATOR_OR_THRESHOLD_RESPONSE",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closed_now", {}).get("Pi_Rtheta") is True, "cutset did not close Pi", errors)
    expect(
        "selected_threshold_response_functional_instantiated" in cutset.get("still_open", []),
        "cutset missing threshold response blocker",
        errors,
    )
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "stationary_sector_transfer_closed",
        "selected_stationary_rho_s_closed",
        "dotD_alpha1_transport_subgate_closed",
        "matter_slot_routing_closed",
        "primitive_C1_or_no_need_gate_closed",
        "primitive_C1_overlap_contractions_closed",
        "Pi_Rtheta_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure should be true: {key}", errors)
    expect(closure.get("primitive_C1_no_need_theorem_closed") is False, "candidate overclaimed no-need theorem", errors)
    for key in [
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "profile_response_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not recorded", errors)
    expect(cert.get("Pi_Rtheta_closed") is True, "certificate Pi not closed", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "certificate accepted coefficients", errors)

    expect("primitive C1 overlap contractions closed      : true" in note, "note missing primitive closure", errors)
    expect("Pi_Rtheta closed                              : true" in note, "note missing Pi closure", errors)
    expect("accepted coefficient values                   : 0" in note, "note missing zero-value guard", errors)
    expect("selected threshold response instantiated      : false" in note, "note missing threshold guard", errors)

    if errors:
        print("RTheta primitive-C1/Pi audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta primitive-C1/Pi audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
