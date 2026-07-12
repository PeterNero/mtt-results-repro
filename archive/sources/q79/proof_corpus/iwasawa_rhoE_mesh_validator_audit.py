"""Audit the finite-mesh rho_E validator for Iwasawa FE gluing."""

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
CERT = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
BUNDLE_CONTRACT = CERT_DIR / "iwasawa_bundle_fe_gluing_contract_certificate.json"
SCALAR_FE = CERT_DIR / "iwasawa_scalar_fe_gluing_certificate.json"
CONSTANT_VALIDATOR = CERT_DIR / "iwasawa_rhoE_validator_certificate.json"
RHO_TEMPLATE = CERT_DIR / "iwasawa_bundle_rhoE_data.template.json"
PAPER = ROOT / "Iwasawa_RhoE_Mesh_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_rhoE_mesh.py"


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


def identity_matrix() -> list[list[int]]:
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]


def identity_mesh_candidate() -> dict[str, Any]:
    ident = identity_matrix()
    return {
        "certificate": "TemporaryRhoEMeshCandidate",
        "rank": 3,
        "mesh_N": 2,
        "section_convention": "s(gamma*z)=rho_E(gamma,z)s(z)",
        "generator_data": {f"g{i}": matrix(ident) for i in range(1, 7)},
    }


def bad_coordinate_override_candidate() -> dict[str, Any]:
    data = identity_mesh_candidate()
    override = [
        [2, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    data["generator_data"]["g1"] = {
        "matrix": matrix(identity_matrix())["matrix"],
        "values": {
            "0,2,0,0,0,0": matrix(override),
        },
    }
    return data


def missing_table_candidate() -> dict[str, Any]:
    data = identity_mesh_candidate()
    data["generator_data"]["g1"] = {"values": {}}
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
        path = Path(tmp) / "rhoE_mesh_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    bundle_contract = load_json(BUNDLE_CONTRACT)
    scalar_fe = load_json(SCALAR_FE)
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
    identity_code, identity_output = run_temp_candidate(identity_mesh_candidate())
    bad_code, bad_output = run_temp_candidate(bad_coordinate_override_candidate())
    missing_code, missing_output = run_temp_candidate(missing_table_candidate())

    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    supported_ok = (
        "rank must be 3" in str(supported.get("rank", ""))
        and "positive integer" in str(supported.get("mesh_N", ""))
        and "g1..g6" in str(supported.get("generator_data", ""))
        and "x1,x2,y1,y2,t1,t2" in str(supported.get("generator_data", ""))
        and "[real, imag]" in str(supported.get("complex_entry", ""))
        and "overrides" in str(supported.get("constant_fallback", ""))
        and "absorbed" in str(supported.get("absorbed_word_convention", ""))
    )

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_RHOE_MESH_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if bundle_contract.get("status")
            == "IWASAWA_BUNDLE_FE_GLUING_CONTRACT_FORMULATED_RHOE_DATA_OPEN"
            and scalar_fe.get("status")
            == "IWASAWA_SCALAR_FE_GLUING_SKELETON_FORMULATED_BUNDLE_DE_OPEN"
            and constant_validator.get("status")
            == "IWASAWA_RHOE_VALIDATOR_FORMULATED_DATA_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "bundle FE contract, scalar FE skeleton, constant validator, and open template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "validate_mesh_path_independence",
                    "reduce_target",
                    "mesh_N",
                    "return 2",
                    "corner product mismatch",
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
                    "boundary_target_matrix_lookup",
                    "determinants_nonzero_on_visited_boundary_targets",
                    "finite_corner_path_independence",
                    "coordinate_override_bad_candidate_fails",
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
                    "symbolic_coordinate_dependent_cocycle_away_from_the_sample_mesh",
                    "Hermitian_metric_compatibility",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "selected_D_E_action",
                ],
            )
            else "FAIL",
            str(not_checked),
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
            "identity mesh smoke test",
            "PASS"
            if identity_code == 0
            and "finite-mesh rho_E validation PASS" in identity_output
            and smoke.get("identity_mesh_candidate_claim_selected") is False
            else "FAIL",
            identity_output.strip(),
        ),
        Gate(
            "coordinate override fails",
            "PASS"
            if bad_code == 1
            and "finite-mesh rho_E validation FAIL" in bad_output
            and "corner product mismatch" in bad_output
            else "FAIL",
            bad_output.strip(),
        ),
        Gate(
            "missing table remains open",
            "PASS"
            if missing_code == 2
            and "MISSING g1 matrix at boundary target" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("identity_mesh_N2_passes_schema") is True
            and smoke.get("identity_mesh_candidate_claim_selected") is False
            and smoke.get("coordinate_override_bad_candidate_fails") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_mesh_rhoE_table_validator") is True
            and closes.get("corner_path_independence_test_for_supplied_face_values") is True
            and closes.get("coordinate_table_extension_beyond_constant_rhoE_validator") is True
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
                    "proof_rho_E_comes_from_selected_bundle_E",
                    "symbolic_or_all_mesh_cocycle_for_nontrivial_data",
                    "Hermitian_metric_compatibility_values",
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
            if verdict.get("closes_finite_mesh_validator_for_rhoE_candidates") is True
            and verdict.get("closes_actual_selected_rhoE") is False
            and "Hermitian metric" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "finite-mesh boundary-target table validator",
                    "actual selected rho_E values or functions",
                    "Do not use the identity transition table as the selected bundle",
                    "Hermitian metric and sector-projection checks",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa finite-mesh rho_E validator audit")
    print("=========================================")
    print()
    print(f"template_exit={template_code}")
    print(f"identity_exit={identity_code}")
    print(f"bad_exit={bad_code}")
    print(f"missing_table_exit={missing_code}")
    print()

    failed = False
    for gate in gates:
        print(f"{gate.label:<30} {gate.status:<10} {gate.detail}")
        if gate.status == "FAIL":
            failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
