"""Audit the finite Riesz projector and gap validator for Iwasawa slots."""

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
CERT = CERT_DIR / "iwasawa_riesz_gap_validator_certificate.json"
SPECTRAL_GATE = CERT_DIR / "iwasawa_spectral_operator_gate_certificate.json"
GALERKIN_PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
DE_VALIDATOR = CERT_DIR / "iwasawa_de_action_validator_certificate.json"
ZERO_MODE = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
GALERKIN_TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
PAPER = ROOT / "Iwasawa_Riesz_Gap_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_riesz_gap.py"


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
        "low_eigenvalues": [0, 0, 0],
        "cluster_eigenvectors": [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ],
        "residual_norms": [0, 0, 0],
        "riesz_projector": matrix(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ]
        ),
        "contour_radius": 0.25,
        "complement_gap": 1.0,
        "truncation_error_bound": 0.01,
        "selected_source_verified": True,
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
        "low_eigenvalues": [0],
        "cluster_eigenvectors": [[1, 0]],
        "residual_norms": [0],
        "riesz_projector": matrix(
            [
                [1, 0],
                [0, 0],
            ]
        ),
        "contour_radius": 0.25,
        "complement_gap": 1.0,
        "truncation_error_bound": 0.01,
        "selected_source_verified": True,
        "operator_data_verified": True,
        "boundary_conditions_verified": True,
    }


def valid_candidate() -> dict[str, Any]:
    slots = {sector: family_slot() for sector in ("Q", "u", "d", "L", "e", "N")}
    slots["H"] = higgs_slot()
    return {
        "certificate": "TemporaryRieszGapCandidate",
        "spectral_slots": slots,
    }


def bad_projector_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["spectral_slots"]["Q"]["riesz_projector"] = matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0.5, 0],
            [0, 0, 0, 0],
        ]
    )
    return data


def bad_gap_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["spectral_slots"]["Q"]["complement_gap"] = 0.2
    return data


def bad_eigenpair_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["spectral_slots"]["Q"]["stiffness_matrix"] = matrix(
        [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
        ]
    )
    return data


def missing_slot_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["spectral_slots"]["H"] = None
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
        path = Path(tmp) / "riesz_gap_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    spectral_gate = load_json(SPECTRAL_GATE)
    protocol = load_json(GALERKIN_PROTOCOL)
    de_validator = load_json(DE_VALIDATOR)
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
    projector_code, projector_output = run_temp_candidate(bad_projector_candidate())
    gap_code, gap_output = run_temp_candidate(bad_gap_candidate())
    eigen_code, eigen_output = run_temp_candidate(bad_eigenpair_candidate())
    missing_code, missing_output = run_temp_candidate(missing_slot_candidate())

    supported_text = " ".join(str(value) for value in supported.values())
    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_RIESZ_GAP_VALIDATOR_FORMULATED_DATA_OPEN"
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
            and de_validator.get("status")
            == "IWASAWA_DE_ACTION_VALIDATOR_FORMULATED_DATA_OPEN"
            and zero_mode.get("status")
            == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "spectral gate, Galerkin protocol, D_E validator, zero-mode interface, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "epsilon_low + truncation_error",
                    "Gram-self-adjoint",
                    "expected_projector",
                    "Riesz/gap validation PASS",
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
                    "low_eigenvalues",
                    "K v_i = lambda_i G v_i",
                    "P^2=P",
                    "epsilon_low + eta_total < tau < gamma_gap - eta_total",
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
                    "generalized_eigenpair_residuals_within_reported_bounds",
                    "projector_Gram_self_adjoint",
                    "projector_matches_G_orthogonal_span",
                    "robust_contour_gap_inequality",
                    "missing_slot_remains_open",
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
                    "independent_computation_of_eigenpairs",
                    "sharp_truncation_error_from_basis_limit",
                    "dotD_alpha1",
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
            and "missing spectral_slots" in exit_codes["2"]
            else "FAIL",
            str(exit_codes),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "MISSING spectral_slots object" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "toy spectral smoke test",
            "PASS"
            if valid_code == 0
            and "Riesz/gap validation PASS" in valid_output
            and smoke.get("toy_candidate_claim_selected") is False
            else "FAIL",
            valid_output.strip(),
        ),
        Gate(
            "projector defect fails",
            "PASS"
            if projector_code == 1
            and "Riesz/gap validation FAIL" in projector_output
            and "Q Riesz projector is not idempotent" in projector_output
            else "FAIL",
            projector_output.strip(),
        ),
        Gate(
            "gap defect fails",
            "PASS"
            if gap_code == 1
            and "Riesz/gap validation FAIL" in gap_output
            and "Q contour is not below complement gap" in gap_output
            else "FAIL",
            gap_output.strip(),
        ),
        Gate(
            "eigen residual defect fails",
            "PASS"
            if eigen_code == 1
            and "Riesz/gap validation FAIL" in eigen_output
            and "Q eigenpair 0 residual" in eigen_output
            else "FAIL",
            eigen_output.strip(),
        ),
        Gate(
            "missing slot remains open",
            "PASS"
            if missing_code == 2 and "MISSING spectral slot entries: H" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("toy_consistent_spectral_slots_pass_schema") is True
            and smoke.get("toy_candidate_claim_selected") is False
            and smoke.get("projector_bad_candidate_fails") is True
            and smoke.get("gap_bad_candidate_fails") is True
            and smoke.get("eigenpair_bad_candidate_fails") is True
            and smoke.get("missing_slot_candidate_exit_2") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_Riesz_projector_validator") is True
            and closes.get("low_cluster_eigenpair_gate") is True
            and closes.get("Gram_orthogonal_projector_gate") is True
            and closes.get("gap_error_pass_rule") is True
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
                    "actual_selected_spectral_slot_data",
                    "actual_complement_gap_from_selected_operator",
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
            if verdict.get("closes_Riesz_gap_validator_for_candidate_data") is True
            and verdict.get("closes_actual_selected_Riesz_projector") is False
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
                    "Iwasawa Riesz Projector And Gap Validator",
                    "K v_i = lambda_i G v_i",
                    "P = V V^* G",
                    "epsilon_low + eta < tau < gamma - eta",
                    "does not construct the selected operator",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa finite Riesz projector and gap validator audit")
    print("=====================================================")
    print()
    print(f"template_exit={template_code}")
    print(f"toy_valid_exit={valid_code}")
    print(f"projector_bad_exit={projector_code}")
    print(f"gap_bad_exit={gap_code}")
    print(f"eigenpair_bad_exit={eigen_code}")
    print(f"missing_slot_exit={missing_code}")
    print()

    failed = False
    for gate in gates:
        print(f"{gate.label:<32} {gate.status:<10} {gate.detail}")
        if gate.status == "FAIL":
            failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
