"""Audit q79 typed-monad/Cech or HYM connection witness value-fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "attempt_q79_typed_monad_cech_or_hym_connection_witness_value_fill.py"
PACKET = ROOT / "candidate_data" / "q79_typed_monad_cech_or_hym_connection_witness_value_fill_attempt.candidate.json"
CERT = ROOT / "certificates" / "q79_typed_monad_cech_or_hym_connection_witness_value_fill_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_Value_Fill_Attempt_v1.md"

STATUS = "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_VALUE_FILL_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN"
NEXT = "Q79_Selected_Visible_Bundle_or_Direct_HYM_Value_Source_Search_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_packet = json.loads(proc.stdout)

    check("packet and cert match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("theorem proved as honest attempt", packet["theorem"]["proved"] is True, packet["theorem"])
    check("closure not claimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])
    check("all value fill checks pass", all(packet["value_fill_checks"].values()), packet["value_fill_checks"])

    routes = packet["route_attempts"]
    check(
        "route A fails honestly",
        routes["route_A_honest_selected_routec_source_certificate"]["status"] == "BLOCKED"
        and routes["route_A_honest_selected_routec_source_certificate"][
            "selected_hym_operator_source_verified"
        ]
        is False,
        routes["route_A_honest_selected_routec_source_certificate"],
    )
    check(
        "route B lacks typed maps",
        routes["route_B_typed_monad_cech_de_witness"]["status"] == "BLOCKED"
        and routes["route_B_typed_monad_cech_de_witness"]["not_recovered_from_corpus"][
            "explicit_f_i_section_representatives"
        ]
        is True,
        routes["route_B_typed_monad_cech_de_witness"],
    )
    check(
        "route C only conditional",
        routes["route_C_direct_selected_hym_connection"]["status"] == "ABSTRACT_EXISTENCE_ONLY"
        and routes["route_C_direct_selected_hym_connection"][
            "conditional_hym_bridge_proved"
        ]
        is True
        and routes["route_C_direct_selected_hym_connection"]["missing"][
            "selected_HYM_connection_values"
        ]
        is True,
        routes["route_C_direct_selected_hym_connection"],
    )
    check(
        "positive progress separated",
        packet["strongest_positive_progress"]["diagnostic_pipeline_ready"] is True
        and packet["strongest_positive_progress"]["routec_plumbing_diagnostic_passes"] is True,
        packet["strongest_positive_progress"],
    )
    check(
        "minimal payload names direct HYM requirements",
        any(
            "connection coefficients" in item
            for item in packet["minimal_payload_to_close_next"][
                "preferred_route_C_direct_HYM"
            ]
        )
        and any(
            "honest validator replay" in item
            for item in packet["minimal_payload_to_close_next"][
                "preferred_route_C_direct_HYM"
            ]
        ),
        packet["minimal_payload_to_close_next"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check(
        "frontier remains open",
        packet["verdict"]["value_fill_closed"] is False
        and packet["verdict"]["honest_next_step"] == NEXT,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "conditional HYM bridge",
        "does not yet supply selected connection coefficients",
        "Minimal Payload To Close",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 typed-monad/Cech or HYM connection witness value-fill audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
