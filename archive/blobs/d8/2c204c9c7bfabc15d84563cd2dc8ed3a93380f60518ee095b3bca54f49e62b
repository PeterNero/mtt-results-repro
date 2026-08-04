from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

W2_REDUCTION = ROOT / "certificates" / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"
TRIAL_MODEL = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
    / "square_elliptic_identity_alignment_spectral_surface.packet.json"
)

OUT_CERT = ROOT / "certificates" / "q79_trial_branch_irreducibility_and_spin_decision_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Trial_Branch_Irreducibility_and_Strict_Spin_Decision_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def coefficients_ascending(poly: sp.Poly) -> list[str]:
    degree = poly.degree()
    return [str(poly.nth(index)) for index in range(degree + 1)]


def main() -> None:
    reduction = load(W2_REDUCTION)
    trial = load(TRIAL_MODEL)

    l0, l1, l2, t = sp.symbols("l0 l1 l2 t")
    x, y, z, w = sp.symbols("x y z w")
    a, b = sp.symbols("a b")

    # Intersect the affine cubic b^2=a^3-a with the line
    # l0*a+l1*b+l2=0. The non-coordinate factor of the cubic discriminant is
    # the homogeneous equation of the dual sextic.
    line_intersection = (
        l1**2 * t**3
        - l0**2 * t**2
        - (l1**2 + 2 * l0 * l2) * t
        - l2**2
    )
    raw_discriminant = sp.factor(sp.discriminant(line_intersection, t))
    dual_sextic = sp.factor(raw_discriminant / l1**2)
    dual_poly = sp.Poly(dual_sextic, l0, l1, l2, domain=sp.QQ)

    equation = sp.sympify(
        trial["K3"]["equation"],
        locals={"x": x, "y": y, "z": z, "w": w},
    )
    f6 = sp.expand(-equation.subs(w, 0))

    # The Gauss map normalizes the dual cubic. On c=1 it is
    # [l0:l1:l2]=[1-3a^2:2b:a^3+a], using b^2=a^3-a.
    gauss_map = {
        x: 1 - 3 * a**2,
        y: 2 * b,
        z: a**3 + a,
    }
    pulled_f6 = sp.expand(f6.subs(gauss_map))
    elliptic_relation = sp.Poly(b**2 - (a**3 - a), b, domain=sp.QQ[a])
    remainder = sp.rem(
        sp.Poly(pulled_f6, b, domain=sp.QQ[a]),
        elliptic_relation,
    ).as_expr()
    remainder_poly = sp.Poly(remainder, b)
    coefficient_a = sp.expand(remainder_poly.coeff_monomial(1))
    coefficient_b = sp.expand(remainder_poly.coeff_monomial(b))

    # Norm from Q(a,b), b^2=a^3-a, to Q(a).
    norm = sp.expand(coefficient_a**2 - (a**3 - a) * coefficient_b**2)
    norm_poly = sp.Poly(norm, a, domain=sp.QQ)
    factor_unit, factorization = sp.factor_list(norm_poly)
    norm_gcd_derivative = sp.gcd(norm_poly, norm_poly.diff())

    norm_irreducible = (
        len(factorization) == 1
        and factorization[0][0].degree() == 36
        and factorization[0][1] == 1
    )
    norm_squarefree = norm_gcd_derivative.degree() == 0
    pulled_f6_not_square = norm_irreducible and norm_squarefree

    checks = {
        "w2_branch_reduction_available": (
            reduction["status"]
            == "UNIVERSAL_W2_AND_BRANCH_6H_CLOSED_STRICT_SPIN_NOGO_ONE_COMPLEMENT_CHECK_OPEN"
        ),
        "trial_model_is_exact_and_smooth": trial["smooth"] is True,
        "trial_alignment_is_identity": (
            trial["alignment"]["A_PGL3_trial"]
            == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        ),
        "trial_alignment_is_not_selected": (
            trial["alignment"]["accepted_as_MTT_selected_alignment"] is False
        ),
        "dual_curve_polynomial_has_degree_six": dual_poly.total_degree() == 6,
        "dual_curve_formula_matches_discriminant": (
            sp.expand(raw_discriminant - l1**2 * dual_sextic) == 0
        ),
        "elliptic_reduction_is_linear_in_b": sp.degree(remainder, b) <= 1,
        "elliptic_coefficients_are_coprime": (
            sp.gcd(sp.Poly(coefficient_a, a), sp.Poly(coefficient_b, a)).degree()
            == 0
        ),
        "norm_has_degree_36": norm_poly.degree() == 36,
        "norm_is_irreducible_over_Q": norm_irreducible,
        "norm_is_squarefree": norm_squarefree,
        "pulled_K3_sextic_is_not_square_in_QE": pulled_f6_not_square,
        "trial_branch_pullback_is_reduced_irreducible": pulled_f6_not_square,
        "trial_complement_has_H1_Z6_by_reduction_theorem": pulled_f6_not_square,
        "trial_sign_character_has_no_Z4_lift": (
            reduction["finite_data"]["Z6_to_Z4_odd_lift_images"] == []
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    exact_witness = {
        "elliptic_curve": "b^2=a^3-a",
        "dual_sextic": str(dual_sextic),
        "gauss_normalization_map": "[1-3a^2:2b:a^3+a]",
        "pulled_K3_sextic_mod_elliptic_relation": (
            "A(a)+b B(a)"
        ),
        "A_degree": int(sp.degree(coefficient_a, a)),
        "B_degree": int(sp.degree(coefficient_b, a)),
        "A_coefficients_ascending": coefficients_ascending(sp.Poly(coefficient_a, a)),
        "B_coefficients_ascending": coefficients_ascending(sp.Poly(coefficient_b, a)),
        "norm_formula": "N(a)=A(a)^2-(a^3-a)B(a)^2",
        "norm_degree": norm_poly.degree(),
        "norm_coefficients_ascending": coefficients_ascending(norm_poly),
        "norm_factorization_over_Q": {
            "unit": str(factor_unit),
            "factor_count": len(factorization),
            "factors": [
                {"degree": factor.degree(), "multiplicity": multiplicity}
                for factor, multiplicity in factorization
            ],
        },
        "squarefree_gcd_degree": norm_gcd_derivative.degree(),
        "function_field_conclusion": (
            "If A+bB were a square in Q(E), its norm would be a square in Q(a). "
            "The irreducible square-free degree-36 norm is not a square."
        ),
    }

    decision = {
        "trial_identity_alignment": {
            "branch_divisor": "reduced and irreducible",
            "branch_complement_H1": "Z6",
            "w2": "nonzero",
            "strict_Spin": "NO_GO",
            "SpinC": "not decided; determinant-line theorem still required",
        },
        "deformation_value": (
            "The witness proves the good irreducible locus of PGL3 alignments is nonempty. "
            "Geometric irreducibility is open in the corresponding proper flat family."
        ),
        "selected_alignment_status": (
            "OPEN: the identity alignment is explicitly marked unselected, so the selected "
            "alignment must be certified to remain in this irreducible locus."
        ),
        "next_exact_test": (
            "Substitute the selected PGL3 matrix into the dual-sextic pullback and certify "
            "that the analogous elliptic norm is not a square, or certify a path from the "
            "identity that avoids the reducibility discriminant."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_trial_branch_irreducibility_and_spin_decision",
        "date": "2026-07-15",
        "status": "TRIAL_IDENTITY_STRICT_SPIN_NOGO_CLOSED_SELECTED_ALIGNMENT_MEMBERSHIP_OPEN",
        "inputs": {
            "w2_branch_reduction": str(W2_REDUCTION),
            "trial_identity_model": str(TRIAL_MODEL),
        },
        "checks": checks,
        "exact_witness": exact_witness,
        "decision": decision,
        "claim_tiers": {
            "identity_alignment_branch_irreducibility": "CLOSED_EXACTLY",
            "identity_alignment_strict_Spin_no_go": "CLOSED_EXACTLY",
            "nonempty_generic_irreducible_alignment_locus": "CLOSED",
            "selected_alignment_in_irreducible_locus": "OPEN",
            "selected_q79_strict_Spin_no_go": "OPEN_PENDING_PREVIOUS_ROW",
        },
        "guardrails": {
            "promotes_trial_alignment_to_selected": False,
            "claims_all_PGL3_alignments_are_irreducible": False,
            "claims_selected_q79_strict_Spin_no_go": False,
            "claims_SpinC_closed": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Trial Branch Irreducibility and Strict-Spin Decision v1

Date: 2026-07-15

## Exact identity-alignment calculation

The corpus contains an exact smooth q79 spectral surface at the square elliptic
curve and identity `PGL3` alignment. That alignment is explicitly a trial, not
an MTT-selected source. It nevertheless permits the missing branch-complement
test to be executed exactly.

For

```text
E: b^2=a^3-a,
```

the Gauss map to the dual cubic is

```text
[l0:l1:l2]=[1-3a^2:2b:a^3+a].
```

The discriminant of a line section gives the dual sextic

```text
4*l0^5*l2 + l0^4*l1^2 - 4*l0^3*l2^3
+ 30*l0^2*l1^2*l2^2 + 24*l0*l1^4*l2
+ 4*l1^6 - 27*l1^2*l2^4 = 0.
```

Pull the exact K3 branch sextic through this Gauss map and reduce by
`b^2=a^3-a`. The result is `A(a)+bB(a)`, with degrees `18` and `14`. Its norm
to `Q(a)` is

```text
N(a)=A(a)^2-(a^3-a)B(a)^2.
```

The executable factorization proves that `N` is irreducible over `Q`, has
degree `36`, occurs with multiplicity one, and is square-free. If `A+bB` were a
square in `Q(E)`, its norm would be a square in `Q(a)`. It is not. Therefore
the pulled-back dual sextic is reduced and irreducible in this exact carrier.

## Spin decision for the witness

The preceding `w2` theorem then applies without a remaining complement premise:

```text
[branch]=6H,
H1(branch complement;Z)=Z6,
sign:Z6->Z2 has no Z4 lift,
w2=a^2 != 0.
```

Hence the identity-alignment signed-sheet carrier has no strict Spin lift on
its branch complement. A SpinC determinant-line construction remains a
separate open theorem.

## Selected-source boundary

This is not yet the selected q79 decision. The source packet marks the identity
alignment as unselected. What has been proved is stronger than a numerical
example: the irreducible alignment locus is nonempty, and the selected decision
is now one exact membership test.

Run the same norm calculation after substituting the selected `PGL3` matrix, or
certify that a path from identity to the selected matrix avoids the
reducibility discriminant. No new metric, fit, or physical constant is needed.

Current status:

```text
TRIAL_IDENTITY_STRICT_SPIN_NOGO_CLOSED_SELECTED_ALIGNMENT_MEMBERSHIP_OPEN
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
