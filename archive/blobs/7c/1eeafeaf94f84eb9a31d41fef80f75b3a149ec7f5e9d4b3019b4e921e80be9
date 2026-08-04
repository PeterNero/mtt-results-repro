"""Audit Step49 Omega payload clause-owner construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OWNER_LEDGER = PACKET_DIR / "step49_omega_clause_owner_ledger.packet.json"
ROW_TEMPLATES = PACKET_DIR / "step49_omega_source_row_templates.packet.json"
OPERATOR_BRIDGE = PACKET_DIR / "step49_operator_payload_bridge_recheck.packet.json"
EXECUTION_RECHECK = PACKET_DIR / "step49_rthetaalpha1_value_execution_recheck.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step49_next_clause_owner_theorem_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step49_OmegaPayloadClauseFill_or_RThetaAlpha1ValueExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP49_OMEGA_PAYLOAD_CLAUSEFILL_OWNERS_LOCKED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_OmegaClauseOwnerTheorems_or_RThetaAlpha1Rows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ledger = load(OWNER_LEDGER)
    templates = load(ROW_TEMPLATES)
    bridge = load(OPERATOR_BRIDGE)
    execution = load(EXECUTION_RECHECK)
    frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step49 theorem not proved")

    for packet in [data, ledger, templates, bridge, execution, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(ledger["owner_count"] == 8, "owner count mismatch")
    require(ledger["all_owners_bound"] is True, "not all owners bound")
    require(ledger["closed_owner_count"] == 0, "value-bearing owners overclosed")
    require(ledger["open_owner_count"] == 8, "open owner count mismatch")
    require(ledger["all_value_bearing_clauses_closed"] is False, "global clauses overclosed")
    clause_ids = {item["clause_id"] for item in ledger["owners"]}
    for key in [
        "accepted_vsd02_source_rows",
        "magnitude_bearing_projection_weights",
        "generation_resolved_threshold_source_rows",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "true_precision_scale_scheme_loop_convention",
        "full_profile_likelihood",
        "selected_higher_response_operator_payload",
    ]:
        require(key in clause_ids, f"missing owner clause: {key}")
    for item in ledger["owners"]:
        require(item["owner_packet"], f"empty owner packet: {item['clause_id']}")
        require(item["blocking_theorem"], f"empty blocking theorem: {item['clause_id']}")
        require(item["accepted_for_value_execution_now"] is False, f"owner overaccepted: {item['clause_id']}")

    require(templates["template_count"] == 10, "template count mismatch")
    require(templates["accepted_template_count"] == 0, "templates overaccepted")
    for row in templates["templates"]:
        require(row["row_id"].endswith(".source_row_template"), f"bad row id: {row['row_id']}")
        require(row["source_owner"] == "selected_MTT_branch", f"bad source owner: {row['row_id']}")
        require(row["value_payload"] is None, f"value payload overfilled: {row['row_id']}")
        require(row["accepted_as_source_row"] is False, f"source row overaccepted: {row['row_id']}")
        require(row["clause_status"]["no_observed_selector_proof"] is True, "selector proof missing")
        require(row["closed_clause_count"] == 1, f"unexpected closed count: {row['row_id']}")
        require(row["required_clause_count"] in {8, 9}, f"bad required count: {row['row_id']}")

    require(bridge["dotD_alpha1_payload_closed"] is True, "dotD alpha1 support not imported")
    require(bridge["diagonal_End0_operator_payload_closed"] is True, "diagonal End0 support not imported")
    require(bridge["selected_operator_payload_closed"] is False, "selected operator overclosed")
    require(bridge["selected_HYM_sector_payload_closed"] is False, "selected HYM sector overclosed")
    require(bridge["promotable_to_omega_now"] is False, "operator bridge overpromoted")

    require(execution["Rtheta_alpha1_map_constructed"] is True, "Rtheta_alpha1 map missing")
    require(execution["step48_payload_manifest_constructed"] is True, "Step48 manifest not imported")
    require(execution["omega_clause_owners_locked"] is True, "owners not locked")
    require(execution["omega_source_row_templates_filled"] is True, "row templates not filled")
    require(execution["accepted_omega_source_rows"] == 0, "accepted source rows overclosed")
    require(execution["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta rows overclosed")
    require(execution["accepted_internal_scalar_row_count"] == 0, "scalar rows overclosed")
    require(execution["selected_lambda_H_row_closed"] is False, "lambda_H overclosed")
    require(execution["value_rows_execute"] is False, "value execution overclaimed")
    for key in [
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(execution[key] is False, f"execution overclosed: {key}")
        require(data["closure_decision"][key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")

    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")
    require(frontier["closed_now"]["all_8_global_clause_owners_bound"] is True, "frontier owners not closed")
    require(frontier["closed_now"]["all_10_omega_source_row_templates_filled"] is True, "frontier templates not closed")
    require(frontier["closed_now"]["operator_payload_bridge_rechecked"] is True, "frontier bridge missing")
    require(frontier["closed_now"]["Rtheta_alpha1_execution_rechecked"] is True, "frontier recheck missing")
    require(len(frontier["next_owner_theorems_in_order"]) == 8, "next theorem count mismatch")

    decision = data["closure_decision"]
    require(decision["omega_clause_owners_locked"] is True, "decision owners not locked")
    require(decision["omega_source_row_templates_filled"] is True, "decision templates not filled")
    require(decision["accepted_omega_source_rows"] == 0, "decision source rows overaccepted")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "decision Rtheta rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "global clause owners locked           : 8/8",
        "Omega source-row templates filled     : 10/10",
        "accepted Omega source rows            : 0",
        "accepted internal Rtheta rows         : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
