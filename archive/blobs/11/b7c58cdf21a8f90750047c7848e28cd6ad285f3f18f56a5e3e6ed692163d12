"""Audit q79 selected D_E/Green/dotD source gate for primitive C1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = (
    ROOT
    / "scripts"
    / "analyze_q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions.py"
)
SCRIPT = ROOT / "scripts" / "analyze_q79_selected_de_green_dotd_source_for_primitive_c1.py"
CERT = ROOT / "certificates" / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_de_green_dotd_source_for_primitive_c1.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_selected_de_green_dotd_source_for_primitive_c1"
    / "promotion_lane_current_validator_summary.json"
)
CONTRACT = (
    ROOT
    / "candidate_data"
    / "q79_selected_de_green_dotd_source_for_primitive_c1"
    / "de_green_dotd_source_contract.open.json"
)
DEPENDENCIES = (
    ROOT
    / "candidate_data"
    / "q79_selected_de_green_dotd_source_for_primitive_c1"
    / "primitive_c1_sector_dependency_map.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1.md"

STATUS = "Q79_SELECTED_DE_GREEN_DOTD_SOURCE_FOR_PRIMITIVE_C1_GATE_BUILT_PROVENANCE_OPEN"
NEXT = "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1"
VALIDATOR_NAMES = {
    "route_c_residuals",
    "de_action",
    "riesz_gap",
    "reduced_green",
    "dotd_response",
    "selected_source_promotion",
}
SECTOR_SLOTS = {
    "u": {"left": "Q", "right": "u", "higgs": "H"},
    "d": {"left": "Q", "right": "d", "higgs": "H"},
    "e": {"left": "L", "right": "e", "higgs": "H"},
    "nuD": {"left": "L", "right": "N", "higgs": "H"},
}
TERMS = {
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, CONTRACT, DEPENDENCIES, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    contract = load(CONTRACT)
    deps = load(DEPENDENCIES)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(table["status"] == STATUS, "summary table status mismatch", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    stack = cert["current_routec_stack"]
    primitive = cert["primitive_c1_source_gate"]
    closes = cert["what_closes_now"]
    remaining = cert["what_remains_open"]

    require(set(stack["original_validators"]) == VALIDATOR_NAMES, "original validator set changed", failures)
    require(
        set(stack["hypothetical_selected_flags_validators"]) == VALIDATOR_NAMES,
        "hypothetical validator set changed",
        failures,
    )
    for name in VALIDATOR_NAMES:
        require(
            stack["original_validators"][name]["exit_code"] == 1,
            f"original {name} should fail provenance gate",
            failures,
        )
        require(
            stack["hypothetical_selected_flags_validators"][name]["exit_code"] == 0,
            f"hypothetical {name} should pass",
            failures,
        )
        require(
            stack["original_failures_are_source_or_provenance_flags"][name] is True,
            f"{name} failure not classified as source/provenance",
            failures,
        )
    require(stack["hypothetical_selected_flags_all_pass"] is True, "hypothetical stack should pass", failures)
    require(stack["diagnostic_not_proof"] is True, "diagnostic must be marked not proof", failures)

    require(contract["schema"] == "Q79SelectedDEGreenDotDSourceForPrimitiveC1Contract.v1", "contract schema wrong", failures)
    require(contract["status"] == "OPEN_SELECTED_SOURCE_PROVENANCE_REQUIRED", "contract status wrong", failures)
    require(contract["primitive_c1_atom_count"] == 24, "contract primitive count wrong", failures)
    require(len(contract["operator_stack_requirements"]) == 6, "contract stack requirement count wrong", failures)
    require(
        all(item["diagnostic_not_proof"] is True for item in contract["operator_stack_requirements"]),
        "contract requirement lacks diagnostic guardrail",
        failures,
    )

    require(deps["schema"] == "Q79PrimitiveC1SectorDependencyMap.v1", "dependency schema wrong", failures)
    require(deps["atom_count"] == 24, "dependency atom count wrong", failures)
    require(deps["sector_slots"] == SECTOR_SLOTS, "sector slots changed", failures)
    atom_ids = {atom["id"] for atom in deps["atoms"]}
    require(len(atom_ids) == 24, "atom ids not unique", failures)
    require({atom["sector"] for atom in deps["atoms"]} == set(SECTOR_SLOTS), "sector set wrong", failures)
    require({atom["term"] for atom in deps["atoms"]} == TERMS, "term set wrong", failures)
    require(
        all(atom["same_source_required"] is True for atom in deps["atoms"]),
        "some atom lacks same-source requirement",
        failures,
    )
    require(
        all(atom["matrix_shape"] == [3, 3] for atom in deps["atoms"]),
        "some atom has wrong shape",
        failures,
    )
    expected_slots = {
        "sectors.u.left_zero_mode_response": ["Q"],
        "sectors.u.right_zero_mode_response": ["u"],
        "sectors.u.higgs_zero_mode_response": ["H"],
        "sectors.d.left_zero_mode_response": ["Q"],
        "sectors.d.right_zero_mode_response": ["d"],
        "sectors.e.left_zero_mode_response": ["L"],
        "sectors.e.right_zero_mode_response": ["e"],
        "sectors.nuD.left_zero_mode_response": ["L"],
        "sectors.nuD.right_zero_mode_response": ["N"],
        "sectors.nuD.higgs_zero_mode_response": ["H"],
    }
    by_id = {atom["id"]: atom for atom in deps["atoms"]}
    for atom_id, slots in expected_slots.items():
        require(by_id[atom_id]["operator_slots"] == slots, f"wrong slots for {atom_id}", failures)

    require(primitive["atom_count"] == 24, "primitive gate atom count wrong", failures)
    require(primitive["sector_slots"] == SECTOR_SLOTS, "primitive sector slots changed", failures)
    require(primitive["status"] == "OPEN_SELECTED_DE_GREEN_DOTD_SOURCE_REQUIRED", "primitive status wrong", failures)

    for key in (
        "selected_DE_Green_dotD_source_gate_created",
        "current_routec_DE_Riesz_Green_dotD_validators_executed",
        "honest_current_routec_stack_rejected_without_selected_source",
        "selected_flags_only_routec_stack_passes_as_diagnostic",
        "provenance_vs_arithmetic_boundary_sharpened",
        "primitive_c1_24_atom_slot_dependencies_mapped",
    ):
        require(closes[key] is True, f"close flag false: {key}", failures)

    for key in (
        "selected_visible_bundle_operator_source_certificate",
        "selected_RouteC_residual_or_typed_DE_construction",
        "same_source_ChernWeil_GS_row",
        "honest_selected_rhoE_DE_Riesz_Green_dotD",
        "selected_DeltaTheta_C1_Hessian_or_kernel_derivative",
        "all_24_primitive_C1_3x3_matrices",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "selected `D_E`/Green/`dotD` source gate",
        "promotion lane",
        "construction lane",
        "not selected-source proof",
        "current Route-C",
        "24 primitive C1",
        "selected-flags-only diagnostic",
        "Q79SelectedDEGreenDotDSourceGateTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected D_E/Green/dotD source gate audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected D_E/Green/dotD source gate audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
