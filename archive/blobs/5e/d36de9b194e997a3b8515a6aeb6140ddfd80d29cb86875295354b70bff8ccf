"""Attack derivation of the local DifferentiatedPhiFinC1 source axiom."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_differentiatedphifinc1_axiom_derivation_attempt_or_minimalobstruction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_unpatched_clause_attack.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_galerkin_attack.packet.json"
OBSTRUCTION = PACKET_DIR / "minimal_derivation_obstruction.packet.json"
DECISION = PACKET_DIR / "axiom_derivation_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedPhiFinC1_AxiomDerivationAttempt_or_MinimalObstruction_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_AXIOM_DERIVATION_ATTEMPT_BUILT_MINIMAL_OBSTRUCTION_OPEN"
NEXT = "MTT_Selected_PhiFinC1PhysicalVariationSourceTheorem_or_IndependentGalerkinC1Export_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_true(values: list[bool]) -> bool:
    return all(value is True for value in values)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    source_attempt = load(
        DATA
        / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion"
        / "unpatched_source_rule_derivation_attempt.packet.json"
    )
    local_axiom_closure = load(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit.candidate.json")
    physical_attempt = load(
        DATA
        / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
        / "physical_c1_variation_source_promotion_attempt.packet.json"
    )
    cycle_exit = load(
        DATA
        / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
        / "necessary_sufficient_cycle_exit_theorem.packet.json"
    )
    current_physical = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "current_physical_boundary_firstvariation_attempt.packet.json"
    )
    conditional_physical = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "conditional_physical_source_emission_witness.packet.json"
    )
    galerkin_replay = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "first_galerkin_replay_result.packet.json"
    )
    primitive_terms = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "primitive_contraction_terms.packet.json"
    )
    hessian = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "hessian_source_vector.packet.json"
    )
    zero_mode = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "zero_mode_basis.packet.json"
    )
    sector = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "sector_response_matrices.packet.json"
    )

    required_clauses = source_attempt["required_clauses"]
    route_a_clause_status = {
        name: {
            "closed_now": clause["closed_now"],
            "conditional_witness_value": clause["conditional_witness_value"],
            "current_packet_value": clause["current_packet_value"],
        }
        for name, clause in required_clauses.items()
    }
    route_a_closed_now = all_true([entry["closed_now"] for entry in route_a_clause_status.values()])
    route_a_would_close_if_theorem_supplied = all_true(
        [entry["conditional_witness_value"] for entry in route_a_clause_status.values()]
    )
    physical_emissions = current_physical["current_route_A_emissions"]
    conditional_emissions = {
        key: conditional_physical.get(key, value)
        for key, value in {
            "physical_action_identity": conditional_physical["physical_first_variation_identity"],
            "physical_measure_equals_trace_frobenius_pairing": conditional_physical[
                "physical_measure_equals_trace_frobenius_pairing"
            ],
            "no_extra_physical_boundary_or_source_term": conditional_physical[
                "no_extra_physical_boundary_or_source_term"
            ],
            "phase_R_Z_source_selection": conditional_physical["phase_R_Z_source_selection"],
            "shift_R_X_source_selection": conditional_physical["shift_R_X_source_selection"],
            "same_source_b_selected_emission": conditional_physical["same_source_b_selected_emission"],
        }.items()
    }

    route_a = {
        "schema": "MTTRouteAUnpatchedPhiFinC1AxiomClauseAttack.v1",
        "status": "ROUTE_A_ATTACK_SUPPORT_COMPLETE_SOURCE_THEOREM_NOT_DERIVED",
        "theorem_target": "SelectedPhiFinC1PhysicalVariationSourceTheorem",
        "closed_support": source_attempt["closed_support"],
        "required_axiom_clauses": route_a_clause_status,
        "current_route_A_emissions": physical_emissions,
        "conditional_route_A_emissions": conditional_emissions,
        "route_A_closed_now": route_a_closed_now,
        "route_A_would_close_if_theorem_supplied": route_a_would_close_if_theorem_supplied,
        "new_derivation_found_now": False,
        "why_not_derived": [
            "The current corpus does not yet identify the physical C1 action with the C1DefectLeakageFunctional.",
            "The selected admissible differentiated Phi_fin^C1 variation class is not emitted as a theorem.",
            "Boundary cancellation is algebraically supported but not promoted for the selected dynamic trace.",
            "b_selected is still replay/contract data, not a same-source physical Hessian emission.",
        ],
        "minimal_route_A_statement_to_prove": source_attempt["minimal_statement_to_prove"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b_independence_flags = {
        "strict_replay_passes": galerkin_replay["strict_replay_passes"],
        "honest_independent_galerkin_execution_passes": galerkin_replay[
            "honest_independent_galerkin_execution_passes"
        ],
        "zero_mode_selected_source_verified": zero_mode["selected_source_verified"],
        "primitive_terms_selected_source_verified": primitive_terms["selected_source_verified"],
        "primitive_terms_computed_from_independent_galerkin_quadrature": primitive_terms[
            "computed_from_independent_galerkin_quadrature"
        ],
        "b_selected_emitted_by_independent_hessian": hessian["b_selected_emitted_by_independent_hessian"],
        "sector_matrices_emitted_independently": sector["independent_sector_matrices_emitted"],
    }
    route_b_closed_now = all_true(
        [
            route_b_independence_flags["honest_independent_galerkin_execution_passes"],
            route_b_independence_flags["zero_mode_selected_source_verified"],
            route_b_independence_flags["primitive_terms_selected_source_verified"],
            route_b_independence_flags["primitive_terms_computed_from_independent_galerkin_quadrature"],
            route_b_independence_flags["b_selected_emitted_by_independent_hessian"],
            route_b_independence_flags["sector_matrices_emitted_independently"],
        ]
    )

    route_b = {
        "schema": "MTTRouteBIndependentGalerkinAxiomReplacementAttack.v1",
        "status": "ROUTE_B_STRICT_REPLAY_PASSES_BUT_INDEPENDENT_SELECTION_OPEN",
        "cycle_exit_route_B_sufficient_if": cycle_exit["route_B_sufficient_if"],
        "independence_flags": route_b_independence_flags,
        "locked_target": {
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "b_norm_sq": hessian["b_norm_sq"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "passes_locked_target": True,
        },
        "route_B_closed_now": route_b_closed_now,
        "new_independent_execution_found_now": False,
        "why_not_independent": galerkin_replay["why_independent_execution_not_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    minimal_obstruction = {
        "schema": "MTTMinimalPhiFinC1AxiomDerivationObstruction.v1",
        "status": "MINIMAL_OBSTRUCTION_IS_SELECTED_PHYSICAL_SOURCE_BINDING_NOT_LINEAR_ALGEBRA",
        "not_blockers": {
            "qutrit_weyl_carrier": source_attempt["closed_support"]["selected_qutrit_weyl_carrier"],
            "static_sector_routing": source_attempt["closed_support"]["selected_static_routes"],
            "trace_transfer_normalization": source_attempt["closed_support"]["selected_trace_transfer_normalization"],
            "alpha1_dotD_driver": source_attempt["closed_support"]["alpha1_dotD_driver_verified"],
            "canonical_Q_residual": source_attempt["closed_support"]["canonical_Q_residual_available"],
            "least_norm_completion": source_attempt["closed_support"]["least_norm_completion_selects_Q_residual"],
            "locked_linear_algebra": cycle_exit["locked_target"]["passes_locked_target"],
        },
        "actual_obstruction": (
            "A same-source physical selection theorem must bind differentiated Phi_fin^C1 to the "
            "C1DefectLeakageFunctional and its trace/Frobenius residual projector, including boundary "
            "cancellation and b_selected emission; otherwise an independent selected Galerkin/Hessian "
            "execution must replace the local axiom."
        ),
        "minimal_new_lemma": {
            "name": "SelectedPhiFinC1PhysicalVariationSourceTheorem",
            "statement": source_attempt["minimal_statement_to_prove"],
            "would_derive_local_axiom": True,
            "currently_proved": False,
        },
        "countermodel_guard": (
            "The replay packet supplies exact values under the residual-projector contract, so it is a "
            "model of patched closure. It is not a model of unpatched derivation because the physical "
            "action/source binding clauses are false in the current packets."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPhiFinC1AxiomDerivationDecision.v1",
        "status": "AXIOM_NOT_DERIVED_YET_MINIMAL_PROOF_TARGET_IDENTIFIED",
        "local_patched_dynamic_C1_closed": local_axiom_closure["closure_decision"][
            "patched_dynamic_C1_packet_closed"
        ],
        "unpatched_source_axiom_derived_now": False,
        "route_A_closed_now": route_a_closed_now,
        "route_B_closed_now": route_b_closed_now,
        "honest_galerkin_independent": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "best_next_move": NEXT,
        "superset_strategy": {
            "mode": "two legal paths retained under one locked target",
            "route_A": "derive physical source rule for differentiated Phi_fin^C1",
            "route_B": "independent selected Galerkin/Hessian export",
            "locked_target": cycle_exit["locked_target"],
            "paths_used_as_free_parameters": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (OBSTRUCTION, minimal_obstruction),
        (DECISION, decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDifferentiatedPhiFinC1AxiomDerivationAttemptOrMinimalObstruction",
        "status": STATUS,
        "inputs": {
            "unpatched_source_rule_attempt": rel(
                DATA
                / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion"
                / "unpatched_source_rule_derivation_attempt.packet.json"
            ),
            "local_axiom_closure": rel(
                DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit.candidate.json"
            ),
            "physical_source_attempt": rel(
                DATA
                / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
                / "physical_c1_variation_source_promotion_attempt.packet.json"
            ),
            "cycle_exit_theorem": rel(
                DATA
                / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
                / "necessary_sufficient_cycle_exit_theorem.packet.json"
            ),
            "galerkin_replay_result": rel(
                DATA
                / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
                / "first_galerkin_replay_result.packet.json"
            ),
        },
        "output_packets": {
            "route_a_unpatched_clause_attack": rel(ROUTE_A),
            "route_b_independent_galerkin_attack": rel(ROUTE_B),
            "minimal_derivation_obstruction": rel(OBSTRUCTION),
            "axiom_derivation_decision": rel(DECISION),
        },
        "theorem_attempt": {
            "name": "DifferentiatedPhiFinC1ResidualProjectorAxiomDerivationAttempt",
            "proved": False,
            "result": "minimal obstruction identified",
            "derived_axiom_now": False,
        },
        "what_was_achieved": {
            "route_A_attacked": True,
            "route_B_attacked": True,
            "minimal_obstruction_identified": True,
            "values_and_linear_algebra_ruled_out_as_blockers": True,
            "local_axiom_closure_preserved": True,
        },
        "what_remains_open": {
            "selected_phifinc1_physical_variation_source_theorem": True,
            "selected_admissible_variations_and_boundary_cancellation": True,
            "same_source_b_selected_emission": True,
            "independent_selected_galerkin_hessian_export": True,
            "true_SM_equivalence_without_axiom": True,
            "no_knob_flavor_constants": True,
        },
        "closure_decision": {
            "local_patched_dynamic_C1_closed": decision["local_patched_dynamic_C1_closed"],
            "unpatched_source_axiom_derived_now": False,
            "route_A_closed_now": route_a_closed_now,
            "route_B_closed_now": route_b_closed_now,
            "global_closure_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedPhiFinC1_AxiomDerivationAttempt_or_MinimalObstruction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_A_closed_now": route_a_closed_now,
        "route_B_closed_now": route_b_closed_now,
        "unpatched_source_axiom_derived_now": False,
        "minimal_obstruction_identified": True,
        "local_patched_dynamic_C1_closed": decision["local_patched_dynamic_C1_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedPhiFinC1 Axiom Derivation Attempt or Minimal Obstruction v1

Status: `{STATUS}`.

This artifact tries to derive the local
`DifferentiatedPhiFinC1ResidualProjectorAxiom` from the current unpatched
source packets.

Result: the axiom is not derived yet. The obstruction is now minimal and
precise: selected physical source binding, not the C1 linear algebra.

Already closed support:

- selected qutrit Weyl carrier;
- static sector routing;
- finite trace transfer normalization;
- alpha1/dotD driver;
- canonical residual projector `Q_residual`;
- least-norm C1 completion;
- locked target algebra `A^T A=12 I_2`, `A^T b=(12,12)`, `deltaTheta_C1=(1,1)`.

Route A would derive the axiom if the
`SelectedPhiFinC1PhysicalVariationSourceTheorem` is proved. Its required
content is:

> {source_attempt["minimal_statement_to_prove"]}

Route B would avoid the axiom if an independent selected Galerkin/Hessian
export emits the zero-mode basis, primitive 3x3 contractions, sector response
matrices, `b_selected`, and exactness certificate from the same selected source.
The current replay passes the locked target, but is still contract/replay-backed.

So the next real target is:

`{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
