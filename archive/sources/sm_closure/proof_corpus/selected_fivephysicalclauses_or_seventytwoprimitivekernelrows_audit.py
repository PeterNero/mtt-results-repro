"""Audit the final dynamic-C1 execution checklist."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PHYSICAL = PACKET_DIR / "five_physical_clause_execution_checklist.packet.json"
ROWS = PACKET_DIR / "seventy_two_primitive_kernel_row_checklist.packet.json"
PRIORITY = PACKET_DIR / "path_priority_and_blocker_minimization.packet.json"
DECISION = PACKET_DIR / "final_execution_readiness_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FivePhysicalClauses_or_SeventyTwoPrimitiveKernelRows_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_fivephysicalclauses_or_seventytwoprimitivekernelrows.py"

STATUS = "MTT_SELECTED_FIVEPHYSICALCLAUSES_OR_SEVENTYTWOPRIMITIVEKERNELROWS_BUILT_EXECUTION_CHECKLIST_OPEN"
NEXT = "MTT_Selected_PhysicalRZRXBSourceEmission_or_PrimitiveKernelRowFirstExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    physical = load(PHYSICAL)
    rows = load(ROWS)
    priority = load(PRIORITY)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("execution slots" in note, "note does not state execution slot purpose")

    require(physical["status"] == "FIVE_PHYSICAL_CLAUSES_READY_AS_EXECUTION_SLOTS_OPEN", "physical status mismatch")
    require(physical["clause_count"] == 5, "physical clause count mismatch")
    require(physical["closed_clause_count"] == 0, "physical overclosed")
    require(physical["open_clause_count"] == 5, "physical open count mismatch")
    require(physical["route_closed_now"] is False, "physical route overclosed")
    for name, clause in physical["clauses"].items():
        require(clause["closed"] is False, f"physical clause overclosed: {name}")
        require(clause["emission_slot"] == name, f"emission slot mismatch: {name}")
        require(clause["source_required"], f"source requirement missing: {name}")
        require(clause["acceptance_test"], f"acceptance test missing: {name}")
        require(all(clause["current_support"].values()), f"closed support not imported for {name}")

    require(rows["status"] == "SEVENTY_TWO_PRIMITIVE_KERNEL_ROWS_READY_AS_EXECUTION_SLOTS_OPEN", "row status mismatch")
    require(rows["row_count"] == 72, "row count mismatch")
    require(rows["executed_row_count"] == 0, "row overexecution")
    require(rows["open_row_count"] == 72, "open row count mismatch")
    require(rows["route_closed_now"] is False, "row route overclosed")
    require(rows["replay_rows_allowed_as_acceptance_oracle_only"] is True, "replay oracle guard missing")
    require(rows["sector_counts"] == {"d": 18, "e": 18, "nuD": 18, "u": 18}, "sector counts mismatch")
    require(rows["response_counts"] == {"phase": 36, "shift": 36}, "response counts mismatch")
    require(len(rows["coordinate_counts"]) == 9, "coordinate basis mismatch")
    require(all(count == 8 for count in rows["coordinate_counts"].values()), "coordinate count mismatch")
    for row in rows["rows"]:
        require(row["executed"] is False, f"row overexecuted: {row['row_id']}")
        require(row["sector"] in {"u", "e", "d", "nuD"}, f"bad sector: {row['row_id']}")
        require(row["response"] in {"phase", "shift"}, f"bad response: {row['row_id']}")
        require(0 <= row["matrix_coordinate"]["row"] <= 2, f"bad matrix row: {row['row_id']}")
        require(0 <= row["matrix_coordinate"]["column"] <= 2, f"bad matrix column: {row['row_id']}")
        require(row["selected_primitive_kernel_formula"] is None, f"kernel formula unexpectedly filled: {row['row_id']}")
        require(row["computed_complex_entry_value"] is None, f"row value unexpectedly filled: {row['row_id']}")
        require(row["provenance_independent_of_residual_projector_replay"] is False, f"row provenance overclosed: {row['row_id']}")

    require(priority["status"] == "TWO_ROUTES_MINIMIZED_NEITHER_PROMOTED", "priority status mismatch")
    require(all(priority["support_already_closed"].values()), "priority support missing")
    require(all(priority["kernel_support_already_closed"].values()), "kernel support missing")
    require(priority["route_a"]["remaining_objects"] == 5, "Route A remaining mismatch")
    require(priority["route_b"]["remaining_objects"] == 72, "Route B remaining mismatch")
    require(priority["no_route_closes_now"] is True, "priority overclosed a route")
    require("superset" in priority["route_b"]["straight_or_superset"], "Route B superset discipline missing")

    require(decision["status"] == "EXECUTION_CHECKLIST_BUILT_CLOSURE_NOT_CLAIMED", "decision status mismatch")
    require(decision["route_a_slots_ready"] is True, "Route A slots not ready")
    require(decision["route_b_slots_ready"] is True, "Route B slots not ready")
    require(decision["route_a_closed_now"] is False, "Route A overclosed")
    require(decision["route_b_closed_now"] is False, "Route B overclosed")
    require(decision["all_72_rows_executed"] is False, "72-row execution overclaimed")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["next_actionable_target"] == NEXT, "candidate next target mismatch")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "candidate dynamic C1 overclosed")

    for label, payload in [
        ("candidate", data),
        ("physical", physical),
        ("rows", rows),
        ("priority", priority),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
