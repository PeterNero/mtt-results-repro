"""Audit differentiated C1 orthogonal-completion principle / independent quadrature-Hessian solve gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VARIATIONAL_DERIVATION = PACKET_DIR / "orthogonal_completion_variational_derivation.packet.json"
QUADRATURE_SOLVE_SPEC = PACKET_DIR / "independent_quadrature_hessian_solve_spec.packet.json"
SUFFICIENCY_REPLAY = PACKET_DIR / "principle_or_solve_sufficiency_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DIFFERENTIATEDC1ORTHOGONALCOMPLETIONPRINCIPLE_OR_INDEPENDENTQUADRATUREHESSIANSOLVE_BUILT_VARIATIONAL_REDUCTION_OPEN"
NEXT = "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    variational = load(VARIATIONAL_DERIVATION)
    quadrature = load(QUADRATURE_SOLVE_SPEC)
    sufficiency = load(SUFFICIENCY_REPLAY)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(variational["status"] == "EULER_PROJECTION_DERIVED_SELECTED_FUNCTIONAL_OPEN", "variational status mismatch")
    derived = variational["derived_inside_this_gate"]
    require(derived["finite_dimensional_projection_euler_equation"] is True, "Euler projection missing")
    require(derived["least_norm_trace_orthogonal_completion_selects_Q_residual"] is True, "least norm result missing")
    require(derived["if_selected_C1_defect_functional_equals_candidate_then_PhiFinC1_applies_Q_residual"] is True, "conditional PhiFinC1 implication missing")
    not_derived = variational["not_derived_inside_this_gate"]
    require(not_derived["selected_MTT_C1_defect_functional_is_candidate"] is True, "functional selection gap missing")
    require(not_derived["physical_PhiFinC1_variation_minimizes_this_functional"] is True, "physical minimization gap missing")
    require(len(variational["proof_reduction"]) == 4, "proof reduction list mismatch")

    require(quadrature["status"] == "NUMERICAL_SOLVE_SPEC_READY_DATA_MISSING", "quadrature status mismatch")
    require(len(quadrature["required_values"]) == 6, "required value count mismatch")
    require(quadrature["acceptance_tests"]["A_shape"] == [72, 2], "A shape mismatch")
    require(quadrature["acceptance_tests"]["b_shape"] == [72], "b shape mismatch")
    require(quadrature["run_now"] is False, "quadrature run overclaimed")
    require(len(quadrature["why_not_run_now"]) == 3, "why-not-run mismatch")
    require("copying R_Z/R_X from the residual-projector axiom contract" in quadrature["quadrature_requirements"]["forbidden"], "forbidden replay missing")

    require(sufficiency["status"] == "SUFFICIENCY_PROVED_ANTECEDENT_OPEN", "sufficiency status mismatch")
    require(sufficiency["if_variational_source_functional_selected"]["SM_parity_dynamic_packet_closes"] is True, "variational sufficiency missing")
    require(sufficiency["if_independent_quadrature_hessian_solve_passes"]["SM_parity_dynamic_packet_closes"] is True, "quadrature sufficiency missing")
    require(sufficiency["current_replay_values"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(sufficiency["current_replay_values"]["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(sufficiency["current_replay_values"]["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(sufficiency["antecedent_met_now"] is False, "antecedent overclaimed")

    for key in [
        "finite_dimensional_variational_projection_derivation",
        "orthogonal_completion_principle_reduced_to_selected_C1_defect_functional",
        "independent_quadrature_hessian_solve_spec_ready",
        "sufficiency_of_either_route_proved",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "select_C1_defect_leakage_functional_from_MTT",
        "prove_physical_PhiFinC1_minimizes_selected_defect_functional",
        "fill_selected_zero_mode_basis_data",
        "fill_independent_primitive_quadrature_table",
        "fill_independent_hessian_source_vector",
        "run_independent_quadrature_hessian_solve",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    require(decision["variational_euler_projection_derived"] is True, "Euler promotion missing")
    require(decision["selected_C1_defect_functional_proved"] is False, "functional selection overclaimed")
    require(decision["physical_PhiFinC1_application_rule_proved"] is False, "PhiFinC1 overclaimed")
    require(decision["independent_quadrature_hessian_solve_run"] is False, "quadrature overclaimed")
    require(decision["unpatched_SM_parity_dynamic_packet_closed"] is False, "unpatched closure overclaimed")
    require(data["closure_claimed"] is False, "global closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require("variational reduction" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
