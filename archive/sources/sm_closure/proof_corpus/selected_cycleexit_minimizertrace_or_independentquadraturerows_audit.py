"""Audit cycle-exit minimizer-trace / independent quadrature rows gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_cycleexit_minimizertrace_or_independentquadraturerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_minimizer_trace_payload_status.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_quadrature_rows_status.packet.json"
EXIT = PACKET_DIR / "reduced_cycle_exit_obligation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CycleExit_MinimizerTrace_or_IndependentQuadratureRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_CYCLEEXIT_MINIMIZERTRACE_OR_INDEPENDENTQUADRATUREROWS_REDUCED_FIRSTVARIATION_OR_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_FirstVariationBoundary_or_PrimitiveQuadratureRows_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    exit_packet = load(EXIT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(route_a["status"] == "ROUTE_A_PREREQUISITES_PARTIAL_FIRSTVARIATION_OPEN", "route A status mismatch")
    prereqs = route_a["prerequisites_closed"]
    for key in [
        "I1_stationary_trace_map_values",
        "I5_selected_dotD_C1_response_source",
        "formal_C1_defect_functional_source",
        "dynamic_dotD_trace_binding",
    ]:
        require(prereqs[key] is True, f"route A prereq missing: {key}")
    for key in [
        "I1_full_dynamic_minimizer_to_PhiFin_trace",
        "I10_physical_PhiFinC1_minimizes_defect_functional",
        "I11_first_variation_identity",
        "I11_boundary_cancellation_for_selected_trace",
    ]:
        require(route_a["open_physical_payloads"][key] is True, f"route A open missing: {key}")
    require(route_a["can_close_cycle_exit_now"] is False, "route A overclosed")

    require(route_b["status"] == "ROUTE_B_BASIS_READY_PRIMITIVE_AND_INDEPENDENT_HESSIAN_OPEN", "route B status mismatch")
    require(route_b["stage_counts"]["basis"] == 19, "basis count mismatch")
    require(route_b["stage_counts"]["primitive_contractions"] == 72, "primitive count mismatch")
    require(route_b["stage_counts"]["hessian_source"] == 2, "hessian count mismatch")
    require(route_b["stage_counts"]["sector_matrices"] == 36, "sector count mismatch")
    b_prereqs = route_b["prerequisites_closed_or_open"]
    require(b_prereqs["basis_rows_selected"] is True, "basis not selected")
    require(b_prereqs["dynamic_dotD_trace_binding"] is True, "dynamic trace not bound")
    require(b_prereqs["primitive_rows_executed"] == 0, "primitive rows overexecuted")
    require(b_prereqs["independent_hessian_b_selected_emitted"] is False, "independent Hessian overclaimed")
    require(route_b["open_independent_outputs"]["primitive_contraction_rows"] == 72, "open primitive count mismatch")
    require(route_b["can_close_cycle_exit_now"] is False, "route B overclosed")

    require(exit_packet["status"] == "REDUCED_TO_FIRSTVARIATION_OR_PRIMITIVE_ROWS", "exit status mismatch")
    closed = exit_packet["closed_inside_cycle_exit_attempt"]
    for key in [
        "stationary_trace_map_values",
        "selected_dotD_alpha1_C1_response_source",
        "formal_C1_defect_functional_source",
        "selected_basis_projector_gram_gap_rows",
        "dynamic_dotD_trace_binding",
        "locked_target_linear_algebra",
    ]:
        require(closed[key] is True, f"closed prereq missing: {key}")
    require(exit_packet["locked_target"]["A_transpose_b"] == [12.0, 12.0], "locked b mismatch")
    require(exit_packet["locked_target"]["deltaTheta_C1"] == [1.0, 1.0], "locked delta mismatch")
    require(exit_packet["superset_strategy"]["using_combined_paths"] is True, "superset strategy missing")
    require("unpatched dynamic packet closure" in exit_packet["not_claimed"], "guardrail missing")

    for key in [
        "cycle_exit_prerequisites_audited",
        "I1_stationary_trace_component_available",
        "I5_dotD_alpha1_C1_source_component_available",
        "route_B_basis_stage_available",
        "shared_exit_reduced_to_two_minimal_payloads",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "I1_full_dynamic_minimizer_to_PhiFin_trace",
        "I10_physical_PhiFinC1_minimizes_defect_functional",
        "I11_first_variation_boundary_cancellation",
        "primitive_quadrature_rows_executed",
        "independent_b_selected",
        "sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("Remaining exit" in note and "Route A" in note and "Route B" in note, "note missing route summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
