from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXTERNAL = ROOT / "certificates" / "external_clues_btt_support_closure_routes_certificate.json"
NO_GO = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"
UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Equivariant_Central_Circle_TT_Support_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def mat_vec(mat: list[list[float]], vec: list[float]) -> list[float]:
    return [dot(row, vec) for row in mat]


def mat_mat(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def max_abs_matrix(a: list[list[float]]) -> float:
    return max(abs(x) for row in a for x in row)


def main() -> None:
    external = load(EXTERNAL)
    no_go = load(NO_GO)
    uniqueness = load(UNIQUENESS)
    adjoint = load(ADJOINT)

    n = 64
    k = 2
    theta = 2 * math.pi / n

    # Real orthonormal character basis for the k=2/k=62 plane in C[Z64].
    c2 = [math.sqrt(2 / n) * math.cos(k * theta * j) for j in range(n)]
    s2 = [math.sqrt(2 / n) * math.sin(k * theta * j) for j in range(n)]

    # The cyclic shift operator S acts by (Sv)_j = v_{j-1}. On span{c2,s2} it
    # rotates by +k theta in this basis.
    shift = [[1.0 if i == (j + 1) % n else 0.0 for j in range(n)] for i in range(n)]
    uc = mat_vec(shift, c2)
    us = mat_vec(shift, s2)
    shift_on_plane = [
        [dot(c2, uc), dot(c2, us)],
        [dot(s2, uc), dot(s2, us)],
    ]
    expected = [
        [math.cos(k * theta), -math.sin(k * theta)],
        [math.sin(k * theta), math.cos(k * theta)],
    ]

    # U maps TT plus/cross into the exact helicity-2 plane.
    u = [[c2[i], s2[i]] for i in range(n)]
    utu = mat_mat(transpose(u), u)
    projector = mat_mat(u, transpose(u))
    pu_minus_u = [
        [sum(projector[i][j] * u[j][col] for j in range(n)) - u[i][col] for col in range(2)]
        for i in range(n)
    ]

    # This is the algebraic replacement for the failed support premise:
    # if the actual co-shape map is U times an invertible TT-basis matrix, then
    # Pi_exact64 B^*P_TT = B^*P_TT follows by projection.
    sample_rank2_basis_change = [[1.25, -0.2], [0.1, 0.9]]
    bstar_ptt_model = mat_mat(u, sample_rank2_basis_change)
    p_bstar_minus_bstar = [
        [
            sum(projector[i][j] * bstar_ptt_model[j][col] for j in range(n)) - bstar_ptt_model[i][col]
            for col in range(2)
        ]
        for i in range(n)
    ]
    det_basis_change = (
        sample_rank2_basis_change[0][0] * sample_rank2_basis_change[1][1]
        - sample_rank2_basis_change[0][1] * sample_rank2_basis_change[1][0]
    )

    checks = {
        "external_best_route_is_equivariant_selector": (
            external["best_route"]["name"] == "R2_equivariant_central_character_selector"
        ),
        "adjoint_support_nonzero_closed": adjoint["closed_now"]["TT_coupling_nonzero_for_adjoint_support"] is True,
        "no_go_requires_extra_selection": (
            no_go["logical_result"]["current_assumptions_force_exact_dstar_support"] is False
        ),
        "z64_uniqueness_ready": uniqueness["theorem"]["closed"] is True,
        "c2_norm_one": abs(norm(c2) - 1.0) < 1e-12,
        "s2_norm_one": abs(norm(s2) - 1.0) < 1e-12,
        "c2_s2_orthogonal": abs(dot(c2, s2)) < 1e-12,
        "shift_intertwines_as_weight2": max_abs_matrix(
            [
                [shift_on_plane[i][j] - expected[i][j] for j in range(2)]
                for i in range(2)
            ]
        )
        < 1e-12,
        "u_is_isometry": max_abs_matrix(
            [[utu[i][j] - (1.0 if i == j else 0.0) for j in range(2)] for i in range(2)]
        )
        < 1e-12,
        "projector_fixes_u": max_abs_matrix(pu_minus_u) < 1e-12,
        "rank2_basis_change_invertible": abs(det_basis_change) > 1e-12,
        "projector_fixes_model_bstar_ptt": max_abs_matrix(p_bstar_minus_bstar) < 1e-12,
    }

    theorem = {
        "name": "EquivariantCentralCircleTTSupportTheorem.v1",
        "proved_algebraically": all(checks.values()),
        "statement": (
            "Let U_TT be the same-angle helicity-2 equivariant carrier from TT plus/cross "
            "to the selected exact Z64 d_* central-circle plane. If the actual adjoint "
            "TT co-shape support B^*P_TT factors through U_TT by an invertible TT-basis "
            "normalization, then Pi_exact64 B^*P_TT = B^*P_TT."
        ),
        "proof": [
            "The real k=2/k=62 character basis c2,s2 is orthonormal in C[Z64].",
            "The Z64 shift restricts to the spin-2 rotation on span{c2,s2}.",
            "Therefore U_TT: TT_plus/cross -> span{c2,s2} is the same-angle equivariant carrier.",
            "Pi_exact64 is the orthogonal projector onto the selected d_* tensor this real character plane.",
            "Any B^*P_TT = U_TT C with C invertible has image contained in Pi_exact64.",
            "Hence Pi_exact64 B^*P_TT = B^*P_TT.",
        ],
        "consequence_if_sourced_for_actual_shape_map": (
            "support(J_TT)=|d_*> tensor span{c_2,s_2} and lambda_GR,TT=15 in normalized internal units."
        ),
    }

    remaining = {
        "source_status": "SOURCE_EQUIVARIANCE_FOR_ACTUAL_BSTAR_PTT_OPEN",
        "actual_missing_statement": (
            "The corpus still must state or compute that the actual B=DG(Psi*)Pi_coh adjoint "
            "co-shape map satisfies B^*P_TT = U_TT C on the selected branch, for an invertible "
            "TT normalization C, using the same central angle as the exact Z64 shift."
        ),
        "why_this_is_smaller_than_previous_gap": (
            "The old premise directly asserted support(B^*P_TT)=Pi_exact64. The new gate only asks "
            "for same-angle equivariance/factorization of the actual metric co-shape map; the projector "
            "identity is then a verified algebraic consequence."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "equivariant_central_circle_tt_support_theorem",
        "status": "EQUIVARIANT_SELECTOR_ALGEBRA_CLOSED_ACTUAL_SHAPE_MAP_EQUIVARIANCE_OPEN",
        "input_certificates": {
            "external_clues": str(EXTERNAL),
            "btt_exact_support_independence_no_go": str(NO_GO),
            "gr_tt_helicity2_z64_uniqueness": str(UNIQUENESS),
            "btt_adjoint_shape_map_typing": str(ADJOINT),
        },
        "finite_character_data": {
            "group": "Z64",
            "character_label": 2,
            "conjugate_label": 62,
            "character_order": 32,
            "selected_plane": "span{c_2,s_2}",
            "projection_identity_residual": max_abs_matrix(p_bstar_minus_bstar),
            "intertwining_residual": max_abs_matrix(
                [
                    [shift_on_plane[i][j] - expected[i][j] for j in range(2)]
                    for i in range(2)
                ]
            ),
        },
        "checks": checks,
        "theorem": theorem,
        "remaining": remaining,
        "guardrails": {
            "claims_actual_BstarPtt_sourced": False,
            "claims_unconditional_support_identity": False,
            "adds_numeric_knob": False,
            "uses_observed_GR_data": False,
            "conflates_zero_mode_with_helicity_character": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Equivariant Central Circle TT Support Theorem v1

## Algebraic Theorem

Let `U_TT` be the real helicity-2 carrier

```text
U_TT : span{TT_plus, TT_cross} -> |d_*> tensor span{c_2,s_2} subset C[Z64].
```

Here `c_2,s_2` are the real `k=2/k=62` character pair. The cyclic `Z64` shift
restricts to spin-2 rotation on this plane, so `U_TT` is the same-angle
equivariant carrier.

If the actual adjoint TT co-shape map factors as

```text
B^*P_TT = U_TT C
```

for an invertible `2 x 2` TT normalization matrix `C`, then

```text
Pi_exact64 B^*P_TT = B^*P_TT.
```

## Proof

The script verifies the finite character calculation directly.

1. The `k=2` real character vectors `c_2,s_2` are orthonormal in `C[Z64]`.
2. The `Z64` shift restricts to rotation by the spin-2 sampled angle on
   `span{c_2,s_2}`.
3. The orthogonal projector `Pi_exact64` fixes the image of `U_TT`.
4. Therefore it fixes every rank-two co-shape map of the form `U_TT C`.

This closes the algebraic part of the equivariant selector.

## What Remains

The actual source-level statement is still open:

```text
The metric shape map B=DG(Psi*)Pi_coh has adjoint TT support
B^*P_TT = U_TT C
```

on the selected exact GR/QG branch, for an invertible TT normalization `C`, and
with the same central-circle angle as the exact `Z64` shift.

This is strictly smaller than the previous missing premise. We no longer need
to assume the exact support identity directly. We only need to source or compute
same-angle equivariance/factorization of the actual shape map; the support
identity then follows by finite linear algebra.

## Consequence If The Remaining Source Gate Closes

```text
support(J_TT)=|d_*> tensor span{c_2,s_2}
lambda_GR,TT=15
```

in normalized internal exact-branch units.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
