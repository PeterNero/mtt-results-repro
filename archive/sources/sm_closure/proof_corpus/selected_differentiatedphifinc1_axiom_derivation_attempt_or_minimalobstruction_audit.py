"""Audit PhiFin C1 source-axiom derivation attempt and minimal obstruction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_differentiatedphifinc1_axiom_derivation_attempt_or_minimalobstruction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_unpatched_clause_attack.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_galerkin_attack.packet.json"
OBSTRUCTION = PACKET_DIR / "minimal_derivation_obstruction.packet.json"
DECISION = PACKET_DIR / "axiom_derivation_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1_AxiomDerivationAttempt_or_MinimalObstruction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_AXIOM_DERIVATION_ATTEMPT_BUILT_MINIMAL_OBSTRUCTION_OPEN"
NEXT = "MTT_Selected_PhiFinC1PhysicalVariationSourceTheorem_or_IndependentGalerkinC1Export_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    obstruction = load(OBSTRUCTION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(data["theorem_attempt"]["proved"] is False, "axiom derivation overclaimed")
    require(data["theorem_attempt"]["derived_axiom_now"] is False, "axiom derived flag overclaimed")
    require(data["closure_decision"]["global_closure_claimed"] is False, "global closure overclaimed")
    require(data["closure_decision"]["local_patched_dynamic_C1_closed"] is True, "local patched closure lost")
    require(data["closure_decision"]["unpatched_source_axiom_derived_now"] is False, "unpatched axiom overderived")

    require(route_a["status"] == "ROUTE_A_ATTACK_SUPPORT_COMPLETE_SOURCE_THEOREM_NOT_DERIVED", "Route A status mismatch")
    require(route_a["route_A_closed_now"] is False, "Route A overclosed")
    require(route_a["route_A_would_close_if_theorem_supplied"] is True, "Route A conditional witness missing")
    require(route_a["new_derivation_found_now"] is False, "Route A falsely found derivation")
    for name, clause in route_a["required_axiom_clauses"].items():
        require(clause["closed_now"] is False, f"Route A clause unexpectedly closed: {name}")
        require(clause["conditional_witness_value"] is True, f"Route A conditional missing: {name}")
        require(clause["current_packet_value"] is False, f"Route A current value mismatch: {name}")
    for name, value in route_a["current_route_A_emissions"].items():
        require(value is False, f"current Route A emission unexpectedly true: {name}")
    for name, value in route_a["conditional_route_A_emissions"].items():
        require(value is True, f"conditional Route A emission unexpectedly false: {name}")

    require(route_b["status"] == "ROUTE_B_STRICT_REPLAY_PASSES_BUT_INDEPENDENT_SELECTION_OPEN", "Route B status mismatch")
    require(route_b["route_B_closed_now"] is False, "Route B overclosed")
    require(route_b["new_independent_execution_found_now"] is False, "Route B falsely found independent run")
    flags = route_b["independence_flags"]
    require(flags["strict_replay_passes"] is True, "strict replay should pass")
    require(flags["honest_independent_galerkin_execution_passes"] is False, "honest Galerkin overclaimed")
    require(flags["zero_mode_selected_source_verified"] is False, "zero-mode selected source overclaimed")
    require(flags["primitive_terms_selected_source_verified"] is False, "primitive source overclaimed")
    require(flags["primitive_terms_computed_from_independent_galerkin_quadrature"] is False, "quadrature overclaimed")
    require(flags["b_selected_emitted_by_independent_hessian"] is False, "independent b_selected overclaimed")
    require(flags["sector_matrices_emitted_independently"] is False, "sector matrices overclaimed")
    locked = route_b["locked_target"]
    require(locked["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(locked["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(locked["b_norm_sq"] == 24.0, "b norm mismatch")
    require(locked["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(locked["passes_locked_target"] is True, "locked target failed")

    require(
        obstruction["status"] == "MINIMAL_OBSTRUCTION_IS_SELECTED_PHYSICAL_SOURCE_BINDING_NOT_LINEAR_ALGEBRA",
        "obstruction status mismatch",
    )
    for name, value in obstruction["not_blockers"].items():
        require(value is True, f"not-blocker not closed: {name}")
    require(obstruction["minimal_new_lemma"]["would_derive_local_axiom"] is True, "lemma does not derive axiom")
    require(obstruction["minimal_new_lemma"]["currently_proved"] is False, "lemma overproved")
    require("same-source physical selection theorem" in obstruction["actual_obstruction"], "obstruction text too weak")

    require(decision["status"] == "AXIOM_NOT_DERIVED_YET_MINIMAL_PROOF_TARGET_IDENTIFIED", "decision status mismatch")
    require(decision["local_patched_dynamic_C1_closed"] is True, "decision lost local closure")
    require(decision["unpatched_source_axiom_derived_now"] is False, "decision overderived axiom")
    require(decision["route_A_closed_now"] is False, "decision overclosed Route A")
    require(decision["route_B_closed_now"] is False, "decision overclosed Route B")
    require(decision["honest_galerkin_independent"] is False, "decision overclaimed honest Galerkin")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset paths treated as knobs")

    for key in [
        "route_A_attacked",
        "route_B_attacked",
        "minimal_obstruction_identified",
        "values_and_linear_algebra_ruled_out_as_blockers",
        "local_axiom_closure_preserved",
    ]:
        require(data["what_was_achieved"][key] is True, f"achievement missing: {key}")
    for key in [
        "selected_phifinc1_physical_variation_source_theorem",
        "selected_admissible_variations_and_boundary_cancellation",
        "same_source_b_selected_emission",
        "independent_selected_galerkin_hessian_export",
        "true_SM_equivalence_without_axiom",
        "no_knob_flavor_constants",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    require("Result: the axiom is not derived yet" in note, "note missing non-derivation guard")
    require("not the C1 linear algebra" in note, "note missing minimal obstruction")
    require(NEXT in note, "note missing next target")

    for packet in [data, route_a, route_b, obstruction, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
