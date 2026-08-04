"""Audit selected H-response value-source functional or direct Herm(2) rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hresponsevaluesourcefunctional_or_directherm2rows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HResponseValueSourceFunctional_or_DirectHerm2Rows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

FUNCTIONAL = BASE / "hresponse_value_source_functional.packet.json"
DIRECT_ROWS = BASE / "direct_herm2_row_emission_run.packet.json"
ROUTES = BASE / "current_value_route_acceptance_matrix.packet.json"
CUTSET = BASE / "next_cutset_after_hresponse_value_source_functional.packet.json"

STATUS = (
    "MTT_SELECTED_HRESPONSEVALUESOURCEFUNCTIONAL_OR_DIRECTHERM2ROWS_"
    "FUNCTIONAL_CONTRACT_EXECUTED_ZERO_VALUE_ROWS"
)
NEXT = "MTT_Selected_FiniteHFunctionalCandidate_or_DirectHerm2RowEmissionRun_v1"
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
    functional = load(FUNCTIONAL)
    direct = load(DIRECT_ROWS)
    routes = load(ROUTES)
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
        "value_source_functional_contract_closed",
        "domain_and_row_extractors_closed",
        "current_value_routes_rechecked",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_F_H_functional_emitted",
        "selected_F_H_second_variation_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "selected_logdet_from_H_response_emitted",
        "R_H_RG_logdet_value_executed",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_H_response_source_row_count"] == 0, "H rows")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")
    require(decision["accepted_R_H_RG_source_count"] == 0, "RHRG rows")

    nums = candidate["key_numbers"]
    require(nums["value_routes_checked"] == 4, "routes checked")
    require(nums["accepted_value_source_routes"] == 0, "accepted routes")
    require(nums["required_direct_Herm2_row_or_certificate_count"] == 8, "required direct rows")
    require(nums["emitted_direct_Herm2_row_or_certificate_count"] == 0, "emitted direct rows")
    require(nums["accepted_H_response_source_row_count"] == 0, "accepted H rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "accepted RHRG rows")
    require(abs(nums["UP_RET_OVERLAP_HRG_diagnostic_only"] - HRG) < 1e-12, "HRG")
    require(abs(nums["static_H_logdet_support"] - STATIC_LOGDET) < 1e-12, "static")
    require(nums["selected_K_source_rows"] == 9, "K rows")
    require(nums["selected_K_rows_required"] == 10, "K required")

    flags = candidate["support_flags"]
    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "dynamic_Hessian_domain_on_BHuv_closed",
        "second_variation_source_gate_closed",
        "MH_three_row_source_functional_contract_closed",
    ]:
        require(flags[key] is True, f"support true {key}")
    for key in [
        "strict_MH_packet_currently_passes",
        "MH_search_found_selected_rows",
        "H_specific_acceptance_rows_emitted",
    ]:
        require(flags[key] is False, f"support false {key}")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "value_source_functional_contract_closed",
        "domain_and_row_extractors_closed",
        "current_value_routes_rechecked",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "selected_F_H_functional_emitted",
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
    require(cert["accepted_value_source_routes"] == 0, "cert routes")
    require(cert["accepted_H_response_source_row_count"] == 0, "cert H rows")
    require(cert["accepted_R_H_RG_source_count"] == 0, "cert RHRG")

    require(functional["status"] == "VALUE_SOURCE_FUNCTIONAL_CONTRACT_CLOSED_EXECUTED_ZERO_ROWS", "functional status")
    require(functional["execution_decision"]["value_source_functional_contract_closed"] is True, "functional closed")
    require(functional["closed_domain_inputs"]["B_Huv_domain_closed"] is True, "B_Huv domain")
    require(functional["closed_domain_inputs"]["P_H_projector_closed"] is True, "P_H")
    require(functional["closed_domain_inputs"]["R_H_restriction_closed"] is True, "R_H")
    require(functional["closed_domain_inputs"]["Herm2_row_extractors_closed"] is True, "extractors")
    require(functional["closed_domain_inputs"]["dynamic_Hessian_domain_on_BHuv_closed"] is True, "dynamic")
    require(functional["closed_domain_inputs"]["MH_three_row_source_functional_contract_closed"] is True, "MH contract")
    require("direct_F_H_second_variation" in functional["accepted_value_source_contract"], "F_H contract")
    require("direct_Herm2_rows_required" in functional["accepted_value_source_contract"], "direct rows contract")
    for key in [
        "selected_F_H_functional_emitted",
        "selected_F_H_second_variation_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "lambda_H_predicted",
    ]:
        require(functional["execution_decision"][key] is False, f"functional false {key}")
    require(functional["execution_decision"]["accepted_H_response_source_row_count"] == 0, "functional H rows")
    require_no_selector(functional, "functional")

    require(direct["status"] == "DIRECT_HERM2_ROW_RUN_EXECUTED_ZERO_ACCEPTED_ROWS", "direct status")
    require(direct["decision"]["required_row_count"] == 8, "direct required")
    require(direct["decision"]["emitted_row_count"] == 0, "direct emitted")
    require(direct["decision"]["accepted_row_count"] == 0, "direct accepted")
    for key in [
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "source_ownership_certificate_emitted",
        "same_source_exactness_or_error_certificate_emitted",
        "quotient_admissibility_certificate_emitted",
    ]:
        require(direct["decision"][key] is False, f"direct false {key}")
    row_ids = {row["row_id"] for row in direct["required_rows"]}
    for row_id in [
        "Huu",
        "Hud_re",
        "Hud_im",
        "Hdd",
        "Hdu_equals_conj_Hud_certificate",
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
    ]:
        require(row_id in row_ids, f"missing direct row {row_id}")
    for row in direct["required_rows"]:
        require(row["emitted"] is False, f"row emitted {row['row_id']}")
        require(row["accepted"] is False, f"row accepted {row['row_id']}")
    require_no_selector(direct, "direct")

    require(routes["status"] == "ALL_CURRENT_ROUTES_RECHECKED_NO_ACCEPTED_VALUE_SOURCE", "routes status")
    require(routes["decision"]["routes_checked"] == 4, "route count")
    require(routes["decision"]["accepted_value_source_routes"] == 0, "route accepted")
    require(routes["decision"]["all_open_fields_are_source_emission_fields"] is True, "source fields")
    require(routes["decision"]["no_basis_or_domain_blocker_remaining"] is True, "domain not blocker")
    route_ids = {row["route_id"] for row in routes["route_rows"]}
    for route_id in [
        "direct_F_H_second_variation",
        "direct_Herm2_rows",
        "full_M_source_plus_R_H_restriction",
        "C5C6_projection_bridge",
    ]:
        require(route_id in route_ids, f"missing route {route_id}")
    for row in routes["route_rows"]:
        require(row["passes_value_source_functional"] is False, f"route passed {row['route_id']}")
        require(row["missing"], f"route missing list {row['route_id']}")
    require_no_selector(routes, "routes")

    require(cutset["status"] == "NEXT_FRONTIER_FINITE_H_FUNCTIONAL_OR_DIRECT_HERM2_ROW_EMISSION", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("accepted H-response value-source functional contract" in cutset["closed_here"], "cutset closed")
    require("selected finite H-sector functional F_H" in cutset["still_open"], "cutset F_H")
    require("selected nonzero Herm(2) Hessian/value rows Huu,Hud_re,Hud_im,Hdd" in cutset["still_open"], "cutset rows")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "Accepted value-source routes: `0`",
        "Accepted H-response source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H-response value-source functional contract is closed and "
        "all current value routes execute with zero accepted source rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
