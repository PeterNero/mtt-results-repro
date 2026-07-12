from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_strominger_trace_c1_first_variation_or_independent_quadrature_execution_plan_certificate.json"
)
STATUS = "POST_ALPHA_STROMINGER_TRACE_C1_FIRST_VARIATION_OR_INDEPENDENT_QUADRATURE_EXECUTION_PLAN_IMPORTED_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


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
    require(cert["theorem"]["proved"] is True, "long-chain execution-plan bridge should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    frontier = cert["frontier_decision"]
    require(frontier["route_A_I11_certificate_schema_built"] is True, "route A schema missing")
    require(frontier["route_B_independent_row_schedule_built"] is True, "route B schedule missing")
    require(frontier["frontier_is_C1_first_variation_certificate_fill_or_quadrature_rows_first_run"] is True, "wrong frontier")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    source = packet["source_execution_plan_certificate"]
    require(source["closure_claimed"] is False, "source closure overclaimed")
    require(source["theorem"]["proved"] is True, "source execution-plan theorem not proved")

    first = packet["route_A_first_variation_certificate_plan"]
    require(first["verified_now"] is False, "I11 certificate oververified")
    for key in [
        "selected_trace_map",
        "first_variation_identity",
        "hessian_or_coercivity",
        "boundary_cancellation",
        "normalization_compatibility",
    ]:
        require(first["certificate_fields"][key]["required"] is True, f"missing field {key}")
        require(first["certificate_fields"][key]["verified_now"] is False, f"field oververified {key}")

    quad = packet["route_B_independent_quadrature_execution_manifest"]
    require(quad["accepted_now"] is False, "quadrature route overaccepted")
    rows = quad["row_requirements"]
    require(rows["zero_mode_basis_rows"]["count"] == 19, "basis row count drift")
    require(rows["primitive_contraction_rows"]["count"] == 72, "primitive row count drift")
    require(rows["hessian_source_rows"]["count"] == 2, "hessian/source row count drift")
    require(rows["sector_matrix_rows"]["count"] == 36, "sector row count drift")
    require(all(req["filled_now"] is False for req in rows.values()), "quadrature rows overfilled")

    schedule = packet["independent_quadrature_row_schedule"]
    require(schedule["executed_now"] is False, "schedule overexecuted")
    require(schedule["next_executable_stage"] == "basis", "wrong next stage")
    require([stage["stage"] for stage in schedule["execution_order"]] == ["basis", "primitive_contractions", "hessian_source", "sector_matrices"], "stage order drift")
    require([len(stage["rows"]) for stage in schedule["execution_order"]] == [19, 72, 2, 36], "stage row-count drift")

    require(STATUS in note and NEXT in note and "No replay values are promoted" in note, "note missing essentials")
    print("AUDIT_PASS: long-chain Strominger/C1 execution plan imported; I11 and independent quadrature rows remain open")


if __name__ == "__main__":
    main()
