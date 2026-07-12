"""Audit Step 40 dotD transport/alpha1 import and primitive-C1 frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT = PACKET_DIR / "step40_dotd_transport_alpha1_import.packet.json"
FRONTIER = PACKET_DIR / "step40_primitive_c1_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step40_dotDTransportAlpha1Import_or_PrimitiveC1Frontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP40_DOTD_TRANSPORT_ALPHA1_IMPORTED_PRIMITIVE_C1_FRONTIER_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_FullSectorC1ValueEmission_v1"


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

    require(import_packet["status"] == "DOTD_ALPHA1_TRANSPORT_REPLAY_IMPORTED", "import status mismatch")
    for key, value in import_packet["proof_checks"].items():
        require(value is True, f"proof check failed: {key}")
    formula = import_packet["transport_formula"]
    require(formula["U"] == "exp(-u ad(T3))", "transport operator mismatch")
    require("du/dalpha" in formula["dU_dalpha"], "dU/dalpha formula missing")
    alpha = import_packet["alpha1_driver_import"]
    require(alpha["alpha1_driver_verified"] is True, "alpha1 driver not imported")
    require(alpha["selected_dotD_source_verified"] is True, "selected dotD source not imported")
    require(alpha["honest_dotD_alpha1_replay"] is True, "honest dotD replay not imported")
    require(alpha["tangent_residual_l2"] == 0.0, "alpha1 tangent residual not zero")

    closure = import_packet["closure_result"]
    for key in [
        "selected_dotD_transport_derivative_formula_closed",
        "selected_alpha1_driver_normalization_closed",
        "same_branch_dotD_alpha1_values_closed",
        "honest_dotD_alpha1_replay_closed",
    ]:
        require(closure[key] is True, f"dotD close missing: {key}")
    for key in [
        "primitive_C1_contractions_from_operator_values_closed",
        "full_sector_C1_value_emission_closed",
        "internal_R_theta_scalar_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"import overclosed: {key}")
    require("does not emit primitive" in import_packet["guardrail"], "guardrail missing")

    closed = frontier["closed_now"]
    for key in [
        "selected_S3_qutrit_rhoE",
        "diagonal_End0_covariant_D_E",
        "stationary_transport_Riesz_Green",
        "selected_dotD_alpha1_transport_subgate",
        "alpha1_driver_normalization",
    ]:
        require(closed[key] is True, f"frontier close missing: {key}")
    missing = frontier["still_missing_for_true_value_closure"]
    for key in [
        "rank2_to_rank3_sector_transfer_values",
        "offdiagonal_End0_control",
        "coherent_spectral_zero_mode_projectors",
        "primitive_C1_contractions",
        "selected_A_selected",
        "selected_b_selected",
        "internal_R_theta_scalar_rows",
        "Yukawa_CKM_PMNS_masses",
    ]:
        require(missing[key] is True, f"frontier missing key absent: {key}")
    require(frontier["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(frontier["next_required_payload"]["target"] == NEXT, "frontier next mismatch")

    decision = data["closure_decision"]
    for key in [
        "selected_diagonal_End0_covariant_D_E_closed",
        "selected_stationary_projector_Riesz_Green_transport_closed",
        "selected_dotD_transport_derivative_formula_closed",
        "selected_alpha1_driver_normalization_closed",
        "same_branch_dotD_alpha1_values_closed",
        "honest_dotD_alpha1_replay_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "primitive_C1_contractions_from_operator_values_closed",
        "selected_A_selected_closed",
        "selected_b_selected_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["same_branch_dotD_alpha1_values_closed"] is True, "cert dotD missing")
    require(cert["primitive_C1_contractions_from_operator_values_closed"] is False, "cert primitive C1 overclosed")

    for packet in [import_packet, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    for phrase in [
        "retires `dotD_alpha1` as an active blocker",
        "Still open",
        "primitive C1 contractions",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
