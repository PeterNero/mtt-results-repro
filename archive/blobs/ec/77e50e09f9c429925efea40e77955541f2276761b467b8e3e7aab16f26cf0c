"""Audit Step 43 minimal universal-parameter readiness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step43_minimaluniversalparameter_readiness_or_internalrowclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DISTANCE = PACKET_DIR / "step43_distance_to_minimal_parameter_closure.packet.json"
LANES = PACKET_DIR / "step43_minimal_parameter_lanes.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step43_MinimalUniversalParameterReadiness_or_InternalRowClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP43_MINIMAL_UNIVERSAL_PARAMETER_READINESS_BUILT_ONE_ANCHOR_NEAREST_NOT_SELECTED"
NEXT = "MTT_Selected_OneUniversalSourceAnchorTheorem_or_InternalRThetaCoefficientRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    distance = load(DISTANCE)
    lanes = load(LANES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "readiness theorem not proved")

    for packet in [data, distance, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    for key, value in distance["readiness_checks"].items():
        require(value is True, f"readiness check failed: {key}")
    require(distance["readiness_closed"] is True, "distance readiness not closed")
    require(distance["selected_universal_parameter_count"] == 0, "universal parameter overselected")
    require(distance["acceptable_parameter_count_range_if_source_selected"] == [1, 2, 3], "parameter range changed")
    require(distance["nearest_lane"] == "one_universal_source_anchor", "nearest lane mismatch")
    require(
        "one candidate-specific source-anchor theorem plus one row-execution audit"
        in distance["answer_to_how_far"],
        "distance answer missing",
    )

    lane_data = lanes["lanes"]
    zero = lane_data["zero_knob_internal_rows"]
    one = lane_data["one_universal_source_anchor"]
    two = lane_data["two_universal_source_anchors"]
    three = lane_data["three_universal_source_anchors"]
    require(zero["parameter_count"] == 0 and zero["status"] == "OPEN", "zero-knob lane mismatch")
    require(one["parameter_count"] == 1, "one-knob count mismatch")
    require(one["nearest_minimal_fallback"] is True, "one-knob not nearest")
    require(one["status"] == "NEAREST_ALLOWED_BUT_NOT_SELECTED", "one-knob status mismatch")
    require(one["selected_now"] is False, "one-knob overselected")
    require(one["readiness_score"] == "4/6", "one-knob readiness changed")
    require("candidate-specific source-anchor theorem" in one["missing_fields"], "source-anchor missing field absent")
    require(two["parameter_count"] == 2 and two["selected_now"] is False, "two-knob lane overselected")
    require(three["parameter_count"] == 3 and three["selected_now"] is False, "three-knob lane overselected")

    decision = data["closure_decision"]
    require(decision["minimal_universal_parameter_policy_ready"] is True, "policy readiness not closed")
    require(decision["one_to_three_universal_parameters_allowed_if_source_selected"] is True, "1-3 policy not allowed")
    require(decision["nearest_allowed_fallback"] == "one_universal_source_anchor", "nearest decision mismatch")
    require(decision["one_universal_source_anchor_readiness_score"] == "4/6", "decision readiness mismatch")
    require(decision["selected_universal_parameter_count"] == 0, "decision universal parameter overselected")
    for key in [
        "one_universal_source_anchor_selected",
        "minimal_parameter_closure_closed",
        "internal_Rtheta_coefficient_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "Can 1-3 knobs be okay?",
        "selected universal parameters now: `0`",
        "one-knob route",
        "one candidate-specific universal source-anchor theorem plus one row-execution audit",
        "Nearest acceptable fallback",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
