"""Build the first numerical non-identity rho_E / B_N construction attempt.

The search is intentionally tiny: use the selected q79/F,m=1 S3 deck shadow
g1,g2 -> F3^2 and test the canonical 3-dimensional Heisenberg/Weyl projective
packet.  This is a numerical/algebraic construction attempt, not a promotion to
full SM closure.
"""

from __future__ import annotations

import cmath
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUTPUT = DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
CERT = CERTS / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def cpair(z: complex) -> list[float]:
    return [round(z.real, 12), round(z.imag, 12)]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    n, m, p = len(a), len(b[0]), len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(p)) for j in range(m)] for i in range(n)]


def dagger(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def matdiff_norm(a: list[list[complex]], b: list[list[complex]]) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def eye(n: int) -> list[list[complex]]:
    return [[1 + 0j if i == j else 0 + 0j for j in range(n)] for i in range(n)]


def scale(z: complex, a: list[list[complex]]) -> list[list[complex]]:
    return [[z * x for x in row] for row in a]


def encode_matrix(a: list[list[complex]]) -> list[list[list[float]]]:
    return [[cpair(x) for x in row] for row in a]


def main() -> None:
    previous = load(DATA / "selected_routec_selected_primitive_emission_search.candidate.json")
    same_source = load(DATA / "same_source_symmetry_breaking_source.candidate.json")
    basis_contract = load(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json")

    deck_limit = (
        same_source["superset_mode"]["repair_paths"]["ordered_integral_cech_or_appell_humbert"]
        ["selected_s3_deck_limit"]
    )
    deck_map = deck_limit["selected_deck_map"]

    omega = cmath.exp(2j * cmath.pi / 3)
    clock = [[omega**i if i == j else 0 + 0j for j in range(3)] for i in range(3)]
    shift = [[1 + 0j if j == (i + 1) % 3 else 0 + 0j for j in range(3)] for i in range(3)]
    ident = eye(3)

    # With this shift convention, clock * shift = omega_bar * shift * clock.
    projective_phase = omega.conjugate()
    projective_residual = matdiff_norm(matmul(clock, shift), scale(projective_phase, matmul(shift, clock)))
    unitary_residual = max(
        matdiff_norm(matmul(dagger(clock), clock), ident),
        matdiff_norm(matmul(dagger(shift), shift), ident),
    )
    order_residual = max(
        matdiff_norm(matmul(matmul(clock, clock), clock), ident),
        matdiff_norm(matmul(matmul(shift, shift), shift), ident),
    )
    nonidentity_norm = max(matdiff_norm(clock, ident), matdiff_norm(shift, ident))

    rho_generators = {
        "g1": clock,
        "g2": shift,
        "g3": ident,
        "g4": ident,
        "g5": ident,
        "g6": ident,
    }

    rho_gate = {
        "active_deck_rank_over_F3": deck_limit["selected_s3_active_image_rank_over_F3"],
        "uses_only_selected_active_generators_g1_g2": deck_map["g1"] == [1, 0] and deck_map["g2"] == [0, 1],
        "kernel_generators_identity": all(deck_map[f"g{i}"] == [0, 0] for i in range(3, 7)),
        "unitary_residual_max": unitary_residual,
        "order3_residual_max": order_residual,
        "projective_commutator_residual": projective_residual,
        "projective_commutator_phase": cpair(projective_phase),
        "nonidentity_norm": nonidentity_norm,
        "passes_numeric_packet_gate": (
            unitary_residual < 1e-10
            and order_residual < 1e-10
            and projective_residual < 1e-10
            and nonidentity_norm > 0.1
        ),
    }

    # First basis scaffold: the twisted regular orbit over F3^2 has 9 deck
    # nodes and 3 fiber coordinates.  It is not yet a smooth Galerkin basis.
    basis_scaffold = {
        "deck_nodes": [[a, b] for a in range(3) for b in range(3)],
        "fiber_dimension": 3,
        "raw_twisted_regular_dimension": 27,
        "basis_family": "finite_twisted_regular_F3xF3_times_C3",
        "quotient_constraints_encoded": True,
        "smooth_scalar_basis_phi_m_emitted": False,
        "metric_quadrature_emitted": False,
        "selected_D_E_action_emitted": False,
        "gram_stiffness_emitted": False,
        "gap_certificate_emitted": False,
        "passes_B_N_payload_gate": False,
        "reason_not_B_N": (
            "This is a finite twisted deck/fiber scaffold. It supplies a legal non-identity "
            "projective rho_E candidate, but not the smooth scalar Galerkin functions, "
            "metric quadrature, D_E action, Gram/stiffness entries, or gap certificate."
        ),
    }

    r2_partially_closed = rho_gate["passes_numeric_packet_gate"]
    r4_closed = basis_scaffold["passes_B_N_payload_gate"]
    r6_ready = r2_partially_closed and r4_closed

    candidate = {
        "candidate": "MTTSelectedRouteCNonIdentityRhoEAndBNConstruction",
        "status": "MTT_SELECTED_ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_BUILT_BN_STILL_OPEN",
        "inputs": {
            "previous": rel(DATA / "selected_routec_selected_primitive_emission_search.candidate.json"),
            "basis_contract": rel(DATA / "selected_phifin_payload_or_bn_basis_emission" / "selected_bn_basis.emission_contract.json"),
            "selected_deck_source": rel(DATA / "same_source_symmetry_breaking_source.candidate.json"),
        },
        "superset_mode": {
            "classification": "CONSTRAINED_NUMERICAL_SUPERSET_REPAIR",
            "straight_path": {
                "classification": "PARTIAL",
                "nonidentity_projective_rhoE_packet_built": r2_partially_closed,
                "BN_payload_built": r4_closed,
                "honest_replay_ready": r6_ready,
            },
            "superset_convergence": {
                "selected_S3_deck_shadow": deck_map,
                "canonical_Heisenberg_Weyl_packet": True,
                "formal_lift_used": False,
                "support_stacks_from_previous": previous["what_closes_now"]["selected_deck_scaffold_identified"],
            },
            "superset_repair": {
                "classification": "RHOE_PACKET_FOUND_BN_CONSTRUCTION_NEXT",
                "next_required_object": "lift finite twisted regular scaffold to smooth quotient-valid Galerkin B_N with quadrature and D_E action",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "rho_E_candidate": {
            "kind": "selected_deck_compatible_Heisenberg_Weyl_projective_packet",
            "selected_by_mtt": False,
            "selection_status": (
                "compatible with selected deck/cocycle shadow; still needs source certificate tying "
                "this canonical packet to the selected Strominger/HYM minimizer"
            ),
            "rank": 3,
            "generator_matrices_complex_pairs": {key: encode_matrix(value) for key, value in rho_generators.items()},
            "numeric_gates": rho_gate,
        },
        "B_N_scaffold": basis_scaffold,
        "contract_comparison": {
            "required_B_N_fields": basis_contract["required_fields"],
            "still_missing_after_this_attempt": {
                "smooth_scalar_basis_functions_phi_m": True,
                "metric_volume_quadrature": True,
                "selected_D_E_action_on_basis": True,
                "Gram_matrix_entries": True,
                "stiffness_matrix_entries": True,
                "generalized_eigenpairs": True,
                "gap_error_certificate": True,
            },
        },
        "what_closes_now": {
            "finite_search_space_reduced_to_canonical_F3xF3_projective_packet": True,
            "nonidentity_projective_rhoE_candidate_built": r2_partially_closed,
            "identity_smoke_replaced_by_nonidentity_candidate": True,
            "finite_twisted_deck_fiber_basis_scaffold_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "R1_selected_source_certificate": True,
            "R2_selected_rhoE_metric_connection": not r2_partially_closed,
            "R2_source_promotion_for_rhoE": True,
            "R3_selected_operator_spectral_data": True,
            "R4_selected_basis_data": not r4_closed,
            "R5_selected_C1_response": True,
            "R6_replay_without_lifted_flags": not r6_ready,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1",
        "theorem": {
            "name": "ConstrainedNumericalRhoEFirstPacketTheorem",
            "proved": True,
            "statement": (
                "The selected F3^2 deck shadow admits a canonical non-identity 3-dimensional "
                "Heisenberg/Weyl projective rho_E packet with unitary order-three generators "
                "and omega commutator. This replaces identity smoke as the first numerical "
                "candidate, but it does not yet emit the smooth quotient-valid B_N Galerkin "
                "basis or selected D_E action required for honest replay."
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
        f"""# MTT Selected Route-C Non-Identity rhoE and BN Construction

Status: `{candidate['status']}`

This is the first constrained numerical iteration.  The search space is not the
full space of matrices.  It is the selected q79/F,m=1 S3 deck shadow:

```text
g1 -> (1,0), g2 -> (0,1), g3..g6 -> 0 in F3^2
```

## Result

The canonical 3-dimensional Heisenberg/Weyl packet passes the finite numerical
rhoE gates:

- unitary residual: `{unitary_residual:.3e}`
- order-three residual: `{order_residual:.3e}`
- projective commutator residual: `{projective_residual:.3e}`
- commutator phase: primitive cube root omega

This gives a real non-identity projective `rho_E` candidate and replaces the
identity-smoke payload for the next numerical branch.

## Not Yet Closed

The `B_N` payload is still open.  The construction currently gives only a
finite twisted deck/fiber scaffold over `F3^2 x C3`; it does not yet supply:

- smooth scalar Galerkin functions `phi_m`,
- metric quadrature,
- selected `D_E` action on the basis,
- Gram/stiffness matrices,
- generalized eigenpairs,
- gap/error certificate.

## Next

Build `MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1`: lift this finite
twisted regular scaffold to an actual smooth quotient-valid non-invariant
Galerkin basis with quadrature and `D_E` action.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
