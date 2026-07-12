from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_galerkin_input_fill_or_axiom_patch_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom"
DEPENDENCY_AUDIT = SM_DIR / "independence_dependency_audit.packet.json"
MINIMAL_CONTRACT = SM_DIR / "minimal_next_source_contract.packet.json"
DERIVATION_LADDER = SM_DIR / "residual_projector_derivation_ladder.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_galerkin_or_residual_projector_derivation_cutset_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_galerkin_or_residual_projector_derivation_cutset.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentGalerkin_or_ResidualProjectorDerivation_Cutset_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_GALERKIN_OR_RESIDUAL_PROJECTOR_DERIVATION_CUTSET_IMPORTED_OPEN"
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    dependency = load(DEPENDENCY_AUDIT)
    minimal = load(MINIMAL_CONTRACT)
    ladder = load(DERIVATION_LADDER)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["patched_spine_closure_claimed"] is True,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_independent_contractions_or_axiom_derivation"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["patched_spine_closure_preserved"] is True,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["independent_Galerkin_C1_closed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "DependencyCutsetAndDerivationLadderTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["patched_spine_closure_preserved"] is True,
            candidate["promotion_decision"]["patched_spine_closure_preserved"] is True,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["independent_Galerkin_C1_closed"] is False,
            candidate["promotion_decision"]["residual_projector_axiom_derived_from_unpatched_MTT"] is False,
        ]
    )

    dependency_ok = all(
        [
            dependency["schema"] == "MTTIndependentGalerkinDependencyAudit.v1",
            dependency["status"] == "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT",
            dependency["observed_data_used"] is False,
            dependency["target_fitting_used"] is False,
            dependency["first_run_result"]["strict_replay_passes"] is True,
            dependency["first_run_result"]["honest_independent_galerkin_execution_passes"] is False,
            dependency["primitive_contractions"]["computed_from_independent_galerkin_quadrature"] is False,
            dependency["primitive_contractions"]["selected_source_verified"] is False,
            dependency["hessian_source"]["b_selected_emitted_by_independent_hessian"] is False,
            dependency["zero_mode_basis"]["independent_hym_or_galerkin_basis_emitted"] is False,
            len(dependency["independence_obstruction"]) == 3,
        ]
    )

    minimal_ok = all(
        [
            minimal["schema"] == "MTTMinimalNextSourceContract.v1",
            minimal["status"] == "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED",
            minimal["observed_data_used"] is False,
            minimal["target_fitting_used"] is False,
            minimal["recommended_next"] == NEXT,
            minimal["option_A_derive_principle"]["name"] == "DifferentiatedC1OrthogonalCompletionPrinciple",
            minimal["option_B_compute_values"]["name"] == "IndependentGalerkinQuadratureHessianSolve",
            len(minimal["option_A_derive_principle"]["would_promote"]) == 4,
            len(minimal["option_B_compute_values"]["required_values"]) == 6,
            len(minimal["option_B_compute_values"]["would_promote"]) == 3,
        ]
    )

    ladder_ok = all(
        [
            ladder["schema"] == "MTTResidualProjectorDerivationLadder.v1",
            ladder["status"] == "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN",
            ladder["observed_data_used"] is False,
            ladder["target_fitting_used"] is False,
            ladder["levels"]["L0_trace_orthogonal_uniqueness"]["closed"] is True,
            ladder["levels"]["L1_minimal_norm_completion"]["closed_conditionally"] is True,
            ladder["levels"]["L2_physical_PhiFinC1_application"]["closed"] is False,
            ladder["levels"]["L3_independent_quadrature_hessian"]["closed"] is False,
            all(ladder["what_is_now_theorem_derived"].values()),
            all(ladder["what_is_not_theorem_derived"].values()),
        ]
    )

    what_closes_now = {
        "previous_conditional_patch_close_consumed": prev_ok,
        "dependency_cutset_imported": imported_ok,
        "independence_audit_blocks_replay_promotion": dependency_ok,
        "two_minimal_source_options_declared": minimal_ok,
        "residual_projector_derivation_ladder_fixed": ladder_ok,
    }

    what_remains_open = {
        "derive_differentiated_C1_orthogonal_completion_principle": True,
        "prove_physical_PhiFinC1_applies_Q_residual": True,
        "compute_independent_primitive_contractions": True,
        "emit_independent_hessian_b_selected": True,
        "emit_independent_selected_zero_mode_basis": True,
        "close_unpatched_SM_parity_dynamic_packet": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "patched_spine_closure_preserved_but_not_promoted_to_unpatched": True,
        "strict_replay_not_misreported_as_independent_galerkin": True,
        "orthogonal_completion_not_relabelled_as_proved_physical_rule": True,
        "does_not_promote_unpatched_A_or_b": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaIndependentGalerkinOrResidualProjectorDerivationCutsetImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "patched_spine_closure_preserved": True,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "After the guarded local axiom patch and strict replay harness, the exact "
            "unpatched dependency cutset is identified. Algebraic trace-orthogonal "
            "uniqueness of Q_residual and rank-2 replay are theorem-derived, but the "
            "physical differentiated Phi_fin^C1 application rule and independent "
            "Galerkin/Hessian source values remain open. The next sufficient closures "
            "are precisely the DifferentiatedC1OrthogonalCompletionPrinciple or an "
            "IndependentGalerkinQuadratureHessianSolve."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "independence_dependency_audit": dependency,
        "minimal_next_source_contract": minimal,
        "residual_projector_derivation_ladder": ladder,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "L0_trace_orthogonal_uniqueness_closed": True,
            "L1_minimal_norm_completion_conditional": True,
            "L2_physical_PhiFinC1_application_open": True,
            "L3_independent_quadrature_hessian_open": True,
            "frontier_is_orthogonal_completion_principle_or_independent_quadrature_hessian_solve": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "independence_dependency_audit": str(DEPENDENCY_AUDIT),
            "minimal_next_source_contract": str(MINIMAL_CONTRACT),
            "residual_projector_derivation_ladder": str(DERIVATION_LADDER),
        },
    }

    note = f"""# PostAlpha Independent Galerkin or Residual Projector Derivation Cutset Import v1

## Result

The unpatched frontier is now a true cutset.

Closed:

```text
unique Q_residual from trace-orthogonal fixed-fiber span
unique R_Z/R_X residual representatives under the conditional target
exact rank-2 replay
patched-spine closure preserved
```

Open:

```text
physical Phi_fin^C1 applies Q_residual
independent selected Galerkin primitive contractions
independent Hessian/source vector b_selected
independent selected zero-mode basis
```

The next sufficient route is one of:

```text
DifferentiatedC1OrthogonalCompletionPrinciple
IndependentGalerkinQuadratureHessianSolve
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
        "certificate": "post_alpha_independent_galerkin_or_residual_projector_derivation_cutset",
        "status": STATUS,
        "closure_claimed": False,
        "patched_spine_closure_preserved": True,
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
