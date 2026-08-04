from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "certificates" / "protospinor_gr_response_dependency_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))

    require(
        cert["status"] == "PROTOSPINOR_LOOP_RESPONSE_LEDGER_BUILT_GR_NUMERIC_CLOSURE_OPEN",
        "unexpected certificate status",
    )
    inv = cert["topological_invariants"]
    require(inv["pi1_SO3_order"] == 2, "SO(3) binary obstruction must have order 2")
    require(inv["minimal_spin_lift_cover_degree"] == 2, "spin lift must be a double cover")
    require(inv["binary_loop_obstruction_closed"] is True, "loop obstruction must be closed")

    accounting = cert["closure_accounting"]
    require(accounting["protospinor_loop_obstruction_closed"] is True, "protospinor invariant lost")
    require(accounting["full_GR_numeric_closure"] is False, "must not overclaim full GR closure")
    require(
        accounting["space_time_as_response_numerically_closed"] is False,
        "must not overclaim numerical spacetime response closure",
    )
    require(0.0 < accounting["closure_ratio"] < 1.0, "ledger must be partially, not fully, closed")

    guardrails = cert["guardrails"]
    require(guardrails["claims_full_GR_derivation"] is False, "forbidden full GR claim")
    require(guardrails["claims_Newton_constant_prediction"] is False, "forbidden G_N claim")
    require(
        guardrails["allows_structural_alignment_to_count_as_numeric_closure"] is False,
        "structural alignment cannot count as numeric closure",
    )

    imported = cert["imported_certificate_statuses"]
    require(
        imported["internal_rho_uv_radius"] == "FINAL_INTERNAL_RHO_UV_BRANCH_CLOSED",
        "rho_UV imported closed branch missing",
    )
    require(
        imported["dimensionful_obstruction"] == "OBSTRUCTION_CERTIFIED",
        "dimensionful obstruction certificate missing",
    )
    require(
        imported["time_oriented_m1_deresponse"]
        == "TIME_ORIENTED_M1_DERESPONSE_TARGET_COHERENT_SELECTED_SOURCE_OPEN",
        "de-response source-open gate missing",
    )

    row_by_id = {row["id"]: row for row in cert["dependency_rows"]}
    require(row_by_id["selected_internal_rho_uv_branch"]["closed"] is True, "rho_UV row should be closed")
    require(row_by_id["dimensionful_GR_normalization"]["closed"] is False, "GR normalization should remain open")
    require(row_by_id["full_GR_numeric_closure"]["closed"] is False, "full GR target should remain open")

    print("AUDIT_PASS: protospinor GR response dependency certificate is disciplined")


if __name__ == "__main__":
    main()

