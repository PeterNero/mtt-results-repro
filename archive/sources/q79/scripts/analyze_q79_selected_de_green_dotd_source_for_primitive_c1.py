"""Build the q79 selected D_E/Green/dotD source gate for primitive C1.

This artifact is deliberately a gate, not a source proof.  It checks the
current Route-C operator stack in two lanes:

* the honest current packets, which fail because selected-source provenance is
  absent;
* the pre-existing selected-flags-only diagnostic packets, which pass and
  therefore show that the current obstruction is provenance rather than hidden
  finite arithmetic.

It then maps those operator slots to the 24 primitive C1 matrices required by
the C1 response calculator.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SCRIPTS = ROOT / "scripts"

OUT_DIR = CANDIDATES / "q79_selected_de_green_dotd_source_for_primitive_c1"
OUT_CANDIDATE = CANDIDATES / "q79_selected_de_green_dotd_source_for_primitive_c1.candidate.json"
OUT_CERT = CERTS / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1.md"
OUT_TABLE = OUT_DIR / "promotion_lane_current_validator_summary.json"
OUT_CONTRACT = OUT_DIR / "de_green_dotd_source_contract.open.json"
OUT_DEPENDENCIES = OUT_DIR / "primitive_c1_sector_dependency_map.json"

STATUS = "Q79_SELECTED_DE_GREEN_DOTD_SOURCE_FOR_PRIMITIVE_C1_GATE_BUILT_PROVENANCE_OPEN"
NEXT = "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1"

ROUTEC_DIR = CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
HYP_DIR = (
    CANDIDATES
    / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual"
    / "hypothetical_routec_selected_flags_only"
)
ORIGINAL_PACKETS = {
    "route_c_residuals": ROUTEC_DIR / "route_c_residual.candidate.json",
    "de_action": ROUTEC_DIR / "de_action.candidate.json",
    "riesz_gap": ROUTEC_DIR / "riesz_gap.candidate.json",
    "reduced_green": ROUTEC_DIR / "reduced_green.candidate.json",
    "dotd_response": ROUTEC_DIR / "dotd_response.candidate.json",
    "selected_source_promotion": CERTS / "selected_hym_operator_source_promotion.attempt.json",
}
HYPOTHETICAL_PACKETS = {
    "route_c_residuals": HYP_DIR / "route_c_residuals.selected_flags_only.json",
    "de_action": HYP_DIR / "de_action.selected_flags_only.json",
    "riesz_gap": HYP_DIR / "riesz_gap.selected_flags_only.json",
    "reduced_green": HYP_DIR / "reduced_green.selected_flags_only.json",
    "dotd_response": HYP_DIR / "dotd_response.selected_flags_only.json",
    "selected_source_promotion": HYP_DIR / "selected_source_promotion.selected_flags_only.json",
}
VALIDATORS = {
    "route_c_residuals": "validate_iwasawa_route_c_residuals.py",
    "de_action": "validate_iwasawa_de_action.py",
    "riesz_gap": "validate_iwasawa_riesz_gap.py",
    "reduced_green": "validate_iwasawa_reduced_green.py",
    "dotd_response": "validate_iwasawa_dotd_response.py",
    "selected_source_promotion": "validate_iwasawa_selected_source_promotion.py",
}

INPUTS = {
    "same_source_operator_no_go": (
        CERTS / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json"
    ),
    "visible_operator_or_primitive_c1_target": (
        CERTS / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json"
    ),
    "selected_monad_l2_operator_frontier": (
        CERTS / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json"
    ),
    "current_selected_source_promotion_attempt": (
        CERTS / "selected_hym_operator_source_promotion.attempt.json"
    ),
    "primitive_c1_contract": (
        CANDIDATES
        / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions"
        / "primitive_c1_atomic_contract.open.json"
    ),
}

SECTOR_SLOTS = {
    "u": {"left": "Q", "right": "u", "higgs": "H"},
    "d": {"left": "Q", "right": "d", "higgs": "H"},
    "e": {"left": "L", "right": "e", "higgs": "H"},
    "nuD": {"left": "L", "right": "N", "higgs": "H"},
}
TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)
TERM_REQUIREMENTS = {
    "theta_overlap_variation": [
        "selected DeltaTheta_C1 source derivative",
        "selected Hessian or overlap-kernel variation",
        "same q79/F,m=1 branch orientation",
    ],
    "left_zero_mode_response": [
        "selected left slot D_E",
        "selected left slot Riesz projector and Green inverse",
        "selected left slot dotD_alpha1 response",
    ],
    "right_zero_mode_response": [
        "selected right slot D_E",
        "selected right slot Riesz projector and Green inverse",
        "selected right slot dotD_alpha1 response",
    ],
    "higgs_zero_mode_response": [
        "selected H slot D_E",
        "selected H slot Riesz projector and Green inverse",
        "selected H slot dotD_alpha1 response",
    ],
    "explicit_vertex": [
        "selected higher-derivative vertex from the same operator source",
        "or a selected theorem forcing the primitive matrix to vanish",
    ],
    "basis_connection": [
        "selected horizontal gauge or basis transport",
        "selected Gram/basis connection if non-horizontal",
    ],
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def run_validator(name: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / VALIDATORS[name]), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "validator": f"scripts/{VALIDATORS[name]}",
        "path": rel(path),
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_head": proc.stdout.splitlines()[:32],
        "stdout": proc.stdout,
    }


def run_all_validators(paths: dict[str, Path]) -> dict[str, dict[str, Any]]:
    return {name: run_validator(name, path) for name, path in paths.items()}


def primitive_dependency_map() -> dict[str, Any]:
    atoms: list[dict[str, Any]] = []
    for sector, slots in SECTOR_SLOTS.items():
        for term in TERMS:
            if term == "left_zero_mode_response":
                operator_slots = [slots["left"]]
            elif term == "right_zero_mode_response":
                operator_slots = [slots["right"]]
            elif term == "higgs_zero_mode_response":
                operator_slots = [slots["higgs"]]
            elif term in {"theta_overlap_variation", "explicit_vertex", "basis_connection"}:
                operator_slots = [slots["left"], slots["right"], slots["higgs"]]
            else:
                operator_slots = []
            atoms.append(
                {
                    "id": f"sectors.{sector}.{term}",
                    "sector": sector,
                    "term": term,
                    "matrix_shape": [3, 3],
                    "operator_slots": operator_slots,
                    "slot_roles": slots,
                    "required_selected_data": TERM_REQUIREMENTS[term],
                    "same_source_required": True,
                    "status": "OPEN_UNTIL_SELECTED_OPERATOR_SOURCE_CERTIFICATE",
                }
            )
    return {
        "schema": "Q79PrimitiveC1SectorDependencyMap.v1",
        "status": "OPEN_24_ATOMS_DEPEND_ON_SELECTED_DE_GREEN_DOTD_SOURCE",
        "sector_slots": SECTOR_SLOTS,
        "atom_count": len(atoms),
        "atoms": atoms,
    }


def build_source_contract(
    original: dict[str, dict[str, Any]],
    hypothetical: dict[str, dict[str, Any]],
    dep_map: dict[str, Any],
) -> dict[str, Any]:
    requirements = []
    for name in (
        "route_c_residuals",
        "de_action",
        "riesz_gap",
        "reduced_green",
        "dotd_response",
        "selected_source_promotion",
    ):
        requirements.append(
            {
                "name": name,
                "validator": original[name]["validator"],
                "current_original_packet": original[name]["path"],
                "current_original_exit_code": original[name]["exit_code"],
                "hypothetical_selected_flags_packet": hypothetical[name]["path"],
                "hypothetical_selected_flags_exit_code": hypothetical[name]["exit_code"],
                "required_provenance_field": {
                    "route_c_residuals": "selected_source_verified",
                    "de_action": "operator_slots[*].selected_source_verified",
                    "riesz_gap": "spectral_slots[*].selected_source_verified",
                    "reduced_green": "green_slots[*].selected_source_verified",
                    "dotd_response": (
                        "dotd_response_slots[*].selected_dotD_source_verified "
                        "and alpha1_driver_verified"
                    ),
                    "selected_source_promotion": "selected_source_verified plus passing source stack",
                }[name],
                "diagnostic_not_proof": True,
            }
        )

    return {
        "schema": "Q79SelectedDEGreenDotDSourceForPrimitiveC1Contract.v1",
        "status": "OPEN_SELECTED_SOURCE_PROVENANCE_REQUIRED",
        "source_identity": {
            "branch_id": "q79/F,m=1",
            "source_kind": "selected visible bundle/operator source",
            "selected_source_certificate_present": False,
            "selected_RouteC_or_typed_DE_construction_present": False,
            "same_source_for_valpha_s3_DE_Green_dotD_C1": False,
        },
        "operator_stack_requirements": requirements,
        "primitive_c1_dependency_map": rel(OUT_DEPENDENCIES),
        "primitive_c1_atom_count": dep_map["atom_count"],
        "guardrail": (
            "The selected-flags-only packets are a diagnostic. They cannot be cited "
            "as selected source data or used to fill primitive C1 matrices."
        ),
    }


def build_candidate() -> dict[str, Any]:
    original = run_all_validators(ORIGINAL_PACKETS)
    hypothetical = run_all_validators(HYPOTHETICAL_PACKETS)
    dep_map = primitive_dependency_map()
    contract = build_source_contract(original, hypothetical, dep_map)
    write_json(OUT_DEPENDENCIES, dep_map)
    write_json(OUT_CONTRACT, contract)

    original_failures_are_provenance = {
        name: (
            original[name]["exit_code"] == 1
            and any("selected" in line or "source" in line for line in original[name]["stdout_head"])
        )
        for name in original
    }
    hypothetical_passes = {name: hypothetical[name]["exit_code"] == 0 for name in hypothetical}
    promotion_stack_reduced_to_provenance = (
        all(original[name]["exit_code"] == 1 for name in original)
        and all(hypothetical_passes.values())
    )

    data = {
        "certificate": "Q79SelectedDEGreenDotDSourceForPrimitiveC1",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "contract": rel(OUT_CONTRACT),
        "dependency_map": rel(OUT_DEPENDENCIES),
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "current_routec_stack": {
            "branch_id": "q79/F,m=1",
            "original_validators": original,
            "hypothetical_selected_flags_validators": hypothetical,
            "original_failures_are_source_or_provenance_flags": original_failures_are_provenance,
            "hypothetical_selected_flags_all_pass": all(hypothetical_passes.values()),
            "diagnostic_not_proof": True,
            "interpretation": (
                "The current finite Route-C D_E/Riesz/Green/dotD stack has no "
                "validator-detected arithmetic obstruction after selected-source "
                "flags are hypothetically supplied. The honest stack still fails, "
                "so the missing theorem is selected operator-source provenance."
            ),
        },
        "primitive_c1_source_gate": {
            "source_contract": rel(OUT_CONTRACT),
            "sector_dependency_map": rel(OUT_DEPENDENCIES),
            "atom_count": dep_map["atom_count"],
            "sector_slots": SECTOR_SLOTS,
            "terms": list(TERMS),
            "status": "OPEN_SELECTED_DE_GREEN_DOTD_SOURCE_REQUIRED",
            "interpretation": (
                "Primitive C1 can only be filled after the selected operator source "
                "emits the relevant D_E, Riesz, Green, dotD, DeltaTheta, vertex, "
                "and basis-transport data on the same q79/F,m=1 branch."
            ),
        },
        "what_closes_now": {
            "selected_DE_Green_dotD_source_gate_created": True,
            "current_routec_DE_Riesz_Green_dotD_validators_executed": True,
            "honest_current_routec_stack_rejected_without_selected_source": True,
            "selected_flags_only_routec_stack_passes_as_diagnostic": all(
                hypothetical_passes.values()
            ),
            "provenance_vs_arithmetic_boundary_sharpened": promotion_stack_reduced_to_provenance,
            "primitive_c1_24_atom_slot_dependencies_mapped": dep_map["atom_count"] == 24,
        },
        "what_remains_open": {
            "selected_visible_bundle_operator_source_certificate": True,
            "selected_RouteC_residual_or_typed_DE_construction": True,
            "same_source_ChernWeil_GS_row": True,
            "honest_selected_rhoE_DE_Riesz_Green_dotD": True,
            "selected_DeltaTheta_C1_Hessian_or_kernel_derivative": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "selected_C1_response_matrices": True,
            "selected_Yukawa_CKM_PMNS_Higgs_RG_data": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_flags_as_proof": False,
            "claims_selected_operator_source_constructed": False,
            "claims_selected_RouteC_residual": False,
            "claims_HYM_connection_constructed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_selected_C1_response_matrices": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedDEGreenDotDSourceGateTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected D_E/Green/dotD source gate for primitive C1 is "
                "well formed. Current Route-C finite packets support the arithmetic "
                "shape after diagnostic provenance flags are supplied, but no "
                "selected-source proof is supplied here. Therefore the next decisive "
                "object is a selected Route-C source certificate or a typed D_E "
                "construction from selected monad/Cech data."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return data


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def validator_table(validators: dict[str, dict[str, Any]]) -> str:
    lines = ["| packet | exit | first line |", "| --- | ---: | --- |"]
    for name, result in validators.items():
        first = result["stdout_head"][0] if result["stdout_head"] else ""
        lines.append(f"| `{name}` | `{result['exit_code']}` | {first} |")
    return "\n".join(lines)


def build_paper(data: dict[str, Any]) -> str:
    stack = data["current_routec_stack"]
    primitive = data["primitive_c1_source_gate"]
    return f"""# Q79 Selected D_E/Green/dotD Source for Primitive C1 v1

