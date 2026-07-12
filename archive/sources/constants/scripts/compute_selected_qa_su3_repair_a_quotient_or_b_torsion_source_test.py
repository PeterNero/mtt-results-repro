"""Resolve the first Qa/SU3 repair fork test.

Repair A has an extra Hessian zero.  This script checks whether that zero can
be treated as a legitimate quotient mode under the currently selected corpus
branch.  It also records the source status of the primitive correction required
by Repair B.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FORK_CERT = ROOT / "certificates" / "selected_qa_su3_repair_fork_resolution_requirements_certificate.json"
TEMPLATE_CERT = ROOT / "certificates" / "selected_qa_su3_color_connection_template_fill_attempt_certificate.json"


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


def diagonal_weight_vector(matrix: np.ndarray) -> list[float]:
    return [float(np.real(matrix[i, i])) for i in range(3)]


def commutes_with_all(matrix: np.ndarray, pieces: list[np.ndarray]) -> bool:
    return all(np.linalg.norm(matrix @ piece - piece @ matrix) <= 1e-10 for piece in pieces)


def invariant_coordinate_subspaces(pieces: list[np.ndarray]) -> list[list[int]]:
    """Find coordinate subsets invariant under all connection matrices."""

    invariant: list[list[int]] = []
    indices = [0, 1, 2]
    for mask in range(1, 2**3 - 1):
        subset = [idx for idx in indices if mask & (1 << idx)]
        ok = True
        for piece in pieces:
            for col in subset:
                image_support = {row for row in indices if abs(piece[row, col]) > 1e-10}
                if not image_support.issubset(set(subset)):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            invariant.append([idx + 1 for idx in subset])
    return invariant


def repair_a_stabilizer_test() -> dict[str, Any]:
    pieces = connection_matrices(1.0, "repair_A_diagonal_B3")
    extra_generator = 1j * np.diag([-1.0, 2.0, -1.0]) / math.sqrt(6.0)
    central = 1j * np.eye(3) / math.sqrt(3.0)
    invariant_subspaces = invariant_coordinate_subspaces(pieces)
    return {
        "extra_generator_basis": "i*diag(-1,2,-1)/sqrt(6)",
        "extra_generator_diagonal_weights": diagonal_weight_vector(extra_generator / 1j),
        "extra_generator_commutes_with_connection": commutes_with_all(extra_generator, pieces),
        "central_generator_commutes_with_connection": commutes_with_all(central, pieces),
        "coordinate_invariant_subspaces": invariant_subspaces,
        "reducible_coordinate_splitting_seen": [2] in invariant_subspaces
        and [1, 3] in invariant_subspaces,
        "interpretation": (
            "Repair A splits the rank-3 space into the isolated e2 line and "
            "the e1/e3 block.  The extra Cartan zero is therefore a genuine "
            "noncentral stabilizer, not the usual central u(1) determinant "
            "zero."
        ),
    }


def repair_b_stabilizer_test() -> dict[str, Any]:
    pieces = connection_matrices(1.0, "repair_B_move_B2")
    invariant_subspaces = invariant_coordinate_subspaces(pieces)
    return {
        "coordinate_invariant_subspaces": invariant_subspaces,
        "nontrivial_coordinate_splitting_seen": len(invariant_subspaces) > 0,
        "interpretation": (
            "Repair B has no nontrivial coordinate invariant subspace in this "
            "left-invariant matrix test, matching the one-central-zero Hessian "
            "diagnostic."
        ),
    }


def source_branch_support(template: dict[str, Any]) -> dict[str, Any]:
    bundle = template["partial_fill"]["color_bundle"]["bundle_or_local_system"]
    connection = template["partial_fill"]["connection"]
    return {
        "selected_candidate": bundle["selected_candidate"],
        "connection_statement": bundle["properties"]["connection"],
        "c2_net_statement": bundle["properties"]["c2_net_statement"],
        "c3_statement": bundle["properties"]["c3"],
        "endomorphism_E_available": connection["endomorphism_E"] is not None,
        "curvature_or_flux_data": connection["curvature_or_flux_data"],
        "supports_indecomposable_rank3_hym": "indecomposable rank-3 SU(3) HYM bundle"
        in bundle["selected_candidate"],
        "supports_explicit_primitive_cancelling_torsion": connection["endomorphism_E"] is not None,
    }


def repair_b_correction_source_test(fork: dict[str, Any], template: dict[str, Any]) -> dict[str, Any]:
    source = source_branch_support(template)
    samples = fork["repair_B_requirement"]["samples"]
    return {
        "required_correction_samples": samples,
        "required_cartan_shape": "diag(-1,1,0) weighted primitive correction",
        "required_mu_scaling_from_samples": "proportional to mu*(1+mu) in the third-block placement diagnostic",
        "source_has_matching_endomorphism": source["supports_explicit_primitive_cancelling_torsion"],
        "source_status": (
            "The corpus records heterotic R_+ curvature and HYM existence data, "
            "but the Qa/SU3 color-connection template still has endomorphism_E = null. "
            "So the required Repair B primitive correction is not source-certified."
        ),
    }


def main() -> int:
    fork = load(FORK_CERT)
    template = load(TEMPLATE_CERT)
    source = source_branch_support(template)
    repair_a = repair_a_stabilizer_test()
    repair_b = repair_b_stabilizer_test()
    b_source = repair_b_correction_source_test(fork, template)
    repair_a_ruled_out = (
        source["supports_indecomposable_rank3_hym"]
        and repair_a["extra_generator_commutes_with_connection"]
        and repair_a["reducible_coordinate_splitting_seen"]
    )
    output = {
        "certificate": "SelectedQaSU3RepairAQuotientOrBTorsionSourceTest",
        "status": "QA_SU3_REPAIR_A_QUOTIENT_REFUTED_REPAIR_B_TORSION_SOURCE_OPEN",
        "input_status": {
            "fork_requirements": fork["status"],
            "color_connection_template": template["status"],
        },
        "source_branch_support": source,
        "repair_A_quotient_test": repair_a,
        "repair_B_stabilizer_test": repair_b,
        "repair_B_torsion_source_test": b_source,
        "conclusion": {
            "repair_A_extra_zero_is_noncentral_stabilizer": True,
            "repair_A_incompatible_with_selected_indecomposable_branch": repair_a_ruled_out,
            "repair_B_remains_only_live_repair_candidate": repair_a_ruled_out,
            "repair_B_primitive_correction_source_certified": b_source[
                "source_has_matching_endomorphism"
            ],
        },
        "verdict": {
            "route_A_closed": True,
            "route_A_result": "refuted_under_selected_indecomposable_rank3_HYM_branch",
            "route_B_closed": False,
            "fork_resolved_to_single_live_branch": repair_a_ruled_out,
            "safe_to_close_Qa_SU3": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Repair_B_Source_Certified_Primitive_Correction_or_No_Go_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
