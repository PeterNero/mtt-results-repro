from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "central_circle_tt_adjoint_support_proof_attempt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    routes = cert["attempted_routes"]
    tests = cert["route_tests"]
    decision = cert["decision"]
    conditional = cert["conditional_proof_if_selection_premise_added"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "SUPPORT_THEOREM_PROOF_ATTEMPT_BLOCKED_SELECTION_PREMISE_REQUIRED",
        "unexpected status",
    )
    require(tests["central_unique_shared_scalar_channel"] is True, "central route source missing")
    require(tests["central_gravity_operates_on_shared_channel"] is True, "gravity shared route missing")
    require(tests["central_claim_marked_interpretive_not_theorem"] is True, "interpretive guardrail missing")
    require(tests["gr_observable_content_exhausted_by_projection"] is True, "GR completeness missing")
    require(tests["capacity_gravity_as_geometric_bookkeeping"] is True, "capacity bookkeeping missing")
    require(tests["no_go_says_exact_support_independent"] is True, "no-go should block")
    require(tests["adjoint_support_nonzero_closed"] is True, "adjoint support should be closed")
    require(tests["uniqueness_would_close_after_support"] is True, "uniqueness should be ready")

    require(routes["route_A_universal_scalar_channel"]["closes_exact_support"] is False, "route A must not close")
    require(routes["route_B_GR_projection_completeness"]["closes_exact_support"] is False, "route B must not close")
    require(routes["route_C_capacity_bookkeeping"]["closes_exact_support"] is False, "route C must not close")
    require(conditional["valid"] is True and conditional["unconditional"] is False, "conditional proof status wrong")
    require("Pi_TT_shared" in conditional["new_selection_premise"], "selection premise missing")

    require(decision["proved_unconditionally"] is False, "must not prove unconditionally")
    require(decision["proved_conditionally"] is True, "conditional proof should be recorded")
    require("cannot be inferred" in decision["why_unconditional_proof_fails"], "decision should cite no-go")
    require("Why The Direct Proof Fails" in note, "note should explain failure")

    require(guards["claims_exact_support_sourced"] is False, "must not claim support sourced")
    require(guards["claims_unconditional_lambda_GR_TT_15"] is False, "must not claim lambda")
    require(guards["uses_interpretive_synthesis_as_proof"] is False, "must not use synthesis as proof")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")

    print("AUDIT_PASS: central-circle TT support proof attempt blocked by exact selection premise")


if __name__ == "__main__":
    main()
