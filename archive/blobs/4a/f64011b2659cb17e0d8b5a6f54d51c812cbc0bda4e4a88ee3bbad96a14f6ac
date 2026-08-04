from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESEARCH_DATE = "2026-07-30"
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
QG_ROOT = Path(
    os.environ.get(
        "MTT_QG_ROOT",
        TEXPAPERS / "12 Quantum Gravity",
    )
)

PRIOR_BRIDGE = (
    ROOT / "q79_heterotic_maurer_cartan_hodge_repair_bridge.packet.json"
)
PHYSICAL_SEED = (
    ROOT / "q79_physical_gauge_pair_deformation_seed_contract.packet.json"
)
HULL_STROMINGER_TARGET = (
    ROOT / "q79_coupled_hull_strominger_contraction_target.packet.json"
)
BHT_ELIGIBILITY = (
    QG_ROOT / "q79_bht_twisted_fm_eligibility_and_two_twist_contract.packet.json"
)

OUT_PACKET = (
    ROOT / "q79_augmented_heterotic_total_complex_route_correction.packet.json"
)
OUT_NOTE = ROOT / "Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_record(
    repository: str,
    repository_root: Path,
    path: Path,
    payload: dict,
) -> dict[str, object]:
    record: dict[str, object] = {
        "repository": repository,
        "relative_path": path.relative_to(repository_root).as_posix(),
        "sha256": sha256(path),
    }
    if payload.get("schema"):
        record["schema"] = payload["schema"]
    if payload.get("status"):
        record["status"] = payload["status"]
    return record


def matrix_json(value: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.simplify(entry)) for entry in row] for row in value.tolist()]


