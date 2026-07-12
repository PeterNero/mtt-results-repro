"""Audit differentiated-vertex / Hessian counterterm residual value packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket.candidate.json"
RESIDUAL = (
    ROOT
    / "candidate_data"
    / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
    / "differentiated_residual_completion.packet.json"
)
ACCEPTANCE = (
    ROOT
    / "candidate_data"
    / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
    / "residual_completion_acceptance_kernel.packet.json"
)
CERT = ROOT / "certificates" / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedVertex_HessianCounterterm_or_GalerkinC1_ValuePacket_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket.py"

STATUS = (
    "MTT_SELECTED_DIFFERENTIATEDVERTEX_HESSIANCOUNTERTERM_OR_GALERKINC1_VALUEPACKET_"
    "BUILT_RESIDUAL_COMPLETION_OPEN"
)
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"
TOL = 1e-9


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def near(value: float, expected: float, tol: float = TOL) -> bool:
    return abs(value - expected) <= tol


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    residual = load(RESIDUAL)
    acceptance = load(ACCEPTANCE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(residual["status"] == "ORTHOGONAL_RESIDUAL_COMPLETION_COMPUTED_SOURCE_OPEN", "residual packet status mismatch")
    require(acceptance["status"] == "ACCEPTANCE_KERNEL_EMITTED_SOURCE_OPEN", "acceptance packet status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    source = data["source_selector_state"]
    require(source["source_selector_promoted"] is True, "source selector not promoted")
    require(source["dynamic_values_promoted"] is False, "dynamic values overpromoted")
    require(source["A_selected_promoted"] is False, "A_selected overpromoted")
    require(source["b_selected_promoted"] is False, "b_selected overpromoted")

    require(residual["selected_by_MTT"] is False, "residual completion overselected")
    require(residual["observed_data_used"] is False, "observed data used")
    require(residual["target_fitting_used"] is False, "target fitting used")
    require(residual["source_selector_attached"] is True, "source selector not attached")
    require(residual["basis"]["fixed_fiber_class"] == [0, 1, 2], "fixed fiber class mismatch")
    require(residual["basis"]["active_shift"] == [1, 1], "active shift mismatch")
    require(residual["basis"]["absolute_fiber_origin_selected"] is False, "absolute fiber origin overselected")

    phase = residual["phase_I_plus_Z_completion"]
    shift = residual["shift_I_plus_X_completion"]
    require(near(phase["target"]["norm_sq"], 6.0), "phase target norm mismatch")
    require(near(shift["target"]["norm_sq"], 6.0), "shift target norm mismatch")
    require(near(phase["primitive_projection"]["norm_sq"], 2.0), "phase projection norm mismatch")
    require(near(shift["primitive_projection"]["norm_sq"], 4.0), "shift projection norm mismatch")
    require(near(phase["residual_completion"]["norm_sq"], 4.0), "phase residual norm mismatch")
    require(near(shift["residual_completion"]["norm_sq"], 2.0), "shift residual norm mismatch")
    require(phase["decomposition"]["projection_plus_residual_equals_target"] is True, "phase decomposition not exact")
    require(shift["decomposition"]["projection_plus_residual_equals_target"] is True, "shift decomposition not exact")
    require(phase["decomposition"]["closure_error_norm_sq"] <= TOL, "phase closure residual too large")
    require(shift["decomposition"]["closure_error_norm_sq"] <= TOL, "shift closure residual too large")
    require(phase["orthogonality"]["orthogonal_to_fixed_fiber_span"] is True, "phase residual not orthogonal")
    require(shift["orthogonality"]["orthogonal_to_fixed_fiber_span"] is True, "shift residual not orthogonal")

    routed = residual["routed_72_real_completion"]
    require(near(routed["phase_residual_norm_sq_two_sectors"], 8.0), "routed phase residual mismatch")
    require(near(routed["shift_residual_norm_sq_two_sectors"], 4.0), "routed shift residual mismatch")
    require(near(routed["total_residual_norm_sq_four_sectors"], 12.0), "total residual mismatch")
    require(near(routed["conditional_b_norm_sq"], 24.0), "conditional b norm mismatch")
    require(routed["if_promoted_then_remaining_linear_algebra_obstruction"] is False, "linear algebra obstruction should be removed conditionally")

    summary = data["residual_completion_summary"]
    require(near(summary["phase_residual_norm_sq_per_sector"], 4.0), "summary phase residual mismatch")
    require(near(summary["shift_residual_norm_sq_per_sector"], 2.0), "summary shift residual mismatch")
    require(near(summary["total_routed_residual_norm_sq"], 12.0), "summary routed residual mismatch")
    require(summary["phase_residual_orthogonal_to_fixed_fiber_span"] is True, "summary phase orthogonality missing")
    require(summary["shift_residual_orthogonal_to_fixed_fiber_span"] is True, "summary shift orthogonality missing")
    require(summary["exact_reconstruction_if_residual_promoted"] is True, "exact reconstruction missing")

    require(data["acceptance_kernel"] == acceptance, "embedded acceptance kernel mismatch")
    lane_a = acceptance["lane_A_residual_source_promotion"]
    for key in [
        "must_prove_same_branch_differentiated_vertex_emits_phase_residual",
        "must_prove_same_branch_differentiated_vertex_emits_shift_residual",
        "or_Hessian_counterterms_emit_same_residuals",
        "must_preserve_trace_normalization",
        "must_not_use_observed_flavor_targets",
    ]:
        require(lane_a[key] is True, f"lane A requirement missing: {key}")
    lane_b = acceptance["lane_B_honest_Galerkin_C1_emission"]
    require(lane_b["selected_source_verified_currently"] is False, "honest Galerkin oververified")
    require("linear_response_matrices" in lane_b["required_outputs"], "linear response output missing")
    after = acceptance["after_source_promotion_checks"]
    require(after["A_selected_columns_reconstruct_conditional_phase_shift_packet"] is True, "after-promotion reconstruction missing")
    require(after["A_transpose_A_expected_if_same_packet"] == [[12.0, 0.0], [0.0, 12.0]], "expected Gram mismatch")
    require(after["A_transpose_b_expected_if_same_packet"] == [12.0, 12.0], "expected A^T b mismatch")
    require(after["deltaTheta_expected_if_same_packet"] == [1.0, 1.0], "expected deltaTheta mismatch")
    require(after["rank_expected_if_same_packet"] == 2, "expected rank mismatch")
    for key, value in acceptance["promotion_guard"].items():
        require(value is False, f"promotion guard overclaimed: {key}")

    theorem = data["theorem"]
    require(theorem["proved"] is True, "theorem not proved")

    decision = data["promotion_decision"]
    require(decision["residual_completion_packet_computed"] is True, "residual packet not computed")
    require(decision["acceptance_kernel_emitted"] is True, "acceptance kernel not emitted")
    for key in [
        "selected_residual_completion_promoted",
        "selected_differentiated_vertex_promoted",
        "selected_Hessian_counterterms_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "honest_Galerkin_C1_contractions_promoted",
        "full_SM_no_knob_closure_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "exact_orthogonal_residual_completion_computed",
        "next_source_theorem_target_reduced_to_residual_completion",
        "honest_Galerkin_fallback_contract_preserved",
        "conditional_linear_algebra_after_promotion_fixed",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_residual_completion_source_theorem",
        "selected_differentiated_vertex_operator_phase_Z",
        "selected_differentiated_vertex_operator_shift_X",
        "selected_Hessian_counterterms",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "honest_Galerkin_C1_contractions",
        "full_SM_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    for key in [
        "closure_claimed",
        "observed_data_used",
        "target_fitting_used",
        "selected_residual_completion_claimed",
        "selected_differentiated_vertex_claimed",
        "selected_Hessian_counterterms_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")

    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(cert["residual_completion_packet_computed"] is True, "certificate residual flag missing")
    require("No observed masses" in note, "note missing no-observed guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
