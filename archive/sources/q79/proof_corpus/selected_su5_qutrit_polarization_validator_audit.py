"""Audit the selected SU(5) qutrit polarization validator."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_su5_qutrit_polarization_validator_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_su5_qutrit_polarization_data.template.json"
FIXTURE = REPO / "candidate_data" / "selected_su5_qutrit_polarization.unselected_fixture.json"
PAPER = ROOT / "Selected_SU5_Qutrit_Polarization_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_selected_su5_qutrit_polarization.py"


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


def run_validator(path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def parse_report(output: str) -> dict[str, Any]:
    match = re.search(r"polarization_validation_report=(\{.*\})", output)
    if not match:
        return {}
    return json.loads(match.group(1))


def write_temp_packet(data: dict[str, Any]) -> Path:
    handle = tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        suffix=".json",
        delete=False,
    )
    path = Path(handle.name)
    with handle:
        json.dump(data, handle, indent=2)
    return path


def main() -> None:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    fixture = load_json(FIXTURE)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    template_code, template_output = run_validator(TEMPLATE)
    fixture_code, fixture_output = run_validator(FIXTURE)
    fixture_report = parse_report(fixture_output)

    identity_bad = json.loads(json.dumps(fixture))
    identity_bad["sector_basis_data"]["bar5_M"]["basis_matrix_Ubar5"] = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    identity_bad_path = write_temp_packet(identity_bad)
    identity_code, identity_output = run_validator(identity_bad_path)
    identity_bad_path.unlink(missing_ok=True)

    observed_bad = json.loads(json.dumps(fixture))
    observed_bad["source"]["uses_observed_flavor_inputs"] = True
    observed_bad_path = write_temp_packet(observed_bad)
    observed_code, observed_output = run_validator(observed_bad_path)
    observed_bad_path.unlink(missing_ok=True)

    calc = cert.get("calculation_results", {})
    checks = cert.get("validator_checks", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "SELECTED_SU5_QUTRIT_POLARIZATION_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "orientation_mod_rephase_permutation",
                    "validate_qutrit_operators",
                    "promotes_to_selected_heavy_link_input",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "template schema open",
            "PASS"
            if template.get("schema") == "SelectedSU5QutritPolarizationData.v1"
            and template.get("status") == "OPEN"
            and template.get("candidate_role") is None
            else "FAIL",
            str(TEMPLATE),
        ),
        Gate(
            "open template refused",
            "PASS" if template_code == 2 else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "unselected fixture passes",
            "PASS"
            if fixture_code == 0
            and fixture.get("candidate_role") == "UNSELECTED_FIXTURE"
            and fixture_report.get("orientation_mod_rephase_permutation") == "F"
            and fixture_report.get("promotes_to_selected_heavy_link_input") is False
            and fixture_report.get("selected_source_promotes") is False
            else "FAIL",
            fixture_output.strip(),
        ),
        Gate(
            "identity bad candidate fails",
            "PASS"
            if identity_code == 1 and "relative transport is not F" in identity_output
            else "FAIL",
            identity_output.strip(),
        ),
        Gate(
            "observed input bad candidate fails",
            "PASS"
            if observed_code == 1 and "uses_observed_flavor_inputs" in observed_output
            else "FAIL",
            observed_output.strip(),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("open_template_refused_with_exit_2") is True
            and calc.get("unselected_fixture_passes_finite_algebra") is True
            and calc.get("unselected_fixture_promotes_selected_data") is False
            and calc.get("unselected_fixture_orientation") == "F"
            and calc.get("identity_transport_bad_candidate_fails") is True
            and calc.get("observed_input_bad_candidate_fails") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "validator checks",
            "PASS" if all(value is True for value in checks.values()) else "FAIL",
            str(checks),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closes.values()) else "FAIL",
            str(closes),
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
            if verdict.get("validator_ready") is True
            and verdict.get("selected_sector_basis_data_filled") is False
            and verdict.get("can_promote_su5_qutrit_heavy_link_candidate_now") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "scripts/validate_selected_su5_qutrit_polarization.py",
                    "UNSELECTED_FIXTURE",
                    "selected_by_mtt = false",
                    "derive U_10 and U_bar5 from selected zero-mode data",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected SU(5) qutrit polarization validator audit")
    print("===================================================")
    print()
    print(f"template_exit={template_code}")
    print(f"fixture_exit={fixture_code}")
    print(f"fixture_report={fixture_report}")
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
