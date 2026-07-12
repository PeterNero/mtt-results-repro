from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_i10_payload_certificate_or_independent_quadrature_values_fill_certificate.json"
)
STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_I10_PAYLOAD_CERTIFICATE_OR_INDEPENDENT_QUADRATURE_VALUES_FILL_"
    "REANCHORED_CUTSET_OPEN"
)
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


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
    require(cert["theorem"]["proved"] is True, "I10 fill attempt bridge should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    previous = packet["fresh_previous_certificate"]
    require(previous["theorem"]["proved"] is True, "previous theorem not proved")
    require(previous["frontier_decision"]["next_required_artifact"].endswith("QuadratureValuesFill_v1"), "previous frontier drift")

    frontier = cert["frontier_decision"]
    require(frontier["route_A_rejected_at_this_gate"] is True, "route A rejection missing")
    require(frontier["route_B_rejected_at_this_gate"] is True, "route B rejection missing")
    require(frontier["frontier_is_strominger_trace_c1_first_variation_or_quadrature_execution_plan"] is True, "wrong frontier")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    route_a = packet["route_a_i10_payload_certificate_fill_attempt"]
    require(route_a["status"] == "ATTEMPTED_NOT_ACCEPTED_SELECTED_PAYLOADS_OPEN", "wrong route A status")
    require(route_a["accepted_now"] is False, "route A accepted overclaim")
    require(route_a["payload_checks"]["selected_minimizer_trace_payload_verified"]["value"] is False, "trace payload overclaim")
    require(route_a["payload_checks"]["selected_c1_response_payload_verified"]["value"] is False, "C1 payload overclaim")
    require(route_a["payload_checks"]["defect_functional_minimizer_payload_verified"]["value"] is False, "defect payload overclaim")

    route_b = packet["route_b_independent_quadrature_values_fill_attempt"]
    require(route_b["status"] == "ATTEMPTED_VALUES_EMPTY_NOT_ACCEPTED", "wrong route B status")
    require(route_b["accepted_now"] is False, "route B accepted overclaim")
    require(all(count == 0 for count in route_b["table_counts"].values()), "quadrature tables should be empty")
    require(route_b["acceptance_checks"]["no_patched_replay_copying"] is True, "patched-copy guardrail failed")

    cutset = packet["minimal_next_cutset"]
    require(cutset["status"] == "NEXT_CUTSET_SELECTED", "wrong cutset status")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next drift")
    require(len(cutset["route_A_minimal_cutset"]) == 3, "route A cutset drift")
    require(len(cutset["route_B_minimal_cutset"]) == 4, "route B cutset drift")

    require(STATUS in note and NEXT in note and "Both closure routes were evaluated" in note, "note missing essentials")
    print(
        "AUDIT_PASS: reanchored long-chain I10 payload/independent quadrature fill bridge imported; "
        "next cutset remains open"
    )


if __name__ == "__main__":
    main()
