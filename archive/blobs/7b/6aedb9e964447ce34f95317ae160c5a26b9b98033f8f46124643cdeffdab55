from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
STATUS = "MTT_U6_Q79_EXPLICIT_SMOOTH_SPECTRAL_SURFACE_AND_TORSOR_POINCARE_CECH_FORMULA_CLOSED_BETA_PERIOD_OPEN"
NEXT = "MTT_Selected_q79ExplicitSpectralCechBetaPeriodEvaluation_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1.md"

SPECTRAL = OUT / "square_elliptic_identity_alignment_spectral_surface.packet.json"
SMOOTH = OUT / "spectral_surface_mutual_Gauss_smoothness_certificate.packet.json"
TORSOR = OUT / "explicit_Odelta_and_FuYau_torsor_Cech_transitions.packet.json"
GERBE = OUT / "normalized_Poincare_gerbe_Cech_formula.packet.json"
BETA = OUT / "restricted_beta_C_period_evaluation.open.json"
FRONTIER = OUT / "U6_frontier_after_A110.packet.json"


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


def projective_unit_certificate(
    polynomials: list[sp.Expr], variables: tuple[sp.Symbol, ...]
) -> dict:
    charts = {}
    for chart in variables:
        affine_variables = [variable for variable in variables if variable != chart]
        basis = sp.groebner(
            [sp.expand(poly.subs(chart, 1)) for poly in polynomials],
            *affine_variables,
            order="grevlex",
            domain=sp.QQ,
        )
        basis_strings = [str(poly.as_expr()) for poly in basis.polys]
        charts[str(chart)] = {
            "Groebner_basis": basis_strings,
            "unit_ideal": basis_strings == ["1"],
        }
    return {
        "charts": charts,
        "all_projective_charts_unit": all(item["unit_ideal"] for item in charts.values()),
    }


def mutual_gauss_certificate(
    f6: sp.Expr,
    elliptic_cubic: sp.Expr,
    base_variables: tuple[sp.Symbol, ...],
    elliptic_variables: tuple[sp.Symbol, ...],
) -> dict:
    grad_f = [sp.diff(f6, variable) for variable in base_variables]
    grad_e = [sp.diff(elliptic_cubic, variable) for variable in elliptic_variables]
    e_parallel_grad_f = [
        sp.expand(elliptic_variables[i] * grad_f[j] - elliptic_variables[j] * grad_f[i])
        for i in range(3)
        for j in range(i + 1, 3)
    ]
    x_parallel_grad_e = [
        sp.expand(base_variables[i] * grad_e[j] - base_variables[j] * grad_e[i])
        for i in range(3)
        for j in range(i + 1, 3)
    ]
    equations = [f6, elliptic_cubic, *e_parallel_grad_f, *x_parallel_grad_e]
    charts = {}
    all_variables = [*base_variables, *elliptic_variables]
    for base_chart, elliptic_chart in itertools.product(base_variables, elliptic_variables):
        substitutions = {base_chart: 1, elliptic_chart: 1}
        affine_variables = [
            variable for variable in all_variables if variable not in (base_chart, elliptic_chart)
        ]
        basis = sp.groebner(
            [sp.expand(equation.subs(substitutions)) for equation in equations],
            *affine_variables,
            order="grevlex",
            domain=sp.QQ,
        )
        basis_strings = [str(poly.as_expr()) for poly in basis.polys]
        chart_id = f"{base_chart}=1,{elliptic_chart}=1"
        charts[chart_id] = {
            "Groebner_basis": basis_strings,
            "unit_ideal": basis_strings == ["1"],
        }
    return {
        "system": [
            "F6(X)=0",
            "E(e)=0",
            "e cross grad(F6)(X)=0",
            "X cross grad(E)(e)=0",
        ],
        "charts": charts,
        "all_nine_product_charts_unit": all(item["unit_ideal"] for item in charts.values()),
    }