def build_note(packet: dict) -> str:
    readiness = packet["corrected_upper_action_readiness"]
    physical_open = [
        name
        for name, row in readiness["physical_instantiation_gates"].items()
        if row["closed"] is False
    ]
    physical_open_text = "\n".join(
        f"- `{name}`" for name in physical_open
    )
    return f"""# q79 Augmented Heterotic Total Complex Route Correction v1

**Date:** {packet["date"]}

**Executable packet:** `q79_augmented_heterotic_total_complex_route_correction.packet.json`

**Builder:** `build_q79_augmented_heterotic_total_complex_route_correction.py`

**Independent verifier:** `verify_q79_augmented_heterotic_total_complex_route_correction.py`

## 1. Decisive correction

The previous result correctly proved that a Maurer-Cartan plus gauge residual
has a Hodge Hessian. Its provisional next target was too small: the finite
heterotic `L_3` differential is not just the rank-102 operator `Dbar_Q`.

The primary heterotic construction uses

```text
Y_n = Omega^(0,n)(Q) + Omega^(0,n+1)(X)
```

and

```text
ell_1(y,b) = (Dbar y - 1/2 partial b, dbar b).
```

Thus `Dbar_Q` is an invariant diagonal subcomplex, but the full upper
differential is an upper-triangular extension by the `b`-form complex.

## 2. Why q79 cannot discard the b sector by the standard shortcut

Condition on the q79 Fu-Yau complex structure making

```text
pi: X_q79 -> K3
```

a holomorphic principal elliptic bundle. Let `Omega_K3` be the nonzero
holomorphic two-form on K3.

Because `pi` is a holomorphic submersion, `d pi` is surjective. Its dual is
injective, so

```text
pi* Omega_K3 != 0.
```

Holomorphic pullback commutes with `dbar`; hence this is a nonzero
holomorphic `(2,0)` form on `X_q79`. Equivalently its conjugate is a nonzero
anti-holomorphic `(0,2)` form. Therefore

```text
h^(2,0)(X_q79) >= 1
```

at this conditional complex-geometric tier.

More concretely, set

```text
b_K3 = pi* conjugate(Omega_K3).
```

The K3 form is `d`-closed and pullback commutes with `d`, so

```text
partial b_K3 = 0,
dbar b_K3 = 0,
ell_1(0,b_K3)=0.
```

Thus the augmented linear operator has a nonzero `b`-sector kernel direction
before quotienting by gauge. Whether it is exact, gauge removable, or a
physical zero mode remains open.

The heterotic `L_3` paper integrates out `b` in its reduced massless theory
under the sufficient premise `h^(2,0)=0`. That premise is unavailable on this
q79 branch. This does not prove that `b` is a new physical particle. It proves
that eliminating the sector requires a different gauge, quotient, mass or
connecting-map theorem.

The executable pointwise witness represents

```text
d pi = [[1,0,0],[0,1,0]]
```

and the K3 holomorphic symplectic form by its antisymmetric `2x2` matrix. Its
pullback has rank two and is nonzero.

## 3. Correct short exact sequence

Write

```text
Q_n = Omega^(0,n)(Q_phys),
B_n = Omega^(0,n+1)(X).
```

The primary differential carries the cohomological degree sign

```text
ell_1(y,b) = (Dbar y + 1/2 (-1)^n partial b, dbar b)
```

on `Y_n`. Thus the linear heterotic total differential has block form

```text
L_n = [[D_n, (1/2)(-1)^n A_n],
       [  0,                C_n]],
```

where

```text
D_n = Dbar_Q,
A_n = partial into the T*X component of Q,
C_n = dbar on the b-form sector.
```

The cochain law `L_(n+1)L_n=0` is equivalent to

```text
D_(n+1)D_n = 0,
C_(n+1)C_n = 0,
D_(n+1)A_n - A_(n+1)C_n = 0.
```

There is therefore a short exact sequence of complexes

```text
0 -> (Q_*,D) -> (Y_*,L) -> (B_*,C) -> 0.
```

The inclusion `i(y)=(y,0)` is a chain map:

```text
L i = i D.
```

The coordinate projection onto `Q` is generally not a chain map:

```text
p_Q L_n - D_n p_Q = (1/2)(-1)^n A_n p_B.
```

Consequently, the rank-102 cohomology is a genuine subcomplex input, but it
cannot be declared the full physical zero-mode space until the connecting map
induced by `A` is evaluated.

## 4. Hodge compression theorem

Equip the two summands with the declared orthogonal Hilbert pairing. At degree
one,

```text
Delta_Y,1 = L_1* L_1 + L_0 L_0*.
```

Compressing to the `Q_1` summand gives

```text
p_Q Delta_Y,1 i_Q
  = D_1*D_1 + D_0D_0* + 1/4 A_0A_0*
  = Delta_Q,1 + 1/4 A_0A_0*.
```

The correction is positive semidefinite. Therefore the rank-102 Hodge
operator equals the compressed full upper-action Hessian only after proving

```text
A_0*|_(declared Q_1 domain) = 0
```

or after a certified reduction that removes the extra term.

This is not a numerical correction inserted by hand. It is forced by the
off-diagonal `partial b` entry in the primary heterotic total differential.

## 5. Exact finite witness

The verifier uses one-dimensional blocks

```text
D0=0, D1=1,
C0=1, C1=0,
A0=2, A1=2.
```

Then

```text
L0 = [[0, 1],[0,1]],
L1 = [[1,-1],[0,0]],
L1 L0 = 0.
```

The `Q` subcomplex has degree-one Hodge operator `1`, while

```text
p_Q Delta_Y,1 i_Q = 2 = 1 + 1/4 A0 A0*.
```

This proves by exact counterexample that the full total-complex Hodge
compression need not equal the bare `Q` Hodge operator, even though `Q` is an
invariant subcomplex.

## 6. Corrected frontier

The structural/conditional contract is now

```text
{readiness["structural_closed"]}/{readiness["structural_total"]}
```

and the physical instantiation contract remains

```text
{readiness["physical_closed"]}/{readiness["physical_total"]}.
```

The remaining physical gates are:

{physical_open_text}

The former direct-equality target

```text
full heterotic L3 differential = rank-102 Dbar_Q
```

is retired. The correct next object is:

```text
q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1
```

It must instantiate the full triangular differential, its pairing, the
connecting map and nonlinear products on one selected physical q79 endpoint.

## 7. Interpretation

This strengthens rather than discards the rank-102 work:

- `Q_phys` remains the correct coupled geometric deformation carrier;
- `Dbar_Q` remains an exact invariant linear block;
- the full closure-repair action must also track the form-sector extension;
- q79's K3/elliptic geometry supplies a concrete reason that this extension
  cannot be silently removed.

The surviving `b` direction is naturally related to the heterotic B-field and
may become a four-dimensional scalar or axionic mode, but that physical
identification is not proved here.

## 8. Primary-source boundary

The total-complex formula, the `L_3` products and the `h^(2,0)=0` reduction
premise come from:

```text
https://arxiv.org/abs/1806.08367
```

The rigorous `Dbar_Q`, formal adjoint and overdetermined ellipticity results
for the linear heterotic deformation complex are in:

```text
https://doi.org/10.1007/s00220-025-05309-2
```

The latter source does not supply the full nonlinear Maurer-Cartan equation.
This packet therefore uses the two results as a compatibility target, not as
an already-proved identity on the selected q79 endpoint.

## 9. Reproduction

```powershell
python .\\build_q79_augmented_heterotic_total_complex_route_correction.py
python .\\verify_q79_augmented_heterotic_total_complex_route_correction.py
```

Expected output:

```text
Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_BUILD_PASS
Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_VERIFY_PASS
```
"""


