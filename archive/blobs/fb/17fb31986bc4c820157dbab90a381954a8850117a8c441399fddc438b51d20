"""Audit Step 10 loop collapse to the finite-C1 source identity wall."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step10_finitec1sourceidentity_singlewall_or_newrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LOOP_COLLAPSE = PACKET_DIR / "step10_loop_collapse.packet.json"
SINGLE_WALL = PACKET_DIR / "step10_single_source_identity_wall.packet.json"
ROW_EXECUTION_DIAGNOSIS = PACKET_DIR / "step10_row_execution_diagnosis.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step10_to_step11_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step10_FiniteC1SourceIdentity_SingleWall_or_NewRows_v1.md"

STATUS = (
    "MTT_SELECTED_STEP10_FINITEC1SOURCEIDENTITY_SINGLEWALL_OR_NEWROWS_"
    "CLOSED_LOOP_COLLAPSE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_Step11_SelectedFiniteC1SourceIdentityTheorem_ClauseProof_v1"


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
    loop = load(LOOP_COLLAPSE)
    wall = load(SINGLE_WALL)
    rows = load(ROW_EXECUTION_DIAGNOSIS)
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
    guard(loop, errors, "loop collapse", closure=True)
    guard(wall, errors, "single wall", closure=True)
    guard(rows, errors, "row diagnosis", closure=True)
    guard(workorder, errors, "workorder", closure=False)

    expect(loop.get("step9_closed_for_plan_contract") is True, "Step 9 not imported closed", errors)
    expect(loop.get("old_wording_retired", {}).get("selected_physical_PhiFinC1_source_rule_or_independent_Galerkin_rows") is True, "old wording not retired", errors)
    expect(loop.get("route_A_accepts_now") is False, "Route A overaccepted", errors)
    expect(loop.get("route_B_accepts_now") is False, "Route B overaccepted", errors)
    expect(loop.get("both_routes_reduce_to_shared_theorem") is True, "routes not collapsed", errors)
    expect(loop.get("shared_theorem_name") == "SelectedFiniteC1SourceIdentityTheorem", "wrong shared theorem", errors)
    expect(loop.get("new_independent_rows_are_the_only_escape_hatch") is True, "new-row escape not recorded", errors)

    expect(wall.get("theorem_to_prove") == "SelectedFiniteC1SourceIdentityTheorem", "wall theorem mismatch", errors)
    expect(wall.get("proved_now") is False, "wall theorem overproved", errors)
    clauses = wall.get("minimal_clause_set", {})
    for key in [
        "C1_action_restricts_to_finite_trace_measure",
        "zero_extra_boundary_or_source_terms",
        "selected_phase_shift_variation_operators_before_residual_projection",
        "selected_basis_feeds_72_row_functions",
        "row_formula_source_theorem_derived",
        "selected_hessian_counterterm_and_b_source",
        "residual_projector_replay_not_used_as_source",
    ]:
        expect(clauses.get(key) is True, f"minimal clause missing: {key}", errors)
    for key in [
        "formal_110_row_values",
        "canonical_residual_projector",
        "finite_trace_boundary_cancellation",
        "conditional_local_principle_patch",
        "selected_source_map_candidate",
    ]:
        expect(wall.get("already_supports_but_not_proves", {}).get(key) is True, f"support boundary missing: {key}", errors)

    expect(rows.get("strict_rows_required") == 110, "strict row count mismatch", errors)
    expect(rows.get("formal_110_layer_available") is True, "formal 110 layer not available", errors)
    expect(rows.get("row_counts", {}).get("primitive_rows") == 72, "primitive row count mismatch", errors)
    expect(rows.get("row_counts", {}).get("hessian_source_rows") == 2, "hessian row count mismatch", errors)
    expect(rows.get("row_counts", {}).get("sector_rows") == 36, "sector row count mismatch", errors)
    expect(rows.get("row_counts", {}).get("total_rows") == 110, "total row count mismatch", errors)
    for key in [
        "finite_weyl_trace_rule_feeds_all_rows",
        "hessian_source_rows_assembled_from_same_rows",
        "no_locked_target_values_used_as_source",
        "sector_rows_assembled_from_primitive_rows",
    ]:
        expect(rows.get("closed_fields_in_attempt", {}).get(key) is True, f"closed row field missing: {key}", errors)
    for key in [
        "selected_basis_feeds_72_primitive_rows",
        "no_residual_projector_replay_used_as_source",
        "row_formula_source_theorem_derived",
        "source_independent_of_residual_projector_replay",
    ]:
        expect(rows.get("open_fields_in_attempt", {}).get(key) is False, f"open row field mismatch: {key}", errors)
    expect(
        rows.get("source_lineage_is_the_only_route_B_reason_after_prior_closures") is True,
        "Route B source-lineage reduction missing",
        errors,
    )
    expect(
        rows.get("do_not_repeat_full_110_row_value_fill_until_source_lineage_changes") is True,
        "anti-repeat guard missing",
        errors,
    )

    expect(workorder.get("completed_step") == 10, "workorder completed step mismatch", errors)
    expect(workorder.get("next_step") == 11, "workorder next step mismatch", errors)
    expect(workorder.get("next_required_artifact") == NEXT, "workorder next mismatch", errors)
    for key in [
        "restate_route_A_or_route_B_without_new_clause_status",
        "rerun_formal_110_row_replay_without_source_lineage_change",
        "promote_residual_projector_replay_as_independent_source",
        "use_observed_SM_values_as_selectors",
    ]:
        expect(workorder.get("forbidden_next_moves", {}).get(key) is True, f"forbidden move missing: {key}", errors)
    expect(len(workorder.get("step11_first_clause_attack_order", [])) == 7, "clause attack count mismatch", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(workorder.get("must_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step10_closed_for_plan_contract") is True, "candidate Step 10 closure missing", errors)
    expect(decision.get("route_duplication_collapsed") is True, "candidate loop collapse missing", errors)
    expect(decision.get("single_source_identity_wall_identified") is True, "candidate single wall missing", errors)
    for key in [
        "route_A_accepts_now",
        "route_B_accepts_now",
        "SelectedFiniteC1SourceIdentityTheorem_proved",
        "new_independent_110_row_source_export_emitted",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(data.get("step10_contract_closure_claimed") is True, "candidate local Step 10 claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM overclaim", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob overclaim", errors)

    expect(cert.get("route_duplication_collapsed") is True, "certificate loop collapse missing", errors)
    expect(cert.get("single_source_identity_wall_identified") is True, "certificate single wall missing", errors)
    for key in [
        "SelectedFiniteC1SourceIdentityTheorem_proved",
        "new_independent_110_row_source_export_emitted",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
    ]:
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("This resolves the looping language." in note, "note missing loop resolution", errors)
    expect("SelectedFiniteC1SourceIdentityTheorem" in note, "note missing theorem name", errors)
    expect("Step 11 must be a clause proof" in note, "note missing clause-proof guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 10 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 10 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
