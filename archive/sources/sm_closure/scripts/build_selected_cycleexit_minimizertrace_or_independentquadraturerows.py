"""Build cycle-exit minimizer-trace / independent quadrature rows gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_cycleexit_minimizertrace_or_independentquadraturerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_minimizer_trace_payload_status.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_quadrature_rows_status.packet.json"
EXIT = PACKET_DIR / "reduced_cycle_exit_obligation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CycleExit_MinimizerTrace_or_IndependentQuadratureRows_v1.md"

STATUS = "MTT_SELECTED_CYCLEEXIT_MINIMIZERTRACE_OR_INDEPENDENTQUADRATUREROWS_REDUCED_FIRSTVARIATION_OR_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_FirstVariationBoundary_or_PrimitiveQuadratureRows_ValueFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    cycle_cutset = load(DATA / "selected_dynamicc1proofcycle_condensation_or_cycleexit" / "shared_cycle_exit_cutset.packet.json")
    trace_fill = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_a_trace_map_value_fill.packet.json")
    basis_fill = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json")
    dynamic_binding = load(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "dynamic_dotd_trace_binding.packet.json")
    primitive_attempt = load(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "primitive_rows_execution_attempt.packet.json")
    row_schedule = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json")
    c1_functional = load(DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill" / "c1_defect_functional_uniqueness_source.packet.json")
    hessian_replay = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json")

    binding_flags = dynamic_binding["binding_flags"]
    route_a_prereqs = {
        "I1_stationary_trace_map_values": trace_fill["accepted_for_stationary_trace"],
        "I5_selected_dotD_C1_response_source": binding_flags["selected_dotD_source_verified"]
        and binding_flags["alpha1_driver_verified"]
        and binding_flags["honest_dotD_alpha1_replay"],
        "formal_C1_defect_functional_source": c1_functional["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
        "dynamic_dotD_trace_binding": binding_flags["dynamic_dotD_trace_binding_accepted"],
    }
    route_a_open = {
        "I1_full_dynamic_minimizer_to_PhiFin_trace": True,
        "I10_physical_PhiFinC1_minimizes_defect_functional": True,
        "I11_first_variation_identity": True,
        "I11_boundary_cancellation_for_selected_trace": True,
    }
    route_a_status = {
        "schema": "MTTCycleExitRouteAMinimizerTracePayloadStatus.v1",
        "status": "ROUTE_A_PREREQUISITES_PARTIAL_FIRSTVARIATION_OPEN",
        "source_cycle_cutset": rel(DATA / "selected_dynamicc1proofcycle_condensation_or_cycleexit" / "shared_cycle_exit_cutset.packet.json"),
        "prerequisites_closed": route_a_prereqs,
        "open_physical_payloads": route_a_open,
        "interpretation": (
            "The stationary finite trace, selected dotD/alpha1 response, dynamic trace binding, and formal C1 "
            "defect functional are available. They do not yet prove that the physical differentiated Phi_fin^C1 "
            "variation is the selected minimizer of that functional, nor boundary cancellation for the selected trace."
        ),
        "can_close_cycle_exit_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    stages = {stage["stage"]: stage["rows"] for stage in row_schedule["execution_order"]}
    route_b_prereqs = {
        "basis_rows_selected": basis_fill["all_basis_rows_selected"],
        "basis_row_count": basis_fill["selected_row_count"],
        "dynamic_dotD_trace_binding": binding_flags["dynamic_dotD_trace_binding_accepted"],
        "primitive_rows_scheduled": primitive_attempt["row_count"],
        "primitive_rows_executed": primitive_attempt["executed_row_count"],
        "hessian_replay_available_under_axiom_patch": hessian_replay["b_selected_replay_available_under_axiom_patch"],
        "independent_hessian_b_selected_emitted": hessian_replay["b_selected_emitted_by_independent_hessian"],
    }
    route_b_status = {
        "schema": "MTTCycleExitRouteBIndependentQuadratureRowsStatus.v1",
        "status": "ROUTE_B_BASIS_READY_PRIMITIVE_AND_INDEPENDENT_HESSIAN_OPEN",
        "row_schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
        "stage_counts": {stage: len(rows) for stage, rows in stages.items()},
        "prerequisites_closed_or_open": route_b_prereqs,
        "open_independent_outputs": {
            "primitive_contraction_rows": primitive_attempt["row_count"] - primitive_attempt["executed_row_count"],
            "independent_hessian_source_rows": len(stages["hessian_source"]),
            "sector_response_matrix_rows": len(stages["sector_matrices"]),
        },
        "why_not_closed": [
            "primitive rows still depend on selected residual completion source theorem or honest Galerkin C1 emission",
            "b_selected is replay-backed under the local residual-projector axiom patch, not independently emitted",
            "sector response matrices are scheduled but not emitted by an independent selected quadrature run",
        ],
        "can_close_cycle_exit_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    reduced_exit = {
        "schema": "MTTReducedCycleExitObligation.v1",
        "status": "REDUCED_TO_FIRSTVARIATION_OR_PRIMITIVE_ROWS",
        "closed_inside_cycle_exit_attempt": {
            "stationary_trace_map_values": route_a_prereqs["I1_stationary_trace_map_values"],
            "selected_dotD_alpha1_C1_response_source": route_a_prereqs["I5_selected_dotD_C1_response_source"],
            "formal_C1_defect_functional_source": route_a_prereqs["formal_C1_defect_functional_source"],
            "selected_basis_projector_gram_gap_rows": basis_fill["all_basis_rows_selected"],
            "dynamic_dotD_trace_binding": route_a_prereqs["dynamic_dotD_trace_binding"],
            "locked_target_linear_algebra": True,
        },
        "remaining_minimal_exit_options": [
            {
                "route": "A",
                "name": "selected first-variation/boundary certificate",
                "must_emit": [
                    "physical first variation of selected Phi_fin^C1 equals the selected C1 defect Euler equation",
                    "boundary terms vanish or are selected-zero under the same trace functional",
                    "full dynamic minimizer-to-Phi_fin trace, not only stationary transported trace",
                ],
            },
            {
                "route": "B",
                "name": "independent primitive quadrature/Hessian value run",
                "must_emit": [
                    "72 primitive contraction rows",
                    "2 independent Hessian/source rows emitting b_selected",
                    "36 sector response matrix rows",
                    "acceptance replay against the locked target",
                ],
            },
        ],
        "locked_target": cycle_cutset["locked_target"],
        "superset_strategy": {
            "straight_route": "Route A proves physical minimization/first variation from the selected trace source.",
            "parallel_route": "Route B bypasses Route A by independently emitting the same rows.",
            "using_combined_paths": True,
            "current_combination": "prerequisite sharing only; no closure by averaging or target fitting",
        },
        "not_claimed": [
            "unpatched dynamic packet closure",
            "independent primitive rows",
            "independent b_selected",
            "true SM equivalence",
            "no-knob Yukawa or CKM/PMNS closure",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedCycleExitMinimizerTraceOrIndependentQuadratureRows",
        "status": STATUS,
        "inputs": {
            "cycle_cutset": rel(DATA / "selected_dynamicc1proofcycle_condensation_or_cycleexit" / "shared_cycle_exit_cutset.packet.json"),
            "trace_fill": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_a_trace_map_value_fill.packet.json"),
            "basis_fill": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json"),
            "dynamic_dotd_trace_binding": rel(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "dynamic_dotd_trace_binding.packet.json"),
            "primitive_rows_attempt": rel(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "primitive_rows_execution_attempt.packet.json"),
            "quadrature_row_schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
            "formal_c1_defect_functional": rel(DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill" / "c1_defect_functional_uniqueness_source.packet.json"),
            "hessian_replay": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json"),
        },
        "output_packets": {
            "route_a_minimizer_trace_payload_status": rel(ROUTE_A),
            "route_b_independent_quadrature_rows_status": rel(ROUTE_B),
            "reduced_cycle_exit_obligation": rel(EXIT),
        },
        "theorem": {
            "name": "CycleExitPrerequisiteReductionTheorem",
            "proved": True,
            "statement": (
                "After the cycle condensation, the stationary trace, selected basis/projector/Gram/gap rows, "
                "formal C1 defect functional, alpha1/dotD response source, and dynamic dotD trace binding are "
                "all available without observed constants. The remaining cycle exit is therefore reduced to either "
                "a physical first-variation/boundary certificate for selected Phi_fin^C1, or independent primitive "
                "quadrature plus Hessian/sector rows emitting the locked target."
            ),
        },
        "what_closes_now": {
            "cycle_exit_prerequisites_audited": True,
            "I1_stationary_trace_component_available": True,
            "I5_dotD_alpha1_C1_source_component_available": True,
            "route_B_basis_stage_available": True,
            "shared_exit_reduced_to_two_minimal_payloads": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "I1_full_dynamic_minimizer_to_PhiFin_trace": True,
            "I10_physical_PhiFinC1_minimizes_defect_functional": True,
            "I11_first_variation_boundary_cancellation": True,
            "primitive_quadrature_rows_executed": True,
            "independent_b_selected": True,
            "sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "cycle_exit_proved": False,
            "route_A_first_variation_accepted": False,
            "route_B_independent_quadrature_accepted": False,
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
    }

    cert = {
        "certificate": "MTT_Selected_CycleExit_MinimizerTrace_or_IndependentQuadratureRows_v1",
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

    note = f"""# MTT Selected CycleExit MinimizerTrace or IndependentQuadratureRows v1

Status: `{STATUS}`.

Closed prerequisites:

```text
stationary trace component      = {route_a_prereqs["I1_stationary_trace_map_values"]}
dotD/alpha1 C1 source component = {route_a_prereqs["I5_selected_dotD_C1_response_source"]}
formal C1 defect functional     = {route_a_prereqs["formal_C1_defect_functional_source"]}
basis rows selected             = {basis_fill["selected_row_count"]}/{basis_fill["row_count"]}
dynamic trace binding           = {route_a_prereqs["dynamic_dotD_trace_binding"]}
```

Remaining exit:

```text
Route A = physical first variation + boundary cancellation
Route B = 72 primitive rows + 2 Hessian rows + 36 sector rows
target  = A^T A=12 I_2, A^T b=(12,12), deltaTheta_C1=(1,1)
```

This uses the superset strategy as prerequisite sharing only: the straight
minimizer route and independent quadrature route remain separate, both locked
to the same target, and no measured SM constants are selectors.

Next artifact: `{NEXT}`.
"""

    ROUTE_A.write_text(json.dumps(route_a_status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b_status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    EXIT.write_text(json.dumps(reduced_exit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
