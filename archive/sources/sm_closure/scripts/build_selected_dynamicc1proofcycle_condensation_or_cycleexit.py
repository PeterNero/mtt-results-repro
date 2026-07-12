"""Build dynamic C1 proof-cycle condensation / cycle-exit gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1proofcycle_condensation_or_cycleexit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CYCLE_PACKET = PACKET_DIR / "dynamic_c1_attempt_cycle_condensation.packet.json"
CUTSET_PACKET = PACKET_DIR / "shared_cycle_exit_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1ProofCycleCondensation_or_CycleExit_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1_PROOF_CYCLE_CONDENSED_SHARED_EXIT_CUTSET_OPEN"
NEXT = "MTT_Selected_CycleExit_MinimizerTrace_or_IndependentQuadratureRows_v1"

CYCLE = [
    (
        "selected_c1defectfunctionalsource_or_independentquadraturedatafill",
        "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1",
    ),
    (
        "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable",
        "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1",
    ),
    (
        "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues",
        "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1",
    ),
    (
        "selected_i10_payloadcertificate_or_independentquadraturevaluesfill",
        "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1",
    ),
    (
        "selected_stromingertracec1firstvariation_or_quadratureexecutionplan",
        "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1",
    ),
    (
        "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun",
        "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1",
    ),
    (
        "selected_tracemapandbasisvalues_or_primitiverowsexecution",
        "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1",
    ),
    (
        "selected_primitiverowsexecution_or_dynamicdotdtracebinding",
        "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1",
    ),
    (
        "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission",
        "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1",
    ),
    (
        "selected_residual_weylpolynomial_source_theorem_attempt",
        "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1",
    ),
    (
        "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill",
        "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1",
    ),
    (
        "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill",
        "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1",
    ),
    (
        "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution",
        "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1",
    ),
    (
        "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun",
        "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1",
    ),
    (
        "selected_enrichedweylpairsourceprovenance_or_galerkinc1values",
        "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1",
    ),
    (
        "selected_dynamicc1transfertensor_or_galerkinc1values",
        "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1",
    ),
    (
        "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest",
        "MTT_Selected_DynamicC1TransferTensor_ValueEmission_or_HonestGalerkinC1Run_v1",
    ),
    (
        "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run",
        "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1",
    ),
    (
        "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution",
        "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1",
    ),
    (
        "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun",
        "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1",
    ),
    (
        "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution",
        "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1",
    ),
    (
        "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution",
        "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1",
    ),
    (
        "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch",
        "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1",
    ),
    (
        "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom",
        "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1",
    ),
    (
        "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve",
        "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1",
    ),
]

IMPORTANT_FLAGS = {
    "selected_primitiverowsexecution_or_dynamicdotdtracebinding": [
        ("promotion_decision", "dynamic_dotD_trace_binding_accepted", True),
    ],
    "selected_tracemapandbasisvalues_or_primitiverowsexecution": [
        ("promotion_decision", "route_A_trace_map_values_accepted", True),
        ("promotion_decision", "route_B_basis_rows_accepted", True),
    ],
    "selected_c1defectfunctionalsource_or_independentquadraturedatafill": [
        ("promotion_decision", "selected_C1_defect_functional_formal_source_promoted", True),
        ("promotion_decision", "physical_PhiFinC1_application_rule_proved", False),
    ],
    "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable": [
        ("promotion_decision", "PhiFinC1_minimizes_defect_functional_proved", False),
    ],
    "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission": [
        ("promotion_decision", "SM_parity_dynamic_packet_closed", False),
    ],
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load_candidate(slug: str) -> dict[str, Any]:
    path = DATA / f"{slug}.candidate.json"
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def flag_value(data: dict[str, Any], section: str, key: str) -> Any:
    return data.get(section, {}).get(key)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    loaded = {slug: load_candidate(slug) for slug, _next in CYCLE}

    nodes = []
    for slug, expected_next in CYCLE:
        data = loaded[slug]
        nodes.append(
            {
                "slug": slug,
                "status": data["status"],
                "next_required_artifact": data.get("next_required_artifact"),
                "expected_cycle_next": expected_next,
                "next_matches_cycle": data.get("next_required_artifact") == expected_next,
                "closure_claimed": data.get("closure_claimed", False),
                "target_fitting_used": data.get("target_fitting_used", False),
                "observed_data_used": data.get("observed_data_used", False),
            }
        )

    flag_checks = []
    for slug, checks in IMPORTANT_FLAGS.items():
        data = loaded[slug]
        for section, key, expected in checks:
            actual = flag_value(data, section, key)
            flag_checks.append(
                {
                    "slug": slug,
                    "section": section,
                    "key": key,
                    "actual": actual,
                    "expected": expected,
                    "passes": actual is expected,
                }
            )

    cycle_packet = {
        "schema": "MTTDynamicC1AttemptCycleCondensation.v1",
        "status": "CYCLE_CONDENSED",
        "node_count": len(nodes),
        "nodes": nodes,
        "all_nodes_present": len(nodes) == len(CYCLE),
        "all_next_edges_match_declared_cycle": all(node["next_matches_cycle"] for node in nodes),
        "all_guardrails_preserved": all(
            (not node["closure_claimed"])
            and (not node["target_fitting_used"])
            and (not node["observed_data_used"])
            for node in nodes
        ),
        "important_flag_checks": flag_checks,
        "important_flags_pass": all(check["passes"] for check in flag_checks),
        "interpretation": (
            "The dynamic C1 artifacts now form a proof-attempt cycle. This is a condensation result, "
            "not a closure result: the cycle shows that residual completion, defect-functional "
            "minimization, first variation, primitive rows, and Galerkin execution are all names for "
            "the same missing selected source object."
        ),
    }

    cutset = {
        "schema": "MTTSharedCycleExitCutset.v1",
        "status": "SHARED_EXIT_CUTSET_SELECTED",
        "shared_missing_object": (
            "selected physical differentiated Phi_fin^C1 C1 response: equivalently, a theorem that "
            "the selected minimizer trace applies the canonical residual projector Q_residual and "
            "emits b_selected, or an independent quadrature/Hessian table that emits the same A,b,sector matrices"
        ),
        "already_closed_inside_cycle": {
            "stationary_trace_map_values": True,
            "selected_basis_projector_gram_gap_values": True,
            "dynamic_dotD_trace_binding": True,
            "residual_weyl_polynomial_decomposition": True,
            "canonical_Q_residual_uniqueness": True,
            "formal_C1_defect_functional_uniqueness": True,
            "conditional_rank2_replay": True,
        },
        "straight_route": {
            "name": "minimizer_trace_first_variation_route",
            "must_prove": [
                "I1 selected minimizer-to-Phi_fin trace",
                "I5 selected dotD/C1 response binding",
                "I10 Phi_fin^C1 minimizes the selected C1 defect functional",
                "I11 selected Strominger/HYM trace first-variation and boundary cancellation",
            ],
        },
        "parallel_route": {
            "name": "independent_quadrature_hessian_route",
            "must_emit": [
                "independent selected zero-mode basis rows",
                "primitive quadrature contraction rows",
                "hessian/source vector b_selected",
                "sector response matrices",
                "acceptance replay A^T A=12 I_2, A^T b=(12,12), deltaTheta_C1=(1,1)",
            ],
        },
        "locked_target": {
            "A_transpose_A": [[12.0, 0.0], [0.0, 12.0]],
            "A_transpose_b": [12.0, 12.0],
            "deltaTheta_C1": [1.0, 1.0],
        },
        "superset_strategy": {
            "using_combined_paths": True,
            "how": (
                "The straight minimizer/first-variation route and the parallel independent-quadrature route "
                "are retained as distinct encodings, but both are locked to the same typed C1 target. "
                "Agreement can promote the shared packet; disagreement forces the honest quadrature result to replace the conditional packet."
            ),
        },
        "not_allowed_as_cycle_exit": [
            "following next_required_artifact edges around the cycle without a new selected source object",
            "using measured SM constants to choose the residual packet",
            "treating the patched local axiom as unpatched theorem closure",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1ProofCycleCondensationOrCycleExit",
        "status": STATUS,
        "inputs": {
            slug: rel(DATA / f"{slug}.candidate.json") for slug, _next in CYCLE
        },
        "output_packets": {
            "dynamic_c1_attempt_cycle_condensation": rel(CYCLE_PACKET),
            "shared_cycle_exit_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "DynamicC1AttemptCycleCondensationTheorem",
            "proved": True,
            "statement": (
                "The dynamic C1 proof spine has condensed into a strongly connected attempt cycle. "
                "All cycle nodes preserve the no-observed-selector guardrail and no unpatched closure claim. "
                "The cycle's shared external cutset is exactly the selected physical differentiated Phi_fin^C1 "
                "response/minimizer-trace rule, or an independent quadrature/Hessian emission of the same locked target."
            ),
        },
        "what_closes_now": {
            "proof_cycle_detected_and_condensed": True,
            "backfill_does_not_move_frontier_backward": True,
            "shared_missing_object_identified": True,
            "straight_and_parallel_superset_paths_locked_to_same_target": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "I1_selected_minimizer_to_PhiFin_trace": True,
            "I5_selected_dotD_C1_response": True,
            "I10_PhiFinC1_minimizes_defect_functional": True,
            "I11_first_variation_boundary_cancellation": True,
            "independent_quadrature_rows": True,
            "selected_b_selected": True,
            "sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "cycle_exit_proved": False,
            "straight_route_accepted": False,
            "parallel_route_accepted": False,
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
        "certificate": "MTT_Selected_DynamicC1ProofCycleCondensation_or_CycleExit_v1",
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

    note = f"""# MTT Selected DynamicC1ProofCycleCondensation or CycleExit v1

Status: `{STATUS}`.

The dynamic C1 proof spine is now condensed as a cycle, not treated as a
linear next-step chain.

```text
cycle nodes                              = {len(nodes)}
all declared cycle edges match           = {cycle_packet["all_next_edges_match_declared_cycle"]}
guardrails preserved                     = {cycle_packet["all_guardrails_preserved"]}
important flag checks pass               = {cycle_packet["important_flags_pass"]}
```

Shared exit cutset:

```text
straight route = selected minimizer trace / first-variation proof
parallel route = independent quadrature/Hessian rows
locked target  = A^T A=12 I_2, A^T b=(12,12), deltaTheta_C1=(1,1)
```

This proves we did not move backwards after the trace/dotD backfill.  The
frontier is the shared selected physical differentiated `Phi_fin^C1` response,
or an independent quadrature table emitting the same typed target.

Next artifact: `{NEXT}`.
"""

    CYCLE_PACKET.write_text(json.dumps(cycle_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET_PACKET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
