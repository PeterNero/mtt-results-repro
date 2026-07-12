from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_c1_first_variation_certificate_fill_or_quadrature_rows_first_run_certificate.json"
STATUS = "POST_ALPHA_C1_FIRST_VARIATION_PARTIAL_FILL_OR_QUADRATURE_BASIS_FIRST_RUN_IMPORTED_OPEN"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "partial-fill theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "I10_proved",
        "route_A_first_variation_certificate_accepted",
        "route_B_basis_rows_accepted",
        "route_B_can_advance_to_primitive_rows",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    route_a = packet["route_A_first_variation_certificate_partial_fill"]
    fields = route_a["filled_fields"]
    require(route_a["certificate_accepted_now"] is False, "route A overaccepted")
    require(fields["hessian_or_coercivity"]["verified"] is True, "formal Hessian/coercivity not closed")
    require(fields["hessian_or_coercivity"]["constant_c"] == 1.0, "coercivity constant drift")
    require(fields["normalization_compatibility"]["verified"] is True, "normalization not closed")
    require(fields["selected_trace_map"]["verified"] is False, "trace map overfilled")
    require(fields["first_variation_identity"]["verified"] is False, "first variation overfilled")
    require(fields["boundary_cancellation"]["verified"] is False, "boundary overfilled")

    route_b = packet["route_B_basis_rows_first_run"]
    require(route_b["row_count"] == 19, "basis row count drift")
    require(route_b["selected_row_count"] == 0, "selected row count drift")
    require(route_b["all_basis_rows_selected"] is False, "basis rows overaccepted")
    require(route_b["can_advance_to_primitive_rows"] is False, "advanced to primitive rows too early")
    require(len(route_b["basis_rows"]) == 19, "basis row stubs missing")
    for row in route_b["basis_rows"]:
        require(row["selected_now"] is False, f"row overselected: {row['basis_id']}")
        require(row["selected_basis_value"] is None, f"basis value overfilled: {row['basis_id']}")
        require(row["selected_projector_value"] is None, f"projector value overfilled: {row['basis_id']}")
        require(row["gram_matrix"] is None, f"Gram overfilled: {row['basis_id']}")
        require(row["spectral_gap"] is None, f"gap overfilled: {row['basis_id']}")

    cutset = packet["next_cutset_after_partial_fill"]
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next artifact drift")
    require(len(cutset["still_blocks_route_A"]) == 3, "route A block count drift")
    require(len(cutset["still_blocks_route_B"]) == 4, "route B block count drift")
    require("selected HYM/Strominger finite trace" in cutset["recommended_next"]["superset_strategy"]["shared_missing_object"], "shared missing object drift")
    require(STATUS in note and NEXT in note and "The I11 certificate is partially filled" in note, "note missing essentials")
    print("AUDIT_PASS: C1 first-variation partial fill imported; shared trace/basis object remains open")


if __name__ == "__main__":
    main()
