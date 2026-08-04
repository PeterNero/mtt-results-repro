"""Audit selected trace-map/basis values or primitive rows execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tracemapandbasisvalues_or_primitiverowsexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_FILL = PACKET_DIR / "route_a_trace_map_value_fill.packet.json"
BASIS_FILL = PACKET_DIR / "route_b_selected_basis_value_fill.packet.json"
PRIMITIVE_PLAN = PACKET_DIR / "primitive_rows_execution_ready.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TRACEMAP_AND_BASIS_VALUES_FILLED_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    trace = load(TRACE_FILL)
    basis = load(BASIS_FILL)
    primitive = load(PRIMITIVE_PLAN)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    flags = trace["filled_flags"]
    require(flags["selected_trace_map_values"] is True, "trace map not filled")
    require(flags["selected_source_verified_for_functional_End0_trace"] is True, "trace source not verified")
    require(flags["selected_projector_source_verified"] is True, "projector source not verified")
    require(flags["transport_closed_finite_validator_replay"] is True, "transport validator not closed")
    require(trace["accepted_for_stationary_trace"] is True, "stationary trace not accepted")
    require(trace["accepted_for_dynamic_C1_primitive_rows"] is False, "dynamic primitive trace overaccepted")
    require(trace["remaining_dynamic_flags"]["selected_dotD_source_verified"] is False, "dotD oververified")
    require(trace["remaining_dynamic_flags"]["alpha1_driver_verified"] is False, "alpha1 oververified")

    require(basis["row_count"] == 19, "basis row count mismatch")
    require(basis["selected_row_count"] == 19, "selected basis row count mismatch")
    require(basis["all_basis_rows_selected"] is True, "not all basis rows selected")
    require(basis["accepted_for_basis_stage"] is True, "basis stage not accepted")
    for row in basis["basis_rows"]:
        require(row["selected_now"] is True, f"basis row not selected: {row['basis_id']}")
        require(row["selected_basis_value"] is not None, f"basis value missing: {row['basis_id']}")
        require(row["selected_projector_value"] is not None, f"projector value missing: {row['basis_id']}")
        require(row["gram_matrix"] == "identity_preserved_by_unitary_transport", f"Gram mismatch: {row['basis_id']}")
        require(row["gap_preserved"] is True, f"gap not preserved: {row['basis_id']}")
        require(row["source_verified_by_transport_conjugation"] is True, f"source not verified: {row['basis_id']}")

    require(primitive["basis_stage_accepted"] is True, "primitive basis precondition missing")
    require(primitive["primitive_row_count"] == 72, "primitive row count mismatch")
    require(primitive["can_execute_rows_now"] is False, "primitive rows executed too early")
    require("dynamic dotD trace binding" in " ".join(primitive["why_not"]), "dynamic binding blocker missing")

    for key in [
        "selected_trace_map_values_functional_stationary",
        "selected_basis_projector_gram_gap_values_stationary",
        "basis_stage_can_advance",
        "primitive_row_ids_locked",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_first_variation_identity",
        "boundary_cancellation_for_dynamic_C1_trace",
        "selected_dynamic_dotD_trace_binding",
        "primitive_quadrature_rows",
        "hessian_source_rows",
        "sector_matrix_rows",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    require(decision["route_A_trace_map_values_accepted"] is True, "route A trace not accepted")
    require(decision["route_B_basis_rows_accepted"] is True, "route B basis not accepted")
    require(decision["route_B_can_advance_to_primitive_rows_after_dynamic_binding"] is True, "primitive advance flag missing")
    for key in [
        "primitive_rows_executed",
        "I10_proved",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "promotion theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("stationary selected trace-map values" in note and "primitive row ids locked" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
