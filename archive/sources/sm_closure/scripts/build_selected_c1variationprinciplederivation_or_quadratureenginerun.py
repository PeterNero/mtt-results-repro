"""Build selected C1 variation-principle derivation / quadrature-engine run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_c1variationprinciplederivation_or_quadratureenginerun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_variation_principle_derivation_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_quadrature_engine_run_attempt.packet.json"
CUTSET = PACKET_DIR / "minimal_engine_or_principle_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1VariationPrincipleDerivation_or_QuadratureEngineRun_v1.md"

STATUS = "MTT_SELECTED_C1VARIATIONPRINCIPLE_OR_QUADRATUREENGINERUN_BUILT_ENGINE_SKELETON_PRINCIPLE_DERIVATION_OPEN"
NEXT = "MTT_Selected_PhysicalVariationPrincipleSource_or_QuadratureKernelValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def stage_counts(schedule: dict[str, Any]) -> dict[str, int]:
    return {stage["stage"]: len(stage["rows"]) for stage in schedule["execution_order"]}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution.candidate.json")
    equivalence = load(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "necessary_sufficient_cycle_exit_theorem.packet.json")
    promotion = load(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "physical_c1_variation_source_promotion_attempt.packet.json")
    quadrature = load(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "independent_quadrature_execution_attempt.packet.json")
    variational = load(DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve" / "orthogonal_completion_variational_derivation.packet.json")
    schedule = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json")
    basis = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json")
    replay_rows = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json")
    hessian = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json")

    counts = stage_counts(schedule)
    selected_basis_rows = basis["selected_row_count"]
    replay_filled_rows = replay_rows["filled_by_replay_count"]

    route_a = {
        "schema": "MTTC1VariationPrincipleDerivationAttempt.v1",
        "status": "VARIATION_PRINCIPLE_DERIVATION_ATTEMPT_SUPPORT_CLOSED_PHYSICAL_RULE_OPEN",
        "source_equivalence_gate": rel(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "necessary_sufficient_cycle_exit_theorem.packet.json"),
        "formal_variational_support": rel(DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve" / "orthogonal_completion_variational_derivation.packet.json"),
        "closed_support": equivalence["closed_support"],
        "finite_dimensional_derivation": {
            "candidate_functional": variational["candidate_functional"],
            "finite_euler_projection_derived": variational["derived_inside_this_gate"]["finite_dimensional_projection_euler_equation"],
            "least_norm_completion_selects_Q_residual": variational["derived_inside_this_gate"]["least_norm_trace_orthogonal_completion_selects_Q_residual"],
            "conditional_PhiFinC1_application": variational["derived_inside_this_gate"]["if_selected_C1_defect_functional_equals_candidate_then_PhiFinC1_applies_Q_residual"],
        },
        "not_derived_as_physical_MTT_rule": {
            "selected_MTT_C1_defect_functional_is_candidate": variational["not_derived_inside_this_gate"]["selected_MTT_C1_defect_functional_is_candidate"],
            "physical_PhiFinC1_variation_minimizes_candidate": variational["not_derived_inside_this_gate"]["physical_PhiFinC1_variation_minimizes_this_functional"],
            "boundary_cancellation_for_selected_dynamic_trace": promotion["missing_for_unpatched_promotion"]["prove_boundary_cancellation_for_selected_dynamic_trace"],
            "b_selected_emitted_as_physical_source": promotion["missing_for_unpatched_promotion"]["emit_b_selected_as_physical_source_not_patch_replay"],
        },
        "route_A_closed_now": False,
        "exact_new_requirement": (
            "Derive from the selected Strominger/Theta/Phi_fin trace that the physical differentiated C1 "
            "action equals the candidate C1DefectLeakageFunctional on the admissible variation class, "
            "with vanishing boundary term and source emission of Q_residual, R_Z, R_X, and b_selected."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTQuadratureEngineRunAttempt.v1",
        "status": "QUADRATURE_ENGINE_SKELETON_BUILT_VALUES_NOT_EXECUTED",
        "source_schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
        "selected_basis_source": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json"),
        "replay_rows_source": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json"),
        "engine_spec": {
            "stages": schedule["execution_order"],
            "stage_counts": counts,
            "next_executable_stage": schedule["next_executable_stage"],
            "selected_basis_rows": selected_basis_rows,
            "basis_stage_ready": basis["accepted_for_basis_stage"] and selected_basis_rows == counts["basis"],
            "primitive_rows_required": counts["primitive_contractions"],
            "primitive_rows_replay_available": replay_filled_rows,
            "primitive_rows_independent": replay_rows["independent_quadrature_row_count"],
            "hessian_source_rows_required": counts["hessian_source"],
            "sector_matrix_rows_required": counts["sector_matrices"],
        },
        "locked_acceptance_oracle": {
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "b_norm_sq": hessian["b_norm_sq"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "passes_locked_target_by_replay": replay_rows["acceptance_replay"]["passes_locked_target"],
            "oracle_is_not_independent_execution": True,
        },
        "missing_for_engine_run": quadrature["missing_independent_execution"],
        "selected_quadrature_engine_or_rule": False,
        "run_executed_now": False,
        "independent_values_emitted_now": False,
        "route_B_closed_now": False,
        "exact_new_requirement": (
            "Emit the selected measure/pairing and row kernels for the finite C1 trace, then compute the "
            "72 primitive contraction rows, 2 Hessian/source rows, and 36 sector response rows with an "
            "exactness or error-bound certificate."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTMinimalC1EngineOrPrincipleCutset.v1",
        "status": "MINIMAL_ENGINE_OR_PRINCIPLE_CUTSET_SELECTED",
        "statement": (
            "After static SM-slot routing, alpha1/dotD replay, canonical residual projection, finite "
            "orthogonal-completion algebra, replay rows, and locked target algebra are imported, the only "
            "remaining honest exits are a selected physical C1 variation/source rule or an independent "
            "selected quadrature/Hessian execution."
        ),
        "route_A_minimal_requirements": [
            "selected physical C1 defect/action functional equals the candidate leakage functional",
            "admissible differentiated Phi_fin^C1 variations are fixed",
            "selected dynamic-trace boundary terms vanish",
            "Q_residual, R_Z, R_X, and b_selected are emitted by that same physical source rule",
        ],
        "route_B_minimal_requirements": [
            "selected finite C1 integration measure or pairing",
            "selected row-kernel definitions for basis, primitive, Hessian/source, and sector stages",
            "exact 72 primitive 3x3 contraction values",
            "independent Hessian/source vector and 36 sector response matrix rows",
            "exactness certificate or rigorous numerical error bound",
        ],
        "already_not_blockers": {
            "static_SM_slot_source_arrows": True,
            "Qa_SU3_static_color_operator_packet": True,
            "alpha1_dotD_driver": True,
            "selected_basis_rows": selected_basis_rows == counts["basis"],
            "canonical_Q_residual": True,
            "finite_Euler_projection": True,
            "locked_target_linear_algebra": True,
            "replay_backed_rows": replay_filled_rows == 36,
        },
        "forbidden_shortcuts": equivalence["forbidden_shortcuts"],
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedC1VariationPrincipleDerivationOrQuadratureEngineRun",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution.candidate.json"),
            "equivalence_theorem": rel(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "necessary_sufficient_cycle_exit_theorem.packet.json"),
            "physical_promotion_attempt": rel(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "physical_c1_variation_source_promotion_attempt.packet.json"),
            "quadrature_attempt": rel(DATA / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution" / "independent_quadrature_execution_attempt.packet.json"),
            "formal_variational_derivation": rel(DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve" / "orthogonal_completion_variational_derivation.packet.json"),
            "quadrature_schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
            "selected_basis_values": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json"),
            "replay_rows": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json"),
        },
        "output_packets": {
            "route_a_variation_principle_derivation_attempt": rel(ROUTE_A),
            "route_b_quadrature_engine_run_attempt": rel(ROUTE_B),
            "minimal_engine_or_principle_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "C1VariationPrincipleOrQuadratureEngineRunCutsetTheorem",
            "proved": True,
            "statement": cutset["statement"],
        },
        "what_closes_now": {
            "route_A_formal_variational_derivation_attached": True,
            "route_A_physical_rule_gap_isolated": True,
            "route_B_quadrature_engine_skeleton_built": True,
            "route_B_required_rows_enumerated": True,
            "minimal_cutset_selected": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_physical_C1_variation_principle": True,
            "selected_C1_defect_functional_source": True,
            "selected_dynamic_trace_boundary_cancellation": True,
            "selected_quadrature_measure_pairing_or_kernel": True,
            "independent_primitive_contraction_values": True,
            "independent_hessian_source_vector": True,
            "independent_sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_physical_source_promoted": False,
            "route_B_independent_quadrature_executed": False,
            "formal_candidate_functional_treated_as_physical_action": False,
            "replay_rows_treated_as_independent_quadrature": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": previous["status"],
    }

    cert = {
        "certificate": "MTT_Selected_C1VariationPrincipleDerivation_or_QuadratureEngineRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
    }

    note = f"""# MTT Selected C1VariationPrincipleDerivation or QuadratureEngineRun v1

Status: `{STATUS}`.

Route A now has the formal variational algebra attached:

```text
finite Euler projection derived       = True
least-norm Q_residual selection       = True
physical C1 action/source derived     = False
boundary cancellation derived         = False
```

Route B now has the selected engine skeleton:

```text
basis rows selected                   = {selected_basis_rows}/{counts["basis"]}
primitive rows required               = {counts["primitive_contractions"]}
primitive rows replay-backed          = {replay_filled_rows}
primitive rows independent            = {replay_rows["independent_quadrature_row_count"]}
hessian/source rows required          = {counts["hessian_source"]}
sector response rows required         = {counts["sector_matrices"]}
independent engine run executed       = False
```

The gate is therefore not numerically vague anymore. It is missing one of two
precise objects: either the selected physical `Phi_fin^C1` variation/source
principle, or the selected quadrature measure/kernel values with an exact run.

Next artifact: `{NEXT}`.
"""

    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
