"""Audit the terminal-map source principle/base-order attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_terminal_map_source_principle_base_order.py"
CERT = REPO / "certificates" / "terminal_map_source_principle_base_order_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "terminal_map_source_principle_base_order_attempt.candidate.json"
PAPER = ROOT / "Terminal_Map_Source_Principle_and_Base_Order_Attempt_v1.md"


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

    closed = cert.get("closed_now", {})
    not_closed = cert.get("not_closed", {})
    routes = cert.get("route_evaluation", {})
    minimal = cert.get("minimal_remaining_packet", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status reduced open",
            "PASS"
            if cert.get("status")
            == "TERMINAL_MAP_SOURCE_PRINCIPLE_BASE_ORDER_REDUCED_TO_TYPED_OR_OPERATOR_SOURCE_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("minimal_remaining_packet") == minimal
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "closed prerequisites",
            "PASS"
            if closed.get("central_filter_inside_terminal_lane") is True
            and closed.get("ordered_layer_Pic0_quotient") is True
            and closed.get("ordered_layer_reduced_to_terminal_selector") is True
            and closed.get("terminal_monad_sequence_present_in_corpus") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "open selector cutset",
            "PASS"
            if not_closed.get("terminal_map_source_principle") is True
            and not_closed.get("physical_base_order_binding") is True
            and not_closed.get("selected_rhoE_or_transition_data") is True
            else "FAIL",
            not_closed,
        ),
        Gate(
            "routes evaluated",
            "PASS"
            if routes.get("R1_central_circle_filter", {}).get("status") == "CLOSED_SUBFILTER"
            and routes.get("R3_literal_terminal_monad_map", {}).get("status")
            == "BLOCKED_TYPED_MAPS_AND_VISIBLE_ROLE"
            and routes.get("R7_same_source_operator_response", {}).get("status")
            == "PRIMARY_OPEN_SELECTED_RESPONSE"
            else "FAIL",
            routes,
        ),
        Gate(
            "minimal packet named",
            "PASS"
            if minimal.get("name") == "Selected_Terminal_Map_Base_Order_Source_Packet.v1"
            and len(minimal.get("must_supply", [])) == 4
            else "FAIL",
            minimal,
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails
            and guardrails.get("claims_actual_terminal_map_selector_proved") is False
            and all(value is False for key, value in guardrails.items() if key != "claims_actual_terminal_map_selector_proved")
            else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records cutset",
            "PASS"
            if contains_all(
                paper,
                [
                    "terminal-map selector is not proved",
                    "central neutrality and ordered-layer Pic0 are closed",
                    "Selected_Terminal_Map_Base_Order_Source_Packet.v1",
                    "same-source operator response",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Terminal-map source principle/base-order attempt audit")
    print("=====================================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