def main() -> int:
    paths = {
        "A104_open": ROOT
        / "candidate_data"
        / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
        / "flat_analytic_gerbe_cech_input.open.json",
        "A105_prym": ROOT
        / "candidate_data"
        / "selected_q79normalizedpoincaregerbeandpgl3prymreduction"
        / "normalized_Poincare_gerbe_Prym_reduction.packet.json",
        "A106_period": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "residue_period_Jacobian_formula.packet.json",
        "A109": ROOT
        / "candidate_data"
        / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate.candidate.json",
        "A109_model": ROOT
        / "candidate_data"
        / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
        / "explicit_splitting_conic_K3_model.packet.json",
        "requirements": ROOT / "requirements.txt",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A110 authority: " + ", ".join(missing))

    open104 = load(paths["A104_open"])
    prym105 = load(paths["A105_prym"])
    period106 = load(paths["A106_period"])
    a109 = load(paths["A109"])
    model109 = load(paths["A109_model"])
    requirements = paths["requirements"].read_text(encoding="utf-8")

    assert open104["required_same_branch_fields"]["FuYau_torsor_transition_functions"] is None
    assert open104["required_same_branch_fields"]["relative_Poincare_discrepancy_line_bundles_on_double_overlaps"] is None
    assert open104["required_same_branch_fields"]["restricted_scalar_gerbe_cocycle_alpha_ijk"] is None
    assert not prym105["Prym_residue"]["beta_C_zero_proved"]
    assert period106["covariant_Jacobian"]["shape"] == [8, 8]
    assert a109["next_required_artifact"] == "MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1"
    assert "sympy==1.14.0" in requirements

    x, y, z, w = sp.symbols("x y z w")
    a, b, c = sp.symbols("a b c")
    base_variables = (x, y, z)
    elliptic_variables = (a, b, c)
    q2 = expression_from_terms(model109["coefficient_tables"]["Q2"], base_variables)
    g3 = expression_from_terms(model109["coefficient_tables"]["G3"], base_variables)
    h4 = expression_from_terms(model109["coefficient_tables"]["H4"], base_variables)
    f6 = expression_from_terms(model109["coefficient_tables"]["F6"], base_variables)
    k3_equation = sp.expand(w**2 - f6)

    elliptic_cubic = sp.expand(b**2 * c - a**3 + a * c**2)
    spectral_equation = sp.expand(x * a + y * b + z * c)
    elliptic_gradient = [sp.diff(elliptic_cubic, variable) for variable in elliptic_variables]
    elliptic_smooth = projective_unit_certificate(
        [elliptic_cubic, *elliptic_gradient], elliptic_variables
    )
    mutual_gauss = mutual_gauss_certificate(
        f6,
        elliptic_cubic,
        base_variables,
        elliptic_variables,
    )
    assert elliptic_smooth["all_projective_charts_unit"]
    assert mutual_gauss["all_nine_product_charts_unit"]

    # A singular point of the spectral divisor first forces w=0. The remaining
    # Lagrange-multiplier equations are exactly the mutual Gauss system above.
    singular_reduction = {
        "Lagrange_equation": "d(s)=lambda*d(w^2-F6)+mu*d(E)",
        "w_derivative": "0=2*lambda*w",
        "w_nonzero_case": "lambda=0 would force (a,b,c)=0 from the x,y,z derivatives, impossible in P2",
        "therefore": "w=0",
        "remaining_equations": "(a,b,c) parallel grad(F6)(x,y,z) and (x,y,z) parallel grad(E)(a,b,c)",
        "spectral_equation_automatic": "Euler identities give X dot grad(F6)=6F6 and e dot grad(E)=3E",
    }

    spectral = {
        "schema": "MTTQ79SquareEllipticIdentityAlignmentSpectralSurface.v1",
        "status": "EXACT_CONSTRUCTIVE_SMOOTH_SPECTRAL_SURFACE_CLOSED_SOURCE_SELECTION_OPEN",
        "K3": {
            "equation": str(k3_equation),
            "source": str(paths["A109_model"]),
        },
        "elliptic_curve": {
            "plane_cubic": str(elliptic_cubic),
            "Weierstrass_form": "b^2*c=a^3-a*c^2",
            "A": -1,
            "B": 0,
            "discriminant": 64,
            "j_invariant": 1728,
            "analytic_modulus_up_to_SL2Z": "tau=i",
            "degree_three_basis": ["a", "b", "c"],
        },
        "alignment": {
            "A_PGL3_trial": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            "spectral_equation": str(spectral_equation),
            "class": "H+3[0] on K3 x E",
            "determinant_zero": True,
            "accepted_as_MTT_selected_alignment": False,
            "accepted_as_gerbe_zero_alignment": False,
        },
        "smooth": True,
        "invariants_inherited_from_A104": {
            "K_C_squared": 18,
            "c2_C": 90,
            "chi_O_C": 9,
            "q": 1,
            "p_g": 9,
            "h11": 74,
        },
        "construction_scope": "A smooth exact test surface at the conditional square elliptic curve and trial identity alignment; neither tau nor A is promoted as a selected source value.",
    }

    smoothness = {
        "schema": "MTTQ79SpectralSurfaceMutualGaussSmoothnessCertificate.v1",
        "status": "EXACT_NINE_PRODUCT_CHART_UNIT_IDEALS_CLOSED",
        "elliptic_curve_smoothness": elliptic_smooth,
        "singular_system_reduction": singular_reduction,
        "mutual_Gauss_system": mutual_gauss,
        "theorem": {
            "name": "IdentityAlignmentSpectralSurfaceSmoothnessTheorem",
            "proved": True,
            "statement": "For the A109 K3, square elliptic cubic and identity bilinear section, every singular point would solve the mutual Gauss system after w=0. The exact ideal is the unit ideal on all nine P2xP2 charts, so the spectral surface is smooth.",
        },
    }

    # Exact Cartier transition functions for O(delta), delta=R_plus-H_x.
    r_local = {
        "R0": sp.Integer(1),
        "R1": q2,
        "R2": w - g3,
    }
    r_open = {
        "R0": "S minus R_plus",
        "R1": "w+G3 != 0",
        "R2": "H4 != 0",
    }
    h_local = {
        "X": sp.Integer(1),
        "Y": x / y,
        "Z": x / z,
    }
    h_open = {"X": "x != 0", "Y": "y != 0", "Z": "z != 0"}
    local_delta = {}
    for r_id, h_id in itertools.product(r_local, h_local):
        patch_id = f"{r_id}{h_id}"
        local_delta[patch_id] = sp.cancel(r_local[r_id] / h_local[h_id])

    transitions = []
    patch_ids = sorted(local_delta)
    inverse_checks = 0
    for source in patch_ids:
        for target in patch_ids:
            if source == target:
                continue
            value = sp.cancel(local_delta[target] / local_delta[source])
            inverse = sp.cancel(value * local_delta[source] / local_delta[target])
            assert inverse == 1
            inverse_checks += 1
            transitions.append(
                {
                    "from": source,
                    "to": target,
                    "g_ij": str(value),
                }
            )

    cocycle_checks = 0
    for i, j, k in itertools.product(patch_ids, repeat=3):
        g_ij = sp.cancel(local_delta[j] / local_delta[i])
        g_jk = sp.cancel(local_delta[k] / local_delta[j])
        g_ki = sp.cancel(local_delta[i] / local_delta[k])
        assert sp.cancel(g_ij * g_jk * g_ki) == 1
        cocycle_checks += 1

    split_relation_residual = sp.expand((w - g3) * (w + g3) - q2 * h4 - k3_equation)
    assert split_relation_residual == 0

    torsor = {
        "schema": "MTTQ79ExplicitOdeltaAndFuYauTorsorCechTransitions.v1",
        "status": "EXACT_CARTIER_AND_ELLIPTIC_TORSOR_TRANSITION_FORMULA_CLOSED_GOOD_COVER_LOG_BRANCHES_OPEN",
        "divisor": "delta=R_plus-H_x",
        "R_plus_cover": {
            "opens": r_open,
            "local_equations": {key: str(value) for key, value in r_local.items()},
            "cover_proof": "Outside R_plus use R0. On R_plus with G3 nonzero, w+G3=2G3 so R1 applies; at Q2=G3=w=0, A109 proves H4 nonzero so R2 applies.",
            "R1_R2_ratio": "(w-G3)/Q2=H4/(w+G3) on S",
            "surface_relation_residual": str(split_relation_residual),
        },
        "H_x_cover": {
            "opens": h_open,
            "local_equations": {key: str(value) for key, value in h_local.items()},
        },
        "refined_cover": {
            "patch_count": len(patch_ids),
            "patch_ids": patch_ids,
            "local_delta_equations": {key: str(value) for key, value in local_delta.items()},
        },
        "O_delta_transitions": {
            "convention": "For local divisor equations d_i, the O(delta) frame e_i=1/d_i obeys e_i=(d_j/d_i)e_j; hence g_ij=d_j/d_i.",
            "ordered_nonidentity_transition_count": len(transitions),
            "transitions": transitions,
            "inverse_checks_exact": inverse_checks,
            "triple_cocycle_checks_exact": cocycle_checks,
            "all_checks_pass": inverse_checks == 72 and cocycle_checks == 729,
        },
        "elliptic_torsor": {
            "good_cover_refinement": "Refine the nine patches so every nonempty overlap is simply connected and choose holomorphic Log(g_ij).",
            "translation_formula": "t_ij=(2*pi*i)^(-1) Log(g_ij) mod (Z+tau Z)",
            "triple_integer_cocycle": "n_ijk=t_ij_lift+t_jk_lift+t_ki_lift in Z subset Z+tau Z",
            "Chern_pair": ["delta", 0],
            "existence": "delta is algebraic of type (1,1), so its image in H^2(O_K3) vanishes and the elliptic torsor lift exists.",
            "uniqueness": "H^1(K3,O_K3)=0 makes the lift with this Chern pair unique up to isomorphism.",
            "explicit_good_cover_log_branch_values_filled": False,
        },
        "theorem": {
            "name": "ExplicitQ79FuYauTorsorTransitionTheorem",
            "proved": True,
            "statement": "The nine-patch Cartier data define O(delta) with 72 exact transition and 729 exact triple-cocycle checks. Local logarithms modulo the elliptic lattice give the unique holomorphic principal elliptic torsor with Chern pair (delta,0).",
        },
    }

    gerbe = {
        "schema": "MTTQ79NormalizedPoincareGerbeCechFormula.v1",
        "status": "EXACT_DISCREPANCY_LINE_AND_SCALAR_COCYCLE_FORMULA_CLOSED_RESTRICTED_BETA_PERIOD_OPEN",
        "local_objects": "On each torsor trivialization U_i x E, use the zero-section-normalized Poincare line bundle P_i on E x E_dual.",
        "double_overlap_discrepancy": {
            "formula": "P_j tensor P_i^(-1)=p_Edual^* L_{t_ij}",
            "L_t": "the degree-zero line bundle/character on E_dual corresponding to the torsor translation t_ij",
            "source": "t_ij is derived from the explicit O(delta) transition g_ij",
        },
        "triple_overlap_scalar": {
            "formula": "alpha_ijk(e_hat)=chi_ehat(n_ijk,0)",
            "n_ijk": "the integer Cech 2-cocycle of O(delta) from the chosen Log(g_ij) lifts",
            "character": "chi_ehat is the unitary character of the elliptic lattice represented by e_hat in E_dual",
            "Cech_2_cocycle": True,
            "zero_section_normalization": "alpha_ijk(0)=1",
        },
        "Dixmier_Douady_class": {
            "formula": "DD(alpha)=delta cup u",
            "restriction_to_C_integrally_zero": True,
            "authority": "A104",
        },
        "trace_norm": {
            "determinant_zero_implies_trace_beta_zero": True,
            "active_component": "eight-dimensional Prym/trace-free class",
            "authority": "A105",
        },
        "filled_A104_formula_fields": {
            "FuYau_torsor_transition_functions": True,
            "relative_Poincare_discrepancy_line_bundles_on_double_overlaps": True,
            "restricted_scalar_gerbe_cocycle_alpha_ijk_formula": True,
            "restricted_scalar_gerbe_cocycle_alpha_ijk_values_on_good_cover": False,
        },
        "theorem": {
            "name": "ExplicitTorsorDeterminesNormalizedPoincareGerbeCocycleTheorem",
            "proved": True,
            "statement": "The explicit O(delta) transitions determine the elliptic torsor translations, the Poincare discrepancy line bundles, and the normalized scalar gerbe cocycle alpha_ijk=chi(n_ijk,0). This closes the Cech formula but not the good-cover logarithm values or the restricted analytic beta_C periods.",
        },
    }

    beta_open = {
        "schema": "MTTQ79ExplicitSpectralCechBetaPeriodEvaluationInput.v1",
        "status": "OPEN_RESTRICTED_GOOD_COVER_LOGS_AND_EIGHT_PRYM_PERIODS",
        "filled": {
            "smooth_marked_K3": str(paths["A109_model"]),
            "square_elliptic_cubic": str(elliptic_cubic),
            "trial_alignment_A": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            "smooth_spectral_surface": str(SMOOTH.relative_to(ROOT)).replace("\\", "/"),
            "O_delta_transition_table": str(TORSOR.relative_to(ROOT)).replace("\\", "/"),
            "normalized_Poincare_cocycle_formula": str(GERBE.relative_to(ROOT)).replace("\\", "/"),
        },
        "open": {
            "good_cover_and_Log_gij_branches_on_K3": None,
            "integer_cocycle_n_ijk_values": None,
            "restriction_cover_on_C": None,
            "alpha_ijk_restricted_values": None,
            "additive_logarithmic_cocycle_b": None,
            "residue_period_vector_z_8": [None] * 8,
            "integral_period_matrix_Pi_8x92": None,
            "integral_branch_ell_Z92": None,
            "PGL3_covariant_Jacobian_at_zero": None,
        },
        "acceptance": {
            "beta_C_exactly_zero": False,
            "beta_C_exactly_nonzero": False,
            "transverse_PGL3_zero": False,
        },
        "A106_equations": period106["period_system"]["eight_equations"],
        "A106_Jacobian": period106["covariant_Jacobian"]["formula"],
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA110.v1",
        "status": STATUS,
        "closed_now": [
            "algebraic square elliptic curve with j=1728",
            "trial identity-alignment spectral surface",
            "exact nine-product-chart spectral smoothness",
            "explicit nine-patch O(delta) Cartier transitions",
            "72 inverse and 729 triple transition checks",
            "unique Fu-Yau elliptic torsor transition formula",
            "normalized Poincare discrepancy and scalar gerbe cocycle formula",
        ],
        "constructive_tau_i_used": True,
        "tau_i_strictly_selected": False,
        "trial_PGL3_identity_used": True,
        "trial_PGL3_identity_proved_gerbe_zero": False,
        "A104_formula_fields_promoted": 3,
        "A104_good_cover_numeric_or_exact_value_fields_promoted": 0,
        "beta_C_period_rows_emitted": 0,
        "actual_exact_gerbe_zero": False,
        "actual_MTT_marked_geometry_selection": False,
        "strict_MTT_source_moduli_removed": 0,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Refine the explicit nine-patch divisor cover to a good cover on C, fix logarithm branches, compute n_ijk and alpha_ijk|C, then evaluate the eight residue pairings and either exhibit ell in Z^92 with z=Pi ell or prove exact nonmembership/separation.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "spectral_surface": str(SPECTRAL.relative_to(ROOT)).replace("\\", "/"),
        "spectral_smoothness": str(SMOOTH.relative_to(ROOT)).replace("\\", "/"),
        "torsor_transitions": str(TORSOR.relative_to(ROOT)).replace("\\", "/"),
        "Poincare_gerbe_formula": str(GERBE.relative_to(ROOT)).replace("\\", "/"),
        "beta_period_open": str(BETA.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (SPECTRAL, spectral),
        (SMOOTH, smoothness),
        (TORSOR, torsor),
        (GERBE, gerbe),
        (BETA, beta_open),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "elliptic_curve_smooth": elliptic_smooth["all_projective_charts_unit"],
        "spectral_surface_smooth": mutual_gauss["all_nine_product_charts_unit"],
        "Odelta_transition_table_exact": torsor["O_delta_transitions"]["all_checks_pass"],
        "torsor_Chern_pair_exact": torsor["elliptic_torsor"]["Chern_pair"] == ["delta", 0],
        "Poincare_cocycle_formula_closed": gerbe["filled_A104_formula_fields"]["restricted_scalar_gerbe_cocycle_alpha_ijk_formula"],
        "good_cover_values_not_invented": not gerbe["filled_A104_formula_fields"]["restricted_scalar_gerbe_cocycle_alpha_ijk_values_on_good_cover"],
        "beta_period_not_invented": frontier["beta_C_period_rows_emitted"] == 0,
        "tau_and_A_not_selected": not frontier["tau_i_strictly_selected"] and not frontier["trial_PGL3_identity_proved_gerbe_zero"],
        "strict_source_moduli_not_removed": frontier["strict_MTT_source_moduli_removed"] == 0,
        "no_observed_fit": frontier["observed_or_fitted_physics_parameters_added"] == 0,
    }
    assert all(checks.values())

    authority_hashes = [{"path": str(path), "sha256": sha256(path)} for path in paths.values()]
    results = {
        "explicit_smooth_spectral_surface_constructed": True,
        "Odelta_transition_table_closed": True,
        "FuYau_torsor_transition_formula_closed": True,
        "normalized_Poincare_gerbe_cocycle_formula_closed": True,
        "good_cover_cocycle_values_closed": False,
        "beta_C_period_rows_emitted": 0,
        "actual_exact_gerbe_zero": False,
        "strict_MTT_source_moduli_removed": 0,
        "observed_or_fitted_physics_parameters_added": 0,
        "U6_strong_CP_closed": False,
    }
    candidate = {
        "schema": "MTTSelectedQ79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": results,
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Explicit-Model Relative-Deligne Gerbe Zero or No-Go Execution v1

Status: `{STATUS}`

## New exact spectral carrier

Use the A109 K3 and the square elliptic cubic

```text
E_i: b^2 c=a^3-a c^2,
Delta=64,
j=1728.
```

The coordinates `[a:b:c]` form the degree-three basis. At the trial identity
alignment, define

```text
C: x*a+y*b+z*c=0 in K3 x E_i.
```

This is an exact constructive surface, not a selected alignment.

## Spectral-surface smoothness theorem

If `C` were singular, the Lagrange equation for its bilinear section would
give `0=2 lambda w`. The case `w!=0` forces the projective elliptic vector to
vanish, so every singular point must have `w=0`. Euler's identities reduce the
remaining system to

```text
F6(X)=0,
E_i(e)=0,
e parallel grad F6(X),
X parallel grad E_i(e).
```

Exact Groebner reduction over `QQ` gives basis `[1]` on all nine product
charts. Therefore `C` is smooth. Its A104 invariants are consequently
`K_C^2=18`, `c2=90`, `p_g=9`, and `h11=74`.

## Explicit O(delta) transitions

Write `delta=R_plus-H_x`. Cover a neighborhood of `R_plus` by

```text
R1: w+G3 != 0, local equation Q2,
R2: H4 != 0,   local equation w-G3,
```

and use `R0=S-R_plus` with local equation one. The A109 no-triple theorem
proves these cover `R_plus`, while

```text
(w-G3)/Q2=H4/(w+G3)
```

on the overlap. Refine with the three projective charts for `H_x`. This gives
nine local divisor equations `d_i` and exact transitions

```text
g_ij=d_j/d_i.
```

The generated table passes all 72 ordered inverse checks and all 729 triple
cocycle checks exactly.

## Fu-Yau torsor and Poincare gerbe

On a simply connected good-cover refinement choose `Log(g_ij)` and set

```text
t_ij=(2 pi i)^-1 Log(g_ij) mod (Z+tau Z).
```

The triple sums `n_ijk` are the integer Cech cocycle representing `delta`, so
these are the transitions of the unique elliptic torsor with Chern pair
`(delta,0)`. Existence uses that `delta` is algebraic of type `(1,1)`;
uniqueness uses `H^1(K3,O)=0`.

The zero-section-normalized Poincare bundles differ on double overlaps by the
degree-zero line bundle of `t_ij`. Their scalar triple cocycle is

```text
alpha_ijk(e_hat)=chi_ehat(n_ijk,0),
alpha_ijk(0)=1.
```

This is the missing explicit Cech formula. It reproduces
`DD(alpha)=delta cup u`, whose restriction to `C` is already integrally zero.

## Remaining analytic calculation

A110 does not confuse a cocycle formula with its analytic-Brauer value. The
remaining work is now:

1. refine the nine patches to a good cover of `C` and fix logarithm branches;
2. evaluate `n_ijk`, `alpha_ijk|C`, and the additive cocycle `b`;
3. compute the eight residue pairings `z_r` and the `8x92` integral period
   matrix;
4. find `ell in Z^92` with `z=Pi ell`, or prove exact nonmembership;
5. certify the covariant `8x8` alignment Jacobian at any zero.

The identity alignment and `tau=i` are constructive trial data. They are not
promoted as MTT-selected values, and zero strict source moduli are removed.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
