"""Audit the selected HYM/Strominger operator-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
VALIDATOR = REPO / "scripts" / "validate_selected_hym_operator_source.py"
ATTEMPT_SCRIPT = REPO / "scripts" / "attempt_selected_hym_operator_source.py"
TEMPLATE = REPO / "certificates" / "selected_hym_operator_source.template.json"
VALIDATOR_CERT = REPO / "certificates" / "selected_hym_operator_source_validator_certificate.json"
ATTEMPT_PACKET = REPO / "certificates" / "selected_hym_operator_source.attempt.json"
PROMOTION_PACKET = REPO / "certificates" / "selected_hym_operator_source_promotion.attempt.json"
ATTEMPT_CANDIDATE = REPO / "candidate_data" / "selected_hym_operator_source_attempt.candidate.json"
ATTEMPT_CERT = REPO / "certificates" / "selected_hym_operator_source_attempt_certificate.json"
PAPER = ROOT / "Selected_HYM_Operator_Source_Gate_v1.md"


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


def run_command(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def run_attempt() -> dict[str, Any]:
    code, output = run_command([sys.executable, str(ATTEMPT_SCRIPT)])
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def main() -> None:
    attempt = run_attempt()
    template_code, template_output = run_command([sys.executable, str(VALIDATOR), str(TEMPLATE)])
    attempt_code, attempt_output = run_command([sys.executable, str(VALIDATOR), str(ATTEMPT_PACKET)])

    validator_text = read(VALIDATOR)
    attempt_text = read(ATTEMPT_SCRIPT)
    paper = read(PAPER)
    validator_cert = load_json(VALIDATOR_CERT)
    attempt_candidate = load_json(ATTEMPT_CANDIDATE)
    attempt_cert = load_json(ATTEMPT_CERT)
    promotion_packet = load_json(PROMOTION_PACKET)

    calc = attempt.get("calculation_results", {})
    validation_report = attempt.get("validation", {}).get("report", {})
    operator_report = validation_report.get("operator_source", {})
    background_report = validation_report.get("background", {})
    closed = attempt.get("what_this_closes", {})
    open_items = attempt.get("still_open", {})
    guardrails = attempt.get("guardrails", {})
    verdict = attempt.get("verdict", {})

    promotion_stdout = operator_report.get("selected_source_promotion_validator", {}).get("stdout", "")

    gates = [
        Gate(
            "validator present",
            "PASS"
            if VALIDATOR.exists()
            and contains_all(
                validator_text,
                [
                    "SelectedHYMOperatorSource.v1",
                    "source.selected_by_mtt must be true",
                    "background.charge_sector_only must be false",
                    "selected-source promotion validator failed",
                    "Route C residual validator failed",
                ],
            )
            else "FAIL",
            str(VALIDATOR),
        ),
        Gate(
            "attempt script present",
            "PASS"
            if ATTEMPT_SCRIPT.exists()
            and contains_all(
                attempt_text,
                [
                    "CURRENT_FUYAU_ROUTE_C_ATTEMPT_BLOCKED_OPERATOR_SOURCE_MISSING",
                    "selected_hym_operator_source_verified",
                    "closed_charge_sector_not_enough_for_operator_source",
                ],
            )
            else "FAIL",
            str(ATTEMPT_SCRIPT),
        ),
        Gate(
            "template refused",
            "PASS" if template_code == 2 and "OPEN" in template_output else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "validator certificate",
            "PASS"
            if validator_cert.get("status")
            == "SELECTED_HYM_OPERATOR_SOURCE_VALIDATOR_FORMULATED_SOURCE_OPEN"
            and validator_cert.get("verdict", {}).get("validator_formulated") is True
            and validator_cert.get("verdict", {}).get("selected_hym_operator_source_verified")
            is False
            else "FAIL",
            str(validator_cert.get("status")),
        ),
        Gate(
            "attempt packet rejected",
            "PASS"
            if attempt_code == 1
            and "background.charge_sector_only must be false" in attempt_output
            and "selected-source promotion validator failed" in attempt_output
            and "operator_source.selected_D_E_constructed must be true" in attempt_output
            else "FAIL",
            attempt_output.strip(),
        ),
        Gate(
            "attempt certificate status",
            "PASS"
            if attempt_cert.get("status")
            == "SELECTED_HYM_OPERATOR_SOURCE_ATTEMPT_BLOCKED_OPERATOR_SOURCE_MISSING"
            and attempt_candidate.get("calculation") == "SelectedHYMOperatorSourceAttempt"
            else "FAIL",
            str((attempt_cert.get("status"), attempt_candidate.get("calculation"))),
        ),
        Gate(
            "promotion packet exists",
            "PASS"
            if promotion_packet.get("schema") == "IwasawaSelectedSourcePromotionPacket.v1"
            and promotion_packet.get("target_level") == "de_response"
            and promotion_packet.get("selected_source_verified") is False
            else "FAIL",
            str(promotion_packet),
        ),
        Gate(
            "charge sector not enough",
            "PASS"
            if calc.get("fuyau_strominger_charge_sector_closed") is True
            and calc.get("strominger_selection_applies") is True
            and background_report.get("charge_sector_only") is True
            and background_report.get("visible_sm_bundle_model_selected") is False
            and background_report.get("matter_operator_source_constructed") is False
            else "FAIL",
            str((calc, background_report)),
        ),
        Gate(
            "route c operator blocked",
            "PASS"
            if calc.get("route_c_honest_mesh_metric_sector_pass") is True
            and calc.get("route_c_honest_operator_pipeline_pass") is False
            and operator_report.get("route_c_residual_validator", {}).get("exit_code") == 1
            and operator_report.get("selected_source_promotion_validator", {}).get("exit_code")
            == 1
            else "FAIL",
            str(operator_report),
        ),
        Gate(
            "promotion failure diagnostic",
            "PASS"
            if "selected_source_verified must be true" in promotion_stdout
            and "D_E action validation FAIL" in promotion_stdout
            and "Riesz/gap validation FAIL" in promotion_stdout
            and "reduced-Green validation FAIL" in promotion_stdout
            and "dotD response validation FAIL" in promotion_stdout
            else "FAIL",
            promotion_stdout,
        ),
        Gate(
            "closed fields",
            "PASS"
            if closed.get("path_A_first_fill_attempt_executed") is True
            and closed.get("closed_charge_sector_not_enough_for_operator_source") is True
            and closed.get("route_c_honest_operator_blocker_confirmed") is True
            and closed.get("hym_operator_source_gate_instantiated") is True
            else "FAIL",
            str(closed),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in open_items.values()) else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("attempted_path_A_fill") is True
            and verdict.get("selected_hym_operator_source_verified") is False
            and verdict.get("current_status")
            == "BLOCKED_SELECTED_VISIBLE_OPERATOR_SOURCE_MISSING"
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "selected HYM/Strominger operator/source packet for D_E",
                    "closed Z7 Fu-Yau/Strominger charge sector",
                    "charge-sector-only",
                    "selected visible SM bundle/operator source",
                    "does not claim selected `D_E`",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected HYM operator-source gate audit")
    print("=======================================")
    print()
    print(f"template_exit={template_code}")
    print(f"attempt_exit={attempt_code}")
    print(f"selected_hym_operator_source={calc.get('selected_hym_operator_source_verified')}")
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
