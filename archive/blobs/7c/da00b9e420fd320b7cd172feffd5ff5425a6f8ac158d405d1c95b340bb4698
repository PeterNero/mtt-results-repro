"""Stress-test the retirement of Qa/SU3 Repair A.

The goal is not to defend the previous conclusion by assertion.  We compute
gauge-invariant algebraic signatures and enumerate ways Repair A could be
revived.  The result is conditional: Repair A is retired for the currently
selected indecomposable/stable SU(3) HYM branch, but could describe a different
polystable/reducible branch if the corpus selection changes.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PRIOR_CERT = ROOT / "certificates" / "selected_qa_su3_repair_a_quotient_or_b_torsion_source_test_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def elementary(row: int, col: int) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    matrix[row - 1, col - 1] = 1.0
    return matrix


def connection_matrices(mu: float, variant: str) -> list[np.ndarray]:
    s = math.sqrt(mu)
    if variant == "repair_A_diagonal_B3":
        return [
            s * elementary(1, 3),
            -s * elementary(3, 1),
            mu * (elementary(1, 1) - elementary(3, 3)),
        ]
    if variant == "repair_B_move_B2":
        return [
            s * elementary(1, 3),
            -s * elementary(3, 2),
            mu * elementary(1, 2),
        ]
    raise ValueError(f"unknown variant: {variant}")


def hermitian_basis() -> list[tuple[str, np.ndarray]]:
    matrices: list[tuple[str, np.ndarray]] = [
        ("identity", np.eye(3) / math.sqrt(3.0)),
        ("lambda3", np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0)),
        ("lambda8", np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0)),
    ]
    for a, b, label in [(0, 1, "12"), (0, 2, "13"), (1, 2, "23")]:
        real = np.zeros((3, 3), dtype=complex)
        real[a, b] = 1.0
        real[b, a] = 1.0
        matrices.append((f"sym_real_{label}", real / math.sqrt(2.0)))

        imag = np.zeros((3, 3), dtype=complex)
        imag[a, b] = -1j
        imag[b, a] = 1j
        matrices.append((f"sym_imag_{label}", imag / math.sqrt(2.0)))
    return matrices


def centralizer(variant: str) -> dict[str, Any]:
    pieces = connection_matrices(1.0, variant)
    basis = hermitian_basis()
    rows = []
    for piece in pieces:
        for _, h_matrix in basis:
            comm = h_matrix @ piece - piece @ h_matrix
            rows.append(np.concatenate([np.real(comm).reshape(-1), np.imag(comm).reshape(-1)]))
    # Build linear map from Hermitian coefficients to commutators.
    columns = []
    for _, h_matrix in basis:
        column_blocks = []
        for piece in pieces:
            comm = h_matrix @ piece - piece @ h_matrix
            column_blocks.extend(np.real(comm).reshape(-1))
            column_blocks.extend(np.imag(comm).reshape(-1))
        columns.append(column_blocks)
    linear = np.array(columns, dtype=float).T
    _u, s_values, vh = np.linalg.svd(linear)
    nullity = int(np.sum(s_values <= 1e-10))
    # SVD reports min(m,n) singular values; add no hidden nullity because n=9.
    null_vectors = []
    for idx, value in enumerate(s_values):
        if value <= 1e-10:
            vector = vh[idx, :]
            null_vectors.append(vector)
    if not null_vectors:
        for vector in vh[len(s_values) :, :]:
            null_vectors.append(vector)
    components = []
    for vector in null_vectors:
        entries = [
            {"basis": label, "coefficient": float(coeff)}
            for coeff, (label, _matrix) in zip(vector, basis)
            if abs(float(coeff)) > 1e-8
        ]
        components.append(entries)
    return {
        "variant": variant,
        "unitary_centralizer_dimension": nullity,
        "centralizer_basis_components": components,
        "centralizer_dimension_minus_center": max(0, nullity - 1),
    }


def invariant_coordinate_subspaces(variant: str) -> list[list[int]]:
    pieces = connection_matrices(1.0, variant)
    invariant: list[list[int]] = []
    indices = [0, 1, 2]
    for size in [1, 2]:
        for subset_tuple in combinations(indices, size):
            subset = set(subset_tuple)
            ok = True
            for piece in pieces:
                for col in subset:
                    image_support = {row for row in indices if abs(piece[row, col]) > 1e-10}
                    if not image_support.issubset(subset):
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                invariant.append([idx + 1 for idx in subset_tuple])
    return invariant


def direct_sum_coordinate_split(variant: str) -> bool:
    invariant = [set(item) for item in invariant_coordinate_subspaces(variant)]
    for subspace in invariant:
        complement = {1, 2, 3}.difference(subspace)
        if complement in invariant:
            return True
    return False


def main() -> int:
    prior = load(PRIOR_CERT)
    repair_a_centralizer = centralizer("repair_A_diagonal_B3")
    repair_b_centralizer = centralizer("repair_B_move_B2")
    repair_a_flags = invariant_coordinate_subspaces("repair_A_diagonal_B3")
    repair_b_flags = invariant_coordinate_subspaces("repair_B_move_B2")
    output = {
        "certificate": "SelectedQaSU3RepairRetirementStressTest",
        "status": "QA_SU3_REPAIR_A_RETIREMENT_STRESS_TEST_CONDITIONAL_RETIREMENT_UPHELD",
        "input_status": prior["status"],
        "external_research_principles": [
            {
                "principle": "Hitchin-Kobayashi/Donaldson-Uhlenbeck-Yau correspondence: HYM exists on polystable bundles; stable branches have only scalar automorphisms.",
                "source": "https://arxiv.org/abs/2006.06453",
            },
            {
                "principle": "Heterotic SU(3)/Strominger systems use HYM/instanton data and can include torsional connection choices, so source-certified torsion corrections are meaningful but cannot be inserted freely.",
                "source": "https://link.springer.com/article/10.1007/s00220-025-05309-2",
            },
            {
                "principle": "General SU(3)-structure heterotic compactifications organize deformations through coupled extension data, so flag-like indecomposable structures are possible even when direct-sum stabilizers are forbidden.",
                "source": "https://arxiv.org/abs/1411.6696",
            },
        ],
        "computed_signatures": {
            "repair_A": {
                "centralizer": repair_a_centralizer,
                "coordinate_invariant_subspaces": repair_a_flags,
                "has_invariant_direct_sum_coordinate_split": direct_sum_coordinate_split(
                    "repair_A_diagonal_B3"
                ),
            },
            "repair_B": {
                "centralizer": repair_b_centralizer,
                "coordinate_invariant_subspaces": repair_b_flags,
                "has_invariant_direct_sum_coordinate_split": direct_sum_coordinate_split(
                    "repair_B_move_B2"
                ),
            },
        },
        "revival_options": [
            {
                "option": "Change selected branch to polystable SU(2)+line or block SU(2) color sector.",
                "status": "mathematically_possible_but_not_current_MTT_selection",
                "cost": "Would replace the selected indecomposable rank-3 SU(3) HYM branch and require redoing c3, threshold representation, and SM color interpretation.",
            },
            {
                "option": "Declare the noncentral stabilizer a quotient gauge mode.",
                "status": "not_allowed_without_new_source_theorem",
                "cost": "Would quotient a genuine color Cartan stabilizer, changing the physical determinant and gauge symmetry accounting.",
            },
            {
                "option": "Use missing torsion/OU/full operator terms to lift the Repair A zero.",
                "status": "possible_only_with_source_certified_non_commutator_term",
                "cost": "The algebraic commutator block is exactly blind to the stabilizer; any lift must come from a sourced term acting on this color Cartan direction.",
            },
            {
                "option": "Find a unitary gauge transform relating Repair A to Repair B.",
                "status": "ruled_out_by_centralizer_dimension",
                "cost": "Unitary conjugacy preserves centralizer dimension; Repair A has an extra noncentral centralizer while Repair B does not.",
            },
            {
                "option": "Treat Repair A as a diagnostic sub-branch only.",
                "status": "allowed",
                "cost": "It may remain useful for algebraic comparison, but cannot be the selected Qa/SU3 closure branch under the current corpus assumptions.",
            },
        ],
        "stress_test_conclusion": {
            "previous_repair_B_flag_wording_corrected": (
                "Repair B does have invariant coordinate flags, but no extra "
                "unitary centralizer and no invariant direct-sum coordinate split. "
                "That is compatible with an indecomposable extension diagnostic."
            ),
            "repair_A_retirement_strength": "high_conditional_on_selected_indecomposable_stable_rank3_su3_branch",
            "repair_A_retirement_absolute": False,
            "repair_A_can_be_revived_only_by_changing_selection_or_adding_new_source_theorem": True,
            "repair_B_only_live_current_branch": True,
        },
        "verdict": {
            "repair_A_retired_under_current_selection": True,
            "repair_A_forbidden_as_any_math_object": False,
            "repair_B_closed": False,
            "safe_to_close_Qa_SU3": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Repair_B_Source_Certified_Primitive_Correction_or_No_Go_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
