"""Audit q79 same-source operator provenance frontier import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_same_source_operator_provenance_frontier.py"
PACKET = DATA / "q79_same_source_operator_provenance_frontier_import.candidate.json"
CERT = CERTS / "q79_same_source_operator_provenance_frontier_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Same_Source_Operator_Provenance_Frontier_Import_v1.md"


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

    expected = "Q79_SAME_SOURCE_OPERATOR_PROVENANCE_FRONTIER_IMPORTED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported", cert["theorem"]["proved"] is True, cert["theorem"])
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])

    reduction = packet["q79_reduction"]
    check(
        "honest packet remains open",
        reduction["honest_current_patchwork_exit_code"] == 2
        and "selected_by_mtt must be true" in reduction["honest_current_open_items"]
        and "source_certificate missing" in reduction["honest_current_open_items"],
        reduction,
    )
    check(
        "diagnostic reduces to primitive C1 only",
        reduction["no_primitive_open_items"] == ["primitive_C1_contractions must be true"]
        and reduction["full_plumbing_diagnostic_exit_code"] == 0
        and reduction["full_plumbing_open_items"] == [],
        reduction,
    )
    check(
        "evidence layer separated",
        packet["source_evidence_status"]["selected_ordered_source_closed"] is True
        and packet["source_evidence_status"]["selected_operator_DE_Riesz_Green_dotD_closed"]
        is False
        and packet["source_evidence_status"]["primitive_c1_contractions_closed"] is False,
        packet["source_evidence_status"],
    )
    check(
        "next gate exact",
        cert["verdict"]["next_required_artifact"]
        == "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1"
        and packet["decision"]["primitive_c1_contractions_not_closed"],
        packet["decision"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_treat_hypothetical_packets_as_proof"]
        and cert["guardrails"]["does_not_claim_selected_operator_source_constructed"]
        and cert["guardrails"]["does_not_claim_selected_RouteC_residual"]
        and cert["guardrails"]["does_not_claim_primitive_C1_closed"]
        and cert["guardrails"]["does_not_claim_full_SM_closure"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records primitive C1 frontier", "primitive `C1` contractions" in note, NOTE)

    print("\nQ79 same-source operator provenance frontier import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
