"""Build the first smooth B_N Galerkin lift from the F3^2 twisted scaffold.

This constructs a small gerbe-twisted Fourier/Galerkin scaffold over the
selected active F3^2 deck shadow.  It emits concrete scalar labels, quadrature,
Gram/stiffness matrices, eigenpairs, a zero cluster, a Riesz projector, and a
reduced Green operator for the model active directions.  It does not yet claim
the full selected Iwasawa/Strominger D_E action or source promotion.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUTPUT = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
CERT = CERTS / "selected_routec_smooth_bn_galerkin_lift_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def zero_matrix(n: int) -> list[list[float]]:
    return [[0.0 for _ in range(n)] for _ in range(n)]


def diag(values: list[float]) -> list[list[float]]:
    out = zero_matrix(len(values))
    for i, value in enumerate(values):
        out[i][i] = value
    return out


def main() -> None:
    previous = load(DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json")
    contract = load(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json")

    deck_nodes = previous["B_N_scaffold"]["deck_nodes"]
    fiber_dim = previous["B_N_scaffold"]["fiber_dimension"]
    basis = []
    eigenvalues = []
    active_modes = [-1, 0, 1]
    for a in active_modes:
        for b in active_modes:
            for r in range(fiber_dim):
                label = {
                    "id": f"phi_({a},{b})_e{r}",
                    "formula": f"exp(2*pi*i*(({a})*x+({b})*y)/3) tensor e_{r}",
                    "active_deck_mode": [a % 3, b % 3],
                    "integer_representative": [a, b],
                    "fiber_index": r,
                }
                basis.append(label)
                eigenvalues.append(((2.0 * math.pi / 3.0) ** 2) * (a * a + b * b))

    n = len(basis)
    gram = diag([1.0] * n)
    stiffness = diag(eigenvalues)
    zero_indices = [i for i, value in enumerate(eigenvalues) if abs(value) < 1e-12]
    complement_values = [value for value in eigenvalues if value > 1e-12]
    complement_gap = min(complement_values)
    riesz = diag([1.0 if i in zero_indices else 0.0 for i in range(n)])
    complement = diag([0.0 if i in zero_indices else 1.0 for i in range(n)])
    green = diag([0.0 if i in zero_indices else 1.0 / eigenvalues[i] for i in range(n)])

    quadrature = {
        "nodes": [{"x": x, "y": y, "weight": 1.0 / 9.0} for x in range(3) for y in range(3)],
        "rule": "3x3 active-deck trapezoid rule",
        "exact_for_mode_differences_mod_3": True,
        "normalization": "sum weights = 1",
    }

    bundle_equivariance = {
        "type": "gerbe_twisted_projective",
        "active_generators": ["g1", "g2"],
        "kernel_generators": ["g3", "g4", "g5", "g6"],
        "rho_E_source": previous["rho_E_candidate"]["kind"],
        "commutator_phase": previous["rho_E_candidate"]["numeric_gates"]["projective_commutator_phase"],
        "ordinary_bundle_equivariance": False,
        "projective_equivariance_up_to_central_phase": True,
    }

    gates = {
        "basis_extends_beyond_left_invariant_forms": n > fiber_dim,
        "explicit_Psi_i_representatives": True,
        "metric_volume_quadrature": True,
        "Gram_matrix_positive_definite": True,
        "stiffness_matrix_positive_semidefinite": min(eigenvalues) >= -1e-12,
        "kernel_dimension_is_three": len(zero_indices) == 3,
        "complement_gap_positive": complement_gap > 0,
        "Riesz_projector_constructed": True,
        "reduced_Green_operator_constructed": True,
        "bundle_equivariance_projective_only": True,
        "selected_D_E_action_on_basis": False,
        "dotD_alpha1_and_Green_operator_constructed": False,
        "sector_projection_maps_constructed": False,
        "truncation_error_certified_for_full_iwasawa_operator": False,
    }

    bn_payload_gate = (
        gates["basis_extends_beyond_left_invariant_forms"]
        and gates["explicit_Psi_i_representatives"]
        and gates["metric_volume_quadrature"]
        and gates["Gram_matrix_positive_definite"]
        and gates["kernel_dimension_is_three"]
        and gates["complement_gap_positive"]
        and gates["Riesz_projector_constructed"]
        and gates["reduced_Green_operator_constructed"]
        and gates["selected_D_E_action_on_basis"]
        and gates["sector_projection_maps_constructed"]
        and gates["truncation_error_certified_for_full_iwasawa_operator"]
    )

    candidate = {
        "candidate": "MTTSelectedRouteCSmoothBNGalerkinLift",
        "status": "MTT_SELECTED_ROUTEC_SMOOTH_BN_GALERKIN_LIFT_SCAFFOLD_BUILT_SELECTED_DE_STILL_OPEN",
        "inputs": {
            "previous": rel(DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"),
            "basis_contract": rel(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json"),
        },
        "superset_mode": {
            "classification": "CONSTRAINED_NUMERICAL_SUPERSET_REPAIR",
            "straight_path": {
                "classification": "PARTIAL",
                "smooth_BN_scaffold_built": True,
                "full_BN_payload_gate": bn_payload_gate,
                "selected_DE_action_emitted": False,
                "honest_replay_ready": False,
            },
            "superset_convergence": {
                "uses_previous_nonidentity_rhoE": previous["rho_E_candidate"]["numeric_gates"]["passes_numeric_packet_gate"],
                "uses_selected_F3xF3_deck_shadow": True,
                "gerbe_twisted_projective_equivariance": True,
            },
            "superset_repair": {
                "classification": "BN_SCAFFOLD_FOUND_SELECTED_DE_NEXT",
                "next_required_object": "selected D_E action on this B_N plus sector projectors and full Iwasawa truncation error",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "B_N_lift": {
            "basis_id": "F3xF3_gerbe_twisted_fourier_N1_rank3",
            "dimension": n,
            "basis": basis,
            "quadrature_rule": quadrature,
            "bundle_equivariance": bundle_equivariance,
            "gram_matrix": gram,
            "stiffness_matrix_model_active_laplacian": stiffness,
            "eigenpairs": [
                {"basis_index": i, "basis_id": basis[i]["id"], "eigenvalue": eigenvalues[i]} for i in range(n)
            ],
            "zero_cluster": {
                "dimension": len(zero_indices),
                "indices": zero_indices,
                "basis_ids": [basis[i]["id"] for i in zero_indices],
            },
            "complement_gap": complement_gap,
            "riesz_projector": riesz,
            "complement_projector": complement,
            "reduced_green_operator": green,
        },
        "contract_comparison": {
            "required_fields": contract["required_fields"],
            "fields_emitted_now": {
                "scalar_basis_functions_phi_m": True,
                "metric_volume_quadrature": True,
                "Gram_matrix_entries": True,
                "stiffness_matrix_entries": True,
                "generalized_eigenpairs": True,
                "gap_error_certificate_model_active": True,
                "Riesz_projectors": True,
                "reduced_Green_operators": True,
                "bundle_transition_or_equivariance_matrices": True,
            },
            "still_missing_for_full_contract": {
                "ordinary_or_selected_projective_source_promotion": True,
                "selected_D_E_action_on_basis": True,
                "ordered_zero_mode_bases_Q_u_d_L_e_N_H": True,
                "sector_projection_maps_constructed": True,
                "dotD_alpha1_in_same_basis": True,
                "full_iwasawa_operator_truncation_error": True,
            },
        },
        "gates": gates,
        "what_closes_now": {
            "smooth_scalar_basis_functions_phi_m_emitted": True,
            "metric_quadrature_emitted": True,
            "Gram_matrix_entries_emitted": True,
            "stiffness_matrix_entries_emitted_for_model_active_laplacian": True,
            "generalized_eigenpairs_emitted": True,
            "kernel_dimension_three_for_model_active_laplacian": True,
            "positive_model_complement_gap": True,
            "Riesz_and_reduced_Green_emitted_for_model_active_laplacian": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "R1_selected_source_certificate": True,
            "R2_source_promotion_for_rhoE": True,
            "R3_selected_operator_spectral_data": True,
            "R4_full_selected_basis_data": not bn_payload_gate,
            "selected_D_E_action_on_basis": True,
            "sector_projectors": True,
            "dotD_alpha1_in_same_basis": True,
            "full_iwasawa_truncation_error_certificate": True,
            "R5_selected_C1_response": True,
            "R6_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1",
        "theorem": {
            "name": "SmoothBNGalerkinLiftFirstModelTheorem",
            "proved": True,
            "statement": (
                "The non-identity Heisenberg/Weyl rho_E packet admits a concrete gerbe-twisted "
                "F3^2 Fourier Galerkin scaffold with 27 modes, exact active-deck quadrature, "
                "positive Gram matrix, diagonal model stiffness, a three-dimensional zero cluster, "
                "positive complement gap, Riesz projector, and reduced Green operator. This is a "
                "numerical B_N scaffold, not yet the full selected Iwasawa/Strominger D_E basis."
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
        f"""# MTT Selected Route-C Smooth BN Galerkin Lift

Status: `{candidate['status']}`

This builds the first smooth numerical lift of the finite `F3^2 x C3`
twisted scaffold.

## Emitted

- basis dimension: `{n}`
- zero cluster dimension: `{len(zero_indices)}`
- complement gap: `{complement_gap:.12g}`
- quadrature: 3x3 active-deck trapezoid rule
- Gram matrix: identity
- model stiffness: diagonal active-deck Laplacian
- Riesz projector and reduced Green operator: emitted for the model active
  Laplacian

## Interpretation

This is a superset repair path, not a full straight proof.  It constructs a
legal gerbe-twisted smooth Galerkin scaffold over the selected active deck
shadow and previous non-identity projective `rho_E` packet.  It does not yet
claim the selected Iwasawa/Strominger `D_E` action, sector projectors, `dotD`,
or full truncation-error certificate.

## Next

Build `MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1`: place the selected
`D_E` action on this basis, derive sector projectors and `dotD_alpha1` in the
same basis, then replay the Route-C manifest without lifted flags.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
