"""Validate the imported Route-C operator-source frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "selected_routec_operator_source_frontier.import.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    claims = packet["verified_claims"]
    rejection = packet["same_source_packet_rejection"]
    frontier = packet["operator_source_identity_frontier"]
    lanes = packet["live_lanes"]

    require(packet["status"] == "IMPORTED_OPERATOR_SOURCE_FRONTIER_OPEN", "bad status")
    require(packet["closure_claimed"] is False, "closure must not be claimed")
    require(packet["target_fitting_used"] is False, "target fitting must be false")
    require(packet["observed_physical_data_used"] is False, "observed data selector must be false")

    require(claims["source_level_gerbe_weyl_carrier_closed"] is True, "source-level carrier not imported")
    require(claims["active_shift_1_1_forced"] is True, "active shift not forced")
    require(claims["primitive_only_span_insufficient"] is True, "primitive no-go missing")
    require(claims["conditional_weylpair_transfer_exact"] is True, "conditional transfer not exact")
    require(claims["selected_A_selected_emitted"] is False, "A_selected should remain open")
    require(claims["selected_operator_source_closed"] is False, "operator source should remain open")
    require(claims["same_source_packet_validator_rejects_current_fill"] is True, "validator rejection missing")

    require(rejection["required_fields"] == 7, "unexpected same-source field count")
    require(rejection["selected_emitted"] == 0, "selected emissions should still be zero")
    require(rejection["support_present"] == 6, "unexpected support-only field count")
    require("singlet_neutrino_rule" in rejection["missing_or_unselected_fields"], "1_M rule gap missing")

    require(frontier["source_level_not_operator_level"] is True, "source/operator distinction missing")
    require(frontier["operator_level_projective_rhoE_still_open"] is True, "operator rhoE gap missing")
    require(frontier["visible_operator_source_closed"] is False, "visible operator source incorrectly closed")

    rank2 = lanes["rank2_non_split_valpha"]
    routec = lanes["route_c_finite_hym_strominger"]
    require(rank2["priority"] == 1, "rank2 lane should be primary")
    require(routec["priority"] == 2, "Route-C residual lane should be parallel fallback")
    require(rank2["target_l_vector_abc"] == [1, -2, 0], "rank2 L vector changed")
    require(routec["blocked_by"]["actual_selected_rho_E_values"] is True, "rho_E value gap missing")

    print("Route-C operator-source frontier import PASS")
    print("status", packet["status"])
    print("next", packet["next_required_artifact"])


if __name__ == "__main__":
    main()
