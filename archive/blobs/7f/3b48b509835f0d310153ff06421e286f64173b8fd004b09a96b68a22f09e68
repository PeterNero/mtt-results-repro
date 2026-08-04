"""Audit ordered-layer reduction to terminal monad lane selector."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "reduce_ordered_layer_to_terminal_lane_selector.py"
CERT = REPO / "certificates" / "ordered_layer_terminal_lane_selector_reduction_certificate.json"
CANDIDATE = REPO / "candidate_data" / "ordered_layer_terminal_lane_selector_reduction.candidate.json"
PACKET = REPO / "candidate_data" / "visible_rank2_l2_ordered_source.terminal_lane_hypothetical_selected.json"
PAPER = ROOT / "Ordered_Layer_Terminal_Monad_Lane_Selector_Reduction_v1.md"


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

    premises = cert.get("premises", {})
    validation = cert.get("validation", {})
    selected_validation = validation.get("terminal_lane_hypothetical_selected_packet", {})
    theorem = cert.get("reduction_theorem", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("packet exists", "PASS" if PACKET.exists() else "FAIL", PACKET),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status reduction proved",
            "PASS"
            if cert.get("status") == "ORDERED_LAYER_REDUCED_TO_TERMINAL_MONAD_LANE_SELECTOR"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("reduction_theorem") == theorem
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "premises all true",
            "PASS" if premises and all(premises.values()) else "FAIL",
            premises,
        ),
        Gate(
            "hypothetical selected packet passes",
            "PASS"
            if selected_validation.get("exit_code") == 0
            and selected_validation.get("validator_status") == "PASS"
            and selected_validation.get("open_items") == []
            else "FAIL",
            selected_validation,
        ),
        Gate(
            "packet is terminal-lane hypothetical",
            "PASS"
            if packet.get("source", {}).get("source_certificate")
            == "Selected_Terminal_Monad_Lane_Source_Selector.v1"
            and packet.get("source", {}).get("selected_by_mtt") is True
            and packet.get("pic0_resolution", {}).get("resolution") == "pic0_quotient_rule"
            else "FAIL",
            packet.get("source", {}),
        ),
        Gate(
            "reduction theorem",
            "PASS"
            if theorem.get("proved") is True
            and "only remaining local proof obligation" in theorem.get("statement", "")
            else "FAIL",
            theorem,
        ),
        Gate(
            "closes sole local blocker reduction",
            "PASS"
            if closes.get("ordered_layer_source_lane_selector_is_sole_local_blocker") is True
            and closes.get("no_new_ordered_matrix_or_pic0_search_needed_at_this_layer")
            is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose",
            "PASS"
            if does_not_close.get("actual_terminal_monad_lane_selector") is False
            and does_not_close.get("operator_layer_Pic0_recheck") is False
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
            "paper records reduction",
            "PASS"
            if contains_all(
                paper,
                [
                    "reduced to one local missing theorem",
                    "Selected_Terminal_Monad_Lane_Source_Selector.v1",
                    "Pic0 is no longer a local ordered-layer blocker",
                    "not prove the actual selector",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Ordered-layer terminal monad lane selector reduction audit")
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
