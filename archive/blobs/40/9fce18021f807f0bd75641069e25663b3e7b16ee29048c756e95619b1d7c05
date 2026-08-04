"""Audit the finite sector-projection validator for Iwasawa rho_E data."""

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
CERT = CERT_DIR / "iwasawa_sector_projection_validator_certificate.json"
BUNDLE_CONTRACT = CERT_DIR / "iwasawa_bundle_fe_gluing_contract_certificate.json"
MESH_VALIDATOR = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
METRIC_VALIDATOR = CERT_DIR / "iwasawa_rhoE_metric_validator_certificate.json"
ZERO_MODE = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
RHO_TEMPLATE = CERT_DIR / "iwasawa_bundle_rhoE_data.template.json"
PAPER = ROOT / "Iwasawa_Sector_Projection_Validator_v1.md"
SCRIPT = REPO / "scripts" / "validate_iwasawa_sector_maps.py"


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


def higgs_projector() -> list[list[int]]:
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]


def sector_entry(kind: str, dimension: int, projector: list[list[int]]) -> dict[str, Any]:
    return {
        "kind": kind,
        "dimension": dimension,
        "projector": matrix(projector),
    }


def valid_candidate() -> dict[str, Any]:
    ident = identity_matrix()
    sector_maps = {
        sector: sector_entry("family", 3, ident)
        for sector in ("Q", "u", "d", "L", "e", "N")
    }
    sector_maps["H"] = sector_entry("single_higgs_carrier", 1, higgs_projector())
    return {
        "certificate": "TemporarySectorProjectionCandidate",
        "rank": 3,
        "mesh_N": 2,
        "generator_data": {f"g{i}": matrix(ident) for i in range(1, 7)},
        "sector_projection_maps": sector_maps,
    }


def rank_mismatch_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["sector_projection_maps"]["Q"] = sector_entry("family", 3, higgs_projector())
    return data


def noncommuting_transition_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["generator_data"]["g1"] = matrix(
        [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
        ]
    )
    return data


def missing_sector_candidate() -> dict[str, Any]:
    data = valid_candidate()
    data["sector_projection_maps"]["H"] = None
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
        path = Path(tmp) / "sector_candidate.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> None:
    cert = load_json(CERT)
    bundle_contract = load_json(BUNDLE_CONTRACT)
    mesh_validator = load_json(MESH_VALIDATOR)
    metric_validator = load_json(METRIC_VALIDATOR)
    zero_mode = load_json(ZERO_MODE)
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
    identity_code, identity_output = run_temp_candidate(valid_candidate())
    rank_code, rank_output = run_temp_candidate(rank_mismatch_candidate())
    noncomm_code, noncomm_output = run_temp_candidate(noncommuting_transition_candidate())
    missing_code, missing_output = run_temp_candidate(missing_sector_candidate())

    supported_text = " ".join(str(value) for value in supported.values())
    checks_text = " ".join(checks)
    not_checked_text = " ".join(not_checked)
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_SECTOR_PROJECTION_VALIDATOR_FORMULATED_DATA_OPEN"
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
            and metric_validator.get("status")
            == "IWASAWA_RHOE_METRIC_VALIDATOR_FORMULATED_DATA_OPEN"
            and zero_mode.get("status")
            == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            and template.get("status") == "OPEN"
            else "FAIL",
            "bundle contract, rhoE validators, metric validator, zero-mode interface, and template imported",
        ),
        Gate(
            "validator script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "validate_projectors",
                    "validate_rho_invariance",
                    "sector projection validation PASS",
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
                    "kind family and dimension 3",
                    "single_higgs_carrier",
                    "rho_E(gamma,z) P_sector",
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
                    "all_sector_entries_present",
                    "projector_idempotent",
                    "projector_rank_matches_declared_dimension",
                    "rho_E_invariance_on_boundary_faces",
                    "noncommuting_transition_bad_candidate_fails",
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
                    "proof_sector_maps_are_selected_by_MTT",
                    "SM_gauge_representation_embedding",
                    "Higgs_doublet_triplet_decoupling",
                    "sector_specific_D_E_operators",
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
            and "missing sector_projection_maps entries" in exit_codes["2"]
            else "FAIL",
            str(exit_codes),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "MISSING sector projection entries" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "identity sector smoke test",
            "PASS"
            if identity_code == 0
            and "sector projection validation PASS" in identity_output
            and smoke.get("identity_sector_candidate_claim_selected") is False
            else "FAIL",
            identity_output.strip(),
        ),
        Gate(
            "rank mismatch fails",
            "PASS"
            if rank_code == 1
            and "sector projection validation FAIL" in rank_output
            and "projector rank 1 != dimension 3" in rank_output
            else "FAIL",
            rank_output.strip(),
        ),
        Gate(
            "noncommuting transition fails",
            "PASS"
            if noncomm_code == 1
            and "sector projection validation FAIL" in noncomm_output
            and "sector H not rho_E-invariant" in noncomm_output
            else "FAIL",
            noncomm_output.strip(),
        ),
        Gate(
            "missing sector remains open",
            "PASS"
            if missing_code == 2 and "MISSING sector projection entries: H" in missing_output
            else "FAIL",
            missing_output.strip(),
        ),
        Gate(
            "smoke tests recorded",
            "PASS"
            if smoke.get("open_template_refused_with_exit_2") is True
            and smoke.get("identity_family_projectors_pass_schema") is True
            and smoke.get("identity_sector_candidate_claim_selected") is False
            and smoke.get("rank_mismatch_bad_candidate_fails") is True
            and smoke.get("noncommuting_transition_bad_candidate_fails") is True
            and smoke.get("missing_sector_candidate_exit_2") is True
            else "FAIL",
            str(smoke),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_projector_sector_map_validator") is True
            and closes.get("family_vs_higgs_dimension_gate") is True
            and closes.get("rhoE_invariant_sector_projector_gate") is True
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
                    "actual_selected_sector_projection_maps",
                    "proof_sector_maps_come_from_selected_E6_SM_branch",
                    "selected_D_E_action_on_each_sector",
                    "Gram_and_stiffness_matrices",
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
            if verdict.get("closes_sector_projection_validator_for_candidate_data") is True
            and verdict.get("closes_actual_selected_sector_maps") is False
            and "sector-specific D_E actions" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Sector Projection Validator",
                    "Q,u,d,L,e,N are three-family slots",
                    "P_Q=P_u=P_d=P_L=P_e=P_N=I_3",
                    "Do not use identity family projectors as a proof",
                    "sector-specific `D_E` actions",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa sector projection validator audit")
    print("=========================================")
    print()
    print(f"template_exit={template_code}")
    print(f"identity_exit={identity_code}")
    print(f"rank_mismatch_exit={rank_code}")
    print(f"noncommuting_exit={noncomm_code}")
    print(f"missing_sector_exit={missing_code}")
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
