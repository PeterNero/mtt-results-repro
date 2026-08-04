"""Audit R_theta dynamic Pi evaluator or matter-slot routing closure packet."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure.py"

SLUG = "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaDynamicPiEvaluator_or_MatterSlotRoutingClosure_v1.md"

DOTD_MERGE = PACKET_DIR / "rtheta_dotd_transport_alpha1_driver_merge.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_dotd_transport_merge.packet.json"
ROUTING_GATE = PACKET_DIR / "matter_slot_routing_and_primitive_c1_gate.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_dynamic_pi_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_pi_recheck.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_DYNAMICPIEVALUATOR_OR_MATTERSLOTROUTINGCLOSURE_"
    "CLOSED_DOTD_ALPHA1_TRANSPORT_ROUTING_OPEN"
)
NEXT = "MTT_Selected_RThetaMatterSlotRouting_or_PrimitiveC1NoNeedTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    dotd = load(DOTD_MERGE)
    pi = load(PI_RECHECK)
    routing = load(ROUTING_GATE)
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

    expect(dotd.get("status") == "SELECTED_DOTD_ALPHA1_TRANSPORT_PACKET_CLOSED", "dotD merge status mismatch", errors)
    for key in [
        "local_dotD_transport_formula_closed",
        "alpha1_driver_normalization_imported",
        "selected_dotD_transport_derivative_on_transported_projector_packet",
        "closure_claimed",
    ]:
        expect(dotd.get(key) is True, f"dotD merge did not close: {key}", errors)
    expect(dotd.get("lambda_alpha1") == 1.0, "lambda_alpha1 mismatch", errors)
    expect(dotd.get("N_alpha1_h_ext") == 1.0, "N_alpha1_h_ext mismatch", errors)
    expect(abs(float(dotd.get("tangent_residual_l2", 1.0))) < 1e-12, "alpha1 tangent residual too large", errors)
    for item in [
        "matter-slot routing among u,d,e,N",
        "primitive C1 overlap contractions",
        "selected A/b response matrices",
        "theta_coeff values",
        "lambda_H",
    ]:
        expect(item in dotd.get("does_not_emit", []), f"dotD merge overemits or omits guard: {item}", errors)

    expect(
        routing.get("status") == "MATTER_SLOT_ROUTING_AND_PRIMITIVE_C1_STILL_OPEN",
        "routing gate status mismatch",
        errors,
    )
    expect(routing.get("selected_stationary_source_available") is True, "stationary source not available", errors)
    for key in [
        "matter_slot_routing_closed",
        "primitive_C1_overlap_contractions_closed",
        "primitive_C1_no_need_theorem_closed",
        "primitive_C1_or_no_need_gate_closed",
        "closure_claimed",
    ]:
        expect(routing.get(key) is False, f"routing/C1 gate overclosed: {key}", errors)
    expect(
        "selected_matter_slot_transversality_readout_functional" in routing.get("open_matter_readouts", []),
        "missing matter-slot transversality readout blocker",
        errors,
    )

    expect(
        pi.get("status") == "PI_RTHETA_RECHECKED_DOTD_ALPHA1_TRANSPORT_CLOSED_ROUTING_OPEN",
        "Pi recheck status mismatch",
        errors,
    )
    expect(
        pi.get("retired_missing_primitives")
        == ["selected_dotD_alpha1_transport_derivative_on_transported_projector_packet"],
        "retired dotD primitive mismatch",
        errors,
    )
    expect(
        pi.get("new_minimal_missing_primitives")
        == [
            "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership",
            "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta",
        ],
        "new missing primitive list mismatch",
        errors,
    )
    tests = pi.get("component_tests_after_dotd_transport_merge", {})
    for key in [
        "coherent_spectral_projectors_available",
        "rank2_to_sector_transfer_values_available",
        "selected_DE_Riesz_Green_available",
        "selected_sector_B_N_basis_quadrature_error_contract_available",
        "validator_ready_sector_payload_available",
        "selected_dotD_alpha1_imported_crossrepo",
        "selected_HYM_connection_representative_available",
        "selected_dotD_transport_derivative_local_to_transported_packet",
        "selected_dotD_alpha1_driver_normalization_available",
    ]:
        expect(tests.get(key) is True, f"Pi component should be true: {key}", errors)
    for key in [
        "selected_matter_slot_routing_available",
        "primitive_C1_overlap_or_no_need_available",
    ]:
        expect(tests.get(key) is False, f"Pi component overclosed: {key}", errors)
    expect(pi.get("Pi_Rtheta_closed") is False, "Pi_Rtheta overclosed", errors)
    expect(pi.get("accepted_coefficient_value_count") == 0, "Pi accepted coefficient values", errors)
    expect(pi.get("closure_claimed") is False, "Pi recheck overclaimed", errors)

    expect(
        value.get("status") == "RTHETA_VALUES_STILL_REJECTED_ROUTING_AND_PRIMITIVE_C1_OPEN",
        "value gate status mismatch",
        errors,
    )
    expect(value.get("dotD_alpha1_transport_subgate_closed") is True, "value gate missing dotD closure", errors)
    for key in [
        "matter_slot_routing_closed",
        "primitive_C1_or_no_need_gate_closed",
        "Pi_Rtheta_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "closure_claimed",
    ]:
        expect(value.get(key) is False, f"value gate overclosed: {key}", errors)
    expect(value.get("accepted_coefficient_value_count") == 0, "value gate accepted coefficients", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_RTHETA_MATTER_SLOT_ROUTING_OR_PRIMITIVE_C1_NO_NEED",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("still_open") == pi.get("new_minimal_missing_primitives"), "cutset open list mismatch", errors)
    expect(
        cutset.get("closed_now", {}).get(
            "selected_dotD_alpha1_transport_derivative_on_transported_projector_packet"
        )
        is True,
        "cutset did not close dotD blocker",
        errors,
    )
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "stationary_sector_transfer_closed",
        "selected_stationary_rho_s_closed",
        "dotD_alpha1_transport_subgate_closed",
        "alpha1_driver_normalization_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure should be true: {key}", errors)
    for key in [
        "matter_slot_routing_closed",
        "primitive_C1_or_no_need_gate_closed",
        "Pi_Rtheta_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not recorded", errors)
    expect(cert.get("dotD_alpha1_transport_subgate_closed") is True, "certificate dotD mismatch", errors)
    expect(cert.get("Pi_Rtheta_closed") is False, "certificate Pi overclosed", errors)

    expect("dotD_alpha1 transported-packet subgate closed : true" in note, "note missing dotD closure", errors)
    expect("matter-slot routing closed                    : false" in note, "note missing routing guard", errors)
    expect("primitive C1 overlap/no-need gate closed      : false" in note, "note missing primitive guard", errors)
    expect("Pi_Rtheta closed                              : false" in note, "note missing Pi guard", errors)
    expect("accepted coefficient values                   : 0" in note, "note missing zero-value guard", errors)

    if errors:
        print("RTheta dynamic Pi evaluator audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta dynamic Pi evaluator audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
