"""Audit Selected_PhiFin_C1_Emission_Packet_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_c1_emission_packet_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_c1_emission_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_C1_Emission_Packet_v1.md"
SCRIPT = REPO / "scripts" / "construct_selected_phifin_c1_emission_packet.py"


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_PHIFIN_C1_EMISSION_PACKET_INTERFACE_BUILT_VALUES_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "six emission slots",
        packet["assembly_order"]
        == [
            "S0_selected_source",
            "S1_transition_or_connection_trace",
            "S2_operator_blocks",
            "S3_alpha1_source_vector",
            "S4_hessian_and_zero_modes",
            "S5_c1_contractions_and_response",
        ],
        packet["assembly_order"],
    )
    ok &= check(
        "values remain open",
        packet["closure_predicate"]["A_selected_emitted"] is False
        and packet["closure_predicate"]["b_selected_emitted"] is False
        and cert["what_remains_open"]["A_selected"] is True
        and cert["what_remains_open"]["b_selected"] is True,
        packet["closure_predicate"],
    )
    ok &= check(
        "minimum next payload targets operator source",
        "selected rho_E/connection" in cert["next_computation"]["minimum_new_payload"]
        and "same-branch dotD_alpha1" in cert["next_computation"]["minimum_new_payload"],
        cert["next_computation"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["claims_selected_source_constructed"] is False
        and cert["guardrails"]["claims_A_selected_emitted"] is False
        and cert["guardrails"]["claims_b_selected_emitted"] is False,
        cert["guardrails"],
    )
    ok &= check(
        "note records interface",
        "values are still open" in note and "Minimum new payload" in note,
        NOTE,
    )

    print("\nSelected PhiFin C1 emission packet audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