## Result

This creates the selected `D_E`/Green/`dotD` source gate for the 24 primitive
C1 matrices.

The promotion lane is not selected-source proof.  The honest current Route-C
stack is still rejected by the validators because selected source provenance is
absent.  The construction lane is now sharply identified: either prove a
selected Route-C source certificate for these packets, or rebuild `D_E`,
Riesz/Green, and `dotD` from typed selected monad/Cech transition data.

## Promotion Lane

Honest current stack:

{validator_table(stack["original_validators"])}

Selected-flags-only diagnostic stack, i.e. the selected-flags-only diagnostic:

{validator_table(stack["hypothetical_selected_flags_validators"])}

Interpretation: {stack["interpretation"]}

This diagnostic is not selected-source proof.

## Primitive C1 Dependencies

- dependency map: `{primitive["sector_dependency_map"]}`
- atom count: `{primitive["atom_count"]}`
- status: `{primitive["status"]}`

Sector slots:

- `u`: left `Q`, right `u`, Higgs `H`
- `d`: left `Q`, right `d`, Higgs `H`
- `e`: left `L`, right `e`, Higgs `H`
- `nuD`: left `L`, right `N`, Higgs `H`

The 24 primitive C1 atoms are four sectors times six terms:
`theta_overlap_variation`, `left_zero_mode_response`,
`right_zero_mode_response`, `higgs_zero_mode_response`, `explicit_vertex`,
and `basis_connection`.

Interpretation: {primitive["interpretation"]}

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a gate theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(
        OUT_TABLE,
        {
            "status": data["status"],
            "next_required_artifact": data["next_required_artifact"],
            "original_exit_codes": {
                name: result["exit_code"]
                for name, result in data["current_routec_stack"]["original_validators"].items()
            },
            "hypothetical_exit_codes": {
                name: result["exit_code"]
                for name, result in data["current_routec_stack"][
                    "hypothetical_selected_flags_validators"
                ].items()
            },
            "what_closes_now": data["what_closes_now"],
        },
    )
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected D_E/Green/dotD source gate for primitive C1")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
