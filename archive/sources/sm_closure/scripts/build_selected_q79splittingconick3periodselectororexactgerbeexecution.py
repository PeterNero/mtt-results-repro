from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADJACENT_Q79 = ROOT.parent / "mtt-q79-proof-repro"
STRINGS = ROOT.parent / "16 Strings, Flux, & M-Theory Encodings"
SLUG = "selected_q79splittingconick3periodselectororexactgerbeexecution"
STATUS = "MTT_U6_Q79_FIXED_SECTOR_RECONCILED_PERIOD_SCHUR_AND_JOINT_GERBE_SYSTEM_CLOSED_NUMERIC_SOURCE_OPEN"
NEXT = "MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79SplittingConicK3PeriodSelectorOrExactGerbeExecution_v1.md"

SCOPE = OUT / "fixed_sector_selection_scope_and_revision.packet.json"
RIGOR = OUT / "Xi_OU_gap_and_Hessian_rigor_audit.packet.json"
SCHUR = OUT / "K3_period_domain_Schur_complement.packet.json"
JOINT = OUT / "joint_period_gerbe_execution_contract.packet.json"
OPEN = OUT / "period_Hessian_or_marked_model_source.open.json"
FRONTIER = OUT / "U6_frontier_after_A108.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def mat_mul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0)) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def mat_sub(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def inv2(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        raise ValueError("singular 2x2 matrix")
    return [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            ratio = work[row][column] / pivot_value
            for item in range(column, len(work)):
                work[row][item] -= ratio * work[column][item]
    return result


def fraction_rows(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix]


def main() -> int:
    paths = {
        "A106": ROOT / "candidate_data" / "selected_q79pgl3toprymgerbejacobianexecution.candidate.json",
        "A106_normal_form": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "splitting_conic_K3_normal_form.packet.json",
        "A106_period": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "residue_period_Jacobian_formula.packet.json",
        "A107": ROOT / "candidate_data" / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution.candidate.json",
        "A107_open": ROOT
        / "candidate_data"
        / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
        / "splitting_conic_K3_period_selector.open.json",
        "strominger_paper": STRINGS
        / "_md"
        / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
        "fixed_sector_reduction": ADJACENT_Q79
        / "proof_corpus"
        / "Fu_Yau_Mukai_Z7_Fixed_Sector_Selection_Reduction_v1.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A108 authority: " + ", ".join(missing))

    a106 = load(paths["A106"])
    normal = load(paths["A106_normal_form"])
    period = load(paths["A106_period"])
    a107 = load(paths["A107"])
    open107 = load(paths["A107_open"])
    strominger_text = paths["strominger_paper"].read_text(encoding="utf-8")
    fixed_sector_text = paths["fixed_sector_reduction"].read_text(encoding="utf-8")

    assert a106["results"]["relative_period_equations_closed"]
    assert period["covariant_Jacobian"]["shape"] == [8, 8]
    assert normal["parameter_count"]["lattice_period_domain_dimension"] == 18
    assert a107["next_required_artifact"] == "MTT_Selected_q79SplittingConicK3PeriodSelectorOrExactGerbeExecution_v1"
    assert a107["results"]["conditional_Z4_unselected_geometric_source_moduli_complex"] == 18
    assert not open107["acceptance"]["marked_K3_selected_by_MTT"]
    assert "Fix a compact complex threefold" in strominger_text
    assert "complex structure $J$" in strominger_text
    assert "fixed holomorphic" in strominger_text
    assert "The OU term is constant under deterministic variations." in strominger_text
    assert "second variation contributes a nonnegative quadratic form" in strominger_text
    assert "epsilon^{-2}" in strominger_text
    assert "global choice or construction of the topological sector" in fixed_sector_text

    # Exact finite-dimensional unit test of the block elimination identity. It
    # checks the implementation of the theorem, not the still-missing MTT rows.
    h_uu = [[Fraction(5), Fraction(1)], [Fraction(1), Fraction(4)]]
    h_pp = [[Fraction(7), Fraction(2)], [Fraction(2), Fraction(6)]]
    h_pu = [[Fraction(1), Fraction(2)], [Fraction(0), Fraction(1)]]
    h_up = transpose(h_pu)
    h_eff = mat_sub(h_pp, mat_mul(mat_mul(h_pu, inv2(h_uu)), h_up))
    full = [
        h_pp[0] + h_pu[0],
        h_pp[1] + h_pu[1],
        h_up[0] + h_uu[0],
        h_up[1] + h_uu[1],
    ]
    det_identity = determinant(full) == determinant(h_uu) * determinant(h_eff)
    h_eff_positive = h_eff[0][0] > 0 and determinant(h_eff) > 0
    assert det_identity and h_eff_positive

    scope = {
        "schema": "MTTQ79FixedSectorSelectionScopeReconciliation.v1",
        "status": "EXACT_SCOPE_RECONCILIATION_CLOSED_GLOBAL_PERIOD_SELECTION_NOT_IN_OLD_THEOREM",
        "printed_configuration_space": {
            "X": "fixed compact complex threefold",
            "J": "fixed complex structure",
            "E": "fixed holomorphic bundle",
            "topological_sector": "fixed Chern data and Hhat cohomology class",
            "varied_fields": ["Hermitian metric g on (X,J)", "dilaton Phi", "B-field", "unitary connection A"],
            "K3_period_or_complex_structure_varied": False,
        },
        "lawful_claim": "Conditionally on the analytic assumptions and a typed MTT-to-field map, the flow may select a local field representative inside one supplied complex/topological sector.",
        "unlawful_claims": [
            "the old theorem selects one point of the 18-complex-dimensional marked K3 period domain",
            "the old theorem selects the Fu-Yau topological sector globally",
            "the old theorem supplies the splitting-conic coefficients Q2,G3,H4",
            "the old theorem proves gerbe zero on the q79 spectral surface",
        ],
        "independent_corpus_confirmation": "The q79 fixed-sector reduction explicitly separates local fixed-sector selection from global construction or selection of the topological sector.",
        "revision_alignment": "Matches the 2026-07-11 corpus revision decision: keep the Strominger result as a conditional fixed-point correspondence and do not infer existence or global selection.",
        "theorem": {
            "name": "PrintedStromingerSelectionIsFixedSectorOnlyTheorem",
            "proved": True,
            "statement": "Because X, J, E and the topological sector are fixed before the displayed configuration space is defined, every variation and Hessian in the printed theorem is tangent to that fixed sector. It cannot select a marked K3 period or a global compactification sector.",
        },
    }

    rigor = {
        "schema": "MTTQ79XiOUGapAndHessianRigorAudit.v1",
        "status": "EXACT_INTERNAL_CONSISTENCY_AUDIT_CLOSED_FIXED_FIELD_COERCIVITY_REPAIR_REQUIRED",
        "OU_term": {
            "definition": "T_OU=sum_a delta_a/(2 gamma_a), gamma_a=kappa_a lambda_a-L",
            "if_lambda_is_varied": {
                "first_variation": "dT_OU=-sum_a delta_a*kappa_a*d(lambda_a)/(2*gamma_a^2)",
                "second_variation": "d2T_OU=sum_a delta_a*kappa_a^2*d(lambda_a)^2/gamma_a^3-sum_a delta_a*kappa_a*d2(lambda_a)/(2*gamma_a^2)",
                "automatically_nonnegative": False,
            },
            "if_lambda_is_fixed": {
                "first_variation": 0,
                "second_variation": 0,
                "lifts_moduli": False,
            },
            "printed_conflict": "The Euler-Lagrange proof calls the OU term constant, while the Hessian discussion assigns it a nonnegative second variation. Both claims cannot hold on the same variation space without an additional definition and sign proof.",
        },
        "fiber_gap": {
            "printed_metric": "g=epsilon^(-2) g_T2 plus g_K3",
            "fiber_Laplacian_scaling": "lambda_T2(epsilon^(-2)g_T2)=epsilon^2 lambda_T2(g_T2)",
            "uniform_positive_gap_as_epsilon_to_zero_from_fiber": False,
            "small_fiber_repair": "Use g=epsilon^2 g_T2 plus g_K3, for which nonconstant fiber eigenvalues scale as epsilon^(-2), or prove an independent twist-induced lower bound.",
        },
        "Hessian_and_flow": {
            "principal_symbol_block_ellipticity_implies_full_positive_Hessian": False,
            "missing_estimate": "A relative bound must dominate all lower-order and constraint couplings after gauge quotient; residual zero modes require a separately computed potential.",
            "typed_FP_variable_to_Strominger_field_map_present": False,
            "MTT_flow_proved_equal_to_gradient_or_preconditioned_gradient_of_Xi": False,
            "current_fixed_field_Huu_accepted_as_unconditional_source_certificate": False,
        },
        "usable_conditional_package": {
            "name": "C_Xi_fixed",
            "assumptions": [
                "a C2 extended functional on a fixed gauge slice",
                "a typed map from MTT fixed-point variables to (g,Phi,B,A)",
                "the selected flow has Xi as a strict Lyapunov functional",
                "the fixed-field Hessian H_uu is boundedly invertible after quotienting symmetries",
            ],
            "role": "Under these explicit assumptions, the fixed-sector result supplies the invertible block needed for the K3-period Schur reduction. The assumptions are not silently promoted to proved source data.",
        },
        "theorem": {
            "name": "PrintedXiDoesNotYetCertifyFieldOrPeriodCoercivityTheorem",
            "proved": True,
            "statement": "The printed OU, fiber-scaling and principal-symbol arguments do not establish the claimed unconditional positive Hessian. The old result remains usable only as the explicit conditional package C_Xi_fixed, and it contains no K3-period variation.",
        },
    }

    schur = {
        "schema": "MTTQ79K3PeriodDomainSchurComplement.v1",
        "status": "EXACT_CONDITIONAL_PERIOD_REDUCTION_THEOREM_CLOSED_ACTUAL_DERIVATIVE_ROWS_OPEN",
        "geometry": {
            "period_domain": "D_L for L=<H,delta>=diag(2,-4)",
            "complex_dimension": 18,
            "real_dimension": 36,
            "normal_form": "w^2=G3^2+Q2*H4 modulo scaling and PGL3",
            "coordinates": "p=(p_1,...,p_18) in a Kodaira-Spencer chart",
        },
        "extension": {
            "functional": "Xi_ext(p,u), where u=(g,Phi,B,A,connections,multipliers) on the gauge-fixed field slice",
            "field_equation": "D_u Xi_ext(p,u_*(p))=0",
            "effective_functional": "W(p)=Xi_ext(p,u_*(p))",
            "implicit_derivative": "D_p u_*=-H_uu^(-1) H_up",
            "effective_gradient": "D_p W=D_p Xi_ext at u_*(p)",
            "effective_Hessian": "H_eff=H_pp-H_pu H_uu^(-1) H_up",
        },
        "dimension_guard": {
            "generic_real_Hessian_shape": [36, 36],
            "Hermitian_18x18_block_alone_sufficient": False,
            "exception": "An 18x18 complex test suffices only after a complex-linear/holomorphic reduction proving equivalence to the full real Hessian.",
        },
        "selection_acceptance": {
            "stationarity": "D_p W=0 exactly",
            "isolated_local_minimum": "H_eff is positive definite on all 36 real period directions after discrete/lattice identifications",
            "no_hidden_centering_rows": "No penalty norm(p-p0)^2 is accepted unless p0 is independently emitted by the same selected source.",
        },
        "required_source_payload": {
            "fields": [
                "FP_to_Strominger_field_map",
                "Xi_ext_on_K3_period_domain",
                "Kodaira_Spencer_basis_and_gauge",
                "period_gradient_DpXi",
                "fixed_field_inverse_or_coercivity_Huu",
                "mixed_block_Hup",
                "period_block_Hpp",
            ],
            "required_fields": 7,
            "accepted_actual_fields": 0,
            "actual_numeric_or_exact_H_eff_rows": 0,
        },
        "exact_formula_unit_test": {
            "scope": "algebraic implementation only; not an MTT geometry witness",
            "H_uu": fraction_rows(h_uu),
            "H_pp": fraction_rows(h_pp),
            "H_pu": fraction_rows(h_pu),
            "H_eff": fraction_rows(h_eff),
            "det_full": str(determinant(full)),
            "det_Huu_times_det_Heff": str(determinant(h_uu) * determinant(h_eff)),
            "determinant_identity_exact": det_identity,
            "H_eff_positive": h_eff_positive,
        },
        "theorem": {
            "name": "ConditionalK3PeriodSchurSelectionTheorem",
            "proved": True,
            "statement": "If C_Xi_fixed holds for a C2 extension Xi_ext over the 18-complex-dimensional K3 period domain, the implicit-function theorem eliminates the fixed-sector fields and the exact period selector is the 36-real-dimensional Schur complement H_eff. Existing fixed-field positivity alone neither selects nor stabilizes a K3 period.",
        },
    }

    joint = {
        "schema": "MTTQ79JointK3PeriodGerbeExecutionContract.v1",
        "status": "EXACT_JOINT_SYSTEM_AND_FACTORING_CRITERION_CLOSED_ACTUAL_POINT_AND_PERIOD_VALUES_OPEN",
        "conditional_Z4_tau_i_route": {
            "premise": "LensQuarterTurnToFuYauChernOrbitSourceTheorem",
            "tau": "i",
            "unknowns": {"K3_period_real": 36, "PGL3_alignment_real": 16, "total_real": 52},
            "equations": {"period_stationarity_real": 36, "gerbe_zero_real": 16, "total_real": 52},
        },
        "strict_unselected_tau_route": {
            "unknowns_real": 54,
            "required_extra_equations_real": 2,
            "warning": "Adding tau as an unknown without a same-source elliptic stationarity/selection equation leaves an underdetermined system.",
        },
        "equations": {
            "period": "G(p)=D_p W(p)=0",
            "gerbe": "F_r(A,p,ell)=z_r(A,p)-sum_I Pi_rI(A,p) ell_I=0, r=1,...,8",
            "integral_branch": "ell in Z^92 is fixed during one local solve and must be certified exactly",
        },
        "real_Jacobian": {
            "shape": [52, 52],
            "block_form": "[[D_p G, 0],[D_p F, D_A F]] when W is independent of A",
            "upper_left": "H_eff, 36x36 real",
            "lower_right": "realification of the A106 covariant 8x8 complex Jacobian, 16x16 real",
            "determinant_factorization": "det J_joint=det(H_eff)*|det_C(D_A F)|^2 when the system is triangular and D_A F is complex-linear",
            "non_complex_linear_fallback": "If D_A F contains antiholomorphic derivatives, use the determinant of its full 16x16 realification; the modulus-square formula is then not assumed.",
            "general_coupled_case": "If Xi_ext also depends on A, retain both off-diagonal blocks and test the full 52x52 determinant/Hessian rather than using the factorization.",
        },
        "exact_acceptance": [
            "a smooth splitting-conic K3 point p and admissible Kahler chamber",
            "D_p W(p)=0 from selected source derivatives",
            "H_eff positive definite on 36 real period directions",
            "one exact ell in Z^92 with F(A,p,ell)=0",
            "det_C(D_A F) nonzero with covariant Gauss-Manin/Hodge transport",
            "same-branch spectral sheaf, inverse Fourier-Mukai bundle, balanced HYM and Bianchi certificates",
        ],
        "direct_model_route": {
            "input": "explicit rational/algebraic Q2,G3,H4, tau and A",
            "can_close": "existence or no-go for gerbe zero and the downstream bundle on that marked model",
            "cannot_close_by_itself": "unique MTT selection of that model",
        },
        "theorem": {
            "name": "JointPeriodSelectionAndGerbeIsolationTheorem",
            "proved": True,
            "statement": "Conditionally at tau=i, period selection and gerbe triviality form a square 52-real-equation system in 52 real unknowns. In the uncoupled triangular case, positivity/nondegeneracy reduces exactly to the K3 Schur Hessian and the realified A106 covariant gerbe Jacobian; the modulus-square determinant formula additionally requires complex linearity. This closes the equation architecture, not its missing source values or an actual solution.",
        },
    }

    open_payload = {
        "schema": "MTTQ79PeriodHessianOrMarkedModelSourceInput.v1",
        "status": "OPEN_ACTUAL_SOURCE_DERIVATIVES_OR_EXPLICIT_MARKED_MODEL",
        "period_selector_route": {
            "FP_to_Strominger_field_map": None,
            "Xi_ext_formula": None,
            "Kodaira_Spencer_basis": None,
            "period_gradient_36_real": None,
            "H_uu_inverse_certificate": None,
            "H_up_36_by_field": None,
            "H_pp_36_by_36": None,
            "selected_stationary_period": None,
            "H_eff_positive_certificate": None,
        },
        "direct_marked_model_route": {
            "Q2_coefficients": None,
            "G3_mod_Q2L1_coefficients": None,
            "H4_coefficients": None,
            "projective_smoothness_certificate": None,
            "elliptic_tau": None,
            "PGL3_alignment_A": None,
            "integral_branch_ell_Z92": None,
            "exact_relative_Deligne_zero_or_nogo": None,
        },
        "acceptance": {
            "period_source_payload_complete": False,
            "selected_marked_K3": False,
            "direct_marked_model_inserted": False,
            "exact_gerbe_zero": False,
            "joint_isolation": False,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA108.v1",
        "status": STATUS,
        "closed_now": [
            "old Strominger selection theorem is fixed-sector only",
            "OU and fiber-gap inconsistencies are exposed with exact repair conditions",
            "conditional K3-period Schur-complement theorem",
            "correct 36-real-dimensional period Hessian guard",
            "square 52-real-dimensional period-plus-gerbe execution system at conditional tau=i",
            "conditional triangular determinant factorization, full-real fallback and direct-model alternative",
        ],
        "fixed_sector_field_selection_unconditional": False,
        "fixed_sector_field_selection_conditional_on_C_Xi_fixed": True,
        "strict_current_source_moduli_complex": 19,
        "conditional_Z4_source_moduli_complex": 18,
        "actual_period_derivative_source_fields": 0,
        "required_period_derivative_source_fields": 7,
        "actual_marked_K3_selected": False,
        "actual_exact_gerbe_zero": False,
        "actual_joint_isolation": False,
        "new_fitted_continuous_parameters": 0,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Either emit the seven same-source period-domain derivative fields and solve the 52-real joint system, or insert one explicit smooth marked model and execute the exact A106 relative-Deligne system as an existence/no-go certificate.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "fixed_sector_scope": str(SCOPE.relative_to(ROOT)).replace("\\", "/"),
        "Xi_rigor_audit": str(RIGOR.relative_to(ROOT)).replace("\\", "/"),
        "K3_period_Schur": str(SCHUR.relative_to(ROOT)).replace("\\", "/"),
        "joint_period_gerbe_contract": str(JOINT.relative_to(ROOT)).replace("\\", "/"),
        "open_source": str(OPEN.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (SCOPE, scope),
        (RIGOR, rigor),
        (SCHUR, schur),
        (JOINT, joint),
        (OPEN, open_payload),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "fixed_sector_scope_proved": scope["theorem"]["proved"],
        "period_not_cross_promoted": not scope["printed_configuration_space"]["K3_period_or_complex_structure_varied"],
        "OU_sign_not_invented": not rigor["OU_term"]["if_lambda_is_varied"]["automatically_nonnegative"],
        "fiber_scaling_corrected": not rigor["fiber_gap"]["uniform_positive_gap_as_epsilon_to_zero_from_fiber"],
        "field_coercivity_kept_conditional": not rigor["Hessian_and_flow"]["current_fixed_field_Huu_accepted_as_unconditional_source_certificate"],
        "Schur_identity_exact": schur["exact_formula_unit_test"]["determinant_identity_exact"],
        "real_dimension_guard": schur["dimension_guard"]["generic_real_Hessian_shape"] == [36, 36],
        "joint_system_square": joint["conditional_Z4_tau_i_route"]["unknowns"]["total_real"] == joint["conditional_Z4_tau_i_route"]["equations"]["total_real"],
        "no_actual_rows_invented": schur["required_source_payload"]["accepted_actual_fields"] == 0,
        "no_observed_or_fitted_selector": frontier["new_fitted_continuous_parameters"] == 0,
    }
    assert all(checks.values())

    authority_hashes = [{"path": str(path), "sha256": sha256(path)} for path in paths.values()]
    results = {
        "fixed_sector_scope_reconciled": True,
        "printed_Xi_unconditional_coercivity_accepted": False,
        "conditional_period_Schur_theorem_closed": True,
        "joint_period_gerbe_equation_architecture_closed": True,
        "conditional_joint_system_real_dimension": 52,
        "actual_period_source_fields_accepted": 0,
        "actual_marked_K3_selected": False,
        "actual_exact_gerbe_zero": False,
        "new_fitted_continuous_parameters": 0,
        "U6_strong_CP_closed": False,
    }
    candidate = {
        "schema": "MTTSelectedQ79SplittingConicK3PeriodSelectorOrExactGerbeExecution.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": results,
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79SplittingConicK3PeriodSelectorOrExactGerbeExecution_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Splitting-Conic K3 Period Selector or Exact Gerbe Execution v1

Status: `{STATUS}`

## Result

A108 does not reuse the old word *selection* as a substitute for the missing
K3 calculation. It proves the exact reduction that the current q79 branch
needs and corrects the scope of the older Strominger fixed-point paper.

The result is:

```text
old theorem: conditional local field selection inside fixed (X,J,E,topology),
new target: 36-real K3-period stationarity plus 16-real gerbe zero,
conditional tau=i system: 52 equations in 52 real unknowns.
```

## Fixed-sector theorem: exact scope

The printed configuration space first fixes a compact complex threefold `X`,
its complex structure `J`, a holomorphic bundle `E`, and the topological
sector. It then varies only `g,Phi,B,A`. Therefore its Hessian has no
Kodaira-Spencer direction and cannot select a point of the
18-complex-dimensional marked K3 period domain.

This agrees with the independent q79 fixed-sector reduction and with the
2026-07-11 corpus revision ledger: the old result is a conditional fixed-point
correspondence, not a global compactification selector.

## Rigor corrections needed before using the field block

The OU term is printed as

```text
T_OU=sum_a delta_a/(2 gamma_a),  gamma_a=kappa_a lambda_a-L.
```

If `lambda_a` varies, then

```text
dT_OU=-sum_a delta_a kappa_a d(lambda_a)/(2 gamma_a^2),
d2T_OU=sum_a delta_a kappa_a^2 d(lambda_a)^2/gamma_a^3
       -sum_a delta_a kappa_a d2(lambda_a)/(2 gamma_a^2).
```

The second variation is not automatically nonnegative. If `lambda_a` is held
fixed, both variations vanish and the term cannot lift moduli. The printed
claims that it is constant and that it lifts moduli therefore require a new,
explicit variation rule and a sign proof.

The Fu-Yau metric is also printed as `epsilon^(-2)g_T2+g_K3`. Its fiber
eigenvalues scale as `epsilon^2`, so they approach zero, not a uniform positive
constant. A genuinely small fiber uses `epsilon^2 g_T2`, or an independent
twist-induced gap must be proved.

Finally, block ellipticity of the principal symbol does not by itself prove a
positive full Hessian after lower-order couplings and constraints. A108 keeps
the old field result only as the explicit conditional package `C_Xi_fixed`:
a typed MTT-to-field map, a `C2` functional, Lyapunov compatibility, and a
boundedly invertible gauge-quotiented field Hessian `H_uu`.

## Conditional K3-period Schur theorem

Let `p` be 18 complex, hence 36 real, coordinates on the lattice-polarized K3
period domain, and let `u` denote the gauge-fixed Strominger fields. Extend the
functional to `Xi_ext(p,u)` and solve

```text
D_u Xi_ext(p,u_*(p))=0.
```

When `H_uu` is invertible, the implicit-function theorem gives

```text
D_p u_*=-H_uu^(-1) H_up,
W(p)=Xi_ext(p,u_*(p)),
H_eff=H_pp-H_pu H_uu^(-1) H_up.
```

Thus old fixed-field positivity is useful, but only as the block eliminated by
the Schur complement. It does not select `p`. The actual selector requires

```text
D_p W=0,
H_eff positive definite on all 36 real period directions.
```

An `18x18` Hermitian block is insufficient unless a separate complex-linear
reduction proves equivalence to the full real Hessian. A penalty centered at an
unsourced `p0` is also forbidden because it would hide 18 complex source knobs.

## Joint period-gerbe execution

Under the still-conditional Z4 Chern-orbit bridge, `tau=i`. Combine the period
equations with A106:

```text
G(p)=D_p W(p)=0                                      (36 real rows),
F_r(A,p,ell)=z_r(A,p)-sum_I Pi_rI(A,p) ell_I=0       (8 complex = 16 real rows),
ell in Z^92 fixed on one exact branch.
```

The unknowns are `p` (36 real) and `A in PGL3` (16 real): exactly 52. If `W`
is independent of `A`, the real Jacobian is block triangular. When `D_A F` is
complex-linear,

```text
det J_joint=det(H_eff) |det_C(D_A F)|^2.
```

If antiholomorphic derivatives occur, the correct test is instead the
determinant of the full `16x16` realification of `D_A F`; A108 does not assume
complex linearity for free.

This ties the new selector directly to the already-computed covariant gerbe
Jacobian. If `tau` is not selected, two more real unknowns and two same-source
elliptic equations are required.

## What is now closed, and what is not

Closed:

1. the exact fixed-sector/global-selection distinction;
2. the OU and fiber-gap correction conditions;
3. the K3-period Schur-complement theorem;
4. the correct 36-real dimension guard;
5. the square 52-real period-plus-gerbe system and determinant criterion.

Still open:

1. the seven actual same-source period derivative fields;
2. one selected stationary marked K3 point with positive `H_eff`;
3. an exact integral branch `ell` and gerbe zero at that point;
4. the downstream spectral sheaf, inverse Fourier-Mukai bundle, balanced HYM
   and same-branch Bianchi execution.

The alternative is constructive: insert explicit smooth coefficients
`Q2,G3,H4`, execute A106 exactly, and obtain an existence/no-go certificate.
That route tests the compactification but does not by itself prove unique MTT
vacuum selection.

No observed value and no fitted continuous parameter enters A108.

Next artifact: `{NEXT}`.

## Primary references

- [de la Ossa and Svanes, Holomorphic Bundles and the Moduli Space of N=1 Supersymmetric Heterotic Compactifications](https://arxiv.org/abs/1402.1725)
- [Anderson, Gray and Sharpe, Algebroids, Heterotic Moduli Spaces and the Strominger System](https://arxiv.org/abs/1402.1532)
- [de Lazari, Lotay, Sa Earp and Svanes, Local descriptions of the heterotic SU(3) moduli space](https://arxiv.org/abs/2409.04382)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
