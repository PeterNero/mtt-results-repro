"""Audit C1 defect-functional source / independent quadrature data-fill gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL_SOURCE = PACKET_DIR / "c1_defect_functional_uniqueness_source.packet.json"
PHYSICAL_APPLICATION = PACKET_DIR / "phifinc1_physical_application_source_gap.packet.json"
QUADRATURE_DATA = PACKET_DIR / "independent_quadrature_data_fill_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_C1DEFECTFUNCTIONALSOURCE_OR_INDEPENDENTQUADRATUREDATAFILL_BUILT_FUNCTIONAL_UNIQUENESS_OPEN_APPLICATION"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    functional = load(FUNCTIONAL_SOURCE)
    physical = load(PHYSICAL_APPLICATION)
    quadrature = load(QUADRATURE_DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(
        functional["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
        "functional source status mismatch",
    )
    inputs = functional["selection_inputs"]
    for key in [
        "selected_trace_frobenius_metric",
        "selected_fixed_fiber_response_span",
        "selected_72_real_coordinate_target",
        "selected_no_observed_target_policy",
    ]:
        require(inputs[key] is True, f"functional input missing: {key}")
    require(inputs["selected_static_sector_routing"] == ["Z->u,e", "X->d,nuD"], "static route mismatch")
    conditions = functional["uniqueness_conditions"]
    for key in [
        "quadratic",
        "positive_semidefinite",
        "invariant_under_unitary_change_of_selected_zero_mode_basis",
        "vanishes_on_fixed_fiber_span",
        "penalizes_only_trace_frobenius_leakage_into_residual_complement",
        "no_extra_weights_or_sector_knobs",
    ]:
        require(conditions[key] is True, f"uniqueness condition missing: {key}")
    result = functional["uniqueness_result"]
    require(result["unique_up_to_overall_positive_scale"] is True, "uniqueness missing")
    require(result["overall_scale_cancels_from_euler_projection"] is True, "scale cancellation missing")
    require(result["euler_condition"] == "Delta_residual = Q_residual Delta_target", "Euler condition mismatch")
    require(result["selects_Q_residual"] is True, "Q_residual selection missing")
    for key in [
        "physical_PhiFinC1_variation_minimizes_this_functional",
        "independent_quadrature_hessian_values",
        "unpatched_A_selected_b_selected_promotion",
    ]:
        require(functional["what_this_does_not_source"][key] is True, f"over-sourcing guard missing: {key}")

    require(
        physical["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN",
        "physical application status mismatch",
    )
    now = physical["now_available"]
    require(now["unique_formal_C1_defect_functional"] is True, "formal functional not available")
    require(now["Euler_projection_derivation"] is True, "Euler derivation not available")
    require(now["sufficiency_if_PhiFinC1_minimizes_functional"] is True, "sufficiency not available")
    remaining = physical["remaining_physical_application_rule"]
    require(remaining["not_proved_now"] is True, "physical application overproved")
    require(len(remaining["why_not_automatic"]) == 3, "why-not-automatic mismatch")
    require(physical["if_supplied_then"]["SM_parity_dynamic_packet_closes"] is True, "physical implication missing")

    require(
        quadrature["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED",
        "quadrature status mismatch",
    )
    require(len(quadrature["required_values"]) == 6, "required values mismatch")
    available = quadrature["input_data_available_now"]
    for key in [
        "selected_zero_mode_basis_data",
        "independent_primitive_quadrature_table",
        "independent_hessian_source_vector",
        "independent_sector_response_matrices",
    ]:
        require(available[key] is False, f"quadrature data overfilled: {key}")
    require(quadrature["acceptance_tests"]["A_shape"] == [72, 2], "A shape mismatch")
    require(quadrature["acceptance_tests"]["b_shape"] == [72], "b shape mismatch")
    require("copying b_selected from the patched replay" in quadrature["forbidden_shortcuts"], "forbidden shortcut missing")
    require(quadrature["if_supplied_then"]["honest_independent_Galerkin_C1_closes"] is True, "quadrature implication missing")

    for key in [
        "unique_formal_C1_defect_functional_sourced",
        "no_extra_weight_or_sector_knob_needed_for_functional",
        "euler_projection_scale_independence_verified",
        "physical_application_gap_is_isolated",
        "independent_quadrature_data_requirements_preserved",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "prove_PhiFinC1_minimizes_unique_C1_defect_functional",
        "bind_differentiated_PhiFinC1_to_variational_problem",
        "fill_selected_zero_mode_basis_data",
        "fill_independent_primitive_quadrature_table",
        "fill_independent_hessian_source_vector",
        "run_independent_quadrature_hessian_solve",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    require(decision["selected_C1_defect_functional_formal_source_promoted"] is True, "formal functional not promoted")
    for key in [
        "physical_PhiFinC1_application_rule_proved",
        "independent_quadrature_data_filled",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["patched_spine_closure_preserved"] is True, "patched spine preservation missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require("formal C1 defect functional" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
