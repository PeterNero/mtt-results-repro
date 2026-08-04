"""Audit Step 39 diagonal End0 covariant D_E import and full-sector frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT = PACKET_DIR / "step39_diagonal_end0_covariant_de_import.packet.json"
FRONTIER = PACKET_DIR / "step39_full_sector_operator_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step39_DiagonalEnd0CovariantDEImport_or_FullSectorFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP39_DIAGONAL_END0_COVARIANT_DE_IMPORTED_FULL_SECTOR_VALUES_OPEN"
NEXT = "MTT_Selected_FullSectorDE_DotD_ZeroModeC1_From_DiagonalEnd0Transport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    import_packet = load(IMPORT)
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

    require(import_packet["status"] == "DIAGONAL_END0_COVARIANT_DE_AND_STATIONARY_TRANSPORT_IMPORTED", "import status mismatch")
    for key, value in import_packet["proof_checks"].items():
        require(value is True, f"proof check failed: {key}")

    op = import_packet["selected_diagonal_end0_operator"]
    require(op["basis"] == ["T1", "T2", "T3"], "End0 basis mismatch")
    require(op["rank"] == 3, "End0 rank mismatch")
    require(op["D_E_formula"] == "D_E = d + du ad(T3)", "D_E formula mismatch")
    require(op["ad_T3_matrix"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]], "adT3 mismatch")
    require(sorted(op["active_directions"]) == ["x1", "x2", "y1", "y2"], "active direction mismatch")

    stationary = import_packet["stationary_transport_payload"]
    require(stationary["gauge_transport_trace_closed"] is True, "transport trace not closed")
    require(stationary["selected_functional_zero_mode_bases"] is True, "zero-mode bases not imported")
    require(stationary["selected_projector_source_verified"] is True, "projector source not verified")
    require(stationary["selected_riesz_green_source_verified"] is True, "Riesz/Green source not verified")
    require("not closed" in stationary["dotD_excluded_reason"], "dotD guard missing")

    result = import_packet["closure_result"]
    require(result["selected_diagonal_End0_covariant_D_E_closed"] is True, "diagonal End0 D_E not closed")
    require(result["selected_stationary_projector_Riesz_Green_transport_closed"] is True, "stationary transport not closed")
    for key in [
        "selected_full_sector_covariant_D_E_matrices_closed",
        "rank2_to_rank3_sector_transfer_values_closed",
        "offdiagonal_End0_control_closed",
        "same_branch_dotD_alpha1_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "primitive_C1_contractions_from_operator_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(result[key] is False, f"import overclosed: {key}")

    closed = frontier["closed_now"]
    for key in [
        "selected_S3_class_and_qutrit_rhoE",
        "finite_trace_DE_gap_Riesz_Green_layer",
        "operator_level_projective_rhoE_transition_matrices",
        "diagonal_End0_covariant_D_E_lane",
        "stationary_projector_Riesz_Green_transport_lane",
    ]:
        require(closed[key] is True, f"frontier closed key missing: {key}")
    missing = frontier["still_missing_for_full_sector_values"]
    for key in [
        "rank2_to_rank3_sector_transfer_values",
        "offdiagonal_End0_vanish_or_control_bound",
        "selected_finite_derivative_basis_for_validator",
        "full_sector_covariant_D_E_matrices_Q_u_d_L_e_N_H",
        "same_branch_dotD_alpha1_with_transport_derivative",
        "coherent_spectral_zero_mode_projectors",
        "primitive_C1_overlap_contractions",
        "internal_R_theta_scalar_rows",
    ]:
        require(missing[key] is True, f"frontier missing key absent: {key}")
    require(frontier["next_required_payload"]["target"] == NEXT, "frontier next target mismatch")
    require(frontier["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")

    decision = data["closure_decision"]
    for key in [
        "selected_s3_class_restriction_layer_closed",
        "finite_trace_DE_gap_layer_closed",
        "operator_level_projective_rhoE_transition_matrices_closed",
        "selected_diagonal_End0_covariant_D_E_closed",
        "selected_stationary_projector_Riesz_Green_transport_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "selected_full_sector_covariant_D_E_matrices_closed",
        "rank2_to_rank3_sector_transfer_values_closed",
        "offdiagonal_End0_control_closed",
        "same_branch_dotD_alpha1_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "primitive_C1_contractions_from_operator_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["selected_diagonal_End0_covariant_D_E_closed"] is True, "cert diagonal D_E missing")
    require(cert["selected_full_sector_covariant_D_E_matrices_closed"] is False, "cert full sector overclosed")

    for packet in [import_packet, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    for phrase in [
        "selected diagonal End0 covariant `D_E`",
        "stationary gauge-transport/Riesz-Green replay",
        "Still open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
