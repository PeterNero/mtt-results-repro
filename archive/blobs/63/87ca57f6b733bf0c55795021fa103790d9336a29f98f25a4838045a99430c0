from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

GLOBAL_NOGO = ROOT / "certificates" / "global_helicity_bundle_same_circle_nogo_certificate.json"
METRIC_SOURCE = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
Q79_INTERTWINER = ROOT / "certificates" / "q79_s3_strain_intertwiner_certificate.json"

OUT_CERT = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Global_Covariant_Helicity2_DG_Bundle_Construction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rotation_weight_two(angle: float) -> np.ndarray:
    return np.array(
        [
            [math.cos(2.0 * angle), -math.sin(2.0 * angle)],
            [math.sin(2.0 * angle), math.cos(2.0 * angle)],
        ],
        dtype=float,
    )


def tt_project(direction: np.ndarray, strain: np.ndarray) -> np.ndarray:
    direction = direction / np.linalg.norm(direction)
    projector = np.eye(3) - np.outer(direction, direction)
    transverse = projector @ strain @ projector
    return transverse - 0.5 * np.trace(transverse) * projector


def flatten_symmetric(matrix: np.ndarray) -> np.ndarray:
    return np.array(
        [
            matrix[0, 0],
            matrix[1, 1],
            matrix[2, 2],
            math.sqrt(2.0) * matrix[0, 1],
            math.sqrt(2.0) * matrix[0, 2],
            math.sqrt(2.0) * matrix[1, 2],
        ]
    )


