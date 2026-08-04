"""Audit Step47 Xi argument shell fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step47_alpha1rtheta_xi_argument_fill_or_internalvaluerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
XI_SHELLS = PACKET_DIR / "step47_xi_argument_shells_filled.packet.json"
PAYLOAD_GAP = PACKET_DIR / "step47_xi_magnitude_payload_gap.packet.json"
VALUE_GATE = PACKET_DIR / "step47_internal_value_row_execution_gate.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step47_next_payload_source_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step47_Alpha1RThetaXiArgumentFill_or_InternalValueRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP47_ALPHA1RTHETA_XI_ARGUMENT_SHELLS_FILLED_VALUE_PAYLOADS_OPEN"
NEXT = "MTT_Selected_XiMagnitudePayloadSourceTheorem_or_RThetaValueRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    xi_shells = load(XI_SHELLS)
    payload_gap = load(PAYLOAD_GAP)
    value_gate = load(VALUE_GATE)
    frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Xi shell theorem not proved")

    for packet in [data, xi_shells, payload_gap, value_gate, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(xi_shells["all_shells_constructed"] is True, "Xi shells not constructed")
    require(xi_shells["xi_argument_count"] == 10, "Xi shell count mismatch")
    require(xi_shells["charged_xi_argument_count"] == 9, "charged Xi count mismatch")
    require(xi_shells["higgs_xi_argument_count"] == 1, "Higgs Xi count mismatch")
    require(xi_shells["full_value_execution_argument_count"] == 0, "full arguments overclosed")
    require(xi_shells["all_full_value_execution_arguments_closed"] is False, "all arguments overclosed")
    for xi in xi_shells["xi_arguments"]:
        require(xi["formal_argument_term"].startswith(xi["xi_id"]), f"bad formal term: {xi['xi_id']}")
        require(xi["accepted_as_full_value_execution_argument"] is False, f"Xi overaccepted: {xi['xi_id']}")
        require(xi["postcheck_used_as_selector"] is False, f"postcheck selector: {xi['xi_id']}")
        require(xi["closed_subfield_count"] < xi["required_subfield_count"], f"Xi unexpectedly full: {xi['xi_id']}")
    charged = [xi for xi in xi_shells["xi_arguments"] if xi["sector"] in {"u", "d", "e"}]
    require(all(xi["selected_subfields"]["source_normalized_sector_weight_bound"] is True for xi in charged), "source weights not bound")
    require(all(xi["selected_subfields"]["generation_support_bound"] is True for xi in charged), "generation support not bound")

    require(payload_gap["source_normalized_weights_closed"] is True, "source weights open")
    require(payload_gap["generation_support_closed"] is True, "generation support open")
    for key in [
        "magnitude_bearing_projection_weights_closed",
        "generation_resolved_magnitude_rows_closed",
        "threshold_response_rows_closed",
        "mass_scheme_conversion_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "full_profile_likelihood_closed",
    ]:
        require(payload_gap[key] is False, f"payload gap overclosed: {key}")
    require(payload_gap["accepted_source_row_count"] == 0, "accepted source rows overclaimed")
    require(payload_gap["minimal_payload_theorem"]["name"] == "XiMagnitudePayloadSourceTheorem", "payload theorem mismatch")

    require(value_gate["selected_Rtheta_alpha1_map_constructed"] is True, "map missing")
    require(value_gate["xi_argument_shells_filled"] is True, "value gate shell missing")
    require(value_gate["full_value_execution_argument_count"] == 0, "value gate full args overclosed")
    require(value_gate["accepted_internal_value_row_count"] == 0, "value rows overaccepted")
    require(value_gate["accepted_internal_charged_coefficient_row_count"] == 0, "charged rows overaccepted")
    require(value_gate["lambda_H_internal_row_closed"] is False, "lambda_H overclosed")

    closed_now = frontier["closed_now"]
    require(closed_now["all_10_Xi_argument_shells_constructed"] is True, "frontier shell missing")
    require(closed_now["postcheck_values_forbidden_as_selectors"] is True, "postcheck guard missing")
    require(frontier["still_open"]["XiMagnitudePayloadSourceTheorem"] is True, "payload theorem not open")
    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")

    decision = data["closure_decision"]
    require(decision["xi_argument_shells_constructed"] is True, "decision shell missing")
    require(decision["xi_argument_shell_count"] == 10, "decision shell count mismatch")
    require(decision["full_value_execution_argument_count"] == 0, "decision full args overclosed")
    require(decision["all_full_value_execution_arguments_closed"] is False, "decision full closure overclaimed")
    for key in [
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "Xi argument shells constructed          : true",
        "Xi shell count                          : 10",
        "accepted internal value rows            : 0",
        "Step42 values remain postchecks only",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
