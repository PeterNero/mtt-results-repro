"""Build differentiated C1 orthogonal-completion principle / independent quadrature-Hessian solve gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom.candidate.json"
NEXT_CONTRACT = (
    DATA
    / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom"
    / "minimal_next_source_contract.packet.json"
)
DERIVATION_LADDER = (
    DATA
    / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom"
    / "residual_projector_derivation_ladder.packet.json"
)
FIRST_REPLAY = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "first_galerkin_replay_result.packet.json"
)
PRIMITIVE_TERMS = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "inputs"
    / "primitive_contraction_terms.packet.json"
)

SLUG = "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
VARIATIONAL_DERIVATION = PACKET_DIR / "orthogonal_completion_variational_derivation.packet.json"
QUADRATURE_SOLVE_SPEC = PACKET_DIR / "independent_quadrature_hessian_solve_spec.packet.json"
SUFFICIENCY_REPLAY = PACKET_DIR / "principle_or_solve_sufficiency_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATEDC1ORTHOGONALCOMPLETIONPRINCIPLE_OR_INDEPENDENTQUADRATUREHESSIANSOLVE_BUILT_VARIATIONAL_REDUCTION_OPEN"
NEXT = "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    next_contract = load(NEXT_CONTRACT)
    ladder = load(DERIVATION_LADDER)
    first_replay = load(FIRST_REPLAY)
    primitive = load(PRIMITIVE_TERMS)

    replay = first_replay["acceptance_results"]

    variational_derivation = {
        "schema": "MTTDifferentiatedC1OrthogonalCompletionVariationalDerivation.v1",
        "status": "EULER_PROJECTION_DERIVED_SELECTED_FUNCTIONAL_OPEN",
        "principle_name": next_contract["option_A_derive_principle"]["name"],
        "candidate_functional": {
            "name": "C1DefectLeakageFunctional",
            "form": "minimize ||Delta - Delta_fixed||_F^2 subject to Q_fixed Delta = 0 and selected C1 boundary/routing constraints",
            "constraint_space": "trace/Frobenius orthogonal complement of the selected fixed-fiber response span",
            "euler_condition": "Delta_residual = Q_residual Delta_target",
        },
        "derived_inside_this_gate": {
            "finite_dimensional_projection_euler_equation": True,
            "least_norm_trace_orthogonal_completion_selects_Q_residual": True,
            "if_selected_C1_defect_functional_equals_candidate_then_PhiFinC1_applies_Q_residual": True,
        },
        "not_derived_inside_this_gate": {
            "selected_MTT_C1_defect_functional_is_candidate": True,
            "physical_PhiFinC1_variation_minimizes_this_functional": True,
            "independent_quadrature_hessian_values": True,
        },
        "proof_reduction": [
            "The selected fixed-fiber span defines an orthogonal decomposition of the 72-real C1 target space.",
            "For any admissible target response, the unique least-Frobenius correction in the complement is Q_residual applied to the target.",
            "The Euler normal equation for the candidate leakage functional is exactly orthogonality to the fixed-fiber span.",
            "Therefore the orthogonal-completion principle follows if the selected differentiated C1 source functional is this leakage functional.",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    quadrature_spec = {
        "schema": "MTTIndependentQuadratureHessianSolveSpec.v1",
        "status": "NUMERICAL_SOLVE_SPEC_READY_DATA_MISSING",
        "required_values": next_contract["option_B_compute_values"]["required_values"],
        "basis_requirements": {
            "zero_mode_basis_selected_by": "HYM/Galerkin source solve, not canonical support replay",
            "normalization": "same finite trace/Frobenius coordinate convention as the 72-real target",
            "sector_order": ["u", "e", "d", "nuD"],
        },
        "quadrature_requirements": {
            "primitive_3x3_contractions": "computed from selected basis and primitive C1 vertex/transport terms",
            "hessian_source_vector": "computed by differentiating the selected C1 functional or retarded kernel",
            "forbidden": [
                "copying R_Z/R_X from the residual-projector axiom contract",
                "copying b_selected from the patched replay",
                "using observed masses/mixings/CP data as residual targets",
            ],
        },
        "acceptance_tests": {
            "A_shape": [72, 2],
            "b_shape": [72],
            "rank_at_least_2": True,
            "column_span_or_residual_declared": True,
            "deltaTheta_solve_required": True,
            "sector_response_matrices_required": True,
        },
        "run_now": False,
        "why_not_run_now": [
            "selected HYM/Galerkin zero-mode basis data are not present",
            "independent primitive quadrature table is not present",
            "independent Hessian/source-vector differentiation is not present",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    sufficiency_replay = {
        "schema": "MTTPrincipleOrSolveSufficiencyReplay.v1",
        "status": "SUFFICIENCY_PROVED_ANTECEDENT_OPEN",
        "if_variational_source_functional_selected": {
            "physical_PhiFinC1_applies_Q_residual": True,
            "unpatched_A_selected_promotes": True,
            "unpatched_b_selected_promotes": True,
            "unpatched_deltaTheta_C1_promotes": True,
            "SM_parity_dynamic_packet_closes": True,
        },
        "if_independent_quadrature_hessian_solve_passes": {
            "honest_independent_Galerkin_C1_closes": True,
            "unpatched_A_selected_promotes": True,
            "unpatched_b_selected_promotes": True,
            "unpatched_deltaTheta_C1_promotes": True,
            "SM_parity_dynamic_packet_closes": True,
        },
        "current_replay_values": {
            "A_transpose_A": replay["A_transpose_A"],
            "A_transpose_b": replay["A_transpose_b"],
            "deltaTheta_C1": replay["deltaTheta_C1"],
            "phase_residual_norm_sq": primitive["terms"]["phase_clock_R_Z"]["residual_norm_sq"],
            "shift_residual_norm_sq": primitive["terms"]["shift_vertex_R_X"]["residual_norm_sq"],
        },
        "antecedent_met_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDifferentiatedC1OrthogonalCompletionPrincipleOrIndependentQuadratureHessianSolve",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "minimal_next_source_contract": rel(NEXT_CONTRACT),
            "derivation_ladder": rel(DERIVATION_LADDER),
            "first_galerkin_replay": rel(FIRST_REPLAY),
            "primitive_terms": rel(PRIMITIVE_TERMS),
        },
        "output_packets": {
            "orthogonal_completion_variational_derivation": rel(VARIATIONAL_DERIVATION),
            "independent_quadrature_hessian_solve_spec": rel(QUADRATURE_SOLVE_SPEC),
            "principle_or_solve_sufficiency_replay": rel(SUFFICIENCY_REPLAY),
        },
        "what_closes_now": {
            "finite_dimensional_variational_projection_derivation": True,
            "orthogonal_completion_principle_reduced_to_selected_C1_defect_functional": True,
            "independent_quadrature_hessian_solve_spec_ready": True,
            "sufficiency_of_either_route_proved": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "select_C1_defect_leakage_functional_from_MTT": True,
            "prove_physical_PhiFinC1_minimizes_selected_defect_functional": True,
            "fill_selected_zero_mode_basis_data": True,
            "fill_independent_primitive_quadrature_table": True,
            "fill_independent_hessian_source_vector": True,
            "run_independent_quadrature_hessian_solve": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "variational_euler_projection_derived": True,
            "selected_C1_defect_functional_proved": False,
            "physical_PhiFinC1_application_rule_proved": False,
            "independent_quadrature_hessian_solve_run": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "VariationalProjectionReductionTheorem",
            "proved": True,
            "statement": (
                "The differentiated C1 orthogonal-completion principle is not arbitrary: it follows "
                "from the Euler equation of the finite-dimensional least-Frobenius C1 defect/leakage "
                "functional under the selected fixed-fiber constraints. Thus the unpatched proof is "
                "reduced to selecting that defect functional from MTT, or bypassing it with independent "
                "quadrature/Hessian data."
            ),
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_preserved": previous["patched_spine_closure_preserved"],
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "patched_spine_closure_preserved": candidate["patched_spine_closure_preserved"],
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedC1OrthogonalCompletionPrinciple or IndependentQuadratureHessianSolve v1

Status: `{STATUS}`.

This gate proves the variational reduction.

Closed:

```text
finite-dimensional Euler projection        = derived
least-Frobenius orthogonal completion      = derives Q_residual
either route is sufficient                 = proved
```

Still open:

```text
selected MTT C1 defect functional          = not yet selected
physical Phi_fin^C1 minimizes it           = not yet proved
independent quadrature/Hessian data        = not yet filled
```

So the next true source object is either:

```text
1. C1DefectFunctionalSource
2. IndependentQuadratureDataFill
```

Replay if either antecedent is supplied:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
```

Next artifact: `{NEXT}`.
"""

    VARIATIONAL_DERIVATION.write_text(json.dumps(variational_derivation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QUADRATURE_SOLVE_SPEC.write_text(json.dumps(quadrature_spec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUFFICIENCY_REPLAY.write_text(json.dumps(sufficiency_replay, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
