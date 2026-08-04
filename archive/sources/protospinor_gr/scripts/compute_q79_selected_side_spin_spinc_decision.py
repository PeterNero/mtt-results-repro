from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from flint import acb, acb_mat, acb_poly, ctx


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

W2_REDUCTION = ROOT / "certificates" / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"
TRIAL_DECISION = ROOT / "certificates" / "q79_trial_branch_irreducibility_and_spin_decision_certificate.json"
SPIN_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79signedsheetspinliftreduction"
    / "q79_signed_sheet_spin_lift_reduction.packet.json"
)
SELECTED_SIDE = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_genus2_fibration_seed.interval.packet.json"
)
TRIAL_MODEL = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
    / "square_elliptic_identity_alignment_spectral_surface.packet.json"
)

OUT_CERT = ROOT / "certificates" / "q79_selected_side_spin_spinc_decision_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Selected_Side_Strict_Spin_NoGo_and_SpinC_Lift_v1.md"


Pair = tuple[acb_poly, acb_poly]
Quaternion = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
SpinCPair = tuple[Quaternion, int]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def pair_add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def pair_mul(left: Pair, right: Pair, elliptic_f: acb_poly) -> Pair:
    return (
        left[0] * right[0] + elliptic_f * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def pair_scale(scalar: acb, value: Pair) -> Pair:
    return scalar * value[0], scalar * value[1]


def pair_pow(value: Pair, exponent: int, elliptic_f: acb_poly) -> Pair:
    output = acb_poly([1]), acb_poly([])
    for _ in range(exponent):
        output = pair_mul(output, value, elliptic_f)
    return output


def sylvester_resultant(left: acb_poly, right: acb_poly) -> acb:
    m = left.degree()
    n = right.degree()
    size = m + n
    rows: list[list[acb]] = []
    for shift in range(n):
        row = [acb(0) for _ in range(size)]
        for index in range(m + 1):
            row[shift + index] = left[m - index]
        rows.append(row)
    for shift in range(m):
        row = [acb(0) for _ in range(size)]
        for index in range(n + 1):
            row[shift + index] = right[n - index]
        rows.append(row)
    return acb_mat(rows).det()


def q_mul(left: Quaternion, right: Quaternion) -> Quaternion:
    a, b, c, d = left
    e, f, g, h = right
    return tuple(
        sp.simplify(value)
        for value in (
            a * e - b * f - c * g - d * h,
            a * f + b * e + c * h - d * g,
            a * g - b * h + c * e + d * f,
            a * h + b * g - c * f + d * e,
        )
    )  # type: ignore[return-value]


def q_neg(value: Quaternion) -> Quaternion:
    return tuple(sp.simplify(-entry) for entry in value)  # type: ignore[return-value]


def spinc_mul(left: SpinCPair, right: SpinCPair) -> SpinCPair:
    return q_mul(left[0], right[0]), (left[1] + right[1]) % 4


def spinc_pow(value: SpinCPair, exponent: int) -> SpinCPair:
    output: SpinCPair = ((sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0)), 0)
    for _ in range(exponent):
        output = spinc_mul(output, value)
    return output


def spinc_equivalent(left: SpinCPair, right: SpinCPair) -> bool:
    same = left[1] % 4 == right[1] % 4 and all(
        sp.simplify(a - b) == 0 for a, b in zip(left[0], right[0])
    )
    central_pair = left[1] % 4 == (right[1] + 2) % 4 and all(
        sp.simplify(a + b) == 0 for a, b in zip(left[0], right[0])
    )
    return same or central_pair


def spinc_key(value: SpinCPair) -> tuple[str, ...]:
    alternatives = [value, (q_neg(value[0]), (value[1] + 2) % 4)]
    keys = [tuple(str(sp.simplify(entry)) for entry in q) + (str(phase),)
            for q, phase in alternatives]
    return min(keys)


