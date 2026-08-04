"""Audit q79 selected D_E/Green/dotD source gate import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_selected_de_green_dotd_source_gate.py"
PACKET = DATA / "q79_selected_de_green_dotd_source_gate_import.candidate.json"
CERT = CERTS / "q79_selected_de_green_dotd_source_gate_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_DE_Green_DotD_Source_Gate_Import_v1.md"


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

    expected = "Q79_SELECTED_DE_GREEN_DOTD_SOURCE_GATE_IMPORTED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported", cert["theorem"]["proved"] is True, cert["theorem"])
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])

    routec = packet["routec_stack"]
    check(
        "honest stack fails while diagnostic stack passes",
        all(code == 1 for code in routec["honest_exit_codes"].values())
        and all(code == 0 for code in routec["diagnostic_exit_codes"].values())
        and routec["diagnostic_not_proof"],
        routec,
    )

    primitive = packet["primitive_c1_source_gate"]
    check(
        "primitive C1 source gate has 24 atoms",
        primitive["atom_count"] == 24
        and primitive["status"] == "OPEN_SELECTED_DE_GREEN_DOTD_SOURCE_REQUIRED",
        primitive,
    )

    check(
        "next gate exact",
        cert["verdict"]["next_required_artifact"]
        == "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1"
        and packet["decision"]["selected_RouteC_residual_or_typed_DE_construction_not_closed"],
        packet["decision"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_treat_selected_flags_only_as_proof"]
        and cert["guardrails"]["does_not_claim_selected_operator_source_constructed"]
        and cert["guardrails"]["does_not_claim_selected_RouteC_residual"]
        and cert["guardrails"]["does_not_claim_primitive_C1_values_computed"]
        and cert["guardrails"]["does_not_claim_full_SM_closure"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records diagnostic not proof", "not proof" in note, NOTE)

    print("\nQ79 selected D_E/Green/dotD source gate import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
