from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_residual_projector_insertion_or_galerkin_first_execution_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_residual_projector_axiom_insertion_or_galerkin_c1_first_execution_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_residual_projector_axiom_insertion_or_galerkin_c1_first_execution.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_Import_v1.md"
)

STATUS = (
    "POST_ALPHA_RESIDUAL_PROJECTOR_AXIOM_INSERTION_OR_GALERKIN_C1_FIRST_EXECUTION_"
    "IMPORTED_PREPARATION_CLOSED_SOURCE_OPEN"
)
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source_cert = load(SOURCE_CERT)
    source_packet = load(Path(source_cert["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"][
                "frontier_is_residual_projector_axiom_insertion_or_galerkin_first_execution"
            ]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1",
        ]
    )

    source_ok = all(
        [
            source_cert["theorem"]["proved"] is True,
            source_cert["closure_claimed"] is False,
            source_cert["status"]
            == "POST_ALPHA_RESIDUAL_PROJECTOR_INSERTION_OR_GALERKIN_FIRST_EXECUTION_IMPORTED_OPEN",
            source_cert["frontier_decision"]["next_required_artifact"] == NEXT,
            source_cert["frontier_decision"]["route_A_ready_as_appendix_patch"] is True,
            source_cert["frontier_decision"]["route_B_ready_as_execution_spec"] is True,
            source_cert["frontier_decision"]["main_corpus_axiom_patch_applied_now"] is False,
            source_cert["frontier_decision"]["first_Galerkin_C1_execution_run_now"] is False,
            all(source_cert["what_closes_now"].values()),
            all(source_cert["what_remains_open"].values()),
            all(source_cert["guardrails"].values()),
        ]
    )

    axiom = source_packet["axiom_insertion_package"]
    galerkin = source_packet["galerkin_c1_first_execution_spec"]
    decision = source_packet["route_decision_and_next_inputs"]

    replay_ok = all(
        [
            axiom["after_insertion_replay"]["numeric_replay"]["rank"] == 2,
            axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_A"]
            == [[12.0, 0.0], [0.0, 12.0]],
            axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_b"]
            == [12.0, 12.0],
            axiom["after_insertion_replay"]["numeric_replay"]["deltaTheta_C1"]
            == [1.0, 1.0],
            axiom["after_insertion_replay"]["SM_parity_dynamic_packet_would_close"] is True,
            axiom["after_insertion_replay"]["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    route_ok = all(
        [
            axiom["status"] == "PAPER_APPENDIX_DRAFTS_READY_NOT_CORPUS_PATCHED",
            axiom["inserted_into_main_corpus_now"] is False,
            galerkin["status"] == "FIRST_EXECUTION_SPEC_READY_INPUT_BASIS_VALUES_MISSING",
            galerkin["first_execution_run_now"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            len(galerkin["required_input_files"]) == 4,
            decision["status"] == "TWO_ROUTES_READY_NEXT_INPUTS_SHARP",
            decision["recommended_next"] == NEXT,
            decision["route_A_residual_projector_axiom"]["main_corpus_patched_now"] is False,
            decision["route_B_honest_galerkin_execution"]["run_now"] is False,
            len(decision["route_B_honest_galerkin_execution"]["next_missing_inputs"]) == 4,
        ]
    )

    what_closes_now = {
        "long_name_previous_gate_consumed": prev_ok,
        "audited_preparation_packet_bridged": source_ok,
        "two_route_frontier_locked": route_ok,
        "rank2_replay_preserved": replay_ok,
        "next_input_packets_declared": True,
    }

    what_remains_open = {
        "patch_main_corpus_with_residual_projector_axiom_or_prove_it": True,
        "fill_zero_mode_basis_packet": True,
        "fill_primitive_contraction_terms_packet": True,
        "fill_hessian_source_vector_packet": True,
        "fill_sector_response_matrix_packet": True,
        "run_first_honest_Galerkin_C1_execution": True,
        "promote_A_selected": True,
        "promote_b_selected": True,
        "promote_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_patch_main_corpus": True,
        "does_not_claim_residual_projector_axiom_proof": True,
        "does_not_run_first_Galerkin_execution": True,
        "does_not_promote_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaResidualProjectorAxiomInsertionOrGalerkinC1FirstExecutionBridge",
        "proved": all(
            [
                all(what_closes_now.values()),
                all(what_remains_open.values()),
                all(guardrails.values()),
            ]
        ),
        "closure_claimed": False,
        "statement": (
            "The long-name post-alpha chain now reaches the residual-projector axiom "
            "insertion or Galerkin C1 first-execution frontier. The preparation problem "
            "is closed: Route A is appendix-patch ready, Route B has a strict first "
            "execution schema, and both preserve the exact rank-2 72-real replay. The "
            "source problem remains open because no corpus axiom patch/proof or honest "
            "Galerkin value execution is performed here."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_preparation_certificate": source_cert,
        "axiom_insertion_package": axiom,
        "galerkin_c1_first_execution_spec": galerkin,
        "route_decision_and_next_inputs": decision,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "route_A_ready_as_appendix_patch": True,
            "route_B_ready_as_execution_spec": True,
            "main_corpus_axiom_patch_applied_now": False,
            "first_Galerkin_C1_execution_run_now": False,
            "frontier_is_galerkin_input_basis_fill_or_residual_projector_axiom_corpus_patch": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_preparation_certificate": str(SOURCE_CERT),
            "source_preparation_packet": source_cert["packet_written"],
        },
    }

    note = f"""# PostAlpha ResidualProjectorAxiomInsertion or GalerkinC1FirstExecution Import v1

## Result

The current long-name post-alpha chain now reaches the same sharp frontier as the
audited preparation packet.

Route A is ready as a paper/corpus patch, but it is not inserted here:

```text
DifferentiatedPhiFinC1ResidualProjectorAxiom
selected Phi_fin^C1 applies Q_residual
R_Z, R_X, and b_source are emitted by the same branch
```

Route B is ready as a first Galerkin C1 execution schema, but it is not run here:

```text
zero_mode_basis.packet.json
primitive_contraction_terms.packet.json
hessian_source_vector.packet.json
sector_response_matrices.packet.json
```

Both routes preserve the same replay:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
rank = 2
```

No observed constants, benchmark sector matrices, or target fits are used.

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
        "certificate": "post_alpha_residual_projector_axiom_insertion_or_galerkin_c1_first_execution",
        "status": STATUS,
        "closure_claimed": False,
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
