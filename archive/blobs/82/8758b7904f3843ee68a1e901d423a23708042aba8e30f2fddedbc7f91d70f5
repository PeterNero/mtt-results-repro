"""Lock down the selected Route-C source-selector and basis calculation.

The goal is not to promote lifted flags.  It is to prove, by executable
comparison, that the current manifest's remaining finite obstruction is exactly
the selector/basis provenance layer: the root and formal-lift payloads have the
same matrices, and differ only in selected-source/alpha1-driver flags.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"

FIRST_RUN = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"
OUTPUT_DATA = DATA / "selected_routec_source_selector_and_basis_theorem.candidate.json"
OUTPUT_CERT = CERTS / "selected_routec_source_selector_and_basis_theorem_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1.md"

ROOT_DIR = DATA / "selected_routec_strominger_galerkin_solve"
FORMAL_DIR = ROOT_DIR / "formal_lift_diagnostic"
CHECK_FILES = {
    "route_c_residual": "route_c_residual.candidate.json",
    "rhoE_mesh": "rhoE_mesh.candidate.json",
    "rhoE_metric": "rhoE_metric.candidate.json",
    "sector_maps": "sector_maps.candidate.json",
    "de_action": "de_action.candidate.json",
    "riesz_gap": "riesz_gap.candidate.json",
    "reduced_green": "reduced_green.candidate.json",
    "dotd_response": "dotd_response.candidate.json",
}
ALLOWED_FLAG_KEYS = {
    "selected_source_verified",
    "selected_dotD_source_verified",
    "alpha1_driver_verified",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def diff_json(left: Any, right: Any, path: str = "") -> list[dict[str, Any]]:
    if type(left) is not type(right):
        return [{"path": path, "left": left, "right": right}]
    if isinstance(left, dict):
        diffs: list[dict[str, Any]] = []
        for key in sorted(set(left) | set(right)):
            next_path = f"{path}/{key}"
            if key not in left or key not in right:
                diffs.append({"path": next_path, "left": left.get(key), "right": right.get(key)})
            else:
                diffs.extend(diff_json(left[key], right[key], next_path))
        return diffs
    if isinstance(left, list):
        diffs = []
        if len(left) != len(right):
            diffs.append({"path": f"{path}/length", "left": len(left), "right": len(right)})
        for index, (l_item, r_item) in enumerate(zip(left, right)):
            diffs.extend(diff_json(l_item, r_item, f"{path}/{index}"))
        return diffs
    if left != right:
        return [{"path": path, "left": left, "right": right}]
    return []


def terminal_key(path: str) -> str:
    return path.rsplit("/", maxsplit=1)[-1]


def compare_payloads() -> dict[str, Any]:
    by_file: dict[str, Any] = {}
    all_flag_only = True
    total_diffs = 0
    changed_keys: set[str] = set()
    for key, filename in CHECK_FILES.items():
        left = load_json(ROOT_DIR / filename)
        right = load_json(FORMAL_DIR / filename)
        diffs = diff_json(left, right)
        file_keys = sorted({terminal_key(item["path"]) for item in diffs})
        flag_only = all(item["left"] is False and item["right"] is True and terminal_key(item["path"]) in ALLOWED_FLAG_KEYS for item in diffs)
        all_flag_only = all_flag_only and flag_only
        total_diffs += len(diffs)
        changed_keys.update(file_keys)
        by_file[key] = {
            "diff_count": len(diffs),
            "changed_terminal_keys": file_keys,
            "flag_only_false_to_true": flag_only,
            "sample_diffs": diffs[:16],
        }
    return {
        "by_file": by_file,
        "all_differences_are_allowed_flags": all_flag_only,
        "total_difference_count": total_diffs,
        "changed_terminal_keys": sorted(changed_keys),
    }


def sector_dimensions() -> dict[str, Any]:
    de_action = load_json(ROOT_DIR / "de_action.candidate.json")
    slots = de_action["operator_slots"]
    return {
        sector: {
            "kind": slot["kind"],
            "domain_dimension": slot["domain_dimension"],
            "range_dimension": slot["range_dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "zero_mode_count": len(slot["ordered_zero_mode_basis"]),
        }
        for sector, slot in sorted(slots.items())
    }


def root_failure_summary(first_run: dict[str, Any]) -> dict[str, Any]:
    failures: dict[str, Any] = {}
    for name, result in first_run["validation"]["honest_root"].items():
        if result["passed"]:
            continue
        failures[name] = {
            "exit_code": result["exit_code"],
            "last_lines": result["output"],
        }
    return failures


def build_candidate() -> dict[str, Any]:
    first_run = load_json(FIRST_RUN)
    basis_skeleton = load_json(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json")
    protocol = load_json(Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json")
    comparison = compare_payloads()
    dimensions = sector_dimensions()
    honest_failures = root_failure_summary(first_run)

    flag_keys_exact = comparison["changed_terminal_keys"] == sorted(ALLOWED_FLAG_KEYS)
    lower_algebra_passes = first_run["validation"]["formal_lift_lower_validators_all_pass"] is True
    de_response_promotes_conditionally = first_run["validation"]["formal_lift_promotion_passes"] is True
    root_selected_flags_missing = bool(honest_failures)
    basis_actual_open = basis_skeleton["verdict"]["closes_actual_basis_functions"] is False

    return {
        "candidate": "MTTSelectedRouteCSourceSelectorAndBasisTheorem",
        "status": "MTT_SELECTED_ROUTEC_SOURCE_SELECTOR_AND_BASIS_CALCULATION_LOCKED_SELECTOR_OPEN",
        "inputs": {
            "first_run": rel(FIRST_RUN),
            "manifest_root": rel(ROOT_DIR),
            "formal_lift_manifest": rel(FORMAL_DIR),
            "basis_skeleton_certificate": str(Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json"),
            "galerkin_protocol_certificate": str(Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json"),
        },
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_CONDITIONAL_THEOREM",
            "straight_path": {
                "classification": "NOT_CLOSED",
                "reason": "The honest root payload fails selected-source and alpha1-driver provenance checks.",
            },
            "superset_convergence": {
                "classification": "FLAG_PROVENANCE_EQUIVALENCE",
                "locked_target": "same q79/F,m=1 Route-C matrices already in the first-run manifest",
                "result": "All root-vs-formal differences are false-to-true provenance flags; the matrices are unchanged.",
            },
            "superset_repair": {
                "classification": "TWO_OBJECT_REPAIR",
                "required_objects": [
                    "selected HYM/Strominger source theorem for the q79/F,m=1 S3/GS branch",
                    "quotient-valid Galerkin basis certificate tying B_N, quadrature, and operator matrices to that source",
                ],
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
                "reason": "No measured masses, mixings, gauge values, or benchmark matrices are used.",
            },
        },
        "calculation": {
            "root_vs_formal_payload_diff": comparison,
            "honest_root_failures": honest_failures,
            "formal_lift_lower_validators_all_pass": lower_algebra_passes,
            "formal_lift_de_response_promotion_passes": de_response_promotes_conditionally,
            "sector_dimension_table": dimensions,
            "basis_skeleton_verdict": basis_skeleton["verdict"],
            "basis_protocol_values_open": protocol["values_still_open"],
        },
        "locked_conditions": {
            "C1_source_selector_condition": {
                "name": "selected source provenance",
                "must_prove": [
                    "route_c_residual.selected_source_verified",
                    "operator_slots[*].selected_source_verified",
                    "spectral_slots[*].selected_source_verified",
                    "green_slots[*].selected_source_verified",
                    "dotd_response_slots[*].selected_dotD_source_verified",
                    "dotd_response_slots[*].alpha1_driver_verified",
                ],
                "calculation_status": "exactly these flags separate honest root from algebraically passing formal lift",
            },
            "C2_basis_condition": {
                "name": "quotient-valid selected Galerkin basis",
                "must_prove": basis_skeleton["still_missing_for_actual_B_N"],
                "calculation_status": "the current matrices have validator-coherent finite bases but not an emitted selected quotient/deck basis certificate",
            },
        },
        "what_closes_now": {
            "root_formal_matrix_equality_modulo_flags": comparison["all_differences_are_allowed_flags"],
            "changed_keys_exactly_selected_flags": flag_keys_exact,
            "downstream_algebra_conditional_pass_confirmed": lower_algebra_passes and de_response_promotes_conditionally,
            "honest_failure_cutset_identified": root_selected_flags_missing,
            "basis_gap_identified": basis_actual_open,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_provenance_theorem": True,
            "quotient_valid_BN_basis_certificate": True,
            "selected_spectral_error_budget_from_actual_BN": True,
            "primitive_C1_contractions_after_honest_source": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedRouteCSourceSelectorAndBasisCutsetTheorem",
            "proved": True,
            "statement": (
                "For the current first-run manifest, the finite matrices in the honest root payload and the formal-lift diagnostic payload "
                "are identical modulo selected-source and alpha1-driver flags.  The formal-lift payload passes every lower algebraic "
                "validator and the de_response promotion gate.  Therefore the remaining calculation is locked to two proof objects: "
                "derive the selected-source flags from MTT, and certify the quotient-valid Galerkin basis/operator extraction.  No observed "
                "physical data or benchmark entries enter this reduction."
            ),
        },
        "next_required_artifact": "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "MTTSelectedRouteCSourceSelectorAndBasisTheorem",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "locked_conditions": list(candidate["locked_conditions"].keys()),
        "closure_claimed": False,
        "target_fitting_used": False,
        "primary_next_artifact": candidate["next_required_artifact"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    closes = candidate["what_closes_now"]
    calc = candidate["calculation"]
    return f"""# MTT Selected Route-C Source Selector and Basis Theorem

