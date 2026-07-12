"""Audit q79 retarded/source boundary selector reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_q79_retarded_source_boundary_selector_or_source_origin.py"
PACKET = ROOT / "candidate_data" / "q79_retarded_source_boundary_selector_or_source_origin.candidate.json"
CERT = ROOT / "certificates" / "q79_retarded_source_boundary_selector_or_source_origin_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1.md"

STATUS = "Q79_RETARDED_SOURCE_SELECTOR_REDUCED_TO_SAMESOURCE_CW_OPERATOR_FUNCTIONAL"
NEXT = "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1"


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
    script_packet = json.loads(proc.stdout)

    check("packet and certificate match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("selector checks pass", all(packet["selector_checks"].values()), packet["selector_checks"])
    check("reduction theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("selector not closed", packet["verdict"]["selector_closed"] is False, packet["verdict"])
    check("next artifact", packet["verdict"]["next_required_artifact"] == NEXT, packet["verdict"])

    reduction = packet["selector_reduction"]
    check(
        "manual q79 selection forbidden",
        "observed CP" in reduction["forbidden_shortcut"]
        and reduction["orbit_policy"] == "retain q79/q369 as one selected antiunitary orbit",
        reduction,
    )
    check(
        "correct reduction is CW functional",
        "same-source Chern-Weil/operator functional" in reduction["correct_reduction"],
        reduction["correct_reduction"],
    )
    contract = packet["acceptance_contract"]
    check(
        "contract requires same source payload",
        "same-source D_E/Riesz/Green payload with theorem-derived flags" in contract["must_prove"]
        and "same-branch dotD/alpha1 driver without lifted flags" in contract["must_prove"],
        contract,
    )
    check(
        "contract rejects observed and lifted shortcuts",
        "observed CP sign" in contract["must_not_use"]
        and "lifted selected-source flags" in contract["must_not_use"],
        contract,
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "direct retarded/source selector is not closed",
        "same-source Chern-Weil/operator functional",
        "not from observed CP or lifted selected flags",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 retarded/source boundary selector reduction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
