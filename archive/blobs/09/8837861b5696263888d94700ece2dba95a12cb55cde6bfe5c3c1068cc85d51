from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_external_noninvariant_c1_certificate.json"
STATUS = "POST_ALPHA_EXTERNAL_NONINVARIANT_C1_REDUCED_FIBER_ORIGIN_OPEN"
NEXT = "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["nonzero_unselected_candidate_count"] == 4, "wrong candidate count")
    require(cert["minimal_active_shift_required"] == [1, 1], "wrong active shift")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    facts = packet["imported_facts"]
    require(facts["active_shift_1_1_forced_by_finite_support"] is True, "active shift not forced")
    require(facts["minimal_active_shift_required"] == [1, 1], "wrong minimal active shift")
    require(facts["fixed_fiber_shifts_one_qutrit_gauge_class"] is True, "fiber class not reduced")
    require(facts["all_fiber_envelope_retired"] is True, "all-fiber envelope not retired")
    require(facts["basis_transport_heavy_link_candidate"] is True, "basis transport candidate missing")
    require(all(rank == 3 for sector in facts["fixed_fiber_ranks"].values() for rank in sector.values()), "fixed-fiber ranks should be full")
    require(all(rank == 1 for rank in facts["all_fiber_rank"].values()), "all-fiber ranks should be rank one")

    selection = packet["selection_state"]
    require(all(value is False for value in selection.values()), "selection state should remain open")
    require(packet["route_update"]["updated_primary_route"] == "fiber_origin_or_gauge_invariant_noninvariant_C1_observable", "wrong route update")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "active shift = (1,1)" in note, "note missing essentials")

    print("AUDIT_PASS: external non-invariant C1 reduced to fiber-origin/invariance selector")


if __name__ == "__main__":
    main()
