"""Audit the block-factorized sector-map validator."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_block_factorized_sector_maps_certificate.json"
PACKET = REPO / "candidate_data" / "iwasawa_block_factorized_sector_maps.candidate.json"
PAPER = ROOT / "Iwasawa_Block_Factorized_Sector_Maps_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_block_factorized_sector_maps.py"


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


def run_validator() -> tuple[int, str, dict[str, Any]]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(PACKET)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    match = re.search(r"block_factorized_sector_report=(\{.*\})", proc.stdout)
    report = json.loads(match.group(1)) if match else {}
    return proc.returncode, proc.stdout, report


def main() -> None:
    cert = load_json(CERT)
    packet = load_json(PACKET)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    code, output, report = run_validator()

    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    family = report.get("family_block", {})
    higgs = report.get("higgs_line_block", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "IWASAWA_BLOCK_FACTORIZED_SECTOR_MAPS_VALIDATED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["validate_family_block", "validate_higgs_line"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "packet shape",
            "PASS"
            if packet.get("schema") == "IwasawaBlockFactorizedSectorMaps.v1"
            and packet.get("selected_by_mtt") is False
            else "FAIL",
            str(PACKET),
        ),
        Gate(
            "validator passes",
            "PASS"
            if code == 0
            and report.get("finite_block_factorized_sector_maps_valid") is True
            and family.get("projective_validator_exit") == 0
            and family.get("metric_validator_exit") == 0
            and higgs.get("transition_scalars_trivial") is True
            else "FAIL",
            output.strip(),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("validator_exit_code") == 0
            and calc.get("projective_family_rhoE_mesh_passes") is True
            and calc.get("family_metric_passes") is True
            and calc.get("family_sector_projectors_full_rank_three") is True
            and calc.get("higgs_line_rank_one_projector") is True
            and calc.get("finite_block_factorized_sector_maps_valid") is True
            and calc.get("selected_source_ready") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
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
            if verdict.get("finite_block_factorized_sector_maps_validated") is True
            and verdict.get("selected_source_promoted") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "Q,u,d,L,e,N occupy the full rank-three projective family block",
                    "H occupies a separate ordinary rank-one line",
                    "passes the validator",
                    "selected gerbe/source representative remains",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa block-factorized sector maps audit")
    print("==========================================")
    print()
    print(f"validator_report={report}")
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
