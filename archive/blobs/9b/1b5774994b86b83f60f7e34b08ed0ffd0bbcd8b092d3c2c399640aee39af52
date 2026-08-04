"""Audit promoted PSM-C1-02 selected source-ownership premise execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted"
BUILDER = ROOT / "scripts" / "build_selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PREMISE = PACKET_DIR / "premise_execution_status.packet.json"
NEXT = PACKET_DIR / "gauge_trace_or_independent_rows_next_target.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1.md"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_SELECTEDSOURCEOWNERSHIPPREMISEEXECUTION_"
    "GAUGE_TRACE_OR_INDEPENDENT_ROWS_TARGET_SELECTED"
)
NEXT_ARTIFACT = "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    premise = load(PREMISE)
    next_packet = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("premise", premise),
        ("next", next_packet),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "PSMC102SelectedSourceOwnershipPremiseExecutionTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT_ARTIFACT, "next packet")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(premise["status"] == "PREMISES_EXECUTED_TO_GAUGE_TRACE_OR_INDEPENDENT_ROWS", "premise status")
    require(premise["upstream_remaining_premise_count"] == 2, "upstream premise count")
    require(premise["closed_SM_parity_and_formal_row_boundaries_preserved"] is True, "boundaries")
    require(premise["untransported_BN_shortcut_rejected_for_source_ownership"] is True, "BN shortcut")
    require(premise["physical_finite_quotient_lemma_attacked"] is True, "finite quotient")
    require(premise["local_principle_route_A_two_exit_witness_validates"] is True, "route A witness")
    require(premise["three_field_certificate_is_exact_remaining_route_A"] is True, "three-field")

    require(next_packet["status"] == "NEXT_TARGET_SELECTED", "next status")
    require(next_packet["primary_next_target"] == "SelectedGaugeTransportedBNPhiFinTrace", "primary target")
    require(next_packet["fallback_next_target"] == "IndependentComplexRowExecution", "fallback target")
    require(next_packet["gauge_transport_trace_promoted_to_primary_next_target"] is True, "primary promotion")
    require(next_packet["independent_row_formula_execution_promoted_to_fallback_next_target"] is True, "fallback promotion")
    require(next_packet["Route_A_closed_now"] is False, "route A overclosed")
    require(next_packet["Route_B_closed_now"] is False, "route B overclosed")
    require(next_packet["Route_A_gauge_transport_trace_required"] is True, "route A requirement")
    require(next_packet["Route_B_independent_complex_rows_required"] is True, "route B requirement")

    decision = candidate["closure_decision"]
    require(decision["selected_source_ownership_premise_execution_promoted"] is True, "decision promoted")
    require(decision["untransported_BN_shortcut_rejected_for_source_ownership"] is True, "decision BN")
    require(decision["gauge_transport_trace_promoted_to_primary_next_target"] is True, "decision primary")
    require(decision["independent_row_formula_execution_promoted_to_fallback_next_target"] is True, "decision fallback")
    for key in [
        "Route_A_closed_now",
        "Route_B_closed_now",
        "actual_dynamic_QaSU3_payload_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "untransported BN shortcut rejected                true",
        "three-field certificate is exact route-A target   true",
        "primary target                                    SelectedGaugeTransportedBNPhiFinTrace",
        "fallback target                                   IndependentComplexRowExecution",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
