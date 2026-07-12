"""Audit Selected_PhiFin_S2_Eta_N_Bound_or_Source_Flag_Emission_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_phifin_s2_eta_n_bound_or_source_flag_emission_attempt_certificate.json"
)
PACKET = (
    REPO
    / "candidate_data"
    / "selected_phifin_s2_eta_n_bound_or_source_flag_emission_attempt.candidate.json"
)
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S2_Eta_N_Bound_or_Source_Flag_Emission_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_phifin_s2_eta_n_bound_or_source_flag_emission.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    packet = load(PACKET)
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
    eta = packet["corpus_eta_evidence"]
    flags = packet["source_flag_state"]
    decision = packet["promotion_decision"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "ETA_N_NOT_EMITTED_SOURCE_FLAGS_NOT_PROMOTED",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "eta absent but threshold retained",
        eta["eta_N_value_emitted"] is False
        and eta["eta_N_value"] is None
        and eta["eta_threshold"] == 2.1932454224643014
        and eta["selected_full_operator_compression_A_sel_N_emitted"] is False
        and eta["model_operator_A_model_N_emitted"] is True,
        eta,
    )
    ok &= check(
        "S0 does not promote finite S2 flags",
        flags["abstract_S0_selected_source_closed"] is True
        and flags["S0_selected_source_verified_without_lifted_flags"] is True
        and flags["finite_D_E_selected_source_verified"] is False
        and flags["finite_dotD_selected_source_verified"] is False
        and flags["finite_dotD_alpha1_driver_verified"] is False,
        flags,
    )
    ok &= check(
        "no promotion",
        all(value is False for value in decision.values()),
        decision,
    )
    ok &= check(
        "negative result proved",
        packet["negative_result"]["proved"] is True
        and "abstract S0" in packet["negative_result"]["statement"],
        packet["negative_result"],
    )
    ok &= check(
        "next interface named",
        packet["verdict"]["next_required_artifact"]
        == "Selected_PhiFin_S2_A_sel_N_Form_Bound_Interface_v1",
        packet["verdict"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_treat_S0_as_S2"] is True
        and cert["guardrails"]["does_not_invent_eta_N"] is True
        and cert["guardrails"]["does_not_flip_source_flags"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records A_sel,N requirement",
        "A_sel,N" in note and "abstract selected smooth source is not the same thing" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 eta_N/source-flag emission attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
