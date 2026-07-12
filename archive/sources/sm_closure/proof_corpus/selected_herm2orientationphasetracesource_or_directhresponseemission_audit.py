"""Audit Herm(2) orientation/phase/trace source or direct H-response emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_herm2orientationphasetracesource_or_directhresponseemission"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Herm2OrientationPhaseTraceSource_or_DirectHResponseEmission_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

BRIDGE_RECHECK = BASE / "projection_bridge_vs_direct_hresponse_recheck.packet.json"
PHASE_TRACE = BASE / "orientation_phase_trace_source_inventory.packet.json"
DIRECT_RUN = BASE / "direct_hresponse_emission_after_bridge_completion.packet.json"
CUTSET = BASE / "next_cutset_after_orientation_phase_trace_source.packet.json"

STATUS = (
    "MTT_SELECTED_HERM2ORIENTATIONPHASETRACESOURCE_OR_DIRECTHRESPONSEEMISSION_"
    "PROJECTION_BRIDGE_RETIRED_DIRECT_ROWS_OPEN"
)
NEXT = "MTT_Selected_NonDiagonalHuvHessianSource_or_DirectHerm2Rows_v1"
S_BETA = 0.004701083905943647


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    bridge = load(BRIDGE_RECHECK)
    phase = load(PHASE_TRACE)
    direct = load(DIRECT_RUN)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["minimal_parameter_tier_claimed"] is True, "minimal tier")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "projection_bridge_retired_as_sbeta_blocker",
        "projection_bridge_is_not_direct_Herm2_value_source",
        "orientation_phase_trace_inventory_executed",
        "direct_H_response_emission_rechecked",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "strict_radial_scale_source_emitted",
        "selected_Delta_sign_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "same_source_certificates_emitted",
        "selected_non_diagonal_Huv_Hessian_source_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_H_response_source_row_count"] == 0, "H rows")
    require(decision["accepted_R_H_RG_source_count"] == 0, "RHRG")

    nums = candidate["key_numbers"]
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-15, "s_beta")
    require(nums["accepted_H_response_source_row_count"] == 0, "num H rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "num RHRG")
    require(nums["required_H_response_row_count"] == 7, "required rows")
    require(nums["emitted_H_response_row_count"] == 0, "emitted rows")
    require(nums["accepted_selected_K_source_row_count"] == 9, "K rows")
    require(nums["selected_K_threshold_row_count_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "projection_bridge_retired_as_sbeta_blocker",
        "projection_bridge_is_not_direct_Herm2_value_source",
        "orientation_phase_trace_inventory_executed",
        "direct_H_response_emission_rechecked",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "selected_non_diagonal_Huv_Hessian_source_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "direct_Herm2_rows_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_H_response_source_row_count"] == 0, "cert H rows")
    require(cert["accepted_R_H_RG_source_count"] == 0, "cert RHRG")

    require(bridge["status"] == "C1_C6_PROJECTION_BRIDGE_CLOSED_FOR_SBETA_DIRECT_HRESPONSE_OPEN", "bridge status")
    for key in [
        "C1_branch_and_ordered_channel_labels",
        "C2_typed_E_H_UV_section_basis",
        "C3_selected_HYM_metric_connection",
        "C4_quadrature_trace_normalization",
        "C5a_trace_grid_identity",
        "C5b_projection_measure_equality",
        "C6_no_extra_boundary_source",
    ]:
        require(bridge["bridge_status"][key] is True, f"bridge status {key}")
    require(bridge["projection_result"]["selected_s_beta_value_found"] is True, "s_beta found")
    require(abs(bridge["projection_result"]["selected_s_beta_value"] - S_BETA) < 1e-15, "bridge s")
    require(bridge["projection_result"]["selected_finite_reduction_policy_emitted"] is True, "finite policy")
    for key in [
        "selected_F_H_second_variation_emitted",
        "selected_dynamic_strain_kernel_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
    ]:
        require(bridge["direct_value_result"][key] is False, f"bridge direct {key}")
    require(bridge["decision"]["projection_bridge_retired_as_sbeta_blocker"] is True, "retired")
    require(bridge["decision"]["projection_bridge_is_not_direct_Herm2_value_source"] is True, "not direct")
    require(bridge["decision"]["direct_Herm2_rows_emitted"] is False, "direct rows")
    require(bridge["decision"]["accepted_H_response_source_row_count"] == 0, "bridge H rows")
    require_no_selector(bridge, "bridge")

    require(phase["status"] == "ORIENTATION_PHASE_TRACE_SOURCE_INVENTORY_EXECUTED_ZERO_EMISSIONS", "phase status")
    fields = phase["source_fields"]
    require(fields["r_H"]["status"] == "strict_open_controlled_calibration_available", "r_H")
    require(fields["sigma_D"]["status"] == "open", "sigma")
    require(fields["phi_Omega"]["status"] == "open", "phi")
    require(fields["m0"]["status"] == "open_for_full_H_response_rows", "m0")
    require(fields["m0"]["tracefree_block_status"] == "retired", "m0 tracefree")
    require(fields["certificates"]["status"] == "open", "certs open")
    support = phase["support_not_enough"]
    for key in [
        "Higgs_specific_operator_block_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "selected_H_response_table_emitted",
    ]:
        require(support[key] is False, f"support false {key}")
    require(phase["decision"]["orientation_phase_trace_inventory_executed"] is True, "inventory")
    for key in [
        "strict_radial_scale_source_emitted",
        "selected_Delta_sign_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "same_source_certificates_emitted",
    ]:
        require(phase["decision"][key] is False, f"phase false {key}")
    require_no_selector(phase, "phase")

    require(direct["status"] == "DIRECT_HRESPONSE_EMISSION_RECHECK_ZERO_ROWS", "direct status")
    required = direct["required_table"]
    for key in [
        "Huu",
        "Hud_re",
        "Hud_im",
        "Hdd",
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
    ]:
        require(key in required, f"required {key}")
    for value in required.values():
        require(value is None, "required table unexpectedly filled")
    for value in direct["values_emitted_now"].values():
        require(value is None, "value unexpectedly emitted")
    table = direct["hresponse_row_table_status"]
    require(table["required_row_count"] == 7, "table required")
    require(table["emitted_row_count"] == 0, "table emitted")
    require(table["accepted_source_row_count"] == 0, "table accepted")
    require(direct["decision"]["B_Huv_symbolic_exact_payload_emitted"] is True, "B_Huv")
    require(direct["decision"]["M_H_three_row_functional_closed"] is True, "M_H functional")
    for key in [
        "direct_Herm2_Huv_payload_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_value_emitted",
    ]:
        require(direct["decision"][key] is False, f"direct false {key}")
    require(direct["decision"]["accepted_H_response_source_row_count"] == 0, "direct H rows")
    require_no_selector(direct, "direct")

    require(cutset["status"] == "NEXT_FRONTIER_NONDIAGONAL_HUV_HESSIAN_SOURCE_OR_DIRECT_HERM2_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("C1-C6 projection bridge retired as s_beta/projection blocker" in cutset["closed_here"], "cutset closed")
    for phrase in [
        "selected non-diagonal Huv Hessian/source functional",
        "selected Delta sign",
        "selected Omega phase",
        "direct Huu,Hud,Hdd rows with certificates",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "The C1-C6 projection bridge is now retired as an `s_beta` blocker",
        f"selected `s_beta = {S_BETA}`",
        "Accepted H-response source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: C1-C6 projection bridge is retired for s_beta, but direct "
        "non-diagonal Huv/H-response rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
