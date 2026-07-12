"""Audit finite H scalar transport into the H/lambda threshold frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
R_SOURCE = PACKET_DIR / "finite_hscalar_to_rh_rg_source_transport.packet.json"
K_GATE = PACKET_DIR / "ten_kthreshold_gate_after_finite_hscalar_transport.packet.json"
LAMBDA = PACKET_DIR / "lambda_h_payload_postcheck_and_guardrail.packet.json"
NEXT_PACKET = PACKET_DIR / "next_fullsm_or_prefactor_closure_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HLambdaThresholdPayload_from_FiniteHScalarSource_or_FullSMClosureAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HLAMBDA_THRESHOLD_PAYLOAD_FROM_FINITE_HSCALAR_SOURCE_"
    "RH_RG_REPLACED_ONE_PARAMETER_LAMBDA_PREFACTOR_STILL_GUARDED"
)
NEXT = "MTT_Selected_ElectroweakPrefactorSourceClosure_or_FinalTrueSMAudit_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    r_source = load(R_SOURCE)
    k_gate = load(K_GATE)
    lambda_payload = load(LAMBDA)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("r_source", r_source),
        ("k_gate", k_gate),
        ("lambda", lambda_payload),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["next_required_artifact"] == NEXT, "next artifact")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")

    decision = data["closure_decision"]
    require(decision["selected_R_H_RG_source_emitted"] is True, "R_H source")
    require(decision["selected_H_radial_source_row_emitted"] is True, "H radial source")
    require(decision["old_H_one_parameter_lane_retired_for_radial_source"] is True, "parameter not retired")
    require(decision["H_parameter_count_after_replacement"] == 0, "parameter count")
    require(decision["lambda_H_postcheck_passed"] is True, "lambda postcheck")
    require(decision["lambda_H_value_row_emitted_as_strict_no_knob"] is False, "lambda overclaim")
    require(decision["selected_K_threshold_Omega_H_lambda_emitted"] is False, "K overclaim")
    require(decision["selected_K_threshold_row_count_now"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K row requirement")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(r_source["accepted_as_selected_R_H_RG_source"] is True, "source transport")
    require(r_source["replaces_previous_controlled_parameter"]["parameter_count_after_replacement"] == 0, "replacement count")
    require(r_source["replaces_previous_controlled_parameter"]["within_selected_replay_floor"] is True, "R residual floor")
    require(abs(r_source["source_value"]["r_H_A_N"] - 391.39140285811555) < 1e-10, "r_H value")

    require(k_gate["strict_H_radial_source_emitted"] is True, "H radial in K gate")
    require(k_gate["strict_H_K_threshold_row_emitted"] is False, "strict K overclosed")
    require(k_gate["conditional_ten_K_if_prefactor_row_selected"] is True, "conditional ten K")
    require(k_gate["full_ten_row_K_threshold_closure"] is False, "ten K overclosed")

    require(lambda_payload["selected_R_H_RG_value_used"] is True, "lambda finite R used")
    require(lambda_payload["lambda_H_value_row_postcheck_passed"] is True, "lambda postcheck packet")
    require(lambda_payload["lambda_H_value_row_emitted_as_strict_no_knob"] is False, "lambda packet overclosed")
    require(abs(lambda_payload["lambda_H_from_finite_r_H_A_N"] - 0.12604) < 2e-14, "lambda residual")
    require(lambda_payload["external_lambda_used_as_selector"] is False, "external selector")

    for phrase in [
        "FiniteHScalarToRHRGReplacementTheorem",
        "H parameter count after replacement = 0",
        "strict `lambda_H` value row emitted: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: finite H scalar transports to selected R_H^RG and retires the H knob; "
        "lambda/K threshold prefactor remains guarded."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
