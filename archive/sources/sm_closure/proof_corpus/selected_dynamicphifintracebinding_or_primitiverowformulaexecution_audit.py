"""Audit dynamic Phi_fin trace-binding / primitive-row formula execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_BINDING = PACKET_DIR / "dynamic_trace_binding_reconciled.packet.json"
BOUNDARY = PACKET_DIR / "physical_boundary_emission_reduction.packet.json"
ROW_FORMULA = PACKET_DIR / "primitive_row_formula_execution_contract.packet.json"
DECISION = PACKET_DIR / "dynamic_phifin_or_row_formula_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicPhiFinTraceBinding_or_PrimitiveRowFormulaExecution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicphifintracebinding_or_primitiverowformulaexecution.py"

STATUS = "MTT_SELECTED_DYNAMICPHIFINTRACEBINDING_OR_PRIMITIVEROWFORMULAEXECUTION_BUILT_TRACE_BOUNDARY_REDUCED"
NEXT = "MTT_Selected_PhysicalActionRestrictionClause_or_PrimitiveKernelFormula_v1"


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
    trace = load(TRACE_BINDING)
    boundary = load(BOUNDARY)
    row_formula = load(ROW_FORMULA)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Trace\nnormalization and dynamic trace binding are no longer the blocker" in note, "note misses reduction")

    closed = trace["closed_support"]
    for key in [
        "dynamic_dotD_trace_binding_accepted",
        "stationary_trace_map_values_accepted",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "finite_measure_equals_normalized_trace",
        "trace_frobenius_pairing_for_finite_quotient",
        "algebraic_finite_trace_boundary_cancellation",
    ]:
        require(closed[key] is True, f"trace support missing: {key}")
    for key, value in trace["not_closed"].items():
        require(value is True, f"trace not-closed guard missing: {key}")

    require(boundary["status"] == "PHYSICAL_BOUNDARY_SOURCE_REDUCED_TO_SIX_MINIMAL_CLAUSES_OPEN", "boundary status mismatch")
    require(len(boundary["minimal_physical_clauses"]) == 6, "boundary clause count mismatch")
    require(boundary["finite_boundary_support_is_closed"] is True, "finite boundary support not closed")
    require(boundary["physical_boundary_emitted_now"] is False, "physical boundary overemitted")
    require(boundary["route_A_promoted_now"] is False, "Route A overpromoted")
    require(boundary["route_B_independent_quadrature_promoted_now"] is False, "Route B overpromoted")

    require(row_formula["status"] == "PRIMITIVE_ROW_FORMULA_CONTRACT_BUILT_FORMULA_NOT_EXECUTED", "row formula status mismatch")
    require(row_formula["primitive_row_count"] == 72, "primitive row count mismatch")
    require(len(row_formula["primitive_rows"]) == 72, "primitive rows list mismatch")
    require(all(row_formula["now_available_for_row_formula"].values()), "available row formula support missing")
    for key, value in row_formula["still_missing_for_execution"].items():
        require(value is True, f"row execution missing flag absent: {key}")
    require(row_formula["independent_rows_executed_now"] is False, "primitive rows overexecuted")
    require(row_formula["independent_rows_emitted_count"] == 0, "primitive rows overemitted")
    require(row_formula["replay_rows_allowed_as_acceptance_oracle_only"] is True, "replay guardrail missing")

    require(decision["dynamic_trace_binding_reconciled"] is True, "decision trace not reconciled")
    require(decision["finite_measure_and_algebraic_boundary_closed"] is True, "decision finite boundary not closed")
    require(decision["route_a_reduced_to_physical_action_restriction_and_source_emission"] is True, "Route A reduction missing")
    require(decision["route_b_reduced_to_selected_primitive_kernel_formula_execution"] is True, "Route B reduction missing")
    require(decision["physical_action_restriction_clause_closed"] is False, "physical action overclosed")
    require(decision["primitive_kernel_formula_executed"] is False, "primitive formula overexecuted")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["dynamic_trace_binding_reconciled"] is True, "candidate trace not reconciled")
    require(closure["finite_measure_and_algebraic_boundary_closed"] is True, "candidate finite boundary not closed")
    require(closure["physical_action_restriction_clause_closed"] is False, "candidate physical action overclosed")
    require(closure["primitive_kernel_formula_executed"] is False, "candidate primitive formula overexecuted")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "candidate dynamic C1 overclosed")

    for label, payload in [
        ("candidate", data),
        ("trace", trace),
        ("boundary", boundary),
        ("row_formula", row_formula),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
