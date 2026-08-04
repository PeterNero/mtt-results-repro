"""Audit primitive rows execution / dynamic dotD trace binding gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DYNAMIC_BINDING = PACKET_DIR / "dynamic_dotd_trace_binding.packet.json"
PRIMITIVE_RUN = PACKET_DIR / "primitive_rows_execution_attempt.packet.json"
NEXT_CUTSET = PACKET_DIR / "residual_completion_or_honest_galerkin_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    binding = load(DYNAMIC_BINDING)
    primitive = load(PRIMITIVE_RUN)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    flags = binding["binding_flags"]
    require(flags["stationary_trace_map_values_accepted"] is True, "stationary trace not accepted")
    require(flags["selected_dotD_source_verified"] is True, "dotD source not verified")
    require(flags["alpha1_driver_verified"] is True, "alpha1 driver not verified")
    require(flags["honest_dotD_alpha1_replay"] is True, "honest dotD replay not imported")
    require(flags["dU_dalpha_formula_closed"] is True, "transport derivative not closed")
    require(flags["dynamic_dotD_trace_binding_accepted"] is True, "dynamic binding not accepted")
    require("A_selected" in binding["not_accepted_scope"], "A_selected guardrail missing")
    require(binding["observed_data_used"] is False and binding["target_fitting_used"] is False, "binding data guardrail violated")

    require(primitive["basis_stage_accepted"] is True, "basis stage not accepted")
    require(primitive["dynamic_trace_binding_accepted"] is True, "dynamic trace not accepted for primitive attempt")
    require(primitive["row_count"] == 72, "primitive row count mismatch")
    require(primitive["executed_row_count"] == 0, "primitive rows overexecuted")
    require(primitive["primitive_rows_executed"] is False, "primitive rows overpromoted")
    require(primitive["span_obstruction_summary"]["pure_fixed_fiber_span_can_close"] is False, "span obstruction missing")
    for row in primitive["rows"]:
        require(row["basis_stage_accepted"] is True, f"row basis missing: {row['row_id']}")
        require(row["dynamic_trace_binding_accepted"] is True, f"row dynamic binding missing: {row['row_id']}")
        require(row["executed_now"] is False, f"row overexecuted: {row['row_id']}")

    require(cutset["status"] == "NEXT_CUTSET_SELECTED", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "recommended next mismatch")
    require("residual-completion" in cutset["recommended_next"]["reason"], "residual completion reason missing")
    require(cutset["recommended_next"]["locked_conditional_target"]["deltaTheta_C1"] == [1.0, 1.0], "locked target mismatch")

    for key in [
        "dynamic_dotD_trace_binding",
        "alpha1_driver_verified_for_this_frontier",
        "selected_dotD_source_verified_for_this_frontier",
        "primitive_rows_attempted_against_selected_basis_and_dynamic_trace",
        "residual_completion_cutset_selected",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "primitive_quadrature_rows_executed",
        "selected_residual_completion_source_theorem",
        "honest_Galerkin_C1_contractions",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "hessian_source_rows",
        "sector_matrix_rows",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    require(decision["dynamic_dotD_trace_binding_accepted"] is True, "dynamic binding decision missing")
    for key in [
        "primitive_rows_executed",
        "residual_completion_promoted",
        "honest_Galerkin_C1_emission_promoted",
        "I10_proved",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("dynamic dotD / Phi_fin^C1 trace binding" in note and "primitive rows executed                 = 0" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
