"""Audit primitive-overlap value-emission / honest Galerkin run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"
SPAN = (
    ROOT
    / "candidate_data"
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "primitive_span_obstruction.packet.json"
)
RUN_CONTRACT = (
    ROOT
    / "candidate_data"
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)
CERT = ROOT / "certificates" / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveOverlapContractions_ValueEmission_or_HonestGalerkinRun_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.py"

STATUS = (
    "MTT_SELECTED_PRIMITIVEOVERLAPCONTRACTIONS_VALUEEMISSION_OR_HONESTGALERKINRUN_"
    "BUILT_PRIMITIVE_SPAN_OBSTRUCTION_OPEN"
)
NEXT = "MTT_Selected_DifferentiatedVertex_HessianCounterterm_or_GalerkinC1_ValuePacket_v1"
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
    span = load(SPAN)
    run_contract = load(RUN_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(span["status"] == "PURE_FIXED_FIBER_PRIMITIVE_SPAN_REPLAYED_AND_REJECTED_FOR_DYNAMIC_COLUMNS", "span packet status mismatch")
    require(run_contract["status"] == "HONEST_GALERKIN_RUN_CONTRACT_EMITTED_VALUES_OPEN", "run contract status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    selector = data["selector_attachment"]
    require(selector["source_selector_promoted"] is True, "source selector not promoted")
    require(selector["same_source"] is True, "source selector not same-source")
    require(selector["active_shift"] == [1, 1], "active shift mismatch")
    require(selector["fixed_fiber_quotient_selected"] is True, "fixed-fiber quotient not selected")
    require(selector["absolute_fiber_origin_selected"] is False, "absolute fiber origin overselected")
    require(selector["static_sector_route_selected"] is True, "static route not selected")
    require(selector["alpha1_dotD_driver_selected"] is True, "alpha1/dotD driver not selected")

    replay = data["primitive_value_replay"]
    require(replay["fixed_fiber_representatives_replayed"] is True, "fixed-fiber replay missing")
    require(replay["current_spectral_observable_class_selected"] is True, "current spectral class not selected")
    require(replay["current_layer_promoted_as_flavor_closure"] is False, "current layer overclaimed")
    require(replay["selected_primitive_overlap_values_filled"] is False, "primitive values overfilled")

    orbit = span["fixed_fiber_orbit"]
    require(orbit["fixed_fiber_class"] == [0, 1, 2], "fiber class mismatch")
    require(orbit["representative_shift"] == 0, "representative shift mismatch")
    require(orbit["absolute_origin_selected"] is False, "absolute origin overselected in span")
    require(orbit["basis_dimension"] == 3, "fixed-fiber basis dimension mismatch")
    require(orbit["orbit_sum_rank"] == 1, "orbit sum rank mismatch")

    phase = span["single_sector_least_squares"]["phase_I_plus_Z_against_fixed_fiber_span"]
    shift = span["single_sector_least_squares"]["shift_I_plus_X_against_fixed_fiber_span"]
    require(near(phase["target_norm_sq"], 6.0), "phase target norm mismatch")
    require(near(shift["target_norm_sq"], 6.0), "shift target norm mismatch")
    require(near(phase["residual_norm_sq"], 4.0), "phase residual mismatch")
    require(near(shift["residual_norm_sq"], 2.0), "shift residual mismatch")
    require(phase["in_fixed_fiber_span"] is False, "phase unexpectedly in span")
    require(shift["in_fixed_fiber_span"] is False, "shift unexpectedly in span")

    routed = span["routed_72_real_residuals"]
    require(near(routed["phase_column_residual_norm_sq_two_sectors"], 8.0), "routed phase residual mismatch")
    require(near(routed["shift_column_residual_norm_sq_two_sectors"], 4.0), "routed shift residual mismatch")
    require(near(routed["b_phase_plus_shift_residual_norm_sq_four_sectors"], 12.0), "routed b residual mismatch")
    require(near(routed["conditional_b_norm_sq"], 24.0), "conditional b norm mismatch")

    obstruction = span["obstruction"]
    require(obstruction["pure_fixed_fiber_primitive_span_can_emit_phase_column"] is False, "phase obstruction missing")
    require(obstruction["pure_fixed_fiber_primitive_span_can_emit_shift_column"] is False, "shift obstruction missing")
    require(obstruction["pure_fixed_fiber_primitive_span_can_emit_conditional_weylpair_packet"] is False, "packet obstruction missing")

    contract = data["honest_galerkin_run_contract"]
    require(contract == run_contract, "embedded run contract mismatch")
    require(contract["selected_source_verified"] is False, "honest Galerkin oververified")
    require(contract["target_fitting_forbidden"] is True, "target-fitting guard missing")
    require(contract["observed_flavor_data_forbidden"] is True, "observed-data guard missing")
    require(contract["required_outputs"] == [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ], "required outputs mismatch")
    for key, value in contract["required_inputs"].items():
        require(value is None, f"required input unexpectedly filled: {key}")

    theorem = data["theorem"]
    require(theorem["proved"] is True, "theorem not proved")
    require(len(theorem["proof_steps"]) == 6, "proof step count mismatch")

    decision = data["promotion_decision"]
    require(decision["source_selector_attached_to_template"] is True, "selector not attached")
    require(decision["fixed_fiber_current_layer_replayed"] is True, "fixed-fiber layer not replayed")
    require(decision["pure_fixed_fiber_replay_rejected_as_dynamic_value_fill"] is True, "span no-go missing")
    for key in [
        "selected_primitive_overlap_contractions_promoted",
        "selected_dynamic_overlap_tensor_promoted",
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
        "selected_source_selector_attached_to_differentiated_template",
        "finite_fixed_fiber_primitive_span_replayed",
        "pure_fixed_fiber_span_obstruction_proved",
        "honest_Galerkin_C1_value_run_contract_emitted",
        "next_value_packet_cutset_sharpened",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_differentiated_vertex_operator_phase_Z",
        "selected_differentiated_vertex_operator_shift_X",
        "selected_basis_transport_corrections",
        "selected_Hessian_counterterms",
        "selected_primitive_overlap_contraction_values",
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
        "selected_primitive_overlap_contractions_claimed",
        "selected_dynamic_overlap_tensor_claimed",
        "selected_Hessian_counterterms_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")

    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(cert["pure_fixed_fiber_span_obstruction_proved"] is True, "certificate span no-go missing")
    require("No observed masses" in note, "note missing no-observed guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
