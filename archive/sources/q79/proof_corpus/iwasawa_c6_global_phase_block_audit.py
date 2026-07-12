"""Audit the Iwasawa C6 global phase block."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_c6_global_phase_block_certificate.json"
PAPER = ROOT / "Iwasawa_C6_Global_Phase_Block_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_c6_global_phase_block.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_analysis() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    analysis = run_analysis()
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    implications = cert.get("physical_implications", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    phase_values = analysis.get("phase_values", {})
    branch_blocks = analysis.get("branch_blocks", [])
    global_properties = analysis.get("global_properties", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "IWASAWA_C6_GLOBAL_PHASE_BLOCK_CLOSED_AMPLITUDES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "selected q label",
            "PASS"
            if analysis.get("selected_q_label_from_closed_branch") == 79
            and analysis.get("inverse_label") == 369
            else "FAIL",
            str(
                (
                    analysis.get("selected_q_label_from_closed_branch"),
                    analysis.get("inverse_label"),
                )
            ),
        ),
        Gate(
            "single phase per branch",
            "PASS"
            if len(branch_blocks) == 2
            and all(block.get("is_single_global_phase") is True for block in branch_blocks)
            and [block.get("unique_labels") for block in branch_blocks] == [[79], [369]]
            else "FAIL",
            str(branch_blocks),
        ),
        Gate(
            "phase values",
            "PASS"
            if abs(phase_values.get("79", {}).get("real", 0.0) - 0.4464767119915629)
            < 1e-12
            and abs(phase_values.get("79", {}).get("imag", 0.0) - 0.8947952534793661)
            < 1e-12
            and abs(phase_values.get("369", {}).get("imag", 0.0) + 0.894795253479366)
            < 1e-12
            else "FAIL",
            str(phase_values),
        ),
        Gate(
            "forced certificate consistency",
            "PASS"
            if all(analysis.get("forced_certificate_consistency", {}).values())
            else "FAIL",
            str(analysis.get("forced_certificate_consistency")),
        ),
        Gate(
            "global properties",
            "PASS"
            if global_properties.get("all_surviving_C6_channels_share_one_phase_per_branch")
            is True
            and global_properties.get("global_pair_are_complex_conjugates") is True
            and global_properties.get("unit_modulus") is True
            and global_properties.get("pure_flat_action_S") == 0
            and global_properties.get("exp_minus_S") == 1
            else "FAIL",
            str(global_properties),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("selected_q_label_from_closed_branch") == 79
            and calc.get("inverse_label") == 369
            and calc.get("all_surviving_C6_channels_share_one_phase_per_branch") is True
            and calc.get("global_pair_are_complex_conjugates") is True
            and calc.get("unit_modulus") is True
            and calc.get("pure_flat_action_S") == 0
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "physical implications",
            "PASS" if all(value is True for value in implications.values()) else "FAIL",
            str(implications),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in still_open.values()) else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("C6_global_phase_block_closed") is True
            and verdict.get("C6_phase_knob_overfitting_removed") is True
            and verdict.get("C6_amplitude_and_support_open") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records block",
            "PASS"
            if contains_all(
                paper,
                [
                    "chi_79",
                    "chi_369",
                    "C6 phase alone cannot set mass or mixing magnitudes",
                    "nonzero selected C6 support matrices",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa C6 global phase-block audit")
    print("===================================")
    print()
    print(f"selected_q={analysis.get('selected_q_label_from_closed_branch')}")
    print(f"inverse_label={analysis.get('inverse_label')}")
    print(f"phase_values={phase_values}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
