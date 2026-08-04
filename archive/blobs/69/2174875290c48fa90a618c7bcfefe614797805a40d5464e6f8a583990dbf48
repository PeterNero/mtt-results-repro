"""Audit the symbolic transport-conjugation validator replay."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_transport_conjugation_validator_replay.py"
CANDIDATE = ROOT / "candidate_data" / "selected_transport_conjugation_validator_replay.candidate.json"
CERT = ROOT / "certificates" / "selected_transport_conjugation_validator_replay_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TransportConjugation_ValidatorReplay_v1.md"

STATUS = "MTT_SELECTED_TRANSPORT_CONJUGATION_VALIDATOR_REPLAY_CLOSED_DOTD_OPEN"
NEXT = "MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    result = data["validator_result"]
    acceptance = data["symbolic_acceptance"]
    decision = data["promotion_decision"]
    boundary = data["dotd_boundary"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "theorem proved",
            data["theorem"]["proved"] is True
            and "dotD_alpha1 is excluded" in data["theorem"]["proof_steps"][-1],
            data["theorem"],
        ),
        check(
            "symbolic acceptance exact",
            acceptance["validator_extension"] == "exact_symbolic_transport_conjugation"
            and acceptance["gauge_frame_replay_passes"] is True
            and acceptance["raw_direct_truncated_relative_residual"] > 0.01
            and acceptance["rejects_raw_finite_aliasing_as_failure"] is True,
            acceptance,
        ),
        check(
            "all sectors replay",
            len(data["sector_replay_slots"]) == 7
            and all(
                slot["selected_source_verified_by_symbolic_transport_replay"] is True
                and slot["selected_green_operator_valid_on_conjugated_complement"] is True
                and slot["finite_raw_truncation_replay_used"] is False
                for slot in data["sector_replay_slots"].values()
            ),
            data["sector_replay_slots"],
        ),
        check(
            "finite replay closes",
            result["symbolic_transport_conjugation_validator_extended"] is True
            and result["all_sector_projector_riesz_green_replays_pass"] is True
            and result["selected_source_verified"] is True
            and result["selected_rho_s_validator_ready"] is True
            and cert["finite_validator_replay_closed"] is True,
            result,
        ),
        check(
            "dotD remains open",
            boundary["dotD_alpha1_closed_by_this_artifact"] is False
            and boundary["selected_dotD_source_verified"] is False
            and boundary["alpha1_driver_verified"] is False
            and decision["selected_dotD_source_verified"] is False
            and decision["alpha1_driver_verified"] is False,
            boundary,
        ),
        check(
            "no full closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "does not close `dotD_alpha1`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected transport-conjugation validator replay audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
