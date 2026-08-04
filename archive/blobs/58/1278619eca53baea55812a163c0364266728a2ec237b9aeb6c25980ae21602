"""Audit Step46 selected alpha1-to-Rtheta coefficient map."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MAP_PACKET = PACKET_DIR / "step46_selected_alpha1_to_rtheta_coefficient_map.packet.json"
ARGUMENT_AUDIT = PACKET_DIR / "step46_map_argument_closure_audit.packet.json"
VALUE_ATTEMPT = PACKET_DIR / "step46_value_execution_attempt.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step46_next_value_execution_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step46_Alpha1ToRThetaCoefficientMap_or_ValueExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP46_ALPHA1_TO_RTHETA_COEFFICIENT_MAP_CONSTRUCTED_VALUE_EXECUTION_OPEN"
NEXT = "MTT_Selected_Alpha1RThetaMapArgumentFill_or_InternalValueRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    selected_map = load(MAP_PACKET)
    arguments = load(ARGUMENT_AUDIT)
    value_attempt = load(VALUE_ATTEMPT)
    frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "map construction theorem not proved")

    for packet in [data, selected_map, arguments, value_attempt, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(selected_map["map_symbol"] == "Rtheta_alpha1", "map symbol mismatch")
    require(selected_map["map_domain_closed"] is True, "map domain not closed")
    require(selected_map["codomain_row_count"] == 10, "codomain count mismatch")
    require(len(selected_map["charged_rows"]) == 9, "charged row count mismatch")
    require(selected_map["accepted_value_row_count"] == 0, "value rows overaccepted")
    require(selected_map["source_anchor"]["name"] == "alpha1_source_strength_anchor", "anchor mismatch")
    require(selected_map["source_anchor"]["lambda_alpha1"] == 1.0, "lambda alpha1 mismatch")
    require(selected_map["source_anchor"]["N_alpha1_h_ext"] == 1.0, "N alpha1 mismatch")
    require(selected_map["source_anchor"]["alpha1_driver_verified"] is True, "alpha1 driver missing")
    require(selected_map["higgs_row"]["coefficient_slot"] == "lambda_H", "Higgs row mismatch")
    require(selected_map["higgs_row"]["accepted_as_internal_value_row"] is False, "Higgs overaccepted")
    for row in selected_map["charged_rows"]:
        require(row["accepted_as_internal_value_row"] is False, f"row overaccepted: {row['row_id']}")
        require("Rtheta_alpha1" in row["map_formula"], f"row formula missing map: {row['row_id']}")
        require(row["required_unfilled_argument"].startswith("Xi_"), f"missing Xi arg: {row['row_id']}")

    require(arguments["map_domain_closed"] is True, "argument audit map domain open")
    require(arguments["all_value_execution_arguments_closed"] is False, "arguments overclosed")
    for key in [
        "magnitude_bearing_projection_weights",
        "selected_threshold_response_instantiation",
        "generation_resolved_threshold_source_rows",
        "selected_internal_threshold_mass_derivation",
    ]:
        require(key in arguments["missing_arguments"], f"missing argument not recorded: {key}")

    require(value_attempt["selected_map_constructed"] is True, "value attempt map missing")
    require(value_attempt["all_value_execution_arguments_closed"] is False, "value args overclosed")
    require(value_attempt["accepted_internal_value_row_count"] == 0, "value rows overaccepted")
    require(value_attempt["accepted_charged_coefficient_row_count"] == 0, "charged rows overaccepted")
    require(value_attempt["lambda_H_internal_row_closed"] is False, "lambda_H overclosed")
    require(value_attempt["postcheck_values_available"] is True, "postchecks unavailable")
    require(value_attempt["postcheck_values_used_as_selectors"] is False, "postchecks used as selectors")

    closed_now = frontier["closed_now"]
    require(closed_now["selected_alpha1_to_Rtheta_coefficient_map"] is True, "frontier map not closed")
    require(closed_now["ten_row_codomain_ledger_constructed"] is True, "frontier codomain missing")
    require(frontier["still_open"]["magnitude_bearing_Xi_sg_arguments"] is True, "Xi frontier missing")
    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")

    decision = data["closure_decision"]
    require(decision["selected_alpha1_to_Rtheta_coefficient_map_constructed"] is True, "decision map missing")
    require(decision["all_value_execution_arguments_closed"] is False, "decision arguments overclosed")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "decision coefficient rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    for key in [
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "Rtheta_alpha1",
        "selected alpha1 -> Rtheta coefficient map constructed : true",
        "accepted internal charged coefficient rows            : 0",
        "Step42 values are retained only as postchecks",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
