"""Audit residual-projector axiom insertion / Galerkin C1 first-execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
AXIOM_INSERTION = PACKET_DIR / "residual_projector_axiom_insertion_package.packet.json"
GALERKIN_SPEC = PACKET_DIR / "galerkin_c1_first_execution_spec.packet.json"
DECISION = PACKET_DIR / "route_decision_and_next_inputs.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_RESIDUALPROJECTORAXIOMINSERTION_OR_GALERKINC1FIRSTEXECUTION_BUILT_INSERTION_SPEC_OPEN"
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    axiom = load(AXIOM_INSERTION)
    galerkin = load(GALERKIN_SPEC)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(axiom["status"] == "PAPER_APPENDIX_DRAFTS_READY_NOT_CORPUS_PATCHED", "axiom package status mismatch")
    require(len(axiom["target_drafts"]) == 3, "draft count mismatch")
    for path_text in axiom["target_drafts"].values():
        path = ROOT / path_text
        require(path.exists(), f"draft missing: {path_text}")
        text = path.read_text(encoding="utf-8")
        require("Theorem Slot I9" in text, f"draft missing theorem slot: {path_text}")
        require("observed masses" in text and "target residual fitting" in text, f"draft missing guardrail: {path_text}")
    require(axiom["paper_ready_theorem_slot"]["payload"]["b_source_emitted"] is True, "axiom payload missing b")
    require(axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "axiom replay ATA mismatch")
    require(axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_b"] == [12.0, 12.0], "axiom replay ATb mismatch")
    require(axiom["after_insertion_replay"]["numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0], "axiom replay delta mismatch")
    require(axiom["inserted_into_main_corpus_now"] is False, "main corpus patch overclaimed")

    require(galerkin["status"] == "FIRST_EXECUTION_SPEC_READY_INPUT_BASIS_VALUES_MISSING", "Galerkin spec status mismatch")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "Galerkin target mismatch")
    require(galerkin["coordinate_order"]["sector_order"] == ["u", "e", "d", "nuD"], "sector order mismatch")
    require(len(galerkin["required_input_files"]) == 4, "input file count mismatch")
    for key in [
        "zero_mode_basis_packet",
        "primitive_contraction_terms_packet",
        "hessian_or_source_vector_packet",
        "sector_response_matrix_packet",
    ]:
        require(key in galerkin["required_input_files"], f"missing Galerkin input: {key}")
    require(galerkin["first_execution_run_now"] is False, "first execution overclaimed")
    require(len(galerkin["why_not_run_now"]) == 3, "why-not-run list mismatch")

    require(decision["status"] == "TWO_ROUTES_READY_NEXT_INPUTS_SHARP", "decision status mismatch")
    require(decision["route_A_residual_projector_axiom"]["ready_as_paper_appendix_draft"] is True, "Route A not ready")
    require(decision["route_A_residual_projector_axiom"]["main_corpus_patched_now"] is False, "Route A patch overclaimed")
    require(decision["route_B_honest_galerkin_execution"]["ready_as_execution_spec"] is True, "Route B not ready")
    require(decision["route_B_honest_galerkin_execution"]["run_now"] is False, "Route B run overclaimed")
    require(len(decision["route_B_honest_galerkin_execution"]["next_missing_inputs"]) == 4, "missing input list mismatch")
    require("Two superset paths" in decision["superset_strategy"], "superset strategy missing")

    for key in [
        "residual_projector_axiom_appendix_drafts_written",
        "galerkin_first_execution_schema_fixed",
        "route_A_and_route_B_locked_to_same_72_real_target",
        "next_input_files_declared",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "patch_main_corpus_with_residual_projector_axiom_or_prove_it",
        "fill_zero_mode_basis_packet",
        "fill_primitive_contraction_terms_packet",
        "fill_hessian_source_vector_packet",
        "fill_sector_response_matrix_packet",
        "run_first_honest_Galerkin_C1_execution",
        "promote_A_selected",
        "promote_b_selected",
        "promote_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "main_corpus_axiom_patch_applied_now",
        "residual_projector_axiom_proved_now",
        "first_Galerkin_C1_execution_run_now",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")
    for key in ["observed_data_used", "target_fitting_used", "closure_claimed"]:
        require(data[key] is False, f"guardrail overclaimed: {key}")

    require(data["theorem"]["proved"] is True, "theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Nothing is promoted yet" in note, "note missing non-promotion guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
