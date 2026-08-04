"""Audit the monad-difference L^2 source sufficiency theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_monad_difference_l2_source_sufficiency.py"
CERT = REPO / "certificates" / "monad_difference_l2_source_sufficiency_certificate.json"
CANDIDATE = REPO / "candidate_data" / "monad_difference_l2_source_sufficiency.candidate.json"
PACKET = (
    REPO / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_hypothetical_selected.json"
)
PAPER = ROOT / "Monad_Difference_L2_Source_Sufficiency_Theorem_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    packet = load_json(PACKET)
    paper = read(PAPER)

    packets = cert.get("packets", {})
    unselected = packets.get("unselected_validation", {})
    selected = packets.get("hypothetical_selected_validation", {})
    delta = cert.get("promotion_delta", {})
    theorem = cert.get("relative_theorem", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("hypothetical packet exists", "PASS" if PACKET.exists() else "FAIL", str(PACKET)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status sufficiency proved",
            "PASS"
            if cert.get("status")
            == "MONAD_DIFFERENCE_L2_SOURCE_SUFFICIENCY_PROVED_SELECTION_THEOREM_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("relative_theorem") == cert.get("relative_theorem")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "unselected refused",
            "OPEN"
            if unselected.get("exit_code") == 2
            and unselected.get("parsed_report", {}).get("status") == "OPEN"
            else "FAIL",
            str(unselected),
        ),
        Gate(
            "hypothetical selected passes",
            "PASS"
            if selected.get("exit_code") == 0
            and selected.get("parsed_report", {}).get("status") == "PASS"
            and selected.get("parsed_report", {}).get("failures") == []
            and selected.get("parsed_report", {}).get("open_items") == []
            else "FAIL",
            str(selected),
        ),
        Gate(
            "selected packet marked selected",
            "PASS"
            if packet.get("status") == "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED"
            and packet.get("source", {}).get("selected_by_mtt") is True
            and packet.get("pic0_resolution", {}).get("resolution")
            == "neutral_character_selected"
            else "FAIL",
            str(packet),
        ),
        Gate(
            "delta scoped",
            "PASS"
            if delta.get("only_source_selection_and_pic0_fields_changed") is True
            and "source.selected_by_mtt" in delta.get("changed_fields", [])
            and "pic0_resolution.source_selected_or_quotiented"
            in delta.get("changed_fields", [])
            else "FAIL",
            str(delta),
        ),
        Gate(
            "relative theorem proved",
            "PASS" if theorem.get("proved") is True else "FAIL",
            str(theorem),
        ),
        Gate(
            "closes sufficiency",
            "PASS"
            if closes.get("sufficiency_of_selected_monad_difference_for_ordered_source_gate")
            is True
            and closes.get("remaining_gap_localized_to_source_selection_and_pic0") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "does not overclose",
            "PASS"
            if all(value is False for value in does_not_close.values())
            else "FAIL",
            str(does_not_close),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("prove_Selected_Monad_Difference_L2_Source_v1") is True
            and still_open.get("compute_same_source_D_E_dotD_Riesz_Green") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "relative theorem",
                    "hypothetical selected packet passes",
                    "changed only source-selection and Pic0 fields",
                    "Selected_Monad_Difference_L2_Source.v1",
                    "does not prove that MTT has selected L3-K2",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Monad-difference L2 source sufficiency audit")
    print("============================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
