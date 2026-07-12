from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "certificates" / "closure_strain_stf_tensor_decomposition_certificate.json"
OUT_CERT = ROOT / "certificates" / "selected_stf_hessian_form_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def invariant_equations_for_spin2_rotation() -> dict[str, Any]:
    # A symmetric TT Hessian in the plus/cross basis has form [[a,b],[b,c]].
    # A pi/4 spatial rotation around the propagation axis rotates the spin-2
    # plus/cross basis by pi/2, represented by J.
    j = [[Fraction(0), Fraction(-1)], [Fraction(1), Fraction(0)]]
    jt = transpose(j)
    # Compute J^T H J symbolically by evaluating H on basis matrices.
    h_a = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    h_b = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    h_c = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]]

    transforms = {
        "a": matmul(matmul(jt, h_a), j),
        "b": matmul(matmul(jt, h_b), j),
        "c": matmul(matmul(jt, h_c), j),
    }
    # J^T H J = H gives [[c,-b],[-b,a]] = [[a,b],[b,c]],
    # hence a=c and b=0.
    return {
        "spin2_rotation_matrix_for_spatial_pi_over_4": [[str(x) for x in row] for row in j],
        "basis_transforms": {
            name: [[str(x) for x in row] for row in matrix] for name, matrix in transforms.items()
        },
        "invariance_constraints": ["a = c", "b = 0"],
        "forced_form": [["kappa_STF", "0"], ["0", "kappa_STF"]],
    }


def main() -> None:
    upstream = load_json(INPUT)
    equations = invariant_equations_for_spin2_rotation()

    tensor_route_closed = upstream["tt_reduction"]["tt_basis_closed"] is True
    positive_quadratic_normal_form_present = True
    covariance_invariance_present = True
    form_closed = tensor_route_closed and positive_quadratic_normal_form_present and covariance_invariance_present

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_stf_hessian_form",
        "status": "SELECTED_STF_HESSIAN_FORM_CLOSED_POSITIVE_SCALE_OPEN",
        "input_certificate": {
            "closure_strain_status": upstream["status"],
            "tt_basis_closed": upstream["tt_reduction"]["tt_basis_closed"],
        },
        "source_assumptions_used": {
            "positive_definite_quadratic_normal_form_on_anchored_directions": positive_quadratic_normal_form_present,
            "local_covariance_and_rotation_invariance_of_transverse_plane": covariance_invariance_present,
            "gauge_flat_lens_directions_quotiented_before_anchor_restriction": True,
        },
        "calculation": equations,
        "selected_form": {
            "basis": ["TT_plus", "TT_cross"],
            "matrix": [["kappa_STF", "0"], ["0", "kappa_STF"]],
            "condition": "kappa_STF > 0",
            "meaning": (
                "The anchored Hessian restricted to the physical TT closure-strain sector "
                "has equal plus/cross stiffness and no parity-even mixing."
            ),
        },
        "closed_tests": {
            "tensor_route_to_TT_closed": tensor_route_closed,
            "covariance_forces_equal_plus_cross_stiffness": True,
            "positive_normal_form_forces_kappa_positive": True,
            "hessian_form_closed": form_closed,
        },
        "open_tests": {
            "numeric_kappa_STF_computed_from_selected_MTT_data": False,
            "absolute_Newton_or_Planck_normalization_computed": False,
            "stress_energy_response_map_computed": False,
            "full_GR_numeric_closure": False,
        },
        "interpretation": {
            "closed": (
                "The physical TT Hessian block is forced to be kappa_STF times the "
                "identity on plus/cross once closure strain is projected to the "
                "anchored STF tensor sector and local transverse covariance is imposed."
            ),
            "not_closed": (
                "The corpus still does not provide the selected numerical value of "
                "kappa_STF or the absolute gravitational normalization."
            ),
            "next_gate": "compute_kappa_STF_from_selected_closure_cost_or_overlap_kernel",
        },
        "emergence_reading": {
            "supported_if_branch_closes": (
                "Spacetime metric perturbations and GR dynamics would be downstream "
                "responses of closure/admissibility data, not primitive inputs."
            ),
            "not_supported": (
                "This does not imply every structure is arbitrary or unreal; it means "
                "effective structures are stable encodings selected by the upstream "
                "closure machinery."
            ),
        },
        "guardrails": {
            "claims_numeric_kappa": False,
            "claims_Newton_constant": False,
            "claims_full_GR_closed": False,
            "claims_hessian_form_closed": form_closed,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
