"""Audit the finite dotD_alpha1 response validator for Iwasawa slots."""

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
CERT = CERT_DIR / "iwasawa_dotd_response_validator_certificate.json"
GREEN_VALIDATOR = CERT_DIR / "iwasawa_reduced_green_validator_certificate.json"
RIESZ_VALIDATOR = CERT_DIR / "iwasawa_riesz_gap_validator_certificate.json"
ZERO_MODE = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
C1_REDUCTION = CERT_DIR / "c1_finite_response_matrix_reduction_certificate.json"
GALERKIN_TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
PAPER = ROOT / "Iwasawa_DotD_Response_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_dotd_response.py"


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
        "dotD_alpha1_matrix": matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 2, 3, 0],
            ]
        ),
        "ordered_zero_mode_basis": [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ],
        "source_vectors": [
            [0, 0, 0, 1],
            [0, 0, 0, 2],
            [0, 0, 0, 3],
        ],
        "horizontal_response_vectors": [
            [0, 0, 0, -1],
            [0, 0, 0, -2],
            [0, 0, 0, -3],
        ],
        "selected_dotD_source_verified": True,
        "alpha1_driver_verified": True,
        "green_operator_verified": True,
        "horizontal_gauge_verified": True,
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
        "dotD_alpha1_matrix": matrix(
            [
                [0, 0],
                [1, 0],
            ]
        ),
        "ordered_zero_mode_basis": [[1, 0]],
        "source_vectors": [[0, 1]],
        "horizontal_response_vectors": [[0, -1]],
        "selected_dotD_source_verified": True,
        "alpha1_driver_verified": True,
        "green_operator_verified": True,
        "horizontal_gauge_verified": True,
    }


def valid_candidate() -> dict[str, Any]:
    slots = {sector: family_slot() for sector in ("Q", "u", "d", "L", "e", "N")}
    slots["H"] = higgs_slot()
    return {
        "certificate": "TemporaryDotDResponseCandidate",
        "dotd_response_slots": slots,
    }


def bad_source_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["dotd_response_slots"]["Q"]["source_vectors"][0] = [0, 0, 0, 2]
    return data


def bad_response_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["dotd_response_slots"]["Q"]["horizontal_response_vectors"][0] = [0, 0, 0, -2]
    return data


def bad_horizontal_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["dotd_response_slots"]["Q"]["horizontal_response_vectors"][0] = [1, 0, 0, -1]
    return data


