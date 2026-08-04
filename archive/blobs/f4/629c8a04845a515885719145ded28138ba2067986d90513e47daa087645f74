from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_galerkin_c1_input_basis_fill_or_residual_projector_axiom_corpus_patch_certificate.json"
)
STATUS = (
    "POST_ALPHA_GALERKIN_C1_INPUT_BASIS_FILL_OR_RESIDUAL_PROJECTOR_AXIOM_CORPUS_PATCH_"
    "IMPORTED_PATCHED_CLOSE_UNPATCHED_OPEN"
)
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "unqualified closure overclaimed")
    require(cert["patched_spine_closure_claimed"] is True, "patched closure not recorded")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "bridge theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    frontier = cert["frontier_decision"]
    require(frontier["patched_spine_dynamic_packet_closes"] is True, "patched close missing")
    require(frontier["unpatched_MTT_dynamic_packet_closes"] is False, "unpatched close overclaimed")
    require(frontier["first_Galerkin_replay_passes"] is True, "replay missing")
    require(frontier["honest_independent_Galerkin_C1_closes"] is False, "independent Galerkin overclaimed")
    require(
        frontier["frontier_is_independent_galerkin_contractions_or_residual_projector_axiom_derivation"]
        is True,
        "wrong frontier",
    )
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    patch = packet["local_axiom_patch"]
    require(patch["status"] == "LOCAL_PROOF_CORPUS_PATCH_APPLIED_GUARDED_AXIOM", "wrong patch status")
    require(patch["main_external_obsidian_papers_modified_now"] is False, "external papers modified")
    require(patch["after_patch_promotions_in_patched_spine"]["SM_parity_dynamic_packet"] is True, "patched dynamic close missing")
    require(patch["after_patch_promotions_in_patched_spine"]["no_knob_flavor_constants"] is False, "no-knob overclaim")

    replay = packet["first_galerkin_replay_result"]
    require(replay["status"] == "STRICT_REPLAY_PASSES_BUT_NOT_INDEPENDENT_HONEST_GALERKIN", "wrong replay status")
    require(replay["strict_replay_passes"] is True, "strict replay failed")
    require(replay["honest_independent_galerkin_execution_passes"] is False, "independent execution overclaimed")
    require(replay["acceptance_results"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram drift")
    require(replay["acceptance_results"]["A_transpose_b"] == [12.0, 12.0], "ATb drift")
    require(replay["acceptance_results"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta drift")

    inputs = packet["input_packets"]
    require(inputs["zero_mode_basis"]["selected_source_verified"] is False, "zero-mode source overclaimed")
    require(inputs["primitive_contraction_terms"]["computed_from_independent_galerkin_quadrature"] is False, "independent quadrature overclaimed")
    require(inputs["hessian_source_vector"]["b_selected_emitted_by_independent_hessian"] is False, "independent b overclaimed")
    require(inputs["sector_response_matrices"]["independent_sector_matrices_emitted"] is False, "independent sectors overclaimed")

    require(STATUS in note and NEXT in note and "patched" in note and "proof spine" in note, "note missing essentials")
    print(
        "AUDIT_PASS: Galerkin C1 input-basis/axiom-patch bridge imported; "
        "patched close recorded and unpatched closure remains open"
    )


if __name__ == "__main__":
    main()
