"""Audit independent Galerkin C1 contractions / residual-projector axiom derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INDEPENDENCE_AUDIT = PACKET_DIR / "independence_dependency_audit.packet.json"
DERIVATION_LADDER = PACKET_DIR / "residual_projector_derivation_ladder.packet.json"
NEXT_CONTRACT = PACKET_DIR / "minimal_next_source_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_INDEPENDENTGALERKINC1CONTRACTIONS_OR_DERIVERESIDUALPROJECTORAXIOM_BUILT_DEPENDENCY_CUTSET_OPEN"
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    independence = load(INDEPENDENCE_AUDIT)
    ladder = load(DERIVATION_LADDER)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(independence["status"] == "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT", "independence status mismatch")
    require(independence["zero_mode_basis"]["declared"] is True, "zero basis missing")
    require(independence["zero_mode_basis"]["selected_source_verified"] is False, "zero basis oververified")
    require(independence["primitive_contractions"]["present"] is True, "primitive missing")
    require(independence["primitive_contractions"]["computed_from_independent_galerkin_quadrature"] is False, "primitive independence overclaimed")
    require(independence["hessian_source"]["present"] is True, "hessian missing")
    require(independence["hessian_source"]["b_selected_emitted_by_independent_hessian"] is False, "b independence overclaimed")
    require(independence["first_run_result"]["strict_replay_passes"] is True, "strict replay missing")
    require(independence["first_run_result"]["honest_independent_galerkin_execution_passes"] is False, "honest Galerkin overclaimed")
    require(len(independence["independence_obstruction"]) == 3, "obstruction list mismatch")

    require(ladder["status"] == "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN", "ladder status mismatch")
    levels = ladder["levels"]
    require(levels["L0_trace_orthogonal_uniqueness"]["closed"] is True, "L0 not closed")
    require(levels["L1_minimal_norm_completion"]["closed_conditionally"] is True, "L1 conditional not set")
    require(levels["L2_physical_PhiFinC1_application"]["closed"] is False, "L2 overclosed")
    require(levels["L3_independent_quadrature_hessian"]["closed"] is False, "L3 overclosed")
    require(ladder["what_is_now_theorem_derived"]["unique_Q_residual_given_fixed_fiber_span"] is True, "Q uniqueness missing")
    require(ladder["what_is_not_theorem_derived"]["physical_differentiated_PhiFinC1_applies_Q_residual"] is True, "PhiFinC1 gap missing")

    require(contract["status"] == "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED", "contract status mismatch")
    require(contract["option_A_derive_principle"]["name"] == "DifferentiatedC1OrthogonalCompletionPrinciple", "option A name mismatch")
    require(len(contract["option_A_derive_principle"]["would_promote"]) == 4, "option A promotion list mismatch")
    require(contract["option_B_compute_values"]["name"] == "IndependentGalerkinQuadratureHessianSolve", "option B name mismatch")
    require(len(contract["option_B_compute_values"]["required_values"]) == 6, "option B values mismatch")
    require(contract["recommended_next"] == NEXT, "recommended next mismatch")

    for key in [
        "dependency_cutset_identified",
        "algebraic_Q_residual_uniqueness_reaffirmed",
        "minimal_orthogonal_completion_principle_is_sufficient_if_derived",
        "independent_Galerkin_value_requirements_are_exact",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "derive_differentiated_C1_orthogonal_completion_principle",
        "prove_physical_PhiFinC1_applies_Q_residual",
        "emit_independent_selected_zero_mode_basis",
        "compute_independent_primitive_contractions",
        "emit_independent_hessian_b_selected",
        "close_unpatched_SM_parity_dynamic_packet",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    decision = data["promotion_decision"]
    require(decision["patched_spine_closure_preserved"] is True, "patched closure not preserved")
    require(decision["unpatched_A_selected_promoted"] is False, "unpatched A overclaim")
    require(decision["unpatched_b_selected_promoted"] is False, "unpatched b overclaim")
    require(decision["independent_Galerkin_C1_closed"] is False, "independent Galerkin overclaim")
    require(decision["residual_projector_axiom_derived_from_unpatched_MTT"] is False, "axiom derivation overclaim")
    require(decision["unpatched_SM_parity_dynamic_packet_closed"] is False, "unpatched closure overclaim")
    require(data["closure_claimed"] is False, "global closure overclaimed")
    require(data["patched_spine_closure_preserved"] is True, "patched closure flag missing")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require("true dependency" in note, "note missing dependency summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
