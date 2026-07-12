from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_independent_enriched_weylpair_source_provenance_or_galerkin_c1_values_certificate.json"
STATUS = "POST_ALPHA_INDEPENDENT_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_OR_GALERKIN_C1_VALUES_IMPORTED_STATIC_CLOSED_DYNAMIC_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "independent static provenance import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")
    require(cert["frontier_decision"]["static_enriched_weylpair_source_provenance_closed"] is True, "static provenance not closed")
    require(cert["frontier_decision"]["dynamic_C1_values_open_after_static_closure"] is True, "dynamic boundary lost")

    static = packet["static_enriched_weylpair_source_provenance"]
    require(static["status"] == "STATIC_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_CLOSED", "static provenance status drift")
    require(static["provenance_closed"] is True, "static provenance not closed")
    require(static["source_level_carrier"]["phase_Z_source_proved"] is True, "Z source missing")
    require(static["source_level_carrier"]["shift_X_source_proved"] is True, "X source missing")
    require(static["source_level_carrier"]["active_shift_1_1_proved"] is True, "active shift missing")
    require(static["static_sector_route"]["phase_Z_to"] == ["u", "e"], "Z route drift")
    require(static["static_sector_route"]["shift_X_to"] == ["d", "nuD"], "X route drift")
    require(static["static_normalization"]["selected_overlap_transfer_normalization"] is True, "normalization missing")

    dynamic = packet["dynamic_c1_value_boundary"]
    require(dynamic["status"] == "DYNAMIC_C1_VALUES_OPEN_AFTER_STATIC_PROVENANCE", "dynamic boundary status drift")
    require(dynamic["after_static_provenance_closure"]["source_level_weylpair_provenance_open"] is False, "static source still open")
    require(dynamic["after_static_provenance_closure"]["static_sector_routing_open"] is False, "static route still open")
    require(dynamic["after_static_provenance_closure"]["static_transfer_normalization_open"] is False, "static normalization still open")
    require(dynamic["after_static_provenance_closure"]["selected_dynamic_source_to_C1_transfer_tensor_open"] is True, "dynamic tensor overclosed")
    require(dynamic["after_static_provenance_closure"]["selected_primitive_C1_overlap_contractions_open"] is True, "primitive contractions overclosed")
    require(dynamic["dynamic_value_promotion"]["A_selected_promoted"] is False, "A_selected overclaimed")
    require(dynamic["dynamic_value_promotion"]["b_selected_promoted"] is False, "b_selected overclaimed")
    require(dynamic["dynamic_value_promotion"]["deltaTheta_C1_promoted"] is False, "deltaTheta overclaimed")
    require(dynamic["dynamic_value_promotion"]["SM_parity_dynamic_packet_closed"] is False, "SM parity overclaimed")

    galerkin = packet["galerkin_c1_values_fallback"]
    require(galerkin["status"] == "HONEST_GALERKIN_C1_VALUES_STILL_OPEN", "Galerkin status drift")
    require(galerkin["selected_source_verified"] is False, "Galerkin source overclaimed")
    require(galerkin["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True, "Galerkin implication missing")
    require(galerkin["would_close_no_knob_flavor_constants_if_values_emitted"] is False, "Galerkin no-knob overclaim")

    require(STATUS in note and NEXT in note and "static enriched Weyl-pair provenance theorem" in note, "note missing essentials")
    print("AUDIT_PASS: long-chain static enriched Weyl-pair provenance imported; dynamic C1 values remain open")


if __name__ == "__main__":
    main()
