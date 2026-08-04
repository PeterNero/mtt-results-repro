"""Audit the Selected_VAlpha_ChernWeil_Operator_Source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "attempt_selected_valpha_chern_weil_operator_source.py"
CERT = REPO / "certificates" / "selected_valpha_chern_weil_operator_source_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "selected_valpha_chern_weil_operator_source_attempt.candidate.json"
PACKET = REPO / "candidate_data" / "selected_valpha_chern_weil_operator_source.current_attempt.json"
PAPER = REPO / "proof_corpus" / "Selected_VAlpha_ChernWeil_Operator_Source_Attempt_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    packet = load(PACKET)
    paper = read(PAPER)

    parsed = cert.get("validator_result", {}).get("parsed_report", {})
    sub = cert.get("subvalidator_exit_codes", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})
    closed_inputs = cert.get("closed_inputs_consumed", {})
    first_open = cert.get("first_open_items", [])

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("attempt packet exists", "PASS" if PACKET.exists() else "FAIL", PACKET),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status open",
            "PASS"
            if cert.get("status") == "SELECTED_VALPHA_CHERN_WEIL_OPERATOR_SOURCE_ATTEMPT_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("open_item_count") == cert.get("open_item_count")
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "packet schema",
            "PASS"
            if packet.get("schema") == "SelectedVAlphaChernWeilOperatorSource.v1"
            and packet.get("source_identity", {}).get("branch_id") == "q79/F,m=1"
            else "FAIL",
            packet.get("schema"),
        ),
        Gate(
            "validator returns open",
            "OPEN"
            if parsed.get("exit_code") == 2 and parsed.get("status") == "OPEN"
            else "FAIL",
            parsed.get("open_items", [])[:12],
        ),
        Gate(
            "subvalidator pattern",
            "PASS"
            if sub.get("ordered_source") == 2
            and sub.get("s3_class_restriction") == 0
            and sub.get("visible_gs_source") == 1
            and sub.get("selected_source_promotion") == 1
            else "FAIL",
            sub,
        ),
        Gate(
            "closed inputs consumed",
            "PASS" if closed_inputs and all(value is True for value in closed_inputs.values()) else "FAIL",
            closed_inputs,
        ),
        Gate(
            "first open flags include source core",
            "PASS"
            if "selected_by_mtt must be true" in first_open
            and "terminal_monad_difference_L3_minus_K2_selector_closed must be true"
            in first_open
            and "pic0_selected_or_quotiented must be true" in first_open
            and "chern_weil_row_derived_from_same_source must be true" in first_open
            else "FAIL",
            first_open[:20],
        ),
        Gate(
            "closes executable slot only",
            "PASS"
            if closes.get("selected_valpha_operator_source_validator_created") is True
            and closes.get("critical_packet_attempt_materialized") is True
            and closes.get("open_fields_are_machine_reported") is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose",
            "PASS"
            if does_not_close.get("selected_visible_valpha_source") is False
            and does_not_close.get("Pic0_selection_or_quotient") is False
            and does_not_close.get("selected_D_E_dotD_Riesz_Green") is False
            and does_not_close.get("full_SM_closure") is False
            else "FAIL",
            does_not_close,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records slot",
            "PASS"
            if contains_all(
                paper,
                [
                    "Selected_VAlpha_ChernWeil_Operator_Source.v1",
                    "Current Validator Result",
                    "What Passed",
                    "What Remains Open",
                    "This is not full SM closure.",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Selected V_alpha Chern-Weil operator source attempt audit")
    print("=========================================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
