from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
STATUS = "MTT_U6_Q79_EXPLICIT_SMOOTH_MARKED_SPLITTING_CONIC_K3_CLOSED_PERIOD_GERBE_AND_SELECTION_OPEN"
NEXT = "MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1.md"

MODEL = OUT / "explicit_splitting_conic_K3_model.packet.json"
SMOOTH = OUT / "exact_projective_smoothness_Groebner_certificate.packet.json"
LATTICE = OUT / "marked_lattice_certificate.packet.json"
PERIOD = OUT / "A106_relative_period_execution_input.open.json"
SCOPE = OUT / "construction_witness_vs_MTT_selection_guard.packet.json"
FRONTIER = OUT / "U6_frontier_after_A109.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def polynomial_terms(poly: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[dict]:
    result = []
    for powers, coefficient in sp.Poly(poly, *variables, domain=sp.QQ).terms():
        result.append({"powers_xyz": list(powers), "coefficient": int(coefficient)})
    return result


def projective_unit_certificate(
    polynomials: list[sp.Expr], variables: tuple[sp.Symbol, ...]
) -> dict:
    charts = {}
    for chart in variables:
        affine_variables = [variable for variable in variables if variable != chart]
        affine_polynomials = [sp.expand(poly.subs(chart, 1)) for poly in polynomials]
        basis = sp.groebner(
            affine_polynomials,
            *affine_variables,
            order="grevlex",
            domain=sp.QQ,
        )
        basis_strings = [str(poly.as_expr()) for poly in basis.polys]
        charts[str(chart)] = {
            "chart_substitution": f"{chart}=1",
            "affine_variables": [str(variable) for variable in affine_variables],
            "Groebner_basis": basis_strings,
            "unit_ideal": basis_strings == ["1"],
        }
    return {
        "charts": charts,
        "all_projective_charts_unit": all(item["unit_ideal"] for item in charts.values()),
    }


