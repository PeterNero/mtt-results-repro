"""Audit same-branch gauge/action source or one-primitive policy packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samebranchgaugeactionsource_or_oneprimitivepolicy"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_SOURCE = PACKET_DIR / "strict_samebranch_source_recheck.packet.json"
PRIMITIVE_ADMISSION = PACKET_DIR / "one_primitive_prefactor_admission.packet.json"
HLAMBDA_REPLAY = PACKET_DIR / "h_lambda_one_primitive_replay.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "claim_boundary_minimal_vs_noknob.packet.json"
NEXT_PACKET = PACKET_DIR / "next_empirical_audit_or_strict_source_upgrade.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameBranchGaugeActionSource_or_OnePrimitivePolicy_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SAMEBRANCHGAUGEACTIONSOURCE_OR_ONEPRIMITIVEPOLICY_"
    "MINIMAL_HLAMBDA_ONE_PRIMITIVE_CLOSED_STRICT_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_HLambdaEmpiricalAudit_or_StrictSameBranchGaugeActionSourceUpgrade_v1"


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
    strict = load(STRICT_SOURCE)
    primitive = load(PRIMITIVE_ADMISSION)
    replay = load(HLAMBDA_REPLAY)
    boundary = load(CLAIM_BOUNDARY)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("primitive", primitive),
        ("replay", replay),
        ("boundary", boundary),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "next artifact")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["minimal_one_primitive_H_lambda_closure_claimed"] is True, "minimal lane")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["measured_primitive_input_used"] is True, "primitive input")

    decision = data["closure_decision"]
    require(decision["selected_R_H_RG_source_emitted"] is True, "R_H source")
    require(decision["H_radial_parameter_count"] == 0, "H radial count")
    require(decision["accepted_strict_samebranch_source_rows"] == 0, "strict rows")
    require(decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(decision["one_physical_prefactor_primitive_admitted"] is True, "primitive admitted")
    require(decision["one_primitive_parameter_count"] == 1, "primitive count")
    require(decision["minimal_one_primitive_H_lambda_lane_closed"] is True, "minimal closure")
    require(decision["lambda_H_conditional_prediction_from_non_Higgs_prefactor"] is True, "conditional")
    require(decision["lambda_H_calibrated_from_lambda_H"] is False, "H target calibration")
    require(decision["strict_no_knob_closed"] is False, "strict overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(strict["accepted_strict_source_row_count"] == 0, "strict accepted")
    require(primitive["admitted_primitive"]["declared_parameter_count"] == 1, "primitive packet count")
    require(primitive["admitted_primitive"]["lambda_H_used_to_choose_value"] is False, "lambda chooser")
    require(primitive["guardrails"]["per_observable_retuning_forbidden"] is True, "retuning guard")

    require(replay["closure_scope"]["minimal_one_primitive_H_lambda_lane_closed"] is True, "replay closure")
    require(replay["closure_scope"]["strict_no_knob_lambda_H_closed"] is False, "replay no-knob")
    require(abs(replay["postcheck"]["absolute_residual"]) < 2e-15, "lambda replay residual")

    budget = boundary["parameter_budget_after_this_artifact"]
    require(budget["H_radial_parameters"] == 0, "budget H")
    require(budget["physical_prefactor_primitives"] == 1, "budget prefactor")
    require(budget["ordinary_H_only_knobs"] == 0, "budget H-only")
    require(budget["total_new_parameters_for_H_lambda_minimal_lane"] == 1, "budget total")

    for phrase in [
        "SameBranchGaugeActionSourceOrOnePrimitivePolicyTheorem",
        "parameter count = 1",
        "lambda_H is not used to choose this value",
        "postcheck residual",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: one-primitive H/lambda lane closed with one physical prefactor; "
        "strict no-knob and true SM equivalence remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
