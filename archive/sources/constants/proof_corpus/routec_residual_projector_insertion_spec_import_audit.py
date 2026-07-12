"""Audit Route-C residual-projector insertion spec import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_residual_projector_insertion_spec_import.candidate.json"
CERT = ROOT / "certificates" / "routec_residual_projector_insertion_spec_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_ResidualProjectorInsertionSpec_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_residual_projector_insertion_spec.py"

STATUS = "ROUTEC_RESIDUAL_PROJECTOR_INSERTION_SPEC_IMPORTED_INPUTS_OPEN"
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    summary = data["residual_projector_insertion_spec_summary"]
    require(summary["route_A_appendix_drafts_ready"] is True, "Route A not ready")
    require(summary["route_A_main_corpus_patched_now"] is False, "Route A patch overclaimed")
    require(summary["route_B_execution_spec_ready"] is True, "Route B not ready")
    require(summary["route_B_first_execution_run_now"] is False, "Route B run overclaimed")
    require(summary["strict_target_real_coordinates"] == 72, "strict target mismatch")
    require(summary["sector_order"] == ["u", "e", "d", "nuD"], "sector order mismatch")
    require(summary["missing_input_count"] == 4, "missing input count mismatch")
    require(set(summary["required_input_files"]) == {
        "zero_mode_basis_packet",
        "primitive_contraction_terms_packet",
        "hessian_or_source_vector_packet",
        "sector_response_matrix_packet",
    }, "required input keys mismatch")
    require(summary["conditional_rank"] == 2, "rank mismatch")
    require(summary["conditional_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["conditional_A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["conditional_deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(summary["conditional_b_norm_sq"] == 24.0, "b norm mismatch")

    upstream = data["upstream_candidate"]
    for key in [
        "residual_projector_axiom_appendix_drafts_written",
        "galerkin_first_execution_schema_fixed",
        "route_A_and_route_B_locked_to_same_72_real_target",
        "next_input_files_declared",
        "observed_constants_excluded_as_selectors",
    ]:
        require(upstream["what_closes_now"][key] is True, f"close flag missing: {key}")
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
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")
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
        require(upstream["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    axiom = data["upstream_packets"]["axiom_insertion_package"]
    galerkin = data["upstream_packets"]["galerkin_first_execution_spec"]
    decision = data["upstream_packets"]["route_decision_and_next_inputs"]
    require(axiom["inserted_into_main_corpus_now"] is False, "axiom patch overclaimed")
    require(galerkin["first_execution_run_now"] is False, "Galerkin run overclaimed")
    require(decision["recommended_next"] == NEXT, "decision next mismatch")
    require("Two superset paths" in decision["superset_strategy"], "strategy missing")

    guard = data["guardrails"]
    for key in [
        "claims_main_corpus_axiom_patch_applied",
        "claims_residual_projector_axiom_proved",
        "claims_first_Galerkin_C1_execution_run",
        "claims_A_selected",
        "claims_b_selected",
        "claims_deltaTheta_C1",
        "claims_SM_parity_dynamic_packet_closure",
        "claims_true_SM_equivalence_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("Route A: residual-projector axiom appendix draft" in note, "note missing Route A")
    require("Route B: honest Galerkin C1 first-execution spec" in note, "note missing Route B")
    require("Nothing is promoted yet" in note, "note missing guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
