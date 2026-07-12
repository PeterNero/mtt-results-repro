"""Audit the finite projector source-promotion theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_finite_projector_source_promotion.py"
CANDIDATE = ROOT / "candidate_data" / "selected_finite_projector_source_promotion.candidate.json"
CERT = ROOT / "certificates" / "selected_finite_projector_source_promotion_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteProjector_SourcePromotion_v1.md"

STATUS = "MTT_SELECTED_FINITE_PROJECTOR_SOURCE_PROMOTION_PROVED_DOTD_OPEN"
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
    decision = data["promotion_decision"]
    evidence = data["evidence_chain"]
    boundary = data["boundary"]
    slots = data["promoted_sector_slots"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "theorem proved",
            data["theorem"]["proved"] is True
            and "raw untransported" in data["theorem"]["statement"]
            and "dotD_alpha1 is excluded" in data["theorem"]["proof_steps"][-1],
            data["theorem"],
        ),
        check(
            "evidence chain closed",
            evidence["bridge_theorem_proved"] is True
            and evidence["finite_projector_values_emitted"] is True
            and evidence["gauge_transported_trace_proved"] is True
            and evidence["symbolic_transport_validator_closed"] is True
            and evidence["all_sector_replays_pass"] is True
            and evidence["target_fitting_used"] is False,
            evidence,
        ),
        check(
            "sector promotions complete",
            len(slots) == 7
            and all(
                slot["source_verified_by_transport_conjugation"] is True
                and slot["stationary_rho_s_promoted"] is True
                and slot["projector_idempotent"] is True
                and slot["projector_self_adjoint"] is True
                and slot["rank_preserved"] is True
                and slot["green_operator_valid"] is True
                and slot["finite_raw_truncation_replay_used"] is False
                for slot in slots.values()
            )
            and slots["Q"]["rank"] == 3
            and slots["H"]["rank"] == 1,
            slots,
        ),
        check(
            "promotion decision exact",
            decision["finite_projector_source_promotion_proved"] is True
            and decision["selected_projector_source_verified"] is True
            and decision["validator_ready_stationary_rho_s"] is True
            and decision["old_raw_value_flags_left_unchanged"] is True
            and decision["raw_untransported_packet_promoted"] is False
            and decision["transported_packet_promoted"] is True,
            decision,
        ),
        check(
            "dotD boundary honest",
            decision["selected_dotD_source_verified"] is False
            and decision["alpha1_driver_verified"] is False
            and "selected dotD_alpha1 replay" in boundary["what_is_not_proved"]
            and boundary["raw_direct_truncated_residual"] > 0.01
            and boundary["gauge_frame_residual"] < 1e-12,
            boundary,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records theorem and boundary",
            "selected_source_verified" in note
            and "raw untransported `B_N` packet is not promoted" in note
            and "stationary finite projector source promotion only" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected finite projector source-promotion audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
