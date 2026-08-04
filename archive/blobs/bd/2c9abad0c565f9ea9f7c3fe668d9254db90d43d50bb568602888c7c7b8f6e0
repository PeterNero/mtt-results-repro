"""Audit the SU(5) block-orientation route split."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_su5_block_orientation_route_split.py"
CANDIDATE = REPO / "candidate_data" / "su5_block_orientation_route_split.candidate.json"
CERT = REPO / "certificates" / "su5_block_orientation_route_split_certificate.json"
PAPER = ROOT / "SU5_Block_Orientation_Route_Split_v1.md"


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


def run_script() -> dict[str, Any]:
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


def all_bool(data: dict[str, Any], expected: bool) -> bool:
    return all(value is expected for value in data.values())


def branch(report: dict[str, Any], name: str) -> dict[str, Any]:
    for item in report.get("branches", []):
        if item.get("branch") == name:
            return item
    return {}


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    calc = report.get("calculation_results", {})
    cert_calc = cert.get("calculation_results", {})
    q79 = branch(report, "current_q79_orientation")
    q369 = branch(report, "conjugate_q369_orientation")

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "SU5BlockOrientationRouteSplit",
                    "SU5_MULTIPLETS",
                    "LEFT_DOUBLETS",
                    "RIGHT_SINGLET_OR_CONJUGATES",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status") == "SU5_BLOCK_ORIENTATION_ROUTE_SPLIT_DETECTED_SOURCE_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "conditional tensor preserved",
            "PASS"
            if calc.get("conditional_su5_tensor_closed") is True
            and calc.get("selected_source_closed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "multiplet route split detected",
            "PASS"
            if calc.get("su5_multiplets_uniform_under_current_branch_packets") is False
            and calc.get("left_right_sector_split_coherent_under_current_branch_packets") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "block transport no mismatch",
            "PASS"
            if calc.get("all_sm_trivial_higgs_pairs_allowed_by_block_orientations") is True
            and calc.get("up_down_transport_mismatch_generated_by_block_orientations") is False
            and calc.get("block_route_by_itself_gives_delta_t_mismatch") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "q79 multiplets nonuniform",
            "PASS"
            if q79.get("multiplet_orientation_uniformity", {}).get("10_M", {}).get(
                "uniform_orientation"
            )
            is False
            and q79.get("multiplet_orientation_uniformity", {}).get("bar5_M", {}).get(
                "uniform_orientation"
            )
            is False
            and q79.get("sm_trivial_higgs_pair_transports", {}).get("up", {}).get(
                "finite_transport_kind"
            )
            == "F"
            and q79.get("sm_trivial_higgs_pair_transports", {}).get("down", {}).get(
                "finite_transport_kind"
            )
            == "F"
            else "FAIL",
            str(q79),
        ),
        Gate(
            "q369 multiplets nonuniform",
            "PASS"
            if q369.get("multiplet_orientation_uniformity", {}).get("10_M", {}).get(
                "uniform_orientation"
            )
            is False
            and q369.get("multiplet_orientation_uniformity", {}).get("bar5_M", {}).get(
                "uniform_orientation"
            )
            is False
            and q369.get("sm_trivial_higgs_pair_transports", {}).get("up", {}).get(
                "finite_transport_kind"
            )
            == "F_conjugate"
            and q369.get("sm_trivial_higgs_pair_transports", {}).get("down", {}).get(
                "finite_transport_kind"
            )
            == "F_conjugate"
            else "FAIL",
            str(q369),
        ),
        Gate(
            "candidate file matches run",
            "PASS"
            if candidate.get("calculation_results") == calc
            and cert_calc == calc
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "closed fields",
            "PASS" if all_bool(cert.get("what_this_closes", {}), True) else "FAIL",
            str(cert.get("what_this_closes")),
        ),
        Gate(
            "still open fields",
            "PASS" if all_bool(cert.get("still_open", {}), True) else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "guardrails",
            "PASS" if all_bool(cert.get("guardrails", {}), False) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "paper records split",
            "PASS"
            if contains_all(
                paper,
                [
                    "The monolithic tensor remains a valid conditional finite calculation",
                    "not sourced by the current block-factorized trivial-Higgs packet",
                    "Route A is the high-scale SU(5)/E6 route",
                    "Route B is the block-factorized SM route",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("SU(5) block orientation route split audit")
    print("=========================================")
    print()
    print(f"su5_multiplets_uniform={calc.get('su5_multiplets_uniform_under_current_branch_packets')}")
    print(f"left_right_coherent={calc.get('left_right_sector_split_coherent_under_current_branch_packets')}")
    print(f"block_delta_t_mismatch={calc.get('block_route_by_itself_gives_delta_t_mismatch')}")
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
