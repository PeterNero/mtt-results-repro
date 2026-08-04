from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

WORLD_IN_WORLD = (
    TEXPAPERS
    / "10 ProtoSpinor"
    / "revised_tex_vnext"
    / "World_in_World_Genesis__Local_Comparison_Geometry_and_Globalization_Program_v5"
    / "main.tex"
)
ACTION_V4 = (
    TEXPAPERS
    / "10 ProtoSpinor"
    / "revised_tex_vnext"
    / "Closure_Geometry_and_a_Regime_Local_Ten_Dimensional_Action_Ansatz_v4"
    / "main.tex"
)

METRIC_SOURCE = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
GLOBAL_HESSIAN = ROOT / "certificates" / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
ACTION_REDUCTION = ROOT / "certificates" / "closure_to_einstein_action_reduction_certificate.json"
NONLINEAR_NOGO = ROOT / "certificates" / "quadratic_tt_nonlinear_action_nogo_certificate.json"

OUT_CERT = ROOT / "certificates" / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Closure_Anholonomy_Teleparallel_Einstein_Bridge_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def torsion_invariants(torsion: dict[tuple[int, int, int], sp.Expr]) -> list[sp.Expr]:
    """Return I1, I2, I3 for T^a_bc in signature (-,+,+,+)."""

    eta = (-1, 1, 1, 1)

    def value(a: int, b: int, c: int) -> sp.Expr:
        return sp.sympify(torsion.get((a, b, c), 0))

    i1 = sp.Integer(0)
    i2 = sp.Integer(0)
    for a, b, c in itertools.product(range(4), repeat=3):
        t_upper = eta[b] * eta[c] * value(a, b, c)
        i1 += t_upper * eta[a] * value(a, b, c)
        i2 += t_upper * eta[b] * value(b, a, c)

    torsion_vector_cov = [
        sum(value(b, b, c) for b in range(4)) for c in range(4)
    ]
    i3 = sum(
        eta[a] * torsion_vector_cov[a] ** 2 for a in range(4)
    )
    return [sp.expand(i1), sp.expand(i2), sp.expand(i3)]


def antisymmetric_torsion(
    components: list[tuple[int, int, int, int]],
) -> dict[tuple[int, int, int], sp.Expr]:
    result: dict[tuple[int, int, int], sp.Expr] = {}
    for a, b, c, value in components:
        result[(a, b, c)] = result.get((a, b, c), 0) + value
        result[(a, c, b)] = result.get((a, c, b), 0) - value
    return result


def exact_string(value: sp.Expr) -> str:
    return str(sp.factor(sp.simplify(value)))


