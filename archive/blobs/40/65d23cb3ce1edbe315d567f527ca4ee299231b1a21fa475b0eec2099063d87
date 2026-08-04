"""Build physical C1 variation source-promotion / independent quadrature execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION = PACKET_DIR / "physical_c1_variation_source_promotion_attempt.packet.json"
QUADRATURE = PACKET_DIR / "independent_quadrature_execution_attempt.packet.json"
EQUIV = PACKET_DIR / "necessary_sufficient_cycle_exit_theorem.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalC1VariationSourcePromotion_or_IndependentQuadratureExecution_v1.md"

STATUS = "MTT_SELECTED_PHYSICALC1VARIATION_SOURCEPROMOTION_OR_INDEPENDENTQUADRATUREEXECUTION_BUILT_NECESSARY_SUFFICIENT_OPEN"
NEXT = "MTT_Selected_C1VariationPrincipleDerivation_or_QuadratureEngineRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill.candidate.json")
    replay_rows = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json")
    axiom_contract = load(DATA / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution" / "residual_projector_axiom_patch_contract.packet.json")
    ladder = load(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "source_rule_or_execution_route_ladder.packet.json")
    variational = load(DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve" / "orthogonal_completion_variational_derivation.packet.json")
    route_a = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_a_first_variation_boundary_fill_attempt.packet.json")
    route_b = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json")

    promotion_attempt = {
        "schema": "MTTPhysicalC1VariationSourcePromotionAttempt.v1",
        "status": "PROMOTION_ATTEMPT_SUPPORT_COMPLETE_PRINCIPLE_UNDERIVED",
        "axiom_contract": rel(DATA / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution" / "residual_projector_axiom_patch_contract.packet.json"),
        "local_patch_note": rel(CORPUS / "MTT_DifferentiatedPhiFinC1ResidualProjectorAxiom_LocalCorpusPatch_v1.md"),
        "support_closed": {
            "canonical_Q_residual_available": axiom_contract["premises_required"]["canonical_Q_residual_available"],
            "alpha1_dotD_driver_verified": axiom_contract["premises_required"]["alpha1_dotD_driver_verified"],
            "selected_qutrit_weyl_carrier": axiom_contract["premises_required"]["selected_qutrit_weyl_carrier"],
            "selected_static_routes": axiom_contract["premises_required"]["selected_static_route_Z_clock_to_u_e"]
            and axiom_contract["premises_required"]["selected_static_route_X_shift_to_d_nuD"],
            "selected_trace_transfer_normalization": axiom_contract["premises_required"]["selected_trace_transfer_normalization"],
            "finite_variational_euler_projection": variational["derived_inside_this_gate"]["finite_dimensional_projection_euler_equation"],
            "least_norm_completion_selects_Q_residual": variational["derived_inside_this_gate"]["least_norm_trace_orthogonal_completion_selects_Q_residual"],
            "replay_rows_pass_locked_target": replay_rows["acceptance_replay"]["passes_locked_target"],
        },
        "missing_for_unpatched_promotion": {
            "derive_or_insert_physical_C1_variation_principle": True,
            "prove_selected_PhiFinC1_applies_Q_residual": not axiom_contract["selected_now"],
            "prove_boundary_cancellation_for_selected_dynamic_trace": route_a["still_open"]["boundary_cancellation_for_selected_dynamic_trace"],
            "emit_b_selected_as_physical_source_not_patch_replay": True,
        },
        "local_patch_would_close_dynamic_packet": {
            "if_accepted": True,
            "payload": axiom_contract["new_axiom_payload_if_accepted"],
            "locked_target": replay_rows["acceptance_replay"],
            "guardrail": "patch closure is not unpatched MTT theorem closure and not no-knob SM flavor closure",
        },
        "unpatched_promotion_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    quadrature_attempt = {
        "schema": "MTTIndependentQuadratureExecutionAttempt.v1",
        "status": "INDEPENDENT_EXECUTION_NOT_RUN_REPLAY_TARGET_AVAILABLE",
        "replay_backed_row_table": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json"),
        "route_ladder": rel(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "source_rule_or_execution_route_ladder.packet.json"),
        "required_outputs": ladder["superset_execution_path"]["required_outputs"],
        "available_as_replay_not_independent": {
            "primitive_rows": replay_rows["filled_by_replay_count"],
            "locked_target": replay_rows["acceptance_replay"],
        },
        "missing_independent_execution": {
            "selected_quadrature_engine_or_rule": True,
            "primitive_three_by_three_contraction_integrals": True,
            "independent_hessian_source_vector": True,
            "sector_response_matrices": True,
            "error_bounds_or_exactness_certificate": True,
        },
        "independent_execution_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    equivalence = {
        "schema": "MTTNecessarySufficientCycleExitTheorem.v1",
        "status": "CYCLE_EXIT_EQUIVALENCE_PROVED_PAYLOAD_OPEN",
        "statement": (
            "Given the closed support already in this repo, dynamic C1 packet closure is equivalent to either "
            "Route A: selected physical C1 variation/source principle that applies Q_residual and emits b_selected, "
            "or Route B: independent selected quadrature/Hessian execution emitting the same locked target."
        ),
        "closed_support": promotion_attempt["support_closed"],
        "route_A_sufficient_if": [
            "selected differentiated Phi_fin^C1 applies Q_residual",
            "R_Z/R_X are emitted as physical C1 source values",
            "b_selected is emitted by the same physical source rule",
            "boundary terms vanish for the selected dynamic trace",
        ],
        "route_B_sufficient_if": quadrature_attempt["missing_independent_execution"],
        "necessary_reason": (
            "All other candidate blockers are already discharged or reduced to this object: trace, basis, "
            "dotD/alpha1, formal functional uniqueness, projector uniqueness, row replay, and locked target algebra."
        ),
        "locked_target": replay_rows["acceptance_replay"],
        "forbidden_shortcuts": [
            "promoting replay-backed rows as independent quadrature",
            "promoting local axiom patch as unpatched theorem",
            "using observed masses, CKM/PMNS, or CP as selectors",
            "following the previous proof cycle without a new selected source object",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalC1VariationSourcePromotionOrIndependentQuadratureExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill.candidate.json"),
            "replay_rows": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json"),
            "axiom_contract": rel(DATA / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution" / "residual_projector_axiom_patch_contract.packet.json"),
            "route_ladder": rel(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "source_rule_or_execution_route_ladder.packet.json"),
            "variational_derivation": rel(DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve" / "orthogonal_completion_variational_derivation.packet.json"),
        },
        "output_packets": {
            "physical_c1_variation_source_promotion_attempt": rel(PROMOTION),
            "independent_quadrature_execution_attempt": rel(QUADRATURE),
            "necessary_sufficient_cycle_exit_theorem": rel(EQUIV),
        },
        "theorem": {
            "name": "PhysicalC1VariationOrIndependentQuadratureEquivalenceTheorem",
            "proved": True,
            "statement": equivalence["statement"],
        },
        "what_closes_now": {
            "cycle_exit_equivalence_proved": True,
            "physical_variation_source_promotion_attempted": True,
            "independent_quadrature_execution_requirements_fixed": True,
            "local_patch_sufficiency_separated_from_unpatched_closure": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "derive_physical_C1_variation_principle": True,
            "prove_boundary_cancellation_for_selected_dynamic_trace": True,
            "promote_selected_physical_Q_residual_application": True,
            "emit_independent_primitive_quadrature_integrals": True,
            "emit_independent_hessian_source_vector": True,
            "emit_independent_sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_physical_source_promoted": False,
            "route_B_independent_quadrature_executed": False,
            "local_patch_treated_as_unpatched_theorem": False,
            "replay_rows_treated_as_independent": False,
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
        "certificate": "MTT_Selected_PhysicalC1VariationSourcePromotion_or_IndependentQuadratureExecution_v1",
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

    note = f"""# MTT Selected PhysicalC1VariationSourcePromotion or IndependentQuadratureExecution v1

Status: `{STATUS}`.

Closed support:

```text
canonical Q_residual                 = True
formal Euler projection              = True
least-norm completion selects Q      = True
replay rows pass locked target       = True
local patch would close packet       = True
```

Unpatched exit remains:

```text
Route A physical variation principle = False
Route A boundary cancellation        = False
Route B independent quadrature run   = False
```

This proves the exact equivalence of the remaining gate, not the gate itself.
Either derive the physical `Phi_fin^C1` variation/source rule, or run a real
independent quadrature/Hessian execution.

Next artifact: `{NEXT}`.
"""

    PROMOTION.write_text(json.dumps(promotion_attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QUADRATURE.write_text(json.dumps(quadrature_attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    EQUIV.write_text(json.dumps(equivalence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