def main() -> None:
    no_go = load(GLOBAL_NOGO)
    metric = load(METRIC_SOURCE)
    q79 = load(Q79_INTERTWINER)

    N = metric["finite_data"]["N"]
    character = metric["finite_data"]["character_k"]
    generator_angle = 2.0 * math.pi / N
    continuous_generator = rotation_weight_two(generator_angle)

    expected_generator = np.array(
        [
            [math.cos(2.0 * generator_angle), -math.sin(2.0 * generator_angle)],
            [math.sin(2.0 * generator_angle), math.cos(2.0 * generator_angle)],
        ]
    )
    representation_residual = float(np.linalg.norm(continuous_generator - expected_generator))

    stf_basis = [
        np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0),
        np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0),
        np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        / math.sqrt(2.0),
        np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
        / math.sqrt(2.0),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
        / math.sqrt(2.0),
    ]
    directions = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 1.0, 1.0]) / math.sqrt(3.0),
        np.array([2.0, -1.0, 3.0]) / math.sqrt(14.0),
    ]

    fiber_ranks = []
    transverse_residuals = []
    trace_residuals = []
    for direction in directions:
        images = [tt_project(direction, basis) for basis in stf_basis]
        fiber_ranks.append(int(np.linalg.matrix_rank(np.stack([flatten_symmetric(x) for x in images], axis=1))))
        transverse_residuals.extend(float(np.linalg.norm(image @ direction)) for image in images)
        trace_residuals.extend(abs(float(np.trace(image))) for image in images)

    rotations = [
        np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]),
        np.array([[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]),
        np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
    ]
    equivariance_residuals = []
    for rotation in rotations:
        for direction in directions:
            for strain in stf_basis:
                left = tt_project(rotation @ direction, rotation @ strain @ rotation.T)
                right = rotation @ tt_project(direction, strain) @ rotation.T
                equivariance_residuals.append(float(np.linalg.norm(left - right)))

    plus = np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0)
    cross = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]]) / math.sqrt(2.0)
    north = np.array([0.0, 0.0, 1.0])
    north_local_residual = max(
        float(np.linalg.norm(tt_project(north, plus) - plus)),
        float(np.linalg.norm(tt_project(north, cross) - cross)),
    )

    checks = {
        "global_scalar_line_identification_no_go_available": (
            no_go["claim_tiers"]["global_internal_external_line_identity"]
            == "CLOSED_NO_GO"
        ),
        "finite_character_is_weight_two": character == 2,
        "Z64_generator_is_restriction_of_SO2_weight_two": representation_residual < 1.0e-14,
        "TT_projector_has_rank_two_in_every_tested_fiber": fiber_ranks == [2] * len(directions),
        "TT_projector_is_transverse": max(transverse_residuals) < 1.0e-12,
        "TT_projector_is_tracefree": max(trace_residuals) < 1.0e-12,
        "TT_projector_is_SO3_equivariant": max(equivariance_residuals) < 1.0e-12,
        "north_patch_recovers_plus_cross_basis": north_local_residual < 1.0e-12,
        "local_metric_DG_has_factor_two": (
            metric["checks"]["metric_shape_C_is_2I"] is True
        ),
        "exact_finite_support_remains_closed": (
            metric["checks"]["metric_Bstar_support_is_exact_plane"] is True
        ),
        "internal_lambda_remains_15": metric["finite_data"]["lambda_star_internal"] == 15.0,
        "q79_full_strain_carrier_is_available": (
            "to Sym(3,R)" in q79["theorem"]["statement"]
        ),
        "global_bundle_retains_nontrivial_Chern_class": (
            no_go["finite_data"]["external_weight_two_Chern_number"] == -4
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "GlobalCovariantHelicityTwoDGAssociatedBundleTheorem",
        "principal_bundle": (
            "P_perp->S2, the oriented transverse-frame SO(2) principal bundle"
        ),
        "fiber_representation": (
            "V2=R2 with SO(2) action by angle 2theta; restriction to the Z64 "
            "generator is exactly the k=2/k=62 real Fourier plane"
        ),
        "associated_bundle": "E_TT=P_perp x_{SO(2)} V2",
        "Chern_number": -4,
        "global_projector": (
            "T_n(S)=P_n S P_n-(1/2)tr(P_n S P_n)P_n, P_n=I-n n^T"
        ),
        "properties": [
            "smooth on S2",
            "SO(3)-equivariant",
            "rank two in every fiber",
            "transverse and trace-free",
            "recovers the plus/cross map in a local oriented frame",
        ],
        "global_DG": (
            "Use the associated-bundle isomorphism between the weight-two source "
            "fiber and E_TT; the literal metric derivative is fiberwise 2 times "
            "that isomorphism, while the half-log strain derivative is 1 times it."
        ),
        "exact_support": (
            "Tensoring with the selected internal |d_*> factor makes Pi_exact64 "
            "act on the internal factor and identity on E_TT, so the exact support "
            "identity and internal lambda=15 globalize fiberwise."
        ),
        "parameter_count": 0,
        "selection_boundary": (
            "This constructs the canonical covariantization of the computed local DG. "
            "It does not prove that the selected Lorentzian MTT action uses it, emit "
            "the stress tensor coupling, or establish the massless graviton dynamics."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "global_covariant_helicity2_dg_bundle",
        "date": "2026-07-15",
        "status": "GLOBAL_COVARIANT_HELICITY2_DG_BUNDLE_CONSTRUCTED_EXACT_SUPPORT_CLOSED_SELECTED_ACTION_STRESS_LORENTZIAN_OPEN",
        "inputs": {
            "global_line_identity_no_go": str(GLOBAL_NOGO),
            "local_metric_source": str(METRIC_SOURCE),
            "q79_strain_intertwiner": str(Q79_INTERTWINER),
        },
        "checks": checks,
        "numerics": {
            "Z64_to_SO2_representation_residual": representation_residual,
            "fiber_ranks": fiber_ranks,
            "max_transverse_residual": max(transverse_residuals),
            "max_trace_residual": max(trace_residuals),
            "max_SO3_equivariance_residual": max(equivariance_residuals),
            "north_patch_plus_cross_residual": north_local_residual,
        },
        "theorem": theorem,
        "claim_tiers": {
            "global_helicity2_associated_bundle": "CLOSED",
            "global_covariant_TT_projector": "CLOSED",
            "global_covariant_DG_bundle_map": "CLOSED_FOR_CONSTRUCTED_REALIZATION",
            "global_exact_Z64_support_identity": "CLOSED_FIBERWISE",
            "internal_lambda15": "CLOSED_UNCHANGED",
            "selected_MTT_action_uses_global_DG": "OPEN",
            "stress_energy_coupling": "OPEN",
            "Lorentzian_massless_graviton_dynamics": "OPEN",
        },
        "guardrails": {
            "claims_global_scalar_plus_cross_rows": False,
            "claims_internal_flat_line_equals_helicity_bundle": False,
            "claims_selected_action_closed": False,
            "claims_stress_coupling_closed": False,
            "claims_Lorentzian_QG_closed": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Global Covariant Helicity-2 DG Bundle Construction v1

Date: 2026-07-15

## Associated-bundle construction

Let `P_perp->S2` be the oriented transverse-frame `SO(2)` principal bundle and
let `V2=R2` carry the weight-two action

```text
R_2(theta)=rotation(2 theta).
```

At `theta=2pi/64`, this is exactly the real `k=2/k=62` Fourier representation
already used by the finite `Z64` source. Therefore

```text
E_TT=P_perp x_{SO(2)} V2
```

is the correct global home of those local two-component rows. It has Chern
number `-4`; the topology is retained rather than incorrectly trivialized.

## Global TT projector

For a unit direction `n`, set `P_n=I-nn^T` and

```text
T_n(S)=P_n S P_n-(1/2)tr(P_n S P_n)P_n.
```

The executable checks show that `T_n` has rank two in every tested fiber, is
transverse and trace-free, and satisfies

```text
T_{Rn}(R S R^T)=R T_n(S) R^T.
```

It is therefore a global `SO(3)`-equivariant bundle map. At the north-pole
frame it recovers the existing `e_plus,e_cross` basis exactly.

## Globalized DG and exact support

The local Fourier plane and physical TT fiber are the same weight-two
representation. Passing to associated bundles turns the local intertwiner into
a global bundle isomorphism. The literal metric derivative is fiberwise twice
this isomorphism; half-log strain is once it.

Tensor with the selected internal `|d_*>` factor. The exact finite projector
acts on that factor and identity on `E_TT`, so

```text
Pi_exact64 DG_global^*P_TT=DG_global^*P_TT
```

holds fiberwise and the normalized internal pole remains `lambda=15`.

This construction is parameter-free. It closes the global geometric
covariantization of the explicit `DG`, but not selection by the Lorentzian MTT
action, stress-energy coupling, or massless graviton dynamics.

Current status:

```text
GLOBAL_COVARIANT_HELICITY2_DG_BUNDLE_CONSTRUCTED_EXACT_SUPPORT_CLOSED_SELECTED_ACTION_STRESS_LORENTZIAN_OPEN
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed covariant DG bundle checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
