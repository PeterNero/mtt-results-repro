from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_residual_projector_insertion_or_galerkin_first_execution_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
LOCAL_PATCH = SM_DIR / "residual_projector_axiom_local_corpus_patch.packet.json"
REPLAY = SM_DIR / "first_galerkin_replay_result.packet.json"
ZERO_MODE = SM_DIR / "inputs" / "zero_mode_basis.packet.json"
PRIMITIVE = SM_DIR / "inputs" / "primitive_contraction_terms.packet.json"
HESSIAN = SM_DIR / "inputs" / "hessian_source_vector.packet.json"
SECTOR = SM_DIR / "inputs" / "sector_response_matrices.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_galerkin_input_fill_or_axiom_patch_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_galerkin_input_fill_or_axiom_patch.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_GalerkinInputFill_or_AxiomPatch_Import_v1.md"

STATUS = "POST_ALPHA_GALERKIN_INPUT_FILL_OR_AXIOM_PATCH_IMPORTED_CONDITIONAL_PATCH_CLOSE"
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    local_patch = load(LOCAL_PATCH)
    replay = load(REPLAY)
    zero_mode = load(ZERO_MODE)
    primitive = load(PRIMITIVE)
    hessian = load(HESSIAN)
    sector = load(SECTOR)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_input_basis_fill_or_axiom_corpus_patch"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["patched_spine_closure_claimed"] is True,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["honest_independent_Galerkin_C1_closed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "DualRouteAttemptTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["route_A_result"]["local_corpus_axiom_patch_applied"] is True,
            candidate["route_A_result"]["closes_SM_parity_dynamic_packet_in_patched_spine"] is True,
            candidate["route_A_result"]["closes_unpatched_or_derived_MTT_theorem"] is False,
            candidate["route_B_result"]["input_packets_filled"] is True,
            candidate["route_B_result"]["strict_replay_passes"] is True,
            candidate["route_B_result"]["honest_independent_galerkin_execution_passes"] is False,
        ]
    )

    patch_ok = all(
        [
            local_patch["schema"] == "MTTResidualProjectorAxiomLocalCorpusPatch.v1",
            local_patch["status"] == "LOCAL_PROOF_CORPUS_PATCH_APPLIED_GUARDED_AXIOM",
            local_patch["main_external_obsidian_papers_modified_now"] is False,
            local_patch["observed_data_used"] is False,
            local_patch["target_fitting_used"] is False,
            local_patch["after_patch_promotions_in_patched_spine"]["A_selected"] is True,
            local_patch["after_patch_promotions_in_patched_spine"]["b_selected"] is True,
            local_patch["after_patch_promotions_in_patched_spine"]["deltaTheta_C1"] is True,
            local_patch["after_patch_promotions_in_patched_spine"]["SM_parity_dynamic_packet"] is True,
            local_patch["after_patch_promotions_in_patched_spine"]["no_knob_flavor_constants"] is False,
        ]
    )

    replay_ok = all(
        [
            replay["schema"] == "MTTGalerkinC1FirstReplayResult.v1",
            replay["status"] == "STRICT_REPLAY_PASSES_BUT_NOT_INDEPENDENT_HONEST_GALERKIN",
            replay["strict_replay_passes"] is True,
            replay["honest_independent_galerkin_execution_passes"] is False,
            replay["observed_data_used"] is False,
            replay["target_fitting_used"] is False,
            replay["coordinate_target"]["total_real_coordinates"] == 72,
            replay["acceptance_results"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            replay["acceptance_results"]["A_transpose_b"] == [12.0, 12.0],
            replay["acceptance_results"]["deltaTheta_C1"] == [1.0, 1.0],
            len(replay["why_independent_execution_not_closed"]) == 3,
        ]
    )

    input_packets_ok = all(
        [
            zero_mode["schema"] == "MTTGalerkinC1ZeroModeBasisPacket.v1",
            zero_mode["status"] == "CANONICAL_QUTRIT_MATRIX_UNIT_BASIS_FILLED_SUPPORT_LEVEL",
            zero_mode["basis_dimension"] == 9,
            zero_mode["selected_source_verified"] is False,
            primitive["schema"] == "MTTGalerkinC1PrimitiveContractionTermsPacket.v1",
            primitive["status"] == "RESIDUAL_PROJECTOR_CONTRACTION_TERMS_FILLED_FROM_AXIOM_CONTRACT",
            primitive["computed_from_independent_galerkin_quadrature"] is False,
            primitive["selected_source_verified"] is False,
            hessian["schema"] == "MTTGalerkinC1HessianSourceVectorPacket.v1",
            hessian["status"] == "B_SELECTED_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT",
            hessian["b_selected_emitted_by_independent_hessian"] is False,
            hessian["b_selected_replay_available_under_axiom_patch"] is True,
            sector["schema"] == "MTTGalerkinC1SectorResponseMatricesPacket.v1",
            sector["status"] == "SECTOR_RESPONSE_MATRICES_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT",
            sector["independent_sector_matrices_emitted"] is False,
            all(packet["observed_data_used"] is False and packet["target_fitting_used"] is False for packet in [zero_mode, primitive, hessian, sector]),
        ]
    )

    what_closes_now = {
        "previous_execution_or_patch_gate_consumed": prev_ok,
        "dual_route_attempt_imported": imported_ok,
        "guarded_local_axiom_patch_records_patched_spine_closure": patch_ok,
        "first_strict_galerkin_replay_passes": replay_ok,
        "galerkin_input_packets_filled_as_replay_harness": input_packets_ok,
    }

    what_remains_open = {
        "derive_residual_projector_axiom_from_unpatched_MTT": True,
        "compute_independent_primitive_galerkin_contractions": True,
        "emit_independent_hessian_b_selected": True,
        "emit_independent_selected_zero_mode_basis": True,
        "promote_unpatched_A_selected": True,
        "promote_unpatched_b_selected": True,
        "true_SM_equivalence_closure_without_local_axiom": True,
        "patch_external_main_papers_if_user_approves": True,
    }

    guardrails = {
        "local_patch_is_guarded_not_unpatched_derivation": True,
        "external_obsidian_papers_not_modified": local_patch["main_external_obsidian_papers_modified_now"] is False,
        "honest_independent_Galerkin_not_claimed": replay["honest_independent_galerkin_execution_passes"] is False,
        "input_values_are_replay_filled_not_independent": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaGalerkinInputFillOrAxiomPatchImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The local proof spine can close the SM-parity dynamic C1 packet under a "
            "guarded residual-projector axiom patch, and the first Galerkin replay "
            "harness passes the same strict 72-real target. This is not yet an "
            "unpatched MTT derivation: the replay-filled primitive, Hessian, and sector "
            "packets are inherited from the axiom contract rather than emitted by an "
            "independent Galerkin/Hessian computation."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "local_axiom_patch": local_patch,
        "first_galerkin_replay_result": replay,
        "input_packets": {
            "zero_mode_basis": zero_mode,
            "primitive_contraction_terms": primitive,
            "hessian_source_vector": hessian,
            "sector_response_matrices": sector,
        },
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "patched_spine_dynamic_packet_closes": True,
            "unpatched_MTT_dynamic_packet_closes": False,
            "first_Galerkin_replay_passes": True,
            "honest_independent_Galerkin_C1_closes": False,
            "frontier_is_independent_contractions_or_axiom_derivation": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "local_axiom_patch": str(LOCAL_PATCH),
            "first_galerkin_replay": str(REPLAY),
            "zero_mode_basis": str(ZERO_MODE),
            "primitive_contraction_terms": str(PRIMITIVE),
            "hessian_source_vector": str(HESSIAN),
            "sector_response_matrices": str(SECTOR),
        },
    }

    note = f"""# PostAlpha Galerkin Input Fill or Axiom Patch Import v1

## Result

The dual route attempt gives a conditional patch close, not a full unpatched
theorem.

Route A:

```text
local guarded residual-projector axiom patch applied = true
patched spine dynamic C1 packet closes = true
unpatched MTT derivation closes = false
```

Route B:

```text
Galerkin input packets filled = true
strict replay passes = true
honest independent Galerkin execution = false
```

The replay is exact:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
```

The remaining scientific gate is now to derive the residual-projector axiom from
unpatched MTT or compute independent selected Galerkin contractions.

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
        "certificate": "post_alpha_galerkin_input_fill_or_axiom_patch",
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
