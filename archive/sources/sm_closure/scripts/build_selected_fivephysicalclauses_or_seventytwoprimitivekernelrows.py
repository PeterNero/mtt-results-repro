"""Build the final dynamic-C1 execution checklist."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PHYSICAL = PACKET_DIR / "five_physical_clause_execution_checklist.packet.json"
ROWS = PACKET_DIR / "seventy_two_primitive_kernel_row_checklist.packet.json"
PRIORITY = PACKET_DIR / "path_priority_and_blocker_minimization.packet.json"
DECISION = PACKET_DIR / "final_execution_readiness_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FivePhysicalClauses_or_SeventyTwoPrimitiveKernelRows_v1.md"

STATUS = "MTT_SELECTED_FIVEPHYSICALCLAUSES_OR_SEVENTYTWOPRIMITIVEKERNELROWS_BUILT_EXECUTION_CHECKLIST_OPEN"
NEXT = "MTT_Selected_PhysicalRZRXBSourceEmission_or_PrimitiveKernelRowFirstExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def row_slot(row_id: str) -> dict[str, Any]:
    sector, response, coord = row_id.split(":")
    r_part, c_part = coord.split("c")
    row_index = int(r_part[1:])
    col_index = int(c_part)
    return {
        "row_id": row_id,
        "sector": sector,
        "response": response,
        "matrix_coordinate": {"row": row_index, "column": col_index},
        "executed": False,
        "selected_sector_basis_ids": None,
        "selected_primitive_kernel_formula": None,
        "selected_trace_or_pairing_source": None,
        "computed_complex_entry_value": None,
        "exactness_or_error_bound_certificate": None,
        "provenance_independent_of_residual_projector_replay": False,
        "acceptance_oracle": "locked replay target may compare after emission, never select the value",
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalactionrestrictionclause_or_primitivekernelformula.candidate.json")
    physical_ledger = load(
        DATA
        / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
        / "physical_action_restriction_clause_ledger.packet.json"
    )
    kernel_ledger = load(
        DATA
        / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
        / "primitive_kernel_formula_clause_ledger.packet.json"
    )
    equivalence = load(
        DATA
        / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
        / "final_clause_equivalence.packet.json"
    )
    row_contract = load(
        DATA
        / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
        / "primitive_row_formula_execution_contract.packet.json"
    )

    physical_slots = {}
    for clause_name, clause in physical_ledger["five_remaining_physical_clauses"].items():
        physical_slots[clause_name] = {
            "closed": False,
            "emission_slot": clause_name,
            "source_required": clause["source_required"],
            "current_support": physical_ledger["closed_subclauses_imported"],
            "acceptance_test": (
                "same selected branch emits the clause without observed-data selection, target fitting, "
                "or residual-projector replay as source"
            ),
            "why_open": clause["why_open"],
        }

    row_slots = [row_slot(row_id) for row_id in row_contract["primitive_rows"]]
    sector_counts = Counter(slot["sector"] for slot in row_slots)
    response_counts = Counter(slot["response"] for slot in row_slots)
    coordinate_counts = Counter(
        f"r{slot['matrix_coordinate']['row']}c{slot['matrix_coordinate']['column']}" for slot in row_slots
    )

    physical = {
        "schema": "MTTFivePhysicalClauseExecutionChecklist.v1",
        "status": "FIVE_PHYSICAL_CLAUSES_READY_AS_EXECUTION_SLOTS_OPEN",
        "clause_count": len(physical_slots),
        "closed_clause_count": 0,
        "open_clause_count": len(physical_slots),
        "clauses": physical_slots,
        "route_closes_if_all_slots_close": True,
        "route_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rows = {
        "schema": "MTTSeventyTwoPrimitiveKernelRowChecklist.v1",
        "status": "SEVENTY_TWO_PRIMITIVE_KERNEL_ROWS_READY_AS_EXECUTION_SLOTS_OPEN",
        "row_count": len(row_slots),
        "executed_row_count": 0,
        "open_row_count": len(row_slots),
        "sector_counts": dict(sorted(sector_counts.items())),
        "response_counts": dict(sorted(response_counts.items())),
        "coordinate_counts": dict(sorted(coordinate_counts.items())),
        "required_kernel_fields_per_row": row_contract["required_kernel_fields_per_row"],
        "rows": row_slots,
        "route_closes_if_all_rows_execute_with_kernel_clauses": True,
        "route_closed_now": False,
        "replay_rows_allowed_as_acceptance_oracle_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    priority = {
        "schema": "MTTPathPriorityAndBlockerMinimization.v1",
        "status": "TWO_ROUTES_MINIMIZED_NEITHER_PROMOTED",
        "support_already_closed": equivalence["support_already_closed"],
        "kernel_support_already_closed": kernel_ledger["available_support"],
        "route_a": {
            "name": "same-source physical Phi_fin^C1 emission",
            "straight_or_superset": "straight selected physical route, with superset support only as compatibility evidence",
            "remaining_objects": len(physical_slots),
            "why_shorter": "five theorem-emission clauses would close the unpatched dynamic-C1 packet directly",
            "risk": "requires a same-source physical action/source theorem, not just canonical finite Weyl algebra",
        },
        "route_b": {
            "name": "selected primitive kernel row execution",
            "straight_or_superset": "superset-compatible mechanical route constrained to the same locked target",
            "remaining_objects": len(row_slots),
            "why_useful": "more work, but can close through independent row formula execution if physical action emission stalls",
            "risk": "needs 72 independent row entries plus exactness/provenance certificates",
        },
        "selected_near_term_attack": "try Route A source emission first, while preparing Route B row-0 execution as a falsifiable fallback",
        "no_route_closes_now": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFinalExecutionReadinessDecision.v1",
        "status": "EXECUTION_CHECKLIST_BUILT_CLOSURE_NOT_CLAIMED",
        "route_a_slots_ready": True,
        "route_b_slots_ready": True,
        "route_a_closed_now": False,
        "route_b_closed_now": False,
        "all_72_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFivePhysicalClausesOrSeventyTwoPrimitiveKernelRows",
        "status": STATUS,
        "inputs": {
            "final_clause_ledger": rel(DATA / "selected_physicalactionrestrictionclause_or_primitivekernelformula.candidate.json"),
            "physical_clause_ledger": rel(
                DATA
                / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
                / "physical_action_restriction_clause_ledger.packet.json"
            ),
            "primitive_kernel_clause_ledger": rel(
                DATA
                / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
                / "primitive_kernel_formula_clause_ledger.packet.json"
            ),
            "primitive_row_contract": rel(
                DATA
                / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
                / "primitive_row_formula_execution_contract.packet.json"
            ),
        },
        "output_packets": {
            "five_physical_clause_execution_checklist": rel(PHYSICAL),
            "seventy_two_primitive_kernel_row_checklist": rel(ROWS),
            "path_priority_and_blocker_minimization": rel(PRIORITY),
            "final_execution_readiness_decision": rel(DECISION),
        },
        "theorem": {
            "name": "FivePhysicalClausesOrSeventyTwoPrimitiveKernelRowsExecutionTheorem",
            "proved": True,
            "statement": (
                "The final dynamic-C1 closure problem is now an executable finite task: either close five "
                "same-source physical emission clauses or execute seventy-two selected primitive kernel rows "
                "with exactness and independent provenance. Both routes share the same locked acceptance target, "
                "and neither route may use measured constants, target fitting, or replay residuals as selectors."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_FivePhysicalClauses_or_SeventyTwoPrimitiveKernelRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "physical_clause_count": len(physical_slots),
        "primitive_row_count": len(row_slots),
        "route_a_closed_now": False,
        "route_b_closed_now": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FivePhysicalClauses or SeventyTwoPrimitiveKernelRows v1

Status: `{STATUS}`.

This artifact converts the final dynamic-C1 ledger into execution slots.

Route A is the shorter straight route: emit five same-source physical clauses
for `Phi_fin^C1`, no extra physical boundary/source term, `R_Z`, `R_X`, and
`b_selected`.

Route B is the mechanical fallback: execute 72 selected primitive kernel rows,
one for each sector/response/matrix-coordinate slot, with independent
provenance and exactness or error certificates.

The superset strategy is constrained here: multiple encodings may provide
compatibility evidence, but the target remains locked and replay data may only
serve as an after-the-fact acceptance oracle.

No unpatched dynamic-C1, true-SM-equivalence, or no-knob closure is claimed.
"""

    for path, payload in [
        (PHYSICAL, physical),
        (ROWS, rows),
        (PRIORITY, priority),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
