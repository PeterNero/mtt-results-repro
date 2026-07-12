"""Audit accepted precision import or selected Qa/SU3 operator-slot source values attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EDGE_A = PACKET_DIR / "edge_a_accepted_precision_profile_import_attempt.packet.json"
EDGE_B = PACKET_DIR / "edge_b_selected_qasu3_operator_slot_source_values_attempt.packet.json"
DECISION = PACKET_DIR / "dual_edge_promotion_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedPrecisionProfileImport_or_SelectedQaSU3OperatorSlotSourceValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_ACCEPTEDPRECISIONPROFILEIMPORT_OR_SELECTEDQASU3OPERATORSLOTSOURCEVALUES_BUILT_SUPPORT_DIAGNOSTIC_VALUES_OPEN"
NEXT = "MTT_Selected_ProfileRowReplacementPayload_or_QaSU3SlotSourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    edge_a = load(EDGE_A)
    edge_b = load(EDGE_B)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    profile = edge_a["profile_import_attempt"]
    require(profile["structural_schema_tests_pass"] is True, "profile structural tests not imported")
    require(profile["precision_acceptance_tests_pass"] is False, "profile precision tests overaccepted")
    require(profile["accepted_as_profile_convention_import"] is False, "profile import overaccepted")
    require(profile["accepted_precision_row_count"] == 0, "profile row count overaccepted")
    require(len(profile["rejection_reasons"]) >= 3, "profile rejection reasons missing")

    rows = edge_a["row_replacement_attempt"]
    require(rows["row_count"] == 10, "row replacement controller row count changed")
    require(rows["accepted_row_count"] == 0, "row replacements unexpectedly accepted")
    require(len(rows["blocked_channels"]) == 10, "blocked channel count mismatch")
    require(rows["route_A_formula_fallback_available_for_all_rows"] is True, "route A fallback not available")
    require(rows["profile_import_still_preferred_for_bulk_precision"] is True, "profile preference missing")
    require(edge_a["promotion_result"]["edge_attempted"] is True, "edge A not attempted")
    require(edge_a["promotion_result"]["accepted_precision_rows_imported_now"] == 0, "edge A imported rows unexpectedly")
    require(edge_a["promotion_result"]["closed_now"] is False, "edge A overclosed")

    slots = edge_b["slot_summary"]
    require(slots["required_operator_slot_count"] == 8, "slot count changed")
    require(slots["support_slots_present_count"] >= 4, "support slot diagnostics too weak")
    require(slots["selected_source_values_emitted_count"] == 0, "selected slot values overemitted")
    require(slots["selected_slots"] == [], "selected slot list should be empty")
    require(len(slots["missing_selected_slots"]) == 8, "missing selected slots should include all slots")
    for slot, status in edge_b["slot_source_value_attempt"].items():
        require("support_present" in status, f"slot missing support flag: {slot}")
        require(status["selected_source_value_emitted"] is False, f"slot overselected: {slot}")
        require(status["blocking_condition"], f"slot blocking condition missing: {slot}")
    require(edge_b["promotion_result"]["edge_attempted"] is True, "edge B not attempted")
    require(edge_b["promotion_result"]["selected_operator_slot_source_values_closed"] is False, "edge B source values overclosed")
    require(edge_b["promotion_result"]["actual_QaSU3_operator_packet_closed"] is False, "edge B Qa/SU3 overclosed")
    require(edge_b["promotion_result"]["new_selected_slots_filled_now"] == 0, "edge B filled slots unexpectedly")

    require(decision["status"] == "BOTH_EDGES_ATTEMPTED_SUPPORT_ONLY_VALUES_OPEN", "decision status mismatch")
    require(decision["edge_A"]["accepted_precision_import_closed"] is False, "decision overclosed edge A")
    require(decision["edge_A"]["accepted_row_replacements"] == 0, "decision overaccepted row replacements")
    require(decision["edge_B"]["actual_QaSU3_operator_packet_closed"] is False, "decision overclosed edge B")
    require(decision["edge_B"]["selected_operator_slot_source_values"] == 0, "decision overemitted slot values")
    require(decision["edge_B"]["support_slots_present_count"] >= 4, "decision missing support diagnostics")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["accepted_precision_profile_import_closed"] is False, "candidate overclosed precision import")
    require(data["closure_decision"]["selected_operator_slot_source_values_closed"] is False, "candidate overclosed slot values")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "candidate overclosed Qa/SU3")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require(data["what_closes_now"]["precision_row_replacement_cutset_locked"] is True, "precision cutset not locked")
    require(data["what_closes_now"]["qasu3_slot_support_diagnostics_built"] is True, "slot diagnostics not built")
    require(data["what_remains_open"]["accepted_external_precision_profile_packet"] is True, "precision packet gate missing")
    require(data["what_remains_open"]["selected_operator_slot_source_values"] is True, "slot values gate missing")
    require("zero accepted precision rows" in note, "note missing precision zero guard")
    require("zero selected operator slot source values" in note, "note missing slot zero guard")

    for packet in [data, edge_a, edge_b, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
