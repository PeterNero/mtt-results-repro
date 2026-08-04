from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"

ROOTPLANE_FUNCTOR = (
    ROOT
    / "certificates"
    / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
)
SPECTRAL_SYMBOL = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
SPECTRAL_COVER = (
    SM_REPO
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "q79_genus_two_determinant_zero_spectral_cover.packet.json"
)
NORMALIZED_POINCARE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79normalizedpoincaregerbeandpgl3prymreduction"
    / "normalized_Poincare_gerbe_Prym_reduction.packet.json"
)
INTEGRAL_DD = (
    SM_REPO
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "integral_DD_restriction.packet.json"
)
HYM_GATE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "HYM_Bianchi_execution_gate.packet.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Ordinary_Exterior_Dual_HYM_NoGo_and_Derived_Kernel_Cutset_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_unit(row: int, column: int) -> sp.Matrix:
    result = sp.zeros(3)
    result[row, column] = 1
    return result


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


def hermitian_bases() -> tuple[list[sp.Matrix], ...]:
    diagonal = [matrix_unit(index, index) for index in range(3)]
    pairs = [(1, 2), (0, 2), (0, 1)]
    symmetric = [
        (matrix_unit(i, j) + matrix_unit(j, i)) / sp.sqrt(2)
        for i, j in pairs
    ]
    skew_hermitian_coordinates = [
        sp.I * (matrix_unit(i, j) - matrix_unit(j, i)) / sp.sqrt(2)
        for i, j in pairs
    ]
    return diagonal, symmetric, skew_hermitian_coordinates


def hilbert_schmidt(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(left.conjugate().T * right))


def action_matrix(
    transform, basis: list[sp.Matrix]
) -> sp.Matrix:
    return sp.Matrix.hstack(
        *[
            sp.Matrix(
                [hilbert_schmidt(reference, transform(atom)) for reference in basis]
            )
            for atom in basis
        ]
    )


def as_rows(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(sp.simplify(value)) for value in row] for row in matrix.tolist()]


