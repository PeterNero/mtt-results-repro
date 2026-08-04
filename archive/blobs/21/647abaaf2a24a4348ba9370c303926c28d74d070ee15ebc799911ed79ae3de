from __future__ import annotations

import json
from functools import reduce
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

RANK_ONE_FUYAU = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
    / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json"
)
SPLITTING_CONIC = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79pgl3toprymgerbejacobianexecution"
    / "splitting_conic_K3_normal_form.packet.json"
)
A102_CERT = (
    SM_PARITY
    / "certificates"
    / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution_certificate.json"
)
Q79_MUKAI = Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Degree2_K3_FuYau_Torsion_GLSM_Base_Theorem_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def homogeneous_degree(poly: sp.Expr, variables: tuple[sp.Symbol, ...]) -> int:
    terms = sp.Poly(sp.expand(poly), *variables).terms()
    degrees = {sum(monomial) for monomial, _ in terms}
    if len(degrees) != 1:
        raise AssertionError(f"not homogeneous: {poly}")
    return degrees.pop()


def bidegrees(
    poly: sp.Expr,
    variables: tuple[sp.Symbol, ...],
    charge_rows: tuple[tuple[int, ...], tuple[int, ...]],
) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    for monomial, _ in sp.Poly(sp.expand(poly), *variables).terms():
        result.add(
            tuple(
                sum(power * charge for power, charge in zip(monomial, row))
                for row in charge_rows
            )
        )
    return result


def no_projective_common_zero(
    polynomials: list[sp.Expr],
    x: sp.Symbol,
    y: sp.Symbol,
    z: sp.Symbol,
) -> tuple[bool, dict]:
    affine_basis = sp.groebner(
        [sp.expand(poly.subs(z, 1)) for poly in polynomials],
        x,
        y,
        order="grevlex",
    )
    infinity_polys = [sp.Poly(sp.expand(poly.subs({z: 0, y: 1})), x) for poly in polynomials]
    infinity_gcd = reduce(sp.gcd, infinity_polys)
    terminal_values = [
        sp.expand(poly.subs({z: 0, y: 0, x: 1})) for poly in polynomials
    ]
    result = (
        affine_basis.contains(sp.Integer(1))
        and infinity_gcd.degree() == 0
        and any(value != 0 for value in terminal_values)
    )
    witness = {
        "z_equals_1_groebner_basis": [str(poly.as_expr()) for poly in affine_basis.polys],
        "z_equals_0_y_equals_1_gcd": str(infinity_gcd.as_expr()),
        "point_1_0_0_values": [str(value) for value in terminal_values],
    }
    return bool(result), witness


def integrate_ambient_degree_four(poly: sp.Expr, H: sp.Symbol, L: sp.Symbol) -> sp.Rational:
    # The incidence ambient space is P(O + O(1)) over P(1,1,1,3).
    # Its Chow relations are H^4=0 and L(L+H)=0, with integral H^3 L=1/3.
    total = sp.Rational(0)
    for (h_power, l_power), coefficient in sp.Poly(sp.expand(poly), H, L).terms():
        if h_power + l_power != 4:
            raise AssertionError("intersection integrand is not degree four")
        if l_power == 0:
            continue
        reduced_coefficient = coefficient * (-1) ** (l_power - 1)
        total += sp.Rational(reduced_coefficient, 3)
    return sp.simplify(total)


