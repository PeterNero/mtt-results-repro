from __future__ import annotations

import json
from itertools import permutations
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

DETERMINANT_BRIDGE = (
    ROOT
    / "certificates"
    / "q79_shared_circle_spinc_determinant_bridge_certificate.json"
)
SAME_SOURCE_MAP = (
    ROOT / "certificates" / "q79_shared_z64_same_source_monodromy_map_certificate.json"
)
ROOTSTACK_BRIDGE = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
QUARTERTURN_HESSIAN = (
    ROOT
    / "certificates"
    / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
)
PARENT_DESCENT = (
    ROOT
    / "certificates"
    / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
)
SQUARE_THETA_NOGO = (
    ROOT
    / "certificates"
    / "q79_square_theta_quarterturn_strain_nogo_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Shared_RootPlane_Twisted_Exterior_JDE_Functor_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for source, target in enumerate(permutation):
        matrix[target, source] = 1
    return matrix


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def exterior_square(matrix: sp.Matrix) -> sp.Matrix:
    # Oriented opposite-edge basis: e2^e3, e3^e1, e1^e2.
    pairs = [(1, 2), (2, 0), (0, 1)]
    result = sp.zeros(3)
    for column, (first, second) in enumerate(pairs):
        for row, (out_first, out_second) in enumerate(pairs):
            result[row, column] = (
                matrix[out_first, first] * matrix[out_second, second]
                - matrix[out_second, first] * matrix[out_first, second]
            )
    return result


def as_int_rows(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(value) for value in row] for row in matrix.tolist()]


