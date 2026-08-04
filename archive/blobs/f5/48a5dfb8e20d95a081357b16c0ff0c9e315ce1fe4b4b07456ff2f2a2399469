"""Validate the imported Route-C HYM operator-values frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "selected_routec_hym_operatorvalues_frontier.import.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    claims = packet["verified_claims"]
    rank2 = packet["rank2_l2_report"]
    global_destab = packet["global_destabilizer_report"]
    frontier = packet["current_frontier"]

    require(packet["status"] == "IMPORTED_HYM_OPERATOR_VALUES_FRONTIER_OPEN", "bad status")
    require(packet["closure_claimed"] is False, "closure must not be claimed")
    require(packet["target_fitting_used"] is False, "target fitting must be false")
    require(packet["observed_physical_data_used"] is False, "observed data selector must be false")

    require(claims["rank2_l2_cohomology_input_closed"] is True, "rank2 L2 input not closed")
    require(claims["h1_value"] == 8, "unexpected h1")
    require(claims["nonzero_ext_class_selected"] is True, "nonzero Ext class not selected")
    require(claims["reduced_ah_global_destabilizer_enumeration_proved"] is True, "global AH enumeration not proved")
    require(claims["rank_one_torsion_free_reflexive_hull_reduction_proved"] is True, "reflexive hull reduction missing")
    require(claims["equalradius_gauduchon_hym_existence_bridge_closed"] is True, "Gauduchon/HYM bridge not closed")
    require(claims["selected_hym_operator_values_emitted"] is False, "operator values should remain open")
    require(claims["selected_DE_Riesz_Green_dotD_emitted"] is False, "DE/Riesz/Green/dotD should remain open")

    require(rank2["h1"] == 8, "rank2 h1 changed")
    require(rank2["extension_class_vector_C1"][0] == 1, "extension class seed changed")
    require(rank2["uses_observed_flavor_inputs"] is False, "observed inputs used")

    require(global_destab["hom_to_L_nonnegative_candidates"] == [], "Hom-to-L should be empty")
    require(len(global_destab["hom_to_Q_nonnegative_candidates"]) == 6, "expected six Hom-to-Q candidates")
    require(global_destab["all_candidates_obstructed"] is True, "central candidates not obstructed")

    require(frontier["abstract_hym_existence_blocker_removed"] is True, "HYM existence blocker not removed")
    require(frontier["operator_values_blocker_open"] is True, "operator value blocker should be open")
    require("D_E" in frontier["required_extraction_chain"], "D_E extraction missing")
    require("C1/overlap matrices" in frontier["required_extraction_chain"], "C1 extraction missing")

    print("Route-C HYM operator-values frontier import PASS")
    print("status", packet["status"])
    print("next", packet["next_required_artifact"])


if __name__ == "__main__":
    main()
