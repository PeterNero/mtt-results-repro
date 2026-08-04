"""Audit the visible Route-C Phi_fin alpha1 derivative fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "visible_routec_phifin_alpha1_derivative_fill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FILL = PACKET_DIR / "visible_routec_phifin_alpha1_derivative_fill.packet.json"
OBSTRUCTION = PACKET_DIR / "phifin_alpha1_derivative_obstruction.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_VISIBLE_ROUTEC_PHIFIN_ALPHA1_DERIVATIVE_FILL_ATTEMPT_BUILT_PAYLOAD_DRIVER_OPEN"
NEXT = "MTT_Selected_PhiFinAlpha1PayloadValues_or_TypedBNRetardedDerivativeExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    fill = load(FILL)
    obstruction = load(OBSTRUCTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    lane_a = fill["lane_A_visible_routec_source_identity"]
    require(lane_a["source_identity"]["selected_emitted"] is True, "source identity regressed")
    require(lane_a["visible_routec_operator_source"]["selected_emitted"] is True, "visible source regressed")
    require(lane_a["phi_fin_payload"]["selected_emitted"] is False, "Phi_fin payload overfilled")
    require(lane_a["phi_fin_payload"]["theorem_derived"] is False, "Phi_fin payload overderived")
    require(lane_a["same_branch_alpha1_derivative"]["selected_emitted"] is False, "alpha1 derivative overfilled")
    require(lane_a["same_branch_alpha1_derivative"]["alpha1_driver_verified"] is False, "alpha1 driver oververified")
    require(lane_a["dotd_validator_replay"]["honest_validator_exit_code"] == 1, "honest dotD validator unexpectedly passed")
    require(lane_a["dotd_validator_replay"]["source_only_fails_only_by_alpha1_driver"] is True, "dotD failure not localized")
    require(fill["validation"]["ok"] is False and fill["validation"]["exit_code"] == 1, "validator should remain open")
    require("certificate: neither lane validates" in fill["validation"]["errors"], "validator missing lane failure")

    require(obstruction["remaining_lane_A_blockers"]["selected_PhiFin_alpha1_payload_values"] is True, "payload blocker missing")
    require(obstruction["remaining_lane_A_blockers"]["same_branch_alpha1_driver_theorem"] is True, "driver blocker missing")
    require(obstruction["remaining_lane_A_blockers"]["honest_dotD_validator_replay"] is True, "dotD blocker missing")
    require(len(obstruction["selected_payload_open_flags"]) >= 5, "payload open flags underspecified")

    require(data["closure_decision"]["stationary_source_identity_closed"] is True, "candidate source identity missing")
    require(data["closure_decision"]["visible_routec_operator_source_closed"] is True, "candidate visible source missing")
    require(data["closure_decision"]["phi_fin_alpha1_payload_closed"] is False, "candidate payload overclosed")
    require(data["closure_decision"]["same_branch_alpha1_derivative_closed"] is False, "candidate derivative overclosed")
    require(data["closure_decision"]["honest_dotd_validator_replay_closed"] is False, "candidate dotD overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(cert["validator_ok"] is False, "certificate validator overpassed")

    for packet in [fill, obstruction, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("must not be promoted" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
