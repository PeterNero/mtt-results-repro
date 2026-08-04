"""Audit Selected_PhiFin_S2_27_Mode_Provenance_Theorem_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s2_27_mode_provenance_theorem_attempt_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s2_27_mode_provenance_theorem_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S2_27_Mode_Provenance_Theorem_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_phifin_s2_27_mode_provenance_theorem.py"


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
    evidence = packet["evidence_table"]
    closure = packet["current_closure"]
    eta = packet["diagnostic_eta"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "CONDITIONAL_PROVENANCE_THEOREM_CLOSED_UNCONDITIONAL_MORPHISM_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "conditional not unconditional",
        packet["conditional_theorem"]["proved"] is True
        and packet["unconditional_attempt"]["proved"] is False,
        packet["unconditional_attempt"],
    )
    ok &= check(
        "evidence split",
        evidence["S0_abstract_selected_source"] is True
        and evidence["same_27_mode_basis_available"] is True
        and evidence["actual_27_mode_matrix_entries_emitted"] is True
        and evidence["diagnostic_eta_below_threshold"] is True
        and evidence["functorial_finite_Phi_fin_trace_proved"] is False
        and evidence["existing_27_mode_matrices_identified_as_selected_compression"] is False,
        evidence,
    )
    ok &= check(
        "eta ready but unpromoted",
        eta["eta_if_provenance_supplied"] == 1.0
        and eta["passes_threshold"] is True
        and eta["selected_eta_emitted_now"] is False,
        eta,
    )
    ok &= check(
        "missing morphism isolated",
        packet["missing_morphism"]["name"]
        == "FiniteTraceMorphismIdentifies27ModeScaffold"
        and len(packet["missing_morphism"]["must_supply"]) == 5,
        packet["missing_morphism"],
    )
    ok &= check(
        "closure honest",
        closure["conditional_provenance_theorem_closed"] is True
        and closure["unconditional_provenance_theorem_closed"] is False
        and closure["selected_eta_promoted"] is False
        and closure["selected_gap_error_certificate_closed"] is False,
        closure,
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_promote_conditional_to_unconditional"] is True
        and cert["guardrails"]["does_not_set_selected_source_flags"] is True
        and cert["guardrails"]["does_not_treat_model_active_as_selected"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records next morphism",
        "The conditional theorem is proved" in note
        and "FiniteTraceMorphismIdentifies27ModeScaffold" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 27-mode provenance theorem attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
