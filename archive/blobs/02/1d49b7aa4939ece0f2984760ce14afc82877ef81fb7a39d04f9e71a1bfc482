"""Audit H-response spectrum source rows or R_H^RG logdet value execution packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HResponseSpectrumSourceRows_or_RHRGLogDetValueExecution_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

ROW_TABLE = BASE / "hresponse_source_row_execution_table.packet.json"
SPECTRUM_PACKET = BASE / "hresponse_spectrum_from_rows_attempt.packet.json"
RHRG_PACKET = BASE / "rhrg_logdet_value_execution_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_hresponse_source_rows.packet.json"

STATUS = (
    "MTT_SELECTED_HRESPONSESPECTRUMSOURCEROWS_OR_RHRGLOGDETVALUEEXECUTION_"
    "ROW_TABLE_EXECUTED_ZERO_ACCEPTED_ROWS"
)
NEXT = "MTT_Selected_HResponseValueSourceFunctional_or_DirectHerm2Rows_v1"
HRG = 391.39140285811936
STATIC_LOGDET = 43.802475498298655


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
    rows = load(ROW_TABLE)
    spectrum = load(SPECTRUM_PACKET)
    rhrg = load(RHRG_PACKET)
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
    require(decision["hresponse_source_row_table_executed"] is True, "row table")
    for key in [
        "direct_Herm2_rows_emitted",
        "selected_H_response_spectrum_emitted",
        "selected_logdet_from_H_response_emitted",
        "R_H_RG_logdet_value_executed",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_H_response_source_row_count"] == 0, "H response count")
    require(decision["accepted_R_H_RG_source_count"] == 0, "RHRG count")

    nums = candidate["key_numbers"]
    require(nums["required_H_response_row_count"] == 7, "required rows")
    require(nums["emitted_H_response_row_count"] == 0, "emitted rows")
    require(nums["accepted_H_response_source_row_count"] == 0, "accepted H rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "accepted RHRG rows")
    require(abs(nums["UP_RET_OVERLAP_HRG_diagnostic_only"] - HRG) < 1e-12, "HRG")
    require(abs(nums["static_H_logdet_support"] - STATIC_LOGDET) < 1e-12, "static")
    require(nums["selected_K_source_rows"] == 9, "K rows")
    require(nums["selected_K_rows_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["hresponse_source_row_table_executed"] is True, "cert row table")
    for key in [
        "direct_Herm2_rows_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_logdet_value_executed",
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

    require(rows["status"] == "HRESPONSE_SOURCE_ROW_TABLE_EXECUTED_ZERO_ACCEPTED_ROWS", "rows status")
    require(rows["decision"]["required_row_count"] == 7, "rows required")
    require(rows["decision"]["emitted_row_count"] == 0, "rows emitted")
    require(rows["decision"]["accepted_source_row_count"] == 0, "rows accepted")
    require(rows["support_imports"]["MH_three_row_source_functional_contract_closed"] is True, "MH contract")
    require(rows["support_imports"]["second_variation_source_gate_closed"] is True, "second variation")
    require(rows["support_imports"]["dynamic_Hessian_domain_closed"] is True, "dynamic domain")
    require(rows["support_imports"]["strict_mh_current_packet_passes"] is False, "strict MH overpass")
    row_ids = {row["row_id"] for row in rows["source_rows"]}
    for row_id in [
        "Huu",
        "Hud_re",
        "Hud_im",
        "Hdd",
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
    ]:
        require(row_id in row_ids, f"missing row {row_id}")
    for row in rows["source_rows"]:
        require(row["emitted"] is False, f"row emitted {row['row_id']}")
        require(row["accepted"] is False, f"row accepted {row['row_id']}")
    require_no_selector(rows, "rows")

    require(spectrum["status"] == "HRESPONSE_SPECTRUM_FROM_ROWS_NOT_EXECUTABLE_ZERO_ROWS", "spectrum status")
    require(spectrum["execution_inputs"]["accepted_source_row_count"] == 0, "spectrum inputs")
    for key in [
        "selected_H_response_spectrum_emitted",
        "selected_logdet_from_H_response_emitted",
        "positive_spectrum_certificate_emitted",
        "H_response_logdet_executable",
    ]:
        require(spectrum["decision"][key] is False, f"spectrum false {key}")
    require_no_selector(spectrum, "spectrum")

    require(rhrg["status"] == "RHRG_LOGDET_VALUE_EXECUTION_NOT_RUN_HRESPONSE_ROWS_OPEN", "rhrg status")
    require(abs(rhrg["diagnostic_values_not_used_as_source"]["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "rhrg HRG")
    require(abs(rhrg["diagnostic_values_not_used_as_source"]["static_H_logdet"] - STATIC_LOGDET) < 1e-12, "rhrg static")
    require(rhrg["diagnostic_values_not_used_as_source"]["previous_static_logdet_used_as_R_H_RG"] is False, "static promoted")
    for key in [
        "R_H_RG_value_emitted",
        "R_H_RG_logdet_value_executed",
        "lambda_H_predicted",
        "target_independent_validation_run_executed",
    ]:
        require(rhrg["decision"][key] is False, f"rhrg false {key}")
    require(rhrg["decision"]["accepted_R_H_RG_source_count"] == 0, "rhrg source count")
    require_no_selector(rhrg, "rhrg")

    require(cutset["status"] == "NEXT_FRONTIER_HRESPONSE_VALUE_SOURCE_FUNCTIONAL_OR_DIRECT_HERM2_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("H-response source row table executed" in cutset["closed_here"], "cutset closed")
    require("selected finite H-sector functional F_H" in cutset["still_open"], "cutset open")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "Accepted H-response source rows: `0`",
        "No selected H-response spectrum",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H-response source row table is explicit; zero rows/certificates emitted, "
        "so no spectrum/logdet/R_H^RG value executes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
