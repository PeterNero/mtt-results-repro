"""Audit q79 Route-C selected-source witness-reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_routec_selected_source_witness_reduction.py"
PACKET = DATA / "q79_routec_selected_source_witness_reduction_import.candidate.json"
CERT = CERTS / "q79_routec_selected_source_witness_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_RouteC_Selected_Source_Witness_Reduction_Import_v1.md"

STATUS = "Q79_ROUTEC_SELECTED_SOURCE_WITNESS_REDUCTION_IMPORTED"
NEXT = "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1"


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

    check("certificate status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported", cert["theorem"]["proved"] is True, cert["theorem"])
    check(
        "closure not claimed",
        cert["theorem"]["closure_claimed"] is False
        and packet["theorem"]["closure_claimed"] is False,
        cert["theorem"],
    )
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])

    honest = packet["honest_routec_selected_source_attempt"]
    diagnostic = packet["hypothetical_selected_source_diagnostic"]
    check(
        "honest selected source fails",
        honest["validator_exit_code"] == 1
        and honest["selected_hym_operator_source_verified"] is False,
        honest,
    )
    check(
        "diagnostic passes only as diagnostic",
        diagnostic["validator_exit_code"] == 0
        and diagnostic["diagnostic_not_proof"] is True,
        diagnostic,
    )

    routes = packet["route_evaluation"]
    check(
        "routes classified",
        routes["route_A_selected_routec_source_certificate"]["status"]
        == "BLOCKED_CURRENT_HONEST_PACKET_FAILS"
        and routes["route_B_typed_monad_cech_de_construction"]["status"] == "BLOCKED"
        and routes["route_C_direct_HYM_connection"]["status"] == "ABSTRACT_EXISTENCE_ONLY",
        routes,
    )
    check(
        "witness contracts explicit",
        packet["selected_connection_witness_contract"]["schema"]
        == "Q79SelectedConnectionWitnessContract.v1"
        and packet["typed_de_witness_contract"]["schema"] == "Q79TypedDEWitnessContract.v1"
        and packet["typed_de_witness_contract"]["currently_computable"] is False
        and packet["typed_de_witness_contract"]["one_of_count"] == 3,
        {
            "selected": packet["selected_connection_witness_contract"],
            "typed": packet["typed_de_witness_contract"],
        },
    )
    check(
        "remaining frontier retained",
        cert["what_remains_open"]["selected_connection_witness_values"] is True
        and cert["what_remains_open"]["honest_selected_DE_Riesz_Green_dotD_packets"] is True
        and cert["what_remains_open"]["selected_C1_response_matrices"] is True
        and cert["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
        cert["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in cert["guardrails"].values()), cert["guardrails"])
    check("next artifact", cert["verdict"]["next_required_artifact"] == NEXT, cert["verdict"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "typed",
        "monad/Cech `D_E` data",
        "selected HYM/Route-C connection with residual bounds",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 Route-C selected-source witness-reduction import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
