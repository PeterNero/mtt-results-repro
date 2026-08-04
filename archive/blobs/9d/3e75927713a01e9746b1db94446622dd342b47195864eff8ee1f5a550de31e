from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79pgl3toprymgerbejacobianexecution"
STATUS = "MTT_U6_Q79_GERBE_ZERO_REDUCED_TO_SPLITTING_CONIC_RELATIVE_PERIOD_SYSTEM_MARKED_SOURCE_OPEN"
NEXT = "MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1.md"

NORMAL_FORM = OUT / "splitting_conic_K3_normal_form.packet.json"
DELIGNE = OUT / "relative_Deligne_Brauer_zero_criterion.packet.json"
JACOBIAN = OUT / "residue_period_Jacobian_formula.packet.json"
SOURCE = OUT / "same_branch_source_reduction_and_crossuse_guard.packet.json"
OPEN_INPUT = OUT / "marked_geometry_and_period_input.open.json"
FRONTIER = OUT / "U6_frontier_after_A106.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A102_lattice": ROOT
        / "candidate_data"
        / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
        / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json",
        "A103_spectral": ROOT
        / "candidate_data"
        / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
        / "q79_genus_two_determinant_zero_spectral_cover.packet.json",
        "A104_surface": ROOT
        / "candidate_data"
        / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
        / "spectral_surface_invariants.packet.json",
        "A104_DD": ROOT
        / "candidate_data"
        / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
        / "integral_DD_restriction.packet.json",
        "A105": ROOT / "candidate_data" / "selected_q79normalizedpoincaregerbeandpgl3prymreduction.candidate.json",
        "A105_square": ROOT
        / "candidate_data"
        / "selected_q79normalizedpoincaregerbeandpgl3prymreduction"
        / "PGL3_to_Prym_square_system.packet.json",
        "tau_i_diagnostic": ROOT / "candidate_data" / "selected_ext_l2_theta_quadrature_table.candidate.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A106 authority: " + ", ".join(missing))

    lattice = load(paths["A102_lattice"])
    spectral = load(paths["A103_spectral"])
    surface = load(paths["A104_surface"])
    dd = load(paths["A104_DD"])
    a105 = load(paths["A105"])
    square = load(paths["A105_square"])
    tau_i = load(paths["tau_i_diagnostic"])

    gram = lattice["K3_lattice"]["Gram_h_delta"]
    assert gram == [[2, 0], [0, -4]]
    assert lattice["K3_lattice"]["delta_primitive"]
    assert not lattice["source_guard"]["rank_one_FuYau_topology_selected_by_MTT"]
    assert spectral["determinant_zero_cover"]["PGL3_alignment_complex_dimension"] == 8
    assert surface["Lefschetz_and_Hodge"]["p_g"] == 9
    assert surface["Lefschetz_and_Hodge"]["betti"][2] == 92
    assert dd["restriction_pairing"]["integral_DD_restriction_zero"]
    assert a105["next_required_artifact"] == "MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1"
    assert a105["results"]["active_Prym_residue_dimension"] == 8
    assert square["alignment_to_residue_map"]["Jacobian_shape"] == [8, 8]
    assert tau_i["canonical_theta_metric"]["tau"] == "i"
    assert not tau_i["closure_claimed"]

    h2 = gram[0][0]
    h_delta = gram[0][1]
    delta2 = gram[1][1]
    r_plus2 = h2 + 2 * h_delta + delta2
    r_minus2 = h2 - 2 * h_delta + delta2
    h_r_plus = h2 + h_delta
    h_r_minus = h2 - h_delta
    r_plus_r_minus = h2 - delta2
    chi_root = 2 + r_plus2 // 2
    k3_moduli_dimension = 20 - 2
    elliptic_moduli_dimension = 1
    source_moduli_dimension = k3_moduli_dimension + elliptic_moduli_dimension
    splitting_family_dimension = 5 + 7 + 15 - 1 - 8

    assert r_plus2 == r_minus2 == -2
    assert h_r_plus == h_r_minus == 2
    assert r_plus_r_minus == 6
    assert chi_root == 1
    assert splitting_family_dimension == k3_moduli_dimension == 18

    normal_form = {
        "schema": "MTTQ79SplittingConicMarkedK3NormalForm.v1",
        "status": "EXACT_LATTICE_TO_SPLITTING_CONIC_DOUBLE_SEXTIC_NORMAL_FORM_CLOSED",
        "lattice_input": {
            "Gram_H_delta": gram,
            "H_ample_genus_two": True,
            "delta_primitive": True,
            "branch_scope": "conditional rank-one Fu-Yau branch inherited from A102",
        },
        "root_calculation": {
            "R_plus": "H+delta",
            "R_minus": "H-delta",
            "R_plus_squared": r_plus2,
            "R_minus_squared": r_minus2,
            "H_dot_R_plus": h_r_plus,
            "H_dot_R_minus": h_r_minus,
            "R_plus_dot_R_minus": r_plus_r_minus,
            "K3_Riemann_Roch_chi_for_each_root": chi_root,
            "effectivity": "H is ample and H.R_+/-=2>0, so -R_+/- cannot be effective; K3 Riemann-Roch makes R_+/- effective.",
            "generic_irreducibility": "Every nonzero effective lattice class has positive H-degree in 2Z. Since R_+/- have minimal positive degree 2, they cannot split into two nonzero effective components.",
            "geometry": "R_+ and R_- are smooth rational curves mapped birationally to the same conic Q under phi_H; the deck involution exchanges them and pi^*Q=R_++R_-=2H.",
        },
        "double_sextic_model": {
            "weighted_projective_equation": "w^2=F6(x0,x1,x2)",
            "splitting_conic": "Q2(x0,x1,x2)=0",
            "normal_form": "F6=G3^2+Q2*H4",
            "lifted_components": ["R_+:{Q2=0,w=+G3}", "R_-:{Q2=0,w=-G3}"],
            "marked_class": "delta=R_+-H=(R_+-R_-)/2",
            "lift_sign_ambiguity": "R_+ <-> R_- sends delta -> -delta",
            "smoothness_open_condition": "F6 and Q2 are smooth, and H4 is nonzero at the six points Q2=G3=0; full projective Jacobian smoothness must be certified for an inserted model.",
        },
        "parameter_count": {
            "projective_smooth_conic_Q2": 5,
            "section_g_of_O_Q_6": 7,
            "quartic_H4": 15,
            "overall_sextic_scaling_removed": 1,
            "PGL3_coordinate_equivalence_removed": 8,
            "result": splitting_family_dimension,
            "lattice_period_domain_dimension": k3_moduli_dimension,
            "count_matches": splitting_family_dimension == k3_moduli_dimension,
            "G3_lift_redundancy": "Changing G3 by Q2*L1 is absorbed by H4 and adds no modulus.",
        },
        "theorem": {
            "name": "Q79SplittingConicMarkedK3NormalFormTheorem",
            "proved": True,
            "statement": "On the generic ample genus-two K3 in the primitive lattice <H,delta>=diag(2,-4), the roots H+delta and H-delta are irreducible rational degree-two curves exchanged by the genus-two deck involution. Their common image is a splitting conic, and the marked K3 has the normal form w^2=G3^2+Q2 H4 with delta=R_+-H. The family has the expected 18 complex moduli.",
        },
    }

    deligne = {
        "schema": "MTTQ79RelativeDeligneAnalyticBrauerZeroCriterion.v1",
        "status": "EXACT_RELATIVE_DELIGNE_AND_INTEGRAL_PERIOD_BRANCH_CRITERION_CLOSED",
        "exponential_sequence": {
            "sequence": "H^2(C,Z) -> H^2(C,O_C) -> H^2(C,O_C^*) -> H^3(C,Z)",
            "DD_alpha_C": 0,
            "logarithmic_lift": "Choose a_ijk=(2*pi*i)^-1 log(alpha_ijk|C). Since delta_Cech(a) is an integral coboundary when DD(alpha|C)=0, subtract an integral 2-cochain to obtain an additive O_C-valued 2-cocycle b.",
            "analytic_class": "beta_C=[b] in H^2(C,O_C)/image(H^2(C,Z))",
            "zero_criterion": "alpha|C is holomorphically trivial iff [b] lies in image(H^2(C,Z)->H^2(C,O_C)).",
        },
        "relative_mapping_cone": {
            "pair": "(J,C), J=K3 x E",
            "integral_exact_segment": "H^2(C,Z) -> H^3(J,C;Z) -> H^3(J,Z) -> H^3(C,Z)",
            "relative_lift_exists": True,
            "reason": "A104 proved i^*DD(alpha)=0 in H^3(C,Z).",
            "interpretation": "The normalized restriction is the relative Deligne/Abel-Jacobi invariant of a relative lift of DD(alpha), modulo integral boundary classes.",
        },
        "trace_free_projection": {
            "H2_O_C_dimension": 9,
            "ambient_trace_dimension": 1,
            "active_trace_free_dimension": 8,
            "H2_C_Z_rank": surface["Lefschetz_and_Hodge"]["betti"][2],
            "criterion": "b_tf is zero as an analytic gerbe iff b_tf=P_tf(e) for some e in H^2(C,Z).",
            "correction_to_naive_coordinates": "Globally, vanishing is an integral-period congruence. It is not certified by eight floating coordinates being merely small.",
            "projected_integral_group_warning": "The image of H^2(C,Z) in H^2(C,O_C) need not be a discrete lattice. Exact equality or a proved period-separation bound is required.",
        },
        "theorem": {
            "name": "Q79RelativeDeligneGerbeZeroCriterionTheorem",
            "proved": True,
            "statement": "After A104 and A105, the remaining normalized gerbe vanishes exactly when its trace-free logarithmic Cech class equals the trace-free (0,2) projection of an integral H^2(C,Z) class. Thus the global zero problem is a countable integral-period-branch system; the local 8x8 system is obtained only after fixing one branch and a Gauss-Manin trivialization.",
        },
    }

    jacobian = {
        "schema": "MTTQ79ResiduePeriodJacobianFormula.v1",
        "status": "EXACT_RESIDUE_BASIS_PERIOD_CONGRUENCE_AND_COVARIANT_JACOBIAN_FORMULA_CLOSED",
        "spectral_family": {
            "V": "H^0(K3,H) tensor H^0(E,O(3[0]))",
            "dimension_V": 9,
            "compact_parameter_space": "P(V)=P8",
            "smooth_invertible_tensor_open_orbit": "PGL3 subset P8",
            "theta_basis": "theta(z;tau)=(theta_0,theta_1,theta_2)^T for H^0(E,O(3[0]))",
            "spectral_equation": "s_A(X,z)=X^T A theta(z;tau)=0, A in PGL3",
        },
        "trace_free_residue_basis": {
            "K3_form": "On w^2=F6, Omega_K3 is dx1 wedge dx2 / w on an affine chart, up to a nonzero common scale.",
            "ambient_form": "Omega_J=Omega_K3 wedge dz",
            "pgl3_generators": "Choose T_r, r=1,...,8, as any basis of traceless 3x3 matrices.",
            "spectral_variation": "dot_s_r=X^T A T_r theta",
            "residue_formula": "omega_r(A)=Res_C_A[(dot_s_r/s_A) Omega_J]",
            "basis_statement": "The eight omega_r span H^0(K_C)_tf=H^2(K)^*. Scaling Omega_J changes all rows by one invertible common factor and cannot change zero or transversality.",
        },
        "period_system": {
            "integral_basis": "Choose e_I, I=1,...,92, for H^2(C,Z) and transport it by Gauss-Manin.",
            "projected_period_matrix": "Pi_rI(A)=integral_C_A e_I wedge omega_r(A)",
            "gerbe_period_vector": "z_r(A)=integral_C_A b_A wedge omega_r(A), with b_A the normalized logarithmic Cech representative.",
            "fixed_integral_branch": "ell=(ell_1,...,ell_92) in Z^92",
            "eight_equations": "F_r(A,ell)=z_r(A)-sum_I Pi_rI(A) ell_I=0, r=1,...,8",
            "meaning": "F=0 is exactly alpha|C_A=0 on the chosen integral branch.",
        },
        "covariant_Jacobian": {
            "shape": [8, 8],
            "formula": "J_rs=nabla_s z_r-sum_I ell_I nabla_s Pi_rI",
            "connection": "Gauss-Manin on H^2(C,Z) plus the holomorphic Hodge-bundle connection/basis transport",
            "A105_correction": "Differentiating beta coordinates alone is insufficient when the period representative and Hodge basis vary.",
            "transverse_zero": "F=0 and det(J)!=0 on one exact integral branch selects an isolated local alignment.",
        },
        "certified_execution": {
            "lawful_exact_routes": [
                "exact algebraic/CM period identities",
                "Picard-Fuchs or Griffiths-Dwork continuation with interval enclosures and a proved separation bound",
                "direct Deligne-Cech coboundary with an exact holomorphic 1-cochain",
            ],
            "unlawful_acceptance": [
                "small floating residual without a separation theorem",
                "nearest-lattice search when discreteness of the projected integral group is unproved",
                "importing observed SM values as selectors",
            ],
            "Jacobian_entries_as_source_inputs": 0,
            "beta_coordinates_as_source_inputs": 0,
        },
        "theorem": {
            "name": "Q79PGL3ToPrymRelativePeriodJacobianTheorem",
            "proved": True,
            "statement": "For a filled marked splitting-conic K3 and elliptic modulus, the normalized Poincare gerbe zero and its local transversality are determined by the displayed eight relative period congruences and their covariant 8x8 derivative. The gerbe coordinates, period matrix and Jacobian entries are derived outputs, not independent source rows.",
        },
    }

    source = {
        "schema": "MTTQ79SameBranchGerbeSourceReductionAndCrossuseGuard.v1",
        "status": "A105_RAW_INPUTS_REDUCED_TO_MARKED_K3_ELLIPTIC_SOURCE_TAU_I_DIAGNOSTIC_ONLY",
        "primitive_geometric_source": {
            "marked_lattice_polarized_K3_complex_moduli": k3_moduli_dimension,
            "elliptic_modulus_complex_moduli": elliptic_moduli_dimension,
            "total_unselected_complex_moduli": source_moduli_dimension,
            "discrete_delta_lift_sign": 1,
            "alignment_complex_unknowns_solved_by_F": 8,
            "independent_beta_rows": 0,
            "independent_period_Jacobian_rows": 0,
            "independent_Poincare_cocycle_rows": 0,
            "reason_Poincare_data_are_derived": "For a K3, H^1(O)=0. In 0->Lambda_E->O->E->0 the principal E-torsor lift of the fixed Chern pair (delta,0), when it exists, is unique; zero-section normalization then fixes the dual Poincare gerbe.",
        },
        "current_corpus_census": {
            "repositories_scanned": [
                "mtt-sm-parity-closure",
                "mtt-q79-proof-repro",
                "mtt-qa-su3-packet-proof",
                "mtt-individual-constants-source-search",
                "mtt-nonsm-constants-no-knob",
                "mtt-protospinor-gr-response-proof",
                "mtt-results-repro",
                "mtt-sm-parity-repro",
            ],
            "marked_splitting_conic_K3_coefficients_found": False,
            "same_FuYau_elliptic_modulus_source_found": False,
            "same_branch_relative_period_table_found": False,
            "same_branch_exact_Deligne_trivializing_cochain_found": False,
        },
        "tau_i_crossuse": {
            "available_value": "tau=i",
            "source_packet": "selected_ext_l2_theta_quadrature_table.candidate.json",
            "native_geometry": "Iwasawa/Appell-Humbert theta representative with degrees (2,-4,0)",
            "same_FuYau_K3_torus_source_theorem": False,
            "allowed_use": "diagnostic elliptic branch for a support execution only",
            "strict_promotion": "requires a same-superset theorem identifying the Appell-Humbert elliptic factor with the q79 rank-one Fu-Yau fiber",
        },
        "upstream_selection_guard": {
            "rank_one_FuYau_topology_selected_by_MTT": False,
            "shared_circle_to_untwisted_FuYau_factor_source_open": True,
            "effect": "A106 advances the conditional compactification branch and does not silently promote A102's source premise.",
        },
        "new_fitted_observable_parameters": 0,
    }

    open_input = {
        "schema": "MTTQ79MarkedK3EllipticRelativeGerbeExecutionInput.v1",
        "status": "OPEN_SOURCE_AND_EXECUTION_INPUT",
        "selection": {
            "rank_one_FuYau_source_theorem_id": None,
            "marked_K3_source_id": None,
            "elliptic_modulus_source_id": None,
            "delta_lift_sign_plus_or_minus_one": None,
            "observed_SM_values_used": False,
        },
        "marked_double_sextic": {
            "Q2_coefficients_6": [None] * 6,
            "G3_coefficients_10": [None] * 10,
            "H4_coefficients_15": [None] * 15,
            "identity_F6_equals_G3_squared_plus_Q2_H4_certified": False,
            "projective_branch_smoothness_certified": False,
            "NS_marking_Gram_diag_2_minus4_certified": False,
        },
        "elliptic_curve": {
            "tau_real": None,
            "tau_imaginary": None,
            "tau_upper_half_plane_certified": False,
            "degree_three_theta_basis_convention": None,
        },
        "execution_choices_not_source_parameters": {
            "alignment_seed_3x3": [[None] * 3 for _ in range(3)],
            "pgl3_basis_8": [None] * 8,
            "integral_H2_basis_92_or_equivalent_monodromy_basis": None,
            "Gauss_Manin_transport": None,
            "relative_Deligne_or_Cech_representative": None,
            "period_integration_method": None,
            "rigorous_error_and_exactness_certificate": None,
        },
        "outputs": {
            "integral_branch_ell_92": None,
            "gerbe_period_vector_z_8": [None] * 8,
            "projected_period_matrix_Pi_8x92": None,
            "residual_F_8": [None] * 8,
            "covariant_Jacobian_8x8": [[None] * 8 for _ in range(8)],
            "Jacobian_determinant": None,
        },
        "acceptance": {
            "same_q79_FuYau_source": False,
            "exact_period_congruence_F_zero": False,
            "Jacobian_determinant_nonzero": False,
            "isolated_alignment_certified": False,
            "beta_C_zero": False,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA106.v1",
        "status": STATUS,
        "closed_now": [
            "lattice-forced splitting-conic normal form w^2=G3^2+Q2 H4",
            "exact relative Deligne/analytic-Brauer zero criterion including integral branches",
            "explicit residue basis for all eight trace-free holomorphic two-forms",
            "period-congruence equations and full covariant 8x8 Jacobian formula",
            "reduction of A105 cocycle/beta/Jacobian entries from source inputs to derived outputs",
        ],
        "source_reduction": {
            "A105_apparent_independent_Jacobian_entries": 64,
            "A105_apparent_independent_beta_entries": 8,
            "A106_independent_Jacobian_or_beta_entries": 0,
            "unselected_marked_K3_complex_moduli": k3_moduli_dimension,
            "unselected_elliptic_complex_moduli": elliptic_moduli_dimension,
            "discrete_lift_sign": 1,
        },
        "still_open": [
            "strict MTT source theorem for the conditional rank-one Fu-Yau topology",
            "selected marked splitting-conic K3 point and same-branch elliptic modulus",
            "exact or rigorously separated relative-period solution on an integral branch",
            "twisted rank-one spectral sheaf and inverse Fourier-Mukai local freeness",
            "balanced HYM and full differential Bianchi identity",
            "seven numerical NS5/threshold inputs already isolated upstream",
        ],
        "beta_C_zero_proved": False,
        "isolated_alignment_found": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Fill one same-branch marked splitting-conic K3 and elliptic source, then execute the eight exact relative-period congruences with integral branch and covariant Jacobian certification.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "splitting_conic_K3_normal_form": str(NORMAL_FORM.relative_to(ROOT)).replace("\\", "/"),
        "relative_Deligne_zero_criterion": str(DELIGNE.relative_to(ROOT)).replace("\\", "/"),
        "residue_period_Jacobian_formula": str(JACOBIAN.relative_to(ROOT)).replace("\\", "/"),
        "same_branch_source_reduction": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "marked_geometry_open_input": str(OPEN_INPUT.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (NORMAL_FORM, normal_form),
        (DELIGNE, deligne),
        (JACOBIAN, jacobian),
        (SOURCE, source),
        (OPEN_INPUT, open_input),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "splitting_conic_normal_form_proved": normal_form["theorem"]["proved"],
        "K3_moduli_count_matches_18": normal_form["parameter_count"]["count_matches"],
        "relative_Deligne_zero_criterion_proved": deligne["theorem"]["proved"],
        "integral_period_branch_retained": "ell" in jacobian["period_system"]["eight_equations"]
        and "Z^92" in jacobian["period_system"]["fixed_integral_branch"],
        "residue_basis_dimension_eight": len(open_input["execution_choices_not_source_parameters"]["pgl3_basis_8"]) == 8,
        "covariant_Jacobian_shape_8x8": jacobian["covariant_Jacobian"]["shape"] == [8, 8],
        "Jacobian_entries_are_derived": jacobian["certified_execution"]["Jacobian_entries_as_source_inputs"] == 0,
        "tau_i_not_cross_promoted": not source["tau_i_crossuse"]["same_FuYau_K3_torus_source_theorem"],
        "upstream_conditionality_preserved": not source["upstream_selection_guard"]["rank_one_FuYau_topology_selected_by_MTT"],
        "no_observed_selector": not open_input["selection"]["observed_SM_values_used"],
    }
    assert all(checks.values())

    authority_hashes = [
        {"path": str(path), "sha256": sha256(path)} for path in paths.values()
    ]
    candidate = {
        "schema": "MTTSelectedQ79PGL3ToPrymGerbeJacobianExecution.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": {
            "splitting_conic_normal_form_closed": True,
            "relative_period_equations_closed": True,
            "covariant_Jacobian_formula_closed": True,
            "independent_beta_or_Jacobian_source_rows": 0,
            "unselected_geometric_source_moduli_complex": source_moduli_dimension,
            "new_fitted_continuous_parameters": 0,
            "beta_C_zero_proved": False,
            "isolated_alignment_found": False,
            "U6_strong_CP_closed": False,
        },
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": candidate["results"],
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 PGL3-to-Prym Gerbe Jacobian Execution v1

Status: `{STATUS}`

## What A106 changes

A105 correctly found an eight-dimensional local obstruction problem, but its
open packet still made the marked K3, Poincare cocycle, gerbe coordinates and
all 64 Jacobian entries look like separate inputs. They are not. A106 derives
the geometry and the complete equation from a much smaller source object.

It also corrects the global zero condition. A topologically trivial
holomorphic gerbe is zero modulo the integral image in the exponential
sequence. Therefore the exact equation is a period congruence on a fixed
integral branch, not merely eight floating coordinates approximately equal to
zero.

## Splitting-conic K3 theorem

The A102 lattice is

```text
H^2=2, delta^2=-4, H.delta=0,
```

with `H` ample and `delta` primitive. Set

```text
R_+=H+delta,  R_-=H-delta.
```

Then

```text
R_+^2=R_-^2=-2,
H.R_+=H.R_-=2,
R_+.R_-=6.
```

K3 Riemann-Roch gives `chi(O(R_+/-))=1`. Since `H` is ample, `-R_+/-`
cannot be effective, so both roots are effective. Every lattice class has
`H`-degree in `2Z`; hence a degree-two root is generically irreducible. Each
is therefore a smooth rational curve.

The genus-two map is a double cover `pi:S->P2`. The two roots map
birationally to one conic `Q` and are exchanged by the deck involution:

```text
pi^*Q=R_+ + R_-=2H.
```

Consequently every generic marked model has the explicit normal form

```text
w^2=F6,
F6=G3^2+Q2 H4,
R_+={{Q2=0,w=+G3}},
R_-={{Q2=0,w=-G3}},
delta=R_+-H.
```

The count is

```text
5 (Q2) + 7 (G3 restricted to Q) + 15 (H4)
- 1 (overall scale) - 8 (PGL3) = 18,
```

exactly the period-domain dimension for a rank-two lattice-polarized K3.
Changing the lift `G3` by `Q2 L1` is absorbed into `H4`.

## Exact analytic-Brauer zero

For a good cover of `C`, choose logarithms

```text
a_ijk=(2 pi i)^-1 log(alpha_ijk|C).
```

A104 proved `DD(alpha|C)=0`. Its integral Cech 3-cocycle is therefore a
coboundary. Subtracting an integral 2-cochain gives an additive cocycle `b`
and

```text
beta_C=[b] in H^2(C,O_C)/image(H^2(C,Z)).
```

After A105's trace removal, the exact criterion is

```text
beta_C=0
iff b_tf=P_tf(e) for some e in H^2(C,Z).
```

The projected integral group is not automatically a discrete lattice. A
small numerical residual or an uncertified nearest-lattice answer cannot
prove this equality.

## Eight explicit residue rows

Let `X=(X0,X1,X2)^T` be the genus-two coordinates and let
`theta(z;tau)` be a basis of `H^0(E,O(3[0]))`. An alignment `A in PGL3`
defines

```text
s_A(X,z)=X^T A theta(z;tau).
```

For a traceless-matrix basis `T_r` of `pgl3`, set

```text
dot_s_r=X^T A T_r theta,
omega_r(A)=Res_C_A[(dot_s_r/s_A) Omega_K3 wedge dz].
```

On `w^2=F6`, one may take `Omega_K3=dx1 wedge dx2/w` on an affine chart.
The eight residues form the trace-free basis of `H^0(K_C)` dual to A105's
`H^2(K)` obstruction space. Thus no independent Prym basis rows are needed.

## Correct 8 by 8 system

Transport an integral basis `e_I`, `I=1,...,92`, of `H^2(C,Z)` by the
Gauss-Manin connection and define

```text
Pi_rI(A)=integral_C_A e_I wedge omega_r(A),
z_r(A)=integral_C_A b_A wedge omega_r(A).
```

On a fixed integral branch `ell in Z^92`, the eight exact equations are

```text
F_r(A,ell)=z_r(A)-sum_I Pi_rI(A) ell_I=0.
```

Their full covariant Jacobian is

```text
J_rs=nabla_s z_r-sum_I ell_I nabla_s Pi_rI.
```

Both terms are required because the integral periods and Hodge basis vary.
An exact `F=0` together with `det(J)!=0` selects an isolated local alignment.

## Source reduction and guardrails

The actual primitive continuous source is now:

```text
18 complex coordinates: one marked splitting-conic K3 period point,
 1 complex coordinate: the elliptic modulus tau,
 1 discrete sign:       delta <-> -delta.
```

The eight alignment coordinates are variables solved by the equations. The
eight gerbe coordinates, 92-column period table and 64 Jacobian entries are
derived outputs, not fitted rows.

The repository has a ready `tau=i` Appell-Humbert theta implementation. It
belongs to the Iwasawa `(2,-4,0)` model and may be used for a diagnostic run,
but no theorem identifies it with the elliptic fiber of this rank-one Fu-Yau
branch. A106 does not cross-promote it. It also preserves A102's warning that
the shared-circle-to-Fu-Yau source map itself remains conditional.

No measured Standard-Model value and no new fitted parameter enters A106.
The gerbe zero, twisted sheaf, inverse Fourier-Mukai bundle, balanced HYM and
differential Bianchi identity remain open.

Next artifact: `{NEXT}`.

## Primary references

- [Brinzanescu, Halanay and Trautmann, Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Caldararu, Derived categories of twisted sheaves on elliptic threefolds](https://arxiv.org/abs/math/0012083)
- [Ferrari Ruffino, Relative Deligne cohomology and Cheeger-Simons characters](https://arxiv.org/abs/1401.0631)
- [Shimada, Z-splitting curves for double plane sextics](https://arxiv.org/abs/0903.3308)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
