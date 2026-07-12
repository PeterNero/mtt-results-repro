"""Audit the finite D_E action validator for Iwasawa Galerkin slots."""

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
CERT = CERT_DIR / "iwasawa_de_action_validator_certificate.json"
SPECTRAL_GATE = CERT_DIR / "iwasawa_spectral_operator_gate_certificate.json"
GALERKIN_PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
ZERO_MODE = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
SECTOR_VALIDATOR = CERT_DIR / "iwasawa_sector_projection_validator_certificate.json"
GALERKIN_TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
PAPER = ROOT / "Iwasawa_DE_Action_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_de_action.py"


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
        "domain_dimension": 4,
        "range_dimension": 1,
        "domain_gram": matrix(identity(4)),
        "range_gram": matrix(identity(1)),
        "D_E_matrix": matrix([[0, 0, 0, 1]]),
        "stiffness_matrix": matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1],
            ]
        ),
        "ordered_zero_mode_basis": [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ],
        "selected_source_verified": True,
        "boundary_conditions_verified": True,
    }


def higgs_slot() -> dict[str, Any]:
    return {
        "kind": "single_higgs_carrier",
        "expected_kernel_dimension": 1,
        "domain_dimension": 2,
        "range_dimension": 1,
        "domain_gram": matrix(identity(2)),
        "range_gram": matrix(identity(1)),
        "D_E_matrix": matrix([[0, 1]]),
        "stiffness_matrix": matrix(
            [
                [0, 0],
                [0, 1],
            ]
        ),
        "ordered_zero_mode_basis": [[1, 0]],
        "selected_source_verified": True,
        "boundary_conditions_verified": True,
    }


def valid_candidate() -> dict[str, Any]:
    slots = {sector: family_slot() for sector in ("Q", "u", "d", "L", "e", "N")}
    slots["H"] = higgs_slot()
    return {
        "certificate": "TemporaryDEActionCandidate",
        "operator_slots": slots,
    }


def bad_stiffness_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["operator_slots"]["Q"]["stiffness_matrix"] = matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2],
        ]
    )
    return data


def bad_zero_mode_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["operator_slots"]["Q"]["D_E_matrix"] = matrix([[1, 0, 0, 1]])
    data["operator_slots"]["Q"]["stiffness_matrix"] = matrix(
        [
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1],
        ]
    )
    return data


def missing_slot_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["operator_slots"]["H"] = None
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
        path = Path(tmp) / "de_action_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    spectral_gate = load_json(SPECTRAL_GATE)
    protocol = load_json(GALERKIN_PROTOCOL)
    zero_mode = load_json(ZERO_MODE)
    sector_validator = load_json(SECTOR_VALIDATOR)
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
    stiffness_code, stiffness_output = run_temp_candidate(bad_stiffness_candidate())
    zero_code, zero_output = run_temp_candidate(bad_zero_mode_candidate())
    missing_code, missing_output = run_temp_candidate(missing_slot_candidate())

    supported_text = " ".join(str(value) for value in supported.values())
    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_DE_ACTION_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if spectral_gate.get("status")
            == "SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_OPERATOR_AND_BASIS_DATA"
            and protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            and zero_mode.get("status")
            == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            and sector_validator.get("status")
            == "IWASAWA_SECTOR_PROJECTION_VALIDATOR_FORMULATED_DATA_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "spectral gate, Galerkin protocol, zero-mode interface, sector validator, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "computed_stiffness",
                    "stiffness mismatch",
                    "D_E action validation PASS",
                    "zero-mode",
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
                    "D_E_matrix",
                    "K = D_E^* G_range D_E",
                    "D_E psi_i = 0",
                    "selected_source_verified",
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
                    "stiffness_equals_Dstar_Grange_D",
                    "kernel_dimension_matches_expected",
                    "zero_modes_annihilated_by_D_E",
                    "zero_modes_orthonormal_in_domain_gram",
                    "selected_source_and_boundary_flags_required",
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
                    "Riesz_projector_and_complement_gap",
                    "dotD_alpha1",
                    "reduced_Green_operator",
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
            and "missing operator_slots" in exit_codes["2"]
            else "FAIL",
            str(exit_codes),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "MISSING operator_slots object" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "toy operator smoke test",
            "PASS"
            if valid_code == 0
            and "D_E action validation PASS" in valid_output
            and smoke.get("toy_candidate_claim_selected") is False
            else "FAIL",
            valid_output.strip(),
        ),
        Gate(
            "stiffness mismatch fails",
            "PASS"
            if stiffness_code == 1
            and "D_E action validation FAIL" in stiffness_output
            and "Q stiffness mismatch" in stiffness_output
            else "FAIL",
            stiffness_output.strip(),
        ),
        Gate(
            "zero mode residual fails",
            "PASS"
            if zero_code == 1
            and "D_E action validation FAIL" in zero_output
            and "Q zero-mode 0 residual" in zero_output
            else "FAIL",
            zero_output.strip(),
        ),
        Gate(
            "missing slot remains open",
            "PASS"
            if missing_code == 2 and "MISSING operator slot entries: H" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("toy_consistent_operator_slots_pass_schema") is True
            and smoke.get("toy_candidate_claim_selected") is False
            and smoke.get("stiffness_bad_candidate_fails") is True
            and smoke.get("zero_mode_bad_candidate_fails") is True
            and smoke.get("missing_slot_candidate_exit_2") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_D_E_action_validator") is True
            and closes.get("stiffness_assembly_gate") is True
            and closes.get("kernel_dimension_and_zero_mode_basis_gate") is True
            and closes.get("domain_and_range_Gram_consistency_gate") is True
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
                    "proof_D_E_comes_from_selected_MTT_operator_source",
                    "Riesz_projector_gap_error_certificate",
                    "dotD_alpha1_and_Green_operator",
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
            if verdict.get("closes_D_E_action_validator_for_candidate_data") is True
            and verdict.get("closes_actual_selected_D_E") is False
            and "Riesz projector" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Finite `D_E` Action Validator",
                    "K = D_E^* G_range D_E",
                    "toy schema candidate",
                    "Do not treat the toy finite operator as selected data",
                    "Riesz projector",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa finite D_E action validator audit")
    print("=========================================")
    print()
    print(f"template_exit={template_code}")
    print(f"toy_valid_exit={valid_code}")
    print(f"stiffness_bad_exit={stiffness_code}")
    print(f"zero_mode_bad_exit={zero_code}")
    print(f"missing_slot_exit={missing_code}")
    print()

    failed = False
    for gate in gates:
        print(f"{gate.label:<31} {gate.status:<10} {gate.detail}")
        if gate.status == "FAIL":
            failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
