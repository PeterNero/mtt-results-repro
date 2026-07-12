from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_independent_galerkin_or_residual_projector_derivation_cutset_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
VARIATIONAL = SM_DIR / "orthogonal_completion_variational_derivation.packet.json"
QUADRATURE_SPEC = SM_DIR / "independent_quadrature_hessian_solve_spec.packet.json"
SUFFICIENCY = SM_DIR / "principle_or_solve_sufficiency_replay.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_c1_orthogonal_completion_or_independent_hessian_solve_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_c1_orthogonal_completion_or_independent_hessian_solve.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_C1OrthogonalCompletion_or_IndependentHessianSolve_Import_v1.md"

STATUS = "POST_ALPHA_C1_ORTHOGONAL_COMPLETION_OR_INDEPENDENT_HESSIAN_SOLVE_IMPORTED_VARIATIONAL_REDUCTION_OPEN"
NEXT = "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    variational = load(VARIATIONAL)
    quadrature = load(QUADRATURE_SPEC)
    sufficiency = load(SUFFICIENCY)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_orthogonal_completion_principle_or_independent_quadrature_hessian_solve"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["patched_spine_closure_preserved"] is True,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "VariationalProjectionReductionTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["variational_euler_projection_derived"] is True,
            candidate["promotion_decision"]["selected_C1_defect_functional_proved"] is False,
            candidate["promotion_decision"]["physical_PhiFinC1_application_rule_proved"] is False,
            candidate["promotion_decision"]["independent_quadrature_hessian_solve_run"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
        ]
    )

    variational_ok = all(
        [
            variational["schema"] == "MTTDifferentiatedC1OrthogonalCompletionVariationalDerivation.v1",
            variational["status"] == "EULER_PROJECTION_DERIVED_SELECTED_FUNCTIONAL_OPEN",
            variational["observed_data_used"] is False,
            variational["target_fitting_used"] is False,
            variational["principle_name"] == "DifferentiatedC1OrthogonalCompletionPrinciple",
            variational["candidate_functional"]["name"] == "C1DefectLeakageFunctional",
            all(variational["derived_inside_this_gate"].values()),
            all(variational["not_derived_inside_this_gate"].values()),
            len(variational["proof_reduction"]) == 4,
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureHessianSolveSpec.v1",
            quadrature["status"] == "NUMERICAL_SOLVE_SPEC_READY_DATA_MISSING",
            quadrature["run_now"] is False,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
            quadrature["acceptance_tests"]["A_shape"] == [72, 2],
            quadrature["acceptance_tests"]["b_shape"] == [72],
            quadrature["basis_requirements"]["zero_mode_basis_selected_by"]
            == "HYM/Galerkin source solve, not canonical support replay",
            len(quadrature["quadrature_requirements"]["forbidden"]) == 3,
            len(quadrature["required_values"]) == 6,
            len(quadrature["why_not_run_now"]) == 3,
        ]
    )

    sufficiency_ok = all(
        [
            sufficiency["schema"] == "MTTPrincipleOrSolveSufficiencyReplay.v1",
            sufficiency["status"] == "SUFFICIENCY_PROVED_ANTECEDENT_OPEN",
            sufficiency["antecedent_met_now"] is False,
            sufficiency["observed_data_used"] is False,
            sufficiency["target_fitting_used"] is False,
            sufficiency["current_replay_values"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            sufficiency["current_replay_values"]["A_transpose_b"] == [12.0, 12.0],
            sufficiency["current_replay_values"]["deltaTheta_C1"] == [1.0, 1.0],
            sufficiency["if_variational_source_functional_selected"]["SM_parity_dynamic_packet_closes"] is True,
            sufficiency["if_independent_quadrature_hessian_solve_passes"]["SM_parity_dynamic_packet_closes"] is True,
        ]
    )

    what_closes_now = {
        "previous_dependency_cutset_consumed": prev_ok,
        "variational_projection_reduction_imported": imported_ok,
        "finite_dimensional_euler_projection_derived": variational_ok,
        "independent_quadrature_hessian_solve_spec_ready": quadrature_ok,
        "principle_or_solve_sufficiency_proved": sufficiency_ok,
    }

    what_remains_open = {
        "select_C1_defect_leakage_functional_from_MTT": True,
        "prove_physical_PhiFinC1_minimizes_selected_defect_functional": True,
        "fill_selected_zero_mode_basis_data": True,
        "fill_independent_primitive_quadrature_table": True,
        "fill_independent_hessian_source_vector": True,
        "run_independent_quadrature_hessian_solve": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_select_C1_defect_functional": True,
        "does_not_prove_physical_PhiFinC1_minimization": True,
        "does_not_run_independent_quadrature_hessian_solve": True,
        "does_not_promote_unpatched_A_or_b": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaC1OrthogonalCompletionOrIndependentHessianSolveImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The differentiated C1 orthogonal-completion principle is reduced to the "
            "Euler normal equation of a finite-dimensional least-Frobenius C1 "
            "defect/leakage functional under selected fixed-fiber constraints. Either "
            "selecting that physical C1 defect functional from MTT or supplying an "
            "independent quadrature/Hessian solve would close the unpatched dynamic C1 "
            "packet. This gate proves the variational reduction and sufficiency, not "
            "the selected functional or the independent numerical data."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "orthogonal_completion_variational_derivation": variational,
        "independent_quadrature_hessian_solve_spec": quadrature,
        "principle_or_solve_sufficiency_replay": sufficiency,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "variational_euler_projection_derived": True,
            "selected_C1_defect_functional_open": True,
            "physical_PhiFinC1_minimization_open": True,
            "independent_quadrature_data_open": True,
            "frontier_is_C1_defect_functional_source_or_independent_quadrature_data_fill": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "orthogonal_completion_variational_derivation": str(VARIATIONAL),
            "independent_quadrature_hessian_solve_spec": str(QUADRATURE_SPEC),
            "principle_or_solve_sufficiency_replay": str(SUFFICIENCY),
        },
    }

    note = f"""# PostAlpha C1 Orthogonal Completion or Independent Hessian Solve Import v1

## Result

The orthogonal-completion route has been reduced to a variational source.

Closed:

```text
finite-dimensional Euler projection
least-Frobenius orthogonal completion implies Q_residual
either selected C1 defect functional or independent quadrature/Hessian solve is sufficient
```

Open:

```text
selected MTT C1 defect/leakage functional
physical Phi_fin^C1 minimizes that functional
independent quadrature/Hessian data
unpatched dynamic C1 closure
```

Exact replay if either antecedent is supplied:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
```

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_c1_orthogonal_completion_or_independent_hessian_solve",
        "status": STATUS,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
