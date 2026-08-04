"""Audit selected C1 variation-principle derivation / quadrature-engine run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1variationprinciplederivation_or_quadratureenginerun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_variation_principle_derivation_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_quadrature_engine_run_attempt.packet.json"
CUTSET = PACKET_DIR / "minimal_engine_or_principle_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1VariationPrincipleDerivation_or_QuadratureEngineRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_C1VARIATIONPRINCIPLE_OR_QUADRATUREENGINERUN_BUILT_ENGINE_SKELETON_PRINCIPLE_DERIVATION_OPEN"
NEXT = "MTT_Selected_PhysicalVariationPrincipleSource_or_QuadratureKernelValues_v1"


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
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(route_a["status"] == "VARIATION_PRINCIPLE_DERIVATION_ATTEMPT_SUPPORT_CLOSED_PHYSICAL_RULE_OPEN", "route A status mismatch")
    for key, value in route_a["closed_support"].items():
        require(value is True, f"closed support missing: {key}")
    derived = route_a["finite_dimensional_derivation"]
    require(derived["finite_euler_projection_derived"] is True, "finite Euler derivation missing")
    require(derived["least_norm_completion_selects_Q_residual"] is True, "least-norm Q derivation missing")
    require(derived["conditional_PhiFinC1_application"] is True, "conditional PhiFinC1 application missing")
    for key in [
        "selected_MTT_C1_defect_functional_is_candidate",
        "physical_PhiFinC1_variation_minimizes_candidate",
        "boundary_cancellation_for_selected_dynamic_trace",
        "b_selected_emitted_as_physical_source",
    ]:
        require(route_a["not_derived_as_physical_MTT_rule"][key] is True, f"route A gap missing: {key}")
    require(route_a["route_A_closed_now"] is False, "route A overclaimed")

    require(route_b["status"] == "QUADRATURE_ENGINE_SKELETON_BUILT_VALUES_NOT_EXECUTED", "route B status mismatch")
    engine = route_b["engine_spec"]
    require(engine["stage_counts"]["basis"] == 19, "basis stage count mismatch")
    require(engine["stage_counts"]["primitive_contractions"] == 72, "primitive stage count mismatch")
    require(engine["stage_counts"]["hessian_source"] == 2, "hessian stage count mismatch")
    require(engine["stage_counts"]["sector_matrices"] == 36, "sector stage count mismatch")
    require(engine["selected_basis_rows"] == 19 and engine["basis_stage_ready"] is True, "basis readiness mismatch")
    require(engine["primitive_rows_replay_available"] == 36, "replay row count mismatch")
    require(engine["primitive_rows_independent"] == 0, "independent primitive row overclaim")
    require(route_b["locked_acceptance_oracle"]["passes_locked_target_by_replay"] is True, "locked target replay missing")
    require(route_b["locked_acceptance_oracle"]["oracle_is_not_independent_execution"] is True, "oracle guardrail missing")
    for key in [
        "selected_quadrature_engine_or_rule",
        "primitive_three_by_three_contraction_integrals",
        "independent_hessian_source_vector",
        "sector_response_matrices",
        "error_bounds_or_exactness_certificate",
    ]:
        require(route_b["missing_for_engine_run"][key] is True, f"route B gap missing: {key}")
    require(route_b["selected_quadrature_engine_or_rule"] is False, "quadrature engine overclaimed")
    require(route_b["run_executed_now"] is False, "engine run overclaimed")
    require(route_b["independent_values_emitted_now"] is False, "independent values overclaimed")
    require(route_b["route_B_closed_now"] is False, "route B overclaimed")

    require(cutset["status"] == "MINIMAL_ENGINE_OR_PRINCIPLE_CUTSET_SELECTED", "cutset status mismatch")
    for key in [
        "static_SM_slot_source_arrows",
        "Qa_SU3_static_color_operator_packet",
        "alpha1_dotD_driver",
        "selected_basis_rows",
        "canonical_Q_residual",
        "finite_Euler_projection",
        "locked_target_linear_algebra",
        "replay_backed_rows",
    ]:
        require(cutset["already_not_blockers"][key] is True, f"already-not-blocker missing: {key}")
    require("promoting replay-backed rows as independent quadrature" in cutset["forbidden_shortcuts"], "replay shortcut guardrail missing")
    require(cutset["closure_claimed"] is False and cutset["unpatched_theorem_closure_claimed"] is False, "cutset closure overclaim")

    for key in [
        "route_A_formal_variational_derivation_attached",
        "route_A_physical_rule_gap_isolated",
        "route_B_quadrature_engine_skeleton_built",
        "route_B_required_rows_enumerated",
        "minimal_cutset_selected",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_physical_C1_variation_principle",
        "selected_C1_defect_functional_source",
        "selected_dynamic_trace_boundary_cancellation",
        "selected_quadrature_measure_pairing_or_kernel",
        "independent_primitive_contraction_values",
        "independent_hessian_source_vector",
        "independent_sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("physical C1 action/source derived     = False" in note, "note missing route A status")
    require("independent engine run executed       = False" in note, "note missing route B status")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
