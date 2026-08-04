from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

Q79_INTERTWINER = ROOT / "certificates" / "q79_s3_strain_intertwiner_certificate.json"
EXACT_BRANCH = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"
HELICITY_FUNCTOR = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"
NO_GO = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"

OUT_CERT = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "World_in_World_Z64_Metric_Source_Map_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_exp_symmetric(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.exp(values)) @ vectors.T


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def main() -> None:
    q79 = load(Q79_INTERTWINER)
    exact = load(EXACT_BRANCH)
    helicity = load(HELICITY_FUNCTOR)
    no_go = load(NO_GO)

    n = 64
    k = 2
    theta = 2.0 * math.pi / n
    norm = math.sqrt(2.0 / n)
    c2 = np.array([norm * math.cos(k * theta * j) for j in range(n)])
    s2 = np.array([norm * math.sin(k * theta * j) for j in range(n)])
    u_tt = np.column_stack((c2, s2))

    shift = np.zeros((n, n))
    for j in range(n):
        shift[(j + 1) % n, j] = 1.0
    rotation2 = np.array(
        [
            [math.cos(k * theta), -math.sin(k * theta)],
            [math.sin(k * theta), math.cos(k * theta)],
        ]
    )

    e_plus = np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0)
    e_cross = np.array(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
    ) / math.sqrt(2.0)

    # The actual nonlinear candidate is
    #   S(psi)=<c2,psi> e_plus + <s2,psi> e_cross,
    #   Q(psi)=exp(S(psi)), G(psi)=Q(psi)^T Q(psi)=exp(2S(psi)).
    # Therefore the derivative in orthonormal TT coordinates is B=2 U_TT^T.
    b_metric = 2.0 * u_tt.T
    b_metric_star = b_metric.T
    b_log_strain = u_tt.T
    b_log_strain_star = b_log_strain.T

    projector_exact_plane = u_tt @ u_tt.T
    metric_support_residual = max_abs(
        projector_exact_plane @ b_metric_star - b_metric_star
    )
    strain_support_residual = max_abs(
        projector_exact_plane @ b_log_strain_star - b_log_strain_star
    )
    metric_c = u_tt.T @ b_metric_star
    strain_c = u_tt.T @ b_log_strain_star
    shift_intertwining_residual = max_abs(shift @ u_tt - u_tt @ rotation2)

    # Solve the real intertwiner equation S U = U R numerically. Its nullity is
    # two: scale plus polarization phase. Isometry fixes scale; a plus/cross
    # anchor fixes phase, which is a basis convention rather than measured data.
    equation = np.kron(np.eye(2), shift) - np.kron(rotation2.T, np.eye(n))
    singular_values = np.linalg.svd(equation, compute_uv=False)
    intertwiner_nullity = int(np.count_nonzero(singular_values < 1.0e-10))

    rng = np.random.default_rng(6415)
    direction = rng.normal(size=n)
    direction /= np.linalg.norm(direction)
    coordinates = u_tt.T @ direction
    strain_matrix = coordinates[0] * e_plus + coordinates[1] * e_cross
    epsilon = 1.0e-7
    q_epsilon = matrix_exp_symmetric(epsilon * strain_matrix)
    metric_epsilon = q_epsilon.T @ q_epsilon
    derivative_numeric = (metric_epsilon - np.eye(3)) / epsilon
    derivative_predicted = 2.0 * strain_matrix
    derivative_residual = float(
        np.linalg.norm(derivative_numeric - derivative_predicted, ord="fro")
    )

    lambda_star = float(exact["exact_branch_import"]["lambda_star_internal"])
    metric_propagator_residue = b_metric @ b_metric_star / lambda_star
    strain_propagator_residue = b_log_strain @ b_log_strain_star / lambda_star

    checks = {
        "q79_local_metric_derivative_available": (
            q79["theorem"]["computed_derivative"] == "DG(0)[delta f]=2 J(delta f)"
        ),
        "prior_no_go_requires_actual_DG": (
            no_go["logical_result"]["current_assumptions_force_exact_dstar_support"] is False
        ),
        "prior_helicity_functor_constructed": (
            helicity["verdict"]["canonical_helicity2_carrier_functor_constructed"] is True
        ),
        "U_TT_is_isometry": max_abs(u_tt.T @ u_tt - np.eye(2)) < 1.0e-12,
        "shift_intertwines_weight2": shift_intertwining_residual < 1.0e-12,
        "metric_Bstar_support_is_exact_plane": metric_support_residual < 1.0e-12,
        "log_strain_Bstar_support_is_exact_plane": strain_support_residual < 1.0e-12,
        "metric_shape_C_is_2I": max_abs(metric_c - 2.0 * np.eye(2)) < 1.0e-12,
        "log_strain_C_is_I": max_abs(strain_c - np.eye(2)) < 1.0e-12,
        "metric_shape_rank_is_2": np.linalg.matrix_rank(b_metric, tol=1.0e-12) == 2,
        "equivariant_intertwiner_space_has_real_dimension_2": intertwiner_nullity == 2,
        "finite_difference_confirms_actual_DG": derivative_residual < 1.0e-6,
        "exact_branch_lambda_is_15": lambda_star == 15.0,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    construction = {
        "name": "WorldInWorldZ64MetricSourceMap.v1",
        "source_space": "real exact-branch K64=C[Z64] coefficients on the selected d_* tower",
        "TT_basis": ["e_plus=(E11-E22)/sqrt(2)", "e_cross=(E12+E21)/sqrt(2)"],
        "fourier_analysis_map": "F2(psi)=(<c2,psi>,<s2,psi>)",
        "strain_map": "S(psi)=<c2,psi> e_plus + <s2,psi> e_cross",
        "comparison_field": "Q(psi)=exp(S(psi))",
        "metric_observable": "G(psi)=Q(psi)^T Q(psi)=exp(2 S(psi))",
        "background": "psi_*=0, Q_*=I, G_*=I",
        "actual_metric_derivative": "DG(0)=2 T_TT U_TT^*",
        "actual_metric_adjoint": "DG(0)^* P_TT=2 U_TT T_TT^*",
        "half_log_metric_derivative": "D[(1/2)log G](0)=T_TT U_TT^*",
        "support_identity": "Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT",
        "support_identity_residual": metric_support_residual,
        "core_factorization_matrix_C_for_metric_g": metric_c.tolist(),
        "core_factorization_matrix_C_for_log_strain": strain_c.tolist(),
        "normalization_consequence": (
            "The earlier canonical fill C=I is exact for the half-log metric/strain "
            "coordinate. For the literal metric derivative delta g/delta psi, the "
            "induced-metric construction gives C=2I. The factor changes residue, "
            "not the selected eigenvalue or pole location."
        ),
    }

    uniqueness = {
        "statement": (
            "Among real linear maps from the Z64 regular carrier to a TT plane "
            "that intertwine the generator with helicity-2 rotation, only the "
            "k=2/k=62 character plane survives. The real intertwiner space is "
            "two-dimensional, corresponding to one scale and one polarization "
            "phase. Isometry fixes scale; anchoring c2 to plus and s2 to cross "
            "fixes phase up to a TT basis gauge."
        ),
        "computed_real_dimension_before_normalization": intertwiner_nullity,
        "continuous_fitted_physical_parameters_after_isometry_and_basis_anchor": 0,
        "remaining_non_numeric_selection": (
            "MTT must select that the exact Z64 shared-circle generator is the "
            "same action as the transverse-frame rotation used by the physical TT quotient."
        ),
    }

    scope = {
        "closed_for_this_explicit_realization": [
            "a displayed nonlinear metric observable G rather than a prefilled B0",
            "the exact derivative and adjoint TT source rows",
            "rank two and exact Z64 support",
            "same-angle helicity-2 equivariance",
            "C=2I for delta g and C=I for half-log metric strain",
            "internal normalized pole support at lambda=15",
        ],
        "not_yet_an_unconditional_MTT_selection_theorem": [
            "same shared-circle equals transverse orientation-circle identification",
            "proof that the selected MTT action chooses this metric observable rather than another equivariant observable",
            "global q79 branch-locus and HYM connection compatibility",
            "dimensionful Newton/Planck normalization and stress-response normalization",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "world_in_world_z64_metric_source_map",
        "status": "EXPLICIT_DG_AND_EXACT_SUPPORT_CLOSED_FOR_CONSTRUCTED_REALIZATION_UNIQUE_MTT_SELECTION_OPEN",
        "input_certificates": {
            "q79_s3_strain_intertwiner": str(Q79_INTERTWINER),
            "exact_branch_internal_aint_gap": str(EXACT_BRANCH),
            "tt_helicity2_z64_carrier": str(HELICITY_FUNCTOR),
            "btt_exact_support_no_go": str(NO_GO),
        },
        "checks": checks,
        "construction": construction,
        "uniqueness": uniqueness,
        "finite_data": {
            "N": n,
            "character_k": k,
            "character_order": n // math.gcd(n, k),
            "lambda_star_internal": lambda_star,
            "metric_support_residual": metric_support_residual,
            "strain_support_residual": strain_support_residual,
            "shift_intertwining_residual": shift_intertwining_residual,
            "finite_difference_DG_residual": derivative_residual,
            "metric_B_Ainv_Bstar": metric_propagator_residue.tolist(),
            "log_strain_B_Ainv_Bstar": strain_propagator_residue.tolist(),
        },
        "scope": scope,
        "guardrails": {
            "claims_all_MTT_realizations_must_use_this_G": False,
            "claims_same_circle_physical_identification_previously_proved": False,
            "claims_global_HYM_metric_source_closed": False,
            "claims_dimensionful_GR_gap_or_Newton_constant": False,
            "adds_fitted_numeric_parameter": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# World-in-World Z64 Metric Source Map v1

## The missing object is now explicit

Let `c2,s2` be the normalized real `k=2/k=62` Fourier pair in `R[Z64]`, and
let `e_plus,e_cross` be the normalized spatial TT tensors for a selected wave
direction. For an exact-branch source coefficient vector `psi`, define

```text
x_plus(psi)  = <c2,psi>,
x_cross(psi) = <s2,psi>,
S(psi)       = x_plus e_plus + x_cross e_cross,
Q(psi)       = exp(S(psi)),
G(psi)       = Q(psi)^T Q(psi) = exp(2 S(psi)).
```

This is an actual nonlinear world-in-world metric observable. At `psi_*=0`,

```text
DG(0)[delta psi] = 2(<c2,delta psi> e_plus
                     + <s2,delta psi> e_cross).
```

Consequently,

```text
DG(0)^* e_plus  = 2 c2,
DG(0)^* e_cross = 2 s2,
Pi_exact64 DG(0)^* P_TT = DG(0)^* P_TT.
```

The support identity is now calculated for this displayed realization. It is
not obtained by writing `B0^*P_TT := U_TT` and then setting a Boolean source
acceptance flag.

## Normalization found, not assumed

With orthonormal Frobenius and group-algebra bases,

```text
B_metric^* P_TT = U_TT (2 I2).
```

For the half-log metric, which is exactly the closure strain coordinate,

```text
B_strain^* P_TT = U_TT I2.
```

Thus the earlier `C=I2` packet is correct for logarithmic strain. The literal
metric derivative has `C=2I2`. This factor changes the propagator residue but
not its selected eigenvalue or pole location: the exact internal support still
has `lambda_*=15` in normalized branch units.

## Why the Fourier row is essentially forced

The audit solves the real intertwining equation between the `Z64` shift and
spin-2 rotation. Its solution space has dimension two: overall scale and
polarization phase. Isometry fixes the scale. Anchoring `c2` to plus and `s2`
to cross fixes the phase, which is a polarization-basis convention rather than
a measured constant. No fitted continuous physical parameter remains.

## Exact status

Closed for the constructed realization:

- a nonlinear `G(Psi)` and its derivative;
- exact TT adjoint rows and rank;
- exact `Z64` support and helicity-2 equivariance;
- the normalization matrices `2I2` and `I2`;
- the normalized internal pole support at `15`.

Still open as a theorem about MTT selection:

- prove that the exact `Z64` shared-circle generator is the same action as the
  transverse-frame orientation circle;
- prove that the selected MTT action chooses this induced metric observable;
- extend the q79 carrier map through branching and the selected HYM connection;
- derive dimensionful Newton/Planck and stress-response normalization.

So this is an explicit zero-fit realization and a genuine computation of
`DG`. It is not yet a uniqueness theorem saying every admissible MTT branch
must select this realization.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
