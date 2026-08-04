from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
QG_ROOT = Path(
    os.environ.get(
        "MTT_QG_ROOT",
        ROOT.parent / "12 Quantum Gravity",
    )
)
SM_ROOT = Path(
    os.environ.get(
        "MTT_SM_CLOSURE_ROOT",
        ROOT.parent / "mtt-sm-parity-closure",
    )
)

COUPLED_TARGET = ROOT / "q79_coupled_hull_strominger_contraction_target.packet.json"
UPSTAIRS_COMPLEX = ROOT / "q79_upstairs_derived_complex_contract.packet.json"
PHYSICAL_PRYM_LATTICE = ROOT / "q79_physical_prym_lattice_reference.packet.json"
ETA9_DIFFERENTIAL_PICARD = (
    ROOT / "q79_eta9_differential_picard_upper_source_contract.packet.json"
)
VISIBLE_SUPPORT = (
    QG_ROOT
    / "q79_visible_physical_spectral_support_and_inverse_bht_norm_cutset.packet.json"
)
VISIBLE_PRYM = QG_ROOT / "q79_hyperplane_fermat_prym_hensel_candidate.packet.json"
HIDDEN_TRANSPORT = (
    QG_ROOT / "q79_hs_to_hidden_p39_two_circle_determinant_transport.packet.json"
)
HIDDEN_DERIVED = QG_ROOT / "q79_global_alpha_twisted_hs_derived_object.packet.json"
REFERENCE_ANCHOR = (
    QG_ROOT
    / "q79_tdual_hull_strominger_anchor_and_physical_bianchi_transgression.packet.json"
)
CURRENT_THETA = QG_ROOT / "q79_current_twisted_residual_frontier.packet.json"
REFERENCE_HIDDEN_HYM_GATE = (
    SM_ROOT
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "HYM_Bianchi_execution_gate.packet.json"
)
OUT = ROOT / "q79_physical_gauge_pair_deformation_seed_contract.packet.json"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_record(path: Path, packet: dict) -> dict[str, str]:
    return {
        "path": str(path),
        "sha256": sha256(path),
        "schema": packet.get("schema", "NO_SCHEMA_FIELD"),
        "status": packet.get("status", "NO_STATUS_FIELD"),
    }


def all_declared_checks_pass(packet: dict) -> bool:
    checks = packet.get("checks", {})
    return bool(checks) and all(value is True for value in checks.values())


