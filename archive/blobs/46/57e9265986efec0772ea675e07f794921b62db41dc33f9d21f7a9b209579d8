from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_strominger_trace_c1_first_variation_or_quadrature_execution_plan_certificate.json"
STATUS = "POST_ALPHA_STROMINGER_TRACE_C1_FIRST_VARIATION_OR_QUADRATURE_EXECUTION_PLAN_IMPORTED_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


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
    require(cert["theorem"]["proved"] is True, "execution-plan theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    summary = packet["source_candidate_summary"]
    require(summary["promotion_decision"]["I10_proved"] is False, "I10 overclaimed")
    require(summary["promotion_decision"]["route_A_first_variation_certificate_accepted"] is False, "route A overclaimed")
    require(summary["promotion_decision"]["route_B_quadrature_execution_accepted"] is False, "route B overclaimed")
    require(summary["promotion_decision"]["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    target = summary["superset_strategy"]["locked_target"]
    require(target["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(target["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(target["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")

    first = packet["route_A_first_variation_certificate_plan"]
    require(first["verified_now"] is False, "I11 certificate should not be verified")
    require(first["theorem_slot"] == "I11_strominger_trace_c1_first_variation", "wrong theorem slot")
    for key in [
        "selected_trace_map",
        "first_variation_identity",
        "hessian_or_coercivity",
        "boundary_cancellation",
        "normalization_compatibility",
    ]:
        require(first["certificate_fields"][key]["required"] is True, f"missing required field {key}")
        require(first["certificate_fields"][key]["verified_now"] is False, f"field oververified {key}")

    quad = packet["route_B_quadrature_execution_manifest"]
    require(quad["accepted_now"] is False, "quadrature should not be accepted")
    rows = quad["row_requirements"]
    require(rows["zero_mode_basis_rows"]["count"] == 19, "basis row count drift")
    require(rows["primitive_contraction_rows"]["count"] == 72, "primitive row count drift")
    require(rows["hessian_source_rows"]["count"] == 2, "hessian/source row count drift")
    require(rows["sector_matrix_rows"]["count"] == 36, "sector row count drift")
    require(all(req["filled_now"] is False for req in rows.values()), "quadrature rows overfilled")
    require("using measured masses, mixings, or CP phase as row targets" in quad["acceptance_equations"]["forbidden_shortcuts"], "measured-target guardrail missing")

    schedule = packet["quadrature_row_schedule"]
    require(schedule["status"] == "ROW_SCHEDULE_BUILT_NOT_EXECUTED", "schedule status drift")
    require(schedule["next_executable_stage"] == "basis", "wrong next stage")
    require(schedule["executed_now"] is False, "schedule overexecuted")
    require([stage["stage"] for stage in schedule["execution_order"]] == ["basis", "primitive_contractions", "hessian_source", "sector_matrices"], "stage order drift")
    require([len(stage["rows"]) for stage in schedule["execution_order"]] == [19, 72, 2, 36], "stage row-count drift")

    require(STATUS in note and NEXT in note and "The next proof step is now executable" in note, "note missing essentials")
    print("AUDIT_PASS: Strominger/C1 first-variation plan imported; quadrature schedule fixed and open")


if __name__ == "__main__":
    main()
