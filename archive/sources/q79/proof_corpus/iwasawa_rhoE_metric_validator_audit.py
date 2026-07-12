"""Audit the Hermitian metric validator for Iwasawa rho_E data."""

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
CERT = CERT_DIR / "iwasawa_rhoE_metric_validator_certificate.json"
BUNDLE_CONTRACT = CERT_DIR / "iwasawa_bundle_fe_gluing_contract_certificate.json"
MESH_VALIDATOR = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
CONSTANT_VALIDATOR = CERT_DIR / "iwasawa_rhoE_validator_certificate.json"
RHO_TEMPLATE = CERT_DIR / "iwasawa_bundle_rhoE_data.template.json"
PAPER = ROOT / "Iwasawa_RhoE_Metric_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_rhoE_metric.py"


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


def identity_matrix() -> list[list[int]]:
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]


def identity_metric_candidate() -> dict[str, Any]:
    ident = identity_matrix()
    return {
        "certificate": "TemporaryRhoEMetricCandidate",
        "rank": 3,
        "mesh_N": 2,
        "section_convention": "s(gamma*z)=rho_E(gamma,z)s(z)",
        "generator_data": {f"g{i}": matrix(ident) for i in range(1, 7)},
        "metric_data": matrix(ident),
    }


def scaled_nonunitary_candidate() -> dict[str, Any]:
    data = identity_metric_candidate()
    data["generator_data"]["g1"] = matrix(
        [
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
    return data


def missing_metric_candidate() -> dict[str, Any]:
    data = identity_metric_candidate()
    del data["metric_data"]
    return data


def non_hermitian_metric_candidate() -> dict[str, Any]:
    data = identity_metric_candidate()
    data["metric_data"] = matrix(
        [
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
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
        path = Path(tmp) / "rhoE_metric_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    bundle_contract = load_json(BUNDLE_CONTRACT)
    mesh_validator = load_json(MESH_VALIDATOR)
    constant_validator = load_json(CONSTANT_VALIDATOR)
    template = load_json(RHO_TEMPLATE)
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

    template_code, template_output = run_validator(RHO_TEMPLATE)
    identity_code, identity_output = run_temp_candidate(identity_metric_candidate())
    scaled_code, scaled_output = run_temp_candidate(scaled_nonunitary_candidate())
    missing_code, missing_output = run_temp_candidate(missing_metric_candidate())
    nonhermitian_code, nonhermitian_output = run_temp_candidate(
        non_hermitian_metric_candidate()
    )

    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    supported_ok = (
        "rank must be 3" in str(supported.get("rank", ""))
        and "positive integer" in str(supported.get("mesh_N", ""))
        and "g1..g6" in str(supported.get("generator_data", ""))
        and "Hermitian metric matrix" in str(supported.get("metric_data", ""))
        and "rho_E(gamma,z)^*" in str(supported.get("compatibility_equation", ""))
    )

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_RHOE_METRIC_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if bundle_contract.get("status")
            == "IWASAWA_BUNDLE_FE_GLUING_CONTRACT_FORMULATED_RHOE_DATA_OPEN"
            and mesh_validator.get("status")
            == "IWASAWA_RHOE_MESH_VALIDATOR_FORMULATED_DATA_OPEN"
            and constant_validator.get("status")
            == "IWASAWA_RHOE_VALIDATOR_FORMULATED_DATA_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "bundle FE contract, mesh validator, constant validator, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "validate_metric_compatibility",
                    "is_positive_definite_hermitian",
                    "rho_E metric validation PASS",
                    "return 2",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "supported format",
            "PASS" if supported_ok else "FAIL",
            str(supported),
        ),
        Gate(
            "implemented checks",
            "PASS"
            if all(checks.values())
            and contains_all(
                checks_text,
                [
                    "metric_data_present",
                    "metric_hermitian_on_visited_nodes",
                    "metric_positive_definite_on_visited_nodes",
                    "boundary_face_metric_compatibility",
                    "scaled_nonunitary_transition_fails",
                    "missing_metric_remains_open",
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
                    "proof_metric_is_selected_HYM_metric",
                    "metric_compatibility_away_from_sample_mesh",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "selected_D_E_action",
                    "quadrature_volume_form",
                ],
            )
            else "FAIL",
            str(not_checked),
        ),
        Gate(
            "exit codes",
            "PASS"
            if set(exit_codes) == {"0", "1", "2"}
            and "missing metric_data" in exit_codes["2"]
            else "FAIL",
            str(exit_codes),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "MISSING generator entries" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "identity metric smoke test",
            "PASS"
            if identity_code == 0
            and "rho_E metric validation PASS" in identity_output
            and smoke.get("identity_metric_candidate_claim_selected") is False
            else "FAIL",
            identity_output.strip(),
        ),
        Gate(
            "scaled transition fails",
            "PASS"
            if scaled_code == 1
            and "rho_E metric validation FAIL" in scaled_output
            and "metric compatibility failed" in scaled_output
            else "FAIL",
            scaled_output.strip(),
        ),
        Gate(
            "missing metric remains open",
            "PASS"
            if missing_code == 2 and "MISSING metric_data object" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "non-Hermitian metric fails",
            "PASS"
            if nonhermitian_code == 1
            and "metric at" in nonhermitian_output
            and "not Hermitian" in nonhermitian_output
            else "FAIL",
            nonhermitian_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("identity_rho_identity_metric_mesh_N2_passes_schema") is True
            and smoke.get("identity_metric_candidate_claim_selected") is False
            and smoke.get("scaled_nonunitary_transition_fails") is True
            and smoke.get("missing_metric_candidate_exit_2") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_mesh_metric_compatibility_validator") is True
            and closes.get("positive_definite_hermitian_metric_gate") is True
            and closes.get("unitary_transition_gate_for_supplied_metric") is True
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
                    "actual_selected_rho_E_values_or_functions",
                    "actual_selected_Hermitian_metric",
                    "proof_metric_solves_HYM_or_selected_Strominger_system",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "selected_D_E_action_on_validated_basis",
                    "Gram_and_stiffness_matrices",
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
            if verdict.get("closes_metric_validator_for_rhoE_candidates") is True
            and verdict.get("closes_actual_selected_metric") is False
            and verdict.get("closes_actual_selected_rhoE") is False
            and "sector projection maps" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Hermitian metric compatibility",
                    "rho_E(gamma,target)^* H(source) rho_E(gamma,target) = H(target)",
                    "actual selected Hermitian/HYM metric",
                    "Do not identify the identity metric with the selected HYM metric",
                    "sector projection maps",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa rho_E Hermitian metric validator audit")
    print("==============================================")
    print()
    print(f"template_exit={template_code}")
    print(f"identity_exit={identity_code}")
    print(f"scaled_exit={scaled_code}")
    print(f"missing_metric_exit={missing_code}")
    print(f"nonhermitian_exit={nonhermitian_code}")
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
