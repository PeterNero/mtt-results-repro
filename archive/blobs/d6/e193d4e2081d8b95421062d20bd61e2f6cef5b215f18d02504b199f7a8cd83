"""Audit q79 Route-C source or typed D_E decision import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_routec_source_or_typed_de_decision.py"
PACKET = DATA / "q79_routec_source_or_typed_de_decision_import.candidate.json"
CERT = CERTS / "q79_routec_source_or_typed_de_decision_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_RouteC_Source_or_Typed_DE_Decision_Import_v1.md"


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
    script_cert = json.loads(proc.stdout)

    expected = "Q79_ROUTEC_SOURCE_OR_TYPED_DE_DECISION_IMPORTED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported", cert["theorem"]["proved"] is True, cert["theorem"])
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])

    decision = packet["decision"]
    check(
        "selected DE remains absent but pipeline ready",
        decision["selected_D_E_constructed"] is False
        and decision["diagnostic_hodge_pipeline_ready"] is True
        and decision["recommended_first_build"]
        == "C_direct_finite_hym_strominger_solve",
        decision,
    )
    check("three legal routes", len(packet["legal_routes"]) == 3, packet["legal_routes"])
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_claim_selected_D_E_found"]
        and cert["guardrails"]["does_not_use_diagnostic_candidate_as_selected"]
        and cert["guardrails"]["does_not_promote_abstract_HYM_to_matrix"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"]
        and cert["guardrails"]["does_not_claim_full_SM_closure"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records finite scaffold next", "Finite_Selected_Connection_Solve_Scaffold" in note, NOTE)

    print("\nQ79 Route-C source or typed D_E decision import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
