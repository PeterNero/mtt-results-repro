"""Audit Route-C dual attempt patched-spine import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_dual_attempt_patched_spine_import.candidate.json"
CERT = ROOT / "certificates" / "routec_dual_attempt_patched_spine_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_DualAttemptPatchedSpine_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_dual_attempt_patched_spine.py"

STATUS = "ROUTEC_DUAL_ATTEMPT_PATCHED_SPINE_IMPORTED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


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
    require(data["theorem"]["closure_claimed"] is False, "global closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    summary = data["dual_attempt_summary"]
    require(summary["patched_spine_dynamic_packet_closed"] is True, "patched closure missing")
    require(summary["global_closure_claimed"] is False, "global closure overclaimed")
    require(summary["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(summary["honest_independent_galerkin_closed"] is False, "honest Galerkin overclaimed")
    require(summary["external_obsidian_papers_modified"] is False, "external papers overclaimed")
    require(summary["strict_replay_passes"] is True, "strict replay missing")
    require(summary["total_real_coordinates"] == 72, "target mismatch")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(len(summary["route_B_independence_gaps"]) == 3, "gap list mismatch")

    upstream = data["upstream_candidate"]
    require(upstream["patched_spine_closure_claimed"] is True, "upstream patched claim missing")
    require(upstream["unpatched_theorem_closure_claimed"] is False, "upstream unpatched overclaim")
    require(upstream["closure_claimed"] is False, "upstream global closure overclaim")
    require(upstream["promotion_decision"]["SM_parity_dynamic_packet_closed_in_patched_spine"] is True, "patched closure flag missing")
    require(upstream["promotion_decision"]["A_selected_promoted_in_unpatched_spine"] is False, "unpatched A overclaim")
    require(upstream["promotion_decision"]["b_selected_promoted_in_unpatched_spine"] is False, "unpatched b overclaim")
    require(upstream["promotion_decision"]["honest_independent_Galerkin_C1_closed"] is False, "honest overclaim")

    packets = data["upstream_packets"]
    require(packets["zero_mode_basis"]["selected_source_verified"] is False, "zero-mode oververified")
    require(packets["primitive_contraction_terms"]["computed_from_independent_galerkin_quadrature"] is False, "primitive independence overclaimed")
    require(packets["primitive_contraction_terms"]["selected_source_verified"] is False, "primitive source oververified")
    require(packets["hessian_source_vector"]["b_selected_emitted_by_independent_hessian"] is False, "independent b overclaimed")
    require(packets["sector_response_matrices"]["independent_sector_matrices_emitted"] is False, "sector independence overclaimed")
    require(packets["first_galerkin_replay_result"]["strict_replay_passes"] is True, "replay failed")
    require(packets["first_galerkin_replay_result"]["honest_independent_galerkin_execution_passes"] is False, "honest Galerkin overclaimed")
    require(packets["residual_projector_axiom_local_corpus_patch"]["main_external_obsidian_papers_modified_now"] is False, "external mutation overclaimed")

    for key in [
        "derive_residual_projector_axiom_from_unpatched_MTT",
        "compute_independent_primitive_galerkin_contractions",
        "emit_independent_hessian_b_selected",
        "emit_independent_selected_zero_mode_basis",
        "promote_unpatched_A_selected",
        "promote_unpatched_b_selected",
        "true_SM_equivalence_closure_without_local_axiom",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    for key in [
        "claims_global_SM_closure",
        "claims_unpatched_MTT_derivation",
        "claims_honest_independent_Galerkin_C1",
        "claims_external_papers_patched",
        "claims_no_knob_flavor_constants",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("guarded local residual-projector axiom patch" in note, "note missing patch caveat")
    require("not global SM closure" in note, "note missing global caveat")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
