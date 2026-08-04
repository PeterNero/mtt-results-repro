"""Audit Herm(2) polar source completion or H-response rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_herm2polarsourcecompletion_or_hresponserows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Herm2PolarSourceCompletion_or_HResponseRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

TRACEFREE = BASE / "tracefree_polar_source_completion.packet.json"
ORIENTATION = BASE / "omega_phase_orientation_recheck.packet.json"
HROWS = BASE / "conditional_hresponse_row_schema_after_polar_completion.packet.json"
CUTSET = BASE / "next_cutset_after_herm2_polar_completion.packet.json"

STATUS = (
    "MTT_SELECTED_HERM2POLARSOURCECOMPLETION_OR_HRESPONSEROWS_"
    "TRACEFREE_CONTRACT_CLOSED_PHASE_TRACE_ROWS_OPEN"
)
NEXT = "MTT_Selected_Herm2OrientationPhaseTraceSource_or_DirectHResponseEmission_v1"
S_BETA = 0.004701083905943647
SQRT_S = 0.068564450744855
SQRT_C = 0.9976466890107221


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
    tracefree = load(TRACEFREE)
    orientation = load(ORIENTATION)
    hrows = load(HROWS)
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
        "tracefree_polar_contract_closed",
        "m0_retired_for_tracefree_threshold_block",
        "orientation_packets_rechecked",
        "orientation_import_rejected_as_Higgs_phase_source",
        "conditional_H_response_row_schema_closed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "m0_retired_for_full_H_response_rows",
        "strict_radial_scale_source_emitted",
        "selected_Delta_sign_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "same_source_certificates_emitted",
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
    require(abs(nums["sqrt_s_beta"] - SQRT_S) < 1e-15, "sqrt s")
    require(abs(nums["sqrt_1_minus_s_beta"] - SQRT_C) < 1e-15, "sqrt c")
    require(nums["accepted_H_response_source_row_count"] == 0, "num H rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "num RHRG")
    require(nums["required_H_response_row_count"] == 7, "required rows")
    require(nums["emitted_H_response_row_count"] == 0, "emitted rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "tracefree_polar_contract_closed",
        "m0_retired_for_tracefree_threshold_block",
        "orientation_import_rejected_as_Higgs_phase_source",
        "conditional_H_response_row_schema_closed",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "m0_retired_for_full_H_response_rows",
        "selected_Omega_phase_emitted",
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

    require(tracefree["status"] == "TRACEFREE_POLAR_CONTRACT_CLOSED_VALUES_CONDITIONAL", "tracefree status")
    support = tracefree["closed_support"]
    require(support["Herm2_polar_reconstruction_law_closed"] is True, "polar support")
    require(support["H_specific_tracefree_normal_form_fixed"] is True, "normal form")
    require(support["Pauli_Riesz_three_row_source_functional_contract_closed"] is True, "Pauli")
    block = tracefree["tracefree_block"]
    require(block["matrix"] == "[[Delta, Omega], [conj(Omega), -Delta]]", "matrix")
    require(block["Delta"] == "sigma_D * r_H * sqrt(s_beta)", "Delta")
    require(block["Omega"] == "r_H * sqrt(1-s_beta) * exp(i phi_Omega)", "Omega")
    require(abs(block["s_beta"] - S_BETA) < 1e-15, "block s")
    require(abs(block["sqrt_s_beta"] - SQRT_S) < 1e-15, "block sqrt s")
    require(abs(block["sqrt_1_minus_s_beta"] - SQRT_C) < 1e-15, "block sqrt c")
    require("m0 is not needed to define Delta, Omega, or the trace-free threshold block" in tracefree["what_tracefree_closes"], "m0 close")
    require("full H-response rows Huu and Hdd when m0 is nonzero" in tracefree["what_tracefree_does_not_close"], "m0 open")
    require(tracefree["decision"]["tracefree_polar_contract_closed"] is True, "tracefree closed")
    require(tracefree["decision"]["m0_retired_for_tracefree_threshold_block"] is True, "m0 tf")
    require(tracefree["decision"]["m0_retired_for_full_H_response_rows"] is False, "m0 full")
    for key in ["Delta_row_emitted", "Omega_row_emitted", "direct_Herm2_rows_emitted"]:
        require(tracefree["decision"][key] is False, f"tracefree false {key}")
    require_no_selector(tracefree, "tracefree")

    require(orientation["status"] == "ORIENTATION_SUPPORT_RECHECKED_NO_HIGGS_OMEGA_PHASE_SOURCE", "orientation status")
    checked = orientation["orientation_support_checked"]
    require(checked["static_lambda_orbit_selected"] is True, "static orbit")
    require(checked["individual_lambda_value_selected"] is False, "individual lambda")
    require(checked["dynamic_first_response_layer_closed"] is True, "dynamic first")
    require(checked["selected_second_order_physical_matrices_promoted"] is False, "second order")
    legal = orientation["legal_import_decision"]
    require(legal["can_import_static_lambda_orbit_as_Higgs_Omega_phase"] is False, "static import")
    require(legal["can_import_dynamic_first_response_as_Higgs_Omega_phase"] is False, "dynamic import")
    require("same-source H_uv" in legal["reason"], "reason")
    require(orientation["decision"]["orientation_packets_rechecked"] is True, "orientation rechecked")
    require(orientation["decision"]["orientation_import_rejected_as_Higgs_phase_source"] is True, "orientation rejected")
    require(orientation["decision"]["selected_Omega_phase_emitted"] is False, "Omega phase")
    require(orientation["decision"]["selected_Delta_sign_emitted"] is False, "Delta sign")
    require_no_selector(orientation, "orientation")

    require(hrows["status"] == "HRESPONSE_ROWS_CONDITIONAL_SCHEMA_CLOSED_VALUES_OPEN", "hrows status")
    required = hrows["required_source_fields"]
    for key in ["r_H", "sigma_D", "phi_Omega", "m0", "certificates"]:
        require(key in required, f"hrow required {key}")
    rows = hrows["conditional_rows"]
    require(rows["Delta"] == "sigma_D * r_H * sqrt(s_beta)", "row Delta")
    require("cos(phi_Omega)" in rows["Hud_re"], "row Hud_re")
    require("sin(phi_Omega)" in rows["Hud_im"], "row Hud_im")
    require(rows["Huu"] == "m0 + Delta", "row Huu")
    require(rows["Hdd"] == "m0 - Delta", "row Hdd")
    current = hrows["current_row_table_status"]
    require(current["required_H_response_row_count"] == 7, "current req")
    require(current["emitted_H_response_row_count"] == 0, "current emitted")
    require(current["accepted_H_response_source_row_count"] == 0, "current accepted")
    routes = hrows["route_rechecks"]
    require(routes["full_M_source_route_instantiated_but_values_open"] is True, "Msource route")
    require(routes["E_H_UV_binding_trace_identity_still_open"] is True, "E_H open")
    require(routes["direct_Herm2_Huv_payload_emitted"] is False, "direct payload")
    require(routes["value_source_contract_closed"] is True, "contract")
    require(hrows["decision"]["conditional_H_response_row_schema_closed"] is True, "schema")
    for key in [
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_value_emitted",
    ]:
        require(hrows["decision"][key] is False, f"hrows false {key}")
    require(hrows["decision"]["accepted_H_response_source_row_count"] == 0, "hrows accepted")
    require_no_selector(hrows, "hrows")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_HERM2_ORIENTATION_PHASE_TRACE_SOURCE_OR_DIRECT_HRESPONSE_EMISSION",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("trace-free Herm(2) polar completion contract" in cutset["closed_here"], "cutset closed")
    for phrase in [
        "strict selected radial scale r_H",
        "selected Delta sign sigma_D",
        "selected Omega phase phi_Omega in H_uv basis",
        "trace-center m0 source or full quotient trace-free H-response theorem",
        "direct H-response row emission",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "M_H^tf = [[Delta, Omega], [conj(Omega), -Delta]]",
        f"s_beta = {S_BETA}",
        f"sqrt(s_beta) = {SQRT_S}",
        "m0` is retired only for the trace-free threshold block",
        "Accepted H-response source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: trace-free Herm(2) polar contract and conditional H-response "
        "row schema are closed; phase/trace/source rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
