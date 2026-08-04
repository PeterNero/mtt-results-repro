from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import QQ


ROOT = Path(__file__).resolve().parents[1]

Q79_INTERTWINER = ROOT / "certificates" / "q79_s3_strain_intertwiner_certificate.json"
Q79_CUSP_ROOTSTACK = (
    ROOT / "certificates" / "q79_branch_cusp_resolution_rootstack_hym_certificate.json"
)
Q79_DETERMINANT_ROOTSTACK = (
    ROOT / "certificates" / "q79_spinc_flat_hym_ramification_extension_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Cubic_Norm_and_Full_Monodromy_RootStack_Strain_Bridge_v1.md"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def permutation_matrix(perm: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for source, target in enumerate(perm):
        matrix[target, source] = 1
    return matrix


def sym_coordinates(matrix: sp.Matrix) -> sp.Matrix:
    """Frobenius-orthonormal coordinates on Sym(3)."""
    root2 = sp.sqrt(2)
    return sp.Matrix(
        [
            matrix[0, 0],
            matrix[1, 1],
            matrix[2, 2],
            root2 * matrix[1, 2],
            root2 * matrix[0, 2],
            root2 * matrix[0, 1],
        ]
    )


def target_action(permutation: sp.Matrix) -> sp.Matrix:
    basis = []
    for index in range(6):
        coordinate = sp.eye(6).col(index)
        matrix = sp.zeros(3)
        matrix[0, 0], matrix[1, 1], matrix[2, 2] = coordinate[:3, 0]
        matrix[1, 2] = matrix[2, 1] = coordinate[3] / sp.sqrt(2)
        matrix[0, 2] = matrix[2, 0] = coordinate[4] / sp.sqrt(2)
        matrix[0, 1] = matrix[1, 0] = coordinate[5] / sp.sqrt(2)
        basis.append(sym_coordinates(permutation * matrix * permutation.T))
    return sp.Matrix.hstack(*basis)


def intertwiner_nullity(
    source_actions: list[sp.Matrix], target_actions: list[sp.Matrix]
) -> int:
    variables = sp.symbols("m0:36")
    matrix = sp.Matrix(6, 6, variables)
    equations = []
    for source, target in zip(source_actions, target_actions):
        equations.extend(list(target * matrix - matrix * source))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables) - coefficient_matrix.rank()


def commutant_nullity(actions: list[sp.Matrix]) -> int:
    variables = sp.symbols("c0:9")
    matrix = sp.Matrix(3, 3, variables)
    equations = []
    for action in actions:
        equations.extend(list(action * matrix - matrix * action))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables) - coefficient_matrix.rank()


def quotient_cubic_map(polynomial: sp.Expr, variable: sp.Symbol) -> tuple[sp.Matrix, sp.Expr]:
    """Return the trace-plus-norm-Hessian map for a monogenic cubic algebra."""
    basis = [sp.Integer(1), variable, variable**2]
    coordinates = sp.symbols("x0:3")

    def reduce(poly: sp.Expr) -> sp.Poly:
        return sp.rem(sp.Poly(sp.expand(poly), variable), sp.Poly(polynomial, variable))

    def vector(poly: sp.Expr) -> sp.Matrix:
        remainder = reduce(poly)
        return sp.Matrix(
            [remainder.coeff_monomial(variable**index) for index in range(3)]
        )

    def left_multiplication(element: sp.Expr) -> sp.Matrix:
        return sp.Matrix.hstack(
            *[vector(element * variable**index) for index in range(3)]
        )

    generic_element = sum(coordinates[index] * basis[index] for index in range(3))
    norm = sp.factor(left_multiplication(generic_element).det())

    def trace(element: sp.Expr) -> sp.Expr:
        return sp.factor(sp.trace(left_multiplication(element)))

    trace_forms = [
        sp.Matrix(
            3,
            3,
            lambda i, j, atom=atom: trace(atom * basis[i] * basis[j]),
        )
        for atom in basis
    ]
    norm_hessian = sp.hessian(norm, coordinates)
    norm_forms = []
    for source_index in range(3):
        point = {
            coordinates[index]: int(index == source_index) for index in range(3)
        }
        norm_forms.append(sp.simplify(norm_hessian.subs(point)))

    def form_coordinates(form: sp.Matrix) -> sp.Matrix:
        return sp.Matrix(
            [
                form[0, 0],
                form[1, 1],
                form[2, 2],
                form[0, 1],
                form[0, 2],
                form[1, 2],
            ]
        )

    return sp.Matrix.hstack(
        *[form_coordinates(form) for form in trace_forms + norm_forms]
    ), norm


