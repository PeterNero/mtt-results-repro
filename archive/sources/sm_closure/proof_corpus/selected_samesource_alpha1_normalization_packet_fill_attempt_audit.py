"""Audit the same-source alpha1 normalization packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_samesource_alpha1_normalization_packet_fill_attempt.py"
PACKET = ROOT / "candidate_data" / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
CANDIDATE = ROOT / "candidate_data" / "selected_samesource_alpha1_normalization_packet_fill_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_samesource_alpha1_normalization_packet_fill_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_Attempt_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_PACKET_FILL_ATTEMPT_FAILED_FINAL_VALIDATION"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_SourceIdentity_or_RetardedKernel_Value_v1"


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

    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    validator = data["validator_report"]
    summary = data["fill_summary"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "paths",
            cert["candidate_path"].endswith(CANDIDATE.name)
            and cert["filled_packet_path"].endswith(PACKET.name),
            cert,
        ),
        check(
            "candidate values filled",
            packet["source_strength_coordinate"]["lambda_alpha1"] == 1.0
            and packet["normalization_functional"]["N_alpha1_h_ext"] == 1.0
            and packet["tangent_equality"]["residual_l2"] == 0.0,
            packet,
        ),
        check(
            "final validation fails honestly",
            validator["ok"] is False
            and validator["exit_code"] == 1
            and summary["validator_ok"] is False
            and summary["selected_emitted_fields"] == 0,
            validator,
        ),
        check(
            "failure is source/provenance not numerical",
            data["kernel_decision"]["lambda_alpha1"] == 1.0
            and data["kernel_decision"]["N_alpha1_h_ext"] == 1.0
            and data["kernel_decision"]["promotes_selected_value"] is False
            and "selected-source" in data["kernel_decision"]["reason"],
            data["kernel_decision"],
        ),
        check(
            "required failed fields recorded",
            set(data["failed_fields"]) == {
                "source_identity",
                "source_strength_coordinate",
                "normalization_functional",
                "tangent_equality",
                "sector_dotd_equality",
            },
            data["failed_fields"],
        ),
        check(
            "no target fitting or closure",
            data["target_fitting_used"] is False
            and data["closure_claimed"] is False
            and cert["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["selected_value_emitted"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "N_alpha1(h_ext) = 1" in note
            and "final validation fails" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected same-source alpha1 normalization packet fill attempt audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
