"""Validate the imported HYM-to-dynamic-C1 source-rule frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "selected_routec_hym_dynamic_c1_sourcerule_frontier.import.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    claims = packet["verified_claims"]
    numeric = packet["numeric_payload"]
    routing = packet["static_sector_routing"]
    frontier = packet["dynamic_c1_frontier"]

    require(packet["status"] == "IMPORTED_HYM_DYNAMIC_C1_SOURCE_RULE_FRONTIER_OPEN", "bad status")
    require(packet["closure_claimed"] is False, "closure must not be claimed")
    require(packet["target_fitting_used"] is False, "target fitting must be false")
    require(packet["observed_physical_data_used"] is False, "observed data selector must be false")

    require(claims["diagonal_End0_connection_formula_emitted"] is True, "End0 D_E missing")
    require(claims["protected_T3_Riesz_Green_closed"] is True, "T3 Green missing")
    require(claims["T1_T2_covariant_Green_closed"] is True, "T1/T2 Green missing")
    require(claims["row_model_offdiagonal_Ext_control_closed"] is True, "offdiagonal control missing")
    require(claims["static_weyl_sector_routing_closed"] is True, "static routing missing")
    require(claims["physical_dotD_alpha1_removed_from_active_frontier"] is True, "dotD frontier not retired")
    require(claims["dynamic_C1_candidate_values_ready"] is True, "dynamic values not ready")
    require(claims["differentiated_PhiFinC1_source_rule_derived"] is False, "source rule should remain open")
    require(claims["honest_selected_Galerkin_C1_tables_exported"] is False, "Galerkin table export should remain open")
    require(claims["axiom_promotion_package_ready"] is True, "axiom package missing")

    require(numeric["T3_green"]["green_residual_l2"] < 1e-12, "T3 Green residual too large")
    require(numeric["T1T2_covariant_green"]["gauge_frame_residual_l2"] < 1e-12, "T1/T2 Green residual too large")
    require(numeric["Ext_density_tangent"]["residual_l2"] < 1e-12, "Ext tangent residual too large")
    require(numeric["End0_DE_direction_l2"]["y2"] > numeric["End0_DE_direction_l2"]["x2"], "direction l2 sanity failed")

    require(routing["proved"] is True, "static routing not proved")
    require(routing["clock_phase_side"]["sectors"] == ["u", "e"], "phase route changed")
    require(routing["shift_non10_side"]["sectors"] == ["d", "nuD"], "shift route changed")
    require(routing["selected_static_trace_transfer_normalization_emitted"] is True, "static trace normalization missing")
    require(routing["promotes_conditional_A_to_A_selected"] is False, "A_selected overpromoted")

    require(frontier["conditional_hessian_values_attached"] is True, "conditional Hessian values missing")
    require(frontier["exact_phase_R_Z_candidate_table_emitted"] is True, "phase table missing")
    require(frontier["exact_shift_R_X_candidate_table_emitted"] is True, "shift table missing")
    require(frontier["source_rule_or_galerkin_export_is_only_remaining_dynamic_gate"] is True, "frontier not sharpened")

    print("Route-C HYM-to-dynamic-C1 source-rule frontier import PASS")
    print("status", packet["status"])
    print("next", packet["next_required_artifact"])


if __name__ == "__main__":
    main()
