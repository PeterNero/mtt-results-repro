"""Audit physical C1 variation source-promotion / independent quadrature execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION = PACKET_DIR / "physical_c1_variation_source_promotion_attempt.packet.json"
QUADRATURE = PACKET_DIR / "independent_quadrature_execution_attempt.packet.json"
EQUIV = PACKET_DIR / "necessary_sufficient_cycle_exit_theorem.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalC1VariationSourcePromotion_or_IndependentQuadratureExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALC1VARIATION_SOURCEPROMOTION_OR_INDEPENDENTQUADRATUREEXECUTION_BUILT_NECESSARY_SUFFICIENT_OPEN"
NEXT = "MTT_Selected_C1VariationPrincipleDerivation_or_QuadratureEngineRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    promotion = load(PROMOTION)
    quadrature = load(QUADRATURE)
    equiv = load(EQUIV)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(promotion["status"] == "PROMOTION_ATTEMPT_SUPPORT_COMPLETE_PRINCIPLE_UNDERIVED", "promotion status mismatch")
    support = promotion["support_closed"]
    for key in [
        "canonical_Q_residual_available",
        "alpha1_dotD_driver_verified",
        "selected_qutrit_weyl_carrier",
        "selected_static_routes",
        "selected_trace_transfer_normalization",
        "finite_variational_euler_projection",
        "least_norm_completion_selects_Q_residual",
        "replay_rows_pass_locked_target",
    ]:
        require(support[key] is True, f"support missing: {key}")
    missing = promotion["missing_for_unpatched_promotion"]
    require(missing["derive_or_insert_physical_C1_variation_principle"] is True, "variation principle gap missing")
    require(missing["prove_selected_PhiFinC1_applies_Q_residual"] is True, "Q application gap missing")
    require(missing["prove_boundary_cancellation_for_selected_dynamic_trace"] is True, "boundary gap missing")
    require(promotion["local_patch_would_close_dynamic_packet"]["if_accepted"] is True, "patch sufficiency missing")
    require(promotion["unpatched_promotion_now"] is False, "unpatched promotion overclaimed")

    require(quadrature["status"] == "INDEPENDENT_EXECUTION_NOT_RUN_REPLAY_TARGET_AVAILABLE", "quadrature status mismatch")
    require(quadrature["available_as_replay_not_independent"]["primitive_rows"] == 36, "replay row count mismatch")
    require(quadrature["available_as_replay_not_independent"]["locked_target"]["passes_locked_target"] is True, "locked replay missing")
    for key in [
        "selected_quadrature_engine_or_rule",
        "primitive_three_by_three_contraction_integrals",
        "independent_hessian_source_vector",
        "sector_response_matrices",
        "error_bounds_or_exactness_certificate",
    ]:
        require(quadrature["missing_independent_execution"][key] is True, f"quadrature gap missing: {key}")
    require(quadrature["independent_execution_now"] is False, "independent execution overclaimed")

    require(equiv["status"] == "CYCLE_EXIT_EQUIVALENCE_PROVED_PAYLOAD_OPEN", "equivalence status mismatch")
    require("equivalent to either Route A" in equiv["statement"], "equivalence statement mismatch")
    require(equiv["locked_target"]["passes_locked_target"] is True, "equiv locked target mismatch")
    require("promoting replay-backed rows as independent quadrature" in equiv["forbidden_shortcuts"], "shortcut guardrail missing")
    require("promoting local axiom patch as unpatched theorem" in equiv["forbidden_shortcuts"], "patch guardrail missing")

    for key in [
        "cycle_exit_equivalence_proved",
        "physical_variation_source_promotion_attempted",
        "independent_quadrature_execution_requirements_fixed",
        "local_patch_sufficiency_separated_from_unpatched_closure",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "derive_physical_C1_variation_principle",
        "prove_boundary_cancellation_for_selected_dynamic_trace",
        "promote_selected_physical_Q_residual_application",
        "emit_independent_primitive_quadrature_integrals",
        "emit_independent_hessian_source_vector",
        "emit_independent_sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("exact equivalence" in note and "Route B independent quadrature run   = False" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
