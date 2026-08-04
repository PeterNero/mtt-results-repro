"""Audit the Iwasawa monad L^2 branch-orientation candidate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_iwasawa_monad_l2_branch_orientation_candidate.py"
CERT = REPO / "certificates" / "iwasawa_monad_l2_branch_orientation_candidate_certificate.json"
CANDIDATE = REPO / "candidate_data" / "iwasawa_monad_l2_branch_orientation_candidate.candidate.json"
PACKET = REPO / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
PAPER = ROOT / "Iwasawa_Monad_L2_Branch_Orientation_Candidate_v1.md"


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

    scan = cert.get("ordered_difference_scan", {})
    key = cert.get("key_candidate", {})
    packet_result = cert.get("ordered_source_candidate_packet", {}).get("validation", {})
    packet_report = packet_result.get("parsed_report", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("packet exists", "PASS" if PACKET.exists() else "FAIL", str(PACKET)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status candidate found",
            "PASS"
            if cert.get("status")
            == "IWASAWA_MONAD_L2_BRANCH_ORIENTATION_CANDIDATE_FOUND_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("key_candidate") == cert.get("key_candidate")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "exact line-table difference",
            "PASS"
            if key.get("ordered_difference") == "L3_minus_K2"
            and key.get("value") == [1, -2, 0]
            and key.get("double_value") == [2, -4, 0]
            and key.get("matches_target_L") is True
            and key.get("matches_target_L2_after_doubling") is True
            else "FAIL",
            str(key),
        ),
        Gate(
            "dual typed g3 recorded",
            "PASS"
            if key.get("dual_printed_g3_type") == [-1, 2, 0]
            and key.get("dual_printed_g3_type_is_negative_target") is True
            else "FAIL",
            str(key),
        ),
        Gate(
            "scan records target",
            "PASS"
            if "L3_minus_K2" in scan.get("exact_target_matches", [])
            and "K2_minus_L3" in scan.get("reverse_target_matches", [])
            and "L3_minus_K2" in scan.get("differences_whose_double_is_target_L2", [])
            else "FAIL",
            str(scan),
        ),
        Gate(
            "validator refuses promotion",
            "OPEN"
            if packet.get("candidate_role") == "UNSELECTED_FIXTURE"
            and packet_result.get("exit_code") == 2
            and packet_report.get("status") == "OPEN"
            and "source.selected_by_mtt is not true" in packet_report.get("open_items", [])
            and "Pic0 character not selected or quotiented"
            in packet_report.get("open_items", [])
            else "FAIL",
            str(packet_result),
        ),
        Gate(
            "closes candidate discovery",
            "PASS"
            if closes.get("hidden_monad_line_difference_scan") is True
            and closes.get("exact_ordered_integral_target_L_candidate_found") is True
            and closes.get("previous_monad_rejection_for_full_L2_cochain_packet_still_valid")
            is True
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
            if still_open.get("prove_L3_minus_K2_is_selected_visible_source_slot") is True
            and still_open.get("select_or_quotient_neutral_Pic0_character") is True
            and still_open.get("derive_same_source_D_E_dotD_Riesz_Green") is True
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
                    "L3 - K2 = (1,-2,0)",
                    "2(L3 - K2) = (2,-4,0)",
                    "stronger than the finite mod-3 qutrit quotient",
                    "not a selected visible V_alpha source",
                    "Selected_Monad_Difference_L2_Source.v1",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa monad L2 branch-orientation candidate audit")
    print("==================================================")
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