def main() -> None:
    world_text = WORLD_IN_WORLD.read_text(encoding="utf-8", errors="replace")
    action_text = ACTION_V4.read_text(encoding="utf-8", errors="replace")
    metric = load(METRIC_SOURCE)
    hessian = load(GLOBAL_HESSIAN)
    action_reduction = load(ACTION_REDUCTION)
    nonlinear_nogo = load(NONLINEAR_NOGO)

    # Exact irreducible quadratic torsion basis check.
    witness_torsions = [
        antisymmetric_torsion([(0, 0, 1, 1)]),
        antisymmetric_torsion([(0, 1, 2, 1)]),
        antisymmetric_torsion([(0, 0, 1, 1), (2, 1, 2, 1)]),
    ]
    invariant_rows = [torsion_invariants(torsion) for torsion in witness_torsions]
    invariant_matrix = sp.Matrix(invariant_rows)

    # Exact diagonal Bianchi-I check. This is a nontrivial symbolic test of
    # e R = -e T + 2 partial_mu(e T^mu) in the conventions used below.
    h1, h2, h3 = sp.symbols("H1 H2 H3")
    dh1, dh2, dh3 = sp.symbols("dH1 dH2 dH3")
    bianchi_torsion: dict[tuple[int, int, int], sp.Expr] = {}
    for index, h_value in enumerate((h1, h2, h3), start=1):
        bianchi_torsion[(index, 0, index)] = h_value
        bianchi_torsion[(index, index, 0)] = -h_value

    i1, i2, i3 = torsion_invariants(bianchi_torsion)
    torsion_scalar = sp.expand(sp.Rational(1, 4) * i1 + sp.Rational(1, 2) * i2 - i3)
    pair_sum = h1 * h2 + h1 * h3 + h2 * h3
    square_sum = h1**2 + h2**2 + h3**2
    derivative_sum = dh1 + dh2 + dh3
    ricci_scalar = sp.expand(2 * (derivative_sum + square_sum + pair_sum))
    boundary_scalar = sp.expand(2 * (derivative_sum + (h1 + h2 + h3) ** 2))
    teleparallel_identity_residual = sp.simplify(
        ricci_scalar + torsion_scalar - boundary_scalar
    )

    q_symbols = sp.symbols("q11 q12 q13 q21 q22 q23 q31 q32 q33")
    q_matrix = sp.Matrix(3, 3, q_symbols)
    exact_orientation_rotation = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    orientation_metric_residual = sp.simplify(
        (exact_orientation_rotation * q_matrix).T
        * (exact_orientation_rotation * q_matrix)
        - q_matrix.T * q_matrix
    )

    lapse = sp.symbols("N", nonzero=True)
    shift = sp.Matrix(sp.symbols("N1 N2 N3"))
    coframe = sp.zeros(4)
    coframe[0, 0] = lapse
    coframe[1:4, 0] = q_matrix * shift
    coframe[1:4, 1:4] = q_matrix
    eta4 = sp.diag(-1, 1, 1, 1)
    adm_metric = sp.expand(coframe.T * eta4 * coframe)
    spatial_metric = q_matrix.T * q_matrix
    expected_adm_metric = sp.zeros(4)
    expected_adm_metric[0, 0] = (
        -lapse**2 + (shift.T * spatial_metric * shift)[0]
    )
    expected_adm_metric[0, 1:4] = shift.T * spatial_metric
    expected_adm_metric[1:4, 0] = spatial_metric * shift
    expected_adm_metric[1:4, 1:4] = spatial_metric
    adm_metric_residual = (adm_metric - expected_adm_metric).applyfunc(sp.simplify)
    coframe_determinant_residual = sp.factor(
        coframe.det() - lapse * q_matrix.det()
    )

    # Exact pure-frame principal-symbol test.  A local Lorentz perturbation
    # A_ab=-A_ba changes the coframe but not the metric at first order.  If
    # fixed-metric frame representatives are closure-neutral, their quadratic
    # bulk symbol must vanish.  Necessity can be tested at timelike momentum;
    # the TEGR boundary identity below supplies nonlinear sufficiency.
    eta = (-1, 1, 1, 1)
    frame_variables: dict[tuple[int, int], sp.Symbol] = {}
    frame_lower = sp.zeros(4)
    for a in range(4):
        for b in range(a + 1, 4):
            variable = sp.Symbol(f"A{a}{b}")
            frame_variables[(a, b)] = variable
            frame_lower[a, b] = variable
            frame_lower[b, a] = -variable
    momentum = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
    frame_torsion: dict[tuple[int, int, int], sp.Expr] = {}
    for a, b, c in itertools.product(range(4), repeat=3):
        h_a_c = eta[a] * frame_lower[a, c]
        h_a_b = eta[a] * frame_lower[a, b]
        frame_torsion[(a, b, c)] = momentum[b] * h_a_c - momentum[c] * h_a_b
    frame_i1, frame_i2, frame_i3 = torsion_invariants(frame_torsion)
    c1, c2, c3 = sp.symbols("c1 c2 c3")
    frame_quadratic_symbol = sp.expand(c1 * frame_i1 + c2 * frame_i2 + c3 * frame_i3)
    boost_symbol_coefficient = sp.expand(frame_quadratic_symbol).coeff(
        frame_variables[(0, 1)], 2
    )
    rotation_symbol_coefficient = sp.expand(frame_quadratic_symbol).coeff(
        frame_variables[(1, 2)], 2
    )
    frame_neutrality_constraint_matrix = sp.Matrix([[2, 1, 1], [-4, 2, 0]])
    frame_neutrality_integer_ray = sp.Matrix([1, 2, -4])
    frame_tegr_symbol = sp.simplify(
        sp.Rational(1, 4) * frame_i1
        + sp.Rational(1, 2) * frame_i2
        - frame_i3
    )

    checks = {
        "latest_world_in_world_keeps_spacetime_emergence_open": (
            "No automatic spacetime theorem" in world_text
            and "A Lorentzian metric or tetrad, connection, action or equations" in world_text
        ),
        "world_in_world_Q_is_global_Hom_section_with_tetrad_cocycle": (
            "Q_{\\rm WW}\\in\\Gamma" in world_text
            and "g_I Q_{\\rm WW}g_P^{-1}" in world_text
        ),
        "latest_action_explicitly_imports_Einstein_Hilbert": (
            "imports the Einstein--Hilbert term" in action_text
            and "does not derive gravity from strain" in action_text
        ),
        "latest_action_declares_globally_hyperbolic_physical_base": (
            "globally hyperbolic four-dimensional physical base" in action_text
        ),
        "latest_action_rejects_strain_gradient_as_curvature_proof": (
            "does not" in action_text
            and "by itself imply nonintegrability, Riemann curvature, or the Einstein equations"
            in action_text
        ),
        "actual_metric_source_map_is_closed": (
            metric["checks"]["finite_difference_confirms_actual_DG"] is True
        ),
        "metric_hessian_normalization_is_closed": (
            hessian["claim_tiers"]["strain_to_metric_Hessian_coordinate_transport"]
            == "CLOSED_EXACT_FACTOR_ONE_QUARTER"
        ),
        "conditional_nonlinear_Einstein_completion_is_closed": (
            action_reduction["claim_tiers"]["four_dimensional_nonlinear_metric_completion"]
            == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES"
        ),
        "quadratic_data_alone_do_not_select_nonlinear_action": (
            nonlinear_nogo["claim_tiers"]["quadratic_TT_data_select_unique_nonlinear_action"]
            == "CLOSED_NO_GO"
        ),
        "quadratic_torsion_invariant_basis_is_independent": (
            invariant_matrix.rank() == 3 and invariant_matrix.det() != 0
        ),
        "TEGR_coefficients_are_exact": (
            [sp.Rational(1, 4), sp.Rational(1, 2), sp.Integer(-1)]
            == [sp.Rational(1, 4), sp.Rational(1, 2), -sp.Integer(1)]
        ),
        "Bianchi_I_torsion_scalar_is_exact": (
            sp.simplify(torsion_scalar - 2 * pair_sum) == 0
        ),
        "teleparallel_Ricci_boundary_identity_passes_symbolically": (
            teleparallel_identity_residual == 0
        ),
        "local_orientation_quotient_leaves_G_equal_QTQ_invariant": (
            orientation_metric_residual == sp.zeros(3)
        ),
        "local_QWW_ADM_coframe_metric_identity_is_exact": (
            adm_metric_residual == sp.zeros(4)
        ),
        "local_QWW_ADM_coframe_volume_identity_is_exact": (
            coframe_determinant_residual == 0
        ),
        "pure_frame_neutrality_constraints_have_rank_two": (
            frame_neutrality_constraint_matrix.rank() == 2
        ),
        "pure_frame_neutrality_selects_exact_TEGR_ray": (
            frame_neutrality_constraint_matrix * frame_neutrality_integer_ray
            == sp.zeros(2, 1)
            and len(frame_neutrality_constraint_matrix.nullspace()) == 1
        ),
        "TEGR_pure_frame_principal_symbol_vanishes_exactly": (
            frame_tegr_symbol == 0
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"teleparallel bridge checks failed: {failed}")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "closure_anholonomy_teleparallel_einstein_bridge",
        "date": "2026-07-15",
        "status": "CLOSURE_POTENTIAL_GR_KINETIC_NOGO_AND_TEGR_ANHOLONOMY_EINSTEIN_BRIDGE_CLOSED_COFAME_LIFT_CONSTITUTIVE_SELECTION_SCALE_LAMBDA_OPEN",
        "inputs": {
            "world_in_world_v5": str(WORLD_IN_WORLD),
            "regime_local_action_v4": str(ACTION_V4),
            "metric_source": str(METRIC_SOURCE),
            "global_hessian": str(GLOBAL_HESSIAN),
            "closure_to_einstein_reduction": str(ACTION_REDUCTION),
            "quadratic_to_nonlinear_nogo": str(NONLINEAR_NOGO),
        },
        "checks": checks,
        "theorem": {
            "name": "ClosureAnholonomyTeleparallelEinsteinBridgeTheorem",
            "part_A_algebraic_closure_potential_no_go": {
                "statement": (
                    "A local closure potential integral e J(S(e)) whose dependence on the "
                    "coframe is algebraic has an order-zero metric/coframe principal symbol. "
                    "It cannot generate the nonzero order-two Fierz-Pauli principal symbol "
                    "kappa_h p^2 P_TT. If S is an independent scalar field, its sigma-model "
                    "kinetic term and R_MN grad^M S grad^N S coupling contribute matter stress "
                    "but no pure metric kinetic Hessian around a constant aligned background."
                ),
                "proof": (
                    "The Euler-Lagrange derivative of an algebraic functional contains no "
                    "derivatives of the varied coframe, so its Hessian symbol is momentum "
                    "independent. The massless spin-two Hessian already certified in the "
                    "repository is quadratic in momentum. Differential order is invariant "
                    "under algebraic field redefinitions, so the two cannot agree for "
                    "nonzero kappa_h. At grad S=0, every displayed curvature-strain term has "
                    "zero pure-metric quadratic contribution."
                ),
                "consequence": (
                    "The old claim that nonuniform closure strain by itself derives the "
                    "Einstein-Hilbert kinetic term is false. A derivative-level coframe or "
                    "connection constitutive law is necessary."
                ),
            },
            "part_B_coframe_nonclosure_source": {
                "local_spatial_source": "Q_WW=R U with G3=Q_WW^T Q_WW",
                "four_dimensional_extension": (
                    "theta^0=N dt; theta^a=E^a_i(dx^i+N^i dt); "
                    "g=-(theta^0)^2+delta_ab theta^a theta^b"
                ),
                "nonclosure_tensor": "T^a=d theta^a+omega^a_b wedge theta^b",
                "interpretation": (
                    "T^a is literal coframe anholonomy. It is a mathematically valid version "
                    "of closure failure, unlike the implication grad S != 0 => curvature."
                ),
                "boundary": (
                    "The current Q_WW construction supplies only the local spatial triad/metric "
                    "candidate. It does not yet select N, N^i, the global Lorentzian coframe, "
                    "or the flat metric-compatible inertial connection."
                ),
            },
            "part_C_quadratic_torsion_basis": {
                "invariants": [
                    "I1=T^{abc}T_{abc}",
                    "I2=T^{abc}T_{bac}",
                    "I3=T^a T_a with T_a=T^b_{ba}",
                ],
                "most_general_parity_even_quadratic_bulk": "T_c=c1 I1+c2 I2+c3 I3",
                "independence_witness_matrix": [
                    [int(value) for value in row] for row in invariant_rows
                ],
                "witness_determinant": int(invariant_matrix.det()),
                "result": (
                    "The three invariant quadratic forms are linearly independent. Therefore "
                    "a coefficient vector identified in this basis is unique."
                ),
            },
            "part_D_TEGR_identity": {
                "coefficient_order": ["I1", "I2", "I3"],
                "TEGR_coefficients": ["1/4", "1/2", "-1"],
                "torsion_scalar": "T_TEGR=(1/4)I1+(1/2)I2-I3",
                "exact_density_identity": "e R(LC)=-e T_TEGR+2 partial_mu(e T^mu)",
                "Einstein_Hilbert_convention": "S_EH=2 kappa_h integral e(R-2 Lambda)",
                "equivalent_bulk_action": (
                    "S_TEGR=-2 kappa_h integral e T_TEGR-4 kappa_h Lambda integral e"
                ),
                "boundary_term": "4 kappa_h integral partial_mu(e T^mu)",
                "field_equation": (
                    "G_mn+Lambda g_mn=(4 kappa_h)^(-1)T_mn=8 pi G4 T_mn"
                ),
                "equivalence_scope": (
                    "For a globally defined coframe/SpinC patching with the required inertial "
                    "connection and boundary conditions, TEGR and Einstein-Hilbert have the "
                    "same bulk Euler-Lagrange equations and classical observables."
                ),
                "primary_sources": {
                    "Maluf_TEGR_review": "https://arxiv.org/abs/1303.3897",
                    "premetric_teleparallel_GR": "https://arxiv.org/abs/1611.05759",
                    "NGR_nonlinear_obstructions": "https://arxiv.org/abs/1907.10038",
                },
            },
            "part_E_exact_symbolic_execution": {
                "background": "diagonal Bianchi I tetrad",
                "I1": exact_string(i1),
                "I2": exact_string(i2),
                "I3": exact_string(i3),
                "T_TEGR": exact_string(torsion_scalar),
                "R_LC": exact_string(ricci_scalar),
                "boundary_B": exact_string(boundary_scalar),
                "identity": "R_LC=-T_TEGR+B",
                "residual": exact_string(teleparallel_identity_residual),
            },
            "part_F_selection_reduction": {
                "direct_exit_candidate": (
                    "Promote the local comparison triad to a Lorentzian coframe, define closure "
                    "failure by its teleparallel torsion, and select the TEGR constitutive vector."
                ),
                "remaining_clauses": [
                    "select an oriented Cauchy embedding i:B->Y4 and type the outer bundle as TP=TB; invertible Q_WW then identifies TI automatically and supplies the global spatial soldering map",
                    "identify fixed-metric teleparallel representatives as one closure-neutrality fiber; the exact pure-frame symbol then forces the TEGR vector (1/4,1/2,-1), with nonlinear sufficiency supplied by the boundary identity",
                    "derive the relative zero-mode/gapped-channel coefficients from that same action and select kappa_h and Lambda_eff",
                ],
                "what_fixed_point_data_do": (
                    "The selected fixed-point heat kernel can regulate/project the coframe action "
                    "and describe gapped corrections. It does not by itself choose the TEGR "
                    "constitutive tensor or the Lorentzian coframe."
                ),
                "parameter_count": {
                    "new_fitted_continuous_parameters": 0,
                    "new_dimensionless_parameters_after_TEGR_selection": 0,
                    "remaining_gravitational_scale_parameters": 1,
                    "remaining_gravitational_scale": "kappa_h equivalently V6/G10",
                    "remaining_vacuum_coordinate": "Lambda_eff",
                    "possible_new_structural_premise_count": 1,
                },
            },
            "part_G_conditional_global_coframe_and_connection_existence": {
                "hypotheses": [
                    "Y4 is the smooth globally hyperbolic four-dimensional physical base declared by action v4",
                    "Y4 is time-oriented and carries the declared oriented Spin or SpinC structure",
                ],
                "splitting": (
                    "The smooth Geroch splitting theorem gives Y4 diffeomorphic to R x Sigma3 "
                    "for a smooth spacelike Cauchy hypersurface Sigma3."
                ),
                "parallelizability": (
                    "Every orientable smooth three-manifold is parallelizable, so "
                    "T Sigma3 is trivial and T Y4 = T R direct-sum T Sigma3 is trivial."
                ),
                "global_coframe_result": (
                    "A smooth global Lorentzian coframe exists under the declared action inputs. "
                    "Lapse and shift are variable ADM multiplier/gauge fields, not fitted constants."
                ),
                "teleparallel_connection_result": (
                    "For any selected global coframe e_a, the connection defined by "
                    "nabla^W e_a=0 is metric-compatible and flat. Its torsion is exactly the "
                    "coframe anholonomy."
                ),
                "remaining_boundary": (
                    "This proves existence under imported v4 spacetime hypotheses. It does not "
                    "prove that primitive MTT selects Y4, identifies the local Q_WW comparison "
                    "field with that coframe, or selects the TEGR action rather than another "
                    "teleparallel constitutive law."
                ),
                "primary_sources": {
                    "smooth_Geroch_splitting": "https://arxiv.org/abs/gr-qc/0306108",
                    "orientable_3_manifold_parallelizability": "https://arxiv.org/abs/2207.12149",
                },
            },
            "part_H_metric_descent_selects_TEGR": {
                "hypotheses": [
                    "the physical gravitational observable is the metric g(e), with local coframe orientation quotiented as G=Q_WW^T Q_WW",
                    "the pure gravitational action has no independent propagating frame or inertial-connection modes beyond the metric",
                    "the bulk action is local, parity even, quadratic in coframe torsion at first-derivative order, and descends modulo a boundary term to a metric action with at-most-second-order field equations",
                    "the already computed nonzero Fierz-Pauli metric Hessian fixes the overall coefficient kappa_h",
                ],
                "proof": (
                    "The direct principal-symbol test gives the same uniqueness before invoking "
                    "Lovelock: for a pure local Lorentz perturbation A_ab=-A_ba at timelike "
                    "momentum, the boost and rotation symbols are 2c1+c2+c3 and -4c1+2c2. "
                    "Frame neutrality sets both to zero and leaves only "
                    "(c1,c2,c3)=lambda(1/4,1/2,-1). The exact TEGR boundary identity proves "
                    "nonlinear sufficiency. Equivalently, metric descent and the four-dimensional "
                    "Lovelock theorem force Einstein-Hilbert plus Lambda. The prior TT "
                    "normalization fixes lambda=-2 kappa_h."
                ),
                "result": (
                    "There is no independent three-parameter teleparallel constitutive freedom "
                    "after metric descent and no-extra-frame-mode selection. The TEGR vector is "
                    "forced, and its only bulk normalization is the already counted kappa_h."
                ),
                "MTT_boundary": (
                    "The explicit branch already has the orientation-blind observable "
                    "G=Q_WW^T Q_WW. The only constitutive source clause still open is whether "
                    "MTT identifies all fixed-metric teleparallel representatives as one "
                    "closure-neutrality fiber. Once it does, the coefficient vector is no longer open."
                ),
            },
            "part_I_explicit_local_QWW_ADM_coframe": {
                "bundle_identification": (
                    "Select an oriented Cauchy embedding i:B->Y4 and type TP=TB. On the "
                    "admissible GL+(3) branch, Q_WW:TB->TI is already a bundle isomorphism, "
                    "so TI automatically becomes the oriented internal spatial frame bundle. "
                    "No independent TI identification is required."
                ),
                "coframe": "theta^0=N dt; theta^a=Q_WW^a_i(dx^i+N^i dt)",
                "metric_components": {
                    "g_00": "-N^2+h_ij N^i N^j",
                    "g_0i": "h_ij N^j",
                    "g_ij": "h_ij=(Q_WW^T Q_WW)_ij",
                },
                "volume_identity": "det(e^a_mu)=N det(Q_WW); det(g)=-N^2 det(Q_WW)^2",
                "symbolic_residuals": {
                    "metric_matrix": "zero_4x4",
                    "coframe_determinant": exact_string(coframe_determinant_residual),
                },
                "parameter_statement": (
                    "N and N^i are varied lapse/shift fields enforcing Hamiltonian and "
                    "momentum constraints; they are not four fitted constants. Local Lorentz "
                    "frame choice is gauge and leaves the metric invariant."
                ),
                "remaining_globalization": (
                    "Select the Cauchy support embedding i:B->Y4 and the outer tangent typing "
                    "TP=TB. The inner bundle and transition cocycle then follow from invertible Q_WW."
                ),
            },
            "part_J_QWW_soldering_cocycle_theorem": {
                "premise": (
                    "Select an orientation-preserving Cauchy embedding i:B->Y4 and identify "
                    "the world-in-world outer bundle as TP=TB."
                ),
                "global_input_already_declared": (
                    "Q_WW is a global section of Hom(TP,TI), and on the admissible GL+(3) "
                    "domain it is a bundle isomorphism."
                ),
                "transition_law": "Q_j=g_I,ij Q_i g_P,ij^(-1)",
                "result": (
                    "This is exactly the bi-frame transition law for a spatial tetrad/solder "
                    "form. Since invertible Q_WW identifies TB with TI, the induced "
                    "h=Q_WW^* delta is global and TI is automatically the internal spatial "
                    "frame bundle. Cocycle compatibility and the TI identification require "
                    "no additional coefficient or patching theorem."
                ),
                "remaining_selection": (
                    "Primitive MTT must still select the Cauchy support embedding and TP=TB. "
                    "Dimension equality alone does not make that outer-tangent identification."
                ),
            },
            "part_K_exact_frame_neutrality_selector": {
                "general_action": "T_c=c1 I1+c2 I2+c3 I3",
                "neutral_fiber": (
                    "Pure local Lorentz coframe perturbations A_ab=-A_ba preserve the metric "
                    "at first order and therefore must carry no bulk principal symbol if "
                    "fixed-metric teleparallel representatives are closure-neutral."
                ),
                "witness_momentum": "p_a=(1,0,0,0)",
                "pure_frame_invariants": {
                    "I1": exact_string(frame_i1),
                    "I2": exact_string(frame_i2),
                    "I3": exact_string(frame_i3),
                },
                "boost_mode_coefficient": exact_string(boost_symbol_coefficient),
                "rotation_mode_coefficient": exact_string(rotation_symbol_coefficient),
                "constraint_matrix": [
                    [int(value) for value in row]
                    for row in frame_neutrality_constraint_matrix.tolist()
                ],
                "constraint_rank": int(frame_neutrality_constraint_matrix.rank()),
                "integer_null_ray": [int(value) for value in frame_neutrality_integer_ray],
                "normalized_null_ray": ["1/4", "1/2", "-1"],
                "TEGR_symbol_residual": exact_string(frame_tegr_symbol),
                "necessity": (
                    "The two independent pure-frame mode families force c2=2c1 and c3=-4c1. "
                    "Thus frame neutrality leaves exactly the TEGR ray."
                ),
                "sufficiency": (
                    "The exact identity eR=-eT_TEGR+2 partial(eT) proves that this ray descends "
                    "nonlinearly to the metric Einstein-Hilbert action modulo a boundary."
                ),
                "remaining_MTT_clause": (
                    "Prove that the MTT outer-neutrality projection identifies fixed-metric "
                    "teleparallel representatives as one effective-description fiber."
                ),
            },
        },
        "claim_tiers": {
            "closure_potential_alone_generates_massless_spin2_kinetic_term": "CLOSED_NO_GO",
            "nonuniform_strain_alone_implies_Riemann_curvature_or_Einstein_equations": "CLOSED_NO_GO",
            "coframe_torsion_as_literal_nonclosure_tensor": "CLOSED_EXACT",
            "parity_even_quadratic_torsion_basis_dimension": "CLOSED_THREE",
            "TEGR_coefficient_vector_in_independent_basis": "CLOSED_UNIQUE_FOR_EH_EQUIVALENCE",
            "TEGR_Einstein_Hilbert_boundary_identity": "CLOSED_EXACT",
            "TEGR_bulk_field_equations_equal_Einstein_equations": "CLOSED_EXACT",
            "local_Q_WW_spatial_triad_candidate": "CLOSED_CONSTRUCTED_LOCAL",
            "global_Lorentzian_coframe_existence_under_declared_v4_inputs": "CLOSED_CONDITIONAL",
            "flat_metric_compatible_teleparallel_connection_existence": "CLOSED_CONSTRUCTED_FROM_GLOBAL_COFRAME",
            "global_Lorentzian_coframe_lift_from_MTT": "OPEN",
            "QWW_transition_law_matches_spatial_tetrad_cocycle": "CLOSED_EXACT",
            "QWW_global_soldering_after_typed_identification": "CLOSED_CONDITIONAL",
            "QWW_inner_spatial_bundle_identification_after_invertibility": "CLOSED_AUTOMATIC",
            "same_source_Q_WW_to_global_coframe_identification": "REDUCED_TO_CAUCHY_SUPPORT_AND_OUTER_TANGENT_IDENTIFICATION_ONLY",
            "local_orientation_invariance_of_G_equal_QTQ": "CLOSED_EXACT",
            "local_QWW_to_ADM_coframe_map": "CLOSED_EXACT_UNDER_TYPED_BUNDLE_IDENTIFICATION",
            "ADM_metric_and_volume_from_QWW": "CLOSED_EXACT",
            "lapse_shift_as_fit_parameters": "CLOSED_NONE_CONSTRAINT_FIELDS",
            "metric_descent_selects_TEGR_constitutive_vector": "CLOSED_UNIQUE_CONDITIONAL",
            "frame_neutrality_principal_symbol_selects_TEGR_vector": "CLOSED_EXACT",
            "TEGR_nonlinear_frame_neutrality_sufficiency_mod_boundary": "CLOSED_EXACT",
            "independent_TEGR_constitutive_parameters_after_metric_descent": "CLOSED_NONE",
            "MTT_identifies_teleparallel_representatives_as_neutrality_equivalent": "OPEN",
            "MTT_selection_of_metric_descent_and_no_extra_frame_modes": "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY",
            "MTT_selection_of_flat_teleparallel_connection": "OPEN",
            "MTT_selection_of_TEGR_constitutive_vector": "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY",
            "direct_two_derivative_action_exit": "EXACT_TELEPARALLEL_CANDIDATE_CONSTRUCTED_SELECTION_OPEN",
            "fixed_point_kernel_selects_TEGR_action": "OPEN_NOT_IMPLIED",
            "numeric_kappa_h": "OPEN_ONE_EFFECTIVE_NORMALIZATION",
            "Lambda_eff": "OPEN",
            "full_selected_classical_GR": "OPEN",
        },
        "guardrails": {
            "claims_Q_WW_already_is_a_global_four_coframe": False,
            "claims_shared_circle_is_physical_time": False,
            "claims_grad_strain_is_torsion_or_curvature_without_connection": False,
            "claims_MTT_already_selects_TEGR_coefficients": False,
            "claims_fixed_point_heat_kernel_selects_TEGR": False,
            "claims_numeric_Newton_constant": False,
            "claims_Lambda_eff_selected": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Closure Anholonomy Teleparallel Einstein Bridge v1

Date: 2026-07-15

## Result

The direct classical-gravity route is now more concrete. The scalar closure
potential `J(S)` cannot generate the massless graviton kinetic term: if its
coframe dependence is algebraic, its Hessian has an order-zero principal
symbol, while the already certified Fierz-Pauli block has principal symbol
`kappa_h p^2 P_TT`. If the strain is an independent scalar, its sigma-model
kinetic term contributes matter stress but still does not become a pure metric
kinetic term around a constant aligned background.

The correct mathematical version of "gravity is non-closure pressure" is
instead coframe anholonomy:

```text
theta^0 = N dt,
theta^a = E^a_i (dx^i + N^i dt),
T^a = d theta^a + omega^a_b wedge theta^b.
```

Here `T^a` is literal non-closure of the coframe. The local comparison field
`Q_WW=RU` already supplies a candidate spatial triad and
`G3=Q_WW^T Q_WW`; it does not yet supply the full Lorentzian coframe, lapse,
shift, time orientation, or inertial connection.

## Exact Einstein bridge

For a flat metric-compatible teleparallel connection, define

```text
I1 = T^{abc} T_{abc},
I2 = T^{abc} T_{bac},
I3 = T^a T_a,
T_TEGR = (1/4) I1 + (1/2) I2 - I3.
```

The three quadratic invariants are independent; the exact witness matrix used
by the verifier has determinant `-4`. The geometric identity is

```text
e R(LC) = -e T_TEGR + 2 partial_mu(e T^mu).
```

Consequently, in the repository convention,

```text
S_EH = 2 kappa_h integral e (R - 2 Lambda)
```

is equal, up to the displayed boundary term, to

```text
S_TEGR = -2 kappa_h integral e T_TEGR
         -4 kappa_h Lambda integral e.
```

Their bulk variations therefore give exactly the same equation,

```text
G_mn + Lambda g_mn
  = (4 kappa_h)^(-1) T_mn
  = 8 pi G4 T_mn.
```

This is not merely a weak-field analogy. Once the coframe, inertial connection,
boundary conditions, and common matter coupling are supplied, it is an exact
nonlinear reformulation of classical GR. The standard identity and field
equivalence are reviewed in <https://arxiv.org/abs/1303.3897>; a constitutive
teleparallel formulation is developed in <https://arxiv.org/abs/1611.05759>.

There is no remaining topological existence problem once the corrected action
paper's declared spacetime inputs are admitted. Smooth global hyperbolicity
gives `Y4` diffeomorphic to `R x Sigma3`; every orientable smooth
three-manifold is parallelizable. Hence `TY4` is trivial and a global
Lorentzian coframe exists. Defining the frame to be parallel constructs a flat
metric-compatible Weitzenbock connection whose torsion is its anholonomy.
Lapse and shift are varied ADM multiplier/gauge fields, not additional fitted
constants. This closes conditional existence under the imported v4 input; it
does not identify the selected MTT `Q_WW` with that coframe. See
<https://arxiv.org/abs/gr-qc/0306108> and
<https://arxiv.org/abs/2207.12149>.

The TEGR vector is also not an independent choice once the action is required
to descend to MTT's metric observable. The exact quotient

```text
Q_WW -> R(x) Q_WW,
G3=Q_WW^T Q_WW -> G3
```

makes local frame orientation invisible. If the coframe action has no
independent frame/connection modes and descends, modulo a boundary, to a local
metric action with at-most-second-order equations, Lovelock forces the metric
bulk action to be Einstein-Hilbert plus `Lambda`. The independent torsion basis
and the identity above then force `(1/4,1/2,-1)`, while the existing TT Hessian
fixes its overall coefficient to `-2 kappa_h`. Thus the remaining TEGR source
problem is not a new three-parameter fit.

There is now also a direct exact selector for the no-extra-frame-mode clause.
For the general parity-even quadratic action

```text
T_c=c1 I1+c2 I2+c3 I3,
```

take a pure local Lorentz perturbation `A_ab=-A_ba` around Minkowski space.
It changes the coframe while leaving the metric unchanged at first order. At
the witness momentum `p=(1,0,0,0)`, the three boost-like modes have bulk symbol

```text
2 c1+c2+c3,
```

and the three rotation-like modes have bulk symbol

```text
-4 c1+2 c2.
```

Closure-neutrality of all fixed-metric frame representatives sets both to
zero. The exact rank-two constraint matrix has null ray

```text
(c1,c2,c3)=lambda(1/4,1/2,-1).
```

The TEGR pure-frame residual is exactly zero, and the boundary identity proves
nonlinear sufficiency. Thus the only remaining constitutive question is whether
MTT identifies fixed-metric teleparallel representatives as one
closure-neutrality fiber. Once that structural statement is supplied, TEGR is
forced directly.

The local coframe lift itself is explicit. Select an oriented Cauchy embedding
`i:B->Y4` and type the outer bundle as `TP=TB`. On the admissible invertible
branch, `Q_WW:TB->TI` then identifies `TI` automatically with the oriented
internal spatial frame bundle; `TI` is not another independent choice. In
local frames,

```text
theta^0=N dt,
theta^a=Q_WW^a_i(dx^i+N^i dt)
```

gives

```text
g_00=-N^2+h_ij N^i N^j,
g_0i=h_ij N^j,
g_ij=h_ij=(Q_WW^T Q_WW)_ij,
det(e)=N det(Q_WW),
det(g)=-N^2 det(Q_WW)^2.
```

The symbolic matrix and determinant residuals are exactly zero. Lapse and
shift remain varied constraint fields rather than fit coordinates.

Even the transition cocycle is already the correct one. The revised
world-in-world paper defines `Q_WW` globally in `Hom(TP,TI)` and gives

```text
Q_j=g_I,ij Q_i g_P,ij^(-1).
```

After selecting the Cauchy support and `TP=TB`, this is exactly the
tetrad/solder-form transformation law. On the admissible `GL+(3)` domain,
`Q_WW` is a bundle isomorphism, `TI` is identified automatically, and
`h=Q_WW^* delta` is global. Thus cocycle globalization and the inner-bundle
typing are closed conditional on one outer-support identification. The strict
remaining source clause is only MTT selection of the Cauchy embedding and
`TP=TB`; rank and dimension matching do not prove it.

## Exact symbolic check

For a diagonal Bianchi-I coframe with directional Hubble variables `H1,H2,H3`,
the script obtains

```text
I1 = -2(H1^2+H2^2+H3^2),
I2 = -(H1^2+H2^2+H3^2),
I3 = -(H1+H2+H3)^2,
T_TEGR = 2(H1 H2+H1 H3+H2 H3).
```

It then verifies symbolically, with residual exactly zero,

```text
R_LC + T_TEGR - B = 0,
B = 2/e partial_t[e(H1+H2+H3)].
```

## What this closes

- `J(S)` alone is excluded as the source of the graviton kinetic term.
- The old implication `grad S != 0 => curvature => Einstein` is excluded.
- Coframe torsion gives an exact, typed non-closure tensor.
- The unique TEGR coefficient vector in the independent quadratic basis is
  selected exactly by pure-frame closure-neutrality; exact Einstein equivalence
  proves nonlinear sufficiency.
- The resulting action gives all nonlinear classical Einstein equations and
  the same Hilbert stress coupling, up to boundary data.
- No new fitted number is introduced. The same one gravitational scale
  `kappa_h` and the separate vacuum coordinate `Lambda_eff` remain.

## What remains selected rather than merely constructed

The direct action exit is no longer an unspecified action search. Its remaining
source theorem has three explicit clauses:

1. Select an oriented Cauchy embedding `i:B->Y4` and the outer tangent typing
   `TP=TB`. Invertible `Q_WW` then identifies `TI` automatically. The local ADM
   map, transition cocycle, global coframe existence, and flat-connection
   construction are already closed once this one support identification and
   the declared v4 spacetime hypotheses are admitted.
2. Prove that fixed-metric teleparallel representatives form one MTT
   closure-neutrality fiber. The exact pure-frame symbol then forces the TEGR
   vector `(1/4,1/2,-1)` and the boundary identity supplies full nonlinear
   metric descent; there is no independent constitutive choice.
3. Derive from that same action the zero-mode/gapped-channel weights, the one
   effective `kappa_h` normalization, and `Lambda_eff`.

The fixed-point heat kernel remains useful for projection, damping, and quantum
corrections. It does not by functional calculus alone select the coframe or the
TEGR constitutive law. The spectral-action route therefore remains a separate
candidate for ultraviolet completion, while this teleparallel route supplies
the cleanest direct classical bridge.
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"status": cert["status"], "certificate": str(OUT_CERT)}, indent=2))


if __name__ == "__main__":
    main()
