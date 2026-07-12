"""Audit the executable validator for candidate Iwasawa rho_E data."""

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
CERT = CERT_DIR / "iwasawa_rhoE_validator_certificate.json"
RECOVERY = CERT_DIR / "iwasawa_rhoE_source_recovery_certificate.json"
BUNDLE_CONTRACT = CERT_DIR / "iwasawa_bundle_fe_gluing_contract_certificate.json"
RHO_TEMPLATE = CERT_DIR / "iwasawa_bundle_rhoE_data.template.json"
PAPER = ROOT / "Iwasawa_RhoE_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_rhoE.py"


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


def entry(value: complex | float | int) -> float | list[float]:
    z = complex(value)
    if abs(z.imag) < 1e-12:
        return float(z.real)
    return [float(z.real), float(z.imag)]


def matrix(values: list[list[complex | float | int]]) -> dict[str, Any]:
    return {"matrix": [[entry(value) for value in row] for row in values]}


def candidate(mats: dict[str, list[list[complex | float | int]]]) -> dict[str, Any]:
    return {
        "certificate": "TemporaryRhoECandidate",
        "rank": 3,
        "section_convention": "s(gamma*z)=rho_E(gamma,z)s(z)",
        "generator_data": {name: matrix(value) for name, value in mats.items()},
    }


def identity_candidate() -> dict[str, Any]:
    ident = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    return candidate({f"g{i}": ident for i in range(1, 7)})


def bad_candidate() -> dict[str, Any]:
    ident = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    bad_g1 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    bad_g3 = [
        [1, 0, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
    mats = {f"g{i}": ident for i in range(1, 7)}
    mats["g1"] = bad_g1
    mats["g3"] = bad_g3
    return candidate(mats)


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
        path = Path(tmp) / "rhoE_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    recovery = load_json(RECOVERY)
    bundle_contract = load_json(BUNDLE_CONTRACT)
    template = load_json(RHO_TEMPLATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    supported = cert.get("supported_format_v1", {})
    checks = cert.get("implemented_checks", {})
    exit_codes = cert.get("script_exit_codes", {})
    smoke = cert.get("smoke_tests", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    template_code, template_output = run_validator(RHO_TEMPLATE)
    identity_code, identity_output = run_temp_candidate(identity_candidate())
    bad_code, bad_output = run_temp_candidate(bad_candidate())

    supported_text = " ".join(str(value) for value in supported.values())
    supported_format_ok = (
        "g1..g6" in str(supported.get("generator_data", ""))
        and "3x3 matrix" in str(supported.get("generator_data", ""))
        and "[real, imag]" in str(supported.get("complex_entry", ""))
        and supported.get("constant_generator_matrices_only") is True
        and "future extension"
        in str(supported.get("node_or_coordinate_dependent_rhoE", ""))
    )
    checks_text = " ".join(checks)
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_RHOE_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if recovery.get("status")
            == "IWASAWA_RHOE_SOURCE_RECOVERY_BLOCKED_SELECTED_TRANSITIONS_MISSING"
            and bundle_contract.get("status")
            == "IWASAWA_BUNDLE_FE_GLUING_CONTRACT_FORMULATED_RHOE_DATA_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "rhoE recovery, bundle contract, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "validate_constant_matrices",
                    "g1 g3 = g5 g3 g1",
                    "g5 g2 g4 = g4 g2",
                    "return 2",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "supported format",
            "PASS"
            if supported_format_ok
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
                    "relation_g1_g3_equals_g5_g3_g1",
                    "relation_g2_g3_equals_g6_g3_g2",
                    "relation_g5_g2_g4_equals_g4_g2",
                    "central_g5_g6_commute_with_generators",
                ],
            )
            else "FAIL",
            str(checks),
        ),
        Gate(
            "exit codes",
            "PASS"
            if set(exit_codes) == {"0", "1", "2"}
            and "incomplete/open" in exit_codes["2"]
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
            "identity smoke test",
            "PASS"
            if identity_code == 0
            and "rho_E validation PASS" in identity_output
            and smoke.get("identity_constant_matrices_claim_selected") is False
            else "FAIL",
            identity_output.strip(),
        ),
        Gate(
            "bad candidate fails",
            "PASS"
            if bad_code == 1
            and "rho_E validation FAIL" in bad_output
            and "g1 g3 = g5 g3 g1 failed" in bad_output
            else "FAIL",
            bad_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("identity_constant_matrices_pass_schema") is True
            and smoke.get("identity_constant_matrices_claim_selected") is False
            and smoke.get("noncommuting_bad_candidate_fails") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "still open",
            "OPEN"
            if all(open_items.values())
            and contains_all(
                open_text,
                [
                    "actual_selected_rho_E_values_or_functions",
                    "coordinate_dependent_rhoE_validator",
                    "proof_rho_E_comes_from_selected_bundle_E",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "selected_D_E_action_on_validated_basis",
                ],
            )
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_rho_E_constructed") is False
            and guardrails.get("claims_identity_rhoE_selected") is False
            and guardrails.get("claims_constant_matrix_format_suffices_for_all_bundles") is False
            and guardrails.get("uses_benchmark_or_observed_data") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_validator_for_constant_rhoE_candidates") is True
            and verdict.get("closes_actual_selected_rhoE") is False
            and "iwasawa_bundle_rhoE_data.template.json" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa rho_E Validator",
                    "scripts/validate_iwasawa_rhoE.py",
                    "g1 g3 = g5 g3 g1",
                    "g5 g2 g4 = g4 g2",
                    "open template -> exit 2",
                    "identity matrices -> exit 0 as schema smoke test",
                    "Actual selected `rho_E` remains open",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa rho_E validator audit")
    print("=============================")
    print()
    print(f"template_exit={template_code}")
    print(f"identity_exit={identity_code}")
    print(f"bad_exit={bad_code}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
