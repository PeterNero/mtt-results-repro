"""Audit Step 28 sector-promotion reconciliation / operator-sector value cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LOCKED = PACKET_DIR / "step28_locked_stationary_sector_promotions.packet.json"
FRONTIER = PACKET_DIR / "step28_refined_operator_sector_frontier.packet.json"
CONTRACT = PACKET_DIR / "step28_operator_sector_value_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step28_SectorPromotionReconciliation_or_OperatorSectorValueCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP28_SECTORPROMOTION_RECONCILIATION_BUILT_STATIONARY_PROMOTION_LOCKED_OPERATORSECTOR_VALUES_OPEN"
NEXT = "MTT_Selected_Step29_OperatorSectorRhoEDEValues_or_InternalRThetaRows_v1"
SECTORS = {"Q", "u", "d", "L", "e", "N", "H"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    locked = load(LOCKED)
    frontier = load(FRONTIER)
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    step17 = locked["from_step17"]
    require(step17["selected_projector_promotion_Ps_Ks_closed"] is True, "Step17 Ps/Ks not imported")
    require(step17["selected_stationary_rho_s_matrix_values_closed"] is True, "Step17 rho_s not imported")
    require(step17["selected_projective_rhoE_source_level_closed"] is True, "Step17 rhoE source not imported")
    require(step17["operator_level_projective_rhoE_from_selected_connection_closed"] is False, "operator rhoE overclosed")
    require(step17["selected_DE_Riesz_Green_dotD_values_closed"] is False, "operator values overclosed")

    projector = locked["projector_packet"]
    require(projector["finite_projector_source_promotion_proved"] is True, "projector theorem missing")
    require(projector["selected_projector_source_verified"] is True, "projector source not verified")
    require(projector["transported_packet_promoted"] is True, "transport not promoted")
    require(projector["validator_ready_stationary_rho_s"] is True, "stationary rho_s not ready")
    require(projector["selected_dotD_source_verified"] is False, "stationary packet should not overclaim dotD")
    require(projector["alpha1_driver_verified"] is False, "stationary packet should not overclaim alpha1")
    require(set(projector["sector_summary"]) == SECTORS, "sector set mismatch")
    for sector, slot in projector["sector_summary"].items():
        expected_rank = 1 if sector == "H" else 3
        require(slot["rank"] == expected_rank, f"rank mismatch: {sector}")
        require(slot["source_verified_by_transport_conjugation"] is True, f"source not verified: {sector}")
        require(slot["stationary_rho_s_promoted"] is True, f"rho_s not promoted: {sector}")

    step18 = locked["from_step18"]
    for key in [
        "alpha1_dotD_driver_imported",
        "honest_dotD_replay_imported",
        "matter_slot_orientation_imported",
        "operator_blocks_imported",
        "overlap_normalization_imported",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
    ]:
        require(step18[key] is True, f"Step18 import missing: {key}")
    require(locked["anti_reopen_rule"]["these_must_not_be_relisted_as_open_sector_promotion_items"] is True, "anti-reopen rule missing")

    require(frontier["step27_wording_reconciled"] is True, "Step27 wording not reconciled")
    for key in [
        "diagonal_End0_HYM_subpayload_closed",
        "protected_T3_Riesz_Green_closed",
        "T1_T2_covariant_Green_closed",
        "row_model_offdiagonal_control_closed",
        "functional_PhiFin_trace_closed",
        "static_U10_Ubar5_1M_source_closed",
    ]:
        require(frontier["closed_from_step27"][key] is True, f"closed support missing: {key}")
    retired = frontier["retired_from_step27_open_list"]
    for key in [
        "selected_End0_to_sector_routing_values",
        "selected_Ps_Ks_projector_promotion_values",
        "selected_stationary_rho_s_matrix_values",
        "source_level_projective_rhoE",
    ]:
        require(key in retired, f"retired item missing: {key}")
    for key in [
        "operator_level_projective_rhoE_from_selected_connection",
        "selected_rhoE_transition_payload_in_fullS2_operator_tier",
        "selected_sector_basis_D_E_matrices",
        "selected_sector_basis_Riesz_projectors",
        "selected_sector_basis_Green_operators",
        "selected_sector_basis_dotD_matrices",
        "internal_Rtheta_scalar_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(frontier["still_open_after_reconciliation"][key] is True, f"open item missing: {key}")
    require(frontier["scalar_row_state"]["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")

    require(contract["next_required_artifact"] == NEXT, "contract next mismatch")
    require(contract["closure_claimed"] is False, "contract overclaimed")
    require(set(contract["acceptance_tests"]["all_sector_slots_present"]) == SECTORS, "contract sector set mismatch")
    require(contract["acceptance_tests"]["selected_source_flags_derived_by_theorem_not_flipped"] is True, "source flag guard missing")
    require(contract["acceptance_tests"]["observed_masses_mixings_cp_not_inputs"] is True, "observed-data guard missing")
    for forbidden in [
        "stationary transported P_s/K_s projector promotion",
        "stationary rho_s matrix values",
        "source-level projective S3 gerbe rho_E",
        "functional U10/Ubar5/1M matter-slot orientation",
        "diagonal End0 D_E and Green subpayload",
    ]:
        require(forbidden in contract["must_not_reopen"], f"anti-reopen missing: {forbidden}")

    decision = data["closure_decision"]
    for key in [
        "step27_sector_promotion_frontier_refined",
        "selected_stationary_End0_to_sector_routing_values_closed",
        "selected_projector_promotion_Ps_Ks_closed",
        "selected_stationary_rho_s_matrix_values_closed",
        "selected_projective_rhoE_source_level_closed",
        "functional_matter_slot_blocks_and_overlap_normalization_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "operator_level_projective_rhoE_from_selected_connection_closed",
        "selected_rhoE_transition_payload_fullS2_operator_tier_closed",
        "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed",
        "dynamic_PhiFin_C1_payload_closed",
        "fullS2_operator_payload_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["operator_sector_values_closed"] is False, "certificate overclosed operator values")

    for phrase in [
        "stationary transported P_s/K_s projectors              closed by Step17",
        "operator-level projective rho_E transition             open",
        "sector-basis D_E/Riesz/Green/dotD matrices             open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
