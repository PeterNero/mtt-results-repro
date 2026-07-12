"""Audit Selected_PhiFin_S1_RhoE_Trace_Fill_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s1_rhoe_trace_fill_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s1s2_value_emission.partial_filled.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S1_RhoE_Trace_Fill_v1.md"
SCRIPT = REPO / "scripts" / "fill_selected_phifin_s1_rhoe_trace.py"


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
    s1 = packet["S1_transition_or_connection_trace"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_PHIFIN_S1_RHOE_TRACE_PARTIAL_FILL_DONE_S2_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "S1 rhoE filled",
        packet["status"] == "PARTIAL_FILLED_S1_RHOE_TRACE_S2_VALUES_OPEN"
        and s1["selected_connection_or_rhoE_entries"]["status"] == "PARTIAL_FILLED_PROJECTIVE_RHOE_TRACE"
        and s1["nonidentity_or_equivalent_connection_trace"] is True,
        s1,
    )
    ok &= check(
        "identity smoke rejected",
        packet["discipline"]["identity_smoke_used_as_selected_rhoE"] is False
        and cert["what_closes_now"]["identity_rhoE_smoke_replaced_for_S1"] is True,
        packet["discipline"],
    )
    ok &= check(
        "numeric checks imported",
        s1["selected_connection_or_rhoE_entries"]["numeric_checks"]["projective_commutator_residual"]
        < 1e-9
        and s1["selected_connection_or_rhoE_entries"]["numeric_checks"]["nonidentity_norm_g1_minus_I"]
        > 1.0,
        s1["selected_connection_or_rhoE_entries"]["numeric_checks"],
    )
    ok &= check(
        "full payload remains open",
        packet["partial_fill_guardrail"]["full_selected_payload_emitted"] is False
        and packet["validator_replay"]["selected_source_promotion_passes_without_lifted_flags"] is False
        and cert["what_remains_open"]["S2_selected_D_E_dotD_Riesz_Green_entries"] is True,
        packet["partial_fill_guardrail"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["claims_full_selected_payload_emitted"] is False
        and cert["guardrails"]["claims_selected_source_flags_may_be_set_true"] is False
        and cert["guardrails"]["claims_A_selected_emitted"] is False,
        cert["guardrails"],
    )
    ok &= check(
        "note records partial fill",
        "partially filled" in note and "does not set selected" in note,
        NOTE,
    )

    print("\nSelected PhiFin S1 rhoE trace fill audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
