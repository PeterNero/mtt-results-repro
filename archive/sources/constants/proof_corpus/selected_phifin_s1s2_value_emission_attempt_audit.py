"""Audit Selected_PhiFin_S1S2_Value_Emission_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s1s2_value_emission_attempt_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s1s2_value_emission_attempt.candidate.json"
TEMPLATE = REPO / "candidate_data" / "selected_phifin_s1s2_value_emission.required_payload.template.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S1S2_Value_Emission_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_phifin_s1s2_value_emission.py"


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
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
        cert["status"]
        == "SELECTED_PHIFIN_S1S2_VALUE_EMISSION_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_VALUES",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "criterion proved",
        cert["criterion_proved"] is True
        and packet["value_emission_criterion"]["proved"] is True,
        packet["value_emission_criterion"],
    )
    ok &= check(
        "current files rejected",
        packet["analysis"]["all_current_value_files_rejected_as_selected_emission"] is True
        and packet["analysis"]["value_shapes_present_in_current_files"] is True,
        packet["analysis"],
    )
    ok &= check(
        "template requires selected entries",
        template["S1_transition_or_connection_trace"]["selected_connection_or_rhoE_entries"] is None
        and template["S2_galerkin_basis_and_operator_blocks"]["D_E_matrix_entries"] is None
        and template["validator_replay"]["selected_source_promotion_passes_without_lifted_flags"] is None,
        template,
    )
    ok &= check(
        "values remain open",
        cert["what_remains_open"]["fill_selected_connection_or_rhoE_entries"] is True
        and cert["what_remains_open"]["fill_selected_D_E_dotD_Riesz_Green_entries"] is True
        and cert["what_remains_open"]["A_selected"] is True,
        cert["what_remains_open"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["claims_selected_values_emitted"] is False
        and cert["guardrails"]["uses_formal_lift_flags_as_proof"] is False
        and cert["guardrails"]["claims_validators_pass_honestly"] is False,
        cert["guardrails"],
    )
    ok &= check(
        "note records rejection and next artifact",
        "identity smoke rhoE" in note and "Selected_PhiFin_S1S2_Value_Emission_v1" in note,
        NOTE,
    )

    print("\nSelected PhiFin S1S2 value emission attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
