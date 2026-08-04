"""Audit third Qa/SU3 operator-source slot closure via Pic0 gerbe replacement."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thirdqasu3operatorslotclosure_or_pic0gerbereplacement"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
THIRD_SLOT = PACKET_DIR / "third_qasu3_operator_source_slot_closure.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_pic0_slot.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThirdQaSU3OperatorSlotClosure_or_Pic0GerbeReplacement_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_THIRDQASU3OPERATORSLOTCLOSURE_OR_PIC0GERBEREPLACEMENT_BUILT_THREE_OPERATOR_SOURCE_SLOTS_CLOSED"
NEXT = "MTT_Selected_FourthQaSU3OperatorSlotClosure_or_VisibleChernWeilSource_v1"
SLOT = "Pic0_selection_or_physical_quotient_theorem"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    third = load(THIRD_SLOT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(third["filled_slot"] == SLOT, "filled slot mismatch")
    value = third["selected_source_value"]
    require(value["direct_pic0_invariance_status"] == "RETIRED_FOR_NOW", "direct Pic0 status mismatch")
    require(value["neutral_pic0_selection_status"] == "ABSENT", "neutral Pic0 status mismatch")
    require(value["operator_pic0_replacement"] == "selected_q79_F_m1_S3_gerbe_differential_cohomology_route", "replacement route mismatch")
    require(value["branch"] == {"orientation": "F", "q": 79, "torsion_label_m": 1}, "branch mismatch")
    require(value["source_selected_by_mtt"] is True, "S3 source not selected")
    require(value["fixed_differential_cohomology_class"] is True, "fixed class missing")
    require(value["same_class_as_finite_m1_deck_cocycle"] is True, "finite deck cocycle mismatch")
    for key, closed in third["proof_inputs"].items():
        require(closed is True, f"proof input not closed: {key}")
    for key, closed in third["closed_at_source_or_restriction_level"].items():
        require(closed is True, f"source/restriction support not closed: {key}")

    status = third["slot_status_after_closure"]
    require(status["required_operator_slot_count"] == 8, "required slot count mismatch")
    require(status["filled_operator_slot_count"] == 3, "filled slot count mismatch")
    require(status["remaining_missing_slot_count"] == 5, "remaining slot count mismatch")
    require(SLOT not in status["missing_slots"], "Pic0 slot still missing")
    closure = third["closure_result"]
    require(closure["third_operator_source_slot_closed"] is True, "third slot not closed")
    require(closure["selected_source_value_emitted"] is True, "selected value not emitted")
    require(closure["pic0_closed_by_direct_invariance"] is False, "direct Pic0 overclaimed")
    require(closure["pic0_closed_by_neutral_character_selection"] is False, "neutral Pic0 overclaimed")
    require(closure["pic0_closed_by_selected_gerbe_replacement"] is True, "gerbe replacement not used")
    require(closure["actual_DE_payload_emitted"] is False, "D_E overemitted")
    require(closure["operator_level_projective_rhoe_promoted"] is False, "operator rhoE overpromoted")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")

    require(decision["operator_source_slots_closed"] == 3, "decision closed slots mismatch")
    require(decision["operator_source_slots_remaining"] == 5, "decision remaining slots mismatch")
    require(decision["actual_DE_payload_emitted"] is False, "decision D_E overemitted")
    require(decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "decision dynamic overclosed")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure_decision = data["closure_decision"]
    require(closure_decision["third_QaSU3_operator_source_slot_closed"] is True, "candidate third slot missing")
    require(closure_decision["operator_source_slots_closed_total"] == 3, "candidate total slots mismatch")
    require(closure_decision["Pic0_slot_closed_by_gerbe_replacement"] is True, "candidate Pic0 replacement missing")
    require(closure_decision["actual_DE_payload_emitted"] is False, "candidate D_E overemitted")
    require(closure_decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(data["what_closes_now"]["Pic0_selection_or_physical_quotient_theorem_slot"] is True, "Pic0 close flag missing")
    require(data["what_closes_now"]["qasu3_operator_cutset_reduced_to_five_slots"] is True, "five-slot reduction missing")
    require(data["what_remains_open"]["transition_rhoE_or_Cech_Dolbeault_DE_data"] is True, "transition gate missing")
    require(data["what_remains_open"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic gate missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims full closure")
    require("does **not** prove direct operator-layer Pic0 invariance" in note, "note missing direct Pic0 guard")
    require("five\nremaining slots" in note, "note missing five-slot frontier")

    for packet in [data, third, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
