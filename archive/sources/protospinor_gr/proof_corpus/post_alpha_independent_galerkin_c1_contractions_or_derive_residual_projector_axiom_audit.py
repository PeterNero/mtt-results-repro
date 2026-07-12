from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_galerkin_c1_contractions_or_derive_residual_projector_axiom_certificate.json"
)
STATUS = (
    "POST_ALPHA_INDEPENDENT_GALERKIN_C1_CONTRACTIONS_OR_DERIVE_RESIDUAL_PROJECTOR_AXIOM_"
    "IMPORTED_CUTSET_OPEN"
)
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["patched_spine_closure_preserved"] is True, "patched close not preserved")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched close overclaimed")
    require(cert["theorem"]["proved"] is True, "cutset bridge theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    frontier = cert["frontier_decision"]
    require(frontier["L0_trace_orthogonal_uniqueness_closed"] is True, "L0 not closed")
    require(frontier["L1_minimal_norm_completion_conditional"] is True, "L1 conditional missing")
    require(frontier["L2_physical_PhiFinC1_application_open"] is True, "L2 should remain open")
    require(frontier["L3_independent_quadrature_hessian_open"] is True, "L3 should remain open")
    require(
        frontier[
            "frontier_is_differentiated_C1_orthogonal_completion_principle_or_independent_quadrature_hessian_solve"
        ]
        is True,
        "wrong frontier",
    )
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    dependency = packet["independence_dependency_audit"]
    require(dependency["status"] == "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT", "wrong dependency status")
    require(dependency["first_run_result"]["strict_replay_passes"] is True, "strict replay missing")
    require(
        dependency["first_run_result"]["honest_independent_galerkin_execution_passes"] is False,
        "independent Galerkin overclaimed",
    )
    require(
        dependency["primitive_contractions"]["computed_from_independent_galerkin_quadrature"] is False,
        "independent primitive quadrature overclaimed",
    )
    require(
        dependency["hessian_source"]["b_selected_emitted_by_independent_hessian"] is False,
        "independent Hessian b overclaimed",
    )

    contract = packet["minimal_next_source_contract"]
    require(contract["status"] == "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED", "wrong source contract status")
    require(contract["recommended_next"] == NEXT, "contract next drift")
    require(contract["option_A_derive_principle"]["name"] == "DifferentiatedC1OrthogonalCompletionPrinciple", "wrong option A")
    require(contract["option_B_compute_values"]["name"] == "IndependentGalerkinQuadratureHessianSolve", "wrong option B")

    ladder = packet["residual_projector_derivation_ladder"]
    require(ladder["status"] == "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN", "wrong ladder status")
    require(ladder["levels"]["L0_trace_orthogonal_uniqueness"]["closed"] is True, "L0 ladder drift")
    require(ladder["levels"]["L1_minimal_norm_completion"]["closed_conditionally"] is True, "L1 ladder drift")
    require(ladder["levels"]["L2_physical_PhiFinC1_application"]["closed"] is False, "L2 overclosed")
    require(ladder["levels"]["L3_independent_quadrature_hessian"]["closed"] is False, "L3 overclosed")

    require(STATUS in note and NEXT in note and "unpatched dependency cutset" in note, "note missing essentials")
    print(
        "AUDIT_PASS: independent Galerkin/residual-projector axiom cutset bridge imported; "
        "orthogonal-completion or independent quadrature remains open"
    )


if __name__ == "__main__":
    main()
