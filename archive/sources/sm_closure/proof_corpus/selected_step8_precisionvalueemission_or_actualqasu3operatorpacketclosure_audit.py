"""Audit Step 8 precision-value/operator-packet route execution boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECISION_ROUTE = PACKET_DIR / "step8_precision_value_route_status.packet.json"
OPERATOR_ROUTE = PACKET_DIR / "step8_operator_source_slot_closure.packet.json"
TRUE_BOUNDARY = PACKET_DIR / "step8_dynamic_true_equivalence_boundary.packet.json"
CLOSURE_BOUNDARY = PACKET_DIR / "step8_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step8_to_step9_handoff.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step8_PrecisionValueEmission_or_ActualQaSU3OperatorPacketClosure_v1.md"

STATUS = (
    "MTT_SELECTED_STEP8_PRECISIONVALUEEMISSION_OR_ACTUALQASU3OPERATORPACKETCLOSURE_"
    "CLOSED_SOURCE_SLOTS_DYNAMIC_VALUES_OPEN"
)
NEXT = "MTT_Selected_Step9_DynamicQaSU3C1Response_or_PrecisionProfileCompletion_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    precision = load(PRECISION_ROUTE)
    operator = load(OPERATOR_ROUTE)
    true_boundary = load(TRUE_BOUNDARY)
    boundary = load(CLOSURE_BOUNDARY)
    handoff = load(HANDOFF)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(precision, errors, "precision route", closure=True)
    guard(operator, errors, "operator route", closure=True)
    guard(true_boundary, errors, "true boundary", closure=True)
    guard(boundary, errors, "closure boundary", closure=False)
    guard(handoff, errors, "handoff", closure=False)

    expect(precision.get("partial_precision_values_emitted") is True, "partial precision values missing", errors)
    expect(precision.get("minimal_local_QFT_value_suite_filled") is True, "minimal local QFT suite missing", errors)
    expect(precision.get("precision_observable_table_closed") is False, "precision observable table overclosed", errors)
    expect(precision.get("full_precision_observable_value_table_closed") is False, "full precision table overclosed", errors)
    expect(precision.get("published_or_reconstructed_profile_likelihood_closed") is False, "profile likelihood overclosed", errors)

    expect(operator.get("operator_source_slots_closed") == 8, "operator slot closed count mismatch", errors)
    expect(operator.get("operator_source_slots_remaining") == 0, "operator slots remain open", errors)
    expect(operator.get("source_slot_layer_closed") is True, "source slot layer not closed", errors)
    expect(operator.get("all_operator_source_slots_closed") is True, "all operator slots not closed", errors)
    expect(
        operator.get("finite_determinant_heat_spectrum_or_torsion_response_closed") is True,
        "heat/torsion slot not closed",
        errors,
    )
    expect(operator.get("finite_heat_spectrum_response_emitted") is True, "heat response not emitted", errors)
    expect(
        operator.get("finite_positive_complement_pseudodeterminant_emitted") is True,
        "pseudodeterminant not emitted",
        errors,
    )
    invariants = operator.get("selected_finite_invariants", {})
    expect(invariants.get("total_positive_dimension") == 170, "total positive dimension mismatch", errors)
    expect(invariants.get("operator_source_slots_closed") is None, "invariants should not contain slot count", errors)
    expect(operator.get("actual_dynamic_QaSU3_operator_packet_closed") is False, "dynamic QaSU3 overclosed", errors)
    expect(operator.get("smooth_analytic_torsion_closed") is False, "smooth torsion overclosed", errors)
    expect(operator.get("full_S2_value_emission_closed") is False, "full S2 overclosed", errors)
    expect(operator.get("primitive_C1_response_closed") is False, "primitive C1 overclosed", errors)
    expect(
        operator.get("selected_dotD_alpha1_source_identity_closed") is False,
        "dotD alpha1 source identity overclosed",
        errors,
    )

    expect(true_boundary.get("VSD01_dynamic_tensor_subgate_closed") is True, "VSD01 dynamic subgate missing", errors)
    expect(
        true_boundary.get("transition_rhoE_or_Cech_Dolbeault_DE_data_closed") is True,
        "transition DE trace slot missing",
        errors,
    )
    expect(
        true_boundary.get("actual_dynamic_QaSU3_operator_packet_closed") is False,
        "true boundary dynamic QaSU3 overclosed",
        errors,
    )
    expect(
        true_boundary.get("accepted_Yukawa_Higgs_RG_value_layer_closed") is False,
        "Yukawa/Higgs value layer overclosed",
        errors,
    )
    expect(true_boundary.get("true_SM_equivalence_closed") is False, "true boundary true SM overclosed", errors)
    expect(true_boundary.get("full_no_knob_closed") is False, "true boundary no-knob overclosed", errors)
    expect(len(true_boundary.get("true_SM_equivalence_still_requires", [])) == 5, "remaining requirement count mismatch", errors)

    for key in [
        "precision_route_executed",
        "operator_source_slot_route_closed",
        "all_operator_source_slots_closed",
        "source_slot_layer_closed",
        "step8_closed_for_plan_contract",
    ]:
        expect(boundary.get(key) is True, f"boundary missing: {key}", errors)
    expect(boundary.get("precision_route_full_closure") is False, "boundary precision route overclosed", errors)
    expect(boundary.get("operator_source_slots_closed") == 8, "boundary slot count mismatch", errors)
    expect(boundary.get("operator_source_slots_remaining") == 0, "boundary remaining slot mismatch", errors)
    expect(boundary.get("actual_dynamic_QaSU3_operator_packet_closed") is False, "boundary dynamic QaSU3 overclosed", errors)
    expect(boundary.get("true_SM_equivalence_closed") is False, "boundary true SM overclosed", errors)
    expect(boundary.get("full_no_knob_closed") is False, "boundary no-knob overclosed", errors)

    expect(handoff.get("completed_step") == 8, "handoff completed step mismatch", errors)
    expect(handoff.get("next_step") == 9, "handoff next step mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    for key in [
        "actual_dynamic_QaSU3_operator_packet",
        "selected_dotD_alpha1_and_primitive_C1_response_source_identity",
        "full_S2_value_emission_beyond_DE_gap_layer",
        "precision_QFT_observable_functor_with_accepted_RG_threshold_covariance",
        "no_proxy_Yukawa_mixing_value_derivation_for_no_knob_upgrade",
    ]:
        expect(handoff.get("step9_must_close", {}).get(key) is True, f"Step 9 blocker missing: {key}", errors)
    for key in [
        "all_eight_operator_source_slots_closed",
        "selected_finite_heat_spectrum_response",
        "transition_DE_trace_slot",
        "VSD01_dynamic_first_response_layer",
        "partial_precision_values",
    ]:
        expect(handoff.get("step9_can_reuse", {}).get(key) is True, f"Step 9 reuse missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(handoff.get("step9_must_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step8_closed_for_plan_contract") is True, "candidate Step 8 closure missing", errors)
    expect(decision.get("precision_route_executed") is True, "candidate precision route missing", errors)
    expect(decision.get("precision_route_full_closure") is False, "candidate precision route overclosed", errors)
    expect(decision.get("operator_source_slot_route_closed") is True, "candidate operator route missing", errors)
    expect(decision.get("all_operator_source_slots_closed") is True, "candidate all slots not closed", errors)
    expect(decision.get("operator_source_slots_closed") == 8, "candidate slot count mismatch", errors)
    expect(decision.get("operator_source_slots_remaining") == 0, "candidate remaining slots mismatch", errors)
    expect(decision.get("actual_dynamic_QaSU3_operator_packet_closed") is False, "candidate dynamic QaSU3 overclosed", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "candidate true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "candidate no-knob overclosed", errors)
    expect(data.get("step8_contract_closure_claimed") is True, "candidate Step 8 local claim missing", errors)
    expect(data.get("operator_source_slot_layer_closure_claimed") is True, "candidate source-slot claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM claim overclosed", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob claim overclosed", errors)

    expect(cert.get("step8_contract_closure_claimed") is True, "certificate Step 8 local claim missing", errors)
    expect(cert.get("operator_source_slot_layer_closure_claimed") is True, "certificate source-slot claim missing", errors)
    expect(cert.get("all_operator_source_slots_closed") is True, "certificate all slots not closed", errors)
    expect(cert.get("operator_source_slots_closed") == 8, "certificate slot count mismatch", errors)
    expect(cert.get("operator_source_slots_remaining") == 0, "certificate remaining slots mismatch", errors)
    expect(cert.get("actual_dynamic_QaSU3_operator_packet_closed") is False, "certificate dynamic QaSU3 overclosed", errors)
    expect(cert.get("true_SM_equivalence_claimed") is False, "certificate true SM claim overclosed", errors)
    expect(cert.get("full_no_knob_closure_claimed") is False, "certificate no-knob claim overclosed", errors)

    expect("Step 8 is closed as route execution and source-slot closure" in note, "note missing Step 8 closure", errors)
    expect("operator source slots closed          : 8" in note, "note missing slot count", errors)
    expect("operator source slots remaining       : 0" in note, "note missing remaining count", errors)
    expect("actual dynamic Qa/SU3 packet closed   : false" in note, "note missing dynamic guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 8 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 8 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
