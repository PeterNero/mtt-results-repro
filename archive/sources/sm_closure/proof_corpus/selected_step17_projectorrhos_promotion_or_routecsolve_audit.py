"""Audit Step 17 projector/rho_s promotion and Route-C solve frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step17_projectorrhos_promotion_or_routecsolve"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROJECTOR_PACKET = PACKET_DIR / "step17_selected_projector_rhos_promotion.packet.json"
SOURCE_PACKET = PACKET_DIR / "step17_projective_rhoe_source_boundary.packet.json"
SOLVE_FRONTIER = PACKET_DIR / "step17_routec_strominger_solve_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step17_to_step18_routec_solve_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step17_ProjectorRhoS_Promotion_or_RouteCSolve_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP17_PROJECTORRHOS_PROMOTION_CLOSED_ROUTEC_STROMINGER_SOLVE_FRONTIER"
NEXT = "MTT_Selected_Step18_RouteCStromingerGalerkinSolve_or_InternalRThetaRows_v1"
SECTORS = {"Q", "u", "d", "L", "e", "N", "H"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    projector = load(PROJECTOR_PACKET)
    source = load(SOURCE_PACKET)
    frontier = load(SOLVE_FRONTIER)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(projector["finite_projector_source_promotion_proved"] is True, "projector theorem not proved")
    require(projector["selected_projector_source_verified"] is True, "selected projector source not verified")
    require(projector["transported_packet_promoted"] is True, "transported packet not promoted")
    require(projector["validator_ready_stationary_rho_s"] is True, "stationary rho_s not ready")
    require(projector["selected_dotD_source_verified"] is False, "dotD overclosed")
    require(projector["alpha1_driver_verified"] is False, "alpha1 overclosed")
    require(set(projector["sector_summary"]) == SECTORS, "sector set mismatch")
    for sector, slot in projector["sector_summary"].items():
        expected_rank = 1 if sector == "H" else 3
        require(slot["rank"] == expected_rank, f"rank mismatch: {sector}")
        require(slot["projector_idempotent"] is True, f"projector not idempotent: {sector}")
        require(slot["projector_self_adjoint"] is True, f"projector not self-adjoint: {sector}")
        require(slot["green_operator_valid"] is True, f"Green invalid: {sector}")
        require(slot["riesz_projector_valid"] is True, f"Riesz invalid: {sector}")
        require(slot["source_verified_by_transport_conjugation"] is True, f"source not verified: {sector}")
        require(slot["stationary_rho_s_promoted"] is True, f"rho_s not promoted: {sector}")
    require(projector["closed_for_step17"]["selected_projector_promotion_Ps_Ks"] is True, "Ps/Ks not closed")
    require(projector["closed_for_step17"]["selected_stationary_rho_s_matrix_values"] is True, "rho_s values not closed")
    require(projector["not_closed_by_stationary_packet"]["operator_level_rhoE_DE_Riesz_Green_dotD_C1"] is True, "operator boundary missing")

    require(source["ordinary_rhoE_route_retired"] is True, "ordinary rhoE not retired")
    require(source["projective_twisted_rhoE_candidate_locked"] is True, "projective candidate not locked")
    require(source["source_level_projective_gerbe_rhoE_promoted"] is True, "source-level rhoE not promoted")
    require(source["operator_level_projective_rhoE_promoted"] is False, "operator rhoE overclosed")
    require(source["closed_for_step17"]["selected_S3_projective_gerbe_source"] is True, "S3 gerbe source not closed")
    for key in [
        "selected_D_E_dotD_Riesz_Green",
        "selected_visible_Chern_Weil_operator_source",
        "coherent_spectral_zero_mode_projectors",
        "primitive_C1_contractions",
    ]:
        require(source["not_closed_by_source_level_promotion"][key] is True, f"source boundary missing: {key}")

    require(frontier["sector_functor"]["End0_tensor_product_carrier_constructed"] is True, "End0 carrier not constructed")
    require(frontier["sector_functor"]["commutator_and_projector_checks_pass"] is True, "sector checks fail")
    require(frontier["adjoint_triplet_theorem_proved"] is True, "adjoint theorem not proved")
    require(frontier["conditional_Gram_theorem_proved"] is True, "Gram theorem not proved")
    require(frontier["canonical_rho_candidate_constructed"] is True, "canonical rho not constructed")
    require(frontier["zero_mode_bridge_theorem_proved"] is True, "zero-mode bridge not proved")
    require(frontier["spectral_reduction_target"] == "SelectedRouteCStromingerGalerkinResidualSolve", "wrong solve target")
    require(frontier["old_fulls2_gate"]["higher_response_full_S2_value_execution_closed"] is False, "old fullS2 overclosed")
    require(frontier["old_fulls2_gate"]["hym_rhoE_DE_fullS2_execution_closed"] is False, "old HYM overclosed")
    require(frontier["frontier_after_step17"]["selected_projector_promotion_Ps_Ks"] is False, "Ps/Ks still marked open")
    require(frontier["frontier_after_step17"]["selected_stationary_rho_s_matrix_values"] is False, "rho_s still marked open")
    require(frontier["frontier_after_step17"]["selected_projective_rhoE_source_level"] is False, "source-level rhoE still marked open")
    require(frontier["frontier_after_step17"]["selected_RouteC_Strominger_Galerkin_residual_solve"] is True, "Route-C solve not open")
    require(frontier["frontier_after_step17"]["internal_Rtheta_scalar_rows"] is True, "internal scalar rows not open")

    decision = data["closure_decision"]
    require(decision["step17_projector_rhos_promotion_closed"] is True, "Step 17 not closed")
    require(decision["selected_projector_promotion_Ps_Ks_closed"] is True, "Ps/Ks not closed in decision")
    require(decision["selected_stationary_rho_s_matrix_values_closed"] is True, "rho_s not closed in decision")
    require(decision["selected_projective_rhoE_source_level_closed"] is True, "rhoE source not closed in decision")
    require(decision["selected_RouteC_Strominger_Galerkin_residual_solve_closed"] is False, "Route-C overclosed")
    require(decision["selected_DE_Riesz_Green_dotD_values_closed"] is False, "DE/dotD overclosed")
    require(decision["internal_scalar_row_execution_closed"] is False, "internal scalar overclosed")
    require(decision["accepted_internal_scalar_row_count"] == 0, "internal scalar rows over-emitted")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(next_workorder["next_step"] == 18, "next step mismatch")
    require(next_workorder["must_not_reopen"]["stationary_transported_projector_Ps_Ks"] is True, "Ps/Ks anti-reopen missing")
    require(next_workorder["must_not_reopen"]["source_level_projective_S3_gerbe_rhoE"] is True, "rhoE anti-reopen missing")
    require(next_workorder["success_criterion"]["observed_values_not_used_as_selectors"] is True, "selector guard missing")

    for phrase in [
        "selected transported stationary projectors P_s/K_s     closed",
        "source-level projective S3 gerbe rho_E                 closed",
        "honest selected Route-C/Strominger Galerkin residual solve",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
