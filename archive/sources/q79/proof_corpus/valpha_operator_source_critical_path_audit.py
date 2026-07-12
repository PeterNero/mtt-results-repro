"""Audit the V_alpha operator-source critical-path reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "reduce_valpha_operator_source_critical_path.py"
CERT = REPO / "certificates" / "valpha_operator_source_critical_path_certificate.json"
CANDIDATE = REPO / "candidate_data" / "valpha_operator_source_critical_path.candidate.json"
PAPER = REPO / "proof_corpus" / "VAlpha_Operator_Source_Critical_Path_v1.md"


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

    retired = cert.get("retired_blockers", {})
    remaining = cert.get("remaining_independent_obligations", {})
    row = cert.get("source_row_diagnosis", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})
    contract = cert.get("critical_packet_contract", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status reduced",
            "PASS"
            if cert.get("status")
            == "VALPHA_OPERATOR_SOURCE_CRITICAL_PATH_REDUCED_TO_SINGLE_PACKET_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("critical_packet_contract") == contract
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "retired blockers all true",
            "PASS" if retired and all(value is True for value in retired.values()) else "FAIL",
            retired,
        ),
        Gate(
            "remaining obligations all true",
            "OPEN"
            if remaining and all(value is True for value in remaining.values())
            else "FAIL",
            remaining,
        ),
        Gate(
            "row and finite operators diagnosed",
            "PASS"
            if row.get("visible_gs_attempt_has_required_row") is True
            and row.get("visible_gs_attempt_rejected_as_unselected_source") is True
            and row.get("finite_D_E_Green_dotD_shape_reaches_validator_layer") is True
            and row.get("q369_conjugate_reaches_same_layer") is True
            else "FAIL",
            row,
        ),
        Gate(
            "contract names exact packet",
            "PASS"
            if contract.get("name") == "Selected_VAlpha_ChernWeil_Operator_Source.v1"
            and "validate_selected_qa_su3_same_source_valpha_s3_operator_packet.py"
            in contract.get("would_unlock_validators", [])
            and "selected or physically quotiented Pic0 character"
            in contract.get("must_supply", [])
            else "FAIL",
            contract,
        ),
        Gate(
            "closes reduction only",
            "PASS"
            if closes.get("remaining_cut_set_collapsed_to_selected_source_packet") is True
            and closes.get("critical_path_is_not_h1_algebra") is True
            and closes.get("critical_path_is_not_s3_freed_witten_or_block_projectors") is True
            and closes.get("critical_path_is_not_visible_gs_curvature_row") is True
            and closes.get("critical_path_is_not_finite_q79_q369_matrix_shape") is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose source",
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
            "paper records critical packet",
            "PASS"
            if contains_all(
                paper,
                [
                    "Selected_VAlpha_ChernWeil_Operator_Source.v1",
                    "Retired Blockers",
                    "Still Open",
                    "The next step is therefore not another arithmetic search.",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha operator-source critical-path audit")
    print("===========================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
