from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_routec_payload_value_import_attempt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    attempted = cert["attempted_import"]
    slots = cert["import_slot_resolution"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "SELECTED_ROUTEC_PAYLOAD_VALUE_IMPORT_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN",
        "unexpected Route-C import attempt status",
    )
    require(verdict["attempt_executed"] is True, "attempt should execute")
    require(verdict["selected_values_promotable"] is False, "selected values must not promote")
    require(verdict["all_interface_slots_resolved"] is False, "interface slots must remain unresolved")
    require(verdict["selected_matter_payload_import_closed"] is False, "matter payload import must remain open")
    require(verdict["selected_matter_stress_coefficients_closed"] is False, "stress coefficients must remain open")
    require(verdict["honest_candidate_data_available"] is True, "honest candidate data should be present")
    require(verdict["proof_usable_selected_values_available"] is False, "proof-usable selected values must be absent")
    require(packet["can_import_to_gr_stress_gate"] is False, "packet must block GR stress import")

    require(attempted["routec_strominger_galerkin_first_run"]["proof_promotion_allowed"] is False, "first run must not promote")
    require(attempted["de_action_candidate"]["selected_by_mtt"] is False, "D_E candidate must be unselected")
    require(attempted["de_action_candidate"]["all_sector_selected_source_verified"] is False, "D_E sector flags must be false")
    require(attempted["c1_primitive_contractions"]["selected_source_verified"] is False, "C1 primitives must be unselected")
    require(all(row["promotable"] is False for row in attempted.values()), "no attempted import should promote")
    require(all(row["resolved"] is False for row in slots.values()), "no import slot should resolve")

    require("selected_by_mtt = false" in note, "note must include selected_by_mtt guardrail")
    note_lower = note.lower()
    require("no selected matter stress coefficients" in note_lower, "note must state no stress coefficients import")
    require(all(guards.values()), "all guardrails must hold")

    print("AUDIT_PASS: Route-C payload value import attempted and correctly blocked on selected source values")


if __name__ == "__main__":
    main()
