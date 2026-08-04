from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_residual_projector_insertion_or_galerkin_first_execution_certificate.json"
STATUS = "POST_ALPHA_RESIDUAL_PROJECTOR_INSERTION_OR_GALERKIN_FIRST_EXECUTION_IMPORTED_OPEN"
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "preparation theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["route_A_ready_as_appendix_patch"] is True, "route A not ready")
    require(decision["route_B_ready_as_execution_spec"] is True, "route B not ready")
    require(decision["main_corpus_axiom_patch_applied_now"] is False, "corpus patch overclaimed")
    require(decision["first_Galerkin_C1_execution_run_now"] is False, "execution overclaimed")
    require(decision["frontier_is_input_basis_fill_or_axiom_corpus_patch"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    axiom = packet["axiom_insertion_package"]
    require(axiom["status"] == "PAPER_APPENDIX_DRAFTS_READY_NOT_CORPUS_PATCHED", "wrong axiom package status")
    require(axiom["inserted_into_main_corpus_now"] is False, "axiom patch applied")
    require(axiom["after_insertion_replay"]["numeric_replay"]["rank"] == 2, "rank drift")
    require(axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(axiom["after_insertion_replay"]["numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")

    galerkin = packet["galerkin_c1_first_execution_spec"]
    require(galerkin["status"] == "FIRST_EXECUTION_SPEC_READY_INPUT_BASIS_VALUES_MISSING", "wrong Galerkin status")
    require(galerkin["first_execution_run_now"] is False, "first execution run")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "coordinate target drift")
    require(len(galerkin["required_input_files"]) == 4, "required input packet count drift")

    route = packet["route_decision_and_next_inputs"]
    require(route["status"] == "TWO_ROUTES_READY_NEXT_INPUTS_SHARP", "wrong route decision status")
    require(route["route_A_residual_projector_axiom"]["main_corpus_patched_now"] is False, "route A patched")
    require(route["route_B_honest_galerkin_execution"]["run_now"] is False, "route B run")
    require(len(route["route_B_honest_galerkin_execution"]["next_missing_inputs"]) == 4, "missing-input list drift")
    require(STATUS in note and NEXT in note and "not run" in note, "note missing essentials")
    print("AUDIT_PASS: residual-projector insertion/Galerkin first-execution prep imported; patch and execution remain open")


if __name__ == "__main__":
    main()
