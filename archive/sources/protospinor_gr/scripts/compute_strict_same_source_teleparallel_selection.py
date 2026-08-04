from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

FOUNDATION_V8 = (
    TEXPAPERS
    / "3 Core Foundations"
    / "revised_tex_vnext"
    / "Modal_Triplet_Theory__Foundation_v8"
    / "main.tex"
)
WORLD_V5 = (
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
SOURCE_FACTORIZATION = (
    ROOT / "certificates" / "selected_q79_z64_qww_source_factorization_certificate.json"
)
SPECTRAL_HYM_STRAIN_SYMBOL = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
QUARTERTURN_HESSIAN = (
    ROOT
    / "certificates"
    / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
)
PARENT_QUARTERTURN_DESCENT = (
    ROOT
    / "certificates"
    / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
)
SQUARE_THETA_NOGO = (
    ROOT
    / "certificates"
    / "q79_square_theta_quarterturn_strain_nogo_certificate.json"
)
ROOTPLANE_JDE_FUNCTOR = (
    ROOT
    / "certificates"
    / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
)
ORDINARY_HYM_FUNCTOR_NOGO = (
    ROOT
    / "certificates"
    / "q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset_certificate.json"
)
MARKED_C4_DESCENT_NOGO = (
    ROOT
    / "certificates"
    / "q79_marked_shared_circle_c4_descent_nogo_certificate.json"
)
TEGR_BRIDGE = ROOT / "certificates" / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"

OUT_CERT = ROOT / "certificates" / "strict_same_source_teleparallel_selection_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Strict_Same_Source_Teleparallel_Selection_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    foundation_text = FOUNDATION_V8.read_text(encoding="utf-8", errors="replace")
    world_text = WORLD_V5.read_text(encoding="utf-8", errors="replace")
    action_text = ACTION_V4.read_text(encoding="utf-8", errors="replace")
    metric = load(METRIC_SOURCE)
    source_factorization = load(SOURCE_FACTORIZATION)
    spectral_hym_strain_symbol = load(SPECTRAL_HYM_STRAIN_SYMBOL)
    quarterturn_hessian = load(QUARTERTURN_HESSIAN)
    parent_quarterturn_descent = load(PARENT_QUARTERTURN_DESCENT)
    square_theta_nogo = load(SQUARE_THETA_NOGO)
    rootplane_jde_functor = load(ROOTPLANE_JDE_FUNCTOR)
    ordinary_hym_functor_nogo = load(ORDINARY_HYM_FUNCTOR_NOGO)
    marked_c4_descent_nogo = load(MARKED_C4_DESCENT_NOGO)
    bridge = load(TEGR_BRIDGE)

    # Differential of r(Q)=Q^T Q at Q=I.  Its kernel is exactly the
    # three-dimensional skew/orientation tangent, while its image is all six
    # symmetric metric directions.
    dq_symbols = sp.symbols("dq11 dq12 dq13 dq21 dq22 dq23 dq31 dq32 dq33")
    dq = sp.Matrix(3, 3, dq_symbols)
    dg = dq.T + dq
    symmetric_coordinates = sp.Matrix(
        [dg[0, 0], dg[1, 1], dg[2, 2], dg[0, 1], dg[0, 2], dg[1, 2]]
    )
    quotient_jacobian = symmetric_coordinates.jacobian(dq_symbols)

    skew_basis = [
        sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, -1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    ]
    skew_residuals = [basis.T + basis for basis in skew_basis]

    symmetric_basis = [
        sp.diag(1, 0, 0),
        sp.diag(0, 1, 0),
        sp.diag(0, 0, 1),
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    ]
    symmetric_source_rank = sp.Matrix.hstack(
        *[sp.Matrix(basis).reshape(9, 1) for basis in symmetric_basis]
    ).rank()

    frame_selector = bridge["theorem"]["part_K_exact_frame_neutrality_selector"]
    source_construction = metric["construction"]

    checks = {
        "foundation_contains_exact_autonomous_descent_iff": (
            "Autonomous descent criterion" in foundation_text
            and "r(x)=r(x')" in foundation_text
            and "r(\\Phi x)=r(\\Phi x')" in foundation_text
        ),
        "world_source_is_typed_global_Hom_section": (
            "Q_{\\rm WW}\\in\\Gamma" in world_text
            and "operatorname{Hom}(TP,TI)" in world_text
        ),
        "world_source_bundles_have_declared_Euclidean_metrics": (
            "oriented Euclidean" in world_text and "rank-three bundles" in world_text
        ),
        "world_source_has_biframe_transition_law": (
            "g_I Q_{\\rm WW}g_P^{-1}" in world_text
        ),
        "canonical_physical_realization_has_globally_hyperbolic_Y4": (
            "globally hyperbolic four-dimensional physical base" in action_text
        ),
        "selected_candidate_Q_has_no_orientation_coordinate": (
            source_construction["comparison_field"] == "Q(psi)=exp(S(psi))"
        ),
        "selected_candidate_metric_factors_through_QTQ": (
            source_construction["metric_observable"]
            == "G(psi)=Q(psi)^T Q(psi)=exp(2 S(psi))"
        ),
        "metric_quotient_differential_has_rank_six": quotient_jacobian.rank() == 6,
        "metric_quotient_orientation_kernel_has_dimension_three": (
            9 - quotient_jacobian.rank() == 3
        ),
        "displayed_skew_basis_is_exactly_metric_null": all(
            residual == sp.zeros(3) for residual in skew_residuals
        ),
        "selected_symmetric_source_tangent_has_rank_six": symmetric_source_rank == 6,
        "pure_frame_neutrality_selects_TEGR_exactly": (
            frame_selector["constraint_rank"] == 2
            and frame_selector["integer_null_ray"] == [1, 2, -4]
            and frame_selector["TEGR_symbol_residual"] == "0"
        ),
        "TEGR_is_nonlinearly_metric_descending_mod_boundary": (
            bridge["claim_tiers"]["TEGR_Einstein_Hilbert_boundary_identity"]
            == "CLOSED_EXACT"
            and bridge["claim_tiers"][
                "TEGR_nonlinear_frame_neutrality_sufficiency_mod_boundary"
            ]
            == "CLOSED_EXACT"
        ),
        "selected_branch_q79_Z64_QWW_source_factorization_is_unique": (
            source_factorization["claim_tiers"][
                "selected_branch_q79_Z64_QWW_source_realization"
            ]
            == "CLOSED_UNIQUE_UP_TO_GAUGE"
            and source_factorization["claim_tiers"][
                "continuous_fitted_physical_parameters"
            ]
            == "CLOSED_ZERO"
        ),
        "primitive_rootstack_Lorentzian_branch_and_actual_HYM_operator_remain_open": (
            source_factorization["claim_tiers"][
                "primitive_MTT_selects_minimal_rootstack_Lorentzian_branch"
            ]
            == "OPEN"
            and spectral_hym_strain_symbol["claim_tiers"][
                "dynamic_projected_HYM_Hessian_on_TT_standard_block"
            ]
            == "OPEN_REDUCED_TO_SYMMETRIC_2_BY_2_BLOCK"
        ),
        "quarterturn_conditionally_scalarizes_the_physical_HYM_block": (
            quarterturn_hessian["claim_tiers"][
                "self_adjoint_S3_quarterturn_Hessian_scalarization"
            ]
            == "CLOSED_EXACT"
            and quarterturn_hessian["claim_tiers"][
                "physical_TT_block_scalarization"
            ]
            == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
            and quarterturn_hessian["finite_data"]["physical_TT_block"]
            == "H_std=kappa_standard*I2"
        ),
        "C4_parent_is_closed_but_descent_or_induced_functor_remains_open": (
            parent_quarterturn_descent["claim_tiers"][
                "shared_Z64_unique_order4_subgroup"
            ]
            == "CLOSED_EXACT"
            and parent_quarterturn_descent["claim_tiers"][
                "free_orbit_covariance_implies_single_branch_Hessian_invariance"
            ]
            == "CLOSED_NO_GO"
            and parent_quarterturn_descent["claim_tiers"][
                "MTT_types_C4_as_Lens_redundancy_not_physical_superselection"
            ]
            == "OPEN"
        ),
        "direct_square_theta_same_carrier_shortcut_is_closed_no_go": (
            square_theta_nogo["claim_tiers"][
                "direct_theta_adjoint_realizes_six_dimensional_JDE"
            ]
            == "CLOSED_NO_GO"
            and square_theta_nogo["claim_tiers"][
                "nontrivial_inverse_Fourier_Mukai_induced_JDE_functor"
            ]
            == "OPEN"
        ),
        "shared_rootplane_twisted_exterior_functor_closes_flat_symbol_JDE": (
            rootplane_jde_functor["claim_tiers"][
                "typed_shared_C4_to_rootstack_strain_JDE_functor"
            ]
            == "CLOSED_EXACT_ON_FLAT_SHEET_SYMBOL"
            and rootplane_jde_functor["claim_tiers"][
                "JDE_parallel_under_minimal_rootstack_flat_connection"
            ]
            == "CLOSED_EXACT"
            and rootplane_jde_functor["claim_tiers"][
                "actual_inverse_Fourier_Mukai_HYM_induced_JDE"
            ]
            == "OPEN"
        ),
        "spectral_sheet_symbol_bridge_and_full_connection_no_go_are_closed": (
            spectral_hym_strain_symbol["claim_tiers"][
                "spectral_sheet_symbol_to_q79_rootstack_strain_carrier"
            ]
            == "CLOSED_EXACT"
            and spectral_hym_strain_symbol["claim_tiers"][
                "literal_full_inverse_Fourier_Mukai_HYM_connection_identity"
            ]
            == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION"
        ),
        "ordinary_dual_exterior_HYM_extension_is_closed_no_go_for_JDE": (
            ordinary_hym_functor_nogo["claim_tiers"][
                "ordinary_dual_and_exterior_square_preserve_HYM_equations"
            ]
            == "CLOSED_EXACT"
            and ordinary_hym_functor_nogo["claim_tiers"][
                "ordinary_dual_or_exterior_square_realizes_JDE"
            ]
            == "CLOSED_NO_GO"
            and ordinary_hym_functor_nogo["claim_tiers"][
                "nonzero_c3_branch_is_complex_linearly_self_dual"
            ]
            == "CLOSED_NO_GO"
            and ordinary_hym_functor_nogo["finite_data"][
                "derived_kernel_contract_rows_available"
            ]
            == 2
        ),
        "marked_shared_circle_C4_descent_is_closed_no_go_in_current_setup": (
            marked_c4_descent_nogo["claim_tiers"][
                "autonomous_Lens_descent_in_current_marked_shared_circle_setup"
            ]
            == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
            and marked_c4_descent_nogo["claim_tiers"][
                "shared_circle_c3_clutching_is_C4_equivariant"
            ]
            == "CLOSED_NO_GO_FOR_DISPLAYED_CLUTCHING_DIRECTION"
            and marked_c4_descent_nogo["finite_data"][
                "unmarked_modular_exit_contract_rows_available"
            ]
            == 0
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"strict same-source TEGR selection checks failed: {failed}")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "strict_same_source_teleparallel_selection",
        "date": "2026-07-15",
        "status": "STRICT_SAME_SOURCE_CANONICAL_PHYSICAL_BRANCH_SELECTS_TEGR_IR_ACTION_EXACT_PRIMITIVE_REALIZATION_KAPPA_LAMBDA_UV_OPEN",
        "inputs": {
            "foundation_v8": str(FOUNDATION_V8),
            "world_in_world_v5": str(WORLD_V5),
            "action_v4": str(ACTION_V4),
            "metric_source_certificate": str(METRIC_SOURCE),
            "q79_z64_qww_source_factorization_certificate": str(
                SOURCE_FACTORIZATION
            ),
            "q79_spectral_hym_strain_symbol_bridge_certificate": str(
                SPECTRAL_HYM_STRAIN_SYMBOL
            ),
            "q79_complement_quarterturn_hessian_scalarization_certificate": str(
                QUARTERTURN_HESSIAN
            ),
            "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate": str(
                PARENT_QUARTERTURN_DESCENT
            ),
            "q79_square_theta_quarterturn_strain_nogo_certificate": str(
                SQUARE_THETA_NOGO
            ),
            "q79_shared_rootplane_twisted_exterior_jde_functor_certificate": str(
                ROOTPLANE_JDE_FUNCTOR
            ),
            "teleparallel_bridge_certificate": str(TEGR_BRIDGE),
        },
        "checks": checks,
        "theorem": {
            "name": "StrictSameSourceTeleparallelSelectionTheorem",
            "part_A_exact_metric_quotient": {
                "map": "r:GL+(3)->Sym+(3), r(Q)=Q^T Q",
                "differential_at_identity": "Dr_I[dQ]=dQ^T+dQ",
                "jacobian_rank": int(quotient_jacobian.rank()),
                "kernel_dimension": int(9 - quotient_jacobian.rank()),
                "kernel": "so(3), the three skew/orientation directions",
                "image": "Sym(3), all six spatial metric/strain directions",
                "exact_fiber": "r(RQ)=r(Q) for every R in SO(3)",
            },
            "part_B_selected_candidate_source_support": {
                "finite_source": source_construction["source_space"],
                "strain_map": source_construction["strain_map"],
                "comparison_field": source_construction["comparison_field"],
                "metric_observable": source_construction["metric_observable"],
                "source_tangent": "symmetric strain only",
                "orientation_source_coordinates": 0,
                "selected_branch_provenance": (
                    "The exact Z64 k=2/k=62 plane has the unique q79 preimages "
                    "f_plus=(1/sqrt(2),-1/sqrt(2),0;0,0,0) in A0 and "
                    "f_cross=(0,0,0;0,0,1) in A on the minimal full-monodromy "
                    "root stack. J, exp, and pullback metric give the displayed packet."
                ),
                "selected_branch_uniqueness": "CLOSED_UP_TO_POLARIZATION_FRAME_AND_DIFF_GAUGE",
                "consequence": (
                    "A bulk action with a nonzero skew/frame Hessian introduces a source "
                    "coordinate absent from the selected candidate packet. It is therefore "
                    "not a strict same-source completion of this packet."
                ),
            },
            "part_C_foundation_factor_through_application": {
                "foundation_result": (
                    "A reduced autonomous map exists exactly when microscopic evolution is "
                    "constant after projection on every fiber of the reduction map."
                ),
                "gravity_reduction": "r(Q)=Q^T Q",
                "strict_same_source_requirement": (
                    "The leading gravitational action/dynamics is a functor of the selected "
                    "metric source, so it factors through r and is constant on orientation fibers."
                ),
                "alternative": (
                    "A modified teleparallel action with independent frame modes is a valid "
                    "larger-source theory only after an orientation/connection source is added."
                ),
            },
            "part_D_exact_TEGR_selection": {
                "general_parity_even_quadratic_torsion_action": "c1 I1+c2 I2+c3 I3",
                "orientation_fiber_bulk_constraints": [
                    "2c1+c2+c3=0",
                    "-4c1+2c2=0",
                ],
                "constraint_rank": frame_selector["constraint_rank"],
                "unique_ray": "(c1,c2,c3)=lambda(1/4,1/2,-1)",
                "nonlinear_sufficiency": "eR(LC)=-eT_TEGR+2 partial_mu(eT^mu)",
                "result": (
                    "At strict same-source, parity-even, first-derivative/two-derivative IR "
                    "order, the candidate action is uniquely TEGR/Einstein-Hilbert up to its "
                    "overall kappa_h normalization, Lambda, and a boundary term."
                ),
            },
            "part_E_cauchy_support_typing": {
                "premises": [
                    "the canonical physical realization supplies a globally hyperbolic Y4",
                    "Q_WW is used as a local spatial source without an additional support/pullback map",
                    "strict same-source completion forbids adding an unselected localization map",
                ],
                "result": (
                    "The world-in-world base is typed as an oriented Cauchy support B=Sigma3 "
                    "up to diffeomorphism and TP=TB. On GL+(3), Q_WW:TB->TI identifies TI "
                    "automatically. Different Cauchy charts are diffeomorphism gauge, not fit data."
                ),
                "scope": (
                    "This closes typing inside the declared canonical physical realization. "
                    "Primitive MTT selection of that realization remains independent."
                ),
            },
            "part_F_claim_boundary": {
                "closed": [
                    "the explicit q79/Z64-to-Q_WW source factorization on the selected massless-helicity-two minimal-rootstack branch",
                    "orientation-fiber neutrality for a strict completion of the displayed metric source",
                    "the TEGR coefficient ray at leading two-derivative IR order",
                    "Cauchy support and inner-bundle typing inside the canonical physical realization without an extra support map",
                    "all nonlinear classical Einstein equations modulo boundary data",
                ],
                "open": [
                    "primitive MTT selection of the minimal-rootstack massless-helicity-two physical branch",
                    "the q79 gerbe branch, inverse Fourier-Mukai local freeness, and balanced HYM connection",
                    "a genuinely nonlocal same-branch extension of the closed flat-symbol root-plane/twisted-exterior J_DE functor satisfying the 11-row kernel/Ext1/Hessian contract, or the projected symmetric 2x2 TT Hessian block directly; ordinary dual/exterior HYM transport and autonomous C4/Lens descent in the current marked shared-circle setup are closed no-go, while an unmarked modular replacement has a separate 0-of-5 contract",
                    "primitive MTT selection of the canonical Lorentzian physical realization",
                    "kappa_h and Lambda_eff values",
                    "higher-derivative EFT coefficients and quantum/UV completion",
                ],
            },
            "part_G_canonical_pullback_metric_selection": {
                "input": (
                    "A bundle morphism Q_WW:TP->TI and the declared Euclidean inner "
                    "metric delta_I on TI."
                ),
                "universal_property": (
                    "G_Q(v,w)=delta_I(Q_WW v,Q_WW w) for all v,w in TP."
                ),
                "local_matrix": "G_Q=Q_WW^T Q_WW",
                "positivity": (
                    "If Q_WW is invertible, G_Q(v,v)=||Q_WW v||_I^2>0 for v!=0."
                ),
                "transition": (
                    "Q_j=g_I,ij Q_i g_P,ij^(-1) and orthogonality of g_I imply "
                    "G_j=(g_P,ij^(-1))^T G_i g_P,ij^(-1), the metric cocycle."
                ),
                "uniqueness": (
                    "The universal property fixes every bilinear value of G_Q, so no "
                    "second metric satisfying it exists. Any nonlinear f(Q^TQ) is extra "
                    "observable-source data, not the induced metric of Q."
                ),
                "parameter_count": 0,
                "result": (
                    "Given the selected Q_WW comparison field, the spatial metric "
                    "observable is canonically and uniquely Q_WW^*delta_I. The old "
                    "metric-observable-choice gate is closed."
                ),
                "remaining_boundary": (
                    "The q79/Z64 source map is now unique on the selected minimal-"
                    "rootstack massless-helicity-two branch. This theorem does not "
                    "make primitive MTT select that branch or the canonical Lorentzian "
                    "physical realization."
                ),
            },
            "part_H_selected_branch_source_factorization": {
                "source_map": source_factorization["theorem"]["selected_source_map"][
                    "local_formula"
                ],
                "factorization": source_factorization["theorem"]["factorization"],
                "uniqueness": source_factorization["theorem"]["uniqueness"]["result"],
                "parameter_count": 0,
                "result": (
                    "The old q79/Z64-to-Q_WW source-map gate is closed on the "
                    "selected massless-helicity-two minimal-rootstack branch. The "
                    "remaining primitive gate is branch selection, not matrix emission."
                ),
            },
            "part_I_conditional_HYM_Hessian_scalarization": {
                "canonical_complex_structure": "J_DE(d,e)=(-e,d)",
                "commutant_dimension_reduction": "6->2",
                "physical_block": "H_std=kappa_standard*I2",
                "root_independent_parent": "C4=<16>={0,16,32,48}; both odd Z64 roots restrict as i^m",
                "flat_symbol_functor": (
                    "E_S=det(E_D) tensor Lambda^2 E_D; the realified shared root "
                    "plane tensored with E_D induces J_DE globally and in parallel"
                ),
                "free_orbit_covariance": "CLOSED_NO_GO_AS_SINGLE_BRANCH_INVARIANCE",
                "direct_unital_Herm3_adjoint": "CLOSED_NO_GO_AS_FULL_SIX_DIMENSIONAL_JDE",
                "result": (
                    "If C4 is an autonomous Lens redundancy under which the HYM "
                    "operator descends, or a genuinely nonlocal same-branch "
                    "Fourier-Mukai autoequivalence extends the closed flat-symbol "
                    "outer functor and preserves its functional, then "
                    "h_DE=0 and h_DD=h_EE=kappa_standard>0 exactly."
                ),
                "remaining_boundary": (
                    "The root-independent C4 parent and its exact flat-symbol J_DE "
                    "functor are closed, but free-orbit covariance does not scalarize "
                    "one branch and no direct unital Herm(3) adjoint can realize full "
                    "J_DE. Ordinary dual/exterior HYM transport is also closed no-go: "
                    "it preserves D/S/K and flips nonzero c3. In the current marked "
                    "shared-circle setup C4 also exchanges the shared and twisted "
                    "directions, so autonomous Lens descent is closed no-go. The "
                    "nonlocal 11-row kernel/Ext1/Hessian contract or the actual block remains open."
                ),
            },
        },
        "claim_tiers": {
            "selected_candidate_source_factors_through_G_equal_QTQ": "CLOSED_EXACT",
            "orientation_fiber_dimension": "CLOSED_EXACT_THREE",
            "selected_candidate_orientation_source_coordinates": "CLOSED_ZERO",
            "strict_same_source_requires_orientation_fiber_neutrality": "CLOSED_CHARACTERIZATION",
            "strict_same_source_two_derivative_teleparallel_action": "CLOSED_UNIQUE_TEGR_RAY",
            "strict_same_source_nonlinear_metric_descent": "CLOSED_EXACT_MOD_BOUNDARY",
            "cauchy_support_typing_without_extra_source_map": "CLOSED_CONDITIONAL_ON_CANONICAL_PHYSICAL_REALIZATION",
            "inner_spatial_bundle_typing": "CLOSED_AUTOMATIC_FROM_INVERTIBLE_QWW",
            "leading_two_derivative_classical_GR_on_candidate_branch": "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY",
            "canonical_pullback_metric_given_QWW": "CLOSED_EXACT_UNIQUE",
            "metric_observable_choice_given_QWW": "CLOSED_NO_REMAINING_CHOICE",
            "selected_branch_q79_Z64_QWW_source_realization": "CLOSED_UNIQUE_UP_TO_GAUGE",
            "selected_branch_source_realization_fitted_parameters": "CLOSED_ZERO",
            "primitive_MTT_selects_candidate_metric_source_realization": "REDUCED_TO_PRIMITIVE_MINIMAL_ROOTSTACK_LORENTZIAN_BRANCH_SELECTION",
            "spectral_sheet_symbol_to_rootstack_strain_carrier": "CLOSED_EXACT",
            "strain_symbol_normalized_overlap_metric": "CLOSED_EXACT_IDENTITY",
            "literal_full_inverse_Fourier_Mukai_HYM_connection_identity": "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION",
            "actual_q79_inverse_Fourier_Mukai_visible_bundle": "OPEN_GERBE_AND_LOCAL_FREENESS",
            "actual_q79_balanced_HYM_connection": "OPEN",
            "canonical_complement_lane_complex_structure": "CLOSED_EXACT",
            "quarterturn_Hessian_scalarization": "CLOSED_EXACT",
            "physical_HYM_TT_block_scalarization": "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE",
            "shared_Z64_unique_order4_subgroup": "CLOSED_EXACT",
            "shared_Z64_odd_root_C4_restriction": "CLOSED_EXACT_ROOT_INDEPENDENT",
            "free_C4_orbit_covariance_scalarizes_branch_Hessian": "CLOSED_NO_GO",
            "autonomous_Lens_descent_scalarizes_Hessian": "CLOSED_EXACT_CONDITIONAL",
            "MTT_types_C4_as_Lens_redundancy": "CLOSED_NO_GO_IN_CURRENT_MARKED_SHARED_CIRCLE_SETUP_UNMARKED_REFORMULATION_OPEN",
            "marked_shared_circle_C4_autonomous_descent": "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING",
            "unmarked_modular_parent_descent_contract": "OPEN_5_ROWS_0_AVAILABLE",
            "square_theta_direct_adjoint_realizes_JDE": "CLOSED_NO_GO",
            "determinant_twisted_exterior_square_edge_identification": "CLOSED_EXACT",
            "shared_root_C4_to_flat_rootstack_strain_JDE_functor": "CLOSED_EXACT_ROOT_INDEPENDENT",
            "JDE_parallel_under_minimal_rootstack_flat_connection": "CLOSED_EXACT",
            "direct_unital_Herm3_adjoint_realizes_full_JDE": "CLOSED_NO_GO",
            "ordinary_dual_and_exterior_square_preserve_HYM": "CLOSED_EXACT_ON_TRACEFREE_SU3_SECTOR",
            "ordinary_dual_or_exterior_square_realizes_JDE": "CLOSED_NO_GO",
            "nonzero_c3_chiral_branch_complex_linear_self_duality": "CLOSED_NO_GO",
            "nonlocal_same_branch_Fourier_Mukai_kernel_contract": "OPEN_11_ROWS_2_TOPOLOGICAL_ROWS_AVAILABLE",
            "nontrivial_inverse_Fourier_Mukai_induced_JDE": "OPEN_EXTENSION_FROM_FLAT_SYMBOL_TO_ACTUAL_HYM",
            "typed_lane_quarterturn_to_FuYau_source_functor": "CLOSED_CONDITIONAL_AT_FLAT_SYMBOL_AND_FUYAU_PARENT_REPRESENTATION_TIER_ACTUAL_HYM_EXTENSION_OPEN",
            "selected_HYM_action_quarterturn_invariance": "OPEN",
            "dynamic_projected_HYM_TT_Hessian": "OPEN_ACTUAL_OPERATOR_CONDITIONAL_SCALAR_FORM_CLOSED",
            "primitive_MTT_selects_canonical_Lorentzian_realization": "OPEN_INPUT_IN_CURRENT_CORPUS",
            "numeric_kappa_h": "OPEN_ONE_EFFECTIVE_NORMALIZATION",
            "Lambda_eff": "OPEN",
            "higher_derivative_and_quantum_completion": "OPEN",
        },
        "guardrails": {
            "claims_primitive_MTT_uniquely_selects_current_metric_source": False,
            "claims_primitive_MTT_derives_Y4_without_physical_realization_input": False,
            "claims_all_teleparallel_theories_are_TEGR": False,
            "claims_higher_derivative_terms_are_absent": False,
            "claims_numeric_Newton_constant": False,
            "claims_full_nonzero_Chern_HYM_connection_equals_flat_rootstack_connection": False,
            "claims_dynamic_projected_HYM_Hessian_computed": False,
            "claims_abstract_quarterturn_match_is_typed_FuYau_source_functor": False,
            "claims_free_C4_orbit_covariance_scalarizes_one_branch": False,
            "claims_direct_square_theta_adjoint_realizes_JDE": False,
            "claims_flat_symbol_JDE_functor_is_actual_inverse_Fourier_Mukai_HYM_functor": False,
            "claims_direct_unital_Herm3_adjoint_can_realize_full_JDE": False,
            "claims_ordinary_dual_or_exterior_square_realizes_JDE": False,
            "claims_opposite_chirality_dual_branch_is_same_selected_branch": False,
            "claims_derived_equivalence_automatically_preserves_HYM_Hessian": False,
            "claims_unmarked_modular_parent_preserves_marked_shared_circle": False,
            "claims_shared_circle_c3_clutching_is_C4_equivariant": False,
            "claims_MTT_types_C4_as_Lens_redundancy": False,
            "claims_selected_HYM_action_quarterturn_invariance": False,
            "claims_Lambda_eff_selected": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Strict Same-Source Teleparallel Selection Theorem v1

Date: 2026-07-15

## Result

The remaining teleparallel-neutrality clause closes exactly for the current
strict same-source candidate branch. It does not require a new fitted number or
an independent gravitational axiom.

The displayed source packet is

```text
psi -> S(psi) -> Q(psi)=exp S(psi) -> G(psi)=Q(psi)^T Q(psi).
```

Its selected-branch provenance is now explicit rather than assumed. On the
minimal full-monodromy q79 root stack,

```text
Phi_q79(psi)=<c2,psi>(1/sqrt(2),-1/sqrt(2),0;0,0,0)
             +<s2,psi>(0,0,0;0,0,1),
S=J Phi_q79(psi).
```

The first vector is the rank-two trace-zero shape lane and the second is the
rank-three shear lane. Helicity two fixes the `Z64` plane, the natural q79 map
fixes its preimage, `Q_WW=exp(S)` fixes the positive polar representative, and
pullback fixes the metric. Thus this source realization is unique up to
polarization, frame, and diffeomorphism gauge on the selected branch, with no
fitted physical parameter.

It contains symmetric strain coordinates and no skew/orientation source
coordinate. The metric quotient

```text
r(Q)=Q^T Q
```

has differential

```text
Dr_I[dQ]=dQ^T+dQ.
```

The exact Jacobian has rank six and a three-dimensional kernel, precisely
`so(3)`. Thus the three left-orientation directions are the fiber erased by the
selected candidate observable.

The metric formula itself is now selected exactly once `Q_WW` is supplied. The
inner bundle already has its declared Euclidean metric `delta_I`, and

```text
G_Q(v,w)=delta_I(Q_WW v,Q_WW w)
```

is the pullback metric. This universal property uniquely fixes every bilinear
value, has local matrix `Q_WW^T Q_WW`, is positive on the invertible branch,
and obeys the correct metric transition law. Any nonlinear replacement
`f(Q_WW^T Q_WW)` requires an additional observable rule and is not the induced
metric of the comparison field. Thus the old "which metric observable?" gate
is closed given `Q_WW`. The old "which q79/Z64-to-Q_WW map?" gate is also
closed on the selected massless-helicity-two minimal-rootstack branch. What
remains is primitive MTT selection of that physical branch and the dynamic
spectral-HYM calculation. The root-stack carrier is now exactly the
real-symmetric sheet/Weyl symbol of three spectral eigenlines, with normalized
overlap `I6`. It is not the full visible HYM connection: for a nonzero-Chern
realization such as conditional `c2=9`, literal equality with the flat
root-stack connection is topologically impossible. The honest operator target
is the projected symmetric block `H_std`. Its abstract symmetry problem is now
solved. The unique positive sheet-to-opposite-edge complement defines
`J_DE(d,e)=(-e,d)`, with `J_DE^2=-I6` and exact `S3` equivariance. If the
selected HYM functional carries that same typed quarter-turn, its physical
block is forced to

```text
H_std=kappa_standard I2,
h_DE=0,
h_DD=h_EE=kappa_standard>0.
```

The Fu-Yau four-branch Chern orbit carries the same abstract order-four matrix,
and the shared `Z64` now supplies its unique root-independent parent
`C4=<16>={0,16,32,48}`. Both odd roots restrict as `i^m`. A single Fu-Yau
Chern branch is ruled out, but the four-branch parent alone is not enough:
free-orbit covariance admits a six-parameter family
`H_m=J_DE^m H_0 J_DE^-m`, so covariance is not one-branch invariance.

If the four orientations are autonomous Lens redundancy and the HYM operator
descends, scalarization follows conditionally. The obvious direct theta-space
shortcut has also been tested: `U_theta=diag(-1,i,1)` on the square cubic gives
only a four-dimensional `J^2=-1` sector on `Herm(3)` and mixes `D+S` into `K`.
It therefore cannot realize the six-dimensional `J_DE` in any basis.

The nontrivial functor is now constructed at the flat-symbol tier. Since
`Lambda^2 E_D=sign tensor E_D`, twisting by the shared SpinC determinant sign
gives the unordered-edge bundle `E_S`. Tensoring `E_D` with the realified odd-
root `C4` plane and using the unique positive opposite-edge map induces exactly
`J_DE=[[0,-I3],[I3,0]]`. It is global and parallel on the minimal root-stack
sheet symbol. No direct unital Herm(3) adjoint can replace it because such an
adjoint fixes the identity while `J_DE` sends trace to edge-sum. What remains
cannot be supplied by ordinary bundle duality or exterior square. Those
functors preserve the `SU(3)` HYM equation, but their exact action preserves
`D`, `S`, and `K` separately and squares as an involution rather than the
quarter-turn. Duality also flips `c3`, so it exchanges opposite-chirality
branches instead of acting within one nonzero-`c3` branch. The surviving
extension is a genuinely nonlocal same-branch Fourier-Mukai autoequivalence
obeying the emitted 11-row kernel/`Ext1`/Hessian contract (currently `2/11`),
or direct computation of the projected HYM block.

The shared-circle marking also closes the apparent Lens shortcut for the
current topology. In the vertical basis `(twisted, shared)`, the quarter-turn
sends the marked shared direction to the twisted direction. Its marked
stabilizer has no order-four element, and the existing `c3=+/-6` construction
clutches specifically along `S1_shared`. Autonomous Lens descent is therefore
a no-go in the marked realization. An unmarked modular replacement would have
to rederive five absent marking, clutching, HYM, and Hessian rows.

Foundation v8's autonomous-descent theorem is an if-and-only-if statement: a
reduced autonomous law exists exactly when the microscopic law is constant
after projection on each reduction fiber. Therefore a strict same-source
gravitational completion of the displayed `G` packet must be neutral on the
orientation fiber. Giving that fiber a bulk kinetic term would add an
orientation/connection source absent from the packet and would define a larger
modified-teleparallel theory instead.

## Exact coefficient selection

For

```text
T_c=c1 I1+c2 I2+c3 I3,
```

the certified pure-frame calculation gives

```text
2c1+c2+c3=0,
-4c1+2c2=0.
```

The constraint matrix has rank two, so its unique ray is

```text
(c1,c2,c3)=lambda(1/4,1/2,-1).
```

This is TEGR. Its pure-frame residual is zero, and

```text
e R(LC)=-e T_TEGR+2 partial_mu(e T^mu)
```

proves nonlinear metric descent modulo the boundary term. Hence the leading
parity-even two-derivative action on this strict same-source branch is exactly
Einstein-Hilbert/TEGR. The overall `kappa_h` and `Lambda_eff` remain values to
select; there is no additional dimensionless torsion parameter.

## Support typing

Inside the already declared canonical physical realization, `Y4` is globally
hyperbolic. If `Q_WW` is to be a local spatial source without introducing a new
support or pullback map, strict same-source typing places its base on an
oriented Cauchy slice `B=Sigma3` up to diffeomorphism and sets `TP=TB`. On the
invertible branch, `Q_WW:TB->TI` identifies `TI` automatically. The lapse and
shift remain constraint fields, and different Cauchy charts are gauge rather
than fitted data.

## Exact boundary of the claim

Closed:

- the q79/`Z64`-to-`Q_WW` source factorization on the selected massless-
  helicity-two minimal-rootstack branch, uniquely up to gauge;
- orientation neutrality for a strict completion of the displayed metric
  source;
- the unique TEGR coefficient ray;
- nonlinear classical Einstein equivalence modulo boundary data;
- Cauchy and bundle typing inside the canonical physical realization without
  an extra support map.

Still open:

- primitive MTT selection of the minimal-rootstack massless-helicity-two
  physical branch;
- the q79 gerbe branch, inverse Fourier-Mukai local freeness, and balanced HYM;
- a genuinely nonlocal same-branch Fourier-Mukai extension of the closed
  flat-symbol root-plane/twisted-exterior `J_DE` functor satisfying the 11-row
  kernel/`Ext1`/Hessian contract (currently `2/11`), or direct calculation of
  the projected operator; ordinary dual/exterior HYM transport and autonomous
  Lens descent in the current marked shared-circle setup are closed no-go;
- primitive selection of the canonical Lorentzian realization itself;
- numerical `kappa_h` and `Lambda_eff`;
- higher-derivative coefficients and quantum/UV completion.

So the action-form problem is closed on the current strict same-source branch.
The remaining classical selection problem is now upstream: select this branch
and its two dimensionful values, rather than search again for a gravitational
coefficient vector.
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"status": cert["status"], "certificate": str(OUT_CERT)}, indent=2))


if __name__ == "__main__":
    main()
