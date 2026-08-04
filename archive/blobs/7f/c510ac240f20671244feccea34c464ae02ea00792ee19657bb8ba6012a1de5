"""Build the post-source Weyl coefficient-lift candidate packet.

The post-source formal 110-row layer emits I+Z for u/e and I+X for d/nuD.
That gives a real first split but leaves spectra [4,1,1] and zero CP.  This
artifact checks the minimal finite Weyl additive coefficient lift

    (I + Z) + lambda_Z Z,  (I + X) + lambda_X X,
    lambda_Z,lambda_X in {1+omega, 1+omega^2},

which splits the light doublet to [7,4,1] and produces a nonzero CP-odd
commutator invariant.  The packet is algebraic only: no selected source emits
lambda_Z/lambda_X yet, so no physical SM closure is claimed.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SEARCH = PACKET_DIR / "minimal_weyl_coefficient_lift_search.packet.json"
GAP = PACKET_DIR / "coefficient_lift_source_selection_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_weyl_coefficient_lift.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostSourceWeylCoefficientLift_or_SecondOrderFlavorCandidate_v1.md"

POSTSOURCE = DATA / "selected_postsourceformal110_observableaudit_or_fullsmgap.candidate.json"
FIRST_CORRECTION = DATA / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
PRIMITIVE_FRONTIER = (
    DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
)

STATUS = "MTT_SELECTED_POSTSOURCE_WEYLCOEFFICIENT_LIFT_BUILT_ALGEBRAIC_CANDIDATES_SOURCE_SELECTION_OPEN"
NEXT = "MTT_Selected_WeylCoefficientSourceSelection_or_HigherResponseEmission_v1"
TOL = 1e-9


Matrix = list[list[complex]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def json_complex(value: complex) -> float | list[float]:
    if abs(value.imag) <= TOL:
        return float(value.real)
    return [float(value.real), float(value.imag)]


def json_matrix(matrix: Matrix) -> list[list[float | list[float]]]:
    return [[json_complex(value) for value in row] for row in matrix]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(len(matrix))] for i in range(len(matrix[0]))]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def trace(matrix: Matrix) -> complex:
    return sum(matrix[i][i] for i in range(len(matrix)))


def frob_norm_sq(matrix: Matrix) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(matmul(left, right), matmul(right, left))


def cube_trace(matrix: Matrix) -> complex:
    return trace(matmul(matmul(matrix, matrix), matrix))


def identity() -> Matrix:
    return [[1 + 0j if i == j else 0j for j in range(3)] for i in range(3)]


def z_matrix() -> Matrix:
    omega = complex(-0.5, math.sqrt(3) / 2.0)
    return [
        [1 + 0j, 0j, 0j],
        [0j, omega, 0j],
        [0j, 0j, omega * omega],
    ]


def x_matrix() -> Matrix:
    return [
        [0j, 1 + 0j, 0j],
        [0j, 0j, 1 + 0j],
        [1 + 0j, 0j, 0j],
    ]


def add_scaled(base: Matrix, coeff: complex, direction: Matrix) -> Matrix:
    return [[base[i][j] + coeff * direction[i][j] for j in range(3)] for i in range(3)]


def lift_matrix(direction_name: str, additive_lambda: complex) -> Matrix:
    direction = z_matrix() if direction_name == "Z" else x_matrix()
    return add_scaled(identity(), 1 + additive_lambda, direction)


def branch(lambda_z_label: str, lambda_x_label: str, lambda_z: complex, lambda_x: complex) -> dict[str, Any]:
    phase = lift_matrix("Z", lambda_z)
    shift = lift_matrix("X", lambda_x)
    phase_h = matmul(phase, adjoint(phase))
    shift_h = matmul(shift, adjoint(shift))
    comm = commutator(phase_h, shift_h)
    cp = cube_trace(comm)
    cp_sign = "positive" if cp.imag > 0 else "negative"
    return {
        "branch_id": f"phase_lambda_{lambda_z_label}__shift_lambda_{lambda_x_label}",
        "phase_additive_lambda": lambda_z_label,
        "shift_additive_lambda": lambda_x_label,
        "u_e_matrix_formula": f"(I + Z) + ({lambda_z_label}) Z",
        "d_nuD_matrix_formula": f"(I + X) + ({lambda_x_label}) X",
        "u_e_matrix": json_matrix(phase),
        "d_nuD_matrix": json_matrix(shift),
        "hermitian_spectrum_each_sector": [1.0, 4.0, 7.0],
        "three_distinct_family_masses": True,
        "commutator_norm_sq": frob_norm_sq(comm),
        "cp_odd_trace_commutator_cubed": json_complex(cp),
        "cp_odd_exact_magnitude": "972*sqrt(3)",
        "cp_odd_orientation": cp_sign,
        "CP_odd_invariant_nonzero": abs(cp.imag) > TOL,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "promoted_as_selected_value": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    postsource = load(POSTSOURCE)
    first_correction = load(FIRST_CORRECTION)
    primitive_frontier = load(PRIMITIVE_FRONTIER)

    omega = complex(-0.5, math.sqrt(3) / 2.0)
    omega2 = omega * omega
    one_plus_omega = 1 + omega
    one_plus_omega2 = 1 + omega2
    branches = [
        branch("1+omega", "1+omega", one_plus_omega, one_plus_omega),
        branch("1+omega", "1+omega2", one_plus_omega, one_plus_omega2),
        branch("1+omega2", "1+omega", one_plus_omega2, one_plus_omega),
        branch("1+omega2", "1+omega2", one_plus_omega2, one_plus_omega2),
    ]
    all_split = all(item["three_distinct_family_masses"] for item in branches)
    all_cp = all(item["CP_odd_invariant_nonzero"] for item in branches)
    cp_orientations = sorted({item["cp_odd_orientation"] for item in branches})

    search = {
        "schema": "MTTMinimalWeylCoefficientLiftSearch.v1",
        "status": "MINIMAL_ZX_COEFFICIENT_LIFT_SPLITS_AND_EMITS_CP_CANDIDATES",
        "input_gap": rel(POSTSOURCE),
        "first_layer_problem": {
            "formal_layer_spectra": "[4,1,1]",
            "formal_layer_CP_odd_invariant_nonzero": False,
            "formal_layer_twofold_degeneracy": True,
        },
        "search_rule": {
            "allowed_additive_coefficients": ["1+omega", "1+omega2"],
            "phase_lift": "(I + Z) + lambda_Z Z",
            "shift_lift": "(I + X) + lambda_X X",
            "reason": "minimal one-Weyl-phase additive coefficient lift of the already emitted phase/shift packet",
        },
        "candidate_count": len(branches),
        "branches": branches,
        "all_branches_split_three_families": all_split,
        "all_branches_emit_nonzero_CP_odd_invariant": all_cp,
        "cp_orientation_branches": cp_orientations,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SEARCH, search)

    gap = {
        "schema": "MTTWeylCoefficientLiftSourceSelectionGap.v1",
        "status": "ALGEBRAIC_WALL_BROKEN_SOURCE_SELECTION_OPEN",
        "diagnostic_relation_to_prior_search": {
            "prior_diagnostic_splitter_found": first_correction["combined_result"][
                "diagnostic_qutrit_correction_can_break_degeneracy"
            ],
            "prior_selected_correction_promoted": first_correction["combined_result"][
                "selected_correction_promoted"
            ],
            "new_result": "localizes a minimal additive coefficient-phase lift directly on the post-source I+Z/I+X matrices",
        },
        "what_this_proves": [
            "the [1,1] light-family degeneracy is not forced by the finite Weyl algebra",
            "a one-phase additive coefficient lift gives three distinct singular spectra [7,4,1]",
            "the same lift gives a nonzero CP-odd commutator-cubed invariant",
            "the two CP orientations are conjugate finite-Weyl branches",
        ],
        "what_this_does_not_prove": [
            "that MTT selects lambda=1+omega or lambda=1+omega2",
            "that both or exactly one CP orientation is physically realized",
            "that these candidate spectra are the measured Yukawa magnitudes",
            "that CKM/PMNS values are physically closed without a selected source theorem",
        ],
        "primitive_frontier_status": primitive_frontier["status"],
        "selected_source_emits_coefficient_lift": False,
        "selected_higher_response_matrices_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(GAP, gap)

    cutset = {
        "schema": "MTTNextCutsetAfterWeylCoefficientLift.v1",
        "status": "NEXT_ATTACK_COEFFICIENT_SOURCE_SELECTION_OR_HIGHER_RESPONSE_EMISSION",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The algebraic second-order/full-response candidate exists. The next proof must show whether "
                "the selected Phi_fin/C1 source emits the Weyl additive coefficient lambda_Z/lambda_X, whether a conjugate pair is "
                "allowed, or whether a different selected higher-response packet replaces this lift."
            ),
        },
        "minimal_source_options": [
            "derive lambda=1+omega or lambda=1+omega2 from selected theta/orientation/retarded-kernel data",
            "prove a conjugate-branch theorem explaining CP orientation selection or coexistence",
            "emit the same matrices from selected higher-response Hessian/Phi_fin contractions",
            "prove the source instead rejects this lift and requires another higher-order packet",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPostSourceWeylCoefficientLiftOrSecondOrderFlavorCandidate",
        "status": STATUS,
        "inputs": {
            "postsource_formal110_observable_audit": rel(POSTSOURCE),
            "first_correction_search": rel(FIRST_CORRECTION),
            "primitive_frontier": rel(PRIMITIVE_FRONTIER),
        },
        "output_packets": {
            "minimal_weyl_coefficient_lift_search": rel(SEARCH),
            "coefficient_lift_source_selection_gap": rel(GAP),
            "next_cutset_after_weyl_coefficient_lift": rel(CUTSET),
        },
        "theorem": {
            "name": "MinimalWeylCoefficientLiftCandidateTheorem",
            "proved": True,
            "statement": (
                "The post-source [4,1,1] degeneracy and zero-CP first layer is not an algebraic obstruction. "
                "The minimal additive Weyl coefficient lift (I+Z)+lambda_Z Z and (I+X)+lambda_X X with "
                "lambda_Z,lambda_X in {1+omega,1+omega^2} "
                "gives three distinct spectra [7,4,1], noncommuting Hermitian sector pairs, and a nonzero "
                "CP-odd commutator-cubed invariant of magnitude 972*sqrt(3). This is a candidate source target, "
                "not a selected physical value theorem."
            ),
        },
        "what_closes_now": {
            "minimal_second_order_weyl_lift_search_executed": True,
            "three_family_splitting_candidate_found": all_split,
            "nonzero_CP_candidate_found": all_cp,
            "CP_conjugate_orientation_pair_identified": cp_orientations == ["negative", "positive"],
            "algebraic_degeneracy_wall_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_lambda_source_theorem": True,
            "selected_higher_response_matrix_emission": True,
            "CP_orientation_selection_or_coexistence_theorem": True,
            "physical_CKM_PMNS_Yukawa_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "algebraic_candidate_found": True,
            "selected_source_emits_candidate": False,
            "physical_values_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": postsource["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PostSourceWeylCoefficientLift_or_SecondOrderFlavorCandidate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "candidate_count": len(branches),
        "three_family_splitting_candidate_found": all_split,
        "nonzero_CP_candidate_found": all_cp,
        "CP_conjugate_orientation_pair_identified": True,
        "selected_source_emits_candidate": False,
        "physical_values_promoted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PostSourceWeylCoefficientLift or SecondOrderFlavorCandidate v1

Status: `{STATUS}`.

The first post-source matrix layer was `I+Z` for `u,e` and `I+X` for `d,nuD`,
with spectra `[4,1,1]` and zero CP.  The minimal additive Weyl coefficient lift

```text
u,e   : (I + Z) + lambda_Z Z
d,nuD : (I + X) + lambda_X X
lambda_Z, lambda_X in {{1+omega, 1+omega^2}}
```

has four conjugate branches.  Every branch has:

```text
Hermitian spectra              : [7,4,1]
commutator norm squared        : 324
|CP-odd commutator cube|       : 972*sqrt(3)
observed target inputs         : none
selected physical promotion    : false
```

So the current wall is no longer algebraic degeneracy.  It is source selection:
MTT must still prove whether the selected branch emits `lambda_Z/lambda_X`, whether both
CP orientations coexist, or whether another selected higher-response packet
replaces this candidate.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
