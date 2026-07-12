"""Audit Selected_PhiFin_Finite_Trace_Existence_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_finite_trace_existence_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_finite_trace_existence.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_Finite_Trace_Existence_v1.md"
SCRIPT = REPO / "scripts" / "prove_selected_phifin_finite_trace_existence.py"


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
        cert["status"] == "SELECTED_PHIFIN_FINITE_TRACE_EXISTENCE_PROVED_VALUES_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "theorem proved",
        cert["theorem_proved"] is True and all(packet["prerequisites"].values()),
        packet["prerequisites"],
    )
    ok &= check(
        "abstract S1-S2 closure only",
        packet["abstract_closure"]["S1_transition_or_connection_trace_exists"] is True
        and packet["abstract_closure"]["S2_DE_dotD_matrices_exist"] is True
        and packet["validator_implication"]["can_set_selected_source_verified_now"] is False,
        packet["abstract_closure"],
    )
    ok &= check(
        "values remain required",
        packet["emission_still_required"]["selected_connection_or_rhoE_entries"] is True
        and packet["emission_still_required"]["D_E_matrix_entries"] is True
        and packet["emission_still_required"]["gap_gamma_N_and_residual_epsilon_N"] is True,
        packet["emission_still_required"],
    )
    ok &= check(
        "next artifact",
        cert["next_required_artifact"] == "Selected_PhiFin_S1S2_Value_Emission_v1",
        cert["next_required_artifact"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["claims_finite_values_emitted"] is False
        and cert["guardrails"]["claims_validators_pass_honestly"] is False
        and cert["guardrails"]["claims_A_selected_emitted"] is False,
        cert["guardrails"],
    )
    ok &= check(
        "note records value boundary",
        "finite values are still\nopen" in note and "Emission Boundary" in note,
        NOTE,
    )

    print("\nSelected PhiFin finite trace existence audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
