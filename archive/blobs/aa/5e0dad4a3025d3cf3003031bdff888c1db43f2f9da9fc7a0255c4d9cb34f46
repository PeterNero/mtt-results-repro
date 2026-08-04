"""Audit the ordered-layer Pic0 quotient theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_ordered_layer_pic0_quotient.py"
CERT = REPO / "certificates" / "ordered_layer_pic0_quotient_certificate.json"
CANDIDATE = REPO / "candidate_data" / "ordered_layer_pic0_quotient.candidate.json"
PACKET = (
    REPO
    / "candidate_data"
    / "visible_rank2_l2_ordered_source.monad_difference_pic0_quotiented_layer.json"
)
PAPER = ROOT / "Ordered_Layer_Pic0_Quotient_Theorem_v1.md"


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

    checks = cert.get("source_checks", {})
    theorem = cert.get("quotient_theorem", {})
    validation = cert.get("validation", {})
    layer_validation = validation.get("pic0_quotiented_layer_packet", {})
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
            "status quotient proved",
            "PASS"
            if cert.get("status")
            == "ORDERED_LAYER_PIC0_QUOTIENT_PROVED_OPERATOR_LAYER_REOPENS"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("quotient_theorem") == theorem
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "source checks",
            "PASS" if checks and all(checks.values()) else "FAIL",
            checks,
        ),
        Gate(
            "packet marked Pic0 quotient",
            "PASS"
            if packet.get("pic0_resolution", {}).get("resolution") == "pic0_quotient_rule"
            and packet.get("pic0_resolution", {}).get("source_selected_or_quotiented")
            is True
            and packet.get("pic0_resolution", {}).get("scope")
            == "ordered_chern_h1_curvature_layer_only"
            else "FAIL",
            packet.get("pic0_resolution", {}),
        ),
        Gate(
            "validator removes Pic0 items",
            "OPEN"
            if layer_validation.get("exit_code") == 2
            and validation.get("pic0_items_absent_after_quotient") is True
            and validation.get("only_source_selection_items_remain") is True
            else "FAIL",
            layer_validation,
        ),
        Gate(
            "theorem scoped",
            "PASS"
            if theorem.get("proved_for_ordered_layer") is True
            and "ordered Chern/H1/ordinary-curvature layer only"
            in theorem.get("scope", "")
            and "must recheck Pic0" in theorem.get("reopen_condition", "")
            else "FAIL",
            theorem,
        ),
        Gate(
            "closes layer Pic0",
            "PASS"
            if closes.get("pic0_quotient_for_ordered_chern_h1_curvature_layer")
            is True
            and closes.get("pic0_switch_removed_from_ordered_layer_validator") is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose",
            "PASS"
            if does_not_close.get("terminal_monad_lane_source_selector") is False
            and does_not_close.get("full_physical_pic0_quotient_for_operator_layer")
            is False
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
            "paper records scope",
            "PASS"
            if contains_all(
                paper,
                [
                    "layer-restricted Pic0 quotient",
                    "ordered Chern/H1/ordinary-curvature layer only",
                    "D_E/Riesz/Green/dotD",
                    "not a full physical Pic0 quotient",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Ordered-layer Pic0 quotient audit")
    print("=================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
