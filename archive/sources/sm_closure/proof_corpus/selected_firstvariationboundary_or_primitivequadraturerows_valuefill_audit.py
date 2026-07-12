"""Audit first-variation boundary / primitive quadrature rows value-fill gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_firstvariationboundary_or_primitivequadraturerows_valuefill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_first_variation_boundary_fill_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_replay_backed_primitive_rows.packet.json"
NEXT_PACKET = PACKET_DIR / "source_promotion_or_independent_quadrature_next.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstVariationBoundary_or_PrimitiveQuadratureRows_ValueFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FIRSTVARIATIONBOUNDARY_OR_PRIMITIVEQUADRATUREROWS_VALUEFILL_REPLAY_ROWS_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalC1VariationSourcePromotion_or_IndependentQuadratureExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(route_a["status"] == "FORMAL_HESSIAN_NORMALIZATION_CLOSED_PHYSICAL_VARIATION_BOUNDARY_OPEN", "route A status mismatch")
    require(route_a["verified_now"]["formal_hessian_or_coercivity"] is True, "hessian not retained")
    require(route_a["verified_now"]["normalization_compatibility"] is True, "normalization not retained")
    require(route_a["verified_now"]["stationary_trace_component_available"] is True, "stationary trace missing")
    require(route_a["verified_now"]["dynamic_dotD_trace_binding_available"] is True, "dynamic trace binding missing")
    require(route_a["still_open"]["physical_first_variation_identity"] is True, "first variation overclosed")
    require(route_a["still_open"]["boundary_cancellation_for_selected_dynamic_trace"] is True, "boundary overclosed")
    require(route_a["can_close_route_A_now"] is False, "route A overclosed")

    require(route_b["status"] == "REPLAY_BACKED_ROWS_BUILT_NOT_INDEPENDENT_QUADRATURE", "route B status mismatch")
    require(route_b["row_count"] == 72, "row count mismatch")
    require(route_b["filled_by_replay_count"] == 36, "replay fill count mismatch")
    require(route_b["independent_quadrature_row_count"] == 0, "independent rows overclaimed")
    require(route_b["acceptance_replay"]["passes_locked_target"] is True, "locked target replay failed")
    require(route_b["projector_guardrail"]["Q_residual_selected_as_canonical_mathematical_projector"] is True, "projector support missing")
    require(route_b["projector_guardrail"]["Q_residual_selected_as_physical_C1_transfer_application"] is False, "physical projector overpromoted")
    require(route_b["can_close_route_B_now"] is False, "route B overclosed")
    replay_rows = [row for row in route_b["rows"] if row["filled_by_replay_now"]]
    require(all(row["independently_quadrature_emitted"] is False for row in replay_rows), "replay rows marked independent")

    require(next_packet["status"] == "NEXT_SOURCE_PROMOTION_OR_INDEPENDENT_EXECUTION_SELECTED", "next packet status mismatch")
    require(next_packet["next_artifact"] == NEXT, "next packet artifact mismatch")
    require("replay-backed primitive row table" in next_packet["closed_now"], "closed-now summary missing")
    require("physical Phi_fin^C1 first variation identity" in next_packet["still_open"], "first variation gap missing")
    require(next_packet["superset_strategy"]["current_combination"].startswith("shared replay target"), "superset guardrail missing")

    for key in [
        "replay_backed_primitive_row_table_built",
        "locked_target_replay_verified",
        "formal_first_variation_hessian_normalization_retained",
        "source_vs_independent_quadrature_boundary_sharpened",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_first_variation_identity",
        "boundary_cancellation_for_selected_dynamic_trace",
        "selected_physical_Q_residual_application",
        "independent_primitive_quadrature_rows",
        "independent_b_selected_hessian_rows",
        "independent_sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("rows filled by replay" in note and "independent quadrature rows    = 0" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
