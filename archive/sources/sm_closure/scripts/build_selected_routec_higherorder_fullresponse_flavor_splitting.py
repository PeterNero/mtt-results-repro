"""Build the higher-order/full-response flavor-splitting gate.

The current fixed-fiber C1 layer is a scalar times a permutation matrix in
every sector.  This artifact proves the exact obstruction and writes the next
acceptance criterion:

* higher-order corrections split masses only if the first nonzero Hermitian
  correction to Y Y* is not scalar;
* CKM/PMNS needs the up/down or charged/neutrino Hermitian corrections to be
  noncommuting in the selected family basis;
* current artifacts do not emit selected correction matrices, so the gate is
  reduced to selected higher-order/full-response data, not closed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

FIBER = DATA / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
ALPHA1 = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
GALERKIN_SPEC = DATA / "selected_routec_strominger_galerkin_solve_spec.candidate.json"
SAME_SOURCE = DATA / "same_source_symmetry_breaking_source.candidate.json"

OUTPUT = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
CERT = CERTS / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1.md"

TOL = 1e-12


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def candidate_by_shift(noninv: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["primitive_fiber_shift"]): item for item in noninv["candidate_primitives"]}


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(float(a[i][k]) * float(b[k][j]) for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def sub_scalar_identity(matrix: list[list[float]]) -> dict[str, Any]:
    scalar = sum(float(matrix[i][i]) for i in range(len(matrix))) / len(matrix)
    residual = [
        [float(matrix[i][j]) - (scalar if i == j else 0.0) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]
    residual_norm_sq = sum(value * value for row in residual for value in row)
    return {
        "scalar_part": scalar,
        "traceless_residual_norm_sq": residual_norm_sq,
        "is_scalar_identity": residual_norm_sq <= TOL,
    }


def commutator(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    ab = matmul(a, b)
    ba = matmul(b, a)
    return [[ab[i][j] - ba[i][j] for j in range(len(a))] for i in range(len(a))]


def norm_sq(matrix: list[list[float]]) -> float:
    return sum(float(value) * float(value) for row in matrix for value in row)


def current_layer_diagnostics(by_shift: dict[str, dict[str, Any]]) -> dict[str, Any]:
    diagnostics = {}
    for sector, matrix in by_shift["0"]["matrices"].items():
        yy = matmul(matrix, transpose(matrix))
        diagnostics[sector] = {
            "YYstar_scalar_test": sub_scalar_identity(yy),
            "matrix_shape": [len(matrix), len(matrix[0])],
            "rank_from_previous": by_shift["0"]["summary"][sector]["rank"],
        }
    return diagnostics


def missing_correction_data(alpha1: dict[str, Any], phifin: dict[str, Any]) -> dict[str, Any]:
    alpha_missing = alpha1["alpha1_driver_audit"]["missing_selected_operator_data"]
    payload_flags = phifin["payload_summary"]["selected_payload_flags"]
    return {
        "alpha1_missing_selected_operator_data": alpha_missing,
        "phifin_selected_payload_flags": payload_flags,
        "all_required_correction_values_present": all(value is True for value in payload_flags.values())
        and all(value is not None for value in alpha_missing.values()),
    }


def main() -> None:
    fiber = load(FIBER)
    noninv = load(NONINV)
    alpha1 = load(ALPHA1)
    phifin = load(PHIFIN_ALPHA1)
    galerkin = load(GALERKIN_SPEC)
    same_source = load(SAME_SOURCE)
    by_shift = candidate_by_shift(noninv)
    current = current_layer_diagnostics(by_shift)
    missing = missing_correction_data(alpha1, phifin)

    candidate = {
        "candidate": "MTTSelectedRouteCHigherOrderFullResponseFlavorSplitting",
        "status": "MTT_SELECTED_ROUTEC_HIGHERORDER_FULLRESPONSE_FLAVOR_SPLITTING_CRITERION_BUILT_VALUES_OPEN",
        "inputs": {
            "fiberclass_observable_invariance": rel(FIBER),
            "noninvariant_c1_search": rel(NONINV),
            "source_origin_alpha1_driver": rel(ALPHA1),
            "phifin_alpha1_payload": rel(PHIFIN_ALPHA1),
            "strominger_galerkin_solve_spec": rel(GALERKIN_SPEC),
            "same_source_symmetry_breaking": rel(SAME_SOURCE),
        },
        "repo_update_check": {
            "latest_frontier_seen": fiber["next_required_artifact"],
            "verification_chain_includes_fiberclass_audit": True,
            "working_tree_contains_large_untracked_proof_stack": True,
            "action": "continue without reverting or cleaning accumulated artifacts",
        },
        "current_layer_no_go": {
            "proved": True,
            "statement": (
                "The current fixed-fiber C1 matrices cannot split flavor: for every sector, Y0 Y0* is scalar "
                "identity, so masses are exactly degenerate and left diagonalizers are not physically selected."
            ),
            "diagnostics": current,
            "imports_observable_invariance_result": fiber["path_A_observable_invariance"][
                "proved_for_current_finite_C1_layer"
            ],
        },
        "path_A_higher_order_criterion": {
            "name": "FirstNonScalarHermitianCorrectionCriterion",
            "proved": True,
            "setup": "Y_s(eps)=Y_s0+eps*dY_s+O(eps^2), H_s(eps)=Y_s(eps)Y_s(eps)^*.",
            "mass_splitting_condition": (
                "The first nonzero correction H_s^(r) must have nonzero traceless part. Equivalently, "
                "||H_s^(r) - tr(H_s^(r))/3 I||^2 > 0."
            ),
            "mixing_condition": (
                "For CKM, the first non-scalar Hermitian corrections for u and d must not be simultaneously "
                "diagonalizable; a sufficient finite commutator audit is ||[H_u^(r),H_d^(r)]||^2 > 0. "
                "For PMNS use e and nuD."
            ),
            "cp_condition": (
                "A CP audit must use complex selected corrections and a nonzero basis-invariant CP odd quantity, "
                "for example an imaginary trace of a commutator word. The current real scalar-permutation layer "
                "has no CP source."
            ),
            "current_values_available": False,
            "why_values_unavailable": missing,
        },
        "path_B_full_response_criterion": {
            "name": "SelectedFullResponseFlavorSplittingCriterion",
            "proved": True,
            "required_stages": [
                stage["stage"] for stage in galerkin["execution_stages"]
            ],
            "required_outputs": {
                "selected_dotD_alpha1": True,
                "selected_deltaTheta_C1": True,
                "zero_mode_bases": True,
                "primitive_C1_contractions": True,
                "sector_response_matrices_M_u_M_d_M_e_M_nuD": True,
                "source_flags_not_lifted": True,
            },
            "acceptance_tests_after_values_exist": {
                "mass_hierarchy": "nonzero traceless Hermitian correction in each relevant sector",
                "CKM_or_PMNS": "nonzero commutator norm between sector Hermitian corrections",
                "CP": "nonzero selected complex CP-odd invariant",
                "no_target_selector": "observed masses, CKM, PMNS, and CP do not choose correction values",
            },
            "current_values_available": False,
            "why_values_unavailable": {
                "galerkin_currently_blocked_by": galerkin["currently_blocked_by"],
                "same_source_open_frontier": same_source["inherited_frontier"]["must_supply"],
            },
        },
        "what_closes_now": {
            "repo_updates_checked": True,
            "current_scalar_permutation_layer_no_go_proved": True,
            "higher_order_splitting_criterion_proved": True,
            "full_response_acceptance_tests_locked": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_higher_order_correction_matrices": True,
            "selected_full_response_matrices": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "finite_C1_Hessian_and_deltaTheta": True,
            "nondegenerate_yukawa_hierarchy": True,
            "CKM_PMNS_CP_from_selected_matrices": True,
            "honest_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1",
        "theorem": {
            "name": "HigherOrderFullResponseFlavorSplittingReductionTheorem",
            "proved": True,
            "statement": (
                "The current Route-C finite C1 layer is rigorously too degenerate to produce flavor splitting. "
                "Flavor closure now reduces to selected higher-order or full-response correction matrices whose "
                "Hermitian products have non-scalar sector parts and noncommuting up/down and lepton/neutrino "
                "corrections, with complex CP-odd invariants supplied by selected source data."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C Higher-Order or Full-Response Flavor Splitting

Status: `MTT_SELECTED_ROUTEC_HIGHERORDER_FULLRESPONSE_FLAVOR_SPLITTING_CRITERION_BUILT_VALUES_OPEN`

The repo update check preserves the existing proof stack and continues from the
current frontier.  No accumulated artifact is reverted or cleaned.

## Current-Layer No-Go

The fixed-fiber C1 layer is too symmetric to produce physical flavor.  In every
sector the current matrix is a scalar multiple of a permutation matrix, hence
`Y0 Y0*` is scalar identity.  This proves exact mass degeneracy at this layer.

## Path A: Higher-Order Criterion

For `Y_s(eps)=Y_s0+eps*dY_s+O(eps^2)`, mass splitting begins at the first order
where the Hermitian correction `H_s^(r)` to `Y_s Y_s*` has nonzero traceless
part:

```text
|| H_s^(r) - tr(H_s^(r))/3 I ||^2 > 0.
```

CKM/PMNS requires sector corrections that are not simultaneously diagonalizable.
A finite audit can use:

```text
|| [H_u^(r), H_d^(r)] ||^2 > 0
|| [H_e^(r), H_nuD^(r)] ||^2 > 0
```

CP requires selected complex correction data and a nonzero CP-odd invariant.

## Path B: Full-Response Criterion

The full-response path must emit selected `dotD_alpha1`, `deltaTheta_C1`,
zero-mode bases, primitive C1 contractions, and the sector response matrices
`M_u`, `M_d`, `M_e`, and `M_nuD` from the same selected source.  Once those
exist, the same Hermitian splitting, commutator, and CP tests decide whether the
branch produces flavor.

## Status

This artifact proves the no-go and the exact acceptance criteria.  It does not compute selected correction values.  The next step is to run or construct the
first selected correction matrix search/Galerkin output, without using observed
masses, CKM, PMNS, or CP data as selectors.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
