"""Import Route-C dual attempt with guarded patched-spine closure."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_residual_projector_insertion_spec_import_certificate.json"
UPSTREAM_SLUG = "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1.md"
UPSTREAM_PATCH_NOTE = SM / "proof_corpus" / "MTT_DifferentiatedPhiFinC1ResidualProjectorAxiom_LocalCorpusPatch_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
INPUT_DIR = UPSTREAM_DIR / "inputs"
ZERO_MODE = INPUT_DIR / "zero_mode_basis.packet.json"
PRIMITIVE_TERMS = INPUT_DIR / "primitive_contraction_terms.packet.json"
HESSIAN_SOURCE = INPUT_DIR / "hessian_source_vector.packet.json"
SECTOR_MATRICES = INPUT_DIR / "sector_response_matrices.packet.json"
FIRST_RUN = UPSTREAM_DIR / "first_galerkin_replay_result.packet.json"
CORPUS_PATCH = UPSTREAM_DIR / "residual_projector_axiom_local_corpus_patch.packet.json"

OUTPUT_PACKET = DATA / "routec_dual_attempt_patched_spine_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_dual_attempt_patched_spine_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_DualAttemptPatchedSpine_Import_v1.md"

STATUS = "ROUTEC_DUAL_ATTEMPT_PATCHED_SPINE_IMPORTED_UNPATCHED_OPEN"
PREVIOUS_STATUS = "ROUTEC_RESIDUAL_PROJECTOR_INSERTION_SPEC_IMPORTED_INPUTS_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_GALERKINC1INPUTBASISFILL_OR_RESIDUALPROJECTORAXIOMCORPUSPATCH_BUILT_DUAL_ATTEMPT_CONDITIONAL_CLOSE"
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    zero = load(ZERO_MODE)
    primitive = load(PRIMITIVE_TERMS)
    hessian = load(HESSIAN_SOURCE)
    sectors = load(SECTOR_MATRICES)
    first = load(FIRST_RUN)
    patch = load(CORPUS_PATCH)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    patch_note = UPSTREAM_PATCH_NOTE.read_text(encoding="utf-8")

    replay = first["acceptance_results"]
    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1",
        "F1_upstream_dual_attempt_proved_global_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["patched_spine_closure_claimed"] is True
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["patched_spine_closure_claimed"] is True
        and cert["unpatched_theorem_closure_claimed"] is False
        and cert["honest_independent_Galerkin_C1_closed"] is False,
        "F3_route_A_is_guarded_patch_only": patch["status"] == "LOCAL_PROOF_CORPUS_PATCH_APPLIED_GUARDED_AXIOM"
        and patch["after_patch_promotions_in_patched_spine"]["A_selected"] is True
        and patch["after_patch_promotions_in_patched_spine"]["b_selected"] is True
        and patch["after_patch_promotions_in_patched_spine"]["deltaTheta_C1"] is True
        and patch["after_patch_promotions_in_patched_spine"]["SM_parity_dynamic_packet"] is True
        and patch["after_patch_promotions_in_patched_spine"]["no_knob_flavor_constants"] is False
        and patch["main_external_obsidian_papers_modified_now"] is False
        and "not a derivation from the earlier MTT axioms" in patch["guardrail"]
        and "not yet a derivation from unpatched MTT axioms" in patch_note,
        "F4_route_B_replay_not_independent": zero["status"] == "CANONICAL_QUTRIT_MATRIX_UNIT_BASIS_FILLED_SUPPORT_LEVEL"
        and zero["basis_dimension"] == 9
        and zero["selected_source_verified"] is False
        and primitive["status"] == "RESIDUAL_PROJECTOR_CONTRACTION_TERMS_FILLED_FROM_AXIOM_CONTRACT"
        and primitive["computed_from_independent_galerkin_quadrature"] is False
        and primitive["selected_source_verified"] is False
        and hessian["status"] == "B_SELECTED_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT"
        and hessian["b_selected_emitted_by_independent_hessian"] is False
        and hessian["b_selected_replay_available_under_axiom_patch"] is True
        and sectors["status"] == "SECTOR_RESPONSE_MATRICES_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT"
        and sectors["independent_sector_matrices_emitted"] is False,
        "F5_strict_replay_exact": first["status"] == "STRICT_REPLAY_PASSES_BUT_NOT_INDEPENDENT_HONEST_GALERKIN"
        and first["strict_replay_passes"] is True
        and first["honest_independent_galerkin_execution_passes"] is False
        and first["coordinate_target"]["total_real_coordinates"] == 72
        and replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0]
        and len(first["why_independent_execution_not_closed"]) == 3,
        "F6_upstream_route_flags_preserved": upstream["route_A_result"]["local_corpus_axiom_patch_applied"] is True
        and upstream["route_A_result"]["closes_SM_parity_dynamic_packet_in_patched_spine"] is True
        and upstream["route_A_result"]["closes_unpatched_or_derived_MTT_theorem"] is False
        and upstream["route_B_result"]["input_packets_filled"] is True
        and upstream["route_B_result"]["strict_replay_passes"] is True
        and upstream["route_B_result"]["honest_independent_galerkin_execution_passes"] is False,
        "F7_remaining_gates_preserved": all(
            upstream["what_remains_open"][key] is True
            for key in [
                "derive_residual_projector_axiom_from_unpatched_MTT",
                "emit_independent_selected_zero_mode_basis",
                "compute_independent_primitive_galerkin_contractions",
                "emit_independent_hessian_b_selected",
                "promote_unpatched_A_selected",
                "promote_unpatched_b_selected",
                "true_SM_equivalence_closure_without_local_axiom",
            ]
        ),
        "F8_note_guardrails_present": "Both routes were tried" in note,
    }

    summary = {
        "patched_spine_dynamic_packet_closed": True,
        "global_closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "honest_independent_galerkin_closed": False,
        "external_obsidian_papers_modified": False,
        "strict_replay_passes": True,
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
        "total_real_coordinates": first["coordinate_target"]["total_real_coordinates"],
        "route_B_independence_gaps": first["why_independent_execution_not_closed"],
    }

    return {
        "packet": "RouteC_DualAttemptPatchedSpine_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_patch": str(CORPUS_PATCH),
            "upstream_first_run": str(FIRST_RUN),
        },
        "theorem": {
            "name": "RouteCDualAttemptPatchedSpineImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The guarded residual-projector axiom patch closes the SM-parity "
                "dynamic C1 packet only inside a patched local proof spine.  The "
                "same values replay exactly in the Galerkin harness, but that "
                "harness is not an independent selected Galerkin computation."
            ),
        },
        "checks": checks,
        "dual_attempt_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "zero_mode_basis": zero,
            "primitive_contraction_terms": primitive,
            "hessian_source_vector": hessian,
            "sector_response_matrices": sectors,
            "first_galerkin_replay_result": first,
            "residual_projector_axiom_local_corpus_patch": patch,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_global_SM_closure": False,
            "claims_unpatched_MTT_derivation": False,
            "claims_honest_independent_Galerkin_C1": False,
            "claims_external_papers_patched": False,
            "claims_no_knob_flavor_constants": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCDualAttemptPatchedSpineImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "dual_attempt_summary": packet["dual_attempt_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["dual_attempt_summary"]
    return f"""# RouteC Dual Attempt Patched Spine Import v1

Status: `{cert["status"]}`.

Both routes have now been tried under strict guardrails.

Route A applies a guarded local residual-projector axiom patch.  Inside that
patched local proof spine it promotes `A_selected`, `b_selected`, and
`deltaTheta_C1`, and closes the SM-parity dynamic C1 packet.

Route B replays the same strict 72-real target:

```text
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
```

This is not global SM closure and not an unpatched MTT derivation.  The honest
independent Galerkin lane remains open because the primitive contractions,
`b_selected`, and zero-mode basis are inherited/replayed rather than emitted by
an independent selected Galerkin computation.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