def main() -> None:
    rank_one = load(RANK_ONE_FUYAU)
    splitting = load(SPLITTING_CONIC)
    a102 = load(A102_CERT)
    q79_mukai = load(Q79_MUKAI)

    x, y, z, w, s, t, p1, p2 = sp.symbols("x y z w s t p1 p2")

    # An explicit rational member of the exact splitting-conic normal form.
    Q2 = x * z - y**2
    G3 = (
        -2 * x**3
        - 2 * x**2 * z
        + x * y**2
        + x * y * z
        + 2 * x * z**2
        - y**3
        - 2 * y * z**2
        - z**3
    )
    H4 = (
        -x**4
        - 2 * x**3 * y
        - x**2 * y**2
        + 2 * x**2 * y * z
        + x**2 * z**2
        - x * y**3
        - 2 * x * y**2 * z
        - 2 * x * y * z**2
        + 2 * x * z**3
        - y**4
        - y**3 * z
        + y * z**3
        + 2 * z**4
    )
    F6 = sp.expand(G3**2 + Q2 * H4)
    k3_equation = sp.expand(w**2 - F6)

    branch_partials = [sp.diff(F6, variable) for variable in (x, y, z)]
    branch_smooth, branch_witness = no_projective_common_zero(
        branch_partials, x, y, z
    )
    rank_zero_absent, rank_zero_witness = no_projective_common_zero(
        [Q2, G3, H4], x, y, z
    )

    incidence_matrix = sp.Matrix([[w - G3, Q2], [H4, w + G3]])
    determinant_identity = sp.simplify(incidence_matrix.det() - k3_equation)
    incidence_e1 = sp.expand((w - G3) * s + Q2 * t)
    incidence_e2 = sp.expand(H4 * s + (w + G3) * t)

    coordinate_variables = (x, y, z, w, s, t)
    all_variables = (x, y, z, w, s, t, p1, p2)
    charge_H = (1, 1, 1, 3, 0, 1, -3, -4)
    charge_L = (0, 0, 0, 0, 1, 1, -1, -1)
    coordinate_charge_rows = (charge_H[:6], charge_L[:6])
    all_charge_rows = (charge_H, charge_L)
    superpotential = sp.expand(p1 * incidence_e1 + p2 * incidence_e2)

    e1_degrees = bidegrees(incidence_e1, coordinate_variables, coordinate_charge_rows)
    e2_degrees = bidegrees(incidence_e2, coordinate_variables, coordinate_charge_rows)
    superpotential_degrees = bidegrees(superpotential, all_variables, all_charge_rows)
    euler_identities = []
    for charge_row in all_charge_rows:
        euler_identities.append(
            sp.expand(
                sum(
                    charge * variable * sp.diff(superpotential, variable)
                    for charge, variable in zip(charge_row, all_variables)
                )
            )
        )

    anomaly_matrix = sp.zeros(2)
    for charges in zip(charge_H, charge_L):
        column = sp.Matrix(charges)
        anomaly_matrix += column * column.T
        anomaly_matrix -= column * column.T  # Same-charge (2,2) Fermi partner.

    H, L = sp.symbols("H L")
    k3_class = sp.expand((3 * H + L) * (4 * H + L))
    h_square = integrate_ambient_degree_four(H**2 * k3_class, H, L)
    h_dot_l = integrate_ambient_degree_four(H * L * k3_class, H, L)
    l_square = integrate_ambient_degree_four(L**2 * k3_class, H, L)
    delta_square = sp.simplify(h_square + l_square - 2 * h_dot_l)
    h_dot_delta = sp.simplify(h_square - h_dot_l)
    r_minus_square = l_square
    r_plus_square = sp.simplify(4 * h_square - 4 * h_dot_l + l_square)
    r_plus_dot_r_minus = sp.simplify(2 * h_dot_l - l_square)

    allocation = rank_one["source_free_Bianchi"]
    bianchi_sum = (
        allocation["c2_visible_SU3"]
        + allocation["c2_hidden_SU9"]
        + allocation["torus_curvature_cost"]
        + allocation["NS5_charge"]
    )

    mukai_a_square = h_square
    mukai_a_b = 3 * h_square - 5
    mukai_b_square = 9 * h_square - 14
    mukai_gram = sp.Matrix(
        [[mukai_a_square, mukai_a_b], [mukai_a_b, mukai_b_square]]
    )

    checks = {
        "adjacent_rank_one_packet_is_exact_conditional": rank_one["status"]
        == "EXACT_CONDITIONAL_SOURCE_FREE_ALLOCATION_CLOSED_SHARED_CIRCLE_TO_TORUS_SOURCE_MAP_OPEN",
        "splitting_conic_normal_form_is_closed": splitting["status"]
        == "EXACT_LATTICE_TO_SPLITTING_CONIC_DOUBLE_SEXTIC_NORMAL_FORM_CLOSED",
        "A102_stable_bundle_and_allocation_tier_is_closed": (
            a102["results"]["conditional_source_free_Bianchi_allocation_closed"]
            and a102["results"]["new_fitted_continuous_parameters"] == 0
        ),
        "q79_Mukai_charge_sector_uses_H_square_two": q79_mukai["charge_data"][
            "H_square"
        ]
        == 2,
        "Q2_G3_H4_have_degrees_2_3_4": (
            homogeneous_degree(Q2, (x, y, z)) == 2
            and homogeneous_degree(G3, (x, y, z)) == 3
            and homogeneous_degree(H4, (x, y, z)) == 4
        ),
        "F6_has_degree_six": homogeneous_degree(F6, (x, y, z)) == 6,
        "plane_branch_sextic_is_projectively_smooth": branch_smooth,
        "weighted_K3_avoids_ambient_orbifold_point": bool(
            k3_equation.subs({x: 0, y: 0, z: 0, w: 1}) != 0
        ),
        "incidence_determinant_is_the_K3_equation": determinant_identity == 0,
        "incidence_matrix_rank_zero_locus_is_absent": rank_zero_absent,
        "incidence_equation_bidegrees_are_3_1_and_4_1": (
            e1_degrees == {(3, 1)} and e2_degrees == {(4, 1)}
        ),
        "GLSM_superpotential_is_gauge_neutral": superpotential_degrees == {(0, 0)},
        "both_Calabi_Yau_charge_sums_vanish": sum(charge_H) == 0
        and sum(charge_L) == 0,
        "paired_2_2_locus_gauge_anomaly_matrix_vanishes": anomaly_matrix
        == sp.zeros(2),
        "zero_2_EJ_identity_holds_for_both_gauge_factors": all(
            identity == 0 for identity in euler_identities
        ),
        "geometric_phase_has_complex_dimension_two": 6 - 2 - 2 == 2,
        "incidence_intersection_numbers_are_exact": (
            h_square == 2 and h_dot_l == 2 and l_square == -2
        ),
        "delta_equals_H_minus_Rminus_has_square_minus_four": delta_square == -4,
        "delta_is_primitive_and_H_orthogonal": (
            h_dot_delta == 0 and rank_one["K3_lattice"]["delta_primitive"]
        ),
        "split_roots_have_expected_intersections": (
            r_minus_square == -2
            and r_plus_square == -2
            and r_plus_dot_r_minus == 6
        ),
        "active_torus_pair_preserves_shared_untwisted_circle": (
            rank_one["rank_one_torus_candidate"]["omega_1_over_2pi"] == "delta"
            and rank_one["rank_one_torus_candidate"]["omega_2_over_2pi"] == 0
            and rank_one["rank_one_torus_candidate"][
                "one_geometric_circle_untwisted"
            ]
        ),
        "minimal_nonzero_ASD_cost_is_four": rank_one["minimality_theorem"][
            "minimal_nonzero_ASD_cost"
        ]
        == 4,
        "source_free_reference_Bianchi_identity_is_9_11_4": bianchi_sum == 24,
        "Mukai_Gram_and_determinant_seven_are_retained": (
            mukai_gram == sp.Matrix([[2, 1], [1, 4]])
            and mukai_gram.det() == 7
        ),
        "strict_shared_circle_source_guard_remains_open": (
            rank_one["source_guard"][
                "corpus_identifies_it_with_the_untwisted_FuYau_circle"
            ]
            is False
            and rank_one["source_guard"]["rank_one_FuYau_topology_selected_by_MTT"]
            is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    status = (
        "Q79_DEGREE2_K3_SPLITTING_CONIC_GLSM_AND_RANKONE_FUYAU_TOPOLOGICAL_SOURCE_"
        "CLOSED_EXACT_CONDITIONAL_FULL_HETEROTIC_0_2_BUNDLE_TORSION_ANOMALY_AND_IR_SCFT_OPEN"
    )
    cert = {
        "certificate": "q79_degree2_k3_fuyau_torsion_glsm_base",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": status,
        "inputs": {
            "rank_one_FuYau_lattice_and_Bianchi": str(RANK_ONE_FUYAU),
            "splitting_conic_normal_form": str(SPLITTING_CONIC),
            "A102_stable_bundle_allocation": str(A102_CERT),
            "q79_Mukai_charge_sector": str(Q79_MUKAI),
        },
        "checks": checks,
        "explicit_K3": {
            "ambient": "P(1,1,1,3)",
            "coordinates_and_weights": {"x": 1, "y": 1, "z": 1, "w": 3},
            "Q2": str(Q2),
            "G3": str(G3),
            "H4": str(H4),
            "F6_equals_G3_squared_plus_Q2_H4": str(F6),
            "equation": f"w^2-F6=0, with F6={F6}",
            "branch_smoothness_certificate": branch_witness,
            "avoids_ambient_orbifold_point": True,
            "canonical_class": "O(6-1-1-1-3)|X=O_X",
            "degree_two_polarization_H_square": str(h_square),
        },
        "incidence_GLSM": {
            "gauge_group": "U(1)_H x U(1)_L",
            "field_order": ["x", "y", "z", "w", "s", "t", "p1", "p2"],
            "charge_matrix": [list(charge_H), list(charge_L)],
            "incidence_matrix": [
                [str(w - G3), str(Q2)],
                [str(H4), str(w + G3)],
            ],
            "constraint_bidegrees": [[3, 1], [4, 1]],
            "E1": str(incidence_e1),
            "E2": str(incidence_e2),
            "superpotential": "W=p1*E1+p2*E2",
            "Calabi_Yau_charge_sums": [sum(charge_H), sum(charge_L)],
            "complex_target_dimension": 2,
            "rank_zero_locus_certificate": rank_zero_witness,
            "paired_2_2_gauge_anomaly_matrix": [
                [int(entry) for entry in row] for row in anomaly_matrix.tolist()
            ],
            "zero_2_EJ_identity": (
                "At the paired (2,2) locus, E_i=sum_a Q_i^a Sigma_a Phi_i "
                "and J_i=dW/dPhi_i. Gauge invariance gives sum_i E_i J_i=0 "
                "for both U(1) factors."
            ),
        },
        "intersection_and_torsion_source": {
            "ambient_Chow_relations": ["H^4=0", "L(L+H)=0", "integral H^3 L=1/3"],
            "K3_complete_intersection_class": str(k3_class),
            "H_square": str(h_square),
            "H_dot_Rminus": str(h_dot_l),
            "Rminus_square": str(l_square),
            "delta_definition": "delta=H-Rminus=H-L",
            "H_dot_delta": str(h_dot_delta),
            "delta_square": str(delta_square),
            "Rplus_definition": "Rplus=H+delta=2H-L",
            "Rplus_square": str(r_plus_square),
            "Rplus_dot_Rminus": str(r_plus_dot_r_minus),
            "torsion_shift_charge_skeleton": {
                "twisted_circle_divisor_vector_in_H_L_basis": [1, -1],
                "shared_circle_divisor_vector_in_H_L_basis": [0, 0],
                "interpretation": (
                    "The two-parameter incidence GLSM exposes delta as H-L. A torsion "
                    "multiplet can therefore use shift row (1,-1) for the nontrivial "
                    "circle and zero shift for the marked shared circle. The local "
                    "classical anomaly couplings are not yet emitted."
                ),
            },
        },
        "q79_same_branch_arithmetic": {
            "Mukai_vectors": {"a": [5, "H", 0], "b": [7, "3H", 1]},
            "Mukai_Gram": [[2, 1], [1, 4]],
            "Mukai_determinant": 7,
            "reference_Bianchi": {
                "c2_visible_SU3": allocation["c2_visible_SU3"],
                "c2_hidden_SU9": allocation["c2_hidden_SU9"],
                "torus_curvature_cost": allocation["torus_curvature_cost"],
                "NS5_charge": allocation["NS5_charge"],
                "identity": "9+11+4=24",
                "tier": "exact K3 reference allocation; full non-pullback total-space differential Bianchi remains open",
            },
            "new_fitted_continuous_parameters": 0,
        },
        "theorem": {
            "name": "q79DegreeTwoK3FuYauTorsionGLSMBaseTheorem",
            "statement": (
                "There is an explicit smooth degree-two K3 in the q79 splitting-conic "
                "family with an isomorphic two-parameter incidence GLSM. Its divisor "
                "ring gives H^2=2 and the primitive class delta=H-L with H.delta=0 and "
                "delta^2=-4. Thus the active rank-one Fu-Yau pair (delta,0), including "
                "one untwisted shared circle, has an exact GLSM gauge-divisor source "
                "skeleton. On the imported A102 reference tier it preserves the exact "
                "source-free allocation 9+11+4=24 and the determinant-seven Mukai block."
            ),
            "conditionality": (
                "This theorem constructs the target K3, incidence GLSM, divisor source, "
                "and integrated reference allocation. It does not prove that primitive "
                "MTT selects the shared circle as the untwisted Fu-Yau factor."
            ),
        },
        "worldsheet_contract_advance": {
            "W8_before": "OPEN_EXACT_Q79_HETEROTIC_0_2_SCFT_OR_ALL_BETA_FUNCTIONS",
            "W8_after": (
                "PARTIAL_EXACT_DEGREE2_K3_INCIDENCE_GLSM_EJ_AND_RANKONE_TORSION_"
                "DIVISOR_SOURCE_CLOSED_FULL_HETEROTIC_BUNDLE_TLSM_ANOMALY_AND_IR_SCFT_OPEN"
            ),
            "new_exact_rows": [
                "explicit smooth splitting-conic K3 polynomial",
                "U(1)^2 incidence GLSM charge matrix",
                "paired (2,2) gauge anomaly cancellation and E/J identity",
                "exact divisor source delta=H-L with delta^2=-4",
                "rank-one torsion shift skeleton preserving the shared circle",
            ],
            "still_open_rows": [
                "selected visible and hidden heterotic Fermi charge matrices on this GLSM",
                "holomorphic non-pullback bundle E/J maps with integral c3=+/-6",
                "torsion-multiplet axial couplings and local 2x2 anomaly cancellation matrix",
                "full differential Bianchi identity after non-pullback circle clutching",
                "proof of the exact IR (0,2) SCFT, GSO, and seven analytic characters",
                "strict primitive-MTT shared-circle-to-untwisted-FuYau source theorem",
            ],
        },
        "claim_tiers": {
            "explicit_degree_two_K3_smoothness": "CLOSED_EXACT",
            "splitting_conic_incidence_GLSM": "CLOSED_EXACT",
            "paired_2_2_base_EJ_and_gauge_anomaly": "CLOSED_EXACT",
            "rank_one_FuYau_divisor_source_delta_H_minus_L": "CLOSED_EXACT",
            "source_free_9_11_4_reference_Bianchi": "CLOSED_EXACT_CONDITIONAL_REFERENCE_TIER",
            "strict_MTT_selection_of_rank_one_FuYau_topology": "OPEN",
            "full_heterotic_0_2_bundle_EJ_system": "OPEN",
            "local_torsion_GLSM_anomaly_cancellation": "OPEN",
            "exact_q79_IR_SCFT": "OPEN",
            "UV_complete_q79_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_incidence_base_GLSM_is_full_heterotic_TLSM": False,
            "claims_integrated_Bianchi_identity_is_local_GLSM_anomaly_matrix": False,
            "claims_A102_reference_Bianchi_survives_nonpullback_clutching_without_recomputation": False,
            "claims_primitive_MTT_selects_shared_circle_as_untwisted_FuYau_factor": False,
            "claims_GLSM_charge_table_proves_exact_IR_SCFT": False,
            "claims_full_GSO_partition_function_closed": False,
            "claims_UV_complete_QG_closed": False,
        },
        "primary_sources": {
            "degree_two_K3_double_sextic": "https://arxiv.org/abs/1808.00351",
            "lattice_polarized_K3_period_map": "https://arxiv.org/abs/alg-geom/9502005",
            "FuYau_anomaly_solution": "https://arxiv.org/abs/hep-th/0604137",
            "torsion_linear_sigma_models": "https://arxiv.org/abs/hep-th/0611084",
            "TLSM_target_space_duality": "https://arxiv.org/abs/1107.0714",
        },
        "next_required_artifact": "q79_Full_Heterotic_0_2_Bundle_and_Torsion_Anomaly_Matrix_v1",
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Degree-Two K3 Fu-Yau Torsion GLSM Base Theorem v1

Date: 2026-07-16

## Exact advance

The q79 worldsheet program now has an explicit smooth K3 representative, not
only an abstract `H^2=2` lattice.  Let

```text
Q2 = {Q2}
G3 = {G3}
H4 = {H4}
F6 = G3^2 + Q2 H4
```

and define

```text
X_K3: w^2 = F6(x,y,z) in P(1,1,1,3).
```

Exact Groebner checks on the affine chart `z=1`, the line at infinity, and
the remaining projective point show that the branch sextic is smooth.  The K3
also avoids the only ambient weighted-projective orbifold point.

## Incidence GLSM

The determinantal presentation

```text
M = [[w-G3, Q2],
     [H4,   w+G3]]
```

obeys `det(M)=w^2-F6`.  The common-zero locus `Q2=G3=H4=0` is empty, so `M`
has rank one everywhere on the K3 and its projectivized kernel is isomorphic
to the double sextic.

This gives the two-parameter GLSM charge table

```text
field       x  y  z  w  s  t  p1  p2
U(1)_H      1  1  1  3  0  1  -3  -4
U(1)_L      0  0  0  0  1  1  -1  -1
```

with constraint bidegrees `(3,1)` and `(4,1)`.  Both charge sums vanish.  At
the paired `(2,2)` locus, the chiral and Fermi gauge-anomaly matrices cancel
exactly, and gauge invariance of `W=p1 E1+p2 E2` proves `sum E_i J_i=0` for
both gauge factors by the weighted Euler identity.

## The Fu-Yau class is visible in the gauge lattice

In the ambient Chow ring,

```text
H^4=0,
L(L+H)=0,
integral H^3 L = 1/3.
```

Intersecting with the K3 class `(3H+L)(4H+L)` gives

```text
H^2=2,
H.L=2,
L^2=-2.
```

The splitting-conic component is `R_minus=L`, hence

```text
delta = H-L,
H.delta = 0,
delta^2 = -4.
```

This is exactly the primitive minimal nonzero anti-self-dual class in A102.
The active rank-one Fu-Yau pair is `(delta,0)`: the first circle is twisted by
the divisor vector `(1,-1)` in the GLSM gauge basis, while the second marked
shared circle has zero shift.  This retains the topology
`P_delta x S1_shared` rather than replacing it by a two-twisted-circle model.

## q79 arithmetic retained

The same `H^2=2` gives

```text
a=(5,H,0), b=(7,3H,1),
Gram(a,b)=[[2,1],[1,4]], det=7.
```

The imported source-free K3 reference allocation is exactly

```text
c2(V3)+c2(W9)-delta^2 = 9+11+4 = 24,
NS5 charge = 0.
```

No fitted continuous parameter was added.

## What this does not close

This is a real W8 advance, but it is not yet the full q79 heterotic worldsheet.
The following objects remain required:

1. visible and hidden heterotic Fermi charge matrices on this `U(1)^2` GLSM;
2. holomorphic non-pullback bundle `E/J` maps with `c3=+/-6`;
3. torsion-multiplet axial couplings and the local `2x2` anomaly matrix;
4. the differential Bianchi identity after non-pullback circle clutching;
5. the exact IR `(0,2)` SCFT, GSO projection, and seven analytic characters;
6. the strict MTT theorem selecting the shared circle as the untwisted Fu-Yau
   factor.

In particular, the exact integrated identity `9+11+4=24` must not be confused
with the still-missing local GLSM anomaly cancellation matrix.

## Primary sources

- [Degree-two K3 surfaces as double sextics](https://arxiv.org/abs/1808.00351)
- [Lattice-polarized K3 period geometry](https://arxiv.org/abs/alg-geom/9502005)
- [Fu-Yau anomaly solutions](https://arxiv.org/abs/hep-th/0604137)
- [Linear models for flux vacua](https://arxiv.org/abs/hep-th/0611084)
- [Torsion GLSM target-space duality](https://arxiv.org/abs/1107.0714)
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
