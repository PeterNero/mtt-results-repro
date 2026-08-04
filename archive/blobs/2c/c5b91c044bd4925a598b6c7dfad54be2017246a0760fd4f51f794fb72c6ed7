"""Audit the reduced C1 heavy-link Delta_t calculator."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "c1_heavy_link_delta_t_reduction_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_c1_heavy_link_primitives.template.json"
PAPER = ROOT / "C1_Heavy_Link_DeltaT_Reduction_v1.md"
SCRIPT = REPO / "scripts" / "compute_c1_heavy_link_delta_t.py"
TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)


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


def count_null_entries(template: dict[str, Any]) -> int:
    count = 0
    for sector in ("u", "d"):
        for term in TERMS:
            count += sum(entry is None for entry in template["sectors"][sector][term])
    return count


def run_calculator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def sample_packet() -> dict[str, Any]:
    data = load_json(TEMPLATE)
    data["status"] = "NONSELECTED_AUDIT_FIXTURE"
    for term in TERMS:
        data["sectors"]["u"][term] = [0, 0]
        data["sectors"]["d"][term] = [0, 0]
    data["sectors"]["d"]["explicit_vertex"] = [3, 5]
    return data


def run_sample() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sample_c1_heavy_link.json"
        path.write_text(json.dumps(sample_packet(), indent=2), encoding="utf-8")
        proc = run_calculator(path)
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    template_run = run_calculator(TEMPLATE)
    sample = run_sample()

    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "C1_HEAVY_LINK_DELTA_T_REDUCED_TO_24_SCALARS_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["Delta_t", "missing selected C1 heavy-link data"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "template open",
            "PASS"
            if template.get("status") == "OPEN" and count_null_entries(template) == 24
            else "FAIL",
            f"status={template.get('status')}, nulls={count_null_entries(template)}",
        ),
        Gate(
            "template refusal",
            "PASS"
            if template_run.returncode == 2
            and "missing selected C1 heavy-link data" in template_run.stdout
            and template_run.stdout.count("- sectors.") == 24
            else "FAIL",
            template_run.stdout,
        ),
        Gate(
            "sample fixture computes",
            "PASS"
            if sample.get("Delta_t") == [3.0, 5.0]
            and sample.get("t_u") == [0.0, 0.0]
            and sample.get("t_d") == [3.0, 5.0]
            and sample.get("character_trivial_leading_noncommutation_pass") is True
            else "FAIL",
            json.dumps(sample, sort_keys=True),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("template_refuses_incomplete_data") is True
            and calc.get("missing_template_entries") == 24
            and calc.get("full_primitive_matrix_entries_avoided_for_this_gate") == 192
            and calc.get("fixture_calculator_passes") is True
            and calc.get("fixture_is_not_selected_data") is True
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
            if verdict.get("reduction_closed") is True
            and verdict.get("selected_values_open") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records reduction",
            "PASS"
            if contains_all(
                paper,
                [
                    "Delta_c = (0,0)",
                    "2 sectors x 6 primitive terms x 2 heavy-link entries = 24 scalars",
                    "scripts/compute_c1_heavy_link_delta_t.py",
                    "full 3x3 primitive matrices are not required",
                    "smallest selected-data packet",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("C1 heavy-link Delta_t reduction audit")
    print("=====================================")
    print()
    print(f"template_returncode={template_run.returncode}")
    print(f"template_missing_entries={template_run.stdout.count('- sectors.')}")
    print(f"sample_Delta_t={sample.get('Delta_t')}")
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
