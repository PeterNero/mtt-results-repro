"""Audit R_theta Pi-kernel recheck from selected HYM connection / B_N basis emission."""

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
    / "build_selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission.py"
)

SLUG = "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaPiKernel_from_SelectedHYMConnection_or_BNBasisEmission_v1.md"

HYM_IMPORT = PACKET_DIR / "selected_hym_connection_subgate_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_hym_connection_import.packet.json"
BN_GATE = PACKET_DIR / "bn_basis_and_sector_transfer_gate.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_pi_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hym_connection_pi_recheck.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_PIKERNEL_FROM_SELECTEDHYMCONNECTION_OR_BNBASISEMISSION_"
    "IMPORTED_HYM_CONNECTION_SECTOR_BASIS_OPEN"
)
NEXT = "MTT_Selected_RThetaSectorTransferBNBasis_or_PiKernelClosure_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    hym = load(HYM_IMPORT)
    pi = load(PI_RECHECK)
    bn = load(BN_GATE)
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
        hym.get("status") == "SELECTED_RANK2_HYM_CONNECTION_IMPORTED_FOR_RTHETA_PI_GATE",
        "HYM import status mismatch",
        errors,
    )
    expect(hym.get("selected_HYM_connection_representative_available") is True, "HYM connection not available", errors)
    expect(hym.get("accepted_for_rtheta_pi_source_subgate") is True, "HYM subgate not accepted", errors)
    expect(hym.get("solver_converged") is True, "HYM solve not converged", errors)
    expect(hym.get("final_residual_l2", 1.0) < 1e-10, "HYM residual too large", errors)
    expect(hym.get("diagonal_End0_DE_formula_extracted") is True, "End0 DE not extracted", errors)
    expect(hym.get("full_diagonal_End0_Green_closed") is True, "End0 Green not closed", errors)
    for blocked in [
        "selected sector B_N basis/quadrature/error contract",
        "rank2-to-sector transfer values",
        "sector-ready D_E/Riesz/Green/dotD/C1 payload",
        "Pi_Rtheta",
        "theta_coeff values",
        "lambda_H",
    ]:
        expect(blocked in hym.get("does_not_emit", []), f"HYM import overemits or omits guard: {blocked}", errors)
    expect(hym.get("closure_claimed") is True, "HYM import should close locally", errors)

    expect(
        pi.get("status") == "PI_RTHETA_RECHECKED_HYM_CONNECTION_CLOSED_SECTOR_TRANSFER_OPEN",
        "Pi recheck status mismatch",
        errors,
    )
    expect(pi.get("selected_HYM_connection_subgate_closed") is True, "Pi subgate not closed", errors)
    expect(pi.get("Pi_Rtheta_closed") is False, "Pi_Rtheta overclosed", errors)
    expect(pi.get("accepted_coefficient_value_count") == 0, "Pi recheck accepted values", errors)
    expect(
        pi.get("retired_missing_primitives") == ["gauge_fixed_selected_HYM_connection_representative"],
        "retired primitive mismatch",
        errors,
    )
    expect(
        pi.get("minimal_missing_primitives") == [
            "selected_sector_B_N_basis_quadrature_error_contract",
            "rank2_to_sector_transfer_values",
            "selected_sector_D_E_Riesz_Green_from_connection",
            "coherent_spectral_zero_mode_projector_retention",
        ],
        "Pi missing primitive list mismatch",
        errors,
    )
    tests = pi.get("component_tests_after_hym_import", {})
    for key in [
        "static_block_projectors_available",
        "q79_polarization_available",
        "sector_projector_matrices_available",
        "stationary_projector_source_verified",
        "honest_dotD_alpha1_replay_imported",
        "selected_HYM_connection_representative_available",
        "selected_rank2_End0_DE_Green_lane_available",
    ]:
        expect(tests.get(key) is True, f"Pi component should be true: {key}", errors)
    for key in [
        "selected_finite_basis_quadrature_error_contract_available",
        "selected_DE_Riesz_Green_available",
        "coherent_spectral_projectors_available",
        "rank2_to_sector_transfer_values_available",
        "validator_ready_sector_payload_available",
    ]:
        expect(tests.get(key) is False, f"Pi component overclosed: {key}", errors)
    expect(pi.get("closure_claimed") is False, "Pi recheck overclaimed", errors)

    expect(
        bn.get("status") == "BN_SCAFFOLD_AND_END0_CARRIER_PRESENT_SELECTED_SECTOR_TRANSFER_OPEN",
        "BN gate status mismatch",
        errors,
    )
    for key in [
        "smooth_BN_scaffold",
        "diagnostic_DE_on_BN_matrix",
        "End0_tensor_carrier_or_functor_support",
        "diagonal_rank2_End0_source",
    ]:
        expect(bn.get("support_present", {}).get(key) is True, f"BN support missing: {key}", errors)
    for key in [
        "selected_sector_B_N_basis",
        "selected_quadrature_truncation_error_for_sector_payload",
        "rank2_to_sector_transfer_values",
        "sector_ready_rhoE_DE_Riesz_Green_dotD_C1",
    ]:
        expect(bn.get("selected_values_open", {}).get(key) is True, f"BN selected value not open: {key}", errors)
    expect(bn.get("closure_claimed") is False, "BN gate overclaimed", errors)

    expect(value.get("status") == "RTHETA_VALUE_GATE_PI_OPEN_VALUES_REJECTED", "value gate status mismatch", errors)
    expect(value.get("selected_HYM_connection_subgate_closed") is True, "value gate missing HYM subgate", errors)
    for key in [
        "Pi_Rtheta_closed",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "selected_threshold_response_functional_instantiated",
        "closure_claimed",
    ]:
        expect(value.get(key) is False, f"value gate overclosed: {key}", errors)
    expect(value.get("accepted_coefficient_value_count") == 0, "value gate accepted coefficients", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_RTHETA_SECTOR_TRANSFER_BN_BASIS_OR_PIKERNEL_CLOSURE",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("still_open") == pi.get("minimal_missing_primitives"), "cutset open list mismatch", errors)
    for value_now in cutset.get("closed_now", {}).values():
        expect(value_now is True, "all cutset local closures should be true", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("selected_HYM_connection_subgate_closed") is True, "candidate HYM subgate not closed", errors)
    expect(closure.get("diagonal_End0_DE_Green_lane_closed") is True, "candidate End0 lane not closed", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
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
    expect(cert.get("selected_HYM_connection_subgate_closed") is True, "certificate HYM subgate mismatch", errors)
    expect(cert.get("Pi_Rtheta_closed") is False, "certificate Pi overclosed", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "certificate accepted values mismatch", errors)

    expect("selected HYM connection subgate closed : true" in note, "note missing HYM subgate line", errors)
    expect("Pi_Rtheta closed                       : false" in note, "note missing Pi guard", errors)
    expect("accepted coefficient values            : 0" in note, "note missing zero-value guard", errors)

    if errors:
        print("RTheta Pi-kernel HYM connection audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta Pi-kernel HYM connection audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
