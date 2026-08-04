"""Audit the terminal V_alpha remaining-parts lockdown certificate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "lock_terminal_valpha_remaining_parts.py"
CERT = ROOT / "certificates" / "terminal_valpha_remaining_parts_lockdown_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "terminal_valpha_remaining_parts_lockdown.candidate.json"
PAPER = CORPUS / "Terminal_VAlpha_Remaining_Parts_Lockdown_v1.md"


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
    paper = read(PAPER)

    selected = cert.get("selected_terminal_data", {})
    closed = cert.get("closed_parts", {})
    retired = cert.get("retired_as_nonblockers", {})
    reclass = cert.get("current_operator_attempt_reclassification", {})
    remaining = cert.get("still_open", {})
    gates_list = cert.get("remaining_proof_gates", [])
    validators = cert.get("validator_results", {})
    guardrails = cert.get("guardrails", {})

    gate_names = {entry.get("gate") for entry in gates_list}
    expected_gate_names = {
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
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status locked",
            "PASS"
            if cert.get("status")
            == "TERMINAL_VALPHA_REMAINING_PARTS_LOCKED_TO_STABILITY_AND_OPERATOR_SOURCE_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("closed_parts") == closed
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "selected terminal data",
            "PASS"
            if selected.get("source_label") == "g3 / L3-K2"
            and selected.get("L") == [1, -2, 0]
            and selected.get("L2") == [2, -4, 0]
            and selected.get("c2_valpha") == [4, 0, 0]
            and selected.get("h1") == 8
            else "FAIL",
            selected,
        ),
        Gate(
            "selected validators pass",
            "PASS"
            if validators.get("selected_ordered_source", {}).get("exit_code") == 0
            and validators.get("selected_h1_ext", {}).get("exit_code") == 0
            and validators.get("current_operator_attempt", {}).get("exit_code") == 2
            else "FAIL",
            validators,
        ),
        Gate(
            "closed parts all true",
            "PASS" if closed and all(closed.values()) else "FAIL",
            closed,
        ),
        Gate(
            "nonblockers retired",
            "PASS"
            if retired.get("old_L_sign_search") is True
            and retired.get("old_h1_or_nonzero_ext_search") is True
            and retired.get("split_abelian_hym_source") is True
            and retired.get("validator_plumbing_as_independent_blocker") is True
            and retired.get("benchmark_or_observed_flavor_fitting") is True
            else "FAIL",
            retired,
        ),
        Gate(
            "current attempt reclassified",
            "PASS"
            if len(reclass.get("retired_open_items", {})) >= 5
            and any("non_split_stability_or_hym_proved" in item for item in reclass.get("still_open_items", []))
            and any("chern_weil_row_derived_from_same_source" in item for item in reclass.get("still_open_items", []))
            else "FAIL",
            reclass,
        ),
        Gate(
            "remaining gates exact",
            "OPEN"
            if gate_names == expected_gate_names
            and all(entry.get("status") == "OPEN" for entry in gates_list)
            else "FAIL",
            sorted(gate_names),
        ),
        Gate(
            "still open is honest",
            "OPEN"
            if remaining.get("non_split_extension_stability_or_HYM") is True
            and remaining.get("same_source_D_E_Riesz_Green_dotD") is True
            and remaining.get("primitive_C1_contractions") is True
            and remaining.get("full_SM_closure") is True
            else "FAIL",
            remaining,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records lockdown",
            "PASS"
            if contains_all(
                paper,
                [
                    "Lockdown",
                    "h1=8",
                    "nonzero Ext",
                    "stability/HYM",
                    "same-source D_E/Riesz/Green/dotD",
                    "not full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Terminal V_alpha remaining-parts lockdown audit")
    print("================================================")
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