def main() -> None:
    rootplane = load(ROOTPLANE_FUNCTOR)
    spectral_symbol = load(SPECTRAL_SYMBOL)
    spectral_cover = load(SPECTRAL_COVER)
    normalized_poincare = load(NORMALIZED_POINCARE)
    integral_dd = load(INTEGRAL_DD)
    hym_gate = load(HYM_GATE)

    diagonal, symmetric, skew = hermitian_bases()
    full_basis = diagonal + symmetric + skew
    tracefree_diagonal = [
        (diagonal[0] - diagonal[1]) / sp.sqrt(2),
        (diagonal[0] + diagonal[1] - 2 * diagonal[2]) / sp.sqrt(6),
    ]
    su3_hermitian_basis = tracefree_diagonal + symmetric + skew

    def dual_differential(matrix: sp.Matrix) -> sp.Matrix:
        return -matrix.T

    def exterior_differential(matrix: sp.Matrix) -> sp.Matrix:
        return sp.trace(matrix) * sp.eye(3) - matrix.T

    dual_action = action_matrix(dual_differential, full_basis)
    exterior_action = action_matrix(exterior_differential, full_basis)
    dual_su3_action = action_matrix(dual_differential, su3_hermitian_basis)
    exterior_su3_action = action_matrix(exterior_differential, su3_hermitian_basis)

    t = sp.symbols("t", real=True)
    symbols = sp.symbols("x0:9")
    generic = sp.Matrix(3, 3, symbols)
    group_exterior = exterior_square(sp.eye(3) + t * generic)
    computed_exterior_derivative = group_exterior.diff(t).subs(t, 0)
    formula_exterior_derivative = sp.trace(generic) * sp.eye(3) - generic.T

    expected_dual_action = sp.diag(*([-1] * 6 + [1] * 3))
    expected_exterior_diagonal = sp.ones(3) - sp.eye(3)
    expected_exterior_action = sp.diag(expected_exterior_diagonal, -sp.eye(3), sp.eye(3))
    expected_su3_action = sp.diag(*([-1] * 5 + [1] * 3))

    jde = sp.Matrix(rootplane["finite_data"]["induced_JDE"])
    dual_strain_action = dual_action[:6, :6]
    exterior_strain_action = exterior_action[:6, :6]

    projection_d = sp.diag(1, 1, 1, 0, 0, 0)
    projection_s = sp.eye(6) - projection_d
    offblock_dual = projection_d * dual_strain_action * projection_s
    offblock_dual += projection_s * dual_strain_action * projection_d
    offblock_exterior = projection_d * exterior_strain_action * projection_s
    offblock_exterior += projection_s * exterior_strain_action * projection_d

    reference_c3 = spectral_cover["sectioned_reference_FMW_check"]["integral_c3"]
    dual_reference_c3 = -reference_c3

    visible_gate = hym_gate["visible_bundle_chain"]
    derived_kernel_contract = {
        "normalized_relative_Poincare_gerbe": {
            "required": True,
            "available": normalized_poincare["base_Brauer_normalization"][
                "normalization_unique"
            ],
        },
        "integral_DD_restriction_zero": {
            "required": True,
            "available": integral_dd["restriction_pairing"][
                "integral_DD_restriction_zero"
            ],
        },
        "holomorphic_Prym_gerbe_trivialization": {
            "required": True,
            "available": visible_gate["holomorphic_gerbe_trivialization"],
        },
        "inverse_gerbe_twisted_rank_one_spectral_sheaf": {
            "required": True,
            "available": visible_gate["rank_one_twisted_spectral_object"],
        },
        "WIT_index_and_locally_free_rank3_inverse_transform": {
            "required": True,
            "available": visible_gate["locally_free_rank3_inverse_transform"],
        },
        "determinant_zero_and_actual_total_space_c3": {
            "required": True,
            "available": (
                visible_gate["SU3_determinant_condition"]
                and visible_gate["actual_total_space_c3_plusminus6"]
            ),
        },
        "balanced_stability_and_HYM_connection": {
            "required": True,
            "available": (
                visible_gate["balanced_slope_stability"]
                and visible_gate["balanced_HYM_connection"]
            ),
        },
        "same_branch_FM_autoequivalence_stabilizing_Chern_character": {
            "required": True,
            "available": False,
        },
        "induced_real_map_on_selected_Ext1_six_plane": {
            "required": True,
            "available": False,
        },
        "induced_map_equals_JDE_and_squares_to_minus_identity": {
            "required": True,
            "available": False,
        },
        "L2_Gram_and_projected_Hessian_intertwining": {
            "required": True,
            "available": False,
        },
    }
    available_contract_rows = sum(
        bool(row["available"]) for row in derived_kernel_contract.values()
    )

    checks = {
        "exterior_square_group_derivative_is_trace_minus_transpose": (
            sp.simplify(computed_exterior_derivative - formula_exterior_derivative)
            == sp.zeros(3)
        ),
        "dual_differential_action_is_exact": dual_action == expected_dual_action,
        "exterior_differential_action_is_exact": (
            exterior_action == expected_exterior_action
        ),
        "dual_and_exterior_agree_on_su3_tracefree_sector": (
            dual_su3_action == expected_su3_action
            and exterior_su3_action == expected_su3_action
        ),
        "tracefree_action_is_Hilbert_Schmidt_isometry": (
            dual_su3_action.T * dual_su3_action == sp.eye(8)
            and exterior_su3_action.T * exterior_su3_action == sp.eye(8)
        ),
        "ordinary_functors_preserve_D_S_K_sectors": (
            offblock_dual == sp.zeros(6) and offblock_exterior == sp.zeros(6)
        ),
        "ordinary_dual_is_involution_not_quarterturn": (
            dual_strain_action**2 == sp.eye(6) and jde**2 == -sp.eye(6)
        ),
        "ordinary_exterior_is_not_JDE": exterior_strain_action != jde,
        "ordinary_dual_is_not_JDE": dual_strain_action != jde,
        "JDE_exchanges_D_and_S_while_ordinary_functors_do_not": (
            projection_d * jde * projection_d == sp.zeros(6)
            and projection_s * jde * projection_s == sp.zeros(6)
            and offblock_dual == sp.zeros(6)
            and offblock_exterior == sp.zeros(6)
        ),
        "dualization_flips_reference_c3": (
            reference_c3 == 6 and dual_reference_c3 == -6
        ),
        "nonzero_c3_excludes_complex_linear_self_duality": (
            reference_c3 != dual_reference_c3
        ),
        "flat_symbol_functor_was_not_already_promoted": (
            rootplane["claim_tiers"][
                "actual_inverse_Fourier_Mukai_HYM_induced_JDE"
            ]
            == "OPEN"
        ),
        "literal_full_connection_identity_was_already_excluded": (
            spectral_symbol["claim_tiers"][
                "literal_full_inverse_Fourier_Mukai_HYM_connection_identity"
            ]
            == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION"
        ),
        "q79_FM_construction_is_still_upstream_of_actual_HYM": (
            available_contract_rows == 2
            and not visible_gate["locally_free_rank3_inverse_transform"]
            and not visible_gate["balanced_HYM_connection"]
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_ORDINARY_EXTERIOR_DUAL_HYM_COVARIANCE_CLOSED_SAME_BRANCH_JDE_EXTENSION_CLOSED_NOGO_NONLOCAL_DERIVED_KERNEL_PATH_EXACTLY_TYPED_OPEN",
        "inputs": {
            "rootplane_functor": str(ROOTPLANE_FUNCTOR),
            "spectral_symbol": str(SPECTRAL_SYMBOL),
            "spectral_cover": str(SPECTRAL_COVER),
            "normalized_Poincare": str(NORMALIZED_POINCARE),
            "integral_DD": str(INTEGRAL_DD),
            "HYM_gate": str(HYM_GATE),
        },
        "checks": checks,
        "finite_data": {
            "basis_order": ["D11", "D22", "D33", "S23", "S13", "S12", "K23", "K13", "K12"],
            "dual_differential_action": as_rows(dual_action),
            "exterior_square_differential_action": as_rows(exterior_action),
            "tracefree_su3_action": as_rows(expected_su3_action),
            "ordinary_dual_strain_action": as_rows(dual_strain_action),
            "ordinary_exterior_strain_action": as_rows(exterior_strain_action),
            "desired_JDE": as_rows(jde),
            "reference_c3": reference_c3,
            "dual_reference_c3": dual_reference_c3,
            "derived_kernel_contract": derived_kernel_contract,
            "derived_kernel_contract_rows_available": available_contract_rows,
            "derived_kernel_contract_rows_required": len(derived_kernel_contract),
            "continuous_fitted_parameters": 0,
        },
        "theorem": {
            "name": "OrdinaryExteriorDualHYMCovarianceNoGoAndDerivedKernelCutset",
            "ordinary_HYM_covariance": {
                "connection_formula": "A_dual=-A^T; A_Lambda2=tr(A)I-A^T",
                "curvature_formula": "F_dual=-F^T; F_Lambda2=tr(F)I-F^T",
                "SU3_reduction": "tr(F)=0, hence both induced curvatures are -F^T",
                "consequence": "Type (1,1), primitivity, and the Hilbert-Schmidt Yang-Mills norm are preserved under dual/exterior-square transport.",
            },
            "sector_no_go": {
                "statement": "On Herm(3)=D direct-sum S direct-sum K, ordinary duality acts as (-I3,-I3,+I3), while exterior-square acts as (ones(3)-I3,-I3,+I3). Both preserve D, S, and K. Neither exchanges D with S, neither equals J_DE, and ordinary duality squares to +I rather than -I.",
                "consequence": "The closed flat sheet-symbol twisted-exterior construction cannot be promoted by applying the ordinary bundle dual or exterior-square functor to one HYM bundle.",
            },
            "chirality_obstruction": {
                "formula": "c_k(V*)=(-1)^k c_k(V)",
                "application": "c3(V*)=-c3(V); the reference chiral branch has c3=6 and its dual has c3=-6.",
                "self_duality_no_go": "On a compact connected complex threefold, complex-linear V isomorphic to V* would force c3(V)=0. Thus a nonzero-c3 chiral branch cannot supply the required global V-to-V* identification.",
                "branch_pair_boundary": "Duality may relate opposite-chirality branches with equal HYM energy, but free branch-pair covariance does not imply one selected branch has a J_DE-invariant Hessian.",
            },
            "derived_exit": {
                "statement": "A surviving extension must be a genuinely nonlocal same-branch Fourier-Mukai autoequivalence (or an independently proved physical descent), not ordinary dual/exterior transport.",
                "acceptance_test": "Construct the listed kernel contract, exhibit the induced real map on the selected six-dimensional Ext1/deformation plane, verify T=J_DE and T^2=-I, and prove both L2-Gram and projected-Hessian intertwining while stabilizing the same Chern character.",
            },
        },
        "claim_tiers": {
            "ordinary_dual_and_exterior_square_preserve_HYM_equations": "CLOSED_EXACT",
            "ordinary_dual_and_exterior_square_preserve_HYM_norm": "CLOSED_EXACT_ON_TRACEFREE_SU3_SECTOR",
            "ordinary_dual_or_exterior_square_realizes_JDE": "CLOSED_NO_GO",
            "ordinary_functor_preserves_D_S_K_sectors": "CLOSED_EXACT",
            "nonzero_c3_branch_is_complex_linearly_self_dual": "CLOSED_NO_GO",
            "ordinary_duality_relates_opposite_c3_branches": "CLOSED_EXACT",
            "opposite_branch_HYM_energy_equality_implies_selected_branch_Hessian_JDE_invariance": "CLOSED_NON_SEQUITUR",
            "nonlocal_same_branch_Fourier_Mukai_JDE_autoequivalence": "OPEN_EXACT_KERNEL_AND_EXT1_CONTRACT_EMITTED",
            "actual_q79_inverse_Fourier_Mukai_visible_bundle": "OPEN_UPSTREAM_GERBE_SHEAF_WIT_LOCAL_FREENESS",
            "actual_q79_balanced_HYM_connection": "OPEN",
            "selected_projected_HYM_Hessian_is_JDE_invariant": "OPEN",
        },
        "guardrails": {
            "claims_derived_equivalence_preserves_the_physical_HYM_metric_automatically": False,
            "claims_opposite_chirality_branch_is_same_selected_branch": False,
            "claims_reference_sectioned_c3_is_actual_FuYau_total_space_c3": False,
            "claims_flat_symbol_functor_is_actual_HYM_functor": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "primary_references": [
            "https://arxiv.org/abs/alg-geom/9709029",
            "https://arxiv.org/abs/math/0012083",
            "https://arxiv.org/abs/1008.3365",
        ],
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Ordinary Exterior/Dual HYM No-Go and Derived-Kernel Cutset v1

Status:
`Q79_ORDINARY_EXTERIOR_DUAL_HYM_COVARIANCE_CLOSED_SAME_BRANCH_JDE_EXTENSION_CLOSED_NOGO_NONLOCAL_DERIVED_KERNEL_PATH_EXACTLY_TYPED_OPEN`

## The standard HYM functors

For a rank-three connection, the dual and exterior-square differentials are

```text
A -> -A^T,
A -> tr(A) I - A^T.
```

The second identity is derived exactly in the executable certificate by
differentiating `Lambda^2(I+tA)` in the oriented opposite-edge basis. The same
formulas hold for curvature. On an `SU(3)` connection `tr(F)=0`, so both give
`-F^T`. They preserve type `(1,1)`, primitivity, and the Hilbert-Schmidt norm.
Thus ordinary dual/exterior transport really does preserve the HYM equations.

That valid statement is not the needed quarter-turn.

## Exact sector action

Use the ordered Hermitian basis

```text
(D11,D22,D33 ; S23,S13,S12 ; K23,K13,K12).
```

Ordinary duality acts as

```text
(-I3, -I3, +I3),
```

and exterior square acts as

```text
(ones(3)-I3, -I3, +I3).
```

Both preserve `D`, `S`, and `K` separately. The required map instead is

```text
J_DE(d,s)=(-s,d),
J_DE^2=-I.
```

Therefore neither ordinary functor equals `J_DE`. Ordinary duality is an
involution, and exterior square also has no diagonal/edge exchange. This closes
the most obvious attempted extension of the flat twisted-exterior symbol.

## The chirality obstruction

For any complex bundle,

```text
c_k(V*)=(-1)^k c_k(V).
```

Consequently `c3(V*)=-c3(V)`. The sectioned q79 reference branch has `c3=6`,
so its dual has `c3=-6`. More generally, any intended chiral branch with
nonzero `c3` cannot be complex-linearly self-dual on a compact connected
complex threefold: `V isomorphic to V*` would force `2 c3=0`, hence `c3=0` in
the torsion-free top cohomology.

Duality can relate opposite-chirality branches and gives them equal HYM energy.
It does not act within one selected chiral branch and does not force that
branch's projected Hessian to be `J_DE` invariant.

## What survives

The remaining Fourier-Mukai route must be genuinely nonlocal. A valid
same-branch construction must provide all of the following:

1. the normalized relative Poincare gerbe and vanishing integral restriction;
2. a holomorphic Prym-gerbe trivialization;
3. an inverse-gerbe twisted rank-one spectral sheaf;
4. its WIT index and locally free rank-three inverse transform;
5. determinant zero, actual total-space `c3`, balanced stability, and HYM;
6. a same-branch Fourier-Mukai autoequivalence stabilizing the Chern character;
7. its real action on the selected six-dimensional `Ext1`/deformation plane;
8. exact checks `T=J_DE`, `T^2=-I`, and preservation of the `L2` Gram form and
   projected HYM Hessian.

The current q79 packets close only the first two topological inputs: normalized
Poincare data and integral Dixmier-Douady restriction zero. They do not yet
emit the holomorphic trivialization, spectral sheaf, locally free transform, or
balanced HYM connection. The certificate records this as `2/11`, rather than
mistaking a categorical Fourier-Mukai availability theorem for the selected
physical operator.

## Consequence for the GR program

The ordinary bundle-functor route is now closed no-go. The live choices are:

```text
nonlocal same-branch Fourier-Mukai autoequivalence satisfying the 11-row test,
autonomous Lens/modular descent with the selected structures,
or direct computation of the projected 2x2 HYM Hessian.
```

No measured value and no fitted parameter is used.

## Primary references

- Friedman, Morgan, and Witten, [Vector Bundles over Elliptic Fibrations](https://arxiv.org/abs/alg-geom/9709029)
- Caldararu, [Derived Categories of Twisted Sheaves on Elliptic Threefolds](https://arxiv.org/abs/math/0012083)
- Brinzanescu, Halanay, and Trautmann, [Vector Bundles on non-Kahler Elliptic Principal Bundles](https://arxiv.org/abs/1008.3365)
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
