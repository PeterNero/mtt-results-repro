"""Audit Route A emission or Route B Galerkin-row execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routeaemission_or_routebgalerkinrows_execution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ENGINE = PACKET_DIR / "finite_weyl_trace_quadrature_engine.packet.json"
ROWS = PACKET_DIR / "formal_110_row_execution.packet.json"
PROMOTION = PACKET_DIR / "routeb_promotion_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteAEmissionOrRouteBGalerkinRowsExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_ROUTEAEMISSION_OR_ROUTEBGALERKINROWSEXECUTION_BUILT_FORMAL_ROWS_EXECUTED_PHYSICAL_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalMeasureOrFiniteGalerkinPromotion_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    engine = load(ENGINE)
    rows = load(ROWS)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(engine["status"] == "FINITE_WEYL_TRACE_ENGINE_BUILT_EXACT_FORMAL_QUADRATURE", "engine status mismatch")
    require(engine["weyl_identities"]["Z_cubed_identity"] is True, "Z identity missing")
    require(engine["weyl_identities"]["X_cubed_identity"] is True, "X identity missing")
    require(engine["weyl_identities"]["trace_orthogonality_basis_size"] == 9, "basis size mismatch")
    require(abs(engine["residual_sources_recomputed"]["R_Z_norm_sq"] - 4.0) < 1e-12, "R_Z norm mismatch")
    require(abs(engine["residual_sources_recomputed"]["R_X_norm_sq"] - 2.0) < 1e-12, "R_X norm mismatch")
    require(engine["independent_of_observed_constants"] is True, "observed guardrail missing")
    require(engine["independent_of_target_residual_selection"] is True, "target guardrail missing")
    require(engine["physical_measure_promoted_now"] is False, "physical measure overclaimed")

    require(rows["status"] == "FORMAL_110_ROWS_EXECUTED_BY_FINITE_WEYL_TRACE_QUADRATURE_PHYSICAL_PROMOTION_OPEN", "rows status mismatch")
    counts = rows["row_counts"]
    require(counts["primitive_rows"] == 72, "primitive row count mismatch")
    require(counts["hessian_source_rows"] == 2, "hessian row count mismatch")
    require(counts["sector_matrix_rows"] == 36, "sector row count mismatch")
    require(counts["total_rows"] == 110, "total row count mismatch")
    require(len(rows["primitive_kernel_values"]) == 72, "primitive rows length mismatch")
    require(len(rows["hessian_source_values"]) == 2, "hessian rows length mismatch")
    require(len(rows["sector_matrix_values"]) == 36, "sector rows length mismatch")
    require(rows["comparison_to_prior_algebraic_replay"]["max_abs_error"] < 1e-12, "replay comparison too large")
    require(rows["comparison_to_prior_algebraic_replay"]["matches_prior_replay_under_finite_trace_engine"] is True, "replay comparison mismatch")
    require(rows["comparison_to_prior_algebraic_replay"]["prior_replay_used_as_selector"] is False, "replay used as selector")
    require(rows["independent_formal_rows_executed_now"] is True, "formal rows not executed")
    require(rows["physical_rows_promoted_now"] is False, "physical rows overclaimed")

    require(promotion["status"] == "FORMAL_ROUTE_B_ROWS_EXECUTED_PHYSICAL_ROUTE_B_STILL_OPEN", "promotion status mismatch")
    route_b = promotion["route_B_state_after_exact_finite_quadrature"]
    require(route_b["independent_formal_rows_executed_now"] is True, "formal route B rows missing")
    require(route_b["strict_72_real_coordinate_target_filled"] is True, "72-real target missing")
    require(route_b["total_110_rows_filled"] is True, "110 rows missing")
    require(route_b["A_selected_formal"] == [[12.0, 0.0], [0.0, 12.0]], "formal A mismatch")
    require(route_b["b_selected_formal"] == [12.0, 12.0], "formal b mismatch")
    require(route_b["deltaTheta_C1_formal"] == [1.0, 1.0], "formal delta mismatch")
    require(route_b["sector_response_matrices_formal"] is True, "formal sector matrices missing")
    require(route_b["physical_measure_or_selected_Galerkin_promotion"] is False, "physical route B overclaimed")
    require(route_b["route_B_closes_now"] is False, "route B closure overclaimed")
    require(len(promotion["why_physical_promotion_remains_open"]) == 3, "physical guardrails missing")

    for key in [
        "finite_weyl_trace_quadrature_engine_built",
        "formal_110_rows_executed",
        "formal_A_b_deltaTheta_emitted",
        "sector_response_matrices_formally_emitted",
        "prior_replay_match_checked_not_selected",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_measure_equals_finite_trace_quadrature",
        "selected_Galerkin_replacement_promotes_formal_rows",
        "route_A_same_source_emission",
        "physical_A_selected",
        "physical_b_selected",
        "physical_deltaTheta_C1",
        "physical_sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    require(data["promotion_decision"]["formal_rows_executed"] is True, "formal execution flag missing")
    for key, value in data["promotion_decision"].items():
        if key != "formal_rows_executed":
            require(value is False, f"promotion overclaimed: {key}")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require("formal total rows executed     = 110" in note, "note missing row count")
    require("physical Route B promoted      = False" in note, "note missing promotion guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