def main() -> None:
    prior_bridge = load(PRIOR_BRIDGE)
    physical_seed = load(PHYSICAL_SEED)
    hs_target = load(HULL_STROMINGER_TARGET)
    bht = load(BHT_ELIGIBILITY)

    require(
        prior_bridge["schema"]
        == "MTTQ79HeteroticMaurerCartanHodgeRepairBridge.v1",
        "prior bridge schema",
    )
    require(
        prior_bridge["physical_q79_compatibility_contract"]["closed"] == 4,
        "prior compatibility count",
    )
    require(
        prior_bridge["next_required_object"]["name"]
        == "q79HeteroticMaurerCartanToPhysicalDbarCompatibility.v1",
        "prior direct compatibility target",
    )
    require(
        physical_seed["physical_preprojection_deformation_complex"][
            "total_fiber_rank_complex"
        ]
        == 102,
        "rank-102 physical carrier",
    )
    require(
        physical_seed["physical_preprojection_deformation_complex"][
            "elliptic_operator"
        ]
        == "B_Q=Dbar_Q+Dbar_Q^* with B_Q^2=Delta_Q",
        "rank-102 Hodge declaration",
    )
    require(
        hs_target["theorem"]["tier"]
        == "CLOSED_EXACT_ANALYTIC_THEOREM_NOT_YET_EXECUTED_ON_THE_PHYSICAL_PAIR",
        "physical Hull-Strominger boundary",
    )
    require(
        bht["status"]
        == "BHT_NONEQUIVARIANT_TWISTED_FM_ELIGIBILITY_CLOSED_"
        "CONDITIONAL_TWO_TWIST_SEPARATION_CLOSED_EXACT_"
        "EQUIVARIANT_INTERTWINER_OPEN",
        "BHT source status",
    )
    require(
        bht["BHT_eligibility"]["complex_geometric_condition"]
        == (
            "the selected Fu-Yau complex structure makes X a holomorphic "
            "principal elliptic bundle"
        ),
        "holomorphic principal elliptic source",
    )

    # Pointwise pullback witness for a holomorphic submersion C^3 -> C^2.
    d_pi = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    omega_k3 = sp.Matrix([[0, 1], [-1, 0]])
    omega_pullback = d_pi.T * omega_k3 * d_pi

    # Symbolic scalar-block model of the augmented total differential.
    d0, d1, a0, a1, c0, c1 = sp.symbols(
        "d0 d1 a0 a1 c0 c1",
        real=True,
    )
    half = sp.Rational(1, 2)
    l0_symbolic = sp.Matrix([[d0, half * a0], [0, c0]])
    l1_symbolic = sp.Matrix([[d1, -half * a1], [0, c1]])
    composition_symbolic = sp.simplify(l1_symbolic * l0_symbolic)
    delta_y_symbolic = sp.simplify(
        l1_symbolic.T * l1_symbolic
        + l0_symbolic * l0_symbolic.T
    )
    delta_q_symbolic = sp.simplify(d1**2 + d0**2)
    q_compression_symbolic = sp.simplify(delta_y_symbolic[0, 0])
    q_correction_symbolic = sp.simplify(
        q_compression_symbolic - delta_q_symbolic
    )
    inclusion_q = sp.Matrix([[1], [0]])
    projection_q = sp.Matrix([[1, 0]])
    projection_b = sp.Matrix([[0, 1]])

    # Nontrivial exact finite total-complex witness.
    d0_w = sp.Integer(0)
    d1_w = sp.Integer(1)
    a0_w = sp.Integer(2)
    a1_w = sp.Integer(2)
    c0_w = sp.Integer(1)
    c1_w = sp.Integer(0)
    l0_witness = l0_symbolic.subs(
        {
            d0: d0_w,
            d1: d1_w,
            a0: a0_w,
            a1: a1_w,
            c0: c0_w,
            c1: c1_w,
        }
    )
    l1_witness = l1_symbolic.subs(
        {
            d0: d0_w,
            d1: d1_w,
            a0: a0_w,
            a1: a1_w,
            c0: c0_w,
            c1: c1_w,
        }
    )
    delta_y_witness = (
        l1_witness.T * l1_witness
        + l0_witness * l0_witness.T
    )
    delta_q_witness = d1_w**2 + d0_w**2
    q_compression_witness = (
        projection_q * delta_y_witness * inclusion_q
    )[0]
    correction_witness = sp.Rational(1, 4) * a0_w**2

    structural_gates = {
        "conditional_q79_holomorphic_principal_elliptic_fibration": {
            "closed": True,
            "tier": "CONDITIONAL_SOURCE_IMPORTED",
            "evidence": (
                "The BHT packet records the selected Fu-Yau complex "
                "structure as a holomorphic principal elliptic bundle "
                "condition."
            ),
        },
        "K3_holomorphic_two_form_survives_pullback": {
            "closed": True,
            "tier": "CLOSED_EXACT_CONDITIONAL_ON_FIBRATION",
            "evidence": (
                "A holomorphic submersion has injective pullback on "
                "pointwise holomorphic forms; the exact finite witness has "
                "rank-two nonzero pullback."
            ),
        },
        "h20_zero_b_elimination_premise_is_unavailable": {
            "closed": True,
            "tier": "CLOSED_EXACT_ROUTE_NOGO",
            "evidence": (
                "The pulled-back K3 form proves h^(2,0)(X)>=1, so the "
                "h^(2,0)=0 sufficient reduction premise cannot hold."
            ),
        },
        "pulledback_K3_b_direction_is_in_kernel_of_ell1": {
            "closed": True,
            "tier": "CLOSED_EXACT_CONDITIONAL_LINEAR_KERNEL",
            "evidence": (
                "For b_K3=pi*conjugate(Omega_K3), d b_K3=0, hence "
                "partial b_K3=dbar b_K3=0 and ell_1(0,b_K3)=0. "
                "Gauge exactness is not asserted."
            ),
        },
        "augmented_Yn_degree_spaces_are_the_correct_L3_target": {
            "closed": True,
            "tier": "CLOSED_EXACT_PRIMARY_FORMULA",
            "evidence": (
                "Y_n=Omega^(0,n)(Q)+Omega^(0,n+1)(X) is the primary "
                "heterotic L3 total complex."
            ),
        },
        "rank102_Qphys_is_an_invariant_diagonal_subcomplex": {
            "closed": True,
            "tier": "CLOSED_EXACT_STRUCTURAL_INTERFACE",
            "evidence": (
                "For i_Q(y)=(y,0), ell_1 i_Q=i_Q Dbar_Q; the lower-left "
                "block vanishes."
            ),
        },
        "augmented_total_complex_short_exact_sequence": {
            "closed": True,
            "tier": "CLOSED_EXACT_UNIVERSAL_BLOCK_THEOREM",
            "evidence": (
                "The triangular differential gives 0->Q->Y->B->0, with "
                "the graded mixed cochain identity D A-A C=0."
            ),
        },
        "full_Hodge_Q_compression_has_positive_cross_correction": {
            "closed": True,
            "tier": "CLOSED_EXACT_UNIVERSAL_BLOCK_THEOREM",
            "evidence": (
                "p_Q Delta_Y i_Q=Delta_Q+(1/4)A_0 A_0*, verified "
                "symbolically and by a nontrivial finite witness."
            ),
        },
    }
    physical_gates = {
        "selected_physical_visible_hidden_zero_defect_endpoint": {
            "closed": False,
            "evidence": "B.HS.01 remains open.",
        },
        "physical_A_and_C_maps_domains_and_boundary_conditions": {
            "closed": False,
            "evidence": (
                "No packet instantiates partial, dbar and their domains on "
                "the selected visible-hidden endpoint."
            ),
        },
        "selected_total_complex_Hilbert_or_cyclic_pairing": {
            "closed": False,
            "evidence": (
                "The physical Gauduchon/HYM metric and full Y-sector pairing "
                "remain absent."
            ),
        },
        "q79_b_mode_gauge_quotient_and_connecting_map": {
            "closed": False,
            "evidence": (
                "The pulled-back form defeats the zero-Hodge shortcut, but "
                "its exact gauge quotient and connecting homomorphism have "
                "not been evaluated."
            ),
        },
        "selected_q79_nonlinear_l2_l3_and_D_term_completion": {
            "closed": False,
            "evidence": (
                "No same-source nonlinear products reproduce all physical "
                "F-term, anomaly, HYM and balanced rows."
            ),
        },
        "upper_cohomology_products_and_finite_operator_projection": {
            "closed": False,
            "evidence": (
                "The augmented upper cohomology has not yet reproduced the "
                "accepted particle sectors, transferred products and finite "
                "operators."
            ),
        },
    }

    checks = {
        "d_pi_is_surjective": d_pi.rank() == 2,
        "K3_two_form_is_nonzero": omega_k3 != sp.zeros(2),
        "K3_two_form_is_skew": omega_k3.T == -omega_k3,
        "pullback_two_form_is_nonzero": omega_pullback != sp.zeros(3),
        "pullback_two_form_has_rank_two": omega_pullback.rank() == 2,
        "Q_inclusion_is_invariant_at_degree_zero": (
            l0_symbolic * inclusion_q == inclusion_q * d0
        ),
        "Q_inclusion_is_invariant_at_degree_one": (
            l1_symbolic * inclusion_q == inclusion_q * d1
        ),
        "B_quotient_is_a_chain_map_at_degree_zero": (
            projection_b * l0_symbolic == c0 * projection_b
        ),
        "B_quotient_is_a_chain_map_at_degree_one": (
            projection_b * l1_symbolic == c1 * projection_b
        ),
        "Q_coordinate_projection_has_A_chain_defect": (
            projection_q * l0_symbolic - d0 * projection_q
            == half * a0 * projection_b
        ),
        "symbolic_cochain_composition_has_declared_blocks": (
            composition_symbolic
            == sp.Matrix(
                [
                    [
                        d1 * d0,
                        half * (d1 * a0 - a1 * c0),
                    ],
                    [0, c1 * c0],
                ]
            )
        ),
        "symbolic_Q_Hodge_compression_formula": (
            q_compression_symbolic
            == delta_q_symbolic + sp.Rational(1, 4) * a0**2
        ),
        "symbolic_cross_correction_is_A0_square": (
            q_correction_symbolic == sp.Rational(1, 4) * a0**2
        ),
        "finite_witness_total_differential_squares_to_zero": (
            l1_witness * l0_witness == sp.zeros(2)
        ),
        "finite_witness_Q_subcomplex_is_invariant": (
            l0_witness * inclusion_q == inclusion_q * d0_w
            and l1_witness * inclusion_q == inclusion_q * d1_w
        ),
        "finite_witness_Q_projection_is_not_chain_map": (
            projection_q * l0_witness
            != d0_w * projection_q
        ),
        "finite_witness_b_quotient_is_chain_map": (
            projection_b * l0_witness == c0_w * projection_b
            and projection_b * l1_witness == c1_w * projection_b
        ),
        "finite_witness_Q_Hodge_is_one": delta_q_witness == 1,
        "finite_witness_full_Q_compression_is_two": (
            q_compression_witness == 2
        ),
        "finite_witness_positive_correction_is_one": correction_witness == 1,
        "finite_witness_compression_formula": (
            q_compression_witness
            == delta_q_witness + correction_witness
        ),
        "all_structural_gates_closed": all(
            row["closed"] for row in structural_gates.values()
        ),
        "all_physical_instantiation_gates_open": not any(
            row["closed"] for row in physical_gates.values()
        ),
        "physical_source_rows_still_zero": not any(
            physical_seed["current_execution"]["minimal_source_rows"].values()
        ),
        "physical_HS_execution_rows_still_zero": not any(
            hs_target["physical_execution_rows"].values()
        ),
    }
    require(
        all(checks.values()),
        f"failed checks: {[key for key, value in checks.items() if not value]}",
    )

    packet = {
        "schema": "MTTQ79AugmentedHeteroticTotalComplexRouteCorrection.v1",
        "date": RESEARCH_DATE,
        "status": (
            "Q79_HOLOMORPHIC_TWO_FORM_SURVIVAL_AND_H20_ZERO_"
            "ELIMINATION_ROUTE_NOGO_CLOSED_CONDITIONAL_"
            "AUGMENTED_HETEROTIC_TOTAL_COMPLEX_AND_HODGE_"
            "COMPRESSION_CORRECTION_CLOSED_EXACT_"
            "PHYSICAL_INSTANTIATION_0_OF_6_OPEN"
        ),
        "inputs": {
            "prior_Maurer_Cartan_Hodge_bridge": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                PRIOR_BRIDGE,
                prior_bridge,
            ),
            "physical_rank102_deformation_seed": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                PHYSICAL_SEED,
                physical_seed,
            ),
            "gauge_fixed_Hull_Strominger_target": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                HULL_STROMINGER_TARGET,
                hs_target,
            ),
            "q79_BHT_holomorphic_elliptic_eligibility": source_record(
                "12 Quantum Gravity",
                QG_ROOT,
                BHT_ELIGIBILITY,
                bht,
            ),
        },
        "holomorphic_two_form_survival_theorem": {
            "name": "HolomorphicSubmersionPullbackInjectivityTheorem",
            "hypotheses": [
                "pi:X->S is a holomorphic surjective submersion",
                "Omega_S is a nonzero holomorphic p-form on S",
            ],
            "statement": (
                "pi*Omega_S is a nonzero holomorphic p-form on X. At a point "
                "where Omega_S is nonzero, surjectivity of d pi permits "
                "tangent lifts of every argument, proving nonvanishing. "
                "Holomorphicity follows because pullback commutes with dbar."
            ),
            "q79_specialization": {
                "conditional_fibration": (
                    "pi:X_q79=P_delta x S1_shared -> K3 is the selected "
                    "holomorphic principal elliptic bundle"
                ),
                "base_form": "Omega_K3 in H^0(K3,Omega_K3^2), nonzero",
                "conclusion": (
                    "pi*Omega_K3 is nonzero and h^(2,0)(X_q79)>=1"
                ),
                "massless_reduction_consequence": (
                    "the h^(2,0)=0 sufficient premise used to integrate out "
                    "the heterotic b sector is unavailable"
                ),
                "explicit_linear_kernel_direction": (
                    "b_K3=pi*conjugate(Omega_K3) is nonzero and d-closed, "
                    "so partial b_K3=dbar b_K3=0 and ell_1(0,b_K3)=0"
                ),
                "boundary": (
                    "this does not alone decide whether the b direction is "
                    "gauge-trivial, obstructed, massive by another mechanism "
                    "or a physical four-dimensional mode"
                ),
            },
            "finite_pointwise_witness": {
                "d_pi": matrix_json(d_pi),
                "Omega_K3": matrix_json(omega_k3),
                "pullback_Omega": matrix_json(omega_pullback),
                "d_pi_rank": d_pi.rank(),
                "pullback_rank": omega_pullback.rank(),
            },
            "tier": (
                "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_Q79_"
                "HOLOMORPHIC_ELLIPTIC_STRUCTURE"
            ),
        },
        "primary_heterotic_total_complex": {
            "degree_spaces": (
                "Y_n=Omega^(0,n)(Q_phys) direct_sum Omega^(0,n+1)(X)"
            ),
            "differential": (
                "ell_1(y,b)=(Dbar_Q y-(1/2) partial b, dbar b)"
            ),
            "block_form": (
                "L_n=[[D_n,(1/2)(-1)^n A_n],[0,C_n]], "
                "A_n=partial into T*X subset Q, C_n=dbar"
            ),
            "graded_sign": (
                "the off-diagonal sign is + at degree zero and - at "
                "degree one"
            ),
            "cochain_conditions": [
                "D_(n+1) D_n=0",
                "C_(n+1) C_n=0",
                "D_(n+1) A_n-A_(n+1) C_n=0",
            ],
            "short_exact_sequence": (
                "0 -> (Omega^(0,*)(Q_phys),Dbar_Q) -> "
                "(Y_*,ell_1) -> (Omega^(0,*+1)(X),dbar) -> 0"
            ),
            "rank102_role": (
                "an invariant diagonal subcomplex and principal geometric "
                "block, not the full heterotic L3 degree space"
            ),
            "connecting_map": (
                "the long-exact-sequence connecting homomorphism is induced "
                "by the off-diagonal -(1/2)partial map"
            ),
            "tier": "CLOSED_EXACT_STRUCTURAL_ROUTE_CORRECTION",
        },
        "symbolic_block_certificate": {
            "symbols": ["d0", "d1", "a0", "a1", "c0", "c1"],
            "L0": matrix_json(l0_symbolic),
            "L1": matrix_json(l1_symbolic),
            "L1_L0": matrix_json(composition_symbolic),
            "Delta_Y_degree1": matrix_json(delta_y_symbolic),
            "Delta_Q_degree1": str(delta_q_symbolic),
            "Q_compression": str(q_compression_symbolic),
            "Q_correction": str(q_correction_symbolic),
            "Q_inclusion": matrix_json(inclusion_q),
            "Q_projection": matrix_json(projection_q),
            "B_projection": matrix_json(projection_b),
        },
        "Hodge_compression_theorem": {
            "name": "AugmentedTotalComplexQCompressionTheorem",
            "statement": (
                "For the orthogonal block pairing and "
                "L_n=[[D_n,(1/2)(-1)^n A_n],[0,C_n]], the Q_1 "
                "compression of "
                "Delta_Y,1=L_1*L_1+L_0L_0* is "
                "Delta_Q,1+(1/4)A_0A_0*."
            ),
            "correction": "(1/4)A_0 A_0*",
            "positivity": (
                "<v,(1/4)A_0A_0* v>=(1/4)||A_0* v||^2>=0"
            ),
            "equality_condition": (
                "the compressed full Hessian equals Delta_Q on a declared "
                "Q_1 domain iff A_0* vanishes there"
            ),
            "physical_consequence": (
                "the rank-102 Hessian cannot be promoted as the entire upper "
                "repair Hessian before the b-sector coupling and reduction "
                "are evaluated"
            ),
            "tier": "CLOSED_EXACT_UNIVERSAL_BLOCK_HODGE_THEOREM",
        },
        "finite_nontrivial_total_complex_witness": {
            "block_values": {
                "D0": str(d0_w),
                "D1": str(d1_w),
                "A0": str(a0_w),
                "A1": str(a1_w),
                "C0": str(c0_w),
                "C1": str(c1_w),
            },
            "L0": matrix_json(l0_witness),
            "L1": matrix_json(l1_witness),
            "L1_L0": matrix_json(l1_witness * l0_witness),
            "Delta_Y_degree1": matrix_json(delta_y_witness),
            "Delta_Q_degree1": str(delta_q_witness),
            "Q_compression": str(q_compression_witness),
            "positive_correction": str(correction_witness),
            "conclusion": (
                "Q is an invariant subcomplex, but the full Hodge compression "
                "is 2 while the bare Q Hodge value is 1."
            ),
        },
        "superseded_direct_target": {
            "prior_name": (
                "q79HeteroticMaurerCartanToPhysicalDbarCompatibility.v1"
            ),
            "retired_claim": (
                "the full heterotic L3 degree spaces and differential can be "
                "identified directly with Q_phys and Dbar_Q alone"
            ),
            "reason": (
                "the primary L3 has an additional b-form summand and "
                "off-diagonal partial coupling; q79 does not satisfy the "
                "h^(2,0)=0 sufficient elimination premise"
            ),
            "preserved_subclaim": (
                "Dbar_Q is the invariant diagonal Q_phys subcomplex"
            ),
            "replacement": (
                "q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1"
            ),
        },
        "corrected_upper_action_readiness": {
            "structural_closed": sum(
                row["closed"] for row in structural_gates.values()
            ),
            "structural_total": len(structural_gates),
            "structural_gates": structural_gates,
            "physical_closed": sum(
                row["closed"] for row in physical_gates.values()
            ),
            "physical_total": len(physical_gates),
            "physical_instantiation_gates": physical_gates,
            "interpretation": (
                "The correct upper-object type is selected at structural and "
                "conditional geometric tier. No physical q79 coefficient, "
                "domain, zero-mode or nonlinear action has been emitted."
            ),
        },
        "external_primary_basis": [
            {
                "work": (
                    "Ashmore et al., Finite deformations from a heterotic "
                    "superpotential: holomorphic Chern-Simons and an "
                    "L_infinity algebra"
                ),
                "url": "https://arxiv.org/abs/1806.08367",
                "used_rows": [
                    (
                        "Y_n=Omega^(0,n)(Q) direct_sum "
                        "Omega^(0,n+1)(X)"
                    ),
                    (
                        "ell_1(y,b)=(Dbar y-(1/2)partial b,dbar b)"
                    ),
                    (
                        "h^(2,0)=0 is the sufficient premise used for the "
                        "displayed massless b-sector reduction"
                    ),
                ],
            },
            {
                "work": (
                    "de Lazari et al., Local Descriptions of the Heterotic "
                    "SU(3) Moduli Space"
                ),
                "url": "https://doi.org/10.1007/s00220-025-05309-2",
                "used_rows": [
                    "the first-order Dbar_Q deformation complex",
                    "the formal adjoint and overdetermined ellipticity",
                    "the explicit statement that the full MC equation is open",
                ],
            },
        ],
        "frontier_delta": {
            "newly_closed": [
                (
                    "conditional q79 survival of the pulled-back K3 "
                    "holomorphic two-form and h20>=1"
                ),
                (
                    "exact no-go for using the h20=0 b-elimination shortcut "
                    "on the selected q79 holomorphic elliptic branch"
                ),
                (
                    "a nonzero pulled-back K3 b-sector direction in the "
                    "kernel of the augmented linear differential before "
                    "gauge quotient"
                ),
                (
                    "the augmented heterotic total complex as the correct "
                    "upper-action target"
                ),
                (
                    "rank-102 Dbar_Q as an invariant diagonal subcomplex "
                    "rather than the whole upper differential"
                ),
                (
                    "the exact positive Hodge-compression correction "
                    "(1/4)A0 A0*"
                ),
            ],
            "route_retired": (
                "direct equality of the full L3 differential with Dbar_Q"
            ),
            "replacement_frontier": (
                "instantiate the augmented total complex and connecting map "
                "on one selected physical q79 endpoint"
            ),
            "not_reopened": [
                "the prior universal Maurer-Cartan Hodge theorem",
                "the rank-102 physical deformation carrier",
                "the gauge-fixed Hull-Strominger contraction theorem",
                "the accepted finite particle/gauge representation tiers",
            ],
        },
        "blocker_assessment": {
            "B.ACTION.01": (
                "advanced and route-corrected: the correct upper differential "
                "type is now the augmented heterotic total complex, not "
                "Dbar_Q alone"
            ),
            "B.HS.01": (
                "unchanged: physical visible-hidden endpoint and common HYM "
                "chamber remain required"
            ),
            "B.GEO.01": (
                "sharpened: the commuting map must preserve the augmented "
                "b-form extension and its Hodge correction as well as Q_phys"
            ),
        },
        "next_required_object": {
            "name": (
                "q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1"
            ),
            "required_rows": [
                "one selected physical q79 Hull-Strominger endpoint",
                "the full Dbar_Q, partial and dbar coefficient operators",
                "one common domain and total-complex Hilbert/cyclic pairing",
                (
                    "the connecting homomorphism and gauge quotient of the "
                    "pulled-back K3 two-form direction"
                ),
                "selected nonlinear l2 and l3 products",
                (
                    "a commuting projection to accepted zero modes, "
                    "transferred products and finite operators"
                ),
            ],
        },
        "checks": checks,
        "guardrails": {
            "claims_q79_physical_HS_endpoint_exists": False,
            "claims_b_is_a_new_physical_particle": False,
            "claims_b_cannot_be_removed_by_any_other_mechanism": False,
            "claims_rank102_Dbar_Q_is_wrong": False,
            "claims_full_upper_Hodge_equals_bare_Delta_Q": False,
            "claims_2018_and_2025_operators_are_already_same_source": False,
            "claims_full_physical_action_or_quantization": False,
            "uses_observed_physics_values": False,
            "adds_continuous_fit_parameters": False,
        },
        "new_continuous_fit_parameters": 0,
    }

    OUT_PACKET.write_text(
        json.dumps(packet, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    OUT_NOTE.write_text(build_note(packet), encoding="utf-8")
    print("Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_BUILD_PASS")


if __name__ == "__main__":
    main()
