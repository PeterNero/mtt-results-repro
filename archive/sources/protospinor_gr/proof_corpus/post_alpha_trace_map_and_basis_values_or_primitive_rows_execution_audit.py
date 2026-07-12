from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_trace_map_and_basis_values_or_primitive_rows_execution_certificate.json"
STATUS = "POST_ALPHA_TRACEMAP_AND_BASIS_VALUES_FILLED_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


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
    require(cert["theorem"]["proved"] is True, "trace/basis theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    require(decision["route_A_trace_map_values_accepted"] is True, "trace values not accepted")
    require(decision["route_B_basis_rows_accepted"] is True, "basis rows not accepted")
    require(decision["route_B_can_advance_to_primitive_rows_after_dynamic_binding"] is True, "advance condition missing")
    for key in ["primitive_rows_executed", "I10_proved", "unpatched_SM_parity_dynamic_packet_closed", "true_SM_equivalence_closed"]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    trace = packet["route_A_trace_map_value_fill"]
    require(trace["accepted_for_stationary_trace"] is True, "stationary trace not accepted")
    require(trace["accepted_for_dynamic_C1_primitive_rows"] is False, "dynamic trace overaccepted")
    require(trace["filled_flags"]["selected_trace_map_values"] is True, "trace map values not filled")
    require(trace["remaining_dynamic_flags"]["selected_dotD_source_verified"] is False, "dotD oververified")
    require(set(trace["trace_values"].keys()) == {"Q", "u", "d", "L", "e", "N", "H"}, "trace sector set drift")

    basis = packet["route_B_selected_basis_value_fill"]
    require(basis["accepted_for_basis_stage"] is True, "basis stage not accepted")
    require(basis["row_count"] == 19 and basis["selected_row_count"] == 19, "basis count drift")
    require(basis["all_basis_rows_selected"] is True, "basis rows not all selected")
    for row in basis["basis_rows"]:
        require(row["selected_now"] is True, f"basis row not selected: {row['basis_id']}")
        require(row["selected_basis_value"] is not None, f"basis value missing: {row['basis_id']}")
        require(row["selected_projector_value"] is not None, f"projector value missing: {row['basis_id']}")
        require(row["gram_matrix"] == "identity_preserved_by_unitary_transport", f"Gram mismatch: {row['basis_id']}")
        require(row["spectral_gap"] == "preserved_from_model_gap", f"gap mismatch: {row['basis_id']}")

    primitive = packet["primitive_rows_execution_ready"]
    require(primitive["basis_stage_accepted"] is True, "primitive basis precondition missing")
    require(primitive["primitive_row_count"] == 72, "primitive row count drift")
    require(len(primitive["primitive_row_ids"]) == 72, "primitive row ids missing")
    require(primitive["can_execute_rows_now"] is False, "primitive rows overexecuted")
    require("dynamic dotD trace binding" in " ".join(primitive["why_not"]), "dynamic binding blocker missing")
    require(STATUS in note and NEXT in note and "Stationary selected trace-map and basis data are now filled" in note, "note missing essentials")
    print("AUDIT_PASS: stationary trace/basis values imported; dynamic primitive binding remains open")


if __name__ == "__main__":
    main()
