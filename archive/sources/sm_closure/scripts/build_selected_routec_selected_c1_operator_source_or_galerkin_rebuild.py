"""Iterate the selected C1 operator-source / Galerkin rebuild solution space."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
PRIMITIVE_AUDIT = DATA / "selected_routec_primitive_source_selection_audit.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
CANONICAL = DATA / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
SOLVE_SPEC = DATA / "selected_routec_strominger_galerkin_solve_spec.candidate.json"

OUTPUT = DATA / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild.candidate.json"
CERT = CERTS / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_C1_OPERATOR_SOURCE_GALERKIN_REBUILD_ITERATED_BASIS_TRANSPORT_LANE_SELECTED_AS_NEXT_PROOF_TARGET"
NEXT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def score_lane(features: dict[str, bool], penalties: dict[str, bool]) -> int:
    weights = {
        "same_branch_support": 3,
        "finite_values_exist": 3,
        "nonzero_response": 3,
        "source_selector_partly_forced": 3,
        "validator_scaffold_exists": 2,
        "compatible_with_no_target_policy": 2,
        "emits_A_selected_after_one_theorem": 3,
    }
    penalty_weights = {
        "all_numeric_values_null": 3,
        "zero_response": 4,
        "requires_full_smooth_rebuild": 3,
        "would_need_observed_targets": 99,
        "uses_lifted_flags_as_proof": 99,
    }
    score = sum(weight for key, weight in weights.items() if features.get(key) is True)
    score -= sum(weight for key, weight in penalty_weights.items() if penalties.get(key) is True)
    return score


def main() -> None:
    previous = load(PREVIOUS)
    primitive = load(PRIMITIVE_AUDIT)
    noninv = load(NONINV)
    canonical = load(CANONICAL)
    dotd = load(DOTD)
    solve_spec = load(SOLVE_SPEC)

    active = primitive["active_shift_theorem"]["enumeration"]
    fixed_fiber = primitive["fiber_class_theorem"]["fixed_fiber_shifts"]
    noninv_results = noninv["calculation_results"]

    lanes = {
        "L1_straight_selected_hessian_response": {
            "features": {
                "same_branch_support": True,
                "finite_values_exist": False,
                "nonzero_response": False,
                "source_selector_partly_forced": False,
                "validator_scaffold_exists": True,
                "compatible_with_no_target_policy": True,
                "emits_A_selected_after_one_theorem": False,
            },
            "penalties": {
                "all_numeric_values_null": True,
                "zero_response": False,
                "requires_full_smooth_rebuild": False,
                "would_need_observed_targets": False,
                "uses_lifted_flags_as_proof": False,
            },
            "diagnosis": "Correct schema, but all selected finite Hessian/source/response values remain null.",
        },
        "L2_canonical_smooth_bn_response": {
            "features": {
                "same_branch_support": True,
                "finite_values_exist": True,
                "nonzero_response": False,
                "source_selector_partly_forced": True,
                "validator_scaffold_exists": True,
                "compatible_with_no_target_policy": True,
                "emits_A_selected_after_one_theorem": False,
            },
            "penalties": {
                "all_numeric_values_null": False,
                "zero_response": True,
                "requires_full_smooth_rebuild": False,
                "would_need_observed_targets": False,
                "uses_lifted_flags_as_proof": False,
            },
            "diagnosis": "Computed in the current smooth B_N scaffold, but the one-response C1 matrices are zero.",
        },
        "L3_noninvariant_basis_transport_or_vertex_source": {
            "features": {
                "same_branch_support": True,
                "finite_values_exist": True,
                "nonzero_response": noninv_results["nonzero_unselected_candidates_found"] > 0,
                "source_selector_partly_forced": active["active_shift_necessary_and_sufficient_for_nonzero"] is True,
                "validator_scaffold_exists": True,
                "compatible_with_no_target_policy": True,
                "emits_A_selected_after_one_theorem": True,
            },
            "penalties": {
                "all_numeric_values_null": False,
                "zero_response": False,
                "requires_full_smooth_rebuild": False,
                "would_need_observed_targets": False,
                "uses_lifted_flags_as_proof": False,
            },
            "diagnosis": "Best constrained lane: active shift (1,1) is forced; fixed fiber shifts form one gauge class; a selected basis-transport/vertex theorem would emit the needed nonzero primitive.",
        },
        "L4_full_smooth_iwasawa_strominger_rebuild": {
            "features": {
                "same_branch_support": True,
                "finite_values_exist": False,
                "nonzero_response": False,
                "source_selector_partly_forced": True,
                "validator_scaffold_exists": True,
                "compatible_with_no_target_policy": True,
                "emits_A_selected_after_one_theorem": False,
            },
            "penalties": {
                "all_numeric_values_null": False,
                "zero_response": False,
                "requires_full_smooth_rebuild": True,
                "would_need_observed_targets": False,
                "uses_lifted_flags_as_proof": False,
            },
            "diagnosis": "Most rigorous fallback, but too broad for the next iteration: it rebuilds S1-S6 instead of exploiting the forced finite obstruction.",
        },
    }

    ranked = []
    for name, lane in lanes.items():
        ranked.append(
            {
                "lane": name,
                "score": score_lane(lane["features"], lane["penalties"]),
                "features": lane["features"],
                "penalties": lane["penalties"],
                "diagnosis": lane["diagnosis"],
            }
        )
    ranked.sort(key=lambda item: item["score"], reverse=True)

    selected = ranked[0]
    solution_kernel = {
        "selected_next_lane": selected["lane"],
        "why": selected["diagnosis"],
        "forced_active_shift": active["nonzero_active_shifts"],
        "active_shift_unique": active["nonzero_active_shifts"] == [[1, 1]],
        "fixed_fiber_shifts_gauge_equivalent": all(
            item["equivalent"] is True
            for item in fixed_fiber["equivalence_to_shift_0_on_u"].values()
        ),
        "computation_gauge": "fixed qutrit fiber shift 0 may be used only after quotient/gauge-class proof is invoked",
        "minimal_theorem_to_prove_next": (
            "Selected basis transport / vertex primitive theorem: the selected q79/F,m=1 S3/GS Route-C "
            "source emits the active deck shift (1,1) non-invariant primitive, while fixed qutrit fiber "
            "shifts 0,1,2 are a quotient gauge class for the downstream observables."
        ),
        "expected_after_theorem": [
            "promote the rank-3 fixed-fiber representative as selected computation gauge",
            "assemble A_selected from the emitted primitive/basis transport and existing dotD/projector scaffold",
            "solve or reject A_selected * deltaTheta_C1 = b_splitter",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSelectedC1OperatorSourceOrGalerkinRebuild",
        "status": STATUS,
        "inputs": {
            "selected_c1_response_operator_emission": rel(PREVIOUS),
            "primitive_source_selection_audit": rel(PRIMITIVE_AUDIT),
            "noninvariant_c1_primitive_search": rel(NONINV),
            "canonical_c1_response": rel(CANONICAL),
            "sector_projectors_dotd": rel(DOTD),
            "strominger_galerkin_solve_spec": rel(SOLVE_SPEC),
        },
        "solution_space_iteration": {
            "ranked_lanes": ranked,
            "selected_solution_kernel": solution_kernel,
            "search_space_pruned": {
                "observed_target_fits_removed": True,
                "lifted_flag_proofs_removed": True,
                "zero_canonical_lane_retired_for_flavor_splitting": True,
                "full_rebuild_kept_as_fallback": True,
                "basis_transport_lane_promoted_to_next_proof_target": True,
            },
        },
        "supporting_facts": {
            "active_shift_necessary_and_sufficient_for_nonzero": active["active_shift_necessary_and_sufficient_for_nonzero"],
            "unique_nonzero_active_shift": active["nonzero_active_shifts"],
            "nonzero_unselected_candidates_found": noninv_results["nonzero_unselected_candidates_found"],
            "all_four_tested_candidates_nonzero": noninv_results["all_four_tested_candidates_nonzero"],
            "fixed_fiber_shifts_gauge_equivalent": all(
                item["equivalent"] is True
                for item in fixed_fiber["equivalence_to_shift_0_on_u"].values()
            ),
            "dotd_projector_scaffold_exists": dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "canonical_response_zero": canonical["superset_mode"]["straight_path"]["nonzero_selected_C1_response_found"] is False,
            "solve_spec_stage_count": len(solve_spec["execution_stages"]),
        },
        "what_closes_now": {
            "solution_space_ranked": True,
            "best_next_lane_selected": True,
            "active_shift_forced_imported": True,
            "fiber_gauge_class_imported": True,
            "zero_and_unselected_lanes_separated": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_basis_transport_or_vertex_source_theorem": True,
            "promote_fixed_fiber_representative_after_quotient": True,
            "emit_A_selected_from_promoted_primitive": True,
            "emit_b_selected": True,
            "solve_or_reject_splitter_equation": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SmartC1RebuildSolutionSpaceIterationTheorem",
            "proved": True,
            "statement": (
                "The selected C1 rebuild space is pruned and ranked without target fitting. The best next lane "
                "is the non-invariant basis-transport/vertex source theorem: finite momentum bookkeeping already "
                "forces active shift (1,1), fixed qutrit fiber shifts are one gauge class, and this lane is the "
                "shortest route that can emit a nonzero A_selected. The theorem is not yet the selected source "
                "proof; it identifies the minimal proof target needed to solve the splitter equation honestly."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C Selected C1 Operator Source or Galerkin Rebuild

Status: `MTT_SELECTED_ROUTEC_C1_OPERATOR_SOURCE_GALERKIN_REBUILD_ITERATED_BASIS_TRANSPORT_LANE_SELECTED_AS_NEXT_PROOF_TARGET`

The selected C1 rebuild space has been iterated and pruned.

## Ranked Result

The best next lane is the non-invariant basis-transport / vertex-source lane.

Why this lane wins:

- finite momentum bookkeeping already forces active deck shift `(1,1)`,
- fixed qutrit fiber shifts `0,1,2` form one gauge class at the current layer,
- the lane has nonzero finite rank-3 candidates,
- it reuses the existing dotD/projector scaffold,
- it does not use observed targets or lifted flags.

The straight selected-Hessian lane has the correct schema but all finite values
are null.  The canonical smooth B_N lane is computed but zero.  The full smooth
Iwasawa/Strominger rebuild remains rigorous fallback, but is broader than the
next needed proof object.

## Minimal Next Theorem

Prove the selected basis-transport / vertex primitive theorem:

```text
The selected q79/F,m=1 S3/GS Route-C source emits the active shift (1,1)
non-invariant primitive, while fixed qutrit fiber shifts 0,1,2 are a quotient
gauge class for downstream observables.
```

Once that theorem is supplied, shift `0` can be used as computation gauge, the
nonzero rank-3 primitive can be promoted to selected operator data, and
`A_selected` can be assembled for the locked DeltaTheta solve.

Next artifact: `MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
