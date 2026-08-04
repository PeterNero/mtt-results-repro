"""Audit differentiated residual-projector source-rule / Galerkin C1 execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
SOURCE_RULE = PACKET_DIR / "differentiated_residual_projector_source_rule.contract.json"
ROUTE_LADDER = PACKET_DIR / "source_rule_or_execution_route_ladder.packet.json"
HONEST_EXECUTION = PACKET_DIR / "honest_galerkin_c1_execution_requirement.packet.json"
CERT = ROOT / "certificates" / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution.py"

STATUS = (
    "MTT_SELECTED_DIFFERENTIATEDRESIDUALPROJECTORSOURCERULE_OR_HONESTGALERKINC1EXECUTION_"
    "BUILT_SOURCE_RULE_CONTRACT_OPEN"
)
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source_rule = load(SOURCE_RULE)
    route_ladder = load(ROUTE_LADDER)
    honest_execution = load(HONEST_EXECUTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(source_rule["status"] == "SOURCE_RULE_CONTRACT_EMITTED_VALUES_OPEN", "source rule status mismatch")
    support = source_rule["already_selected_support"]
    for key in [
        "canonical_Q_residual_available",
        "source_selector_promoted",
        "primitive_vertex_or_basis_transport_source_selector_promoted",
        "static_sector_route_selected",
        "static_trace_transfer_normalization_selected",
        "alpha1_dotD_driver_verified",
    ]:
        require(support[key] is True, f"selected support missing: {key}")
    require(support["Q_residual_rank"] == 6, "Q residual rank mismatch")

    why_not = source_rule["why_selector_is_not_enough"]
    require(why_not["source_selector_is_value_emission"] is False, "selector overpromoted as value")
    require(why_not["primitive_fixed_fiber_span_can_close"] is False, "primitive span overclosed")
    require(why_not["phase_single_sector_residual_norm_sq"] == 4.0, "phase residual norm mismatch")
    require(why_not["shift_single_sector_residual_norm_sq"] == 2.0, "shift residual norm mismatch")
    require(why_not["stationary_transport_only_ruled_out"] is True, "transport-only no-go missing")

    conditional = source_rule["exact_conditional_values_if_rule_is_proved"]
    require(conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional ATA mismatch")
    require(conditional["A_transpose_b"] == [12.0, 12.0], "conditional ATb mismatch")
    require(conditional["deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")
    require(conditional["rank"] == 2, "conditional rank mismatch")
    require(conditional["SM_parity_dynamic_packet_would_close"] is True, "SM parity implication missing")
    require(conditional["no_knob_flavor_constants_would_close"] is False, "no-knob overclaim")

    for key in [
        "selected_differentiated_residual_projector_source_rule",
        "selected_basis_transport_vertex_or_Hessian_values",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
    ]:
        require(source_rule["currently_emitted"][key] is False, f"source rule overclaimed: {key}")
    require(source_rule["observed_data_used"] is False, "source rule used observed data")
    require(source_rule["target_fitting_used"] is False, "source rule used target fitting")

    require(route_ladder["status"] == "ROUTE_LADDER_RANKED_NO_PROMOTION", "route ladder status mismatch")
    require(route_ladder["straight_path"]["id"] == "A_differentiated_residual_projector_rule", "straight path id mismatch")
    near = route_ladder["near_straight_source_path"]
    require(near["id"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "near-straight id mismatch")
    require(near["algebraically_sufficient"] is True, "near-straight algebraic sufficiency missing")
    require(near["conditional_A_rank"] == 2, "near-straight rank mismatch")
    require(abs(near["conditional_deltaTheta"][0] - 1.0) < 1e-9, "near-straight delta 0 mismatch")
    require(abs(near["conditional_deltaTheta"][1] - 1.0) < 1e-9, "near-straight delta 1 mismatch")
    require(route_ladder["recommended_next"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "recommended next mismatch")
    require(route_ladder["observed_data_used"] is False, "route ladder used observed data")
    require(route_ladder["target_fitting_used"] is False, "route ladder used target fitting")
    for ruled_out in [
        "stationary transport-only Phi_fin^C1",
        "pure fixed-fiber primitive replay",
        "promoting canonical Q_residual without an application/source rule",
        "using observed SM flavor data or benchmark matrices as selectors",
    ]:
        require(ruled_out in route_ladder["ruled_out_paths"], f"ruled-out path missing: {ruled_out}")

    require(honest_execution["status"] == "HONEST_EXECUTION_REQUIREMENT_REEMITTED_VALUES_OPEN", "honest execution status mismatch")
    require(honest_execution["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "honest manifest mismatch")
    require(honest_execution["selected_source_verified"] is False, "honest execution oververified")
    require(honest_execution["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True, "honest SM implication missing")
    require(honest_execution["would_close_no_knob_flavor_constants_if_values_emitted"] is False, "honest no-knob overclaim")
    require(honest_execution["observed_flavor_data_forbidden"] is True, "observed data not forbidden")
    require(honest_execution["target_fitting_forbidden"] is True, "target fitting not forbidden")
    for output in [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ]:
        require(output in honest_execution["required_outputs"], f"required output missing: {output}")

    for key in [
        "differentiated_residual_projector_source_rule_formalized",
        "enriched_weylpair_route_ranked_primary",
        "honest_Galerkin_execution_requirements_reemitted",
        "selector_vs_value_emission_gap_made_explicit",
        "ruled_out_stationary_and_fixed_fiber_shortcuts",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_differentiated_residual_projector_source_rule",
        "selected_enriched_weylpair_source_emission",
        "selected_basis_transport_vertex_or_Hessian_values",
        "honest_selected_Galerkin_C1_execution_values",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "differentiated_residual_projector_source_rule_promoted",
        "enriched_weylpair_source_emission_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"candidate overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "SM_parity_dynamic_packet_closure_claimed",
        "true_SM_equivalence_claimed",
        "no_knob_closure_claimed",
    ]:
        require(data[key] is False, f"candidate flag overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Route B is ranked primary" in note, "note missing primary route")
    require("selector data is not value emission" in note, "note missing selector/value warning")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
