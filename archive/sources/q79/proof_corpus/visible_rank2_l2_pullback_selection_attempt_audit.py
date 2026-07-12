"""Audit the visible L^2 pullback selection theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_visible_rank2_l2_pullback_selection_attempt.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_pullback_selection_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_pullback_selection_attempt_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Pullback_Selection_Attempt_v1.md"


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
    paper = read(PAPER)

    evidence = cert.get("selection_evidence", {})
    relative = cert.get("relative_selection_theorem", {})
    unconditional = cert.get("unconditional_selection_theorem", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status reduced to source certificate",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_PULLBACK_SELECTION_REDUCED_TO_SOURCE_CERTIFICATE"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("relative_selection_theorem")
            == cert.get("relative_selection_theorem")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "actual packet valid but unselected",
            "PASS"
            if evidence.get("actual_unselected_packet_validates") is True
            and evidence.get("actual_packet_does_not_promote") is True
            else "FAIL",
            str(evidence),
        ),
        Gate(
            "hypothetical selected packet promotes",
            "PASS"
            if evidence.get("hypothetical_selected_same_matrices_promote") is True
            and evidence.get("hypothetical_h1_stays_8") is True
            else "FAIL",
            str(evidence),
        ),
        Gate(
            "source absence detected",
            "OPEN"
            if evidence.get("source_hunt_still_reports_selected_data_absent") is True
            and evidence.get("standard_deck_scaffold_selection_still_open") is True
            and evidence.get("constants_automorphy_attempt_symbolic_only_values_open")
            is True
            else "FAIL",
            str(evidence),
        ),
        Gate(
            "relative theorem proved",
            "PASS"
            if relative.get("proved") is True
            and relative.get("matrices_changed_between_actual_and_hypothetical") is False
            else "FAIL",
            str(relative),
        ),
        Gate(
            "unconditional theorem not overclaimed",
            "OPEN"
            if unconditional.get("proved") is False
            and "source certificate selecting the base-pullback L^2 representative"
            in unconditional.get("blocked_by", [])
            else "FAIL",
            str(unconditional),
        ),
        Gate(
            "closes exact gap only",
            "PASS"
            if closes.get("mathematical_gap_between_pullback_packet_and_selected_packet")
            is True
            and closes.get("unconditional_MTT_selection_of_L2_pullback") is False
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("write_or_find_selected_pullback_L2_source_certificate")
            is True
            and still_open.get("promote_packet_to_SELECTED_DATA") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_unconditional_MTT_selection") is False
            and guardrails.get("claims_selected_packet_written") is False
            and guardrails.get("uses_observed_flavor_data") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records selection attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "same matrices",
                    "h1=8",
                    "SELECTED_DATA",
                    "source certificate selecting the base-pullback L^2 representative",
                    "unconditional selection theorem is not proved",
                    "only remaining gap",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 pullback selection attempt audit")
    print("====================================================")
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
