"""Audit the branch-aware Route C small-N smoke attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_route_c_branch_smoke_attempt_certificate.json"
PAPER = ROOT / "Iwasawa_Route_C_Branch_Smoke_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_iwasawa_route_c_branch_smoke.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all_ci(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


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


def branch(report: dict[str, Any], name: str) -> dict[str, Any]:
    return report.get("branches", {}).get(name, {})


def validator_exits(report: dict[str, Any], name: str, mode: str) -> dict[str, int]:
    validators = branch(report, name).get("validators", {}).get(mode, {})
    return {key: int(value.get("exit_code")) for key, value in validators.items()}


def all_lifted_pass(report: dict[str, Any], name: str) -> bool:
    validators = branch(report, name).get("validators", {}).get(
        "lifted_selected_flags_smoke", {}
    )
    return all(value.get("pass") is True for value in validators.values())


def all_paths_exist(paths: dict[str, Any]) -> bool:
    for branch_paths in paths.values():
        if not isinstance(branch_paths, dict):
            return False
        for path in branch_paths.values():
            if not (REPO / path).exists():
                return False
    return True


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    report = run_script()

    calc = report.get("calculation_results", {})
    cert_calc = cert.get("calculation_results", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    paths = cert.get("written_paths", {})
    branch_names = ["current_q79_orientation", "conjugate_q369_orientation"]
    expected_honest = {
        "route_c_residual": 1,
        "rhoE_mesh": 0,
        "rhoE_metric": 0,
        "sector_maps": 0,
        "de_action": 1,
        "riesz_gap": 1,
        "reduced_green": 1,
        "dotd_response": 1,
    }

    q79_packet = branch(report, "current_q79_orientation").get("branch_packet", {})
    q369_packet = branch(report, "conjugate_q369_orientation").get("branch_packet", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "BRANCH_AWARE_SMALL_N_SMOKE_ALGEBRA_PASSES_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all_ci(
                script_text,
                [
                    "IwasawaRouteCBranchSmokeAttempt",
                    "lift_selected_flags",
                    "nonzero_dotd_response_inserted",
                    "selected_origin_still_missing",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "branch packets",
            "PASS"
            if q79_packet.get("torsion_label_m") == 1
            and q79_packet.get("global_cp_label") == 79
            and q79_packet.get("conditional_su5_transport_orientation") == "F"
            and q369_packet.get("torsion_label_m") == 2
            and q369_packet.get("global_cp_label") == 369
            and q369_packet.get("conditional_su5_transport_orientation") == "F*"
            else "FAIL",
            str([q79_packet, q369_packet]),
        ),
        Gate(
            "honest validator exits",
            "PASS"
            if all(
                validator_exits(report, name, "honest_unselected") == expected_honest
                for name in branch_names
            )
            else "FAIL",
            str({name: validator_exits(report, name, "honest_unselected") for name in branch_names}),
        ),
        Gate(
            "lifted algebra passes",
            "PASS"
            if all(all_lifted_pass(report, name) for name in branch_names)
            else "FAIL",
            str({name: all_lifted_pass(report, name) for name in branch_names}),
        ),
        Gate(
            "calculation results",
            "PASS"
            if calc.get("branches_tested") == [
                "conjugate_q369_orientation",
                "current_q79_orientation",
            ]
            and calc.get("both_conjugate_branches_have_same_algebraic_status") is True
            and calc.get("nonzero_dotd_response_inserted") is True
            and calc.get("selected_origin_still_missing") is True
            and cert_calc.get("selected_origin_still_missing") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "written paths",
            "PASS" if all_paths_exist(paths) else "FAIL",
            str(paths),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("small_N_branch_pipeline_executed") is True
            and verdict.get("algebraic_validator_pipeline_can_be_satisfied") is True
            and verdict.get("selected_source_obligation_remains") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all_ci(
                paper,
                [
                    "Both conjugate packets were built",
                    "all Route C, rho_E, metric, sector, D_E, Riesz, Green, and dotD validators PASS",
                    "It does not prove",
                    "selected_source_verified",
                    "genuine finite HYM/Strominger residual solve",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa Route C branch smoke attempt audit")
    print("==========================================")
    print()
    print(f"branches={calc.get('branches_tested')}")
    print(f"lifted_passes={calc.get('lifted_selected_flags_all_validators_pass')}")
    print(f"selected_origin_still_missing={calc.get('selected_origin_still_missing')}")
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
