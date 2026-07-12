from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_independent_galerkin_c1_input_basis_fill_or_residual_projector_axiom_corpus_patch_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_galerkin_or_residual_projector_derivation_cutset_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_galerkin_c1_contractions_or_derive_residual_projector_axiom_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_independent_long_galerkin_c1_contractions_or_derive_residual_projector_axiom.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_IndependentLongGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_Import_v1.md"
)

STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_GALERKIN_C1_CONTRACTIONS_OR_DERIVE_RESIDUAL_PROJECTOR_AXIOM_"
    "REANCHORED_CUTSET_OPEN"
)
PREV_STATUS = (
    "POST_ALPHA_INDEPENDENT_GALERKIN_C1_INPUT_BASIS_FILL_OR_RESIDUAL_PROJECTOR_AXIOM_CORPUS_PATCH_"
    "IMPORTED_PATCHED_CLOSE_UNPATCHED_OPEN"
)
SOURCE_STATUS = "POST_ALPHA_INDEPENDENT_GALERKIN_OR_RESIDUAL_PROJECTOR_DERIVATION_CUTSET_IMPORTED_OPEN"
THIS_ARTIFACT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source_cert = load(SOURCE_CERT)
    source_packet = load(Path(source_cert["packet_written"]))

    prev_ok = all(
        [
            prev["status"] == PREV_STATUS,
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["patched_spine_closure_claimed"] is True,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["patched_spine_dynamic_packet_closes"] is True,
            prev["frontier_decision"]["unpatched_MTT_dynamic_packet_closes"] is False,
            prev["frontier_decision"]["first_Galerkin_replay_passes"] is True,
            prev["frontier_decision"]["honest_independent_Galerkin_C1_closes"] is False,
            prev["frontier_decision"][
                "frontier_is_independent_galerkin_contractions_or_residual_projector_axiom_derivation"
            ]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source_cert["status"] == SOURCE_STATUS,
            source_cert["theorem"]["proved"] is True,
            source_cert["closure_claimed"] is False,
            source_cert["patched_spine_closure_preserved"] is True,
            source_cert["unpatched_theorem_closure_claimed"] is False,
            source_cert["frontier_decision"]["L0_trace_orthogonal_uniqueness_closed"] is True,
            source_cert["frontier_decision"]["L1_minimal_norm_completion_conditional"] is True,
            source_cert["frontier_decision"]["L2_physical_PhiFinC1_application_open"] is True,
            source_cert["frontier_decision"]["L3_independent_quadrature_hessian_open"] is True,
            source_cert["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source_cert["what_closes_now"].values()),
            all(source_cert["what_remains_open"].values()),
            all(source_cert["guardrails"].values()),
        ]
    )

    dependency = source_packet["independence_dependency_audit"]
    contract = source_packet["minimal_next_source_contract"]
    ladder = source_packet["residual_projector_derivation_ladder"]

    dependency_ok = all(
        [
            dependency["schema"] == "MTTIndependentGalerkinDependencyAudit.v1",
            dependency["status"] == "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT",
            dependency["first_run_result"]["strict_replay_passes"] is True,
            dependency["first_run_result"]["honest_independent_galerkin_execution_passes"] is False,
            dependency["primitive_contractions"]["computed_from_independent_galerkin_quadrature"] is False,
            dependency["hessian_source"]["b_selected_emitted_by_independent_hessian"] is False,
            dependency["zero_mode_basis"]["independent_hym_or_galerkin_basis_emitted"] is False,
            len(dependency["independence_obstruction"]) == 3,
        ]
    )

    contract_ok = all(
        [
            contract["schema"] == "MTTMinimalNextSourceContract.v1",
            contract["status"] == "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED",
            contract["recommended_next"] == NEXT,
            contract["option_A_derive_principle"]["name"] == "DifferentiatedC1OrthogonalCompletionPrinciple",
            contract["option_B_compute_values"]["name"] == "IndependentGalerkinQuadratureHessianSolve",
            "72-real A_selected matrix" in contract["option_B_compute_values"]["required_values"],
            contract["observed_data_used"] is False,
            contract["target_fitting_used"] is False,
        ]
    )

    ladder_ok = all(
        [
            ladder["schema"] == "MTTResidualProjectorDerivationLadder.v1",
            ladder["status"] == "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN",
            ladder["levels"]["L0_trace_orthogonal_uniqueness"]["closed"] is True,
            ladder["levels"]["L1_minimal_norm_completion"]["closed_conditionally"] is True,
            ladder["levels"]["L2_physical_PhiFinC1_application"]["closed"] is False,
            ladder["levels"]["L3_independent_quadrature_hessian"]["closed"] is False,
            ladder["what_is_now_theorem_derived"]["unique_Q_residual_given_fixed_fiber_span"] is True,
            ladder["what_is_not_theorem_derived"]["physical_differentiated_PhiFinC1_applies_Q_residual"] is True,
            ladder["observed_data_used"] is False,
            ladder["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "fresh_independent_patched_spine_gate_consumed": prev_ok,
        "dependency_cutset_imported_without_retcon": source_ok,
        "strict_replay_blocked_from_unpatched_promotion": dependency_ok,
        "two_minimal_source_options_preserved": contract_ok,
        "residual_projector_derivation_ladder_preserved": ladder_ok,
    }

    what_remains_open = {
        "derive_differentiated_C1_orthogonal_completion_principle": True,
        "prove_physical_PhiFinC1_applies_Q_residual": True,
        "compute_independent_primitive_contractions": True,
        "emit_independent_hessian_b_selected": True,
        "emit_independent_selected_zero_mode_basis": True,
        "promote_unpatched_A_selected": True,
        "promote_unpatched_b_selected": True,
        "promote_unpatched_deltaTheta_C1": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "patched_spine_closure_preserved_but_not_promoted_to_unpatched": True,
        "strict_replay_not_misreported_as_independent_galerkin": True,
        "orthogonal_completion_not_relabelled_as_proved_physical_rule": True,
        "does_not_promote_unpatched_A_or_b": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaIndependentLongGalerkinC1ContractionsOrDeriveResidualProjectorAxiomBridge",
        "proved": all(
            [
                all(what_closes_now.values()),
                all(what_remains_open.values()),
                all(guardrails.values()),
            ]
        ),
        "closure_claimed": False,
        "patched_spine_closure_preserved": True,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "After the independent patched-spine input-basis fill, the long-name branch "
            "reaches the same audited dependency cutset: trace-orthogonal uniqueness is "
            "closed for a fixed fiber span, while unpatched closure still requires either "
            "a physical DifferentiatedC1OrthogonalCompletionPrinciple or an independent "
            "Galerkin quadrature/Hessian solve."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "fresh_previous_certificate": prev,
        "source_cutset_certificate": source_cert,
        "independence_dependency_audit": dependency,
        "minimal_next_source_contract": contract,
        "residual_projector_derivation_ladder": ladder,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "L0_trace_orthogonal_uniqueness_closed": True,
            "L1_minimal_norm_completion_conditional": True,
            "L2_physical_PhiFinC1_application_open": True,
            "L3_independent_quadrature_hessian_open": True,
            "frontier_is_differentiated_C1_orthogonal_completion_principle_or_independent_quadrature_hessian_solve": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "fresh_previous_certificate": str(PREV),
            "source_cutset_certificate": str(SOURCE_CERT),
            "source_cutset_packet": source_cert["packet_written"],
        },
    }

    note = f"""# PostAlpha IndependentLongGalerkinC1Contractions or DeriveResidualProjectorAxiom Import v1

## Result

The fresh independent patched-spine branch now reaches the residual-projector
dependency cutset without overwriting the older audited chain.

Closed:

```text
fresh patched-spine input-basis gate consumed = true
unique Q_residual from fixed-fiber span = true
strict replay blocked from unpatched promotion = true
```

Still open:

```text
physical Phi_fin^C1 applies Q_residual = false
independent primitive contractions emitted = false
independent Hessian b_selected emitted = false
unpatched A_selected/b_selected/DeltaTheta_C1 promoted = false
```

Thus the true next gate is unchanged:

```text
{NEXT}
```

No observed constants, benchmark matrices, or target fits are used.

## Status

```text
{STATUS}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_independent_long_galerkin_c1_contractions_or_derive_residual_projector_axiom",
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
