from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_tt_metric_shape_map_image_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    packet = json.loads(Path(cert["candidate_packet_written"]).read_text(encoding="utf-8"))

    require(cert["status"] == "BTT_IMAGE_THEOREM_FORMULATED_CONDITIONAL_PACKET_READY", "unexpected status")
    source = cert["source_tests"]
    theorem = cert["theorem"]
    decision = cert["decision"]
    guards = cert["guardrails"]

    require(source["qg_metric_shape_map_defined_as_DG_Pi"] is True, "metric shape map not sourced")
    require(source["qg_shape_map_factorized_with_Aint_window"] is True, "shape map factorization not sourced")
    require(source["gr_metric_is_observable_pushforward"] is True, "GR pushforward not sourced")
    require(source["central_circle_gravity_operates_on_shared_circle"] is True, "central gravity channel missing")
    require(source["central_circle_unique_shared_gravity_channel"] is True, "central unique channel missing")
    require(source["uniqueness_for_spin2_z64_window_closed"] is True, "uniqueness not closed")
    require(source["helicity2_functor_compresses_to_15"] is True, "compression not closed")
    require(source["source_computes_BTT_image_in_exact_branch"] is False, "BTT image unexpectedly sourced")
    require(source["source_proves_BTT_central_circle_equivariance_weight2"] is False, "BTT weight unexpectedly sourced")

    require(packet["schema"] == "SelectedTTMetricShapeMapImage.v1", "wrong packet schema")
    require(packet["required_properties"]["B_TT_central_circle_weight"] == 2, "packet should require weight 2")
    require(packet["if_valid_then_lambda_GR_TT"] == 15.0, "packet consequence should be 15")

    require(theorem["closed_unconditionally"] is False, "must not close unconditionally")
    require(theorem["closed_conditionally_on_packet"] is True, "conditional theorem should close")
    require(theorem["conditional_conclusion"]["lambda_GR_TT"] == 15.0, "conditional lambda should be 15")
    require("weight 2" in " ".join(theorem["conditional_hypotheses"]), "lost weight hypothesis")

    require(decision["why_not_fully_closed"].startswith("The current corpus defines"), "decision should explain open gate")
    require("direct computation" in note, "note should mention direct computation")

    require(guards["claims_BTT_image_computed"] is False, "must not claim BTT image")
    require(guards["claims_unconditional_lambda_GR_TT_15"] is False, "must not claim unconditional 15")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")
    require(guards["uses_observed_GR_data"] is False, "must not use observed GR")

    print("AUDIT_PASS: selected TT metric shape-map image theorem formulated; packet ready")


if __name__ == "__main__":
    main()
