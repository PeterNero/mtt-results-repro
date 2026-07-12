"""Audit Strominger-trace C1 first-variation / quadrature execution plan gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FIRST_VARIATION = PACKET_DIR / "route_a_first_variation_certificate_plan.packet.json"
QUADRATURE_PLAN = PACKET_DIR / "route_b_quadrature_execution_manifest.packet.json"
ROW_SCHEDULE = PACKET_DIR / "quadrature_row_schedule.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1.md"
PAPER_DRAFT = ROOT / "proof_corpus" / "paper_appendix_drafts" / "selected_source" / "theta_execution_flavor__i11_strominger_trace_c1_first_variation.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STROMINGERTRACE_C1_FIRSTVARIATION_OR_QUADRATURE_EXECUTION_PLAN_BUILT_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    first = load(FIRST_VARIATION)
    quad = load(QUADRATURE_PLAN)
    schedule = load(ROW_SCHEDULE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    draft = PAPER_DRAFT.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(first["theorem_slot"] == "I11_strominger_trace_c1_first_variation", "I11 slot mismatch")
    require(first["verified_now"] is False, "first variation oververified")
    for key in [
        "selected_trace_map",
        "first_variation_identity",
        "hessian_or_coercivity",
        "boundary_cancellation",
        "normalization_compatibility",
    ]:
        require(first["certificate_fields"][key]["required"] is True, f"first-variation field not required: {key}")
        require(first["certificate_fields"][key]["verified_now"] is False, f"first-variation field oververified: {key}")
    require(first["observed_data_used"] is False and first["target_fitting_used"] is False, "first route guardrail violated")

    rows = quad["row_requirements"]
    require(rows["zero_mode_basis_rows"]["count"] == 19, "basis row count mismatch")
    require(rows["primitive_contraction_rows"]["count"] == 72, "primitive row count mismatch")
    require(rows["hessian_source_rows"]["count"] == 2, "hessian row count mismatch")
    require(rows["sector_matrix_rows"]["count"] == 36, "sector row count mismatch")
    for row in rows.values():
        require(row["filled_now"] is False, "quadrature rows unexpectedly filled")
    require(quad["accepted_now"] is False, "quadrature overaccepted")
    require(quad["acceptance_equations"]["rank_minimum"] == 2, "rank minimum mismatch")
    require("using measured masses, mixings, or CP phase as row targets" in quad["acceptance_equations"]["forbidden_shortcuts"], "forbidden measured target missing")

    require(schedule["status"] == "ROW_SCHEDULE_BUILT_NOT_EXECUTED", "schedule status mismatch")
    require(schedule["next_executable_stage"] == "basis", "next stage mismatch")
    require(schedule["executed_now"] is False, "schedule unexpectedly executed")
    require([stage["stage"] for stage in schedule["execution_order"]] == ["basis", "primitive_contractions", "hessian_source", "sector_matrices"], "schedule order mismatch")

    for key in [
        "I11_first_variation_certificate_schema_built",
        "quadrature_execution_row_schedule_built",
        "route_A_and_route_B_next_steps_are_executable",
        "superset_strategy_locked_to_same_target",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_trace_map_values",
        "first_variation_identity_verified",
        "hessian_or_coercivity_verified",
        "boundary_cancellation_verified",
        "quadrature_rows_executed",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    for key in [
        "route_A_first_variation_certificate_accepted",
        "route_B_quadrature_execution_accepted",
        "I10_proved",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "plan theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("Theorem Slot I11" in draft, "draft missing I11")
    require("Route A now requires" in note and "Route B now has" in note, "note missing route summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