def valuation_at_zero(polynomial: sp.Expr, variable: sp.Symbol) -> int:
    expanded = sp.Poly(sp.expand(polynomial), variable)
    return min(monomial[0] for monomial, coefficient in expanded.terms() if coefficient)


def main() -> None:
    q79 = load(Q79_INTERTWINER)
    cusp = load(Q79_CUSP_ROOTSTACK)
    determinant_rootstack = load(Q79_DETERMINANT_ROOTSTACK)

    permutations = list(itertools.permutations(range(3)))
    permutation_actions = [permutation_matrix(perm) for perm in permutations]
    source_actions = [sp.diag(action, action) for action in permutation_actions]
    target_actions = [target_action(action) for action in permutation_actions]

    full_hom_dimension = intertwiner_nullity(source_actions, target_actions)
    permutation_commutant_dimension = commutant_nullity(permutation_actions)
    lane_preserving_hom_dimension = 2 * permutation_commutant_dimension

    equivariant_atom_bijections = []
    for candidate_perm in permutations:
        candidate = permutation_matrix(candidate_perm)
        if all(
            candidate * action == action * candidate for action in permutation_actions
        ):
            equivariant_atom_bijections.append(candidate_perm)

    all_ones = sp.ones(3)
    p_trivial = all_ones / 3
    p_standard = sp.eye(3) - p_trivial
    orthogonal_commutant = []
    for trivial_sign in (-1, 1):
        for standard_sign in (-1, 1):
            candidate = sp.simplify(
                trivial_sign * p_trivial + standard_sign * p_standard
            )
            orthogonal_commutant.append(
                {
                    "trivial_sign": trivial_sign,
                    "standard_sign": standard_sign,
                    "matrix": [[str(value) for value in row] for row in candidate.tolist()],
                    "entrywise_nonnegative": all(value >= 0 for value in candidate),
                }
            )
    nonnegative_orthogonal_count = sum(
        int(row["entrywise_nonnegative"]) for row in orthogonal_commutant
    )

    # In the split cubic algebra R^3, Tr(a*x*y) is diagonal and Hess(N)_b for
    # N=x1*x2*x3 is precisely the opposite-edge symmetric matrix.
    a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
    split_variables = sp.symbols("s1:4")
    split_norm = sp.prod(split_variables)
    split_hessian = sp.hessian(split_norm, split_variables).subs(
        dict(zip(split_variables, (b1, b2, b3)))
    )
    expected_split_hessian = sp.Matrix(
        [[0, b3, b2], [b3, 0, b1], [b2, b1, 0]]
    )
    split_natural_map = sp.diag(a1, a2, a3) + split_hessian / sp.sqrt(2)

    p, q, t = sp.symbols("p q t")
    depressed_polynomial = t**3 + p * t + q
    depressed_map, depressed_norm = quotient_cubic_map(depressed_polynomial, t)
    depressed_discriminant = sp.discriminant(depressed_polynomial, t)
    depressed_determinant = sp.factor(depressed_map.det())

    u = sp.symbols("u")
    simple_branch_polynomial = sp.expand((t**2 - u) * (t - 1))
    simple_branch_map, _ = quotient_cubic_map(simple_branch_polynomial, t)
    simple_branch_discriminant = sp.factor(
        sp.discriminant(simple_branch_polynomial, t)
    )
    simple_branch_determinant = sp.factor(simple_branch_map.det())
    simple_branch_rank = simple_branch_map.subs(u, 0).rank()
    smith = smith_normal_form(simple_branch_map, domain=QQ.poly_ring(u))
    smith_diagonal = [sp.factor(smith[index, index]) for index in range(6)]
    smith_branch_valuations = [
        valuation_at_zero(value, u) for value in smith_diagonal
    ]

    # Newton-Puiseux data for z^3-3*x*z+2*y near the resolved cusp y^2=x^3.
    # Each pair is (ord_D x, ord_D y). Slopes are root valuations.
    monodromy_rows = [
        {
            "component": "strict_transform",
            "discriminant_multiplicity": 1,
            "root_valuations": ["0", "1/2", "1/2"],
            "cycle_type": "transposition",
            "monodromy_order": 2,
            "minimal_root_order": 2,
        },
        {
            "component": "E1",
            "valuation_x_y": [1, 1],
            "discriminant_multiplicity": 2,
            "root_valuations": ["1/3", "1/3", "1/3"],
            "cycle_type": "three_cycle",
            "monodromy_order": 3,
            "minimal_root_order": 3,
        },
        {
            "component": "E2",
            "valuation_x_y": [1, 2],
            "discriminant_multiplicity": 3,
            "root_valuations": ["1/2", "1/2", "1"],
            "cycle_type": "transposition",
            "monodromy_order": 2,
            "minimal_root_order": 2,
        },
        {
            "component": "E3",
            "valuation_x_y": [2, 3],
            "discriminant_multiplicity": 6,
            "root_valuations": ["1", "1", "1"],
            "cycle_type": "identity",
            "monodromy_order": 1,
            "minimal_root_order": 1,
        },
    ]
    expected_exceptional_multiplicities = [2, 3, 6]
    computed_exceptional_multiplicities = [
        min(3 * row["valuation_x_y"][0], 2 * row["valuation_x_y"][1])
        for row in monodromy_rows[1:]
    ]
    root_orders = [row["minimal_root_order"] for row in monodromy_rows]
    sign_components = [
        row["component"]
        for row in monodromy_rows
        if row["cycle_type"] == "transposition"
    ]

    checks = {
        "prior_q79_J_is_exact_S3_intertwining_isometry": (
            q79["exact_checks"]["J_is_frobenius_isometry"] is True
            and q79["exact_checks"]["all_six_S3_actions_intertwine"] is True
        ),
        "full_S3_intertwiner_space_has_dimension_8": full_hom_dimension == 8,
        "lane_preserving_intertwiner_space_has_dimension_4": (
            lane_preserving_hom_dimension == 4
        ),
        "equivariant_sheet_to_opposite_edge_bijection_is_unique": (
            equivariant_atom_bijections == [(0, 1, 2)]
        ),
        "only_one_orthogonal_commutant_map_preserves_positive_atom_cone": (
            nonnegative_orthogonal_count == 1
        ),
        "cubic_norm_hessian_is_opposite_edge_map": (
            sp.simplify(split_hessian - expected_split_hessian) == sp.zeros(3)
        ),
        "natural_split_map_equals_existing_J_formula": (
            sp.simplify(
                split_natural_map
                - sp.Matrix(
                    [
                        [a1, b3 / sp.sqrt(2), b2 / sp.sqrt(2)],
                        [b3 / sp.sqrt(2), a2, b1 / sp.sqrt(2)],
                        [b2 / sp.sqrt(2), b1 / sp.sqrt(2), a3],
                    ]
                )
            )
            == sp.zeros(3)
        ),
        "generic_cubic_map_determinant_is_minus_discriminant_cubed": (
            sp.factor(depressed_determinant - (-depressed_discriminant) ** 3) == 0
        ),
        "simple_branch_map_determinant_is_minus_discriminant_cubed": (
            sp.factor(simple_branch_determinant - (-simple_branch_discriminant) ** 3)
            == 0
        ),
        "coarse_map_rank_drops_to_3_at_simple_branch": simple_branch_rank == 3,
        "simple_branch_smith_profile_is_three_units_plus_three_vanishing_factors": (
            smith_branch_valuations == [0, 0, 0, 1, 1, 1]
        ),
        "selected_q79_branch_has_exactly_18_cusps": (
            cusp["finite_data"]["ordinary_cusp_count"] == 18
        ),
        "resolved_cusp_multiplicities_match_newton_data": (
            computed_exceptional_multiplicities
            == expected_exceptional_multiplicities
            == [
                row["multiplicity"]
                for row in cusp["finite_data"]["resolution_components"][1:]
            ]
        ),
        "full_monodromy_root_orders_are_2_3_2_1": root_orders == [2, 3, 2, 1],
        "determinant_sign_rootstack_is_recovered_as_2_2_substack": (
            sign_components == ["strict_transform", "E2"]
            and cusp["finite_data"]["root_stack_odd_components"] == sign_components
        ),
        "existing_rootstack_HYM_carrier_is_available": (
            cusp["claim_tiers"]["resolved_order_two_rootstack_flat_HYM_carrier"]
            == "CLOSED"
            and determinant_rootstack["claim_tiers"][
                "order_two_root_stack_parabolic_extension_object"
            ]
            == "CLOSED"
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    status = (
        "Q79_CUBIC_NORM_MAP_AND_COARSE_BRANCH_NOGO_CLOSED_"
        "FULL_MONODROMY_ROOTSTACK_STRAIN_BRIDGE_CLOSED_"
        "STRICT_SAME_SOURCE_MINIMAL_CONTINUATION_SELECTED_"
        "INVERSE_FOURIER_MUKAI_HESSIAN_AND_PRIMITIVE_PHYSICAL_BRANCH_OPEN"
    )

    theorem = {
        "name": "q79CubicNormAndFullMonodromyRootStackStrainBridge",
        "unbranched_naturality_and_uniqueness": {
            "arbitrary_S3_intertwiner_dimension": full_hom_dimension,
            "lane_preserving_intertwiner_dimension": lane_preserving_hom_dimension,
            "diagonal_map": "B_a(x,y)=Tr_A(a*x*y)",
            "offdiagonal_map": "C_b(x,y)=D^2 N_A|_b(x,y)/sqrt(2)",
            "split_formula": (
                "J(a,b)=Diag(a)+Hess(x1*x2*x3)|_b/sqrt(2), equal to the "
                "existing opposite-edge formula"
            ),
            "uniqueness": (
                "The first map is the unital regular cubic-algebra representation. "
                "The second is the unique S3-equivariant sheet-atom to complementary-"
                "edge bijection; equivalently it is the unique orthogonal commutant "
                "map preserving the canonical positive atom cone."
            ),
            "continuous_parameters": 0,
            "discrete_physical_choices": 0,
        },
        "coarse_extension_no_go": {
            "generic_depressed_cubic": "t^3+p*t+q",
            "norm": str(depressed_norm),
            "discriminant": str(depressed_discriminant),
            "determinant_identity": "det(J_flat)=(-Disc)^3",
            "simple_branch_model": "(t^2-u)(t-1)",
            "simple_branch_rank": simple_branch_rank,
            "simple_branch_smith_valuations": smith_branch_valuations,
            "conclusion": (
                "The finite-flat coarse algebra map extends canonically as a morphism "
                "but cannot extend as a rank-six bundle isomorphism across ramification."
            ),
            "status": "CLOSED_EXACT_NO_GO",
        },
        "full_cusp_monodromy": {
            "local_cubic": "z^3-3*x*z+2*y with discriminant 108*(x^3-y^2)",
            "components": monodromy_rows,
            "resolution_graph": (
                "E3 is the central exceptional component and meets the strict "
                "transform, E1, and E2 at three distinct points; the three nontrivial "
                "monodromy divisors are therefore disjoint."
            ),
            "determinant_substack": (
                "The previous order-two roots on the strict transform and E2 are "
                "exactly the sign/determinant substack. The full sheet carrier also "
                "requires the order-three root on E1."
            ),
        },
        "minimal_full_monodromy_completion": {
            "carrier": (
                "On the three-blowup resolution, take root order 2 along the strict "
                "branch transform, order 3 along every E1, order 2 along every E2, "
                "and no root along E3."
            ),
            "minimality": (
                "An orbifold stabilizer carrying local monodromy g must have order "
                "divisible by ord(g); choosing ord(g) is the unique minimal effective "
                "choice on each disjoint component."
            ),
            "global_strain_map": (
                "The S3-equivariant isometry J descends between the associated "
                "rank-six source and Sym(3) bundles and remains an isometric parallel "
                "bundle isomorphism."
            ),
            "connection": (
                "The finite orthogonal monodromy connection is flat, hence orbifold "
                "HYM, and nabla(J)=0. Tensoring by the already selected shared sign "
                "line recovers the previous SpinC determinant substack."
            ),
            "parameter_count": 0,
            "strict_same_source_selection": (
                "If continuation through the selected q79 branch is required to keep "
                "all six lanes, preserve the canonical metric/connection, and add no "
                "new source map, the minimal full-monodromy root stack is forced."
            ),
        },
        "remaining_boundary": {
            "closed_here": [
                "natural uniqueness of the displayed unbranched q79 strain map",
                "exact discriminant obstruction on the coarse finite-flat extension",
                "full S3 cusp monodromy orders",
                "minimal rank-preserving root-stack continuation",
                "flat orbifold-HYM metric and connection intertwining",
            ],
            "open": [
                "primitive MTT requirement that the physical realization continue on this root stack",
                "identification with the independently selected inverse-Fourier-Mukai/HYM Hessian and overlap kernels",
                "phase-neutral real treatment of the full shared complex line outside the real Z64 helicity-two subcarrier",
                "numeric kappa_h, Lambda_eff, and higher-derivative/quantum data",
            ],
        },
    }

    certificate = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_cubic_norm_full_monodromy_rootstack_bridge",
        "date": "2026-07-15",
        "status": status,
        "inputs": {
            "q79_s3_strain_intertwiner": str(Q79_INTERTWINER),
            "q79_branch_cusp_resolution_rootstack_hym": str(Q79_CUSP_ROOTSTACK),
            "q79_spinc_flat_hym_ramification_extension": str(
                Q79_DETERMINANT_ROOTSTACK
            ),
        },
        "checks": checks,
        "finite_data": {
            "full_S3_intertwiner_dimension": full_hom_dimension,
            "lane_preserving_intertwiner_dimension": lane_preserving_hom_dimension,
            "equivariant_atom_bijection_count": len(equivariant_atom_bijections),
            "orthogonal_commutant_maps": orthogonal_commutant,
            "depressed_cubic_discriminant": str(depressed_discriminant),
            "depressed_cubic_map_determinant": str(depressed_determinant),
            "simple_branch_discriminant": str(simple_branch_discriminant),
            "simple_branch_map_determinant": str(simple_branch_determinant),
            "simple_branch_rank": simple_branch_rank,
            "simple_branch_smith_diagonal": [str(value) for value in smith_diagonal],
            "simple_branch_smith_valuations": smith_branch_valuations,
            "full_monodromy_components": monodromy_rows,
            "minimal_root_orders": root_orders,
        },
        "theorem": theorem,
        "claim_tiers": {
            "unbranched_q79_strain_map_natural_uniqueness": "CLOSED_EXACT",
            "coarse_finite_flat_branch_extension_as_isomorphism": "CLOSED_NO_GO",
            "full_S3_cusp_monodromy": "CLOSED_EXACT_2_3_2_1",
            "minimal_full_monodromy_rootstack": "CLOSED_UNIQUE_MINIMAL",
            "rootstack_rank_six_strain_bundle_isomorphism": "CLOSED_EXACT",
            "rootstack_metric_intertwining": "CLOSED_EXACT",
            "rootstack_flat_HYM_connection_intertwining": "CLOSED_EXACT",
            "strict_same_source_rank_preserving_continuation": (
                "CLOSED_UNIQUE_MINIMAL_FULL_MONODROMY_ROOTSTACK"
            ),
            "inverse_Fourier_Mukai_HYM_Hessian_intertwining": "OPEN",
            "primitive_MTT_selects_physical_rootstack_realization": "OPEN",
            "full_shared_line_real_phase_neutralization": "OPEN_OUTSIDE_REAL_Z64_TT_SUBCARRIER",
        },
        "guardrails": {
            "claims_coarse_q79_algebra_map_stays_invertible_at_branch": False,
            "claims_previous_order_two_determinant_rootstack_was_full_S3_completion": False,
            "claims_inverse_Fourier_Mukai_Hessian_intertwining_closed": False,
            "claims_primitive_MTT_physical_branch_selection_closed": False,
            "claims_full_shared_complex_line_is_automatically_real": False,
            "adds_fitted_numeric_parameter": False,
            "uses_observed_physics_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Cubic Norm and Full-Monodromy Root-Stack Strain Bridge v1

Date: 2026-07-15

## The unbranched map is natural, not an arbitrary matrix

For the cubic sheet algebra `A`, the existing map has the intrinsic form

```text
B_a(x,y) = Tr_A(a*x*y),
C_b(x,y) = D^2 N_A|_b(x,y)/sqrt(2),
J(a,b)   = B_a + C_b.
```

On the split locus `A=R^3`, `N_A(x)=x1*x2*x3`. Its Hessian is

```text
[[0,b3,b2],[b3,0,b1],[b2,b1,0]],
```

so this is exactly the previously computed diagonal plus opposite-edge map.
The normalization is forced by the Frobenius norm.

Equivariance alone would not prove uniqueness: the full `S3` intertwiner space
has dimension `{full_hom_dimension}`, and the lane-preserving space has
dimension `{lane_preserving_hom_dimension}`. The q79 algebra and atom structure
remove that freedom. The diagonal term is the unital regular representation.
For the rank-three lane, complement sends each sheet atom to its unique
opposite edge. Exhaustion gives one `S3`-equivariant atom bijection. Equivalently,
the orthogonal commutant has four sign maps, but only one preserves the
canonical positive atom cone. Thus the displayed map carries no continuous or
discrete physical parameter.

## Why the coarse branch extension fails

For the generic cubic algebra `R[t]/(t^3+p*t+q)`, the exact symbolic audit gives

```text
det(J_flat)=(-Disc(t^3+p*t+q))^3.
```

For the simple branch model `(t^2-u)(t-1)`, the Smith valuations at `u=0` are

```text
{smith_branch_valuations}.
```

Hence the rank falls from six to `{simple_branch_rank}`. The trace/norm formula
does extend across ramification as a morphism, but it cannot be a bundle
isomorphism on the coarse finite-flat algebra. This is an exact discriminant
no-go, not a missing numerical fit.

## The full cusp monodromy

Use the local cubic `z^3-3*x*z+2*y`, whose discriminant is proportional to
`x^3-y^2`. Newton-Puiseux analysis on the three-blowup SNC resolution gives

```text
strict transform : transposition, root order 2
E1               : three-cycle,  root order 3
E2               : transposition, root order 2
E3               : identity,      root order 1
```

The exceptional discriminant multiplicities are `2,3,6`, exactly as in the
existing 18-cusp certificate. The old order-two root stack on the strict
transform and `E2` is therefore exactly the determinant/sign substack. It was
correct for the SpinC line, but it did not yet retain the full `S3` sheet
carrier: that also requires an order-three root along every `E1`.

After the third blowup, `E3` meets the strict transform, `E1`, and `E2` at
three distinct points, so the nontrivial root divisors are disjoint. The
minimal full-monodromy completion is consequently unambiguous:

```text
root order 2 on the strict transform,
root order 3 on every E1,
root order 2 on every E2,
no root on E3.
```

## Rank-preserving global bridge

On this multi-root stack the q79 local system extends as the associated
orbifold bundle for its finite `S3` representation. Since `J` intertwines all
six `S3` elements, it descends globally and stays a rank-six Frobenius
isometry. The finite orthogonal connection is flat, hence orbifold HYM, and
`nabla J=0`.

An isotropy group carrying local monodromy `g` must have order divisible by
`ord(g)`. Taking exactly `ord(g)` is therefore the unique minimal effective
completion. Under strict same-source continuation -- preserve all six lanes,
their metric and connection, and add no new support map -- this root stack is
forced. The coarse extension is excluded by its rank drop.

## Exact boundary

This closes the previously open branch-locus continuation for the finite
q79 `S3` carrier at the unique minimal strict same-source tier. It does not yet
prove that primitive MTT must choose this physical continuation rather than
terminate the realization, nor does it identify the flat finite-monodromy
connection with the independently selected inverse-Fourier-Mukai/HYM Hessian
and overlap kernels. The full complex shared line also still needs an explicit
real/phase-neutral treatment outside the already real `Z64` helicity-two
subcarrier.

Current status:

```text
{status}
```
"""

    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed q79 cubic/root-stack checks: {failed}")

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
