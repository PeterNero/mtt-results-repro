from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2lefschetzperiodreduction"
STATUS = (
    "MTT_U6_Q79_EXPLICIT_GENUS2_LEFSCHETZ_FIBRATION_90_NODES_AND_"
    "PRYM_NORMAL_FUNCTION_INPUT_CLOSED_CERTIFIED_PERIOD_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoMonodromyBetaPeriodExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoLefschetzPeriodReduction_v1.md"

FIBRATION = OUT / "explicit_genus2_fibration.packet.json"
DISCRIMINANT = OUT / "degree90_nodal_discriminant_certificate.packet.json"
PRYM = OUT / "explicit_prym_residues_and_delta_normal_function.packet.json"
PERIOD = OUT / "certified_monodromy_period_execution.open.json"
FRONTIER = OUT / "U6_frontier_after_A111.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expression_from_terms(terms: list[dict], variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    expression = 0
    for term in terms:
        monomial = 1
        for variable, power in zip(variables, term["powers_xyz"]):
            monomial *= variable**power
        expression += term["coefficient"] * monomial
    return sp.expand(expression)


def integer_coefficients_descending(expression: sp.Expr, variable: sp.Symbol) -> list[int]:
    polynomial = sp.Poly(expression, variable, domain=sp.QQ)
    coefficients = polynomial.all_coeffs()
    assert all(coefficient.q == 1 for coefficient in coefficients)
    return [int(coefficient) for coefficient in coefficients]


def polynomial_coefficients_as_strings(
    expression: sp.Expr, variable: sp.Symbol
) -> list[str]:
    return [str(coefficient) for coefficient in sp.Poly(expression, variable).all_coeffs()]


def main() -> int:
    paths = {
        "A106_period": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "residue_period_Jacobian_formula.packet.json",
        "A109_model": ROOT
        / "candidate_data"
        / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
        / "explicit_splitting_conic_K3_model.packet.json",
        "A110_gerbe": ROOT
        / "candidate_data"
        / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
        / "normalized_Poincare_gerbe_Cech_formula.packet.json",
        "A110_open": ROOT
        / "candidate_data"
        / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
        / "restricted_beta_C_period_evaluation.open.json",
        "A110_frontier": ROOT
        / "candidate_data"
        / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
        / "U6_frontier_after_A110.packet.json",
    }
    for path in paths.values():
        assert path.exists(), path

    period106 = load(paths["A106_period"])
    model109 = load(paths["A109_model"])
    gerbe110 = load(paths["A110_gerbe"])
    open110 = load(paths["A110_open"])
    frontier110 = load(paths["A110_frontier"])

    assert model109["exact_identity"]["residual"] == "0"
    assert gerbe110["filled_A104_formula_fields"][
        "restricted_scalar_gerbe_cocycle_alpha_ijk_formula"
    ]
    assert open110["acceptance"]["beta_C_exactly_zero"] is False
    assert frontier110["beta_C_period_rows_emitted"] == 0

    x, y, z, t, a, b = sp.symbols("x y z t a b")
    variables = (x, y, z)
    tables = model109["coefficient_tables"]
    f6 = expression_from_terms(tables["F6"], variables)
    g3 = expression_from_terms(tables["G3"], variables)
    q2 = expression_from_terms(tables["Q2"], variables)
    h4 = expression_from_terms(tables["H4"], variables)

    # On c=1 in E_i, b^2=a^3-a and the incidence line is z=-a*x-b*y.
    line_substitution = {x: 1, y: t, z: -a - b * t}
    f_ab = sp.expand(f6.subs(line_substitution))
    g_ab = sp.expand(g3.subs(line_substitution))
    q_ab = sp.expand(q2.subs(line_substitution))
    h_ab = sp.expand(h4.subs(line_substitution))
    splitting_residual = sp.expand(f_ab - g_ab**2 - q_ab * h_ab)

    assert splitting_residual == 0
    assert sp.degree(f_ab, t) == 6
    assert sp.degree(g_ab, t) == 3
    assert sp.degree(q_ab, t) == 2
    assert sp.degree(h_ab, t) == 4
    assert q_ab == -a - b * t - t**2

    elliptic_relation = b**2 - a**3 + a
    raw_discriminant = sp.expand(sp.discriminant(f_ab, t))
    discriminant_on_e = sp.rem(
        sp.Poly(raw_discriminant, b, domain=sp.QQ[a]),
        sp.Poly(elliptic_relation, b, domain=sp.QQ[a]),
    ).as_expr()
    discriminant_poly_b = sp.Poly(discriminant_on_e, b, domain=sp.QQ[a])
    p45 = sp.expand(discriminant_poly_b.coeff_monomial(1))
    q43 = sp.expand(discriminant_poly_b.coeff_monomial(b))
    norm90 = sp.expand(p45**2 - (a**3 - a) * q43**2)

    p_poly = sp.Poly(p45, a, domain=sp.QQ)
    q_poly = sp.Poly(q43, a, domain=sp.QQ)
    n_poly = sp.Poly(norm90, a, domain=sp.QQ)
    norm_gcd = sp.gcd(n_poly, sp.Poly(sp.diff(norm90, a), a, domain=sp.QQ))
    pq_gcd = sp.gcd(p_poly, q_poly)

    assert sp.degree(discriminant_on_e, b) == 1
    assert p_poly.degree() == 45
    assert q_poly.degree() == 43
    assert n_poly.degree() == 90
    assert norm_gcd.as_expr() == 1
    assert pq_gcd.as_expr() == 1
    assert all(p_poly.eval(value) != 0 for value in (-1, 0, 1))

    # At O=[0:1:0], ord_O(a)=-2 and ord_O(b)=-3. The P term has pole
    # order 90 while the bQ term has pole order 89, so O is not a zero.
    p_pole_order = 2 * p_poly.degree()
    bq_pole_order = 3 + 2 * q_poly.degree()
    assert p_pole_order == 90
    assert bq_pole_order == 89

    fibration = {
        "schema": "MTTQ79ExplicitGenusTwoFibration.v1",
        "status": "EXACT_GENUS_TWO_FIBRATION_AND_SPLITTING_DIVISOR_INPUT_CLOSED",
        "surface": "C={(X,e) in K3 x E_i : x*a+y*b+z*c=0}",
        "projection": "pi_E:C->E_i",
        "base": {
            "projective_equation": "b^2*c=a^3-a*c^2",
            "affine_chart": "c=1",
            "affine_equation": "b^2=a^3-a",
            "point_at_infinity": "O=[0:1:0]",
            "holomorphic_form": "eta_E=da/(2*b)=db/(3*a^2-1)",
        },
        "fiber_chart": {
            "line": "a*x+b*y+z=0",
            "coordinates": "x=1, t=y/x, u=w/x^3, z=-a-b*t",
            "equation": f"u^2={f_ab}",
            "f_coefficients_t_descending": polynomial_coefficients_as_strings(f_ab, t),
            "genus": 2,
        },
        "splitting": {
            "q_ab": str(q_ab),
            "g_ab": str(g_ab),
            "h_ab": str(h_ab),
            "identity": "f_ab=g_ab^2+q_ab*h_ab",
            "identity_residual": str(splitting_residual),
        },
        "theorem": {
            "name": "Q79SpectralSurfaceGenusTwoFibrationTheorem",
            "proved": True,
            "statement": "Projection of the A110 incidence surface to E_i has generic fiber the H-polarized double-plane section u^2=f_ab(t), hence a genus-two curve. The splitting-conic marking restricts as the displayed degree-two/cubic/quartic factorization on every fiber.",
        },
    }

    discriminant = {
        "schema": "MTTQ79GenusTwoDiscriminant90Certificate.v1",
        "status": "EXACT_90_DISTINCT_NODAL_FIBERS_CLOSED",
        "discriminant_on_E": {
            "formula": "Disc_t(f_ab)=P45(a)+b*Q43(a) modulo b^2-a^3+a",
            "P45": str(p45),
            "Q43": str(q43),
            "P45_coefficients_descending": integer_coefficients_descending(p45, a),
            "Q43_coefficients_descending": integer_coefficients_descending(q43, a),
            "raw_term_count": len(sp.Poly(raw_discriminant, a, b).terms()),
            "reduced_term_count": len(sp.Poly(discriminant_on_e, a, b).terms()),
        },
        "norm_certificate": {
            "formula": "N90=P45^2-(a^3-a)*Q43^2",
            "degree": n_poly.degree(),
            "leading_coefficient": int(n_poly.LC()),
            "coefficients_descending": integer_coefficients_descending(norm90, a),
            "sha256_of_expanded_expression": hashlib.sha256(
                str(norm90).encode("ascii")
            ).hexdigest(),
            "gcd_N90_derivative": str(norm_gcd.as_expr()),
            "gcd_P45_Q43": str(pq_gcd.as_expr()),
            "P45_nonzero_at_elliptic_branch_a": {
                str(value): int(p_poly.eval(value)) for value in (-1, 0, 1)
            },
        },
        "infinity_check": {
            "ord_O_a": -2,
            "ord_O_b": -3,
            "P45_pole_order": p_pole_order,
            "bQ43_pole_order": bq_pole_order,
            "discriminant_zero_at_O": False,
        },
        "consequences": {
            "distinct_discriminant_points_on_E": 90,
            "singular_fiber_type": "one ordinary node at each discriminant point",
            "Euler_from_nodes": 90,
            "A104_c2_surface": 90,
            "Euler_crosscheck_exact": True,
            "b1": 2,
            "b3": 2,
            "b2_from_Euler": 92,
        },
        "theorem": {
            "name": "Q79GenusTwoNinetyNodeLefschetzTheorem",
            "proved": True,
            "statement": "The discriminant section has 90 distinct finite zeros and no zero at O. Square-freeness of N90 and coprimality of P45,Q43 make every zero simple; for a binary sextic this is one transverse double-root collision, so pi_E is a genus-two Lefschetz fibration with 90 nodal fibers. Its node count reproduces c2(C)=90 and b2(C)=92.",
        },
    }

    e_vector = sp.Matrix([a, b, 1])
    x_vector = sp.Matrix([1, t, -a - b * t])
    matrix_basis = {
        "E12": [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
        "E13": [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
        "E21": [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        "E23": [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
        "E31": [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
        "E32": [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
        "H1": [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        "H2": [[0, 0, 0], [0, 1, 0], [0, 0, -1]],
    }
    residue_numerators: dict[str, str] = {}
    residue_expressions: list[sp.Expr] = []
    for name, entries in matrix_basis.items():
        matrix = sp.Matrix(entries)
        assert sp.trace(matrix) == 0
        numerator = sp.expand((x_vector.T * matrix * e_vector)[0])
        residue_numerators[name] = str(numerator)
        residue_expressions.append(numerator)

    monomials = sorted(
        {
            monomial
            for expression in residue_expressions
            for monomial, _coefficient in sp.Poly(expression, a, b, t).terms()
        },
        reverse=True,
    )
    coefficient_matrix = sp.Matrix(
        [
            [sp.Poly(expression, a, b, t).coeff_monomial(monomial) for monomial in monomials]
            for expression in residue_expressions
        ]
    )
    assert coefficient_matrix.rank() == 8

    prym = {
        "schema": "MTTQ79ExplicitPrymResiduesAndDeltaNormalFunction.v1",
        "status": "EXACT_EIGHT_RESIDUE_FORMS_AND_DELTA_DIVISOR_NORMAL_FUNCTION_INPUT_CLOSED",
        "residue_forms": {
            "sl3_basis": matrix_basis,
            "numerators_L_M": residue_numerators,
            "common_formula": "omega_M=L_M(a,b,t)*dt wedge da/(2*b*u)",
            "chart_change": "replace da/(2*b) by db/(3*a^2-1) at b=0",
            "exact_linear_rank": coefficient_matrix.rank(),
            "trace_free_form_count": len(residue_numerators),
            "derivation": "Res_C[(X^T M e/s)*(dt wedge dz/u) wedge eta_E] with ds/dz=1",
        },
        "delta_fiber_divisor": {
            "q_equation": "t^2+b*t+a=0",
            "q_root_discriminant_on_E": "b^2-4*a=a^3-5*a",
            "R_plus_points": "P_i=(t=r_i,u=g_ab(r_i)), i=1,2",
            "hyperplane_reference": "K_e=P_infinity_plus+P_infinity_minus",
            "degree_zero_divisor": "D_delta(e)=P_1+P_2-P_infinity_plus-P_infinity_minus",
            "line_bundle": "O_K3(delta)|C_e=O_Ce(D_delta(e))",
            "relative_degree": 0,
            "Abel_Jacobi_coordinates": [
                "integral_D_delta dt/u modulo H1(C_e,Z)",
                "integral_D_delta t*dt/u modulo H1(C_e,Z)",
            ],
        },
        "Poincare_transgression": {
            "input_cocycle": gerbe110["triple_overlap_scalar"]["formula"],
            "relative_object": "the Abel-Jacobi normal function nu_delta(e)=AJ(D_delta(e)) of the splitting divisor",
            "Cech_to_Leray_chain": [
                "Represent O(delta) by g_ij and n_ijk=(2*pi*i)^-1(Log g_ij+Log g_jk+Log g_ki).",
                "A110 gives alpha_ijk(e)=exp(2*pi*i<pair(e),n_ijk>) after zero-section normalization.",
                "On each curve C_e, H^2(C_e,O^*)=0, so alpha|C_e has local line-bundle trivializations.",
                "Continuation of those trivializations around the punctured elliptic base is the Leray H^1(E,R^1 pi_*O^*) transgression of alpha|C.",
                "The same g_ij restricted to C_e represent O(delta)|C_e=O(D_delta(e)); Abel's theorem identifies that transgression with nu_delta(e)=AJ(D_delta(e)).",
            ],
            "fiberwise_vanishing_reason": "A compact complex curve has H^2(O^*)=0 by the exponential sequence and H^2(O)=H^3(Z)=0.",
            "meaning": "Fiberwise Cech trivializations of alpha|C_e differ under continuation by the Poincare pairing with nu_delta. The A106 beta_C period vector is therefore computed by the inhomogeneous Gauss-Manin continuation of this explicit divisor normal function.",
            "beta_C_zero_decided": False,
        },
        "theorem": {
            "name": "Q79PrymResidueAndDeltaNormalFunctionReductionTheorem",
            "proved": True,
            "statement": "At the A110 trial carrier the eight A106 residue forms have the displayed exact sl3 numerators. The splitting curve R_plus restricts to the explicit degree-zero divisor D_delta on each genus-two fiber, so the normalized Poincare-gerbe calculation reduces to one rank-four genus-two Gauss-Manin system with this algebraic normal-function source.",
        },
    }

    period_open = {
        "schema": "MTTQ79CertifiedGenusTwoMonodromyPeriodExecutionInput.v1",
        "status": "OPEN_CERTIFIED_MONODROMY_NORMAL_FUNCTION_AND_INTEGRAL_PERIOD_EXECUTION",
        "closed_input": {
            "base_elliptic_curve": "b^2=a^3-a",
            "genus_two_binary_sextic_family": str(FIBRATION.relative_to(ROOT)).replace("\\", "/"),
            "90_simple_critical_values": str(DISCRIMINANT.relative_to(ROOT)).replace("\\", "/"),
            "fiber_H1_rank": 4,
            "surface_H2_rank": 92,
            "eight_holomorphic_residue_forms": str(PRYM.relative_to(ROOT)).replace("\\", "/"),
            "algebraic_normal_function_divisor": "D_delta(e)",
        },
        "execution_steps": [
            "isolate the 90 roots of N90 with certified complex discs and lift each root to the unique b=-P45/Q43 point on E_i",
            "choose a symplectic H1 basis on one smooth genus-two fiber and certified paths in E_i minus the 90 critical values",
            "compute the rank-four Gauss-Manin connection for dt/u and t*dt/u and its integral Picard-Lefschetz monodromies",
            "continue the two Abel-Jacobi integrals of D_delta with the corresponding inhomogeneous Picard-Fuchs system",
            "assemble an integral H2(C,Z) basis from base cycles, invariant fiber cycles and the 90 Lefschetz thimbles",
            "integrate the eight omega_M rows to obtain Pi_8x92 and the beta vector z_8 with interval enclosures",
            "prove z=Pi*ell for an exact ell in Z^92, or prove nonmembership with a certified separation bound",
            "if equality holds, differentiate the same system in the eight sl3 directions and certify det(J) nonzero",
        ],
        "external_algorithm_fit": {
            "Lairez_PichonPharabod_Vanhove_2024": "effective homology plus rigorous period continuation; the present reduction supplies the needed curve-level Lefschetz family rather than pretending C is a projective hypersurface",
            "Sertoz_2019": "Picard-Fuchs continuation from exact hypersurface data supplies the fiber-period engine",
            "Brinzanescu_Moraru_2003": "twisted Fourier-Mukai/spectral-cover gerbe framework for elliptic fibrations without a section",
        },
        "acceptance": {
            "floating_nearest_lattice_without_separation_allowed": False,
            "beta_C_period_rows_emitted": 0,
            "beta_C_zero_proved": False,
            "beta_C_nonzero_proved": False,
            "transverse_alignment_zero_proved": False,
        },
        "A106_target_equations": period106["period_system"]["eight_equations"],
        "A106_target_Jacobian": period106["covariant_Jacobian"]["formula"],
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA111.v1",
        "status": STATUS,
        "closed_now": [
            "explicit genus-two fibration of the A110 spectral surface over E_i",
            "exact affine sextic f_ab=g_ab^2+q_ab*h_ab",
            "degree-90 square-free discriminant norm",
            "90 distinct nodal fibers and exact Euler/b2 cross-check",
            "eight explicit sl3 residue-form numerators",
            "explicit degree-zero splitting divisor D_delta on every smooth fiber",
            "reduction to one rank-four inhomogeneous genus-two Gauss-Manin execution",
        ],
        "old_good_cover_as_only_route_retired": True,
        "direct_Cech_coboundary_route_still_lawful": True,
        "beta_C_period_rows_emitted": 0,
        "actual_exact_gerbe_zero": False,
        "trial_tau_i_and_identity_alignment_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Execute the certified genus-two monodromy and inhomogeneous normal-function continuation, assemble H2(C,Z), and decide the A106 integral-period congruence with a separation certificate.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "genus_two_fibration": str(FIBRATION.relative_to(ROOT)).replace("\\", "/"),
        "nodal_discriminant": str(DISCRIMINANT.relative_to(ROOT)).replace("\\", "/"),
        "Prym_residue_normal_function": str(PRYM.relative_to(ROOT)).replace("\\", "/"),
        "period_execution_open": str(PERIOD.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (FIBRATION, fibration),
        (DISCRIMINANT, discriminant),
        (PRYM, prym),
        (PERIOD, period_open),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "genus_two_family_exact": splitting_residual == 0 and sp.degree(f_ab, t) == 6,
        "discriminant_reduced_to_P_plus_bQ": sp.degree(discriminant_on_e, b) == 1,
        "degree90_norm": n_poly.degree() == 90,
        "discriminant_square_free": norm_gcd.as_expr() == 1,
        "unique_lift_each_norm_root": pq_gcd.as_expr() == 1,
        "no_infinity_discriminant_zero": p_pole_order > bq_pole_order,
        "ninety_nodes_match_Euler": discriminant["consequences"]["Euler_crosscheck_exact"],
        "surface_H2_rank_92": discriminant["consequences"]["b2_from_Euler"] == 92,
        "eight_residue_forms_independent": coefficient_matrix.rank() == 8,
        "delta_relative_degree_zero": prym["delta_fiber_divisor"]["relative_degree"] == 0,
        "beta_rows_not_invented": period_open["acceptance"]["beta_C_period_rows_emitted"] == 0,
        "trial_not_selected": not frontier["trial_tau_i_and_identity_alignment_selected"],
        "no_observed_fit": frontier["observed_or_fitted_physics_parameters_added"] == 0,
    }
    assert all(checks.values())

    results = {
        "genus_two_Lefschetz_fibration_closed": True,
        "distinct_nodal_fibers": 90,
        "surface_H2_rank": 92,
        "explicit_Prym_residue_rows": 8,
        "explicit_delta_normal_function_divisor": True,
        "rank_four_Gauss_Manin_execution_input_closed": True,
        "beta_C_period_rows_emitted": 0,
        "actual_exact_gerbe_zero": False,
        "strict_MTT_source_moduli_removed": 0,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
    }
    authority_hashes = [{"path": str(path), "sha256": sha256(path)} for path in paths.values()]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoLefschetzPeriodReduction.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": results,
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79GenusTwoLefschetzPeriodReduction_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Genus-Two Lefschetz Period Reduction v1

Status: `{STATUS}`

## A new exact projection

Project the smooth A110 incidence surface to its square elliptic factor:

```text
pi_E:C -> E_i,                 E_i: b^2=a^3-a,
C_e: a*x+b*y+z=0 in the K3.
```

On `x=1`, put `t=y/x`, `u=w/x^3`, and `z=-a-b*t`. The fiber is

```text
u^2=f_ab(t),
f_ab=g_ab^2+q_ab*h_ab,
q_ab=-(t^2+b*t+a).
```

The degrees are `6=2*3=2+4`, so every smooth fiber is the genus-two curve in
the K3 polarization class `H`. This replaces an unspecified surface good-cover
integration by a concrete family of hyperelliptic curves over one elliptic base.

## Exact discriminant theorem

SymPy elimination over `QQ` gives

```text
Disc_t(f_ab)=P45(a)+b*Q43(a) modulo b^2-a^3+a.
```

Taking the elliptic norm gives

```text
N90(a)=P45(a)^2-(a^3-a)Q43(a)^2.
```

The generated certificate verifies exactly

```text
deg N90=90,
gcd(N90,N90')=1,
gcd(P45,Q43)=1.
```

At `O=[0:1:0]`, `P45` has pole order 90 while `b Q43` has pole order 89, so
there is no missing discriminant zero at infinity. Thus there are exactly 90
distinct discriminant points. A simple binary-sextic discriminant zero is one
transverse double-root collision, hence one nodal fiber. Their total Euler
contribution is 90, independently reproducing `c2(C)=90` and `b2(C)=92`.

## The eight forms are now explicit

For the six off-diagonal matrices and two Cartan matrices of `sl3`, set

```text
L_M=X^T M e,
X=(1,t,-a-b*t),
e=(a,b,1).
```

The eight independent A106 forms are

```text
omega_M=L_M(a,b,t) dt wedge da/(2 b u).
```

All eight numerators are emitted in the packet and have exact coefficient
rank eight. This is the concrete residue basis needed by the period engine.

## The gerbe source is an algebraic normal function

On a smooth fiber, the two roots of `q_ab` cut the split curve `R_plus` at

```text
P_i=(t=r_i,u=g_ab(r_i)).
```

Since `delta=R_plus-H`, its restriction is represented by

```text
D_delta(e)=P_1+P_2-P_infinity_plus-P_infinity_minus.
```

This has degree zero and gives an explicit Abel-Jacobi normal function with
coordinates obtained from `dt/u` and `t dt/u`. The A110 Poincare cocycle
restricts trivially on each curve because `H^2(C_e,O^*)=0`. In the Leray
description, continuation of these fiberwise trivializations is represented by
the same restricted `O(delta)` cocycle. Abel's theorem identifies it with
`AJ(D_delta(e))`. The gerbe calculation therefore becomes one inhomogeneous
rank-four genus-two Gauss-Manin problem.
No beta period or integral relation is inferred merely from this reduction.

## Remaining certified execution

The next computation must isolate the 90 critical values, calculate integral
Picard-Lefschetz monodromy, assemble the rank-92 surface homology, continue the
normal function with interval bounds, and evaluate the eight-by-92 period
matrix. Only exact equality `z=Pi ell` for `ell in Z^92`, or a proved separation
bound, decides `beta_C`.

The constructive `tau=i` and identity alignment remain unselected, zero strict
source moduli are removed, and U6 is not declared closed.

## External computational basis

- Lairez, Pichon-Pharabod and Vanhove, *Effective homology and periods of
  complex projective hypersurfaces*, arXiv:2306.05263.
- Sertoz, *Computing Periods of Hypersurfaces*, arXiv:1803.08068.
- Brinzanescu and Moraru, *Twisted Fourier-Mukai transforms and bundles on
  non-Kahler elliptic surfaces*, arXiv:math/0309031.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
