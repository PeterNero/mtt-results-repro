"""Audit the CKM heavy-link gate calculator and packet schema."""

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
CERT = REPO / "certificates" / "ckm_heavy_link_gate_calculator_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_ckm_heavy_link_packet.template.json"
PAPER = ROOT / "CKM_Heavy_Link_Gate_Calculator_v1.md"
SCRIPT = REPO / "scripts" / "compute_ckm_heavy_link_gate.py"


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
    data["inputs"]["character_trivial_heavy_link"]["u"]["entries"] = [0, 0]
    data["inputs"]["character_trivial_heavy_link"]["d"]["entries"] = [0, 0]
    data["inputs"]["c6_heavy_link"]["u"]["entries"] = [0, 0]
    data["inputs"]["c6_heavy_link"]["d"]["entries"] = [1, 0]
    return data


def run_sample() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sample_heavy_link_packet.json"
        path.write_text(json.dumps(sample_packet(), indent=2), encoding="utf-8")
        proc = run_calculator(path)
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def count_null_entries(template: dict[str, Any]) -> int:
    inputs = template.get("inputs", {})
    count = 0
    for block_name in ("character_trivial_heavy_link", "c6_heavy_link"):
        block = inputs.get(block_name, {})
        for sector in ("u", "d"):
            count += sum(entry is None for entry in block.get(sector, {}).get("entries", []))
    return count


def main() -> None:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    paper = read(PAPER)
    template_run = run_calculator(TEMPLATE)
    sample = run_sample()

    required = cert.get("required_packet_entries", [])
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    sample_gate = sample.get("gate", {})
    sample_derived = sample.get("derived", {})
    sample_phase = sample.get("phase", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "CKM_HEAVY_LINK_GATE_CALCULATOR_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "template open",
            "PASS"
            if template.get("status") == "OPEN"
            and count_null_entries(template) == 8
            else "FAIL",
            f"status={template.get('status')}, nulls={count_null_entries(template)}",
        ),
        Gate(
            "required entries",
            "PASS"
            if required
            == [
                "t_u13",
                "t_u23",
                "t_d13",
                "t_d23",
                "c_u13",
                "c_u23",
                "c_d13",
                "c_d23",
            ]
            else "FAIL",
            str(required),
        ),
        Gate(
            "template refusal",
            "PASS"
            if template_run.returncode != 0
            and "missing selected heavy-link data" in template_run.stdout
            and template_run.stdout.count("- inputs.") == 8
            else "FAIL",
            template_run.stdout,
        ),
        Gate(
            "sample fixture computes",
            "PASS"
            if sample_gate.get("c6_affects_leading_gate") is True
            and sample_gate.get("leading_noncommutation_pass") is True
            and sample_phase.get("selected_label") == 79
            else "FAIL",
            json.dumps(sample, sort_keys=True),
        ),
        Gate(
            "sample delta value",
            "PASS"
            if abs(sample_derived.get("Delta_v", [[0, 0]])[0][0] - 0.4464767119915629)
            < 1e-12
            and abs(sample_derived.get("Delta_v", [[0, 0]])[0][1] - 0.8947952534793661)
            < 1e-12
            and sample_derived.get("Delta_v", [None, None])[1] == 0.0
            else "FAIL",
            str(sample_derived.get("Delta_v")),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("template_refuses_incomplete_data") is True
            and calc.get("missing_template_entries") == 8
            and calc.get("formula") == "Delta_v = Delta_t + chi_q Delta_c"
            and calc.get("calculator_fixture_passes") is True
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
            if verdict.get("calculator_ready") is True
            and verdict.get("selected_packet_values_open") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records calculator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Delta_v = Delta_t + chi_q Delta_c",
                    "all eight entries are still `null`",
                    "Execution II benchmark entries",
                    "heavy-link packet schema",
                    "selected Delta_v value",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("CKM heavy-link gate calculator audit")
    print("====================================")
    print()
    print(f"template_returncode={template_run.returncode}")
    print(f"template_missing_entries={template_run.stdout.count('- inputs.')}")
    print(f"sample_Delta_v={sample_derived.get('Delta_v')}")
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