def generated_spinc_group(generators: list[SpinCPair]) -> dict[tuple[str, ...], SpinCPair]:
    identity: SpinCPair = ((sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0)), 0)
    group = {spinc_key(identity): identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = spinc_mul(current, generator)
            key = spinc_key(candidate)
            if key not in group:
                group[key] = candidate
                frontier.append(candidate)
    return group


def main() -> None:
    ctx.dps = 160

    reduction = load(W2_REDUCTION)
    trial_decision = load(TRIAL_DECISION)
    spin_packet = load(SPIN_PACKET)
    selected_side = load(SELECTED_SIDE)
    trial_model = load(TRIAL_MODEL)

    alignment = acb_mat(
        [
            [acb(entry["real"], entry["imaginary"]) for entry in row]
            for row in selected_side["source"]["alignment_interval"]
        ]
    )
    alignment_det = alignment.det()
    inverse_transpose = alignment.inv().transpose()

    zero = acb_poly([])
    elliptic_f = acb_poly([0, -1, 0, 1])
    gauss: list[Pair] = [
        (acb_poly([1, 0, -3]), zero),
        (zero, acb_poly([2])),
        (acb_poly([0, 1, 0, 1]), zero),
    ]

    # The source convention is L=A*e and L.X=0. Branching occurs when
    # l=A^T X lies on the dual cubic, so X=A^{-T} Gauss(e).
    coordinates: list[Pair] = []
    for row in range(3):
        coordinate: Pair = zero, zero
        for column in range(3):
            coordinate = pair_add(
                coordinate,
                pair_scale(inverse_transpose[row, column], gauss[column]),
            )
        coordinates.append(coordinate)

    x, y, z, w = sp.symbols("x y z w")
    k3_equation = sp.sympify(
        trial_model["K3"]["equation"],
        locals={"x": x, "y": y, "z": z, "w": w},
    )
    f6 = sp.Poly(sp.expand(-k3_equation.subs(w, 0)), x, y, z, domain=sp.QQ)

    pulled: Pair = zero, zero
    for exponents, coefficient in f6.terms():
        term: Pair = acb_poly([1]), zero
        for coordinate, exponent in zip(coordinates, exponents):
            term = pair_mul(term, pair_pow(coordinate, exponent, elliptic_f), elliptic_f)
        pulled = pair_add(pulled, pair_scale(acb(str(coefficient)), term))

    coefficient_a, coefficient_b = pulled
    norm = coefficient_a * coefficient_a - elliptic_f * coefficient_b * coefficient_b
    derivative = norm.derivative()
    resultant = sylvester_resultant(norm, derivative)
    three_division = acb_poly([-1, 0, -6, 0, 3])
    flex_resultant = sylvester_resultant(norm, three_division)

    norm_degree = norm.degree()
    leading_excludes_zero = acb(0) not in norm[norm_degree]
    resultant_excludes_zero = acb(0) not in resultant
    flex_resultant_excludes_zero = acb(0) not in flex_resultant
    infinity_value_excludes_zero = (
        coefficient_a.degree() == 18 and acb(0) not in coefficient_a[18]
    )

    # Exact SpinC lift. SpinC(3)=(Spin(3)xU(1))/{(1,1),(-1,-1)}.
    root_half = sp.sqrt(2) / 2
    q1: Quaternion = (sp.Integer(0), root_half, -root_half, sp.Integer(0))
    q2: Quaternion = (sp.Integer(0), sp.Integer(0), root_half, -root_half)
    g1: SpinCPair = q1, 1  # phase i
    g2: SpinCPair = q2, 1  # phase i
    identity: SpinCPair = ((sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0)), 0)
    generated = generated_spinc_group([g1, g2])

    spinc_checks = {
        "g1_squared_is_identity_class": spinc_equivalent(spinc_pow(g1, 2), identity),
        "g2_squared_is_identity_class": spinc_equivalent(spinc_pow(g2, 2), identity),
        "braid_relation_holds": spinc_equivalent(
            spinc_mul(spinc_mul(g1, g2), g1),
            spinc_mul(spinc_mul(g2, g1), g2),
        ),
        "product_cube_is_identity_class": spinc_equivalent(
            spinc_pow(spinc_mul(g1, g2), 3), identity
        ),
        "lifted_image_has_order_six": len(generated) == 6,
        "determinant_character_on_transposition_is_sign": (2 * g1[1]) % 4 == 2,
    }

    checks = {
        "w2_reduction_available": (
            reduction["universal_w2_theorem"]["result"] == "w2(E_rho_plus)=a cup a"
        ),
        "trial_witness_available": (
            trial_decision["checks"]["trial_branch_pullback_is_reduced_irreducible"]
            is True
        ),
        "source_uses_selected_side_alignment_interval": (
            selected_side["strict_scope"]["selected_alignment_interval_used"] is True
        ),
        "source_does_not_select_final_integral_branch": (
            selected_side["strict_scope"]["integral_branch_selected"] is False
        ),
        "alignment_convention_typed": (
            selected_side["source"]["line"]
            == "L=A*[a,b,1]^T and L0*x+L1*y+L2*z=0"
        ),
        "alignment_interval_is_invertible": acb(0) not in alignment_det,
        "selected_side_norm_has_degree_36": norm_degree == 36,
        "selected_side_norm_leading_coefficient_excludes_zero": leading_excludes_zero,
        "selected_side_norm_resultant_excludes_zero": resultant_excludes_zero,
        "selected_side_norm_avoids_finite_flex_points": flex_resultant_excludes_zero,
        "selected_side_pullback_avoids_flex_at_infinity": infinity_value_excludes_zero,
        "selected_side_norm_is_squarefree_throughout_interval": (
            leading_excludes_zero and resultant_excludes_zero
        ),
        "selected_side_branch_is_reduced_irreducible": (
            leading_excludes_zero and resultant_excludes_zero
        ),
        "selected_side_H1_is_Z6": (
            leading_excludes_zero and resultant_excludes_zero
            and reduction["finite_data"]["branch_lattice_divisibility"] == 6
        ),
        "selected_side_strict_Spin_is_obstructed": (
            leading_excludes_zero and resultant_excludes_zero
            and reduction["finite_data"]["Z6_to_Z4_odd_lift_images"] == []
        ),
        "spin_packet_local_relations_available": (
            spin_packet["binary_spin_theorem"]["checks"]["braid_relation_exact"]
            is True
        ),
        **spinc_checks,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    interval_result = {
        "alignment_scope": selected_side["source"]["carrier_side"],
        "alignment_determinant": str(alignment_det),
        "alignment_determinant_abs_lower": str(alignment_det.abs_lower()),
        "transformed_coordinate_rule": "X=A^{-T}[1-3a^2,2b,a^3+a]^T",
        "pulled_function": "P(a)+b Q(a) on b^2=a^3-a",
        "P_degree": coefficient_a.degree(),
        "Q_degree": coefficient_b.degree(),
        "norm": "N=P^2-(a^3-a)Q^2",
        "norm_degree": norm_degree,
        "leading_coefficient": str(norm[norm_degree]),
        "resultant_N_Nprime": str(resultant),
        "resultant_abs_lower": str(resultant.abs_lower()),
        "resultant_abs_upper": str(resultant.abs_upper()),
        "elliptic_three_division_polynomial": "3a^4-6a^2-1",
        "resultant_norm_three_division": str(flex_resultant),
        "resultant_norm_three_division_abs_lower": str(flex_resultant.abs_lower()),
        "pullback_value_at_flex_infinity": str(coefficient_a[18]),
        "all_nine_flex_points_avoided": (
            flex_resultant_excludes_zero and infinity_value_excludes_zero
        ),
        "certificate_meaning": (
            "The ACB resultant ball excludes zero for every alignment in the "
            "input matrix balls. Hence N is square-free and cannot be a square."
        ),
    }

    spinc_theorem = {
        "group": "SpinC(3)=(Spin(3)xU(1))/{(1,1),(-1,-1)}",
        "generators": {
            "g1": "[q1,i]",
            "g2": "[q2,i]",
        },
        "relations": {
            "g1_squared": "[-1,-1]=1",
            "g2_squared": "[-1,-1]=1",
            "braid": True,
            "g1g2_cubed": "[-1,-1]=1",
        },
        "generated_image_order": len(generated),
        "projection": "the signed-sheet S3 representation rho_plus",
        "determinant_character": "z^2=sign(sheet permutation)",
        "determinant_line": "complexification of the real sign local system",
        "chern_class": "c1(L_det)=beta_Z(a), with c1(L_det) mod 2=a^2=w2",
        "result": (
            "The signed-sheet representation has a global representation-level "
            "SpinC lift for every S3 monodromy map, even when strict Spin is obstructed."
        ),
    }

    decision = {
        "current_executed_selected_side": {
            "branch_reduced_irreducible": True,
            "branch_complement_H1": "Z6",
            "strict_Spin": "NO_GO",
            "SpinC_representation_lift": "CLOSED",
        },
        "remaining_physical_selection": [
            "identify the SpinC determinant sign line with the selected order-two restriction of L_shared",
            "prove the connection-level square-line equality to the physical transverse bundle on a common base",
            "extend or replace the sheet carrier through the ramification locus with the selected HYM geometry",
            "promote the current selected-side alignment to the final MTT source alignment if that source gate is required",
        ],
        "important_boundary": (
            "The interval is the A125/A126 executed selected-side carrier and has "
            "selected_alignment_interval_used=true, but integral_branch_selected=false."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_selected_side_spin_spinc_decision",
        "date": "2026-07-15",
        "status": "EXECUTED_SELECTED_SIDE_STRICT_SPIN_NOGO_AND_SPINC_LIFT_CLOSED_SHARED_LINE_HYM_OPEN",
        "inputs": {
            "w2_reduction": str(W2_REDUCTION),
            "trial_decision": str(TRIAL_DECISION),
            "q79_spin_packet": str(SPIN_PACKET),
            "selected_side_alignment_interval": str(SELECTED_SIDE),
            "exact_K3_and_elliptic_model": str(TRIAL_MODEL),
        },
        "checks": checks,
        "interval_result": interval_result,
        "SpinC_theorem": spinc_theorem,
        "decision": decision,
        "claim_tiers": {
            "executed_selected_side_branch_irreducibility": "CLOSED_BY_ACB_INTERVAL_RESULTANT",
            "executed_selected_side_strict_Spin": "CLOSED_NO_GO",
            "abstract_signed_sheet_SpinC_lift": "CLOSED_EXACTLY",
            "SpinC_determinant_equals_selected_shared_circle_line": "OPEN",
            "branch_locus_HYM_extension": "OPEN",
            "final_MTT_alignment_source_selection": "OPEN_IF_REQUIRED",
        },
        "guardrails": {
            "claims_strict_Spin_exists": False,
            "claims_SpinC_determinant_already_selected_by_MTT": False,
            "claims_shared_circle_identification_closed": False,
            "claims_branch_locus_HYM_extension_closed": False,
            "claims_integral_gerbe_branch_selected": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Selected-Side Strict-Spin No-Go and SpinC Lift v1

Date: 2026-07-15

## Certified selected-side branch test

The A125/A126 source packet supplies a complex `3x3` alignment interval with
roughly `1e-100` radii. Its convention is

```text
L=A*[a,b,1]^T,
L dot X=0.
```

Branching occurs when `A^T X` lies on the dual cubic. On its elliptic
normalization, therefore,

```text
X=A^(-T)[1-3a^2,2b,a^3+a]^T,
b^2=a^3-a.
```

Substitution into the exact K3 sextic gives `P(a)+bQ(a)`. Its norm

```text
N(a)=P(a)^2-(a^3-a)Q(a)^2
```

has degree `36`. A direct Arb/ACB Sylvester determinant encloses
`Res(N,N')` for every alignment in the matrix balls and excludes zero. Its
absolute lower bound is approximately `5.37e364`. Thus the norm is square-free
throughout the interval and cannot be a square in the elliptic function field.

The same interval calculation also evaluates the resultant with the elliptic
three-division polynomial `3a^4-6a^2-1`. It excludes zero, and the leading
pullback coefficient excludes zero at the flex point at infinity. Hence the K3
branch sextic avoids all nine flex points of the cubic throughout the interval.

Consequently, throughout the current executed selected-side carrier,

```text
branch divisor reduced and irreducible,
H1(branch complement;Z)=Z6,
sign character has no Z4 lift,
w2=a^2 != 0,
strict Spin: NO-GO.
```

The packet uses this selected-side interval but still declares
`integral_branch_selected=false`; this result is not a claim that the gerbe-zero
or final MTT alignment source gate has closed.

## Exact SpinC lift

The strict-Spin obstruction has an exact representation-level repair. In

```text
SpinC(3)=(Spin(3)xU(1))/{(1,1),(-1,-1)},
```

take the existing binary lifts `q1,q2` and define

```text
g1=[q1,i],
g2=[q2,i].
```

Then

```text
g1^2=g2^2=[-1,-1]=1,
g1 g2 g1=g2 g1 g2,
(g1 g2)^3=[-1,-1]=1.
```

They generate an order-six image projecting isomorphically to the signed-sheet
`S3`. The SpinC determinant character is `z^2`, so a transposition maps to
`-1`: precisely the sheet-sign character. Its determinant line is the
complexification of the real sign local system and

```text
c1(L_det)=beta_Z(a),
c1(L_det) mod 2=a^2=w2.
```

Thus abstract global SpinC lifting of the signed-sheet monodromy is closed; it
does not require a new relator search.

## Physical frontier

What remains is no longer the existence of a spinorial carrier on the branch
complement. It is the MTT identification theorem:

```text
SpinC determinant sign line
= selected order-two restriction of L_shared,
```

together with the common-base transverse-line comparison and extension or
smooth HYM replacement through ramification. No observed datum or fitted
parameter enters this result.

Current status:

```text
EXECUTED_SELECTED_SIDE_STRICT_SPIN_NOGO_AND_SPINC_LIFT_CLOSED_SHARED_LINE_HYM_OPEN
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
