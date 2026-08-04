from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_residual_projector_axiom_insertion_or_galerkin_c1_first_execution_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_galerkin_c1_input_basis_fill_or_residual_projector_axiom_corpus_patch_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_galerkin_c1_input_basis_fill_or_residual_projector_axiom_corpus_patch_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_galerkin_c1_input_basis_fill_or_residual_projector_axiom_corpus_patch.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentGalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_GALERKIN_C1_INPUT_BASIS_FILL_OR_RESIDUAL_PROJECTOR_AXIOM_CORPUS_PATCH_IMPORTED_PATCHED_CLOSE_UNPATCHED_OPEN"
SOURCE_STATUS = "POST_ALPHA_GALERKIN_C1_INPUT_BASIS_FILL_OR_RESIDUAL_PROJECTOR_AXIOM_CORPUS_PATCH_IMPORTED_PATCHED_CLOSE_UNPATCHED_OPEN"
THIS_ARTIFACT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["route_A_ready_as_appendix_patch"] is True,
            prev["frontier_decision"]["route_B_ready_as_execution_spec"] is True,
            prev["frontier_decision"]["main_corpus_axiom_patch_applied_now"] is False,
            prev["frontier_decision"]["first_Galerkin_C1_execution_run_now"] is False,
            prev["frontier_decision"]["frontier_is_galerkin_input_basis_fill_or_residual_projector_axiom_corpus_patch"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["patched_spine_closure_claimed"] is True,
            source["unpatched_theorem_closure_claimed"] is False,
            source["frontier_decision"]["patched_spine_dynamic_packet_closes"] is True,
            source["frontier_decision"]["unpatched_MTT_dynamic_packet_closes"] is False,
            source["frontier_decision"]["first_Galerkin_replay_passes"] is True,
            source["frontier_decision"]["honest_independent_Galerkin_C1_closes"] is False,
            source["frontier_decision"]["frontier_is_independent_galerkin_contractions_or_residual_projector_axiom_derivation"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    patch = source_packet["local_axiom_patch"]
    replay = source_packet["first_galerkin_replay_result"]
    inputs = source_packet["input_packets"]

    patched_close_ok = all(
        [
            patch["schema"] == "MTTResidualProjectorAxiomLocalCorpusPatch.v1",
            patch["status"] == "LOCAL_PROOF_CORPUS_PATCH_APPLIED_GUARDED_AXIOM",
            patch["main_external_obsidian_papers_modified_now"] is False,
            patch["after_patch_promotions_in_patched_spine"]["A_selected"] is True,
            patch["after_patch_promotions_in_patched_spine"]["b_selected"] is True,
            patch["after_patch_promotions_in_patched_spine"]["deltaTheta_C1"] is True,
            patch["after_patch_promotions_in_patched_spine"]["SM_parity_dynamic_packet"] is True,
            patch["after_patch_promotions_in_patched_spine"]["no_knob_flavor_constants"] is False,
        ]
    )

    replay_harness_ok = all(
        [
            replay["schema"] == "MTTGalerkinC1FirstReplayResult.v1",
            replay["status"] == "STRICT_REPLAY_PASSES_BUT_NOT_INDEPENDENT_HONEST_GALERKIN",
            replay["strict_replay_passes"] is True,
            replay["honest_independent_galerkin_execution_passes"] is False,
            replay["coordinate_target"]["total_real_coordinates"] == 72,
            replay["acceptance_results"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            replay["acceptance_results"]["A_transpose_b"] == [12.0, 12.0],
            replay["acceptance_results"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    replay_inputs_ok = all(
        [
            inputs["zero_mode_basis"]["selected_source_verified"] is False,
            inputs["primitive_contraction_terms"]["computed_from_independent_galerkin_quadrature"] is False,
            inputs["primitive_contraction_terms"]["selected_source_verified"] is False,
            inputs["hessian_source_vector"]["b_selected_emitted_by_independent_hessian"] is False,
            inputs["hessian_source_vector"]["b_selected_replay_available_under_axiom_patch"] is True,
            inputs["sector_response_matrices"]["independent_sector_matrices_emitted"] is False,
            all(
                packet["observed_data_used"] is False and packet["target_fitting_used"] is False
                for packet in inputs.values()
            ),
        ]
    )

    what_closes_now = {
        "long_name_preparation_gate_consumed": prev_ok,
        "audited_dual_route_packet_reanchored": source_ok,
        "patched_spine_dynamic_packet_close_recorded": patched_close_ok,
        "first_galerkin_replay_harness_passes": replay_harness_ok,
        "replay_input_packets_filled_and_guarded": replay_inputs_ok,
    }

    what_remains_open = {
        "derive_residual_projector_axiom_from_unpatched_MTT": True,
        "compute_independent_primitive_galerkin_contractions": True,
        "emit_independent_hessian_b_selected": True,
        "emit_independent_selected_zero_mode_basis": True,
        "promote_unpatched_A_selected": True,
        "promote_unpatched_b_selected": True,
        "promote_unpatched_deltaTheta_C1": True,
        "true_SM_equivalence_closure_without_local_axiom": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "patched_spine_is_not_unpatched_theorem": True,
        "external_obsidian_papers_not_modified": patch["main_external_obsidian_papers_modified_now"] is False,
        "independent_galerkin_not_claimed": replay["honest_independent_galerkin_execution_passes"] is False,
        "replay_values_are_not_independent_selected_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaIndependentGalerkinC1InputBasisFillOrResidualProjectorAxiomCorpusPatchBridge",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the dual attempt at the "
            "Galerkin C1 input-basis fill or residual-projector axiom corpus patch "
            "gate. A guarded local proof-corpus patch closes the SM-parity dynamic "
            "packet only inside the patched spine; the unpatched theorem and honest "
            "independent Galerkin derivation remain open."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_dual_route_certificate": source,
        "local_axiom_patch": patch,
        "first_galerkin_replay_result": replay,
        "input_packets": inputs,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "patched_spine_dynamic_packet_closes": True,
            "unpatched_MTT_dynamic_packet_closes": False,
            "first_Galerkin_replay_passes": True,
            "honest_independent_Galerkin_C1_closes": False,
            "frontier_is_independent_galerkin_contractions_or_residual_projector_axiom_derivation": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_dual_route_certificate": str(SOURCE_CERT),
            "source_dual_route_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent GalerkinC1InputBasisFill or ResidualProjectorAxiomCorpusPatch Import v1

## Result

The guarded local patch closes the SM-parity dynamic packet only in the patched
proof spine.

```text
patched spine dynamic packet closes = true
unpatched MTT dynamic packet closes = false
true SM equivalence closes = false
```

The Galerkin side is a replay harness, not an independent proof:

```text
first Galerkin replay passes = true
honest independent Galerkin C1 closes = false
```

The replay remains exact:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
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
        "certificate": "post_alpha_independent_galerkin_c1_input_basis_fill_or_residual_projector_axiom_corpus_patch",
        "status": STATUS,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
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
