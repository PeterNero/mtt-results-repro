"""Audit full-loop precision import or Qa/SU3 operator-slot fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECISION = PACKET_DIR / "precision_observable_table_full_loop_import_attempt.packet.json"
QASU3 = PACKET_DIR / "qasu3_operator_slot_fill_attempt.packet.json"
DECISION = PACKET_DIR / "promotion_decision_after_full_loop_or_slot_fill.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionObservableTable_FullLoopImport_or_QaSU3OperatorSlotFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRECISIONOBSERVABLETABLE_FULLLOOPIMPORT_OR_QASU3OPERATORSLOTFILL_BUILT_PROXY_INVENTORY_SLOTS_OPEN"
NEXT = "MTT_Selected_AcceptedPrecisionProfileImport_or_SelectedQaSU3OperatorSlotSourceValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    precision = load(PRECISION)
    qasu3 = load(QASU3)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    support = precision["support_inventory"]
    require(support["first_loop_QCD_proxy_layer_closed"] is True, "QCD proxy layer not imported")
    require(support["N3LO_QCD_proxy_values_for_Hbb_Hcc"] is True, "N3LO qq proxy not imported")
    require(support["qq_formula_scaffold_closed"] is True, "qq scaffold not imported")
    require(support["remaining_EW_formula_import_gate_built"] is True, "EW import gate not imported")
    require(support["profile_acceptance_controller_built"] is True, "profile controller not imported")
    require(support["rehearsal_profile_structurally_valid"] is True, "profile rehearsal structure not imported")

    accepted = precision["accepted_precision_import_status"]
    require(accepted["accepted_profile_import"] is False, "profile import overaccepted")
    require(accepted["accepted_row_replacements"] == 0, "row replacements unexpectedly accepted")
    require(accepted["precision_total_width_closed"] is False, "precision total width overclosed")
    require(accepted["precision_branching_ratios_closed"] is False, "precision branching ratios overclosed")
    require(accepted["full_precision_QFT_values_closed"] is False, "full precision QFT overclosed")

    result = precision["full_loop_import_attempt_result"]
    require(result["attempted"] is True, "full-loop import not attempted")
    require(result["accepted_precision_rows_imported_now"] == 0, "accepted precision rows overimported")
    require(result["proxy_or_scaffold_rows_available"] >= 4, "proxy inventory underspecified")
    require(result["closed_now"] is False, "full-loop import overclosed")

    slots = qasu3["slot_status"]
    require(slots["required_operator_slot_count"] == 8, "operator slot count changed")
    require(slots["filled_operator_slot_count"] == 0, "operator slots unexpectedly filled")
    require(slots["filled_slots"] == [], "filled slot list should be empty")
    require(len(slots["missing_slots"]) == 8, "missing slot list should contain all slots")
    slot_result = qasu3["slot_fill_attempt_result"]
    require(slot_result["attempted"] is True, "slot fill not attempted")
    require(slot_result["new_slots_filled_now"] == 0, "new slots unexpectedly filled")
    require(slot_result["actual_selected_operator_payload_filled"] is False, "actual operator payload overfilled")
    require(slot_result["closed_now"] is False, "slot fill overclosed")
    require(len(qasu3["minimal_slot_source_values_to_emit"]) == 8, "minimal slot source list changed")

    require(decision["status"] == "NO_PRECISION_IMPORT_NO_OPERATOR_SLOT_PROMOTION", "decision status mismatch")
    require(decision["route_A_precision"]["proxy_inventory_built"] is True, "decision missing proxy inventory")
    require(decision["route_A_precision"]["accepted_precision_table_closed"] is False, "decision overclosed precision")
    require(decision["route_A_precision"]["accepted_precision_rows_imported_now"] == 0, "decision overimported rows")
    require(decision["route_B_operator"]["slot_manifest_built"] is True, "decision missing slot manifest")
    require(decision["route_B_operator"]["actual_QaSU3_operator_packet_closed"] is False, "decision overclosed Qa/SU3")
    require(decision["route_B_operator"]["new_slots_filled_now"] == 0, "decision overfilled slots")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["precision_proxy_inventory_built"] is True, "candidate proxy inventory missing")
    require(data["closure_decision"]["operator_slot_manifest_built"] is True, "candidate operator manifest missing")
    require(
        data["closure_decision"]["accepted_precision_observable_table_closed"] is False,
        "candidate overclosed precision table",
    )
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "candidate overclosed Qa/SU3")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require(data["what_closes_now"]["accepted_precision_vs_proxy_boundary_enforced"] is True, "proxy boundary not enforced")
    require(data["what_closes_now"]["eight_slot_operator_manifest_locked"] is True, "slot manifest not locked")
    require(data["what_remains_open"]["accepted_precision_profile_import"] is True, "precision profile gate missing")
    require(data["what_remains_open"]["selected_operator_slot_source_values"] is True, "operator slot values gate missing")
    require("No accepted precision observable/profile table row is imported" in note, "note missing precision guard")
    require("No selected operator slot" in note, "note missing operator guard")

    for packet in [data, precision, qasu3, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
