"""Audit the finite reduced Green-operator validator for Iwasawa slots."""

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
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_reduced_green_validator_certificate.json"
RIESZ_VALIDATOR = CERT_DIR / "iwasawa_riesz_gap_validator_certificate.json"
DE_VALIDATOR = CERT_DIR / "iwasawa_de_action_validator_certificate.json"
GALERKIN_PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
ZERO_MODE = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
GALERKIN_TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
PAPER = ROOT / "Iwasawa_Reduced_Green_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_reduced_green.py"


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


def matrix(values: list[list[int | float]]) -> dict[str, Any]:
    return {"matrix": values}


def identity(size: int) -> list[list[int]]:
    return [
        [1 if row == col else 0 for col in range(size)]
        for row in range(size)
    ]


def family_slot() -> dict[str, Any]:
    return {
        "kind": "family",
        "expected_kernel_dimension": 3,
        "dimension": 4,
        "gram_matrix": matrix(identity(4)),
        "stiffness_matrix": matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1],
            ]
        ),
        "riesz_projector": matrix(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ]
        ),
        "complement_projector": matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1],
            ]
        ),
        "reduced_green_operator": matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1],
            ]
        ),
        "complement_gap": 1.0,
        "truncation_error_bound": 0.01,
        "green_norm_bound": 1.02,
        "selected_source_verified": True,
        "riesz_gap_verified": True,
        "operator_data_verified": True,
        "boundary_conditions_verified": True,
    }


def higgs_slot() -> dict[str, Any]:
    return {
        "kind": "single_higgs_carrier",
        "expected_kernel_dimension": 1,
        "dimension": 2,
        "gram_matrix": matrix(identity(2)),
        "stiffness_matrix": matrix(
            [
                [0, 0],
                [0, 1],
            ]
        ),
        "riesz_projector": matrix(
            [
                [1, 0],
                [0, 0],
            ]
        ),
        "complement_projector": matrix(
            [
                [0, 0],
                [0, 1],
            ]
        ),
        "reduced_green_operator": matrix(
            [
                [0, 0],
                [0, 1],
            ]
        ),
        "complement_gap": 1.0,
        "truncation_error_bound": 0.01,
        "green_norm_bound": 1.02,
        "selected_source_verified": True,
        "riesz_gap_verified": True,
        "operator_data_verified": True,
        "boundary_conditions_verified": True,
    }


def valid_candidate() -> dict[str, Any]:
    slots = {sector: family_slot() for sector in ("Q", "u", "d", "L", "e", "N")}
    slots["H"] = higgs_slot()
    return {
        "certificate": "TemporaryReducedGreenCandidate",
        "green_slots": slots,
    }


def bad_green_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["green_slots"]["Q"]["reduced_green_operator"] = matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2],
        ]
    )
    return data


def bad_complement_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["green_slots"]["Q"]["complement_projector"] = matrix(identity(4))
    return data


def bad_norm_bound_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["green_slots"]["Q"]["green_norm_bound"] = 0.5
    return data


def missing_slot_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["green_slots"]["H"] = None
    return data


