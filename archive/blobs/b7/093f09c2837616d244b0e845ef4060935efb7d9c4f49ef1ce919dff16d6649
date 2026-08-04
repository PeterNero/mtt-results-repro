"""Audit the selected missing-data calculation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "selected_missing_data_calculation_certificate.json"
PAPER = ROOT / "Selected_Missing_Data_Calculation_v1.md"
SCRIPT = REPO / "scripts" / "calculate_missing_selected_data.py"


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


def run_calculator() -> dict[str, Any]:
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
    script_text = read(SCRIPT)
    report = run_calculator()

    computed = cert.get("computed_result", {})
    routes = report.get("selected_D_E_routes", {})
    missing_layers = report.get("missing_validator_layers", {})
    null_counts = report.get("null_counts", {})
    primitive_missing = report.get("missing_primitive_contractions", [])
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status") == "SELECTED_DATA_CALCULATION_BLOCKED_BY_ABSENT_SELECTED_OPERATOR_SOURCE"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "calculator exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "first_blocking_layer",
                    "operator_slots",
                    "selected_c1_primitive_contractions",
                    "minimal_new_selected_data_to_compute_c1",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "first blocker calculated",
            "PASS"
            if report.get("first_blocking_layer") == "selected_operator_source"
            and computed.get("first_blocking_layer") == "selected_operator_source"
            else "FAIL",
            str(report.get("first_blocking_layer")),
        ),
        Gate(
            "selected D_E absent",
            "PASS"
            if report.get("selected_D_E_constructed") is False
            and computed.get("selected_D_E_constructed") is False
            else "FAIL",
            str(report.get("selected_D_E_constructed")),
        ),
        Gate(
            "route statuses",
            "PASS"
            if routes.get("R1_corrected_non_invariant_Dolbeault_operator", {}).get("status") == "BLOCKED"
            and routes.get("R2_typed_monad_sections", {}).get("status") == "BLOCKED"
            and routes.get("R3_direct_selected_HYM_solve", {}).get("status")
            == "ABSTRACT_EXISTENCE_ONLY"
            else "FAIL",
            str(routes),
        ),
        Gate(
            "filled slot data absent",
            "PASS"
            if all(report.get("filled_selected_slot_data_found", {}).get(key) == [] for key in (
                "operator_slots",
                "spectral_slots",
                "green_slots",
                "dotd_response_slots",
            ))
            and all(missing_layers.values())
            else "FAIL",
            str(report.get("filled_selected_slot_data_found", {})),
        ),
        Gate(
            "primitive missing count",
            "PASS"
            if len(primitive_missing) == 24
            and null_counts.get("selected_c1_primitive_contractions") == 24
            and computed.get("missing_primitive_contraction_matrices") == 24
            else "FAIL",
            str(primitive_missing),
        ),
        Gate(
            "full SM still not computable",
            "PASS"
            if report.get("can_compute_now", {}).get("actual_selected_Yukawa_matrices") is False
            and report.get("can_compute_now", {}).get("full_SM_closure") is False
            else "FAIL",
            str(report.get("can_compute_now", {})),
        ),
        Gate(
            "guardrails",
            "PASS"
            if all(value is False for value in guardrails.values())
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("missing_data_calculated") is True
            and verdict.get("selected_numerical_values_calculated") is False
            and "operator_slots" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records calculation",
            "PASS"
            if contains_all(
                paper,
                [
                    "Selected Missing Data Calculation",
                    "selected_operator_source",
                    "No non-validator certificate currently contains filled selected slot data",
                    "4 sectors x 6 terms = 24 selected 3x3 matrices",
                    "a computable selected `D_E`, is absent",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected missing-data calculation audit")
    print("=======================================")
    print()
    print(f"first_blocking_layer={report.get('first_blocking_layer')}")
    print(f"missing_primitive_contractions={len(primitive_missing)}")
    print()

    failed = False
    for gate in gates:
        print(f"{gate.label:<29} {gate.status:<8} {gate.detail}")
        if gate.status == "FAIL":
            failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
