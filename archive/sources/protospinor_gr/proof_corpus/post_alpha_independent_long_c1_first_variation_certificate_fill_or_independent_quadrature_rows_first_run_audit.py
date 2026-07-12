from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_c1_first_variation_certificate_fill_or_independent_quadrature_rows_first_run_certificate.json"
)
STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_C1_FIRST_VARIATION_PARTIAL_FILL_OR_INDEPENDENT_"
    "QUADRATURE_BASIS_FIRST_RUN_REANCHORED_OPEN"
)
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "long-chain partial-fill bridge should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    previous = packet["fresh_previous_certificate"]
    require(previous["theorem"]["proved"] is True, "previous theorem not proved")
    require(previous["frontier_decision"]["next_required_artifact"].endswith("RowsFirstRun_v1"), "previous frontier drift")

    frontier = cert["frontier_decision"]
    require(frontier["formal_hessian_and_normalization_closed"] is True, "formal route not closed")
    require(frontier["independent_basis_row_stubs_emitted"] is True, "basis stubs not emitted")
    require(frontier["frontier_is_trace_map_and_basis_values_or_primitive_rows_execution"] is True, "wrong frontier")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    route_a = packet["route_A_first_variation_certificate_partial_fill"]
    fields = route_a["filled_fields"]
    require(route_a["certificate_accepted_now"] is False, "route A overaccepted")
    require(fields["hessian_or_coercivity"]["verified"] is True, "coercivity not closed")
    require(fields["hessian_or_coercivity"]["constant_c"] == 1.0, "coercivity constant drift")
    require(fields["normalization_compatibility"]["verified"] is True, "normalization not closed")
    require(fields["selected_trace_map"]["verified"] is False, "trace map overfilled")
    require(fields["first_variation_identity"]["verified"] is False, "first variation overfilled")
    require(fields["boundary_cancellation"]["verified"] is False, "boundary cancellation overfilled")

    route_b = packet["route_B_independent_basis_rows_first_run"]
    require(route_b["row_count"] == 19, "basis row count drift")
    require(route_b["selected_row_count"] == 0, "basis rows overselected")
    require(route_b["all_basis_rows_selected"] is False, "basis accepted early")
    require(route_b["can_advance_to_primitive_rows"] is False, "advanced to primitive rows early")
    require(len(route_b["basis_rows"]) == 19, "basis row stubs missing")
    for row in route_b["basis_rows"]:
        require(row["selected_now"] is False, f"row overselected: {row['basis_id']}")
        require(row["selected_basis_value"] is None, f"basis value overfilled: {row['basis_id']}")
        require(row["selected_projector_value"] is None, f"projector value overfilled: {row['basis_id']}")
        require(row["gram_matrix"] is None, f"Gram overfilled: {row['basis_id']}")
        require(row["spectral_gap"] is None, f"gap overfilled: {row['basis_id']}")

    cutset = packet["next_cutset_after_partial_fill"]
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next drift")
    require(len(cutset["still_blocks_route_A"]) == 3, "route A block count drift")
    require(len(cutset["still_blocks_route_B"]) == 4, "route B block count drift")
    require(
        "selected HYM/Strominger finite trace"
        in cutset["recommended_next"]["superset_strategy"]["shared_missing_object"],
        "shared object drift",
    )

    require(STATUS in note and NEXT in note and "fresh long-chain branch now imports" in note, "note missing essentials")
    print(
        "AUDIT_PASS: reanchored long-chain C1 partial fill imported; "
        "selected trace/basis values remain open"
    )


if __name__ == "__main__":
    main()