def main() -> None:
    determinant_bridge = load(DETERMINANT_BRIDGE)
    same_source_map = load(SAME_SOURCE_MAP)
    rootstack_bridge = load(ROOTSTACK_BRIDGE)
    quarterturn_hessian = load(QUARTERTURN_HESSIAN)
    parent_descent = load(PARENT_DESCENT)
    square_theta_nogo = load(SQUARE_THETA_NOGO)

    records = []
    s3_actions = []
    twisted_exterior_actions = []
    for permutation in permutations(range(3)):
        sign = permutation_sign(permutation)
        sheet = permutation_matrix(permutation)
        wedge = exterior_square(sheet)
        twisted_wedge = sign * wedge
        records.append(
            {
                "permutation": list(permutation),
                "sign": sign,
                "sheet_matrix": as_int_rows(sheet),
                "exterior_square_matrix": as_int_rows(wedge),
                "determinant_twisted_exterior_matrix": as_int_rows(twisted_wedge),
            }
        )
        s3_actions.append(sp.diag(sheet, sheet))
        twisted_exterior_actions.append(twisted_wedge)

    identity3 = sp.eye(3)
    root_quarterturn = sp.Matrix(parent_descent["finite_data"]["integral_quarterturn"])
    jde = sp.kronecker_product(root_quarterturn, identity3)
    certified_jde = sp.Matrix(quarterturn_hessian["finite_data"]["lane_quarterturn"])

    trace_mode = sp.Matrix([1, 1, 1, 0, 0, 0])
    trace_mode_image = jde * trace_mode
    identity_fixed_residual = trace_mode_image - trace_mode

    root_restrictions = parent_descent["finite_data"][
        "weight1_root_restriction_i_exponents"
    ]
    transposition_rows = [
        row
        for row in same_source_map["finite_data"]["class_table"]
        if row["cycle_type"] == "transposition"
    ]

    checks = {
        "exterior_square_is_sign_twisted_sheet_permutation": all(
            sp.Matrix(record["exterior_square_matrix"])
            == record["sign"] * sp.Matrix(record["sheet_matrix"])
            for record in records
        ),
        "determinant_twist_turns_oriented_edges_into_unordered_edges": all(
            sp.Matrix(record["determinant_twisted_exterior_matrix"])
            == sp.Matrix(record["sheet_matrix"])
            for record in records
        ),
        "shared_SpinC_determinant_is_root_independent_sign_line": (
            determinant_bridge["claim_tiers"][
                "SpinC_determinant_shared_line_flat_connection_identification"
            ]
            == "CLOSED_FOR_THE_UNIQUE_NONTRIVIAL_CENTRAL_MAP"
            and determinant_bridge["claim_tiers"][
                "chi1_vs_chi33_selection_needed_for_determinant"
            ]
            == "NO"
        ),
        "same_source_transpositions_emit_shared_halfturn": (
            len(transposition_rows) == 3
            and all(row["Z64_image"] == 32 for row in transposition_rows)
            and same_source_map["claim_tiers"][
                "finite_same_source_q79_to_Z64_monodromy_map"
            ]
            == "CLOSED_UNIQUE"
        ),
        "both_odd_roots_restrict_to_same_C4_quarterturn": root_restrictions
        == {"1": [0, 1, 2, 3], "33": [0, 1, 2, 3]},
        "rootplane_realification_is_integral_quarterturn": (
            root_quarterturn == sp.Matrix([[0, -1], [1, 0]])
            and root_quarterturn**2 == -sp.eye(2)
            and root_quarterturn.T * root_quarterturn == sp.eye(2)
        ),
        "rootplane_tensor_sheet_is_exact_certified_JDE": jde == certified_jde,
        "JDE_is_orthogonal_complex_structure": (
            jde**2 == -sp.eye(6) and jde.T * jde == sp.eye(6)
        ),
        "JDE_commutes_with_every_S3_holonomy": all(
            jde * action == action * jde for action in s3_actions
        ),
        "minimal_rootstack_flat_connection_intertwines_sheet_symbol": (
            rootstack_bridge["claim_tiers"][
                "rootstack_rank_six_strain_bundle_isomorphism"
            ]
            == "CLOSED_EXACT"
            and rootstack_bridge["claim_tiers"][
                "rootstack_flat_HYM_connection_intertwining"
            ]
            == "CLOSED_EXACT"
        ),
        "positive_atom_complement_is_unique": rootstack_bridge["finite_data"][
            "equivariant_atom_bijection_count"
        ]
        == 1,
        "no_direct_unital_Herm3_automorphism_can_equal_full_JDE": (
            identity_fixed_residual != sp.zeros(6, 1)
            and list(trace_mode_image) == [0, 0, 0, 1, 1, 1]
        ),
        "square_theta_direct_adjoint_was_already_excluded": square_theta_nogo[
            "claim_tiers"
        ]["direct_theta_adjoint_realizes_six_dimensional_JDE"]
        == "CLOSED_NO_GO",
        "actual_inverse_Fourier_Mukai_HYM_operator_remains_open": (
            rootstack_bridge["claim_tiers"][
                "inverse_Fourier_Mukai_HYM_Hessian_intertwining"
            ]
            == "OPEN"
            and parent_descent["claim_tiers"][
                "actual_inverse_Fourier_Mukai_HYM_operator"
            ]
            == "OPEN"
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_shared_rootplane_twisted_exterior_jde_functor",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_SHARED_ROOTPLANE_TWISTED_EXTERIOR_JDE_FUNCTOR_CLOSED_ON_FLAT_ROOTSTACK_SYMBOL_ACTUAL_FM_HYM_INVARIANCE_AND_LENS_TYPING_OPEN",
        "inputs": {
            "determinant_bridge": str(DETERMINANT_BRIDGE),
            "same_source_map": str(SAME_SOURCE_MAP),
            "rootstack_bridge": str(ROOTSTACK_BRIDGE),
            "quarterturn_hessian": str(QUARTERTURN_HESSIAN),
            "parent_descent": str(PARENT_DESCENT),
            "square_theta_no_go": str(SQUARE_THETA_NOGO),
        },
        "checks": checks,
        "finite_data": {
            "S3_twisted_exterior_records": records,
            "shared_C4_subgroup": parent_descent["finite_data"][
                "Z64_order4_subgroup"
            ],
            "shared_root_real_quarterturn": as_int_rows(root_quarterturn),
            "induced_JDE": as_int_rows(jde),
            "trace_mode": list(map(int, trace_mode)),
            "JDE_trace_mode_image": list(map(int, trace_mode_image)),
            "continuous_fitted_parameters": 0,
        },
        "theorem": {
            "name": "SharedRootPlaneTwistedExteriorJDEFunctor",
            "sheet_edge_functor": {
                "sheet_bundle": "E_D=P_sheet x_S3 R^3_vertex",
                "oriented_edge_bundle": "Lambda^2 E_D=sign tensor E_D",
                "unordered_edge_strain_bundle": (
                    "E_S=det(E_D) tensor Lambda^2 E_D, canonically isomorphic "
                    "to E_D by the positive opposite-edge atom map C"
                ),
                "shared_line": (
                    "det(E_D) is the sheet-sign line already identified with the "
                    "root-independent shared-Z64 SpinC determinant line"
                ),
            },
            "rootplane_functor": {
                "construction": (
                    "Realify either odd shared-Z64 root on C4=<16> and tensor its "
                    "real plane with E_D. Identify the real copy with E_D and the "
                    "imaginary copy with E_S through C."
                ),
                "induced_generator": "J_DE(d,e)=(-C^{-1}e,Cd)",
                "matrix": "[[0,-I3],[I3,0]]",
                "root_independence": (
                    "chi_1 and chi_33 both restrict as i^m on C4, so no root "
                    "choice enters the functor"
                ),
                "globalization": (
                    "J_DE commutes with every S3 sheet holonomy and is therefore "
                    "parallel on the minimal full-monodromy flat root-stack symbol"
                ),
            },
            "direct_action_no_go": {
                "statement": (
                    "Every direct unital unitary or antiunitary adjoint on Herm(3) "
                    "fixes the identity. J_DE sends the diagonal trace mode to the "
                    "off-diagonal edge-sum mode, so no such direct algebra action can "
                    "implement the full six-lane functor."
                ),
                "consequence": (
                    "The required physical symmetry must be an outer/duality functor, "
                    "autonomous Lens descent, or be established by direct HYM execution."
                ),
            },
            "boundary": {
                "closed": (
                    "A typed, root-independent common-source C4 action on the flat "
                    "q79 root-stack strain symbol, exactly equal to J_DE."
                ),
                "open": (
                    "Proof that the nonzero-Chern inverse-Fourier-Mukai HYM operator "
                    "carries this outer action, or that the four Fu-Yau orientations "
                    "are autonomous Lens redundancy."
                ),
            },
        },
        "claim_tiers": {
            "determinant_twisted_exterior_square_edge_identification": "CLOSED_EXACT",
            "shared_root_C4_realification": "CLOSED_EXACT_ROOT_INDEPENDENT",
            "typed_shared_C4_to_rootstack_strain_JDE_functor": "CLOSED_EXACT_ON_FLAT_SHEET_SYMBOL",
            "JDE_parallel_under_minimal_rootstack_flat_connection": "CLOSED_EXACT",
            "direct_unital_Herm3_adjoint_realizes_full_JDE": "CLOSED_NO_GO",
            "shared_C4_to_active_FuYau_parent_representation": "CLOSED_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING",
            "MTT_types_C4_as_Lens_redundancy": "OPEN",
            "actual_inverse_Fourier_Mukai_HYM_induced_JDE": "OPEN",
            "selected_HYM_functional_is_JDE_invariant": "OPEN",
            "actual_projected_HYM_Hessian": "OPEN",
        },
        "guardrails": {
            "claims_flat_symbol_functor_is_full_inverse_Fourier_Mukai_functor": False,
            "claims_actual_nonzero_Chern_HYM_connection_is_flat": False,
            "claims_selected_HYM_functional_is_JDE_invariant": False,
            "claims_MTT_types_C4_as_Lens_redundancy": False,
            "claims_direct_theta_adjoint_was_rescued": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Shared Root-Plane Twisted-Exterior JDE Functor v1

Status:
`Q79_SHARED_ROOTPLANE_TWISTED_EXTERIOR_JDE_FUNCTOR_CLOSED_ON_FLAT_ROOTSTACK_SYMBOL_ACTUAL_FM_HYM_INVARIANCE_AND_LENS_TYPING_OPEN`

## Exact sheet-edge functor

Let `E_D` be the real rank-three sheet-permutation bundle. In the oriented
opposite-edge basis,

```text
Lambda^2 E_D = sign tensor E_D.
```

The determinant line of the permutation bundle is exactly `sign`. Therefore

```text
E_S := det(E_D) tensor Lambda^2 E_D is isomorphic to E_D.
```

This is the unordered opposite-edge strain bundle. The isomorphism is the
unique positive atom map

```text
C(d1,d2,d3)=(s23,s13,s12).
```

All six `S3` matrices are checked exactly. The determinant twist cancels the
orientation sign in every case. The determinant line is already identified by
the q79 SpinC theorem with the shared-Z64 sign line, independently of whether
the odd root is `chi_1` or `chi_33`.

## Shared root plane

The unique shared order-four subgroup and the two odd-root restrictions are

```text
C4=<16>={0,16,32,48},
chi_1(16m)=chi_33(16m)=i^m.
```

Realify this root character and tensor its real two-plane with `E_D`. Identify
the real copy with `E_D` and the imaginary copy with `E_S` through `C`.
Multiplication by `i` then induces

```text
J_DE(d,e)=(-C^{-1}e,Cd),
J_DE=[[0,-I3],[I3,0]].
```

This is exactly the previously certified lane quarter-turn, with no fitted
number or root choice. It commutes with every `S3` holonomy, hence is a global
parallel action on the minimal full-monodromy flat root-stack strain symbol.

## What this closes

The common-source functor is no longer merely an abstract equality of two
`2x2` matrices. On the flat sheet-symbol carrier it is the determinant-twisted
exterior-square functor tensored with the shared root plane. This gives a typed,
root-independent `C4` action whose generator is exactly `J_DE`.

## Why this is not yet HYM invariance

This construction acts on the finite sheet/Weyl symbol. It does not identify
that flat symbol connection with the nonzero-Chern inverse-Fourier-Mukai HYM
connection. Nor can the functor be replaced by direct conjugation on `Herm(3)`:
every unital unitary or antiunitary adjoint fixes the identity, whereas `J_DE`
sends the diagonal trace mode to the off-diagonal edge-sum mode. The earlier
square-theta direct-adjoint no-go is therefore an instance of a wider direct
algebra-action obstruction.

The remaining physical fork is exact:

```text
1. prove the actual inverse-Fourier-Mukai/HYM operator carries this outer
   twisted-exterior action and its Hessian is invariant;
2. prove C4 is autonomous Lens redundancy so the HYM operator descends;
3. compute the projected HYM block directly.
```
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