def missing_slot_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["dotd_response_slots"]["H"] = None
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
        path = Path(tmp) / "dotd_response_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    green_validator = load_json(GREEN_VALIDATOR)
    riesz_validator = load_json(RIESZ_VALIDATOR)
    zero_mode = load_json(ZERO_MODE)
    c1_reduction = load_json(C1_REDUCTION)
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
    source_code, source_output = run_temp_candidate(bad_source_candidate())
    response_code, response_output = run_temp_candidate(bad_response_candidate())
    horizontal_code, horizontal_output = run_temp_candidate(bad_horizontal_candidate())
    missing_code, missing_output = run_temp_candidate(missing_slot_candidate())

    supported_text = " ".join(str(value) for value in supported.values())
    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_DOTD_RESPONSE_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if green_validator.get("status")
            == "IWASAWA_REDUCED_GREEN_VALIDATOR_FORMULATED_DATA_OPEN"
            and riesz_validator.get("status")
            == "IWASAWA_RIESZ_GAP_VALIDATOR_FORMULATED_DATA_OPEN"
            and zero_mode.get("status")
            == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            and c1_reduction.get("status")
            == "FINITE_C1_RESPONSE_REDUCED_TO_PRIMITIVE_CONTRACTIONS_VALUES_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "Green validator, Riesz validator, zero-mode interface, C1 reduction, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "source vector",
                    "response vector",
                    "Q dotD psi",
                    "P dotPsi=0",
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
                    "dotD_alpha1_matrix",
                    "source_i = Q dotD_alpha1 psi_i",
                    "dotPsi_i = - R source_i",
                    "P dotPsi_i = 0",
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
                    "source_vectors_equal_Q_dotD_psi",
                    "response_vectors_equal_minus_R_source",
                    "response_vectors_horizontal",
                    "linearized_zero_mode_equation",
                    "horizontal_inner_products_zero",
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
                    "proof_dotD_alpha1_comes_from_selected_Hessian_solution",
                    "primitive_overlap_contractions",
                    "explicit_C1_vertex_absence_or_value",
                    "basis_connection_terms",
                    "full_SM_closure",
                ],
            )
            else "FAIL",
            str(not_checked),
        ),
        Gate(
            "exit codes",
            "PASS"
            if set(exit_codes) == {"0", "1", "2"}
            and "missing dotd_response_slots" in exit_codes["2"]
            else "FAIL",
            str(exit_codes),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "MISSING dotd_response_slots object" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "toy dotD response smoke test",
            "PASS"
            if valid_code == 0
            and "dotD response validation PASS" in valid_output
            and smoke.get("toy_candidate_claim_selected") is False
            else "FAIL",
            valid_output.strip(),
        ),
        Gate(
            "source defect fails",
            "PASS"
            if source_code == 1
            and "dotD response validation FAIL" in source_output
            and "source vector 0 != Q dotD psi" in source_output
            else "FAIL",
            source_output.strip(),
        ),
        Gate(
            "response defect fails",
            "PASS"
            if response_code == 1
            and "dotD response validation FAIL" in response_output
            and "response vector 0 != -R source" in response_output
            else "FAIL",
            response_output.strip(),
        ),
        Gate(
            "horizontal defect fails",
            "PASS"
            if horizontal_code == 1
            and "dotD response validation FAIL" in horizontal_output
            and "violates P dotPsi=0" in horizontal_output
            else "FAIL",
            horizontal_output.strip(),
        ),
        Gate(
            "missing slot remains open",
            "PASS"
            if missing_code == 2 and "MISSING dotD response slot entries: H" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("toy_consistent_dotd_response_slots_pass_schema") is True
            and smoke.get("toy_candidate_claim_selected") is False
            and smoke.get("source_bad_candidate_fails") is True
            and smoke.get("response_bad_candidate_fails") is True
            and smoke.get("horizontal_bad_candidate_fails") is True
            and smoke.get("missing_slot_candidate_exit_2") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_dotD_response_validator") is True
            and closes.get("source_vector_gate") is True
            and closes.get("horizontal_response_gate") is True
            and closes.get("linearized_zero_mode_response_gate") is True
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
                    "actual_selected_dotD_alpha1_operator",
                    "primitive_C1_overlap_contractions",
                    "Yukawa_overlap_matrices",
                    "full_SM_closure",
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
            if verdict.get("closes_dotD_response_validator_for_candidate_data") is True
            and verdict.get("closes_actual_selected_dotD_response") is False
            and "primitive overlap contractions" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa dotD Alpha1 Response Validator",
                    "s_i = Q dotD_alpha1 psi_i",
                    "dotPsi_i = - R s_i",
                    "A dotPsi_i + s_i = 0",
                    "P dotPsi_i = 0",
                    "does not construct the selected `dotD_alpha1` operator",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa finite dotD alpha1 response validator audit")
    print("===================================================")
    print()
    print(f"template_exit={template_code}")
    print(f"toy_valid_exit={valid_code}")
    print(f"source_bad_exit={source_code}")
    print(f"response_bad_exit={response_code}")
    print(f"horizontal_bad_exit={horizontal_code}")
    print(f"missing_slot_exit={missing_code}")
    print()

    failed = False
    for gate in gates:
        print(f"{gate.label:<34} {gate.status:<10} {gate.detail}")
        if gate.status == "FAIL":
            failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
