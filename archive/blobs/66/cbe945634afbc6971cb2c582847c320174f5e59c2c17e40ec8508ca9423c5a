"""Audit the attempt over all remaining terminal V_alpha gates."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "attempt_all_remaining_valpha_gates.py"
CERT = ROOT / "certificates" / "all_remaining_valpha_gates_attempt_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json"
VALPHA_PACKET = (
    ROOT
    / "candidate_data"
    / "all_remaining_valpha_gates"
    / "selected_valpha_chern_weil_operator_source.after_terminal_lockdown.json"
)
FUSION_PACKET = (
    ROOT
    / "candidate_data"
    / "all_remaining_valpha_gates"
    / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json"
)
PAPER = CORPUS / "All_Remaining_VAlpha_Gates_Attempt_v1.md"


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
        cwd=ROOT,
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
    valpha = load(VALPHA_PACKET)
    fusion = load(FUSION_PACKET)
    paper = read(PAPER)

    gate_summary = cert.get("gate_summary", {})
    section = cert.get("unconditional_section_gate", {})
    stability = cert.get("stability_or_routec_gate", {})
    valpha_validator = cert.get("selected_valpha_validator", {})
    fusion_validator = cert.get("same_source_fusion_validator", {})
    primitive = cert.get("primitive_and_sm_gates", {}).get("PrimitiveC1Contractions", {})
    sm = cert.get("primitive_and_sm_gates", {}).get("NoProxyYukawaCKMPMNSAndSMClosure", {})
    retired = cert.get("newly_retired_by_after_lockdown_attempts", {})
    guardrails = cert.get("guardrails", {})

    expected_gates = {
        "UnconditionalTerminalAdmissibleSectionTheorem",
        "SelectedNonSplitVAlphaStabilityOrRouteCResidual",
        "OperatorLayerPic0Recheck",
        "SameSourceChernWeilGSRow",
        "SameSourceDErhoERieszGreenDotD",
        "PrimitiveC1Contractions",
        "NoProxyYukawaCKMPMNSAndSMClosure",
    }

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("valpha packet exists", "PASS" if VALPHA_PACKET.exists() else "FAIL", VALPHA_PACKET),
        Gate("fusion packet exists", "PASS" if FUSION_PACKET.exists() else "FAIL", FUSION_PACKET),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS"
            if cert.get("status")
            == "ALL_REMAINING_VALPHA_GATES_ATTEMPTED_SELECTED_OPERATOR_SOURCE_STILL_REQUIRED"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("gate_summary") == gate_summary
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "all seven gates attempted",
            "PASS" if set(gate_summary) == expected_gates else "FAIL",
            sorted(gate_summary),
        ),
        Gate(
            "section gate not overpromoted",
            "OPEN"
            if section.get("status") == "AXIOM_READY_NOT_UNCONDITIONAL"
            and section.get("closed") is False
            else "FAIL",
            section,
        ),
        Gate(
            "stability partial only",
            "OPEN"
            if stability.get("status") == "PARTIAL_NON_SPLIT_INPUT_CLOSED_STABILITY_OPEN"
            and stability.get("closed_subparts", {}).get("selected_h1_8_nonzero_ext") is True
            and stability.get("closed") is False
            else "FAIL",
            stability,
        ),
        Gate(
            "after-lockdown valpha packet uses selected terminal data",
            "PASS"
            if valpha.get("valpha_extension", {}).get("ordered_source_packet")
            == "candidate_data/terminal_admissible_section_source/visible_rank2_l2_ordered_source.selected_under_section_principle.json"
            and valpha.get("valpha_extension", {}).get("terminal_monad_difference_L3_minus_K2_selector_closed")
            is True
            and valpha.get("valpha_extension", {}).get("nonzero_ext_class_selected") is True
            else "FAIL",
            valpha.get("valpha_extension"),
        ),
        Gate(
            "after-lockdown fusion packet uses selected terminal data",
            "PASS"
            if fusion.get("ordered_source", {}).get("visible_rank2_l2_ordered_source_packet")
            == "candidate_data/terminal_admissible_section_source/visible_rank2_l2_ordered_source.selected_under_section_principle.json"
            and fusion.get("ordered_source", {}).get("ordered_source_validator_passes") is True
            and fusion.get("ordered_source", {}).get("pic0_resolution") == "pic0_quotient_rule"
            else "FAIL",
            fusion.get("ordered_source"),
        ),
        Gate(
            "operator validators still open",
            "OPEN"
            if valpha_validator.get("exit_code") == 2
            and fusion_validator.get("exit_code") == 2
            and valpha_validator.get("status") == "OPEN"
            and fusion_validator.get("status") == "OPEN"
            else "FAIL",
            {
                "valpha": valpha_validator.get("open_item_count"),
                "fusion": fusion_validator.get("open_item_count"),
            },
        ),
        Gate(
            "ordered validators retired",
            "PASS" if retired and all(retired.values()) else "FAIL",
            retired,
        ),
        Gate(
            "primitive C1 still missing 24 matrices",
            "OPEN"
            if primitive.get("calculator_exit_code") == 2
            and primitive.get("missing_primitive_count") == 24
            else "FAIL",
            primitive,
        ),
        Gate(
            "SM closure still blocked",
            "OPEN"
            if sm.get("selected_full_sm_attempt_status")
            == "SELECTED_FULL_SM_DATA_THEOREM_NOT_PROVED_SELECTED_DATA_ABSENT"
            and sm.get("safe_to_claim_theorem") is False
            else "FAIL",
            sm,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records all gates",
            "PASS"
            if contains_all(
                paper,
                [
                    "All Remaining VAlpha Gates",
                    "all seven gates",
                    "h1=8",
                    "24 primitive C1",
                    "same-source D_E/Riesz/Green/dotD",
                    "not full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("All remaining V_alpha gates attempt audit")
    print("==========================================")
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
