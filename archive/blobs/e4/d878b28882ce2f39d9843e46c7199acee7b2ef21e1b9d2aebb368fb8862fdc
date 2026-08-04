"""Audit the Iwasawa orientation-to-D_E/dotD bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_orientation_de_dotd_bridge_certificate.json"
PAPER = ROOT / "Iwasawa_Orientation_DE_dotD_Bridge_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_orientation_de_dotd_bridge.py"


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


def branch_by_name(report: dict[str, Any], name: str) -> dict[str, Any]:
    for branch in report.get("branch_packets", []):
        if branch.get("branch") == name:
            return branch
    return {}


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    report = run_script()

    calc = cert.get("calculation_results", {})
    report_calc = report.get("calculation_results", {})
    contract = cert.get("selection_contract", {})
    report_contract = report.get("selection_contract", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    report_verdict = report.get("verdict", {})
    sensitive = report.get("dependent_quantities", {}).get("orientation_sensitive", [])
    insensitive = report.get("dependent_quantities", {}).get(
        "orientation_insensitive_until_selected_operator_breaks_conjugation", []
    )
    q79_branch = branch_by_name(report, "current_q79_orientation")
    q369_branch = branch_by_name(report, "conjugate_q369_orientation")

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "IWASAWA_ORIENTATION_DE_DOTD_BRIDGE_REDUCED_TO_CONJUGATE_PAIR_OPERATOR_OPEN"
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
                    "IwasawaOrientationDEDotDBridge",
                    "build_branch_packets",
                    "selection_contract",
                    "selected_operator_data_absent",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "branch packets",
            "PASS"
            if q79_branch.get("torsion_label_m") == 1
            and q79_branch.get("global_cp_label") == 79
            and q79_branch.get("conditional_su5_transport_orientation") == "F"
            and q369_branch.get("torsion_label_m") == 2
            and q369_branch.get("global_cp_label") == 369
            and q369_branch.get("conditional_su5_transport_orientation") == "F*"
            else "FAIL",
            str(report.get("branch_packets", [])),
        ),
        Gate(
            "orientation sources cohere",
            "PASS"
            if report_calc.get("existing_orientation_sources_cohere") is True
            and report_calc.get("torsion_candidate_labels") == [1, 2]
            and report_calc.get("global_cp_label_pair") == [79, 369]
            and report_calc.get("c6_label_patterns")
            == [[79, 79, 79, 79], [369, 369, 369, 369]]
            else "FAIL",
            str(report_calc),
        ),
        Gate(
            "selected operator absent",
            "PASS"
            if report_calc.get("selected_D_E_constructed") is False
            and report_calc.get("selected_D_E_source_found") is False
            and report_calc.get("selected_dotD_values_closed") is False
            and report_calc.get("selected_operator_data_absent") is True
            else "FAIL",
            str(report_calc),
        ),
        Gate(
            "route C and SU5 roles",
            "PASS"
            if report_calc.get("route_c_scaffold_ready") is True
            and report_calc.get("su5_orientation_is_conditional_fixture") is True
            and report_calc.get("unique_branch_selected_now") is False
            else "FAIL",
            str(report_calc),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc == {
                key: report_calc.get(key)
                for key in calc
            }
            else "FAIL",
            str(calc),
        ),
        Gate(
            "selection contract",
            "PASS"
            if contract.get("must_select_exactly_one_torsion_label_m") == [1, 2]
            and contract.get("must_bind_m_to_global_cp_label") == {
                "m=1": 79,
                "m=2": 369,
            }
            and contract.get("must_verify_dotD_is_same_branch_derivative") is True
            and "validate_iwasawa_dotd_response.py"
            in report_contract.get("must_feed_existing_validators", [])
            else "FAIL",
            str(contract),
        ),
        Gate(
            "dependent quantities",
            "PASS"
            if "CP-odd observables such as Jarlskog sign" in sensitive
            and "Yukawa singular values under exact antiunitary conjugation" in insensitive
            and "CKM angle magnitudes under exact antiunitary conjugation" in insensitive
            else "FAIL",
            str(report.get("dependent_quantities", {})),
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
            if verdict.get("orientation_dependency_sharpened") is True
            and report_verdict.get("current_status")
            == "one nontrivial structure up to global conjugation"
            and report_verdict.get("unique_orientation_selected_now") is False
            and report_verdict.get("not_two_independent_solutions") is True
            else "FAIL",
            str(report_verdict),
        ),
        Gate(
            "paper records bridge",
            "PASS"
            if contains_all_ci(
                paper,
                [
                    "m=1  <->  q=79",
                    "m=2  <->  q=369",
                    "not two unrelated solutions",
                    "dotD_alpha1 cannot choose a sign independently",
                    "selected D_E branch",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa orientation-to-D_E/dotD bridge audit")
    print("============================================")
    print()
    print(f"global_cp_label_pair={report_calc.get('global_cp_label_pair')}")
    print(f"unique_branch_selected_now={report_calc.get('unique_branch_selected_now')}")
    print(f"selected_operator_data_absent={report_calc.get('selected_operator_data_absent')}")
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
