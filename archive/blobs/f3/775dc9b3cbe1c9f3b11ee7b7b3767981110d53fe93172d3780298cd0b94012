"""Audit R_theta matter-slot routing or primitive-C1 no-need theorem packet."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem.py"

SLUG = "selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaMatterSlotRouting_or_PrimitiveC1NoNeedTheorem_v1.md"

ROUTING_IMPORT = PACKET_DIR / "rtheta_static_matterslot_routing_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_matterslot_routing.packet.json"
PRIMITIVE_GATE = PACKET_DIR / "primitive_c1_noneed_or_overlap_gate.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_matterslot_routing_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_matterslot_routing_recheck.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_MATTERSLOTROUTING_OR_PRIMITIVEC1NONEEDTHEOREM_"
    "CLOSED_STATIC_ROUTING_PRIMITIVE_OPEN"
)
NEXT = "MTT_Selected_RThetaPrimitiveC1Overlap_or_PiNoNeedTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    routing = load(ROUTING_IMPORT)
    pi = load(PI_RECHECK)
    primitive = load(PRIMITIVE_GATE)
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
        routing.get("status") == "STATIC_MATTERSLOT_ROUTING_IMPORTED_FOR_RTHETA_SLOT_OWNERSHIP",
        "routing import status mismatch",
        errors,
    )
    for key in [
        "static_matter_slot_routing_closed",
        "sufficient_for_Rtheta_slot_ownership",
        "old_rho_s_invariant_nogo_preserved",
        "closure_claimed",
    ]:
        expect(routing.get(key) is True, f"routing import did not close: {key}", errors)
    expect(routing.get("dynamic_C1_promoted") is False, "dynamic C1 overpromoted by routing import", errors)
    expect(routing["selected_10M_clock_readout"]["sectors"] == ["u", "e"], "10M route mismatch", errors)
    expect(routing["selected_bar5M_shift_readout"]["sectors"] == ["d"], "bar5 route mismatch", errors)
    expect(routing["selected_1M_Dirac_shift_readout"]["sectors"] == ["nuD"], "1M route mismatch", errors)
    expect(routing["selected_phase_shift_partition"]["phase"] == ["u", "e"], "phase partition mismatch", errors)
    expect(routing["selected_phase_shift_partition"]["shift"] == ["d", "nuD"], "shift partition mismatch", errors)

    expect(
        primitive.get("status") == "PRIMITIVE_C1_OVERLAP_OR_NONEED_THEOREM_STILL_OPEN",
        "primitive gate status mismatch",
        errors,
    )
    for key in [
        "primitive_C1_overlap_contractions_closed",
        "primitive_C1_no_need_theorem_closed",
        "primitive_C1_or_no_need_gate_closed",
        "closure_claimed",
    ]:
        expect(primitive.get(key) is False, f"primitive gate overclosed: {key}", errors)
    expect(
        "selected_primitive_C1_contractions" in primitive.get("open_value_sources", []),
        "missing primitive C1 blocker",
        errors,
    )

    expect(
        pi.get("status") == "PI_RTHETA_RECHECKED_MATTERSLOT_ROUTING_CLOSED_PRIMITIVE_C1_OPEN",
        "Pi recheck status mismatch",
        errors,
    )
    expect(
        pi.get("retired_missing_primitives")
        == ["selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership"],
        "retired matter-slot primitive mismatch",
        errors,
    )
    expect(
        pi.get("new_minimal_missing_primitives")
        == ["primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta"],
        "new missing primitive list mismatch",
        errors,
    )
    tests = pi.get("component_tests_after_matterslot_routing", {})
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
        "selected_matter_slot_routing_available",
        "selected_static_matter_slot_readout_available",
    ]:
        expect(tests.get(key) is True, f"Pi component should be true: {key}", errors)
    expect(tests.get("primitive_C1_overlap_or_no_need_available") is False, "primitive component overclosed", errors)
    expect(pi.get("Pi_Rtheta_closed") is False, "Pi_Rtheta overclosed", errors)
    expect(pi.get("accepted_coefficient_value_count") == 0, "Pi accepted coefficient values", errors)
    expect(pi.get("closure_claimed") is False, "Pi recheck overclaimed", errors)

    expect(value.get("status") == "RTHETA_VALUES_STILL_REJECTED_PRIMITIVE_C1_OPEN", "value gate status mismatch", errors)
    expect(value.get("matter_slot_routing_closed") is True, "value gate missing matter routing", errors)
    for key in [
        "primitive_C1_or_no_need_gate_closed",
        "Pi_Rtheta_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "closure_claimed",
    ]:
        expect(value.get(key) is False, f"value gate overclosed: {key}", errors)
    expect(value.get("accepted_coefficient_value_count") == 0, "value gate accepted coefficients", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_RTHETA_PRIMITIVE_C1_OVERLAP_OR_PI_NONEED",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("still_open") == pi.get("new_minimal_missing_primitives"), "cutset open list mismatch", errors)
    expect(
        cutset.get("closed_now", {}).get(
            "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership"
        )
        is True,
        "cutset did not close matter-slot blocker",
        errors,
    )
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "stationary_sector_transfer_closed",
        "selected_stationary_rho_s_closed",
        "dotD_alpha1_transport_subgate_closed",
        "matter_slot_routing_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure should be true: {key}", errors)
    for key in [
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
    expect(cert.get("matter_slot_routing_closed") is True, "certificate routing mismatch", errors)
    expect(cert.get("Pi_Rtheta_closed") is False, "certificate Pi overclosed", errors)

    expect("static matter-slot routing closed             : true" in note, "note missing routing closure", errors)
    expect("primitive C1 overlap/no-need gate closed      : false" in note, "note missing primitive guard", errors)
    expect("Pi_Rtheta closed                              : false" in note, "note missing Pi guard", errors)
    expect("accepted coefficient values                   : 0" in note, "note missing zero-value guard", errors)

    if errors:
        print("RTheta matter-slot routing audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta matter-slot routing audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
