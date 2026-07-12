"""Audit R_theta sector-transfer/B_N basis recheck or Pi-kernel closure."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_sectortransferbnbasis_or_pikernelclosure.py"

SLUG = "selected_rtheta_sectortransferbnbasis_or_pikernelclosure"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSectorTransferBNBasis_or_PiKernelClosure_v1.md"

PROJECTOR_IMPORT = PACKET_DIR / "selected_transported_projector_source_import.packet.json"
SECTOR_TRANSFER = PACKET_DIR / "rtheta_sector_transfer_stationary_subgate.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_sector_projector_promotion.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_sector_transfer_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sector_transfer_recheck.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_SECTORTRANSFERBNBASIS_OR_PIKERNELCLOSURE_"
    "IMPORTED_TRANSPORTED_PROJECTORS_DOTD_ROUTING_OPEN"
)
NEXT = "MTT_Selected_RThetaDynamicPiEvaluator_or_MatterSlotRoutingClosure_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    projector = load(PROJECTOR_IMPORT)
    transfer = load(SECTOR_TRANSFER)
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
        projector.get("status") == "TRANSPORTED_STATIONARY_PROJECTOR_SOURCE_IMPORTED",
        "projector import status mismatch",
        errors,
    )
    for key in [
        "selected_projector_source_verified",
        "validator_ready_stationary_rho_s",
        "symbolic_transport_validator_closed",
        "transported_packet_promoted",
        "all_sector_stationary_slots_promoted",
        "accepted_for_rtheta_stationary_pi_subgate",
    ]:
        expect(projector.get(key) is True, f"projector import missing: {key}", errors)
    expect(projector.get("raw_untransported_packet_promoted") is False, "raw B_N overpromoted", errors)
    expect(projector.get("gauge_frame_residual", 1.0) < 1e-12, "gauge frame residual too large", errors)
    expect(projector.get("raw_direct_truncated_residual", 0.0) > 0.1, "raw residual guard missing", errors)
    for item in [
        "selected dotD_alpha1 transport derivative",
        "matter-slot routing among u,d,e,N",
        "primitive C1 overlap contractions",
        "theta_coeff values",
        "lambda_H",
    ]:
        expect(item in projector.get("does_not_emit", []), f"projector import overemits or omits guard: {item}", errors)
    expect(projector.get("closure_claimed") is True, "projector local closure should hold", errors)

    expect(
        transfer.get("status") == "STATIONARY_SECTOR_TRANSFER_AND_RHO_S_CLOSED_DYNAMIC_ROUTING_OPEN",
        "sector transfer status mismatch",
        errors,
    )
    for key in [
        "selected_sector_basis_projector_contract_closed",
        "selected_stationary_rho_s_closed",
        "selected_Riesz_Green_stationary_closed",
        "transported_BN_promoted",
    ]:
        expect(transfer.get(key) is True, f"transfer missing: {key}", errors)
    expect(transfer.get("raw_BN_promoted") is False, "transfer raw B_N overpromoted", errors)
    expect(set(transfer.get("selected_sector_basis_labels", {}).keys()) == {"Q", "u", "d", "L", "e", "N", "H"}, "sector label set mismatch", errors)
    expect(len(transfer.get("remaining_dynamic_requirements", [])) == 3, "dynamic requirement count mismatch", errors)
    expect(transfer.get("closure_claimed") is True, "transfer local closure should hold", errors)

    expect(
        pi.get("status") == "PI_RTHETA_RECHECKED_STATIONARY_PROJECTORS_CLOSED_DYNAMIC_ROUTING_OPEN",
        "Pi recheck status mismatch",
        errors,
    )
    expect(
        pi.get("retired_missing_primitives") == [
            "selected_sector_B_N_basis_quadrature_error_contract",
            "rank2_to_sector_transfer_values",
            "selected_sector_D_E_Riesz_Green_from_connection",
            "coherent_spectral_zero_mode_projector_retention",
        ],
        "retired primitive list mismatch",
        errors,
    )
    expect(
        pi.get("new_minimal_missing_primitives") == [
            "selected_dotD_alpha1_transport_derivative_on_transported_projector_packet",
            "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership",
            "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta",
        ],
        "new missing primitive list mismatch",
        errors,
    )
    tests = pi.get("component_tests_after_sector_projector_promotion", {})
    for key in [
        "coherent_spectral_projectors_available",
        "rank2_to_sector_transfer_values_available",
        "selected_DE_Riesz_Green_available",
        "selected_sector_B_N_basis_quadrature_error_contract_available",
        "validator_ready_sector_payload_available",
        "selected_dotD_alpha1_imported_crossrepo",
        "selected_HYM_connection_representative_available",
    ]:
        expect(tests.get(key) is True, f"Pi component should be true: {key}", errors)
    for key in [
        "selected_dotD_transport_derivative_local_to_transported_packet",
        "selected_matter_slot_routing_available",
    ]:
        expect(tests.get(key) is False, f"Pi component overclosed: {key}", errors)
    expect(pi.get("Pi_Rtheta_closed") is False, "Pi_Rtheta overclosed", errors)
    expect(pi.get("accepted_coefficient_value_count") == 0, "Pi recheck accepted coefficient values", errors)
    expect(pi.get("closure_claimed") is False, "Pi recheck overclaimed", errors)

    expect(value.get("status") == "RTHETA_VALUES_STILL_REJECTED_DYNAMIC_PI_OPEN", "value gate status mismatch", errors)
    expect(value.get("stationary_sector_transfer_closed") is True, "value gate missing stationary transfer", errors)
    for key in [
        "Pi_Rtheta_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "closure_claimed",
    ]:
        expect(value.get(key) is False, f"value gate overclosed: {key}", errors)
    expect(value.get("accepted_coefficient_value_count") == 0, "value gate accepted coefficients", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_RTHETA_DYNAMIC_PI_EVALUATOR_OR_MATTER_SLOT_ROUTING",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("still_open") == pi.get("new_minimal_missing_primitives"), "cutset open list mismatch", errors)
    for value_now in cutset.get("closed_now", {}).values():
        expect(value_now is True, "all cutset closures should be true", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("stationary_sector_transfer_closed") is True, "candidate stationary transfer not closed", errors)
    expect(closure.get("selected_stationary_rho_s_closed") is True, "candidate rho_s not closed", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    for key in [
        "Pi_Rtheta_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not recorded", errors)
    expect(cert.get("stationary_sector_transfer_closed") is True, "certificate transfer mismatch", errors)
    expect(cert.get("Pi_Rtheta_closed") is False, "certificate Pi overclosed", errors)

    expect("transported stationary projector source closed : true" in note, "note missing transported closure", errors)
    expect("selected stationary rho_s closed               : true" in note, "note missing rho closure", errors)
    expect("Pi_Rtheta closed                               : false" in note, "note missing Pi guard", errors)
    expect("accepted coefficient values                    : 0" in note, "note missing zero-value guard", errors)

    if errors:
        print("RTheta sector-transfer/B_N basis audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta sector-transfer/B_N basis audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
