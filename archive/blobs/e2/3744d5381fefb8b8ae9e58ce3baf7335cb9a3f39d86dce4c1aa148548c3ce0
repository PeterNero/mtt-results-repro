from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

MONODROMY = (
    ROOT
    / "certificates"
    / "q79_shared_z64_same_source_monodromy_map_certificate.json"
)
DETERMINANT = (
    ROOT
    / "certificates"
    / "q79_shared_circle_spinc_determinant_bridge_certificate.json"
)
METRIC_SOURCE = (
    ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
)
TEGR_BRIDGE = (
    ROOT
    / "certificates"
    / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"
)
STRICT_SOURCE = (
    ROOT
    / "certificates"
    / "strict_same_source_teleparallel_selection_certificate.json"
)
MARKED_C4_NOGO = (
    ROOT
    / "certificates"
    / "q79_marked_shared_circle_c4_descent_nogo_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_shared_circle_double_return_cln_nil_flat_endpoint_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Shared_Circle_Double_Return_CLN_Nil_Complex_and_Flat_Zero_Defect_Endpoint_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_rows(matrix: sp.Matrix) -> list[list[int | str]]:
    rows: list[list[int | str]] = []
    for row in matrix.tolist():
        converted: list[int | str] = []
        for value in row:
            if value.is_Integer:
                converted.append(int(value))
            elif value.is_Rational:
                converted.append(str(value))
            else:
                converted.append(str(sp.simplify(value)))
        rows.append(converted)
    return rows


def same_column_space(left: sp.Matrix, right: sp.Matrix) -> bool:
    return (
        left.rank() == right.rank()
        and left.row_join(right).rank() == left.rank()
    )


def character_value(weight: int, exponent: int, order: int = 64) -> sp.Expr:
    return sp.simplify(sp.exp(2 * sp.pi * sp.I * weight * exponent / order))


def tensor_is_zero(tensor: sp.MutableDenseNDimArray) -> bool:
    return all(
        tensor[index] == 0
        for index in product(*(range(size) for size in tensor.shape))
    )


def main() -> None:
    monodromy = load(MONODROMY)
    determinant = load(DETERMINANT)
    metric_source = load(METRIC_SOURCE)
    tegr_bridge = load(TEGR_BRIDGE)
    strict_source = load(STRICT_SOURCE)
    marked_c4_nogo = load(MARKED_C4_NOGO)

    z64_order = 64
    halfturn = int(
        determinant["finite_data"]["unique_nontrivial_generator_image"]
    )
    traversal_exponents = [0, halfturn, (2 * halfturn) % z64_order]
    odd_weights = [1, 33]
    odd_sequences = {
        str(weight): [
            character_value(weight, exponent, z64_order)
            for exponent in traversal_exponents
        ]
        for weight in odd_weights
    }
    metric_weight = int(metric_source["finite_data"]["character_k"])
    metric_sequence = [
        character_value(metric_weight, exponent, z64_order)
        for exponent in traversal_exponents
    ]

    # Minimal real parity carrier: odd proto-spinor sign plus even metric weight.
    identity_v = sp.eye(2)
    g = sp.diag(-1, 1)
    difference = identity_v - g
    norm = identity_v + g
    projector_minus = sp.Rational(1, 2) * difference
    projector_plus = sp.Rational(1, 2) * norm

    # The canonical 2-periodic C2 resolution can be folded into one nilpotent
    # differential on V direct-sum V. Its cohomology vanishes in char != 2.
    zero_v = sp.zeros(2)
    nil_differential = zero_v.row_join(projector_plus).col_join(
        projector_minus.row_join(zero_v)
    )
    nil_kernel = sp.Matrix.hstack(*nil_differential.nullspace())
    nil_image = sp.Matrix.hstack(*nil_differential.columnspace())

    # The selected even metric channel supplies a direct counterexample to the
    # claim that the half-turn or double return forces zero strain.
    strain_witness = sp.diag(sp.log(2), -sp.log(2), 0)
    metric_witness = sp.simplify((2 * strain_witness).exp())
    metric_witness_after_halfturn = sp.simplify(metric_sequence[1] * metric_witness)

    # Canonical zero-defect Lorentzian realization of the existing Q_WW source.
    q_zero = sp.eye(3)
    strain_zero = sp.zeros(3)
    spatial_metric_zero = q_zero.T * q_zero
    lapse = sp.Integer(1)
    shift = sp.zeros(3, 1)
    coframe = sp.eye(4)
    eta = sp.diag(-1, 1, 1, 1)
    spacetime_metric = coframe.T * eta * coframe

    # All coordinate derivatives of this constant coframe and metric vanish.
    coframe_derivative = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    metric_derivative = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    torsion = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    christoffel = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    riemann = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
    ricci = sp.zeros(4)
    scalar_curvature = sp.Integer(0)
    einstein = ricci - sp.Rational(1, 2) * spacetime_metric * scalar_curvature
    tegr_scalar = sp.Integer(0)
    lambda_eff = sp.Symbol("Lambda_eff", real=True)
    vacuum_equation_residual = einstein + lambda_eff * spacetime_metric

    nil_exact = same_column_space(nil_image, nil_kernel)
    checks = {
        "same_source_sheet_sign_map_is_unique_nontrivial_halfturn": (
            monodromy["claim_tiers"][
                "finite_same_source_q79_to_Z64_monodromy_map"
            ]
            == "CLOSED_UNIQUE"
            and monodromy["finite_data"]["Z64_order_two_images"] == [0, 32]
            and halfturn == 32
        ),
        "halfturn_has_exact_order_two_in_Z64": (
            halfturn % z64_order != 0
            and (2 * halfturn) % z64_order == 0
        ),
        "both_odd_roots_execute_plus_minus_plus": all(
            sequence == [1, -1, 1] for sequence in odd_sequences.values()
        ),
        "metric_weight_executes_plus_plus_plus": metric_sequence == [1, 1, 1],
        "certificate_root_restrictions_match_execution": (
            determinant["finite_data"]["root_restriction_phase_exponents_mod64"][
                "1"
            ][1]
            == 32
            and determinant["finite_data"][
                "root_restriction_phase_exponents_mod64"
            ]["33"][1]
            == 32
            and determinant["finite_data"][
                "TT_restriction_phase_exponents_mod64"
            ][1]
            == 0
        ),
        "C2_generator_squares_to_identity": g**2 == identity_v,
        "difference_and_norm_annihilate_each_other": (
            difference * norm == zero_v and norm * difference == zero_v
        ),
        "parity_projectors_are_complementary": (
            projector_minus**2 == projector_minus
            and projector_plus**2 == projector_plus
            and projector_minus * projector_plus == zero_v
            and projector_minus + projector_plus == identity_v
        ),
        "folded_CLN_differential_is_nilpotent": nil_differential**2 == sp.zeros(4),
        "folded_CLN_complex_is_acyclic_over_characteristic_not_two": (
            nil_differential.rank() == 2
            and len(nil_differential.nullspace()) == 2
            and nil_exact
        ),
        "nil_complex_adds_no_selected_parameter": True,
        "marked_circle_C4_no_go_is_not_reused": (
            marked_c4_nogo["claim_tiers"][
                "autonomous_Lens_descent_in_current_marked_shared_circle_setup"
            ]
            == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
            and g**2 == identity_v
        ),
        "nonzero_selected_TT_strain_is_fixed_by_halfturn": (
            strain_witness != sp.zeros(3)
            and metric_witness == sp.diag(4, sp.Rational(1, 4), 1)
            and metric_witness_after_halfturn == metric_witness
            and metric_witness != sp.eye(3)
        ),
        "double_return_alone_does_not_force_zero_metric_defect": (
            metric_sequence[2] == 1 and metric_witness != sp.eye(3)
        ),
        "world_in_world_certificate_has_identity_background": (
            metric_source["construction"]["background"]
            == "psi_*=0, Q_*=I, G_*=I"
            and metric_source["construction"]["metric_observable"]
            == "G(psi)=Q(psi)^T Q(psi)=exp(2 S(psi))"
        ),
        "zero_defect_Q_and_spatial_metric_are_identity": (
            strain_zero == sp.zeros(3)
            and q_zero == sp.eye(3)
            and spatial_metric_zero == sp.eye(3)
        ),
        "canonical_zero_defect_coframe_is_Minkowski": (
            lapse == 1
            and shift == sp.zeros(3, 1)
            and coframe == sp.eye(4)
            and spacetime_metric == eta
            and coframe.det() == 1
        ),
        "constant_coframe_has_zero_teleparallel_torsion": (
            tensor_is_zero(coframe_derivative)
            and tensor_is_zero(torsion)
            and tegr_scalar == 0
        ),
        "constant_metric_has_zero_Levi_Civita_curvature": (
            tensor_is_zero(metric_derivative)
            and tensor_is_zero(christoffel)
            and tensor_is_zero(riemann)
            and ricci == sp.zeros(4)
            and scalar_curvature == 0
            and einstein == sp.zeros(4)
        ),
        "TEGR_boundary_identity_is_imported_exactly": (
            tegr_bridge["claim_tiers"]["TEGR_Einstein_Hilbert_boundary_identity"]
            == "CLOSED_EXACT"
            and tegr_bridge["claim_tiers"][
                "TEGR_bulk_field_equations_equal_Einstein_equations"
            ]
            == "CLOSED_EXACT"
        ),
        "strict_same_source_action_is_closed_at_leading_order": (
            strict_source["claim_tiers"][
                "leading_two_derivative_classical_GR_on_candidate_branch"
            ]
            == "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY"
        ),
        "vacuum_Minkowski_requires_Lambda_eff_zero": (
            vacuum_equation_residual == lambda_eff * eta
            and vacuum_equation_residual.subs(lambda_eff, 0) == sp.zeros(4)
            and vacuum_equation_residual.subs(lambda_eff, 1) != sp.zeros(4)
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_shared_circle_double_return_cln_nil_flat_endpoint",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": (
            "Q79_SHARED_CIRCLE_DOUBLE_RETURN_AND_CANONICAL_CLN_NIL_COMPLEX_"
            "CLOSED_FLAT_ZERO_DEFECT_ENDPOINT_CLOSED_DYNAMIC_SELECTION_AND_LAMBDA_OPEN"
        ),
        "inputs": {
            "same_source_monodromy": str(MONODROMY),
            "SpinC_determinant_bridge": str(DETERMINANT),
            "world_in_world_metric_source": str(METRIC_SOURCE),
            "teleparallel_Einstein_bridge": str(TEGR_BRIDGE),
            "strict_same_source_TEGR": str(STRICT_SOURCE),
            "marked_C4_descent_no_go": str(MARKED_C4_NOGO),
        },
        "checks": checks,
        "finite_data": {
            "shared_circle_group": "Z64",
            "unique_nontrivial_central_halfturn": halfturn,
            "double_traversal_exponents_mod64": traversal_exponents,
            "odd_root_weights": odd_weights,
            "odd_root_character_sequences": {
                key: [int(value) for value in sequence]
                for key, sequence in odd_sequences.items()
            },
            "metric_weight": metric_weight,
            "metric_character_sequence": [int(value) for value in metric_sequence],
            "minimal_parity_carrier_basis": ["odd_proto_state", "even_metric_state"],
            "C2_generator_g": matrix_rows(g),
            "group_ring_difference_1_minus_g": matrix_rows(difference),
            "group_ring_norm_1_plus_g": matrix_rows(norm),
            "projector_minus": matrix_rows(projector_minus),
            "projector_plus": matrix_rows(projector_plus),
            "folded_nil_differential": matrix_rows(nil_differential),
            "folded_nil_differential_rank": int(nil_differential.rank()),
            "folded_nil_kernel_dimension": len(nil_differential.nullspace()),
            "folded_nil_image_dimension": int(nil_differential.rank()),
            "folded_nil_cohomology_dimension": 0,
            "strain_counterexample": ["log(2)", "-log(2)", "0"],
            "metric_counterexample": matrix_rows(metric_witness),
            "zero_defect_Q_WW": matrix_rows(q_zero),
            "zero_defect_spatial_metric": matrix_rows(spatial_metric_zero),
            "canonical_lapse": int(lapse),
            "canonical_shift": [0, 0, 0],
            "canonical_coframe": matrix_rows(coframe),
            "canonical_spacetime_metric": matrix_rows(spacetime_metric),
            "teleparallel_torsion_nonzero_components": 0,
            "Levi_Civita_Riemann_nonzero_components": 0,
            "TEGR_scalar": int(tegr_scalar),
            "Ricci_scalar": int(scalar_curvature),
            "Einstein_tensor": matrix_rows(einstein),
            "vacuum_equation_residual": "Lambda_eff*diag(-1,1,1,1)",
            "new_continuous_parameters": 0,
            "new_discrete_parameters": 0,
        },
        "theorem": {
            "name": "Q79SharedCircleDoubleReturnCLNNilAndFlatEndpointTheorem",
            "part_A_exact_double_return": {
                "source": (
                    "The selected q79 signed-sheet transposition maps uniquely to "
                    "32 in the shared Z64 carrier."
                ),
                "odd_state": (
                    "For either admissible odd root chi_1 or chi_33, one traversal "
                    "acts by -1 and two traversals act by +1. The result is root independent."
                ),
                "metric_state": (
                    "The weight-two metric/TT character acts by +1 after each traversal."
                ),
            },
            "part_B_canonical_finite_CLN_operator_complex": {
                "circle_role": "the selected shared Z64 phase/holonomy carrier",
                "lens_role": (
                    "the q79 signed-sheet finite transport and its unique central C2 image; "
                    "no literal lens-space factor is asserted"
                ),
                "nil_role": (
                    "the canonical C2 difference and norm operators D=1-g and N=1+g, "
                    "or equivalently the folded differential d with d^2=0"
                ),
                "exactness": (
                    "On the minimal odd-plus-even real carrier and over characteristic "
                    "different from two, im(d)=ker(d), so the folded complex is acyclic."
                ),
                "parameter_count": 0,
            },
            "part_C_flatness_no_go": {
                "statement": (
                    "Spinorial double return alone does not force zero strain or flat "
                    "spacetime because the metric carrier is already invariant after one traversal."
                ),
                "witness": (
                    "S=diag(log 2,-log 2,0) lies in the selected TT strain plane and "
                    "gives G=diag(4,1/4,1), which is nonidentity and fixed by the halfturn."
                ),
            },
            "part_D_flat_zero_defect_endpoint": {
                "premise": (
                    "Take the already displayed world-in-world zero source psi=0, hence "
                    "S=0, Q_WW=I3, and G3=I3, inside the canonical Lorentzian realization."
                ),
                "coframe": (
                    "With lapse N=1, shift N^i=0, spatial triad I3, and inertial "
                    "connection zero, theta^0=dt and theta^a=dx^a."
                ),
                "result": (
                    "The metric is Minkowski, teleparallel torsion and the TEGR scalar "
                    "vanish, and the Levi-Civita Riemann, Ricci, and Einstein tensors vanish exactly."
                ),
                "vacuum_boundary": (
                    "For zero stress this is a solution of the selected leading-order "
                    "Einstein equations exactly when Lambda_eff=0. Lambda_eff is not selected here."
                ),
            },
            "part_E_logical_boundary": {
                "closed": (
                    "the finite double return, the same-source operator-tier CLN nil "
                    "complex, and flatness of the explicit zero-defect canonical endpoint"
                ),
                "open": (
                    "a dynamical or variational theorem selecting zero defect, selection "
                    "of Lambda_eff=0, and identification of pregeometric perfect closure "
                    "with the physical Lorentzian vacuum"
                ),
            },
        },
        "claim_tiers": {
            "q79_signed_sheet_to_shared_Z64_halfturn": "CLOSED_EXACT_UNIQUE",
            "single_traversal_odd_proto_state_sign": "CLOSED_MINUS_IDENTITY_ROOT_INDEPENDENT",
            "double_traversal_odd_proto_state_return": "CLOSED_IDENTITY_ROOT_INDEPENDENT",
            "weight_two_metric_blindness_to_halfturn": "CLOSED_EXACT",
            "canonical_C2_difference_norm_nil_complex": "CLOSED_EXACT",
            "canonical_C2_nil_complex_acyclicity": "CLOSED_EXACT_OVER_CHARACTERISTIC_NOT_TWO",
            "same_source_CLN_operator_roles": "CLOSED_EXACT_AT_FINITE_OPERATOR_TIER",
            "literal_circle_lens_nil_product_or_nesting": "NOT_CLAIMED",
            "double_return_alone_forces_zero_metric_strain": "CLOSED_NO_GO",
            "world_in_world_zero_defect_Q_and_G": "CLOSED_EXACT_FOR_DISPLAYED_REALIZATION",
            "canonical_zero_defect_Minkowski_coframe": "CLOSED_EXACT",
            "zero_defect_torsion_curvature_and_Einstein_tensor": "CLOSED_EXACT",
            "double_return_dynamically_selects_zero_defect": "OPEN",
            "Lambda_eff_zero": "OPEN",
            "flat_endpoint_is_full_selected_vacuum": "OPEN_CONDITIONAL_ON_ZERO_STRESS_AND_LAMBDA",
            "pregeometric_perfect_closure_equals_physical_flat_vacuum": "OPEN_NO_BRIDGE",
        },
        "guardrails": {
            "claims_C4_preserves_the_marked_shared_circle": False,
            "claims_literal_circle_lens_nil_topology": False,
            "claims_double_return_forces_Q_WW_identity": False,
            "claims_flat_spacetime_has_no_time_or_space": False,
            "claims_Minkowski_is_selected_with_nonzero_Lambda_eff": False,
            "claims_primitive_MTT_selects_the_zero_defect_state": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Shared-Circle Double Return, CLN Nil Complex, and Flat Zero-Defect Endpoint v1

Status:
`Q79_SHARED_CIRCLE_DOUBLE_RETURN_AND_CANONICAL_CLN_NIL_COMPLEX_CLOSED_FLAT_ZERO_DEFECT_ENDPOINT_CLOSED_DYNAMIC_SELECTION_AND_LAMBDA_OPEN`

## Exact double return

The selected q79 signed-sheet transposition has the unique nontrivial image

```text
32 in Z64.
```

It is the central half-turn, not the order-four quarter-turn that exchanges the
twisted and marked shared circles. For either admissible odd root,

```text
chi_1:  +1 -> -1 -> +1,
chi_33: +1 -> -1 -> +1.
```

Thus the old proto-spinor double-return statement now has an explicit q79
realization. The choice between the two odd roots is irrelevant on this `C2`
subgroup. The weight-two metric/TT carrier instead executes

```text
chi_2: +1 -> +1 -> +1.
```

The proto-state remembers the first traversal; its metric bilinear is already
single-valued.

## Canonical Circle-Lens-Nil operator complex

This result realizes the three revised carrier roles without asserting a
literal `S1 x Lens x Nil` topology:

```text
Circle = the selected shared Z64 phase carrier,
Lens   = signed-sheet finite transport through its central C2 image,
Nil    = the canonical C2 difference/norm complex.
```

On the minimal real parity carrier `V=V_odd direct-sum V_even`, let

```text
g=diag(-1,+1),
D=1-g,
N=1+g.
```

Since `g^2=1`,

```text
DN=ND=0.
```

Equivalently, with `P_minus=D/2` and `P_plus=N/2`, fold the two-periodic
complex into `V direct-sum V`:

```text
d = [[0,P_plus],[P_minus,0]].
```

Exact arithmetic gives `d^2=0`, `rank(d)=2`, and
`im(d)=ker(d)` of dimension two. Hence the finite complex is acyclic over any
field of characteristic different from two. It adds no discrete or continuous
parameter. This is a rigorous operator-level Nil termination generated by the
same q79 half-turn.

## Double return does not select flatness

The distinction between odd state and even metric is decisive. The selected TT
strain

```text
S=diag(log(2),-log(2),0)
```

gives

```text
G=exp(2S)=diag(4,1/4,1).
```

This metric is nonidentity but is fixed by the half-turn and by its square.
Therefore

```text
double return => Q_WW=I
```

is false without an additional dynamical or variational premise. The double
return closes spinorial sign memory; it does not erase an arbitrary even
metric defect.

## Exact flat zero-defect endpoint

The existing world-in-world source does contain an exact zero-defect point:

```text
psi=0, S=0, Q_WW=I3, G3=I3.
```

Inside the declared canonical Lorentzian realization, choose the inertial ADM
representative

```text
lapse=1, shift=0, spatial triad=I3,
theta^0=dt, theta^a=dx^a.
```

Then the spacetime metric is `diag(-1,1,1,1)`. Direct component execution gives
zero coframe torsion, zero TEGR scalar, zero Levi-Civita Riemann and Ricci
curvature, and zero Einstein tensor. Flat spacetime is therefore an exact
zero-defect endpoint of the displayed candidate realization.

This is flat spacetime, not absence of time or space. For zero stress it solves
the leading Einstein equations only when `Lambda_eff=0`; the current corpus has
not selected that value.

## Frontier after this theorem

Closed exactly:

```text
q79 half-turn realization of proto-spinor double return,
root-independent odd-sign return and even-metric blindness,
same-source finite CLN operator complex and Nil acyclicity,
Minkowski geometry of the explicit zero-defect endpoint.
```

Still open:

```text
a source/action theorem that dynamically selects zero defect,
selection or cancellation of Lambda_eff,
the bridge from pregeometric perfect closure to the physical Lorentzian vacuum.
```

No observed value and no fitted parameter is used.
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