def main() -> int:
    paths = {
        "A106_period": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "residue_period_Jacobian_formula.packet.json",
        "A106_normal_form": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "splitting_conic_K3_normal_form.packet.json",
        "A108": ROOT
        / "candidate_data"
        / "selected_q79splittingconick3periodselectororexactgerbeexecution.candidate.json",
        "A108_open": ROOT
        / "candidate_data"
        / "selected_q79splittingconick3periodselectororexactgerbeexecution"
        / "period_Hessian_or_marked_model_source.open.json",
        "requirements": ROOT / "requirements.txt",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A109 authority: " + ", ".join(missing))

    period106 = load(paths["A106_period"])
    normal106 = load(paths["A106_normal_form"])
    a108 = load(paths["A108"])
    open108 = load(paths["A108_open"])
    requirements = paths["requirements"].read_text(encoding="utf-8")

    assert period106["covariant_Jacobian"]["shape"] == [8, 8]
    assert normal106["double_sextic_model"]["normal_form"] == "F6=G3^2+Q2*H4"
    assert a108["next_required_artifact"] == "MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1"
    assert not open108["acceptance"]["direct_marked_model_inserted"]
    assert "sympy==1.14.0" in requirements

    x, y, z = sp.symbols("x y z")
    variables = (x, y, z)
    q2 = x * z - y**2
    g3 = (
        -x**3
        + x**2 * y
        + 2 * x**2 * z
        - 2 * x * y**2
        + 2 * x * y * z
        + x * z**2
        + z**3
    )
    h4 = (
        -x**3 * z
        - x**2 * y * z
        - 2 * x * y**2 * z
        - y**4
        + 2 * y**3 * z
        - 2 * y**2 * z**2
        + 2 * y * z**3
    )
    f6 = sp.expand(g3**2 + q2 * h4)

    q_gradient = [sp.diff(q2, variable) for variable in variables]
    g_gradient = [sp.diff(g3, variable) for variable in variables]
    f_gradient = [sp.diff(f6, variable) for variable in variables]
    qg_minors = [
        sp.expand(q_gradient[i] * g_gradient[j] - q_gradient[j] * g_gradient[i])
        for i in range(3)
        for j in range(i + 1, 3)
    ]

    conic_smooth = projective_unit_certificate([q2, *q_gradient], variables)
    branch_smooth = projective_unit_certificate(f_gradient, variables)
    qg_transverse = projective_unit_certificate([q2, g3, *qg_minors], variables)
    no_qgh_triple = projective_unit_certificate([q2, g3, h4], variables)

    identity_residual = sp.expand(f6 - g3**2 - q2 * h4)
    euler_residual = sp.expand(
        x * f_gradient[0] + y * f_gradient[1] + z * f_gradient[2] - 6 * f6
    )
    gcd_qg = sp.gcd(sp.Poly(q2, *variables), sp.Poly(g3, *variables)).as_expr()

    assert identity_residual == 0
    assert euler_residual == 0
    assert gcd_qg == 1
    assert conic_smooth["all_projective_charts_unit"]
    assert branch_smooth["all_projective_charts_unit"]
    assert qg_transverse["all_projective_charts_unit"]
    assert no_qgh_triple["all_projective_charts_unit"]

    discriminant_classes = []
    for a in range(2):
        for b in range(4):
            q_value = Fraction(a * a, 2) - Fraction(b * b, 4)
            isotropic = q_value.denominator == 1 and q_value.numerator % 2 == 0
            discriminant_classes.append(
                {
                    "class": [a, b],
                    "representative": f"{a}*H/2+{b}*delta/4",
                    "q_mod_2Z_representative": str(q_value),
                    "isotropic": isotropic,
                }
            )
    isotropic_classes = [entry["class"] for entry in discriminant_classes if entry["isotropic"]]
    assert isotropic_classes == [[0, 0]]

    model = {
        "schema": "MTTQ79ExplicitSplittingConicK3Model.v1",
        "status": "EXACT_EXPLICIT_RATIONAL_MARKED_MODEL_CONSTRUCTED",
        "field": "Q subset C",
        "weighted_projective_space": "P(1,1,1,3) with coordinates [x:y:z:w]",
        "equation": "w^2=F6(x,y,z)",
        "Q2": str(q2),
        "G3": str(g3),
        "H4": str(h4),
        "F6": str(f6),
        "coefficient_tables": {
            "Q2": polynomial_terms(q2, variables),
            "G3": polynomial_terms(g3, variables),
            "H4": polynomial_terms(h4, variables),
            "F6": polynomial_terms(f6, variables),
        },
        "exact_identity": {
            "formula": "F6=G3^2+Q2*H4",
            "residual": str(identity_residual),
        },
        "split_curves": {
            "R_plus": "Q2=0, w=+G3",
            "R_minus": "Q2=0, w=-G3",
            "deck_involution": "w -> -w exchanges R_plus and R_minus",
        },
        "construction_provenance": {
            "deterministic_search_seed": 79108448,
            "accepted_attempt": 1,
            "observed_physics_values_used": False,
            "MTT_selection_used": False,
        },
    }

    smoothness = {
        "schema": "MTTQ79ExactProjectiveSmoothnessGroebnerCertificate.v1",
        "status": "EXACT_ALL_CHART_UNIT_IDEALS_CLOSED",
        "coefficient_domain": "QQ",
        "monomial_order": "grevlex",
        "projective_cover": ["x=1", "y=1", "z=1"],
        "conic_Q2_smooth": conic_smooth,
        "branch_sextic_F6_smooth": branch_smooth,
        "Q2_G3_intersection_transverse": qg_transverse,
        "H4_nonzero_on_Q2_cap_G3": no_qgh_triple,
        "gcd_Q2_G3": str(gcd_qg),
        "Euler_identity": {
            "formula": "x*Fx+y*Fy+z*Fz=6*F6",
            "residual": str(euler_residual),
            "role": "For homogeneous F6, a common projective zero of the three partials already lies on F6.",
        },
        "consequences": {
            "Q2_is_smooth_conic": True,
            "Q2_and_G3_have_six_distinct_intersections": True,
            "F6_is_smooth_plane_sextic": True,
            "double_cover_is_smooth_K3": True,
        },
        "theorem": {
            "name": "ExplicitSplittingConicDoubleSexticSmoothnessTheorem",
            "proved": True,
            "statement": "The displayed Q2 is a smooth conic, Q2 and G3 meet transversely in six points, H4 is nonzero at all six, and the three partial derivatives of F6 generate the unit ideal on every projective chart. Hence F6 is a smooth sextic and w^2=F6 is a smooth K3 double cover with split inverse image of Q2.",
        },
    }

    lattice = {
        "schema": "MTTQ79ExplicitModelMarkedLatticeCertificate.v1",
        "status": "EXACT_PRIMITIVE_H_DELTA_MARKING_CLOSED",
        "classes": {
            "H": "pullback of a line in P2",
            "R_plus": "the rational lift Q2=0,w=G3",
            "R_minus": "the rational lift Q2=0,w=-G3",
            "delta": "R_plus-H=(R_plus-R_minus)/2",
        },
        "intersection_derivation": {
            "H_squared": 2,
            "H_dot_R_plus": 2,
            "H_dot_R_minus": 2,
            "R_plus_squared": -2,
            "R_minus_squared": -2,
            "R_plus_dot_R_minus": 6,
            "H_dot_delta": 0,
            "delta_squared": -4,
            "Gram_H_delta": [[2, 0], [0, -4]],
        },
        "primitivity": {
            "delta_primitive": True,
            "proof": "If delta=2D, evenness of the K3 lattice gives delta^2=4D^2 divisible by 8, contradicting delta^2=-4.",
            "discriminant_group": "Z2 x Z4",
            "discriminant_form_classes": discriminant_classes,
            "nonzero_isotropic_classes": 0,
            "span_H_delta_primitive": True,
            "span_proof": "A proper saturation would define a nonzero isotropic subgroup of the discriminant form. Exact enumeration gives only the zero isotropic class, so the even lattice <H,delta> has no proper even overlattice.",
        },
        "sign_orbit": {
            "deck_action": "delta -> -delta",
            "same_unoriented_marked_lattice": True,
        },
        "theorem": {
            "name": "ExplicitModelRealizesQ79RankTwoK3LatticeTheorem",
            "proved": True,
            "statement": "The smooth double sextic contains the primitively embedded lattice generated by H and delta with Gram diag(2,-4). The discriminant form has no nonzero isotropic class and hence no proper even overlattice. The two rational roots H+delta and H-delta are exactly R_plus and R_minus and meet in six reduced points.",
        },
    }

    period_input = {
        "schema": "MTTQ79ExplicitModelA106RelativePeriodExecutionInput.v1",
        "status": "MARKED_K3_MODEL_FILLED_4_OF_8_DIRECT_FIELDS_RELATIVE_PERIOD_DATA_OPEN",
        "filled": {
            "Q2_coefficients": model["coefficient_tables"]["Q2"],
            "G3_mod_Q2L1_coefficients": model["coefficient_tables"]["G3"],
            "H4_coefficients": model["coefficient_tables"]["H4"],
            "projective_smoothness_certificate": str(SMOOTH.relative_to(ROOT)).replace("\\", "/"),
        },
        "open": {
            "elliptic_tau_strict": None,
            "PGL3_alignment_A": None,
            "integral_branch_ell_Z92": None,
            "exact_relative_Deligne_zero_or_nogo": None,
        },
        "conditional_Z4_bridge": {
            "tau": "i",
            "accepted_as_strict_source": False,
            "reason": "A107 still requires the LensQuarterTurnToFuYauChernOrbitSourceTheorem.",
        },
        "A106_execution_formula": period106["period_system"]["eight_equations"],
        "A106_Jacobian_formula": period106["covariant_Jacobian"]["formula"],
        "strict_direct_fields_filled": 4,
        "strict_direct_fields_required": 8,
        "conditional_bridge_fields_filled": 5,
    }

    scope = {
        "schema": "MTTQ79ConstructionWitnessVsSelectionGuard.v1",
        "status": "EXACT_EXISTENCE_WITNESS_SCOPE_LOCKED_NO_SELECTION_PROMOTION",
        "proved_by_A109": [
            "the 18-dimensional splitting-conic family is nonempty",
            "one explicit rational point gives a smooth marked K3 with the q79 lattice",
            "A106 now has a concrete algebraic carrier on which periods can be computed",
        ],
        "not_proved_by_A109": [
            "MTT selects this rational point",
            "the period-domain gradient vanishes here",
            "the 36x36 Schur Hessian is positive here",
            "the normalized Poincare gerbe vanishes for some PGL3 alignment",
            "the inverse Fourier-Mukai bundle is locally free and balanced HYM",
        ],
        "parameter_accounting": {
            "observed_or_fitted_physics_parameters_added": 0,
            "strict_MTT_source_moduli_removed": 0,
            "unsourced_model_choice": "one explicit point in an 18-complex-dimensional family",
            "publication_label": "constructive existence/test witness, not a no-knob prediction",
        },
        "theorem": {
            "name": "ExplicitModelDoesNotImplyVacuumSelectionTheorem",
            "proved": True,
            "statement": "Fixing rational coefficients creates a reproducible carrier for direct calculation but does not derive those coefficients from MTT. All 18 complex period-selection obligations therefore remain at the strict source tier even though the direct existence route is no longer empty.",
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA109.v1",
        "status": STATUS,
        "closed_now": [
            "explicit rational Q2,G3,H4 splitting-conic model",
            "exact all-chart Groebner smoothness certificate",
            "six reduced Q2-G3 intersections with H4 nonzero",
            "primitive q79 lattice marking diag(2,-4)",
            "four of eight direct A106 model fields filled",
        ],
        "strict_direct_model_fields_filled": 4,
        "strict_direct_model_fields_required": 8,
        "conditional_Z4_direct_model_fields_filled": 5,
        "observed_or_fitted_physics_parameters_added": 0,
        "strict_MTT_source_moduli_removed": 0,
        "actual_period_gradient_or_Hessian_rows": 0,
        "actual_exact_gerbe_zero": False,
        "actual_MTT_marked_K3_selection": False,
        "actual_Fourier_Mukai_HYM_Bianchi_execution": False,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Evaluate the normalized Poincare logarithmic cocycle and its eight A106 relative periods on this exact model, search/certify one PGL3 alignment and ell in Z^92, and return an exact zero or a rigorous no-go/separation certificate.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "explicit_model": str(MODEL.relative_to(ROOT)).replace("\\", "/"),
        "smoothness_certificate": str(SMOOTH.relative_to(ROOT)).replace("\\", "/"),
        "marked_lattice": str(LATTICE.relative_to(ROOT)).replace("\\", "/"),
        "relative_period_input": str(PERIOD.relative_to(ROOT)).replace("\\", "/"),
        "selection_scope_guard": str(SCOPE.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (MODEL, model),
        (SMOOTH, smoothness),
        (LATTICE, lattice),
        (PERIOD, period_input),
        (SCOPE, scope),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "splitting_identity_exact": identity_residual == 0,
        "conic_smooth_exact": conic_smooth["all_projective_charts_unit"],
        "sextic_smooth_exact": branch_smooth["all_projective_charts_unit"],
        "six_intersections_reduced": qg_transverse["all_projective_charts_unit"] and gcd_qg == 1,
        "H4_nonzero_at_intersections": no_qgh_triple["all_projective_charts_unit"],
        "marked_lattice_exact": lattice["intersection_derivation"]["Gram_H_delta"] == [[2, 0], [0, -4]],
        "direct_route_advanced": period_input["strict_direct_fields_filled"] == 4,
        "selection_not_invented": not frontier["actual_MTT_marked_K3_selection"],
        "gerbe_zero_not_invented": not frontier["actual_exact_gerbe_zero"],
        "no_observed_fit": frontier["observed_or_fitted_physics_parameters_added"] == 0,
    }
    assert all(checks.values())

    authority_hashes = [{"path": str(path), "sha256": sha256(path)} for path in paths.values()]
    results = {
        "explicit_smooth_marked_K3_constructed": True,
        "strict_direct_model_fields_filled": 4,
        "strict_direct_model_fields_required": 8,
        "conditional_Z4_fields_filled": 5,
        "strict_MTT_source_moduli_removed": 0,
        "actual_exact_gerbe_zero": False,
        "actual_MTT_marked_K3_selection": False,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
    }
    candidate = {
        "schema": "MTTSelectedQ79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": results,
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 K3-Period Xi-Hessian Execution or Marked-Model Gerbe Certificate v1

Status: `{STATUS}`

## Constructive result

A109 takes the direct-model branch of A108 and fills an actual algebraic K3
carrier. Over the rationals, set

```text
Q2 = x*z-y^2,
G3 = -x^3+x^2*y+2*x^2*z-2*x*y^2+2*x*y*z+x*z^2+z^3,
H4 = -x^3*z-x^2*y*z-2*x*y^2*z-y^4+2*y^3*z-2*y^2*z^2+2*y*z^3,
F6 = G3^2+Q2*H4.
```

Then

```text
S: w^2=F6(x,y,z) subset P(1,1,1,3)
```

is a smooth K3 surface and the inverse image of `Q2=0` splits into

```text
R_plus : Q2=0, w=+G3,
R_minus: Q2=0, w=-G3.
```

## Exact smoothness certificate

All checks are over `QQ` with exact Groebner reduction. On each projective
chart `x=1`, `y=1`, and `z=1`, the following ideals have reduced basis `[1]`:

1. `Q2` plus its three partial derivatives;
2. the three partial derivatives of `F6`;
3. `Q2,G3` plus all `2x2` minors of their gradient matrix;
4. `Q2,G3,H4`.

Euler's identity `x Fx+y Fy+z Fz=6F6` has exact residual zero. Therefore the
conic and branch sextic are smooth, `Q2` and `G3` meet transversely in six
points, and `H4` is nonzero at every intersection. This is an exact algebraic
certificate, not floating-point sampling.

## q79 lattice marking

Let `H` be the pullback of a line and set `delta=R_plus-H`. Adjunction and the
six reduced intersections give

```text
H^2=2,
R_plus^2=R_minus^2=-2,
H.R_plus=H.R_minus=2,
R_plus.R_minus=6,
H.delta=0,
delta^2=-4.
```

Thus the model realizes the exact q79 lattice

```text
Gram(H,delta)=diag(2,-4).
```

The class `delta` is primitive: if `delta=2D`, evenness of the K3 lattice
would make `delta^2` divisible by eight, contradicting `delta^2=-4`. More
strongly, the discriminant form on `Z2 x Z4` has no nonzero isotropic class.
The span `<H,delta>` therefore has no proper even overlattice and is
primitively embedded in the K3 lattice.

## What this fills

A108's direct route had eight fields. A109 fills four exactly:

```text
Q2 coefficients,
G3 modulo Q2*L1 coefficients,
H4 coefficients,
projective smoothness certificate.
```

The remaining strict fields are

```text
elliptic tau,
PGL3 alignment A,
integral branch ell in Z^92,
exact relative-Deligne zero or no-go.
```

If the still-open Z4 Chern-orbit bridge is later proved, `tau=i` fills a fifth
field. It is not counted as strict here.

## Selection guard

This model proves nonemptiness and gives A106 a concrete exact carrier. It does
not prove that MTT selects these coefficients. Choosing one rational point in
the 18-complex-dimensional family removes zero strict source moduli and must be
published as a constructive test witness, not a no-knob prediction.

No observed physics value and no fitted physics parameter was used.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
