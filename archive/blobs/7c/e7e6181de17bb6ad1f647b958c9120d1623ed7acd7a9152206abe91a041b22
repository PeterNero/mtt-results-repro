"""Audit Selected_PhiFin_S0_Source_Prefix_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s0_source_prefix_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s0_source_prefix.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S0_Source_Prefix_v1.md"
SCRIPT = REPO / "scripts" / "prove_selected_phifin_s0_source_prefix.py"


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
        cert["status"] == "SELECTED_PHIFIN_S0_SOURCE_PREFIX_CLOSED_S1_S2_VALUES_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check("S0 closed", cert["s0_closed"] is True and packet["s0_closed"] is True, cert)
    ok &= check(
        "all S0 premises pass",
        all(packet["s0_premises"].values()),
        packet["s0_premises"],
    )
    ok &= check(
        "advanced packet closes only S0",
        packet["advanced_packet"]["emission_slots"]["S0_selected_source"]["status"]
        == "CLOSED_ABSTRACT_SELECTED_SOURCE"
        and packet["advanced_packet"]["emission_slots"]["S1_transition_or_connection_trace"]["status"]
        == "OPEN"
        and packet["what_remains_open"]["S1_transition_or_connection_trace"] is True,
        packet["advanced_packet"]["emission_slots"],
    )
    ok &= check(
        "minimal remaining lemma named",
        cert["minimal_remaining_lemma"] == "SelectedPhiFinFiniteTraceLemma",
        cert["minimal_remaining_lemma"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["claims_finite_rhoE_connection_emitted"] is False
        and cert["guardrails"]["claims_D_E_Riesz_Green_dotD_emitted"] is False
        and cert["guardrails"]["claims_A_selected_emitted"] is False
        and cert["guardrails"]["claims_b_selected_emitted"] is False,
        cert["guardrails"],
    )
    ok &= check(
        "note records narrow proof",
        "abstract selected smooth source" in note
        and "does not emit finite" in note,
        NOTE,
    )

    print("\nSelected PhiFin S0 source prefix audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
