"""Audit the visible/Route-C PhiFin alpha1 derivative bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_selected_visible_routec_phifin_alpha1_derivative_bridge.py"
CANDIDATE = ROOT / "candidate_data" / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json"
CERT = ROOT / "certificates" / "selected_visible_routec_phifin_alpha1_derivative_bridge_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VisibleRouteC_PhiFinAlpha1Derivative_Bridge_v1.md"

STATUS = "MTT_SELECTED_VISIBLE_ROUTEC_PHIFIN_ALPHA1_DERIVATIVE_BRIDGED_ALPHA1_RETIRED_C1_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILDER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    print(proc.stdout, end="")
    require(proc.returncode == 0, "builder failed")

    candidate = load(CANDIDATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "unexpected status")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["closure_claimed"] is False, "must not claim closure")
    require(candidate["target_fitting_used"] is False, "target fitting must be false")
    require(candidate["observed_data_used"] is False, "observed data must be false")
    require(
        candidate["bridge_result"]["stationary_lane_A_source_identity_closed"] is True,
        "stationary lane A source identity should be retained",
    )
    require(
        candidate["bridge_result"]["same_branch_alpha1_derivative_closed_by_import"] is True,
        "alpha1 derivative should be retired by import",
    )
    require(
        candidate["bridge_result"]["honest_dotD_replay_closed_by_import"] is True,
        "honest dotD replay should be retired by import",
    )
    require(
        candidate["bridge_result"]["visible_routec_contract_lane_A_fully_validates_now"] is False,
        "full Lane A validation must remain false",
    )
    require(
        candidate["payload_boundary"]["full_PhiFin_alpha1_payload_selected_values_emitted"] is False,
        "dynamic PhiFin payload must remain open",
    )
    require(
        candidate["what_remains_open"]["primitive_C1_contractions"] is True,
        "primitive C1 contractions must remain open",
    )
    require("does **not** emit" in note, "note must state non-promotion boundary")

    print(f"PASS {CANDIDATE.name}: {STATUS}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
