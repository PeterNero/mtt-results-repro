from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_internal_aint_complement_gap_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "SELECTED_INTERNAL_AINT_GAP_REDUCED_TO_BRANCH_IDENTITY_OR_PACKET_COMPUTATION",
        "unexpected status",
    )
    source = cert["source_tests"]
    result = cert["selection_result"]
    guards = cert["guardrails"]
    routes = {row["id"]: row for row in cert["candidate_routes"]}

    require(source["numeric_gap_refocused_on_internal_Aint"] is True, "gap target should be internal Aint")
    require(source["dimensionless_Aint_formula_closed"] is True, "Aint formula should be closed")
    require(source["z64_conditional_bridge_closed"] is True, "Z64 bridge should be conditionally closed")
    require(source["z64_usable_now_as_GR_modal_gap"] is False, "Z64 must not be unconditional GR gap")
    require(source["direct_z64_identity_not_sourced"] is True, "direct Z64 identity should remain unsourced")
    require(source["selected_global_Aint_packet_closed"] is False, "selected packet must remain open")

    require(routes["exact_z64_central_circle"]["candidate_lambda_star"] == 15.0, "Z64 value mismatch")
    require(routes["theta_nil_floor"]["candidate_lambda_star"] == 0.25, "nil value mismatch")
    require(routes["direct_product_fiber_packet"]["currently_promoted"] is False, "direct packet must not be promoted")
    require(all(row["currently_promoted"] is False for row in routes.values()), "no candidate should be promoted")

    require(result["selected_internal_Aint_gap_computed"] is False, "selected gap must remain open")
    require(result["selected_route"] is None, "route must remain unselected")
    require(result["selected_lambda_star"] is None, "lambda must remain unselected")
    require("lambda_* = 15" in note, "note should preserve Z64 conditional value")
    require("lambda_* = 0.25" in note, "note should preserve nil candidate value")

    require(guards["claims_z64_unconditional_GR_gap"] is False, "must not claim Z64 unconditional")
    require(guards["claims_nil_floor_saturation"] is False, "must not claim nil saturation")
    require(guards["claims_direct_packet_values_known"] is False, "must not claim direct values")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_full_GR_response_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: selected internal Aint gap reduced to branch identity or packet computation")


if __name__ == "__main__":
    main()
