from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_aint_operator_relation_source_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "GR_TT_AINT_OPERATOR_RELATION_THEOREM_BLOCKED_DISTINCT_COMPLEMENT_ROUTE_REQUIRED",
        "unexpected status",
    )

    source = cert["source_status"]
    routes = cert["route_tests"]
    result = cert["theorem_result"]
    next_route = cert["next_constructive_route"]
    guards = cert["guardrails"]

    require(source["coherent_projector_and_lambda_star_sourced"] is True, "projector/lambda source expected")
    require(source["closure_cost_hessian_sourced"] is True, "closure Hessian source expected")
    require(source["selected_GR_internal_row_sourced"] is False, "selected GR row should remain unsourced")
    require(source["A_GR_TT_equals_H_TT_sourced"] is False, "A=H should remain unsourced")
    require(source["c_interface_sourced"] is False, "c_interface should remain unsourced")
    require(routes["route_A_equals_H_TT"]["closed"] is False, "A=H route should not close")
    require(routes["route_A_equals_c_H_TT"]["closed"] is False, "A=cH route should not close")
    require(routes["route_distinct_A_GR_TT"]["closed"] is False, "distinct A route should not close yet")
    require(
        all(row["below_nil_floor_0p25"] is True for row in routes["route_A_equals_H_TT"]["would_give_lambda_rows"]),
        "A=H diagnostic should be below nil floor for tested rows",
    )
    require(result["GR_TT_modal_gap_closed"] is False, "GR TT modal gap must remain open")
    require(next_route["name"] == "Explicit_GR_TT_Aint_Complement_Construction", "wrong next route")
    require(guards["claims_operator_relation_closed"] is False, "must not claim operator relation closed")
    require(guards["claims_GR_TT_modal_gap_closed"] is False, "must not claim modal gap closed")
    require(guards["claims_Z64_GR_identity"] is False, "must not claim Z64 identity")

    print("AUDIT_PASS: GR TT/Aint operator relation theorem blocked; explicit complement route required")


if __name__ == "__main__":
    main()
