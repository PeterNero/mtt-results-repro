"""Audit M_source Huv operator or direct Herm(2) rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_msourcehuvoperator_or_directherm2rows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MSourceHuvOperator_or_DirectHerm2Rows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

MSOURCE_CONTRACT = BASE / "msource_contract_reconciled_with_active_domain.packet.json"
MSOURCE_ATTEMPT = BASE / "msource_execution_attempt_after_bhuv_rh_import.packet.json"
DIRECT_ATTEMPT = BASE / "direct_herm2_rows_after_msource_contract.packet.json"
DIAGONAL_GUARD = BASE / "diagonal_hym_metric_not_msource_guard.packet.json"
CUTSET = BASE / "next_cutset_after_msource_directherm2_attempt.packet.json"

STATUS = "MTT_SELECTED_MSOURCEHUVOPERATOR_OR_DIRECTHERM2ROWS_CONTRACT_RECONCILED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_HResponseTableValueRows_or_DirectHerm2ValueRows_v1"


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
    contract = load(MSOURCE_CONTRACT)
    attempt = load(MSOURCE_ATTEMPT)
    direct = load(DIRECT_ATTEMPT)
    guard = load(DIAGONAL_GUARD)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "M_source_acceptance_contract_reconciled",
        "B_Huv_R_H_domain_available",
        "diagonal_HYM_metric_rechecked_not_M_source",
        "M_source_execution_attempted",
        "direct_Herm2_row_execution_attempted",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "Huv_values_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_F_Huv_rows_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["accepted_H_response_source_row_count"] == 0, "H response rows")
    require(nums["emitted_direct_Herm2_row_or_certificate_count"] == 0, "direct emitted")
    require(nums["required_direct_Herm2_row_or_certificate_count"] == 8, "direct required")
    require(nums["accepted_value_source_routes"] == 0, "value routes")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "M_source_acceptance_contract_reconciled",
        "B_Huv_R_H_domain_available",
        "diagonal_HYM_metric_rechecked_not_M_source",
        "M_source_execution_attempted",
        "direct_Herm2_row_execution_attempted",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "Huv_values_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_F_Huv_rows_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(contract["status"] == "MSOURCE_CONTRACT_RECONCILED_ACTIVE_DOMAIN_CLOSED_VALUES_OPEN", "contract status")
    imported = contract["imported_h7b1i_contract"]
    require(imported["M_source_acceptance_functor_built"] is True, "H7B1I functor")
    require(imported["M_source_value_emitted"] is False, "H7B1I value")
    active = contract["active_domain_supersessions"]
    for key in [
        "B_Huv_symbolic_exact_payload_emitted",
        "R_H_restriction_closed",
        "P_H_projector_closed",
        "dynamic_Hessian_domain_on_BHuv_closed",
        "Herm2_row_extractors_closed",
    ]:
        require(active[key] is True, f"active {key}")
    formula = contract["updated_formula"]
    require("R_H^* H_response R_H" in formula["M_source"], "M_source formula")
    require(formula["Huv"] == "H_uv = B_Huv^* M_source B_Huv", "Huv formula")
    require(contract["decision"]["B_Huv_and_R_H_domain_closed"] is True, "domain closed")
    require(contract["decision"]["M_source_values_emitted"] is False, "contract values")
    require_no_selector(contract, "contract")

    require(attempt["status"] == "MSOURCE_EXECUTION_ATTEMPTED_DOMAIN_CLOSED_ZERO_VALUES", "attempt status")
    support = attempt["available_support"]
    require(support["available_prefix_is_sufficient_for_contract"] is True, "prefix contract")
    require(support["available_prefix_is_sufficient_for_values"] is False, "prefix values")
    missing = attempt["strict_missing_after_active_domain_reconciliation"]
    for key in [
        "selected_H_response_table",
        "selected_Hermitian_M_source_entries",
        "direct_Huv_values",
        "source_exactness_or_error_certificate",
    ]:
        require(missing[key] is True, f"missing {key}")
    for value in attempt["computed_values"].values():
        require(value is None, "attempt value emitted")
    adec = attempt["decision"]
    require(adec["M_source_execution_attempted"] is True, "M attempted")
    require(adec["B_Huv_R_H_domain_available"] is True, "domain available")
    for key in [
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "Huv_values_emitted",
    ]:
        require(adec[key] is False, f"attempt false {key}")
    require_no_selector(attempt, "attempt")

    require(direct["status"] == "DIRECT_HERM2_ROWS_EXECUTED_ZERO_ACCEPTED_AFTER_MSOURCE_CONTRACT", "direct status")
    require(direct["direct_route_status"] == "schema_closed_rows_open", "direct route")
    require(len(direct["required_rows"]) == 8, "direct rows length")
    for value in direct["emitted_rows"].values():
        require(value is None, "direct value emitted")
    ddec = direct["decision"]
    require(ddec["direct_Herm2_row_execution_attempted"] is True, "direct attempted")
    require(ddec["direct_Herm2_Huv_payload_emitted"] is False, "direct payload")
    require(ddec["direct_Huu_Hud_Hdd_emitted"] is False, "direct H rows")
    require(ddec["accepted_row_count"] == 0, "direct accepted")
    require(ddec["accepted_certificate_count"] == 0, "direct cert")
    require_no_selector(direct, "direct")

    require(guard["status"] == "DIAGONAL_HYM_METRIC_RECHECKED_NOT_MSOURCE_OR_DIRECT_HERM2_ROWS", "guard status")
    require(guard["diagonal_HYM_support"]["selected_HYM_metric_or_connection_on_E_H_UV"] is True, "guard HYM")
    require(guard["prior_rejection"]["accepted_as_non_diagonal_Huv_source"] is False, "prior rejection")
    require(guard["H7B1S_direct_nonlinear_attempt"]["direct_nonlinear_HYM_row_execution_closes_Huv"] is False, "H7B1S")
    require(guard["decision"]["diagonal_metric_retired_as_M_source_value"] is True, "metric not M")
    require(guard["decision"]["diagonal_metric_retired_as_direct_Herm2_rows"] is True, "metric not rows")
    require(guard["decision"]["M_source_values_emitted"] is False, "guard M")
    require(guard["decision"]["direct_Herm2_rows_emitted"] is False, "guard rows")
    require_no_selector(guard, "guard")

    require(cutset["status"] == "NEXT_FRONTIER_HRESPONSE_TABLE_VALUE_ROWS_OR_DIRECT_HERM2_VALUE_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "M_source acceptance contract reconciled with active B_Huv/R_H domain",
        "H7B1I old missing-domain language superseded where active B_Huv/R_H is closed",
        "diagonal HYM metric rechecked and rejected as M_source/direct Herm(2) values",
        "direct Herm(2) row execution rerun with zero accepted rows",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected H_response table value rows",
        "selected Hermitian M_source entries",
        "or direct source-owned Huu,Hud,Hdd Herm(2) rows",
        "same-source exactness/error and source ownership certificates",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2",
        "selected `M_source` entries: `0`",
        "direct `Huu,Hud,Hdd` rows: `0`",
        "not a Higgs mass/strain Hessian",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: M_source contract reconciled with active B_Huv/R_H domain; "
        "H_response/M_source/direct Herm(2) value rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
