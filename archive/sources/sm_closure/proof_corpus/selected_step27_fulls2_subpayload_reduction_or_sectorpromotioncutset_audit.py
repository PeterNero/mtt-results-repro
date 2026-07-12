"""Audit Step 27 full-S2 subpayload reduction / sector-promotion cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUBPAYLOAD = PACKET_DIR / "step27_closed_hym_subpayload.packet.json"
PROMOTION_GAP = PACKET_DIR / "step27_sector_promotion_gap.packet.json"
NEXT_CUTSET = PACKET_DIR / "step27_next_sector_promotion_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step27_FullS2SubpayloadReduction_or_SectorPromotionCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP27_FULLS2_SUBPAYLOAD_REDUCTION_OR_SECTORPROMOTIONCUTSET_BUILT_DIAGONAL_GREEN_SUBPAYLOAD_CLOSED_SECTOR_PROMOTION_OPEN"
NEXT = "MTT_Selected_End0SectorTransfer_ProjectorPromotion_or_RhoEDEOperatorValues_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    subpayload = load(SUBPAYLOAD)
    gap = load(PROMOTION_GAP)
    cutset = load(NEXT_CUTSET)
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

    closed = subpayload["closed_subpayloads"]
    for key in [
        "full_expS_diagonal_replay",
        "rank2_metric_connection_payload",
        "End0_D_E_connection_matrices",
        "protected_T3_Riesz_Green",
        "T1_T2_covariant_Green",
        "row_model_offdiagonal_Ext_control",
        "diagonal_End0_D_E_formula",
        "protected_T3_zero_mode_Riesz_projector",
    ]:
        require(closed[key] is True, f"subpayload not closed: {key}")
    require(subpayload["numerical_support"]["green_residual_l2"] < 1e-12, "green residual too large")
    require(subpayload["closure_claimed"] is True, "subpayload should close")

    require(gap["rank2_End0_payload_closed"] is True, "rank2 End0 not closed")
    require(gap["selected_diagonal_HYM_first_solve_closed"] is True, "diagonal HYM solve not closed")
    not_promoted = gap["not_promoted"]
    for key in [
        "rank2_to_sector_transfer_closed",
        "physical_dotD_alpha1_closed_in_fullS2_gate",
        "selected_End0_to_sector_routing_values_extracted",
        "finite_projector_values_promoted_to_selected",
        "rhoE_DE_fullS2_execution_closed",
        "selected_HYM_sector_payload_closed",
    ]:
        require(not_promoted[key] is False, f"promotion gap overclosed: {key}")
    require(gap["post_step26_reconciliation"]["PhiFin_trace_closed_elsewhere"] is True, "PhiFin trace not imported")
    require(gap["post_step26_reconciliation"]["static_matter_slot_source_closed_elsewhere"] is True, "static matter not imported")
    require(gap["post_step26_reconciliation"]["still_not_fullS2_operator_payload"] is True, "fullS2 overclosed")
    exec_state = gap["higher_response_execution_state"]
    require(exec_state["execution_attempted"] is True, "execution not attempted")
    require(exec_state["execution_allowed_now"] is False, "execution overallowed")
    require(exec_state["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(exec_state["selected_HYM_operator_payload_ready"] is False, "HYM ready overclaimed")
    require(exec_state["selected_rhoE_DE_operator_payload_ready"] is False, "rhoE/DE ready overclaimed")
    require(exec_state["selected_End0_sector_functor_ready"] is False, "sector functor ready overclaimed")
    require(gap["closure_claimed"] is False, "gap overclaimed")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    for key in [
        "diagonal_End0_D_E_connection_matrices",
        "protected_T3_Riesz_Green",
        "T1_T2_covariant_Green",
        "row_model_offdiagonal_Ext_control",
        "PhiFin_functional_trace",
        "static_matter_slot_source_tier",
    ]:
        require(cutset["closed_do_not_reopen"][key] is True, f"cutset close missing: {key}")
    for item in [
        "selected End0-to-sector routing values",
        "selected P_s/K_s projector promotion values in the full-S2 operator tier",
        "selected rho_E transition payload",
        "selected D_E/Riesz/Green/dotD operator matrices in sector basis",
    ]:
        require(item in cutset["must_emit_next"], f"next item missing: {item}")
    for key in [
        "selected_fullS2_rhoE_D_E_operator_payload",
        "selected_HYM_sector_payload",
        "rank2_to_sector_transfer",
        "sector_projector_promotion_values",
        "selected_rhoE_transition_payload",
        "internal_Rtheta_scalar_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(cutset["still_open"][key] is True, f"open flag missing: {key}")

    decision = data["closure_decision"]
    for key in [
        "diagonal_End0_HYM_subpayload_closed",
        "protected_T3_Riesz_Green_closed",
        "T1_T2_covariant_Green_closed",
        "row_model_offdiagonal_control_closed",
    ]:
        require(decision[key] is True, f"candidate close missing: {key}")
    for key in [
        "selected_End0_to_sector_routing_values_closed",
        "sector_projector_promotion_values_closed",
        "selected_rhoE_transition_payload_closed",
        "selected_D_E_Riesz_Green_dotD_sector_matrices_closed",
        "fullS2_operator_payload_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["fullS2_operator_payload_closed"] is False, "certificate overclosed fullS2")

    for phrase in [
        "diagonal End0 D_E connection matrices                      closed",
        "selected End0-to-sector routing values                     open",
        "sector-basis D_E/Riesz/Green/dotD matrices                 open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
