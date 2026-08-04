"""Audit second Qa/SU3 operator-source slot closure or production profile import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_secondqasu3operatorslotclosure_or_productionprofileimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SECOND_SLOT = PACKET_DIR / "second_qasu3_operator_source_slot_closure.packet.json"
PRODUCTION = PACKET_DIR / "production_profile_import_status.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_second_slot.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsProductionProfileImport_or_SecondQaSU3OperatorSlotClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_SECONDQASU3OPERATORSLOTCLOSURE_OR_PRODUCTIONPROFILEIMPORT_BUILT_TWO_OPERATOR_SOURCE_SLOTS_CLOSED"
NEXT = "MTT_Selected_ThirdQaSU3OperatorSlotClosure_or_ProductionWorkspaceImport_v1"
FIRST_SLOT = "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source"
SECOND_SLOT_NAME = "standard_lattice_base_ordering_and_base_swap_breaking"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    second_slot = load(SECOND_SLOT)
    production = load(PRODUCTION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(second_slot["filled_slot"] == SECOND_SLOT_NAME, "second slot mismatch")
    value = second_slot["selected_source_value"]
    require(value["standard_lattice_or_equivalent_selected"] is True, "standard lattice not selected")
    require(value["base_factor_order_selected"] is True, "base order not selected")
    require(value["base_order"] == "E1/g1g2 carries +2 and E2/g3g4 carries -4", "base order value mismatch")
    require(value["selected_source_label"] == "g3 / L3-K2", "source label mismatch")
    require(value["selected_L"] == [1, -2, 0], "selected L mismatch")
    require(value["selected_L2"] == [2, -4, 0], "selected L2 mismatch")
    require(value["status"] == "UNCONDITIONAL_IN_PATCHED_PROOF_SPINE", "patched-spine status mismatch")
    for key, closed in second_slot["proof_inputs"].items():
        require(closed is True, f"proof input not closed: {key}")
    slot_status = second_slot["slot_status_after_closure"]
    require(slot_status["required_operator_slot_count"] == 8, "required slot count mismatch")
    require(slot_status["filled_operator_slot_count"] == 2, "filled slot count mismatch")
    require(slot_status["filled_slots"] == [FIRST_SLOT, SECOND_SLOT_NAME], "filled slots mismatch")
    require(slot_status["remaining_missing_slot_count"] == 6, "remaining missing slot count mismatch")
    require(SECOND_SLOT_NAME not in slot_status["missing_slots"], "second slot still missing")
    closure = second_slot["closure_result"]
    require(closure["second_operator_source_slot_closed"] is True, "second slot not closed")
    require(closure["selected_source_value_emitted"] is True, "selected source value missing")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")

    require(production["production_profile_imported_now"] is False, "production profile overimported")
    require(production["production_workspace_imported_now"] is False, "production workspace overimported")
    require(decision["operator_source_slots_closed"] == 2, "decision closed slot count mismatch")
    require(decision["operator_source_slots_remaining"] == 6, "decision remaining slot count mismatch")
    require(decision["closed_slots"] == [FIRST_SLOT, SECOND_SLOT_NAME], "decision closed slots mismatch")
    require(decision["production_profile_imported"] is False, "decision production overimported")
    require(decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "decision dynamic packet overclosed")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure_decision = data["closure_decision"]
    require(closure_decision["second_QaSU3_operator_source_slot_closed"] is True, "candidate second slot missing")
    require(closure_decision["operator_source_slots_closed_total"] == 2, "candidate total slots mismatch")
    require(closure_decision["production_profile_imported"] is False, "candidate production overimported")
    require(closure_decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(closure_decision["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["what_closes_now"]["standard_lattice_base_ordering_and_base_swap_breaking_slot"] is True, "second slot close flag missing")
    require(data["what_closes_now"]["qasu3_operator_cutset_reduced_to_six_slots"] is True, "cutset reduction flag missing")
    require(data["what_remains_open"]["operator_layer_Pic0_or_physical_quotient"] is True, "Pic0 gate missing")
    require(data["what_remains_open"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic gate missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims full closure")
    require("second Qa/SU3 operator-source slot" in note, "note missing second slot")
    require("six remaining slots" in note, "note missing six-slot frontier")

    for packet in [data, second_slot, production, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