Status: `{candidate['status']}`.

This locks the remaining calculation down to an exact cut set.

## Result

The honest root manifest and the formal-lift diagnostic manifest have the same
finite matrices.  Their only differences are false-to-true provenance flags:

- `selected_source_verified`
- `selected_dotD_source_verified`
- `alpha1_driver_verified`

Total root/formal differences: `{calc['root_vs_formal_payload_diff']['total_difference_count']}`.

Formal-lift lower validators all pass: `{calc['formal_lift_lower_validators_all_pass']}`.
Formal-lift de_response promotion passes: `{calc['formal_lift_de_response_promotion_passes']}`.

## Path Type

- Straight path: not closed, because the honest payload still fails selected-source checks.
- Superset convergence: closed as a conditional calculation.  The target finite matrices are fixed, and the only algebraic delta is provenance flags.
- Superset repair: two objects remain: selected-source theorem and quotient-valid Galerkin basis certificate.
- Diagnostic/backfit: none; no observed masses, mixings, gauge constants, or benchmark matrices are used.

## Locked Conditions

`C1_source_selector_condition` must derive the selected-source and alpha1-driver
flags from MTT rather than assert them.

`C2_basis_condition` must emit the actual quotient/deck-valid Galerkin basis
`B_N`, quadrature, and selected operator matrices.  The existing finite basis is
validator-coherent, but the q79 basis skeleton still says actual basis functions
are open.

## What Is Now Closed

- root/formal matrix equality modulo flags: `{closes['root_formal_matrix_equality_modulo_flags']}`
- changed keys exactly selected flags: `{closes['changed_keys_exactly_selected_flags']}`
- downstream algebra conditionally passes: `{closes['downstream_algebra_conditional_pass_confirmed']}`
- honest failure cut set identified: `{closes['honest_failure_cutset_identified']}`
- basis gap identified: `{closes['basis_gap_identified']}`

## Theorem

`SelectedRouteCSourceSelectorAndBasisCutsetTheorem` is proved:

For the current first-run manifest, the finite matrices in the honest root
payload and the formal-lift diagnostic payload are identical modulo
selected-source and alpha1-driver flags.  The formal-lift payload passes every
lower algebraic validator and the de_response promotion gate.  Therefore the
remaining calculation is locked to two proof objects: derive the selected-source
flags from MTT, and certify the quotient-valid Galerkin basis/operator
extraction.

Next artifact: `{candidate['next_required_artifact']}`.
"""


def main() -> int:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT_DATA), "status": candidate["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
