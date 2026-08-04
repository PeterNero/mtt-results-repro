"""Audit Step 38 finite Heisenberg rho_E promotion and D_E frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION = PACKET_DIR / "step38_finite_heisenberg_rhoe_promotion.packet.json"
FRONTIER = PACKET_DIR / "step38_de_operator_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step38_FiniteHeisenbergRhoEPromotion_or_DEOperatorFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP38_FINITE_HEISENBERG_RHOE_PROMOTED_DE_OPERATOR_VALUES_OPEN"
NEXT = "MTT_Selected_CovariantDE_From_ProjectiveRhoE_and_SelectedConnection_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    promotion = load(PROMOTION)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(promotion["status"] == "PROJECTIVE_RHOE_TRANSITION_GAUGE_CLASS_PROMOTED", "promotion status mismatch")
    theorem = promotion["finite_selection_theorem"]
    require(theorem["name"] == "FiniteStoneVonNeumannProjectiveRhoESelection", "theorem name mismatch")
    require(theorem["proved"] is True, "finite selection theorem not proved")
    require("unique up to unitary gauge" in theorem["statement"], "gauge uniqueness missing")
    require(theorem["proof_clauses"]["irreducible_dimension"] == 3, "wrong irreducible dimension")
    require(theorem["proof_clauses"]["central_character"] != [1.0, 0.0], "central character should be nontrivial")

    for key, value in promotion["promotion_checks"].items():
        require(value is True, f"promotion check failed: {key}")

    rhoe = promotion["selected_projective_rhoE_gauge_representative"]
    gates = rhoe["numeric_gates"]
    require(rhoe["basis"] == "qutrit fiber C3 over selected F3xF3 deck shadow", "basis mismatch")
    require(rhoe["active_generators"] == ["g1", "g2"], "active generators mismatch")
    require(rhoe["kernel_generators"] == ["g3", "g4", "g5", "g6"], "kernel generators mismatch")
    require(gates["active_deck_rank_over_F3"] == 2, "deck rank mismatch")
    require(gates["uses_only_selected_active_generators_g1_g2"] is True, "active generator gate failed")
    require(gates["kernel_generators_identity"] is True, "kernel identity gate failed")
    require(gates["passes_numeric_packet_gate"] is True, "numeric rhoE gate failed")
    require(gates["unitary_residual_max"] < 1e-10, "unitary residual too large")
    require(gates["order3_residual_max"] < 1e-10, "order residual too large")
    require(gates["projective_commutator_residual"] < 1e-10, "commutator residual too large")

    result = promotion["closure_result"]
    require(result["operator_level_projective_rhoE_transition_matrices_closed"] is True, "rhoE not closed")
    require(result["nonidentity_projective_rhoE_selected_up_to_unitary_gauge"] is True, "rhoE gauge selection missing")
    require(result["identity_rhoE_smoke_retired_for_operator_frontier"] is True, "identity smoke not retired")
    for key in [
        "selected_covariant_D_E_matrices_closed",
        "selected_Riesz_Green_values_closed",
        "same_branch_dotD_alpha1_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "primitive_C1_contractions_from_operator_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(result[key] is False, f"promotion overclosed: {key}")

    closed = frontier["closed_now"]
    require(closed["selected_s3_class_restriction_layer"] is True, "S3 layer missing")
    require(closed["finite_trace_DE_gap_layer"] is True, "finite trace layer missing")
    require(closed["operator_level_projective_rhoE_transition_gauge_class"] is True, "rhoE frontier close missing")
    missing = frontier["still_missing_as_operator_values"]
    for key in [
        "selected_connection_one_form_or_Cech_Dolbeault_connection",
        "covariant_D_E_matrices_on_selected_B_N_basis",
        "Riesz_projectors_from_emitted_D_E",
        "reduced_Green_operators_from_emitted_D_E",
        "same_branch_dotD_alpha1_from_D_E_derivative",
        "coherent_zero_mode_projectors",
        "primitive_C1_contractions",
        "internal_R_theta_scalar_rows",
    ]:
        require(missing[key] is True, f"missing frontier flag absent: {key}")
    require(frontier["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(frontier["next_minimum_payload"]["target"] == NEXT, "frontier target mismatch")
    for forbidden in ["identity rho_E", "trace scalar as full transition matrix", "observed SM masses or mixings"]:
        require(forbidden in frontier["next_minimum_payload"]["must_not_use"], f"forbidden shortcut missing: {forbidden}")

    decision = data["closure_decision"]
    require(decision["selected_s3_class_restriction_layer_closed"] is True, "decision S3 close missing")
    require(decision["finite_trace_DE_gap_layer_closed"] is True, "decision finite trace close missing")
    require(decision["operator_level_projective_rhoE_transition_matrices_closed"] is True, "decision rhoE close missing")
    require(decision["nonidentity_projective_rhoE_selected_up_to_unitary_gauge"] is True, "decision gauge selection missing")
    for key in [
        "selected_covariant_D_E_matrices_closed",
        "selected_Riesz_Green_values_closed",
        "same_branch_dotD_alpha1_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "primitive_C1_contractions_from_operator_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")

    require(cert["operator_level_projective_rhoE_transition_matrices_closed"] is True, "cert rhoE close missing")
    require(cert["selected_covariant_D_E_matrices_closed"] is False, "cert D_E overclosed")
    require(cert["accepted_internal_scalar_row_count"] == 0, "cert scalar rows overaccepted")
    for packet in [promotion, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    for phrase in [
        "finite Stone-von Neumann uniqueness",
        "operator-level projective `rho_E` transition matrices",
        "Still open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
