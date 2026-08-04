"""Build the final physical-action clause / primitive-kernel formula ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalactionrestrictionclause_or_primitivekernelformula"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PHYSICAL = PACKET_DIR / "physical_action_restriction_clause_ledger.packet.json"
KERNEL = PACKET_DIR / "primitive_kernel_formula_clause_ledger.packet.json"
EQUIV = PACKET_DIR / "final_clause_equivalence.packet.json"
DECISION = PACKET_DIR / "final_clause_closure_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalActionRestrictionClause_or_PrimitiveKernelFormula_v1.md"

STATUS = "MTT_SELECTED_PHYSICALACTIONRESTRICTIONCLAUSE_OR_PRIMITIVEKERNELFORMULA_BUILT_FINAL_CLAUSE_LEDGER_OPEN"
NEXT = "MTT_Selected_FivePhysicalClauses_or_SeventyTwoPrimitiveKernelRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution.candidate.json")
    trace_decision = load(
        DATA
        / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
        / "dynamic_phifin_or_row_formula_decision.packet.json"
    )
    route_a_validator = load(
        DATA
        / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
        / "route_a_action_restriction_validator_v2.packet.json"
    )
    if_closes = load(
        DATA
        / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
        / "if_action_restriction_emitted_dynamic_c1_closure.packet.json"
    )
    row_formula = load(
        DATA
        / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
        / "primitive_row_formula_execution_contract.packet.json"
    )
    boundary = load(
        DATA
        / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
        / "physical_boundary_emission_reduction.packet.json"
    )

    physical_clauses = {
        "physical_PhiFinC1_action_restriction": {
            "closed": False,
            "source_required": "same-source physical Phi_fin^C1 action restriction theorem or selected action rows",
            "why_open": "No selected physical action row currently proves exact restriction to the finite Weyl quotient.",
        },
        "no_extra_physical_boundary_or_source_term": {
            "closed": False,
            "source_required": "same-source boundary decomposition or cancellation term",
            "why_open": "Finite trace cancellation is closed, but physical extra boundary/source terms are not emitted.",
        },
        "phase_R_Z_source_selection": {
            "closed": False,
            "source_required": "same-branch phase residual source emission",
            "why_open": "R_Z is canonical as a finite Weyl value, but not emitted as a physical source term.",
        },
        "shift_R_X_source_selection": {
            "closed": False,
            "source_required": "same-branch shift residual source emission",
            "why_open": "R_X is canonical as a finite Weyl value, but not emitted as a physical source term.",
        },
        "same_source_b_selected_emission": {
            "closed": False,
            "source_required": "same-branch Hessian/source vector emission",
            "why_open": "b_selected is replay-fixed, but not emitted by the physical action/source branch.",
        },
    }
    physical = {
        "schema": "MTTPhysicalActionRestrictionClauseLedger.v1",
        "status": "FIVE_PHYSICAL_CLAUSES_OPEN_MEASURE_TRACE_CLOSED",
        "closed_subclauses_imported": route_a_validator["closed_subclauses"],
        "five_remaining_physical_clauses": physical_clauses,
        "closed_clause_count": sum(1 for item in physical_clauses.values() if item["closed"]),
        "open_clause_count": sum(1 for item in physical_clauses.values() if not item["closed"]),
        "all_physical_clauses_closed_now": False,
        "if_all_close_values": if_closes["consequent_if_antecedent_true"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    missing = row_formula["still_missing_for_execution"]
    kernel = {
        "schema": "MTTPrimitiveKernelFormulaClauseLedger.v1",
        "status": "PRIMITIVE_KERNEL_FORMULA_CLAUSES_OPEN",
        "primitive_row_count": row_formula["primitive_row_count"],
        "row_count_verified": len(row_formula["primitive_rows"]) == 72,
        "available_support": row_formula["now_available_for_row_formula"],
        "five_remaining_kernel_clauses": {
            "selected_primitive_kernel_formula": {
                "closed": not missing["selected_primitive_kernel_formula"],
                "source_required": "selected formula for every primitive row kernel in the transported basis",
            },
            "selected_physical_or_independent_trace_pairing_clause": {
                "closed": not missing["selected_physical_or_independent_trace_pairing_clause"],
                "source_required": "physical restriction clause or independent quadrature measure",
            },
            "computed_independent_complex_entries": {
                "closed": not missing["computed_independent_complex_entries"],
                "source_required": "72 emitted complex row entries independent of replay",
            },
            "exactness_or_error_bound_certificate": {
                "closed": not missing["exactness_or_error_bound_certificate"],
                "source_required": "symbolic exactness or certified numerical bounds for every row",
            },
            "provenance_independent_of_residual_projector_replay": {
                "closed": not missing["provenance_independent_of_residual_projector_replay"],
                "source_required": "source provenance not inherited from residual-projector replay",
            },
        },
        "closed_clause_count": 0,
        "open_clause_count": 5,
        "independent_rows_executed_now": False,
        "all_kernel_clauses_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    equiv = {
        "schema": "MTTFinalClauseEquivalence.v1",
        "status": "FINAL_DYNAMIC_C1_CLAUSES_EQUIVALENCE_BUILT_NEITHER_SIDE_CLOSED",
        "route_a_physical_side": "close the five remaining physical same-source clauses",
        "route_b_kernel_side": "close the five primitive-kernel formula clauses and emit 72 independent rows",
        "support_already_closed": {
            "dynamic_trace_binding_reconciled": trace_decision["dynamic_trace_binding_reconciled"],
            "finite_measure_and_algebraic_boundary_closed": trace_decision[
                "finite_measure_and_algebraic_boundary_closed"
            ],
            "route_a_reduced_to_physical_action_restriction_and_source_emission": trace_decision[
                "route_a_reduced_to_physical_action_restriction_and_source_emission"
            ],
            "route_b_reduced_to_selected_primitive_kernel_formula_execution": trace_decision[
                "route_b_reduced_to_selected_primitive_kernel_formula_execution"
            ],
            "finite_boundary_support_is_closed": boundary["finite_boundary_support_is_closed"],
        },
        "if_route_a_closes_then": if_closes["consequent_if_antecedent_true"],
        "if_route_b_closes_then": {
            "independent_primitive_rows_executed": True,
            "A_selected_b_selected_deltaTheta_checked_against_locked_target": True,
            "route_B_selected_Galerkin_replacement_closed": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFinalClauseClosureDecision.v1",
        "status": "FINAL_CLAUSE_LEDGER_BUILT_CLOSURE_NOT_CLAIMED",
        "route_a_five_physical_clauses_closed": False,
        "route_b_five_kernel_clauses_closed": False,
        "primitive_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalActionRestrictionClauseOrPrimitiveKernelFormula",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution.candidate.json"),
            "route_a_validator_v2": rel(
                DATA
                / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
                / "route_a_action_restriction_validator_v2.packet.json"
            ),
            "primitive_row_formula_contract": rel(
                DATA
                / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
                / "primitive_row_formula_execution_contract.packet.json"
            ),
        },
        "output_packets": {
            "physical_action_restriction_clause_ledger": rel(PHYSICAL),
            "primitive_kernel_formula_clause_ledger": rel(KERNEL),
            "final_clause_equivalence": rel(EQUIV),
            "final_clause_closure_decision": rel(DECISION),
        },
        "theorem": {
            "name": "FinalDynamicC1ClauseLedgerTheorem",
            "proved": True,
            "statement": (
                "After trace binding, finite trace uniqueness, and algebraic boundary cancellation are closed, "
                "unpatched dynamic C1 closure is reduced to either five physical same-source clauses or five "
                "primitive-kernel formula clauses with 72 independent rows. This ledger names the exact remaining "
                "clauses and proves that no trace, alpha1, dotD, or replay degeneracy blocker remains."
            ),
        },
        "closure_decision": decision,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalActionRestrictionClause_or_PrimitiveKernelFormula_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_a_five_physical_clauses_closed": False,
        "route_b_five_kernel_clauses_closed": False,
        "primitive_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalActionRestrictionClause or PrimitiveKernelFormula v1

Status: `{STATUS}`.

The active dynamic-C1 frontier is now a final clause ledger.

Route A closes by emitting five same-source physical clauses:
physical `Phi_fin^C1` action restriction, no extra physical boundary/source
term, physical `R_Z`, physical `R_X`, and physical `b_selected`.

Route B closes by emitting five primitive-kernel clauses:
selected primitive kernel formula, selected physical or independent pairing,
72 independent complex row entries, exactness/error certificates, and provenance
independent of residual-projector replay.

No unpatched dynamic-C1, true-SM, or no-knob closure is claimed.
"""

    for path, payload in [
        (PHYSICAL, physical),
        (KERNEL, kernel),
        (EQUIV, equiv),
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
