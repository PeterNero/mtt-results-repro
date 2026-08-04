"""Audit Step 11 selected finite-C1 source identity clause proof ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step11_selectedfinitec1sourceidentity_clauseproof"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PLAN_POSITION = PACKET_DIR / "step11_plan_position.packet.json"
FIRST_THREE = PACKET_DIR / "step11_first_three_clause_attack.packet.json"
FULL_CLAUSE_MAP = PACKET_DIR / "step11_full_clause_status_map.packet.json"
OVERCLAIM_RECONCILIATION = PACKET_DIR / "step11_historical_overclaim_reconciliation.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step11_to_step12_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step11_SelectedFiniteC1SourceIdentityTheorem_ClauseProof_v1.md"

STATUS = (
    "MTT_SELECTED_STEP11_SELECTEDFINITEC1SOURCEIDENTITY_CLAUSEPROOF_"
    "CLOSED_STATUS_LEDGER_SOURCEOWNERSHIP_OPEN"
)
NEXT = "MTT_Selected_Step12_PreResidualSourceOwnershipClauseProof_or_NewRowSourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    plan = load(PLAN_POSITION)
    first_three = load(FIRST_THREE)
    clause_map = load(FULL_CLAUSE_MAP)
    overclaim = load(OVERCLAIM_RECONCILIATION)
    workorder = load(NEXT_WORKORDER)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(plan, errors, "plan", closure=True)
    guard(first_three, errors, "first three", closure=True)
    guard(clause_map, errors, "clause map", closure=True)
    guard(overclaim, errors, "overclaim reconciliation", closure=True)
    guard(workorder, errors, "workorder", closure=False)

    expect(plan.get("active_step") == 11, "active step mismatch", errors)
    expect(plan.get("active_object") == "SelectedFiniteC1SourceIdentityTheorem", "active object mismatch", errors)
    expect(plan.get("step11_role") == "clause proof/status ledger, not route restatement", "role mismatch", errors)
    for key in [
        "step4_dynamic_physical_matrices_and_admitted_rows",
        "step5_no_knob_minimal_knob_audit",
        "step6_measured_sm_comparison_readiness",
        "step7_common_rg_covariance_observable_suite",
        "step8_precision_route_and_operator_source_slots",
        "step9_dynamic_qasu3_c1_frontier_reduction",
        "step10_route_duplication_collapse",
    ]:
        expect(key in plan.get("closed_plan_steps", {}), f"plan status missing: {key}", errors)

    clauses = first_three.get("clauses", {})
    phase = clauses.get("selected_phase_shift_variation_operators_before_residual_projection", {})
    basis = clauses.get("selected_basis_feeds_72_row_functions", {})
    row_formula = clauses.get("row_formula_source_theorem_derived", {})
    expect(phase.get("shape_and_72_slot_routing_closed") is True, "phase/shift routing not closed", errors)
    expect(phase.get("operator_shapes_selected_as_physical_source") is False, "operator source overclosed", errors)
    expect(phase.get("source_map_selected_by_MTT_now") is False, "source map overselected", errors)
    expect(phase.get("full_clause_proved") is False, "phase/shift clause overproved", errors)
    expect(basis.get("slot_typing_closed_for_all_72_rows") is True, "basis slot typing not closed", errors)
    expect(
        basis.get("selected_basis_independent_of_residual_projector") is True,
        "basis independence missing",
        errors,
    )
    expect(
        basis.get("all_sector_sources_verified_by_transport_conjugation") is True,
        "transport conjugation basis support missing",
        errors,
    )
    expect(
        basis.get("source_independent_of_residual_projector_replay") is False,
        "row source independence overclosed",
        errors,
    )
    expect(basis.get("full_clause_proved") is False, "basis clause overproved", errors)
    expect(row_formula.get("all_72_row_values_exact") is True, "72 exact values missing", errors)
    expect(row_formula.get("all_72_row_count") == 72, "72 row count mismatch", errors)
    expect(
        row_formula.get("provenance_independent_of_residual_projector_replay_for_all_rows") is False,
        "row provenance overclosed",
        errors,
    )
    expect(row_formula.get("new_independent_row_packet_emitted") is False, "new row packet overemitted", errors)
    expect(row_formula.get("full_clause_proved") is False, "row formula theorem overproved", errors)
    expect(first_three.get("first_three_clause_attack_completed") is True, "first three attack not completed", errors)
    expect(first_three.get("first_three_all_values_or_routing_closed") is True, "first three support not closed", errors)
    expect(first_three.get("first_three_source_ownership_closed") is False, "source ownership overclosed", errors)

    statuses = clause_map.get("clause_status", {})
    expect(
        statuses.get("selected_phase_shift_variation_operators_before_residual_projection")
        == "PARTIAL_ROUTING_CLOSED_SOURCE_SELECTION_OPEN",
        "phase/shift status mismatch",
        errors,
    )
    expect(
        statuses.get("selected_basis_feeds_72_row_functions")
        == "PARTIAL_SLOT_TYPING_AND_BASIS_INDEPENDENCE_CLOSED_ROW_SOURCE_OPEN",
        "basis status mismatch",
        errors,
    )
    expect(
        statuses.get("row_formula_source_theorem_derived")
        == "PARTIAL_72_EXACT_VALUES_CLOSED_SOURCE_THEOREM_OPEN",
        "row formula status mismatch",
        errors,
    )
    expect(clause_map.get("trace_assembly_subclause_closed") is True, "trace assembly not closed", errors)
    expect(clause_map.get("source_identity_theorem_proved_now") is False, "theorem overproved", errors)
    expect(
        clause_map.get("new_independent_110_row_source_export_emitted") is False,
        "new 110-row export overemitted",
        errors,
    )

    expect(
        overclaim.get("historical_claims", {}).get("source_replay_SelectedFiniteC1SourceIdentityTheorem_promoted")
        is True,
        "historical source-stack claim not detected",
        errors,
    )
    expect(
        overclaim.get("reason_not_imported_as_step11_theorem", {}).get(
            "depends_on_premise_free_symbolic_transport_certificate"
        )
        is True,
        "premise-free dependency not detected",
        errors,
    )
    expect(
        overclaim.get("reason_not_imported_as_step11_theorem", {}).get("raw_27mode_finite_replay_closed")
        is False,
        "raw 27-mode guard mismatch",
        errors,
    )
    expect(overclaim.get("accepted_use_in_step11") == "support/postcheck only", "overclaim not quarantined", errors)
    expect(
        overclaim.get("source_identity_theorem_proved_by_historical_claims_now") is False,
        "historical claims overpromoted",
        errors,
    )

    expect(workorder.get("completed_step") == 11, "workorder completed step mismatch", errors)
    expect(workorder.get("next_step") == 12, "workorder next step mismatch", errors)
    expect(workorder.get("next_required_artifact") == NEXT, "workorder next mismatch", errors)
    for key in [
        "repeat_exact_72_values_without_new_source_owner",
        "import_premise_free_symbolic_source_stack_as_final_theorem",
        "promote_shape_routing_as_source_selection",
        "use_observed_SM_values_as_selectors",
    ]:
        expect(workorder.get("forbidden_next_moves", {}).get(key) is True, f"forbidden move missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(workorder.get("must_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    for key in [
        "step11_closed_for_plan_contract",
        "first_three_clause_attack_completed",
        "phase_shift_72_slot_routing_closed",
        "selected_basis_slot_typing_closed",
        "all_72_exact_values_closed",
        "finite_trace_assembly_subclause_closed",
    ]:
        expect(decision.get(key) is True, f"candidate closed field missing: {key}", errors)
    for key in [
        "pre_residual_RZ_RX_source_ownership_closed",
        "row_formula_source_theorem_derived",
        "SelectedFiniteC1SourceIdentityTheorem_proved",
        "new_independent_110_row_source_export_emitted",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(data.get("step11_contract_closure_claimed") is True, "candidate Step 11 claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM overclaim", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob overclaim", errors)

    expect(cert.get("first_three_clause_attack_completed") is True, "certificate first three missing", errors)
    expect(cert.get("pre_residual_RZ_RX_source_ownership_closed") is False, "certificate source ownership overclosed", errors)
    expect(cert.get("SelectedFiniteC1SourceIdentityTheorem_proved") is False, "certificate theorem overproved", errors)
    expect(cert.get("new_independent_110_row_source_export_emitted") is False, "certificate new rows overemitted", errors)

    expect("Step 11   : current clause-proof/status ledger" in note, "note missing plan position", errors)
    expect("pre-residual R_Z/R_X source ownership       : false" in note, "note missing source ownership guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 11 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 11 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
