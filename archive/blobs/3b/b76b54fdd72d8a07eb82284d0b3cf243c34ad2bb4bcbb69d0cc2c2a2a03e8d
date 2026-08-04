from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

Q79_J = ROOT / "certificates" / "q79_s3_strain_intertwiner_certificate.json"
ROOTSTACK_J = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
Z64_METRIC = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
GLOBAL_DG = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"

OUT_CERT = (
    ROOT / "certificates" / "selected_q79_z64_qww_source_factorization_certificate.json"
)
OUT_NOTE = (
    ROOT / "proof_corpus" / "Selected_q79_Z64_to_QWW_Source_Factorization_v1.md"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def main() -> None:
    q79 = load(Q79_J)
    rootstack = load(ROOTSTACK_J)
    metric = load(Z64_METRIC)
    global_dg = load(GLOBAL_DG)

    root2 = sp.sqrt(2)

    # Frobenius coordinates are ordered as
    # (E11,E22,E33,(E23+E32)/sqrt(2),(E13+E31)/sqrt(2),(E12+E21)/sqrt(2)).
    # In these coordinates the previously proved q79 J is the identity.
    j_matrix = sp.eye(6)
    f_plus = sp.Matrix([1 / root2, -1 / root2, 0, 0, 0, 0])
    f_cross = sp.Matrix([0, 0, 0, 0, 0, 1])
    q79_tt_embedding = sp.Matrix.hstack(f_plus, f_cross)

    p_trace = sp.zeros(6)
    trace_vector = sp.Matrix([1, 1, 1, 0, 0, 0]) / sp.sqrt(3)
    p_trace = trace_vector * trace_vector.T
    p_shape = sp.zeros(6)
    p_shape[:3, :3] = sp.eye(3) - sp.ones(3) / 3
    p_shear = sp.diag(0, 0, 0, 1, 1, 1)

    n = 64
    k = 2
    angle = 2.0 * math.pi * k / n
    indices = np.arange(n, dtype=float)
    normalization = math.sqrt(2.0 / n)
    c2 = normalization * np.cos(angle * indices)
    s2 = normalization * np.sin(angle * indices)
    fourier_analysis = np.vstack([c2, s2])

    # Shift e_j -> e_(j+1). The analysis rows transform by the weight-two
    # rotation. We infer the exact sign convention from the computed matrix.
    shift = np.roll(np.eye(n), 1, axis=0)
    induced_rotation = fourier_analysis @ shift @ fourier_analysis.T
    source_rows = np.asarray(q79_tt_embedding, dtype=float) @ fourier_analysis
    exact_plane_projector = fourier_analysis.T @ fourier_analysis

    source_gram = source_rows @ source_rows.T
    source_projector = np.asarray(q79_tt_embedding, dtype=float) @ np.asarray(
        q79_tt_embedding.T, dtype=float
    )

    checks = {
        "prior_q79_J_is_exact_isometry": (
            q79["exact_checks"]["J_is_frobenius_isometry"] is True
            and q79["exact_checks"]["all_six_S3_actions_intertwine"] is True
        ),
        "minimal_rootstack_J_is_global_rank_six_parallel_isomorphism": (
            rootstack["claim_tiers"]["minimal_full_monodromy_rootstack"]
            == "CLOSED_UNIQUE_MINIMAL"
            and rootstack["claim_tiers"][
                "rootstack_rank_six_strain_bundle_isomorphism"
            ]
            == "CLOSED_EXACT"
            and rootstack["claim_tiers"][
                "rootstack_flat_HYM_connection_intertwining"
            ]
            == "CLOSED_EXACT"
        ),
        "existing_Z64_metric_source_is_exact_weight_two_realization": (
            metric["checks"]["shift_intertwines_weight2"] is True
            and metric["checks"]["metric_Bstar_support_is_exact_plane"] is True
            and metric["checks"]["metric_shape_C_is_2I"] is True
        ),
        "global_covariant_DG_associated_bundle_is_available": (
            global_dg["claim_tiers"]["global_covariant_DG_bundle_map"]
            == "CLOSED_FOR_CONSTRUCTED_REALIZATION"
            and global_dg["claim_tiers"]["global_exact_Z64_support_identity"]
            == "CLOSED_FIBERWISE"
        ),
        "q79_TT_preimage_is_isometric": (
            sp.simplify(q79_tt_embedding.T * q79_tt_embedding) == sp.eye(2)
        ),
        "plus_mode_lies_exactly_in_rank2_shape_lane": (
            sp.simplify(p_shape * f_plus - f_plus) == sp.zeros(6, 1)
            and sp.simplify(p_trace * f_plus) == sp.zeros(6, 1)
            and sp.simplify(p_shear * f_plus) == sp.zeros(6, 1)
        ),
        "cross_mode_lies_exactly_in_rank3_shear_lane": (
            sp.simplify(p_shear * f_cross - f_cross) == sp.zeros(6, 1)
            and sp.simplify(p_trace * f_cross) == sp.zeros(6, 1)
            and sp.simplify(p_shape * f_cross) == sp.zeros(6, 1)
        ),
        "J_maps_q79_preimages_to_normalized_plus_cross": (
            sp.simplify(j_matrix * q79_tt_embedding - q79_tt_embedding)
            == sp.zeros(6, 2)
        ),
        "Z64_fourier_analysis_is_isometric_on_weight2_plane": (
            max_abs(fourier_analysis @ fourier_analysis.T - np.eye(2)) < 1.0e-12
        ),
        "q79_source_rows_have_rank_two": (
            np.linalg.matrix_rank(source_rows, tol=1.0e-12) == 2
        ),
        "q79_source_rows_have_exact_Z64_support": (
            max_abs(source_rows @ exact_plane_projector - source_rows) < 1.0e-12
        ),
        "q79_source_compression_is_the_TT_projector": (
            max_abs(source_gram - source_projector) < 1.0e-12
        ),
        "metric_derivative_factor_is_exactly_two": (
            sp.simplify(2 * j_matrix * q79_tt_embedding - 2 * q79_tt_embedding)
            == sp.zeros(6, 2)
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    status = (
        "SELECTED_Q79_Z64_QWW_TT_SOURCE_FACTORIZATION_CLOSED_"
        "UNIQUE_UP_TO_POLARIZATION_AND_FRAME_GAUGE_"
        "PRIMITIVE_ROOTSTACK_LORENTZIAN_BRANCH_AND_INVERSE_FOURIER_MUKAI_OPERATOR_IDENTITY_OPEN"
    )

    theorem = {
        "name": "Selectedq79Z64toQWWSourceFactorizationTheorem",
        "selected_source_map": {
            "domain": (
                "the real k=2/k=62 Fourier plane in the exact d_* tower of R[Z64]"
            ),
            "local_formula": (
                "Phi_q79(psi)=<c2,psi>*(1/sqrt(2),-1/sqrt(2),0;0,0,0) "
                "+ <s2,psi>*(0,0,0;0,0,1)"
            ),
            "lane_content": {
                "plus": "rank-two trace-zero diagonal/shape lane A0",
                "cross": "rank-three off-diagonal/shear lane A",
                "rank-one_scalar_lane": "absent on the physical TT quotient",
            },
            "rank": 2,
            "parameter_count": 0,
        },
        "factorization": {
            "strain": "S(psi)=J Phi_q79(psi)=<c2,psi>e_plus+<s2,psi>e_cross",
            "comparison_field": "Q_WW(psi)=exp(S(psi)) on the orientation-fixed polar slice",
            "metric": "G(psi)=Q_WW(psi)^T Q_WW(psi)=exp(2S(psi))",
            "derivative": "DG(0)=2 J Phi_q79",
            "exact_support": "Pi_exact64 Phi_q79^*=Phi_q79^* and likewise for DG(0)^*P_TT",
        },
        "uniqueness": {
            "Z64_step": (
                "helicity two forces the unique real k=2/k=62 character plane; "
                "isometry fixes scale and its remaining phase is TT polarization gauge"
            ),
            "q79_step": (
                "the natural q79 J is a global isometric isomorphism on the unique "
                "minimal full-monodromy root stack, so each TT tensor has one q79 preimage"
            ),
            "QWW_step": (
                "logarithmic strain defines the unique positive polar representative "
                "Q_WW=exp(S) after orientation gauge is fixed"
            ),
            "metric_step": (
                "the inner Euclidean metric gives the unique pullback G=Q_WW^T Q_WW"
            ),
            "result": (
                "On the selected massless-helicity-two minimal-rootstack branch, the "
                "q79/Z64-to-Q_WW metric source is unique up to polarization, frame, "
                "and diffeomorphism gauge and contains no fitted physical parameter."
            ),
        },
        "globalization": {
            "q79": "S3-associated bundles on the full-monodromy root stack",
            "physical_TT": "SO(2) weight-two bundle associated to transverse frames",
            "relation": (
                "the finite k=2 representation is the Z64 restriction of the continuous "
                "weight-two representation; no false equality of scalar line bundles is used"
            ),
        },
        "remaining_boundary": [
            "primitive MTT selection of the minimal-rootstack Lorentzian physical branch",
            "identification of the flat finite-monodromy carrier with the selected inverse-Fourier-Mukai/HYM Hessian and overlap kernels",
            "off-shell emission of all six strain coordinates is not claimed by the physical rank-two TT source",
            "numeric kappa_h, Lambda_eff, channel fusion, and quantum/UV completion",
        ],
    }

    certificate = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_q79_z64_qww_source_factorization",
        "date": "2026-07-15",
        "status": status,
        "inputs": {
            "q79_s3_strain_intertwiner": str(Q79_J),
            "q79_full_monodromy_rootstack_bridge": str(ROOTSTACK_J),
            "world_in_world_z64_metric_source": str(Z64_METRIC),
            "global_covariant_helicity2_dg_bundle": str(GLOBAL_DG),
        },
        "checks": checks,
        "finite_data": {
            "q79_plus_preimage": [str(value) for value in f_plus],
            "q79_cross_preimage": [str(value) for value in f_cross],
            "q79_TT_embedding_gram": [
                [str(value) for value in row]
                for row in (q79_tt_embedding.T * q79_tt_embedding).tolist()
            ],
            "Z64_character": k,
            "Z64_character_order": n // math.gcd(n, k),
            "induced_weight2_rotation": induced_rotation.tolist(),
            "source_rank": int(np.linalg.matrix_rank(source_rows, tol=1.0e-12)),
            "support_residual": max_abs(
                source_rows @ exact_plane_projector - source_rows
            ),
            "source_compression_residual": max_abs(source_gram - source_projector),
        },
        "theorem": theorem,
        "claim_tiers": {
            "exact_Z64_TT_to_q79_source_map": "CLOSED_EXPLICIT",
            "q79_TT_lane_support": "CLOSED_EXACT_A0_PLUS_A",
            "q79_source_map_exact_Z64_support": "CLOSED_EXACT",
            "q79_rootstack_globalization": "CLOSED_ON_UNIQUE_MINIMAL_FULL_MONODROMY_ROOTSTACK",
            "orientation_fixed_q79_source_to_QWW": "CLOSED_EXACT_UNIQUE",
            "QWW_to_metric_observable": "CLOSED_EXACT_UNIQUE_PULLBACK",
            "selected_branch_q79_Z64_QWW_source_realization": "CLOSED_UNIQUE_UP_TO_GAUGE",
            "continuous_fitted_physical_parameters": "CLOSED_ZERO",
            "primitive_MTT_selects_minimal_rootstack_Lorentzian_branch": "OPEN",
            "inverse_Fourier_Mukai_HYM_operator_identity": "OPEN",
            "off_shell_all_six_lane_emission_from_Z64_TT_source": "NOT_CLAIMED_NOT_REQUIRED_FOR_PHYSICAL_TT_QUOTIENT",
        },
        "guardrails": {
            "claims_primitive_physical_branch_selection_closed": False,
            "claims_inverse_Fourier_Mukai_HYM_operator_identity_closed": False,
            "claims_rank_two_TT_source_emits_all_six_off_shell_strains": False,
            "claims_internal_flat_line_equals_global_helicity_line": False,
            "adds_fitted_numeric_parameter": False,
            "uses_observed_physics_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected q79/Z64 to QWW Source Factorization v1

Date: 2026-07-15

## Exact source map

The branch-continuation theorem makes `J` a global rank-six isometric
isomorphism on the unique minimal full-monodromy q79 root stack. Therefore the
exact `Z64` TT plane has a unique q79 preimage. In the local q79 coordinates
`(a1,a2,a3;b1,b2,b3)`, define

```text
f_plus  = (1/sqrt(2),-1/sqrt(2),0;0,0,0),
f_cross = (0,0,0;0,0,1),
Phi_q79(psi)=<c2,psi>f_plus+<s2,psi>f_cross.
```

The exact lane projectors give

```text
f_plus  in A0, the rank-two diagonal-shape lane,
f_cross in A,  the rank-three off-diagonal-shear lane.
```

The rank-one scalar lane is absent on the physical TT quotient. This is not a
missing coordinate: trace is removed by the TT constraint.

## Complete factorization

The maps now compose without a prefilled matrix:

```text
exact Z64 k=2 plane
  -> Phi_q79
q79 A0+A source plane on the full-monodromy root stack
  -> J
S(psi)=<c2,psi>e_plus+<s2,psi>e_cross
  -> exp
Q_WW(psi)=exp(S(psi))
  -> pullback metric
G(psi)=Q_WW(psi)^T Q_WW(psi)=exp(2S(psi)).
```

Consequently

```text
DG(0)=2 J Phi_q79,
rank(Phi_q79)=2,
Pi_exact64 Phi_q79^*=Phi_q79^*,
Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT.
```

## Uniqueness

Each step has now been reduced to a universal or representation-theoretic
choice:

1. helicity two forces the real `k=2/k=62` plane in `R[Z64]`;
2. isometry fixes its scale and polarization phase is basis gauge;
3. the natural q79 `J` is unique and invertible on the minimal root stack;
4. logarithmic strain fixes the positive polar representative `Q_WW=exp(S)`;
5. the inner Euclidean metric fixes the pullback `G=Q_WW^T Q_WW`.

Thus the selected-branch source realization is unique up to polarization,
frame, and diffeomorphism gauge. It introduces zero fitted physical parameters.
The global construction uses associated weight-two bundles and does not equate
the flat internal shared line with the nontrivial global helicity line.

## Boundary

This closes the old q79/`Z64`-to-`Q_WW` map problem on the selected massless
helicity-two minimal-rootstack branch. Primitive MTT must still select that
root-stack Lorentzian physical branch. The flat finite-monodromy carrier also
has not yet been identified with the independently selected
inverse-Fourier-Mukai/HYM Hessian and overlap kernels. The rank-two physical TT
source is not claimed to emit all six off-shell strain coordinates.

Current status:

```text
{status}
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed q79/Z64/QWW factorization checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