def run_validator(path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def run_temp_candidate(data: dict[str, Any]) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "reduced_green_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    riesz_validator = load_json(RIESZ_VALIDATOR)
    de_validator = load_json(DE_VALIDATOR)
    protocol = load_json(GALERKIN_PROTOCOL)
    zero_mode = load_json(ZERO_MODE)
    template = load_json(GALERKIN_TEMPLATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    supported = cert.get("supported_format_v1", {})
    checks = cert.get("implemented_checks", {})
    not_checked = cert.get("not_checked_by_v1", {})
    exit_codes = cert.get("script_exit_codes", {})
    smoke = cert.get("smoke_tests", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    template_code, template_output = run_validator(GALERKIN_TEMPLATE)
    valid_code, valid_output = run_temp_candidate(valid_candidate())
    green_code, green_output = run_temp_candidate(bad_green_candidate())
    complement_code, complement_output = run_temp_candidate(bad_complement_candidate())
    norm_code, norm_output = run_temp_candidate(bad_norm_bound_candidate())
    missing_code, missing_output = run_temp_candidate(missing_slot_candidate())

    supported_text = " ".join(str(value) for value in supported.values())
    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_REDUCED_GREEN_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if riesz_validator.get("status")
            == "IWASAWA_RIESZ_GAP_VALIDATOR_FORMULATED_DATA_OPEN"
            and de_validator.get("status")
            == "IWASAWA_DE_ACTION_VALIDATOR_FORMULATED_DATA_OPEN"
            and protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            and zero_mode.get("status")
            == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "Riesz validator, D_E validator, Galerkin protocol, zero-mode interface, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "operator = matmul(inverse(gram), stiffness)",
                    "A R != Q",
                    "R A != Q",
                    "green_norm_bound",
                    "return 2",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "supported format",
            "PASS"
            if contains_all(
                supported_text,
                [
                    "Q,u,d,L,e,N,H",
                    "A = G^{-1} K",
                    "Q = I - P",
                    "A R = Q",
                    "green_norm_bound",
                ],
            )
            else "FAIL",
            supported_text,
        ),
        Gate(
            "implemented checks",
            "PASS"
            if all(checks.values())
            and contains_all(
                checks_text,
                [
                    "complement_equals_I_minus_P",
                    "green_annihilates_projector",
                    "A_R_equals_Q",
                    "R_A_equals_Q",
                    "green_norm_bound_consistent_with_gap",
                ],
            )
            else "FAIL",
            str(checks),
        ),
        Gate(
            "v1 limitations recorded",
            "PASS"
            if all(not_checked.values())
            and contains_all(
                not_checked_text,
                [
                    "proof_D_E_is_selected_by_MTT",
                    "sharp_operator_norm_in_G_metric",
                    "dotD_alpha1",
                    "horizontal_zero_mode_response",
                    "Yukawa_overlap_values",
                ],
            )
            else "FAIL",
            str(not_checked),
        ),
        Gate(
            "exit codes",
            "PASS"
            if set(exit_codes) == {"0", "1", "2"}
            and "missing green_slots" in exit_codes["2"]
            else "FAIL",
            str(exit_codes),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "MISSING green_slots object" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "toy Green smoke test",
            "PASS"
            if valid_code == 0
            and "reduced-Green validation PASS" in valid_output
            and smoke.get("toy_candidate_claim_selected") is False
            else "FAIL",
            valid_output.strip(),
        ),
        Gate(
            "Green inverse defect fails",
            "PASS"
            if green_code == 1
            and "reduced-Green validation FAIL" in green_output
            and "A R != Q" in green_output
            and "R A != Q" in green_output
            else "FAIL",
            green_output.strip(),
        ),
        Gate(
            "complement defect fails",
            "PASS"
            if complement_code == 1
            and "reduced-Green validation FAIL" in complement_output
            and "Q P is nonzero" in complement_output
            else "FAIL",
            complement_output.strip(),
        ),
        Gate(
            "norm bound defect fails",
            "PASS"
            if norm_code == 1
            and "reduced-Green validation FAIL" in norm_output
            and "green_norm_bound" in norm_output
            else "FAIL",
            norm_output.strip(),
        ),
        Gate(
            "missing slot remains open",
            "PASS"
            if missing_code == 2 and "MISSING Green slot entries: H" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("toy_consistent_green_slots_pass_schema") is True
            and smoke.get("toy_candidate_claim_selected") is False
            and smoke.get("green_bad_candidate_fails") is True
            and smoke.get("complement_bad_candidate_fails") is True
            and smoke.get("norm_bound_bad_candidate_fails") is True
            and smoke.get("missing_slot_candidate_exit_2") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_reduced_Green_validator") is True
            and closes.get("complement_projector_gate") is True
            and closes.get("inverse_on_complement_gate") is True
            and closes.get("Green_norm_gap_bound_gate") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if all(open_items.values())
            and contains_all(
                open_text,
                [
                    "actual_selected_D_E_action",
                    "actual_selected_reduced_Green_operator",
                    "dotD_alpha1_operator",
                    "horizontal_zero_mode_responses",
                    "Yukawa_overlap_matrices",
                ],
            )
            else "FAIL",
            str(open_items),
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
            if verdict.get("closes_reduced_Green_validator_for_candidate_data") is True
            and verdict.get("closes_actual_selected_reduced_Green_operator") is False
            and "dotD_alpha1" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Reduced Green Operator Validator",
                    "A = G^{-1} K",
                    "A R = Q",
                    "R A = Q",
                    "dotPsi_a,i = -R_a Q_a dotD_a Psi_a,i",
                    "does not construct the selected operator",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa finite reduced Green-operator validator audit")
    print("====================================================")
    print()
    print(f"template_exit={template_code}")
    print(f"toy_valid_exit={valid_code}")
    print(f"green_bad_exit={green_code}")
    print(f"complement_bad_exit={complement_code}")
    print(f"norm_bad_exit={norm_code}")
    print(f"missing_slot_exit={missing_code}")
    print()

    failed = False
    for gate in gates:
        print(f"{gate.label:<33} {gate.status:<10} {gate.detail}")
        if gate.status == "FAIL":
            failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
