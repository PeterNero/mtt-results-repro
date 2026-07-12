"""Audit H-sector logdeterminant kernel or selected H-response spectrum packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HSectorLogDeterminantKernel_or_SelectedHResponseSpectrum_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

STATIC_LOGDET_IMPORT = BASE / "static_heat_logdet_kernel_import.packet.json"
HRESPONSE_SPECTRUM_GATE = BASE / "selected_hresponse_spectrum_gate.packet.json"
RHRG_VALUE_ATTEMPT = BASE / "rhrg_value_execution_after_logdet_gate.packet.json"
CUTSET = BASE / "next_cutset_after_hsector_logdet_hresponse_gate.packet.json"

STATUS = (
    "MTT_SELECTED_HSECTORLOGDETERMINANTKERNEL_OR_SELECTEDHRESPONSESPECTRUM_"
    "STATIC_LOGDET_IMPORTED_DYNAMIC_HRESPONSE_OPEN"
)
NEXT = "MTT_Selected_HResponseSpectrumSourceRows_or_RHRGLogDetValueExecution_v1"
HRG = 391.39140285811936
H_LOGDET = 43.802475498298655


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
    static = load(STATIC_LOGDET_IMPORT)
    hgate = load(HRESPONSE_SPECTRUM_GATE)
    rhrg = load(RHRG_VALUE_ATTEMPT)
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
    require(decision["static_H_logdet_imported"] is True, "static import")
    for key in [
        "static_H_logdet_promoted_to_R_H_RG",
        "selected_H_response_spectrum_emitted",
        "selected_F_H_spectrum_emitted",
        "direct_Herm2_rows_emitted",
        "H_response_logdet_executable",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_R_H_RG_source_count"] == 0, "source count")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG_diagnostic_only"] - HRG) < 1e-12, "HRG")
    require(abs(nums["static_H_sector_log_pseudodeterminant"] - H_LOGDET) < 1e-12, "H logdet")
    require(nums["static_H_sector_positive_dimension"] == 26, "positive dim")
    require(nums["static_H_sector_kernel_dimension"] == 1, "kernel dim")
    require(abs(nums["static_H_logdet_over_HRG"] - H_LOGDET / HRG) < 1e-15, "ratio")
    require(nums["accepted_H_response_source_row_count"] == 0, "H response rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "RHRG rows")
    require(nums["selected_K_source_rows"] == 9, "K rows")
    require(nums["selected_K_rows_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["static_H_logdet_imported"] is True, "cert static")
    for key in [
        "static_H_logdet_promoted_to_R_H_RG",
        "selected_H_response_spectrum_emitted",
        "H_response_logdet_executable",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_R_H_RG_source_count"] == 0, "cert source count")

    require(static["status"] == "STATIC_FINITE_HEAT_LOGDET_IMPORTED_SUPPORT_ONLY", "static status")
    require(abs(static["imported_static_values"]["H_sector_log_pseudodeterminant"] - H_LOGDET) < 1e-12, "static logdet")
    require(static["scope_check"]["finite_DE_gap_heat_torsion_slot_closed"] is True, "static slot")
    require(static["scope_check"]["slot_layer_closed"] is True, "slot layer")
    require(static["scope_check"]["static_D_E_gap_layer"] is True, "static layer")
    require(static["scope_check"]["dynamic_H_response_spectrum"] is False, "dynamic overclaim")
    require(static["scope_check"]["mu_dependent_threshold_RG_kernel"] is False, "mu overclaim")
    require(static["scope_check"]["accepted_as_R_H_RG_logdet_kernel"] is False, "RHRG overclaim")
    require_no_selector(static, "static")

    require(hgate["status"] == "SELECTED_HRESPONSE_SPECTRUM_GATE_EXECUTED_VALUES_OPEN", "hgate status")
    for value in hgate["closed_domain_inputs"].values():
        require(value is True, "domain input missing")
    for value in hgate["missing_value_inputs"].values():
        require(value is True, "value input overclosed")
    require(hgate["strict_mh_current_packet_passes"] is False, "strict MH overpass")
    for key in [
        "selected_H_response_spectrum_emitted",
        "selected_F_H_spectrum_emitted",
        "direct_Herm2_rows_emitted",
        "H_response_logdet_executable",
    ]:
        require(hgate["decision"][key] is False, f"hgate false {key}")
    require(hgate["decision"]["accepted_H_response_source_row_count"] == 0, "hgate source count")
    require_no_selector(hgate, "hgate")

    require(rhrg["status"] == "RHRG_VALUE_EXECUTION_REPLAYED_STATIC_LOGDET_NOT_ACCEPTED", "rhrg status")
    require(abs(rhrg["diagnostic_only"]["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "rhrg HRG")
    require(abs(rhrg["diagnostic_only"]["static_H_logdet"] - H_LOGDET) < 1e-12, "rhrg static")
    for key in [
        "static_logdet_used_as_R_H_RG",
        "H_response_logdet_value_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "target_independent_validation_run_executed",
    ]:
        require(rhrg["execution_decision"][key] is False, f"rhrg false {key}")
    require(rhrg["execution_decision"]["accepted_R_H_RG_source_count"] == 0, "rhrg source count")
    require_no_selector(rhrg, "rhrg")

    require(
        cutset["status"] == "NEXT_FRONTIER_HRESPONSE_SPECTRUM_SOURCE_ROWS_OR_RHRG_LOGDET_VALUE_EXECUTION",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("static finite H-sector heat/logdet support imported" in cutset["closed_here"], "cutset closed")
    require("selected F_H functional or selected H_response table on B_Huv" in cutset["still_open"], "cutset open")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "H-sector log pseudodeterminant",
        "It is not promoted to",
        "H-response logdet executable: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: static H-sector heat logdet imported as support; selected H-response spectrum "
        "and R_H^RG logdet value remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
