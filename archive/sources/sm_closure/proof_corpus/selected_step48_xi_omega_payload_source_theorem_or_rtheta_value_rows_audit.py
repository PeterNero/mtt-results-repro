"""Audit Step48 Omega payload source theorem construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step48_xi_omega_payload_source_theorem_or_rtheta_value_rows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OMEGA_MANIFEST = PACKET_DIR / "step48_omega_payload_source_manifest.packet.json"
STRICT_VALIDATOR = PACKET_DIR / "step48_omega_payload_strict_acceptance_validator.packet.json"
EXECUTION_GATE = PACKET_DIR / "step48_rtheta_alpha1_value_execution_gate.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step48_next_omega_payload_clause_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step48_XiOmegaPayloadSourceTheorem_or_RThetaValueRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP48_XI_OMEGA_PAYLOAD_SOURCE_THEOREM_CONSTRUCTED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_OmegaPayloadClauseFill_or_RThetaAlpha1ValueExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    manifest = load(OMEGA_MANIFEST)
    validator = load(STRICT_VALIDATOR)
    execution = load(EXECUTION_GATE)
    frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem construction not proved")

    for packet in [data, manifest, validator, execution, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(manifest["theorem_object"]["constructed"] is True, "Omega theorem object not constructed")
    require(manifest["payload_slot_count"] == 10, "payload slot count mismatch")
    require(manifest["charged_payload_slot_count"] == 9, "charged payload count mismatch")
    require(manifest["higgs_payload_slot_count"] == 1, "Higgs payload count mismatch")
    require(manifest["accepted_payload_source_row_count"] == 0, "payload rows overaccepted")
    require(manifest["accepted_charged_payload_source_row_count"] == 0, "charged payload rows overaccepted")
    require(manifest["higgs_payload_source_row_closed"] is False, "Higgs payload overclosed")
    for slot in manifest["payload_slots"]:
        require(slot["formal_payload_term"].startswith(slot["omega_id"]), f"bad payload term: {slot['omega_id']}")
        require(slot["accepted_as_magnitude_payload_source_row"] is False, f"payload overaccepted: {slot['omega_id']}")
        require(slot["postcheck_used_as_selector"] is False, f"postcheck selector: {slot['omega_id']}")
        require(slot["closed_clause_count"] < slot["required_clause_count"], f"payload unexpectedly full: {slot['omega_id']}")
        require(slot["strict_source_clauses"]["no_observed_selector_proof"] is True, "selector proof missing")

    require(validator["accepted_source_row_count_seen_by_vsd02"] == 0, "VSD02 accepted rows changed")
    require(validator["accepted_payload_source_row_count"] == 0, "validator payload overaccepted")
    require(validator["all_payload_rows_accepted"] is False, "validator overclosed all payloads")
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
        require(key in validator["missing_global_clauses"], f"missing global clause not recorded: {key}")

    require(execution["Rtheta_alpha1_map_constructed"] is True, "map not constructed")
    require(execution["Xi_argument_shells_constructed"] is True, "Xi shells missing")
    require(execution["Omega_payload_theorem_manifest_constructed"] is True, "Omega manifest missing")
    require(execution["accepted_payload_source_row_count"] == 0, "execution payload overaccepted")
    require(execution["required_payload_source_row_count"] == 10, "execution payload count mismatch")
    require(execution["value_rows_execute"] is False, "value execution overclaimed")
    require(execution["accepted_internal_Rtheta_coefficient_row_count"] == 0, "coefficient rows overaccepted")
    require(execution["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(execution["selected_lambda_H_row_closed"] is False, "lambda_H overclosed")

    closed_now = frontier["closed_now"]
    require(closed_now["XiOmegaMagnitudePayloadSourceTheorem_manifest"] is True, "frontier theorem missing")
    require(closed_now["all_10_Omega_payload_slots_constructed"] is True, "frontier payload slots missing")
    require(closed_now["strict_payload_acceptance_validator_constructed"] is True, "frontier validator missing")
    require(frontier["still_open"]["internal_Rtheta_value_rows"] is True, "internal rows not open")
    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")

    decision = data["closure_decision"]
    require(decision["omega_payload_source_theorem_manifest_constructed"] is True, "decision manifest missing")
    require(decision["omega_payload_slot_count"] == 10, "decision slot count mismatch")
    require(decision["accepted_payload_source_row_count"] == 0, "decision payload overaccepted")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "decision coefficient overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar overaccepted")
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
        "Omega payload slots constructed       : 10",
        "accepted Omega payload source rows    : 0",
        "accepted internal Rtheta value rows   : 0",
        "Step42 values remain",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
