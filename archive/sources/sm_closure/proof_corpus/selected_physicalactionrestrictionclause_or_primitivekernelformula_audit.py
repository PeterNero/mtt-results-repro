"""Audit final physical-action clause / primitive-kernel formula ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalactionrestrictionclause_or_primitivekernelformula"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PHYSICAL = PACKET_DIR / "physical_action_restriction_clause_ledger.packet.json"
KERNEL = PACKET_DIR / "primitive_kernel_formula_clause_ledger.packet.json"
EQUIV = PACKET_DIR / "final_clause_equivalence.packet.json"
DECISION = PACKET_DIR / "final_clause_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalActionRestrictionClause_or_PrimitiveKernelFormula_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_physicalactionrestrictionclause_or_primitivekernelformula.py"

STATUS = "MTT_SELECTED_PHYSICALACTIONRESTRICTIONCLAUSE_OR_PRIMITIVEKERNELFORMULA_BUILT_FINAL_CLAUSE_LEDGER_OPEN"
NEXT = "MTT_Selected_FivePhysicalClauses_or_SeventyTwoPrimitiveKernelRows_v1"


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
    kernel = load(KERNEL)
    equiv = load(EQUIV)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("final clause ledger" in note, "note misses final ledger")

    require(physical["status"] == "FIVE_PHYSICAL_CLAUSES_OPEN_MEASURE_TRACE_CLOSED", "physical status mismatch")
    require(physical["closed_clause_count"] == 0, "physical closed count mismatch")
    require(physical["open_clause_count"] == 5, "physical open count mismatch")
    require(physical["all_physical_clauses_closed_now"] is False, "physical clauses overclosed")
    for key, clause in physical["five_remaining_physical_clauses"].items():
        require(clause["closed"] is False, f"physical clause overclosed: {key}")
        require("source_required" in clause, f"physical source requirement missing: {key}")
    require(physical["closed_subclauses_imported"]["finite_measure_normalization_trace_Frobenius"] is True, "measure clause not closed")

    require(kernel["status"] == "PRIMITIVE_KERNEL_FORMULA_CLAUSES_OPEN", "kernel status mismatch")
    require(kernel["primitive_row_count"] == 72, "kernel row count mismatch")
    require(kernel["row_count_verified"] is True, "kernel row count not verified")
    require(kernel["closed_clause_count"] == 0, "kernel closed count mismatch")
    require(kernel["open_clause_count"] == 5, "kernel open count mismatch")
    require(kernel["independent_rows_executed_now"] is False, "kernel rows overexecuted")
    require(kernel["all_kernel_clauses_closed_now"] is False, "kernel clauses overclosed")
    for key, clause in kernel["five_remaining_kernel_clauses"].items():
        require(clause["closed"] is False, f"kernel clause overclosed: {key}")
        require("source_required" in clause, f"kernel source requirement missing: {key}")
    require(all(kernel["available_support"].values()), "kernel support not all closed")

    require(equiv["status"] == "FINAL_DYNAMIC_C1_CLAUSES_EQUIVALENCE_BUILT_NEITHER_SIDE_CLOSED", "equiv status mismatch")
    require(all(equiv["support_already_closed"].values()), "equiv support missing")
    require(equiv["if_route_a_closes_then"]["unpatched_SM_parity_dynamic_packet_closed"] is True, "Route A implication missing")
    require(equiv["if_route_b_closes_then"]["route_B_selected_Galerkin_replacement_closed"] is True, "Route B implication missing")

    require(decision["status"] == "FINAL_CLAUSE_LEDGER_BUILT_CLOSURE_NOT_CLAIMED", "decision status mismatch")
    require(decision["route_a_five_physical_clauses_closed"] is False, "decision Route A overclosed")
    require(decision["route_b_five_kernel_clauses_closed"] is False, "decision Route B overclosed")
    require(decision["primitive_rows_executed"] is False, "decision primitive rows overexecuted")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "decision dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM overclosed")
    require(decision["no_knob_closed"] is False, "decision no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["route_a_five_physical_clauses_closed"] is False, "candidate Route A overclosed")
    require(closure["route_b_five_kernel_clauses_closed"] is False, "candidate Route B overclosed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "candidate dynamic C1 overclosed")

    for label, payload in [
        ("candidate", data),
        ("physical", physical),
        ("kernel", kernel),
        ("equiv", equiv),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
