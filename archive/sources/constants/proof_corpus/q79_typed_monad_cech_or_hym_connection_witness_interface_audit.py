"""Audit the q79 typed-monad/Cech or HYM connection witness interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_q79_typed_monad_cech_or_hym_connection_witness_interface.py"
PACKET = ROOT / "candidate_data" / "q79_typed_monad_cech_or_hym_connection_witness_interface.candidate.json"
CERT = ROOT / "certificates" / "q79_typed_monad_cech_or_hym_connection_witness_interface_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_Interface_v1.md"

STATUS = "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_Value_Fill_Attempt_v1"


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
    check("theorem proved as interface", packet["theorem"]["proved"] is True, packet["theorem"])
    check("closure not claimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])
    check("all interface checks pass", all(packet["interface_checks"].values()), packet["interface_checks"])

    schema = packet["witness_payload_schema"]
    check(
        "three routes only",
        set(schema)
        == {
            "route_A_honest_selected_routec_source_certificate",
            "route_B_typed_monad_cech_de_witness",
            "route_C_direct_selected_hym_connection",
        },
        schema,
    )
    check(
        "route B requires typed maps",
        any("typed f_i and g_i" in item for item in schema["route_B_typed_monad_cech_de_witness"]["must_supply"])
        and any("g o f = 0" in item for item in schema["route_B_typed_monad_cech_de_witness"]["must_supply"]),
        schema["route_B_typed_monad_cech_de_witness"],
    )
    check(
        "route C requires residuals and finite packets",
        any("connection coefficients" in item for item in schema["route_C_direct_selected_hym_connection"]["must_supply"])
        and any("finite rho_E" in item for item in schema["route_C_direct_selected_hym_connection"]["must_supply"]),
        schema["route_C_direct_selected_hym_connection"],
    )
    check(
        "existing attempts remain open",
        packet["existing_attempts"]["finite_connection_source_solve"]["selected_connection_source_solved"] is False
        and packet["existing_attempts"]["typed_monad_data_fill"]["typed_maps_filled"] is False,
        packet["existing_attempts"],
    )
    check(
        "frontier retained",
        packet["what_remains_open"]["typed_f_g_maps_or_direct_connection_coefficients"] is True
        and packet["what_remains_open"]["honest_DE_Riesz_Green_dotD_packets"] is True
        and packet["what_remains_open"]["selected_C1_response_matrices"] is True,
        packet["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check("next value fill", packet["verdict"]["next_required_artifact"] == NEXT, packet["verdict"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "does not fill the",
        "witness values",
        "diagnostic shortcuts forbidden",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 typed-monad/Cech or HYM connection witness interface audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
