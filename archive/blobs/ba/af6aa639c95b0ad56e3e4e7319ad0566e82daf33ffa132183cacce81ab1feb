"""Audit Step 37 finite-trace D_E/gap import and full-operator frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_IMPORT = PACKET_DIR / "step37_finite_trace_degap_import.packet.json"
FRONTIER = PACKET_DIR / "step37_full_operator_value_frontier.packet.json"
CONTRACT = PACKET_DIR / "step37_next_operator_value_construction_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step37_FiniteTraceDEGapImport_or_FullOperatorValueFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP37_FINITE_TRACE_DEGAP_IMPORTED_FULL_OPERATOR_VALUES_OPEN"
NEXT = "MTT_Selected_FullOperatorValuePacket_ProjectiveRhoE_DE_RieszGreen_DotD_ZeroModes_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    trace_import = load(TRACE_IMPORT)
    frontier = load(FRONTIER)
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(trace_import["status"] == "FINITE_TRACE_DE_GAP_LAYER_IMPORTED_FROM_SELECTED_TRACE_PAYLOAD", "trace import status mismatch")
    require(trace_import["selected_branch"] == {"q": 79, "orientation": "F", "torsion_label_m": 1}, "selected branch mismatch")
    require(trace_import["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis mismatch")
    require(trace_import["basis_dimension"] == 27, "basis dimension mismatch")
    require(trace_import["selected_trace_equality"]["proved"] is True, "trace equality not proved")
    require(trace_import["selected_gap_lower_bound"] > 0, "selected gap must be positive")
    require(trace_import["selected_green_norm_bound"] > 0, "Green norm bound must be positive")
    for key, value in trace_import["proof_checks"].items():
        require(value is True, f"trace import proof check failed: {key}")

    closure = trace_import["closure_result"]
    require(closure["finite_trace_DE_gap_layer_closed"] is True, "finite trace layer not closed")
    require(closure["transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed"] is True, "transition trace slot not closed")
    for key in [
        "operator_level_projective_rhoE_transition_matrices_closed",
        "selected_fullS2_DE_Riesz_Green_dotD_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "selected_visible_operator_source_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"trace import overclosed: {key}")
    require("not a full operator-value emission" in trace_import["scope_guard"], "scope guard missing")

    support = frontier["closed_support_now_available"]
    for key in [
        "selected_S3_flat_Deligne_class",
        "selected_S3_pullback_restriction_table",
        "smooth_Freed_Witten_cancellation",
        "block_family_Higgs_projector_retention",
        "visible_Green_Schwarz_curvature_support",
        "finite_trace_DE_gap_layer",
    ]:
        require(support[key] is True, f"closed support missing: {key}")

    missing = frontier["still_missing_as_values"]
    for key in [
        "projective_rho_E_transition_matrices",
        "selected_covariant_D_E_matrices_on_projective_BN_lift",
        "source_verified_Riesz_projectors",
        "source_verified_reduced_Green_operators",
        "same_branch_dotD_alpha1_matrices",
        "coherent_spectral_zero_mode_projectors",
        "primitive_C1_overlap_contractions_from_these_values",
        "internal_R_theta_scalar_rows",
    ]:
        require(missing[key] is True, f"frontier missing value flag absent: {key}")
    require(frontier["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require("finite D_E/gap trace payload missing" in frontier["demoted_stale_blocker_phrases"], "stale blocker not demoted")
    require("full same-source operator-value packet missing" in frontier["remaining_live_blocker_phrase"], "live blocker wrong")

    require(contract["target"] == NEXT, "contract target mismatch")
    for expected in [
        "non-identity projective rho_E transition matrices on the selected projective B_N basis",
        "covariant D_E matrices sector by sector in the same basis",
        "Riesz projectors defined by the selected spectral contour with an explicit positive complement gap",
        "dotD_alpha1 matrices obtained as the same-branch derivative of the emitted D_E package",
        "primitive C1 contractions computed from the emitted zero modes, Green response, and dotD payload",
    ]:
        require(expected in contract["must_emit_same_source_payload"], f"contract payload missing: {expected}")
    for key in [
        "same_source",
        "non_identity",
        "projective_cocycle",
        "operator_equations",
        "gap",
        "no_proxy_fit",
    ]:
        require(key in contract["acceptance_tests"], f"acceptance test missing: {key}")
    for key, value in contract["minimum_closure_keys_for_next_candidate"].items():
        require(value is True, f"next closure key should be true target: {key}")

    decision = data["closure_decision"]
    for key in [
        "selected_s3_class_restriction_layer_closed",
        "finite_trace_DE_gap_layer_closed",
        "transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed",
        "selected_trace_equality_closed",
        "positive_gap_Riesz_Green_lock_imported",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "operator_level_projective_rhoE_transition_matrices_closed",
        "selected_covariant_D_E_matrices_closed",
        "selected_Riesz_Green_values_closed",
        "same_branch_dotD_alpha1_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "primitive_C1_contractions_from_operator_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "internal scalar row count overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["finite_trace_DE_gap_layer_closed"] is True, "certificate finite trace close missing")
    require(cert["full_operator_value_packet_closed"] is False, "certificate full packet overclosed")
    require(cert["accepted_internal_scalar_row_count"] == 0, "certificate scalar rows overaccepted")

    for packet in [trace_import, frontier, contract, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    for phrase in [
        "Step37 imports",
        "finite trace `D_E`/gap/Riesz/Green layer",
        "It does not close",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