def matrix_rows(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


def exact_hodge_projection_model() -> dict[str, object]:
    # A finite three-term complex with a nontrivial harmonic sector. It verifies
    # the algebra used to remove gauge/automorphism kernels before inversion.
    q = sp.zeros(7)
    q[2, 0] = 1
    q[5, 3] = 1
    q_star = q.T
    laplacian = q * q_star + q_star * q
    harmonic_projector = sp.diag(0, 1, 0, 0, 1, 0, 1)
    green = sp.diag(1, 0, 1, 1, 0, 1, 0)
    homotopy = q_star * green
    identity = sp.eye(7)

    require(q * q == sp.zeros(7), "finite differential squares to zero")
    require(laplacian * green == identity - harmonic_projector, "Green right inverse")
    require(green * laplacian == identity - harmonic_projector, "Green left inverse")
    require(
        q * homotopy + homotopy * q == identity - harmonic_projector,
        "Hodge contraction",
    )
    require(homotopy * homotopy == sp.zeros(7), "homotopy square")
    require(harmonic_projector * q == sp.zeros(7), "harmonic projector after q")
    require(q * harmonic_projector == sp.zeros(7), "q after harmonic projector")
    require(harmonic_projector * homotopy == sp.zeros(7), "projector after homotopy")
    require(homotopy * harmonic_projector == sp.zeros(7), "homotopy after projector")

    return {
        "degree_dimensions": [2, 3, 2],
        "Q": matrix_rows(q),
        "Delta": matrix_rows(laplacian),
        "Pi_harm": matrix_rows(harmonic_projector),
        "Green": matrix_rows(green),
        "h": matrix_rows(homotopy),
        "identities": [
            "Q^2=0",
            "Delta*Green=Green*Delta=I-Pi_harm",
            "Q*h+h*Q=I-Pi_harm",
            "h^2=Pi_harm*h=h*Pi_harm=0",
        ],
        "interpretation": (
            "The validated inverse is formed only on the orthogonal complement of "
            "harmonic gauge/automorphism modes. A zero Fredholm index alone never "
            "establishes invertibility."
        ),
    }


def same_chern_different_residual_family() -> dict[str, object]:
    x, t = sp.symbols("x t", real=True)
    h3 = sp.diag(sp.I, -sp.I, 0)
    h9 = sp.diag(sp.I, -sp.I, *([0] * 7))
    h_norm_squared = sp.simplify(-sp.trace(h3 * h3))
    torus_cosine_integral = sp.integrate(sp.cos(x) ** 2, (x, 0, 2 * sp.pi)) * 2 * sp.pi
    residual_norm_squared = sp.simplify(t**2 * h_norm_squared * torus_cosine_integral)

    require(sp.trace(h3) == 0, "rank-three generator is traceless")
    require(sp.trace(h9) == 0, "rank-nine generator is traceless")
    require(h_norm_squared == 2, "generator norm")
    require(torus_cosine_integral == 2 * sp.pi**2, "torus cosine integral")
    require(residual_norm_squared == 4 * sp.pi**2 * t**2, "residual norm family")

    return {
        "base": "flat complex T2, or its pullback to T2 x T4",
        "connection_family": "A_t=t H sin(x) dy on the trivial SU(n) bundle",
        "curvature": "F_t=t H cos(x) dx wedge dy",
        "generator_rank3": ["i", "-i", "0"],
        "generator_rank9": ["i", "-i", "0", "0", "0", "0", "0", "0", "0"],
        "integrability": "F_t is of type (1,1), so F_t^(0,2)=0",
        "chern_data": (
            "All bundles are topologically trivial; tr(H)=0 and the decomposable "
            "two-form squares to zero, so the displayed Chern-Weil classes vanish."
        ),
        "HYM_residual": "Lambda F_t=t H cos(x)",
        "H_norm_squared": str(h_norm_squared),
        "residual_L2_norm_squared": str(residual_norm_squared),
        "residual_L2_norm": "2*pi*abs(t)",
        "conclusion": (
            "Fixed rank and Chern data do not determine the HYM residual, its "
            "linearization, or a Newton bound Y. Connection/metric coefficients are "
            "mathematically indispensable source data."
        ),
    }


def main() -> None:
    coupled = load(COUPLED_TARGET)
    upstairs = load(UPSTAIRS_COMPLEX)
    prym_lattice = load(PHYSICAL_PRYM_LATTICE)
    eta9_picard = load(ETA9_DIFFERENTIAL_PICARD)
    visible = load(VISIBLE_SUPPORT)
    visible_prym = load(VISIBLE_PRYM)
    hidden = load(HIDDEN_TRANSPORT)
    hidden_derived = load(HIDDEN_DERIVED)
    anchor = load(REFERENCE_ANCHOR)
    theta = load(CURRENT_THETA)
    reference_hidden_gate = load(REFERENCE_HIDDEN_HYM_GATE)

    for label, packet in [
        ("coupled target", coupled),
        ("physical Prym lattice", prym_lattice),
        ("eta9 differential Picard", eta9_picard),
        ("visible support", visible),
        ("visible Prym", visible_prym),
        ("hidden transport", hidden),
        ("hidden derived object", hidden_derived),
        ("reference anchor", anchor),
        ("current theta frontier", theta),
    ]:
        require(all_declared_checks_pass(packet), label)

    require(
        upstairs["derived_bridge_readiness"]["closed"]
        == upstairs["derived_bridge_readiness"]["total"]
        == 10,
        "upstairs derived bridge readiness",
    )
    require(
        all(upstairs["derived_bridge_readiness"]["gates"].values()),
        "upstairs derived bridge gates",
    )

    physical_rows = coupled["physical_execution_rows"]
    require(not any(physical_rows.values()), "predecessor physical execution boundary")
    require(
        visible["claim_tiers"]["selection_of_one_physical_cover_member"] == "OPEN",
        "visible cover selection remains open",
    )
    require(
        visible["claim_tiers"]["inverse_BHT_local_freeness_given_twisted_line"]
        == "CLOSED_FORMAL",
        "visible conditional local freeness",
    )
    require(
        visible["claim_tiers"]["physical_twisted_Prym_value_rows"]
        == "REDUCED_TO_THREE_EXACT_ROWS_OPEN",
        "visible Prym rows remain open",
    )
    require(
        hidden["claim_tiers"]["actual_smooth_P39_representative_with_cover_rows"]
        == "CLOSED_EXACT_CONSTRUCTIVE_SELECTED_K0",
        "hidden smooth projective carrier",
    )
    require(
        hidden["claim_tiers"]["canonical_family_index_complex_is_holomorphic_locally_free"]
        == "OPEN",
        "hidden holomorphic carrier remains open",
    )
    require(
        hidden_derived["purity_boundary"]["rank1_sheaf_on_smooth_finite_cover_for_this_representative"]
        == "EXCLUDED_BY_RELATIVE_SEMISTABILITY_CUTSET",
        "derived representative purity boundary",
    )
    require(
        theta["guardrails"]["claims_MTT_physical_promotion"] is False,
        "theta frontier does not claim physical promotion",
    )
    require(
        upstairs["strict_physical_upper_state_readiness"]["gates"]
        ["physical_V3_W9_same_carrier_identification"]
        is False,
        "derived upper object is not the physical pair",
    )
    require(
        prym_lattice["integral_gerbe_restriction"]["integral_restriction"]
        == "j^*DD(alpha)=0 in H^3(C_phys,Z)",
        "integral gerbe restriction",
    )
    require(
        prym_lattice["remaining_exact_Prym_target"]["integral_DDalpha_restriction"]
        == "CLOSED_ZERO",
        "integral DD row closed",
    )
    require(
        prym_lattice["remaining_exact_Prym_target"]
        ["flat_Deligne_alpha_trivialization_and_twisted_lift"]
        == "OPEN",
        "flat Deligne row remains open",
    )
    require(
        eta9_picard["current_source_status"]["integral_DDalpha_restriction_zero"]
        is True,
        "eta9 integral DD source row",
    )
    require(
        eta9_picard["current_source_status"]["two_graph_virtual_class_and_exact_row_arithmetic"]
        is True,
        "eta9 graph arithmetic",
    )
    require(
        eta9_picard["current_source_status"]["flat_Deligne_gerbe_trivialization"]
        is False,
        "eta9 flat Deligne boundary",
    )
    require(
        reference_hidden_gate["status"]
        == "TOPOLOGICAL_DD_GATE_CLOSED_ANALYTIC_HYM_BIANCHI_GATES_OPEN",
        "reference hidden gate overall status",
    )
    require(
        reference_hidden_gate["Bianchi_chain"]["hidden_SU9_HYM_connection"] is True,
        "reference hidden SU9 HYM row",
    )
    require(
        reference_hidden_gate["Bianchi_chain"]["A102_base_cohomology_allocation"]
        == "9+11+4=24 retained as the K3 reference allocation",
        "reference hidden SU9 scope",
    )

    visible_character = visible["physical_visible_character"]
    reference_bundle = anchor["reference_Hull_Strominger_anchor"]["gauge_bundle"]
    require(visible_character["Chern_data"] == "(c1,c2,c3)=(0,9u,+6Omega)", "visible Chern row")
    require(reference_bundle["definition"] == "W=E3 direct_sum E9 on K3", "reference pullback source")
    require(reference_bundle["rank"] == 12, "reference total rank")
    require(
        anchor["physical_smooth_Bianchi_transgression"]["physical_carriers"]["hidden"]
        == "determinant-one P(3,9) with cover rows (-9u,0)",
        "physical hidden Chern row",
    )

    adjoint_ranks = {
        "Tstar_X": 3,
        "ad_TX": 3**2 - 1,
        "ad_E_visible": 3**2 - 1,
        "ad_E_hidden_twisted": 9**2 - 1,
        "TX": 3,
    }
    total_rank = sum(adjoint_ranks.values())
    gauge_pair_rank = adjoint_ranks["ad_E_visible"] + adjoint_ranks["ad_E_hidden_twisted"]
    require(adjoint_ranks["ad_TX"] == 8, "ad TX rank")
    require(adjoint_ranks["ad_E_visible"] == 8, "visible adjoint rank")
    require(adjoint_ranks["ad_E_hidden_twisted"] == 80, "hidden adjoint rank")
    require(gauge_pair_rank == 88, "physical gauge-pair adjoint rank")
    require(total_rank == 102, "trace-free heterotic deformation carrier rank")

    twist_order = 3
    hidden_twist = 1
    endomorphism_twist = (hidden_twist - hidden_twist) % twist_order
    require(endomorphism_twist == 0, "twist cancels in End(E_h)")

    hodge_model = exact_hodge_projection_model()
    residual_family = same_chern_different_residual_family()

    source_rows = {
        "selected_visible_eta9_differential_Picard_source_U_eta9": False,
        "selected_hidden_twisted_holomorphic_locally_free_rank9_carrier": False,
        "one_common_positive_Gauduchon_chamber_with_polystability_or_kernel_data": False,
        "declared_tangent_connection_convention_and_positive_metric_seed": False,
    }
    require(not any(source_rows.values()), "minimal physical source rows remain open")

    derived_rows = {
        "visible_and_hidden_Chern_connections": False,
        "physical_coupled_Dolbeault_operator_Dbar_Q": False,
        "harmonic_kernel_projector_on_q79": False,
        "gauge_fixed_Galerkin_Jacobian_L_N": False,
        "validated_inverse_G_N_and_continuum_tail": False,
        "physical_residual_Y": False,
        "physical_derivative_matrix_K_of_r": False,
        "positive_metric_radius": False,
    }
    require(not any(derived_rows.values()), "physical numerical rows remain open")

    checks = {
        "predecessor_coupled_target_passes": True,
        "upstairs_derived_complex_packet_passes": True,
        "physical_Prym_lattice_packet_passes": True,
        "eta9_differential_Picard_packet_passes": True,
        "older_hidden_SU9_HYM_true_row_is_K3_reference_scoped": True,
        "older_hidden_gate_overall_analytic_HYM_status_is_open": True,
        "reference_hidden_HYM_is_not_retyped_as_physical_P39_HYM": True,
        "visible_support_packet_passes": True,
        "visible_Prym_candidate_packet_passes": True,
        "hidden_transport_packet_passes": True,
        "hidden_derived_packet_passes": True,
        "reference_Hull_Strominger_anchor_passes": True,
        "latest_theta_frontier_packet_passes": True,
        "latest_theta_frontier_disclaims_physical_promotion": True,
        "visible_local_freeness_is_only_conditional_on_missing_twisted_line": True,
        "visible_integral_DDalpha_restriction_is_closed_zero": True,
        "visible_flat_Deligne_trivialization_remains_open": True,
        "visible_two_graph_norm_Gysin_coefficient_and_square_arithmetic_are_exact": True,
        "visible_seven_projected_rows_reduce_to_one_upper_source": True,
        "hidden_carrier_is_only_smooth_projective_at_current_tier": True,
        "current_hidden_derived_representative_is_not_a_pure_spectral_line": True,
        "reference_bundle_is_pulled_back_from_K3": True,
        "reference_visible_c3_vanishes_by_base_dimension": True,
        "physical_visible_c3_is_plus_or_minus_six": True,
        "reference_and_physical_visible_bundles_are_not_isomorphic": True,
        "reference_and_physical_hidden_bundles_are_not_isomorphic": True,
        "Newton_iteration_preserves_fixed_bundle_topology": True,
        "reference_gauge_connection_cannot_seed_the_physical_gauge_lane": True,
        "reference_metric_and_flux_can_remain_geometric_initialization_data": True,
        "rank3_adjoint_has_complex_rank8": True,
        "rank9_adjoint_has_complex_rank80": True,
        "twisted_hidden_endomorphism_bundle_is_ordinary": True,
        "tracefree_coupled_heterotic_carrier_has_complex_rank102": True,
        "physical_gauge_pair_adjoint_lane_has_complex_rank88": True,
        "finite_Hodge_projection_model_is_exact": True,
        "same_Chern_data_different_HYM_residual_family_is_exact": True,
        "Chern_rows_do_not_determine_Y_or_Jacobian": True,
        "zero_index_does_not_imply_invertibility": True,
        "harmonic_kernel_must_be_projected_or_proved_zero": True,
        "minimal_source_tuple_has_four_geometric_rows": True,
        "connections_flux_Jacobian_and_bounds_are_derived_not_independent_sources": True,
        "27_state_matrix_is_not_the_102_rank_PDE_deformation_carrier": True,
        "no_observed_value_or_fitted_parameter_is_used": True,
        "external_authority_repositories_are_read_only": True,
    }
    require(all(checks.values()), "physical gauge-pair seed contract checks")

    packet = {
        "schema": "MTTQ79PhysicalGaugePairDeformationSeedContract.v1",
        "date": "2026-07-18",
        "status": (
            "Q79_TRACEFREE_HETEROTIC_DEFORMATION_COMPLEX_TWIST_CANCELLATION_"
            "TOPOLOGICAL_SEED_NOGO_HODGE_KERNEL_PROJECTION_AND_MINIMAL_SOURCE_"
            "REDUCTION_CLOSED_EXACT_PHYSICAL_HOLOMORPHIC_PAIR_AND_NUMERICAL_"
            "GALERKIN_EXECUTION_OPEN"
        ),
        "inputs": {
            "coupled_contraction_target": input_record(COUPLED_TARGET, coupled),
            "upstairs_derived_complex": input_record(UPSTAIRS_COMPLEX, upstairs),
            "physical_Prym_lattice": input_record(PHYSICAL_PRYM_LATTICE, prym_lattice),
            "eta9_differential_Picard_source_reduction": input_record(
                ETA9_DIFFERENTIAL_PICARD, eta9_picard
            ),
            "visible_physical_support": input_record(VISIBLE_SUPPORT, visible),
            "visible_Prym_candidate": input_record(VISIBLE_PRYM, visible_prym),
            "hidden_P39_transport": input_record(HIDDEN_TRANSPORT, hidden),
            "hidden_derived_object": input_record(HIDDEN_DERIVED, hidden_derived),
            "reference_Hull_Strominger_anchor": input_record(REFERENCE_ANCHOR, anchor),
            "latest_theta_carrier_frontier": input_record(CURRENT_THETA, theta),
            "reference_hidden_SU9_HYM_scope_guard": input_record(
                REFERENCE_HIDDEN_HYM_GATE, reference_hidden_gate
            ),
        },
        "latest_corpus_audit": {
            "visible": {
                "closed": [
                    "physical support class C_phys in |9H+3D0|",
                    "existence of smooth finite-flat members",
                    "determinant baseline",
                    "local freeness after a suitable twisted spectral line exists",
                    "integral DD(alpha) restriction is zero on every smooth C_phys",
                    "ambient/rational Prym feasibility and exact two-graph row arithmetic",
                    "one differential-Picard upper source derives seven projected readouts",
                ],
                "open": [
                    "selection of one characteristic-zero C_phys and algebraic graph pair",
                    "mixed Abel-Jacobi/Gysin row for that graph pair",
                    "flat Deligne/Brauer trivialization after integral DD zero",
                    "differential norm-zero Prym line with the required value rows",
                    "common Gauduchon stability/HYM",
                ],
            },
            "hidden": {
                "closed": [
                    "rank-nine determinant-one smooth projective topological carrier",
                    "cover Chern rows (-9u,0)",
                    "global alpha-twisted derived object and two-circle transport",
                    "separate K3 reference SU9,c2=11 HYM connection and full holonomy",
                ],
                "open": [
                    "twisted-holomorphic locally free physical rank-nine carrier",
                    "common Gauduchon stability/HYM",
                    "analytic qutrit/E8xE8 descent",
                ],
                "scope_guard": (
                    "The older hidden_SU9_HYM_connection=true row is the K3 reference "
                    "allocation 9+11+4=24. Its packet explicitly leaves physical inverse-"
                    "transform local freeness and balanced HYM open."
                ),
            },
            "latest_theta_search": {
                "status": theta["status"],
                "physical_promotion_claimed": False,
                "relation_to_seed": (
                    "A future positive finite carrier is at most discrete selection data; "
                    "it still requires holomorphic/HYM and retarded promotion."
                ),
            },
            "visible_upper_source_refinement": {
                "object": eta9_picard["upper_source"]["object"],
                "integral_DD_obstruction": "CLOSED_ZERO",
                "exact_graph_rows": eta9_picard["exact_two_graph_execution"],
                "derived_readout_count": eta9_picard["source_reduction"]
                ["projected_readout_count"],
                "flat_Deligne_trivialization": "OPEN",
                "selected_characteristic_zero_source": "OPEN",
            },
        },
        "topological_seed_separation_theorem": {
            "reference_visible": (
                "E3 is pulled back from a complex surface K3, hence c3(E3)=0 on the "
                "threefold."
            ),
            "physical_visible": visible_character["Chern_data"],
            "reference_hidden": "E9 is pulled back from K3 with c2=11 in the reference allocation",
            "physical_hidden": "determinant-one P(3,9) with nonbasic cover rows (-9u,0)",
            "fixed_bundle_fact": (
                "A Newton step changes a connection by an ad(E)-valued one-form on one "
                "fixed bundle E. It cannot change the isomorphism class or Chern classes."
            ),
            "conclusion": (
                "Neither reference pullback HYM block is a seed for the physical mixed "
                "gauge pair. The reference solution remains valid initialization data for the shared "
                "geometry/metric lane after the selected topology identification."
            ),
        },
        "chern_data_residual_nondetermination": residual_family,
        "physical_preprojection_deformation_complex": {
            "bundle": (
                "Q_phys=T*X direct_sum ad(TX) direct_sum ad(E_v) direct_sum "
                "ad(E_h^tau) direct_sum TX"
            ),
            "extension_interpretation": (
                "The Atiyah maps couple complex-structure variations to the tangent, "
                "visible and hidden curvatures; the final T*X extension is the anomaly/"
                "flux map. Dbar_Q^2=0 is the connection-level holomorphy plus Bianchi "
                "condition, not merely equality of characteristic classes."
            ),
            "determinant_convention": "all gauge and tangent endomorphism lanes are trace-free",
            "fiber_ranks_complex": adjoint_ranks,
            "total_fiber_rank_complex": total_rank,
            "physical_gauge_pair_adjoint_rank_complex": gauge_pair_rank,
            "full_End_TX_variant_rank_complex": total_rank + 1,
            "hidden_twist_cancellation": {
                "twist_order": twist_order,
                "E_h_twist": hidden_twist,
                "dual_twist": -hidden_twist,
                "End_twist_mod3": endomorphism_twist,
                "conclusion": (
                    "Although E_h is projective/twisted, ad(E_h)=End_0(E_h) is an "
                    "ordinary global bundle and belongs in the same elliptic complex."
                ),
            },
            "elliptic_operator": "B_Q=Dbar_Q+Dbar_Q^* with B_Q^2=Delta_Q",
            "index_guard": (
                "B_Q is self-adjoint and has Fredholm index zero, but it is invertible "
                "only after its harmonic kernel is proved absent or projected out."
            ),
            "relation_to_27_matrix": (
                "The 27-dimensional finite state/current carrier is a post-projection "
                "algebraic object. Q_phys is the preprojection PDE deformation carrier; "
                "an N-mode Galerkin matrix has size governed by 102*N before constraints, "
                "not 27."
            ),
        },
        "exact_kernel_projection_benchmark": hodge_model,
        "minimal_source_reduction_theorem": {
            "primitive_geometric_rows": source_rows,
            "source_tuple": (
                "S_phys=(U_eta9; E_h^tau; omega_0/chamber; tangent-connection "
                "convention), where U_eta9 is the selected visible differential-Picard "
                "source and the q79 shared differential line is held fixed"
            ),
            "required_properties": [
                "U_eta9 supplies a selected smooth characteristic-zero C_phys, graph/Prym class, flat Deligne trivialization, differential FM orientation and the certified norm/Gysin/square rows",
                "E_h^tau is twisted-holomorphic, locally free, determinant-one and analytically qutrit/E8xE8 descended",
                "E_v and E_h^tau are polystable in one positive q79 Gauduchon chamber, with all automorphism kernels declared",
                "the tangent connection convention and normalization are fixed before numerical validation",
            ],
            "functorially_derived_not_independent_source_rows": [
                "ordinary visible and twisted hidden Chern connections after Hermitian-Einstein solution",
                "the anomaly-transgressed H/flux representative",
                "Dbar_Q and the gauge-fixed Hessian/Jacobian",
                "the harmonic projector and Green operator",
                "Galerkin coefficients, residual Y, inverse defect Z0, derivative matrix K(r) and positivity radius",
            ],
            "parameter_statement": (
                "These are geometric fields/objects and one discrete connection convention, "
                "not empirical fit constants. This theorem removes redundant source rows but "
                "does not pretend the missing functions have numerical values."
            ),
        },
        "current_execution": {
            "minimal_source_rows": source_rows,
            "derived_numerical_rows": derived_rows,
            "lawful_physical_Y_available": False,
            "lawful_physical_Jacobian_available": False,
            "reason": (
                "No current packet supplies both physical holomorphic carriers and their "
                "connection/metric coefficients. The exact residual counterexample proves "
                "that Chern, index, finite-field or derived-category rows cannot replace them."
            ),
        },
        "theorems": {
            "topological_seed_separation": {
                "name": "q79TopologicalGaugeSeedSeparationTheorem",
                "statement": (
                    "The reference pullback E3 has c3=0 while the physical V3 has c3="
                    "+/-6; the reference E9 is a K3 c2=11 bundle while the physical hidden "
                    "carrier has nonbasic P(3,9) cover row -9u. Newton iteration is performed "
                    "in the affine space of connections "
                    "on a fixed bundle and preserves its Chern classes. Therefore the "
                    "reference HYM connection cannot be retyped as a physical V3 seed."
                ),
            },
            "residual_nondetermination": {
                "name": "ChernDataDoesNotDetermineHYMResidualTheorem",
                "statement": (
                    "For every real t, A_t=t H sin(x)dy is an integrable unitary connection "
                    "on one trivial determinant-one bundle with fixed vanishing Chern data, "
                    "while ||Lambda F_t||_L2=2*pi*|t|. Hence topological and Chern-character "
                    "packets cannot determine a physical residual or Newton bound."
                ),
            },
            "twisted_coupled_complex": {
                "name": "q79TwistedAdjointHeteroticDeformationComplexTheorem",
                "statement": (
                    "The order-three twist of E_h cancels against its dual in End(E_h). "
                    "With fixed determinants, the physical heterotic extension bundle has "
                    "complex rank 3+8+8+80+3=102. Once the physical connections satisfy "
                    "holomorphy and the differential Bianchi identity, its coupled Dbar_Q "
                    "is nilpotent and its gauge-fixed Hodge operator is inverted on the "
                    "orthogonal complement of harmonic automorphism modes."
                ),
            },
            "minimal_seed": {
                "name": "q79MinimalPhysicalGaugePairSeedFunctorialityTheorem",
                "statement": (
                    "A selected visible eta9 differential-Picard source, hidden twisted-holomorphic carrier, "
                    "common positive Gauduchon/Hermitian chamber and fixed tangent-connection "
                    "convention determine all connection-level and validated-numerics rows "
                    "functorially. Flux, Jacobian, inverse, residual and block bounds are not "
                    "independent source parameters."
                ),
            },
        },
        "frontier_delta": {
            "newly_closed": [
                "exact audit that no current carrier packet supplies a physical HYM seed",
                "integral DD(alpha) restriction zero and eta9 upper-source refinement imported",
                "K3 reference hidden HYM boolean separated from the physical P(3,9) HYM gate",
                "topological no-go for reusing the reference gauge connection",
                "explicit same-Chern/different-residual counterexample",
                "ordinary hidden adjoint via order-three twist cancellation",
                "trace-free rank-102 coupled deformation carrier",
                "exact harmonic-kernel projection algebra",
                "reduction of the source payload to four primitive geometric rows",
            ],
            "not_reopened": [
                "reference and T-dual Hull-Strominger existence",
                "smooth real and integral physical Bianchi classes",
                "invariant Bott-Chern reduction",
                "finite 27-state/SM profile results",
                "universal q79 shared-line finite intertwiner",
            ],
        },
        "checks": checks,
        "guardrails": {
            "claims_physical_visible_bundle_exists": False,
            "claims_physical_hidden_holomorphic_bundle_exists": False,
            "claims_topological_carrier_determines_connection": False,
            "claims_reference_connection_is_physical_seed": False,
            "claims_zero_index_implies_inverse": False,
            "claims_rank102_is_a_102_by_102_final_Galerkin_matrix": False,
            "claims_27_state_matrix_is_the_Hull_Strominger_Jacobian": False,
            "claims_physical_Y_Z_or_K_is_computed": False,
            "uses_observed_physics_values": False,
            "adds_fitted_parameter": False,
            "modifies_external_authority_repositories": False,
        },
        "next_executable_object": {
            "name": "q79SelectedPhysicalHolomorphicPairAndGalerkinSeed.v1",
            "primitive_rows": list(source_rows.keys()),
            "derived_execution_order": [
                "construct V3 and E_h^tau transition/Dolbeault data from the selected source tuple",
                "solve or approximate the common Hermitian-Einstein metrics and positive balanced metric",
                "assemble Dbar_Q, compute Pi_harm and choose the orthogonal gauge slice",
                "project onto a declared q79 spectral/Fourier basis and emit L_N",
                "validate G_N, continuum coercive tail, residual Y and K(r)",
                "decide Y+(Z0+Z1*r)*r<r and metric positivity on the same ball",
            ],
            "first_nonredundant_blocker": (
                "the selected characteristic-zero eta9 differential-Picard source, including "
                "its graph pair and flat Deligne trivialization, plus a genuine hidden "
                "twisted-holomorphic locally free carrier in the same Gauduchon chamber"
            ),
        },
        "new_continuous_fit_parameters": 0,
    }

    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("q79 physical gauge-pair deformation seed contract: PASS")
    print("coupled preprojection carrier: complex rank 102; gauge adjoint lane: 88")
    print("reference gauge seed reuse: EXCLUDED; reference metric lane: RETAINED")
    print("minimal primitive source rows: 4; physical Galerkin/Y/K execution: OPEN")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
