"""Audit the selected V_alpha operator-source conditional sufficiency theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "prove_selected_valpha_operator_source_sufficiency.py"
CERT = REPO / "certificates" / "selected_valpha_operator_source_sufficiency_certificate.json"
CANDIDATE = REPO / "candidate_data" / "selected_valpha_operator_source_sufficiency.candidate.json"
PAPER = REPO / "proof_corpus" / "Selected_VAlpha_Operator_Source_Sufficiency_Theorem_v1.md"


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
    paper = read(PAPER)

    exits = cert.get("validation_exit_codes", {})
    actual = cert.get("actual_packet_validation", {})
    theorem = cert.get("conditional_theorem", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status sufficiency proved",
            "PASS"
            if cert.get("status")
            == "SELECTED_VALPHA_OPERATOR_SOURCE_CONDITIONAL_SUFFICIENCY_PROVED_SOURCE_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("validation_exit_codes") == exits
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "all hypothetical validators pass",
            "PASS" if exits and all(code == 0 for code in exits.values()) else "FAIL",
            exits,
        ),
        Gate(
            "actual packet remains open",
            "OPEN"
            if actual.get("exit_code") == 2 and actual.get("status") == "OPEN"
            else "FAIL",
            actual,
        ),
        Gate(
            "conditional theorem stated",
            "PASS"
            if theorem.get("proved") is True
            and "Selected_VAlpha_ChernWeil_Operator_Source.v1 validator passes"
            in theorem.get("statement", "")
            else "FAIL",
            theorem,
        ),
        Gate(
            "closes no hidden matrix defect",
            "PASS"
            if closes.get("downstream_validator_stack_has_no_hidden_matrix_defect") is True
            and closes.get("next_work_is_source_derivation_not_validator_plumbing") is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose actual source",
            "PASS"
            if does_not_close.get("actual_selected_source_certificate") is False
            and does_not_close.get("Pic0_selection_or_quotient") is False
            and does_not_close.get("selected_D_E_dotD_Riesz_Green_as_proof_data") is False
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
            "paper records hypothetical scope",
            "PASS"
            if contains_all(
                paper,
                [
                    "Conditional Sufficiency",
                    "hypothetical selected copies",
                    "not a physical proof",
                    "source derivation, not validator plumbing",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Selected V_alpha operator-source sufficiency audit")
    print("==================================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
