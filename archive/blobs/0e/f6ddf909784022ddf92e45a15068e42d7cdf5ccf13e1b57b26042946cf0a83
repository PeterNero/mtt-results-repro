"""Audit Galerkin C1 input-basis fill / residual-projector axiom corpus patch."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INPUT_DIR = PACKET_DIR / "inputs"
ZERO_MODE = INPUT_DIR / "zero_mode_basis.packet.json"
PRIMITIVE_TERMS = INPUT_DIR / "primitive_contraction_terms.packet.json"
HESSIAN_SOURCE = INPUT_DIR / "hessian_source_vector.packet.json"
SECTOR_MATRICES = INPUT_DIR / "sector_response_matrices.packet.json"
FIRST_RUN = PACKET_DIR / "first_galerkin_replay_result.packet.json"
CORPUS_PATCH = PACKET_DIR / "residual_projector_axiom_local_corpus_patch.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1.md"
PATCH_NOTE = ROOT / "proof_corpus" / "MTT_DifferentiatedPhiFinC1ResidualProjectorAxiom_LocalCorpusPatch_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_GALERKINC1INPUTBASISFILL_OR_RESIDUALPROJECTORAXIOMCORPUSPATCH_BUILT_DUAL_ATTEMPT_CONDITIONAL_CLOSE"
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    zero = load(ZERO_MODE)
    primitive = load(PRIMITIVE_TERMS)
    hessian = load(HESSIAN_SOURCE)
    sectors = load(SECTOR_MATRICES)
    first_run = load(FIRST_RUN)
    patch = load(CORPUS_PATCH)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    patch_note = PATCH_NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(zero["status"] == "CANONICAL_QUTRIT_MATRIX_UNIT_BASIS_FILLED_SUPPORT_LEVEL", "zero-mode status mismatch")
    require(zero["basis_dimension"] == 9, "zero-mode dimension mismatch")
    require(len(zero["basis"]) == 9, "zero-mode basis count mismatch")
    require(zero["selected_source_verified"] is False, "zero-mode source oververified")

    require(primitive["status"] == "RESIDUAL_PROJECTOR_CONTRACTION_TERMS_FILLED_FROM_AXIOM_CONTRACT", "primitive status mismatch")
    require(primitive["computed_from_independent_galerkin_quadrature"] is False, "primitive independence overclaimed")
    require(primitive["selected_source_verified"] is False, "primitive source oververified")
    require(primitive["sector_routing"] == {"u": "phase_clock_R_Z", "e": "phase_clock_R_Z", "d": "shift_vertex_R_X", "nuD": "shift_vertex_R_X"}, "sector routing mismatch")
    require(primitive["terms"]["phase_clock_R_Z"]["residual_norm_sq"] == 4.0, "phase residual mismatch")
    require(primitive["terms"]["shift_vertex_R_X"]["residual_norm_sq"] == 2.0, "shift residual mismatch")

    require(hessian["status"] == "B_SELECTED_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT", "hessian status mismatch")
    require(hessian["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(hessian["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(hessian["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(hessian["b_selected_emitted_by_independent_hessian"] is False, "independent b overclaimed")
    require(hessian["b_selected_replay_available_under_axiom_patch"] is True, "patched b missing")

    require(sectors["status"] == "SECTOR_RESPONSE_MATRICES_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT", "sector status mismatch")
    require(sectors["independent_sector_matrices_emitted"] is False, "sector independence overclaimed")
    require(set(sectors["sector_responses"]) == {"u", "e", "d", "nuD"}, "sector set mismatch")

    require(first_run["status"] == "STRICT_REPLAY_PASSES_BUT_NOT_INDEPENDENT_HONEST_GALERKIN", "first-run status mismatch")
    require(first_run["strict_replay_passes"] is True, "strict replay failed")
    require(first_run["honest_independent_galerkin_execution_passes"] is False, "honest Galerkin overclaimed")
    require(first_run["acceptance_results"]["A_selected_rank_at_least_2"] is True, "rank acceptance missing")
    require(first_run["acceptance_results"]["observed_flavor_constants_not_used_as_selectors"] is True, "observed guard missing")
    require(len(first_run["why_independent_execution_not_closed"]) == 3, "independent gap list mismatch")

    require(patch["status"] == "LOCAL_PROOF_CORPUS_PATCH_APPLIED_GUARDED_AXIOM", "patch status mismatch")
    require(patch["after_patch_promotions_in_patched_spine"]["SM_parity_dynamic_packet"] is True, "patched dynamic closure missing")
    require(patch["after_patch_promotions_in_patched_spine"]["no_knob_flavor_constants"] is False, "no-knob overclaim")
    require(patch["main_external_obsidian_papers_modified_now"] is False, "external paper mutation overclaimed")
    require("not yet a derivation from unpatched MTT axioms" in patch_note, "patch note missing guardrail")

    require(data["route_A_result"]["local_corpus_axiom_patch_applied"] is True, "Route A patch missing")
    require(data["route_A_result"]["closes_SM_parity_dynamic_packet_in_patched_spine"] is True, "Route A closure missing")
    require(data["route_A_result"]["closes_unpatched_or_derived_MTT_theorem"] is False, "Route A unpatched overclaim")
    require(data["route_B_result"]["input_packets_filled"] is True, "Route B input fill missing")
    require(data["route_B_result"]["strict_replay_passes"] is True, "Route B replay missing")
    require(data["route_B_result"]["honest_independent_galerkin_execution_passes"] is False, "Route B independence overclaim")

    for key in [
        "local_residual_projector_axiom_patch_applied",
        "patched_spine_dynamic_packet_closure",
        "galerkin_input_packets_filled",
        "first_strict_galerkin_replay_passes",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "derive_residual_projector_axiom_from_unpatched_MTT",
        "patch_external_main_papers_if_user_approves",
        "emit_independent_selected_zero_mode_basis",
        "compute_independent_primitive_galerkin_contractions",
        "emit_independent_hessian_b_selected",
        "promote_unpatched_A_selected",
        "promote_unpatched_b_selected",
        "true_SM_equivalence_closure_without_local_axiom",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    decision = data["promotion_decision"]
    require(decision["SM_parity_dynamic_packet_closed_in_patched_spine"] is True, "patched closure missing")
    require(decision["A_selected_promoted_in_unpatched_spine"] is False, "unpatched A overclaim")
    require(decision["b_selected_promoted_in_unpatched_spine"] is False, "unpatched b overclaim")
    require(decision["honest_independent_Galerkin_C1_closed"] is False, "honest Galerkin overclaim")
    require(data["patched_spine_closure_claimed"] is True, "patched closure claim missing")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["closure_claimed"] is False, "global closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require("Both routes were tried" in note, "note missing dual route result")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
