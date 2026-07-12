from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "central_character_window_premise_source_and_proof_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "CENTRAL_CHARACTER_WINDOW_REDUCED_TO_METRIC_SHAPE_MAP_IMAGE", "unexpected status")
    source = cert["source_tests"]
    routes = cert["proof_routes"]
    decision = cert["decision"]
    guards = cert["guardrails"]

    require(source["gr_observables_are_internal_pushforward_of_coherent_sector"] is True, "GR pushforward missing")
    require(source["gr_metric_shape_map_or_projected_metric_present"] is True, "metric shape/projected metric missing")
    require(source["qg_TT_Aint_projector_window_present"] is True, "QG TT/Aint window missing")
    require(source["central_circle_unique_shared_gravity_channel"] is True, "central gravity channel missing")
    require(source["finite_Z64_carrier_retained_by_Pi_coh_condition_sourced"] is True, "finite carrier condition missing")
    require(source["finite_Wilson_deck_carrier_extraction_criterion_sourced"] is True, "carrier criterion missing")

    require(source["source_explicitly_says_GR_TT_shape_map_lands_in_H0_tensor_K64_tensor_dstar"] is False, "shape image unexpectedly sourced")
    require(source["source_explicitly_says_GR_TT_projector_window_is_central_character_subfiber"] is False, "central window unexpectedly sourced")
    require(source["source_explicitly_says_same_angle_for_TT_and_Z64_central_circle"] is False, "same angle unexpectedly sourced")

    require(routes["direct_source_route"]["status"] == "OPEN", "direct route should remain open")
    require(routes["metric_shape_map_route"]["status"] == "PRECISE_NEXT_PROOF", "metric shape route should be next")
    require(routes["coherence_universality_route"]["status"] == "CONDITIONAL_NOT_ENOUGH_ALONE", "universality route overclosed")
    require(routes["minimal_new_lemma_route"]["status"] == "READY", "minimal lemma should be ready")
    require("lambda_GR,TT=15" in routes["minimal_new_lemma_route"]["consequence"], "lost lambda consequence")

    require(decision["can_close_unconditionally_from_current_sources"] is False, "must not close unconditionally")
    require(decision["can_close_as_conditional_exact_branch_theorem"] is True, "conditional theorem should close")
    require(decision["representation_numeric_part_closed"] is True, "representation part should be closed")
    require(decision["remaining_missing_data_type"] == "metric-shape-map image theorem, not a number", "wrong missing type")

    require("metric-shape-map image theorem" in note, "note lost proof route")
    require("lambda_GR,TT = 15" in note, "note lost lambda")

    require(guards["claims_unconditional_source_premise_closed"] is False, "must not claim premise")
    require(guards["claims_full_GR_TT_gap_15_unconditionally"] is False, "must not claim full gap")
    require(guards["claims_metric_shape_map_image_computed"] is False, "must not claim shape image")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    print("AUDIT_PASS: central-character premise reduced to TT metric shape-map image theorem")


if __name__ == "__main__":
    main()
