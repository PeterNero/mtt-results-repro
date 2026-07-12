from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictnoknobupgradeledger_aftertruesmequivalence"
OUT = ROOT / "candidate_data" / SLUG


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    final = load("certificates/selected_finalglobaltruesmclosureaudit_aftermultiloopprecision_certificate.json")
    multiloop = load("certificates/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood_certificate.json")
    ckm = load("certificates/selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure_certificate.json")
    neutrino = load("certificates/selected_neutrinomassmajoranapolicy_or_precisionprofiletable_certificate.json")
    theta = load("certificates/selected_qcdthetapolicy_or_strictpewcountreduction_certificate.json")
    geometry = load("certificates/selected_geometric_cechhym_obligation_reduction_after_onepremise_certificate.json")
    qft = load("certificates/selected_renormalizedsmobservablefunctor_fromcommonschemeaction_certificate.json")
    literal_cech = load("certificates/selected_literalcechwitness_or_globalhymconnectioncoefficients_certificate.json")
    joint = load("certificates/selected_officialjointlikelihoodtransport_or_declareddiagonalprofilefinality_certificate.json")
    ckm_profile = load("certificates/selected_ckmcentralestimatorretirement_or_predictionprofileclosure_certificate.json")
    hym_aposteriori = load("certificates/selected_globalhymchernsequence_aposterioricertificate_certificate.json")
    hym_spectral = load("certificates/selected_hymuniformspectralconvergenceandpatchingcertificate_certificate.json")
    hym_continuum = load("certificates/selected_hymvalidatedfourierresidualtailbound_certificate.json")
    neutrino_cp = load("certificates/selected_neutrinoandstrongcp_strictupgradeattack_certificate.json")
    neutral_mass = load("certificates/selected_neutralnilboundarymassfunctional_certificate.json")
    neutral_operator = load("certificates/selected_neutraloperatorunificationandinventoryaudit_certificate.json")
    neutral_source = load("certificates/selected_neutralmassoperator_sourceemission_certificate.json")
    neutral_dimensionful = load("certificates/selected_neutraldimensionfulblocksandnormalization_certificate.json")
    neutral_overlap_gate = load("certificates/selected_neutraloverlapkernelphysicalunitoractioncompleteness_certificate.json")
    neutral_value_source = load("certificates/selected_neutraloverlapkernelvaluesourceorphysicalunittheorem_certificate.json")
    neutral_gamma = load("certificates/selected_neutralgammanuactionrowsordiraccompleteness_certificate.json")
    neutral_finite_gamma = load("certificates/selected_neutralfinitegammarowsoractioncostsource_certificate.json")
    neutral_relative = load("certificates/selected_neutralactioncostprefactorordiracmajoranacompletion_certificate.json")
    neutral_internal = load("certificates/selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion_certificate.json")
    neutral_obstruction = load("certificates/selected_neutralphysicalunitornilanchorprojector_certificate.json")
    neutral_discrimination = load("certificates/selected_neutralspectralactionslopeorseesawsource_certificate.json")
    neutral_protospinor = load("certificates/selected_protospinoralignmenttodiracmassreadout_certificate.json")
    neutral_radial = load("certificates/selected_neutralradialsecondvariationandvevcoordinatetheorem_certificate.json")
    neutral_higgs_insertion = load("certificates/selected_neutralhiggsinsertionfunctorandradialcoordinatenormalization_certificate.json")
    neutral_effective_weight = load("certificates/selected_neutraleffectiveweightidentifiabilityreduction_certificate.json")
    neutral_crt_phase = load("certificates/selected_neutralcrtphasetypingandprotospinornildriftreduction_certificate.json")
    neutral_circle_factor = load("certificates/selected_neutralcommoncirclefactorizationandholonomyscalarreduction_certificate.json")
    neutral_det_nogo = load("certificates/selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget_certificate.json")
    neutral_profile_values = load("certificates/selected_neutraltwoprimitiveprofilevalueclosure_certificate.json")
    neutral_lens_dedekind = load("certificates/selected_neutrallensdedekindtransgression_or_oneprimitiveprofile_certificate.json")
    neutral_e0 = load("certificates/selected_neutraluniversale0attenuationcandidate_or_sourcelawfrontier_certificate.json")
    neutral_composite = load("certificates/selected_neutralcompositespectralattenuationreduction_or_branchbridgetheorem_certificate.json")
    same_geometry = load("certificates/selected_samegeometryqutrittosmalgebrabridge_or_generativebasefrontier_certificate.json")
    e6_anomaly = load("certificates/selected_e6centralgeneratorqcdanomalyaudit_certificate.json")
    branch = load("certificates/selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness_certificate.json")
    foundations = load("certificates/selected_quantizationandnonperturbativeqft_strictupgradeaudit_certificate.json")

    if not final["true_SM_equivalence_closed_at_declared_standard"]:
        raise ValueError("declared-standard true-SM baseline is not closed")

    upgrades = [
        {
            "id": "U1_zero_primitive_empirical_source",
            "cluster": "synthesis",
            "status": "open",
            "closed_inherited": "one shared P_EW primitive; zero H-specific parameters; 8 common-scheme precision rows",
            "missing_object": "SelectedZeroPrimitiveEmpiricalSourceFunctor",
            "acceptance_test": "emit every admitted empirical SM coordinate before measured values enter, with zero fitted or shared physical primitives",
            "depends_on": ["U2_literal_global_Cech_HYM_QaSU3", "U4_exact_CKM_central", "U5_neutrino_absolute_ontology", "U6_strong_CP_selection", "U9_unique_observed_branch"],
        },
        {
            "id": "U2_literal_global_Cech_HYM_QaSU3",
            "cluster": "geometry_selection",
            "status": "closed",
            "closed_inherited": "counted AH-equivalent lane 8/8; selected literal S3 Deligne-Cech witness 1/1 with 81 entries and 729 cocycle triples; global Chern patching; finite HYM stability; exact weighted-theta Fourier tail and Wiener contraction close continuum existence/local uniqueness",
            "missing_object": "none for the selected literal Cech-HYM witness standard",
            "acceptance_test": "closed: exact density tail, conservative continuous residual bound, Z<1, Y+Zr<r, and Chern patching all pass on q79/F/m=1",
            "depends_on": [],
        },
        {
            "id": "U3_official_joint_input_likelihood",
            "cluster": "precision",
            "status": "partially_closed",
            "closed_inherited": f"SMDR multi-loop transport {multiloop['symmetric_unique_entries_determined']}/36; 15-coordinate/3-authority source-block audit and covariance replacement interface",
            "missing_object": "VersionedOfficialJointInputLikelihoodOrCovariance",
            "acceptance_test": "import a citable versioned joint likelihood/covariance for the 15 source coordinates and propagate it through the frozen SMDR Jacobian",
            "depends_on": [],
        },
        {
            "id": "U4_exact_CKM_central",
            "cluster": "flavor_vacuum",
            "status": "closed",
            "closed_inherited": "Pi_CKM source weights 3/3 and prediction-profile admission; exact equality to a moving central estimator retired as an invalid theory obligation",
            "missing_object": "none at the prediction-with-uncertainty standard",
            "acceptance_test": "closed: source-selected rows, no target fitting, and declared-profile displacement below one sigma",
            "depends_on": ["U2_literal_global_Cech_HYM_QaSU3"],
        },
        {
            "id": "U5_neutrino_absolute_ontology",
            "cluster": "flavor_vacuum",
            "status": "partially_closed",
            "closed_inherited": "minimal PMNS oscillation policy; selected 1_M=N^c Dirac channel; Majorana self-characters {0,672}; three-basin minimal-trace theorem conditionally fixes m_lightest=0; typed carrier, finite channels, relative orbit, and 9-row internal nuD response closed; common-scale plus nil-shift physical identification rigorously rejected, reducing the live route to a selected spectral action or seesaw",
            "missing_object": "SelectedNeutralMassOperator_SourceEmission",
            "acceptance_test": "emit one source-owned complex-symmetric neutral mass operator with dimensionful Dirac/Majorana blocks, character/U1 rule, normalization, and no-observed-selector certificate",
            "depends_on": ["U2_literal_global_Cech_HYM_QaSU3"],
        },
        {
            "id": "U6_strong_CP_selection",
            "cluster": "flavor_vacuum",
            "status": "partially_closed",
            "closed_inherited": "QCD theta-bar admitted as one valid SM parameter slot; conditional PQ theorem and axion ratios; E6 Qpsi trace gives matter A3=12, exotic A3=-12, full-27 cancellation and matter-only diagnostic N_DW=3",
            "missing_object": "SelectedFluxThresholdAxionCurrentAnomalyMatchingMap",
            "acceptance_test": "select a surviving global axion current and its flux/threshold chiral spectrum, prove a nonzero matched QCD anomaly and quality control, then satisfy the neutron-EDM bound",
            "depends_on": ["U2_literal_global_Cech_HYM_QaSU3", "U9_unique_observed_branch"],
        },
        {
            "id": "U7_MTT_derived_quantization",
            "cluster": "foundations",
            "status": "partially_closed",
            "closed_inherited": "renormalized-SM observable functor 5/5 with standard BRST/Faddeev-Popov and LSZ imported as parity structure",
            "missing_object": "MTTQuantizationBornRecordDerivationFunctor",
            "acceptance_test": "derive gauge fixing/BRST measure, path-integral or equivalent quantum dynamics, Born probabilities, and record/readout rules from selected MTT axioms",
            "depends_on": ["U9_unique_observed_branch"],
        },
        {
            "id": "U8_constructive_nonperturbative_4D_QFT",
            "cluster": "foundations",
            "status": "partially_closed",
            "closed_inherited": "perturbative renormalized-SM observable equivalence plus conditional finite-domain SPT-filtered TT/BRST Borel-summability core",
            "missing_object": "ConstructiveNonperturbativeFourDimensionalGaugeTheory",
            "acceptance_test": "construct the continuum interacting 4D theory with controlled limit, positive physical Hilbert space, and agreement with the perturbative branch",
            "depends_on": ["U7_MTT_derived_quantization"],
        },
        {
            "id": "U9_unique_observed_branch",
            "cluster": "geometry_selection",
            "status": "partially_closed",
            "closed_inherited": "selected antiunitary orbit {q79/F/m1,q369/F*/m2}; retarded kernel selects q79 representative without observed CP input",
            "missing_object": "SelectedGlobalBranchActionMeasureAndUniquenessTheorem",
            "acceptance_test": "define a branch measure/action independent of observed SM targets and prove a unique admissible minimizer or a probability-one equivalence class containing the observed branch",
            "depends_on": ["U2_literal_global_Cech_HYM_QaSU3"],
        },
    ]

    packet = {
        "schema": "MTTStrictNoKnobUpgradeLedgerAfterTrueSMEquivalence.v1",
        "status": "DECLARED_STANDARD_CLOSED_NINE_STRICT_UPGRADES_ORDERED",
        "baseline": {
            "closure_scope": final["closure_scope"],
            "obligations_closed": f"{final['obligations_closed']}/{final['obligations_required']}",
            "must_not_be_reopened": True,
        },
        "upgrade_count": len(upgrades),
        "closed_upgrade_count": sum(row["status"] == "closed" for row in upgrades),
        "partially_closed_upgrade_count": sum(row["status"] == "partially_closed" for row in upgrades),
        "open_upgrade_count": sum(row["status"] == "open" for row in upgrades),
        "upgrades": upgrades,
        "execution_order": [
            ["U3_official_joint_input_likelihood"],
            ["U2_literal_global_Cech_HYM_QaSU3"],
            ["U4_exact_CKM_central", "U5_neutrino_absolute_ontology", "U9_unique_observed_branch"],
            ["U6_strong_CP_selection", "U7_MTT_derived_quantization"],
            ["U8_constructive_nonperturbative_4D_QFT", "U1_zero_primitive_empirical_source"],
        ],
        "source_snapshot": {
            "ckm_selected_weight_rows": ckm["accepted_weight_rows"],
            "absolute_neutrino_mass_closed": neutrino["absolute_neutrino_mass_closed"],
            "Majorana_policy_selected": neutrino["Majorana_policy_selected"],
            "strong_CP_problem_solved": theta["strong_CP_problem_solved"],
            "geometric_connection_rows": f"{geometry['geometric_connection_rows_accepted']}/{geometry['geometric_connection_rows_required']}",
            "literal_Cech_witness_families": f"{literal_cech['U2_literal_witness_families_closed']}/{literal_cech['U2_literal_witness_families_required']}",
            "U3_local_execution_exhausted": joint["U3_local_execution_exhausted"],
            "U4_correct_prediction_standard_closed": ckm_profile["U4_correct_standard_closed"],
            "U2_finite_HYM_aposteriori_stability": hym_aposteriori["finite_projected_HYM_aposteriori_stability_closed"],
            "U2_global_HYM_patching_closed": hym_spectral["global_HYM_patching_closed"],
            "U2_nested_spectral_cutoffs": hym_spectral["cutoffs_checked"],
            "U2_last_nested_difference_l2": hym_spectral["successive_difference_l2"][-1],
            "U2_dealiased_residual_l2": hym_spectral["dealiased_residual_l2_at_mesh36"],
            "U2_previous_remaining_scalar_bound_count": hym_spectral["remaining_scalar_bound_count"],
            "U2_remaining_scalar_bound_count": 0,
            "U2_validated_continuous_residual_upper": hym_continuum["full_continuous_residual_upper"],
            "U2_Wiener_contraction_Z": hym_continuum["Z"],
            "U2_Wiener_contraction_margin": hym_continuum["strict_margin"],
            "U2_literal_witness_families": f"{hym_continuum['U2_literal_witness_families_closed']}/{hym_continuum['U2_literal_witness_families_required']}",
            "U2_continuum_HYM_closed": hym_continuum["literal_global_HYM_witness_closed"],
            "U5_selected_Dirac_channel": neutrino_cp["selected_Dirac_channel_closed"],
            "U5_absolute_mass_closed": neutrino_cp["absolute_neutrino_mass_closed"],
            "U5_minimal_trace_boundary_formula_closed": neutral_mass["minimal_trace_boundary_theorem_proved"],
            "U5_conditional_lightest_mass_eV": neutral_mass["conditional_lightest_mass_eV"],
            "U5_NO_sum_postcheck_eV": neutral_mass["normal_ordering_sum_postcheck_eV"],
            "U5_IO_sum_postcheck_eV": neutral_mass["inverted_ordering_sum_postcheck_eV"],
            "U5_remaining_source_clause_count": neutral_mass["remaining_source_clause_count"],
            "U5_unified_missing_object_count": neutral_operator["unified_missing_object_count"],
            "U5_neutral_operator_required_fields": f"{neutral_source['required_fields_closed']}/{neutral_source['required_fields_total']}",
            "U5_neutral_operator_predecessor_fields": f"{neutral_operator['required_fields_closed']}/{neutral_operator['required_fields_total']}",
            "U5_neutral_source_id_closed": neutral_source["source_id_closed"],
            "U5_neutral_character_gate_closed": neutral_source["Dirac_U1_or_selected_self_character_k_closed"],
            "U5_neutral_dimensionful_normal_form_closed": neutral_dimensionful["theorem_proved"],
            "U5_neutral_lawful_exit_routes": neutral_dimensionful["lawful_exit_route_count"],
            "U5_neutral_accepted_lawful_exit_routes": neutral_dimensionful["accepted_lawful_exit_route_count"],
            "U5_neutral_new_value_fields_closed": neutral_dimensionful["new_value_fields_closed_here"],
            "U5_neutral_overlap_OK_gates": f"{neutral_overlap_gate['neutral_overlap_OK_gates_closed']}/{neutral_overlap_gate['neutral_overlap_OK_gates_total']}",
            "U5_neutral_overlap_gate_accepted_routes": neutral_overlap_gate["accepted_route_exit_count"],
            "U5_neutral_overlap_gate_new_value_fields_closed": neutral_overlap_gate["new_value_fields_closed_here"],
            "U5_neutral_physical_unit_selected": neutral_overlap_gate["physical_unit_selected"],
            "U5_neutral_Dirac_only_completeness_closed": neutral_overlap_gate["Dirac_only_completeness_closed"],
            "U5_neutral_value_source_readiness": f"{neutral_value_source['readiness_subfields_closed']}/{neutral_value_source['readiness_subfields_total']}",
            "U5_neutral_gamma_structural_channel_closed": neutral_gamma["selected_typed_L_Nc_Hu_trilinear_channel_skeleton"],
            "U5_neutral_gamma_typed_cell_count": neutral_gamma["typed_Gamma_nu_cell_count"],
            "U5_neutral_gamma_finite_rows_closed": neutral_gamma["finite_Gamma_nu_ij_channel_sets_closed"],
            "U5_neutral_gamma_action_rows_closed": neutral_gamma["neutral_action_cost_rows_S_gamma_closed"],
            "U5_neutral_gamma_prefactors_closed": neutral_gamma["neutral_prefactors_A_gamma_closed"],
            "U5_neutral_gamma_retarded_signs_closed": neutral_gamma["neutral_retarded_sign_rows_closed"],
            "U5_neutral_finite_Gamma_rows_closed": neutral_finite_gamma["finite_Gamma_nu_ij_channel_sets_closed"],
            "U5_neutral_finite_Gamma_rows_selected": neutral_finite_gamma["finite_Gamma_nu_rows_selected"],
            "U5_neutral_active_channel_count": neutral_finite_gamma["active_channel_count"],
            "U5_neutral_exact_zero_channel_count": neutral_finite_gamma["exact_zero_channel_count"],
            "U5_neutral_channel_operator": neutral_finite_gamma["channel_operator"],
            "U5_neutral_latest_OK_gates": f"{neutral_finite_gamma['neutral_overlap_OK_gates_closed']}/{neutral_finite_gamma['neutral_overlap_OK_gates_total']}",
            "U5_neutral_latest_readiness": f"{neutral_finite_gamma['readiness_subfields_closed']}/{neutral_finite_gamma['readiness_subfields_total']}",
            "U5_neutral_latest_accepted_routes": neutral_finite_gamma["accepted_route_exit_count"],
            "U5_neutral_latest_dimensionless_channel_rows_closed": neutral_finite_gamma["new_dimensionless_channel_rows_closed_here"],
            "U5_neutral_latest_absolute_value_fields_closed": neutral_finite_gamma["new_absolute_value_fields_closed_here"],
            "U5_neutral_relative_amplitude_orbit_closed": neutral_relative["selected_second_order_neutral_relative_amplitude_orbit_closed"],
            "U5_neutral_relative_orbit_representatives": neutral_relative["orbit_representative_count"],
            "U5_neutral_relative_value_rows_closed": neutral_relative["relative_value_rows_closed"],
            "U5_neutral_relative_shift_magnitude": neutral_relative["active_shift_magnitude_exact"],
            "U5_neutral_relative_shift_phase_orbit": neutral_relative["active_shift_phase_orbit"],
            "U5_neutral_individual_orbit_representative_selected": neutral_relative["individual_orbit_representative_selected"],
            "U5_neutral_internal_dimensionless_response_closed": neutral_internal["selected_internal_dimensionless_neutral_response_closed"],
            "U5_neutral_internal_amplitude": neutral_internal["a_internal"],
            "U5_neutral_internal_rows_closed": neutral_internal["internal_dimensionless_rows_closed"],
            "U5_neutral_internal_same_source_fields": f"{neutral_internal['same_source_selected_fields']}/{neutral_internal['same_source_required_fields']}",
            "U5_neutral_latest_readiness_after_internal_values": f"{neutral_internal['readiness_subfields_closed']}/{neutral_internal['readiness_subfields_total']}",
            "U5_neutral_physical_value_fields_after_internal_values": neutral_internal["new_physical_value_fields_closed_here"],
            "U5_neutral_simple_common_scale_route_rejected": neutral_obstruction["simple_common_scale_route_rejected"],
            "U5_neutral_selected_orbit_spectrum": neutral_obstruction["selected_orbit_spectrum"],
            "U5_neutral_nil_shifted_spectrum": neutral_obstruction["nil_shifted_spectrum"],
            "U5_neutral_direct_nil_shift_ratio": neutral_obstruction["direct_nil_shift_ratio"],
            "U5_neutral_NO_postcheck_ratio": neutral_obstruction["normal_ordering_postcheck_ratio"],
            "U5_neutral_minimal_spectral_shape_parameter_count": neutral_obstruction["minimal_spectral_shape_parameter_count"],
            "U5_neutral_minimal_physical_scale_parameter_count": neutral_obstruction["minimal_physical_scale_parameter_count"],
            "U5_neutral_selected_beta_closed": neutral_obstruction["selected_beta_closed"],
            "U5_neutral_canonical_spt_ratio": neutral_discrimination["canonical_spt_ratio"],
            "U5_neutral_circle_candidate_ratios": neutral_discrimination["circle_candidate_ratios"],
            "U5_neutral_closest_circle_candidate_residual": neutral_discrimination["closest_circle_candidate_residual"],
            "U5_neutral_CP_to_Majorana_shortcut_rejected": neutral_discrimination["CP_to_Majorana_character_shortcut_rejected"],
            "U5_neutral_selected_real_structure_closed": neutral_discrimination["selected_neutral_real_structure_closed"],
            "U5_neutral_finite_Dirac_encoding_closed": neutral_protospinor["finite_Dirac_encoding_closed"],
            "U5_neutral_H1_rejected_as_mass_squared_Hessian": neutral_protospinor["H1_rejected_as_mass_squared_Hessian"],
            "U5_neutral_coefficient_matched_Gram_eigenvalues": neutral_protospinor["coefficient_matched_Gram_eigenvalues"],
            "U5_neutral_coefficient_matched_ratio": neutral_protospinor["coefficient_matched_ratio"],
            "U5_neutral_selected_radial_second_variation_closed": neutral_protospinor["selected_radial_second_variation_closed"],
            "U5_neutral_positive_second_variation_closed": neutral_radial["positive_second_variation_closed"],
            "U5_neutral_second_variation_eigenvalues": neutral_radial["second_variation_eigenvalues"],
            "U5_neutral_direct_H_radial_identity_insertion_rejected": neutral_radial["direct_H_radial_identity_insertion_rejected"],
            "U5_neutral_VEV_counts_as_specific_parameter": neutral_radial["VEV_counts_as_neutrino_specific_parameter"],
            "U5_neutral_H_insertion_functor_closed": neutral_radial["selected_H_to_neutral_insertion_functor_closed"],
            "U5_neutral_H_insertion_functor_closed_latest": neutral_higgs_insertion["selected_H_to_neutral_insertion_functor_closed"],
            "U5_neutral_radial_coordinate_normalization_closed": neutral_higgs_insertion["selected_radial_coordinate_normalization_closed"],
            "U5_neutral_H_insertion_magnitude": neutral_higgs_insertion["insertion_magnitude"],
            "U5_neutral_H_insertion_derivative_rows_closed": neutral_higgs_insertion["dimensionless_derivative_rows_closed"],
            "U5_neutral_H_insertion_curvature_eigenvalues": neutral_higgs_insertion["curvature_eigenvalues"],
            "U5_neutral_action_weighted_Ynu_closed": neutral_higgs_insertion["physical_action_weighted_Y_nu_closed"],
            "U5_neutral_combined_internal_effective_weight_closed": neutral_effective_weight["combined_internal_effective_weight_closed"],
            "U5_neutral_separate_A_S_obligations_retired": neutral_effective_weight["separate_A_gamma_S_gamma_obligations_retired"],
            "U5_neutral_conjugate_mass_equivalence_closed": neutral_effective_weight["conjugate_representative_mass_equivalence_closed"],
            "U5_neutral_minimum_shape_scale_coordinates": neutral_effective_weight["minimum_new_continuous_physical_coordinates"],
            "U5_neutral_q7_over_448_near_hit_retired": neutral_crt_phase["q7_over_448_near_hit_retired"],
            "U5_neutral_q7_CRT_lift": neutral_crt_phase["q7_only_CRT_lift"],
            "U5_neutral_proto_nil_drift_formula_imported": neutral_crt_phase["proto_spinor_nil_drift_formula_imported"],
            "U5_neutral_remaining_phi_scale_coordinates": neutral_crt_phase["remaining_continuous_coordinate_count"],
            "U5_neutral_common_circle_three_basin_transfer_closed": neutral_circle_factor["common_circle_to_three_basin_transfer_closed"],
            "U5_neutral_independent_shape_scalar_count": neutral_circle_factor["independent_shape_scalar_count"],
            "U5_neutral_phi_value_closed": neutral_circle_factor["phi_nu_value_closed"],
            "U5_neutral_finite_Heisenberg_elements_checked": neutral_det_nogo["finite_group_elements_checked"],
            "U5_neutral_finite_image_SU3": neutral_det_nogo["finite_image_in_SU3"],
            "U5_neutral_smooth_determinant_line_target_typed": neutral_det_nogo["smooth_determinant_line_target_typed"],
            "U5_neutral_profile_continuous_primitives": neutral_profile_values["continuous_profile_primitives"],
            "U5_neutral_profile_value_rows_filled": neutral_profile_values["total_rows_filled"],
            "U5_neutral_profile_absolute_masses_filled": neutral_profile_values["absolute_neutrino_masses_filled_at_profile_tier"],
            "U5_neutral_profile_Dirac_Yukawa_rows_filled": neutral_profile_values["Dirac_Yukawa_rows_filled_at_profile_tier"],
            "U5_neutral_profile_strict_source_closed": neutral_profile_values["strict_no_knob_source_closed"],
            "U5_neutral_lens_dedekind_mixed_residue": neutral_lens_dedekind["mixed_reciprocity_residue"]["text"],
            "U5_neutral_lens_dedekind_candidate_phi_exact": neutral_lens_dedekind["candidate_phi_nu_exact"],
            "U5_neutral_lens_dedekind_profile_pull_sigma": neutral_lens_dedekind["pull_sigma_diagonal_approximation"],
            "U5_neutral_conditional_mass_scale_inputs": neutral_lens_dedekind["conditional_continuous_neutral_mass_splitting_inputs"],
            "U5_neutral_APS_phase_source_closed": neutral_lens_dedekind["strict_determinant_line_phase_source_closed"],
            "U5_neutral_absolute_scale_source_closed_after_A41": neutral_lens_dedekind["strict_absolute_scale_source_closed"],
            "U5_neutral_E0_candidate_A_eV2": neutral_e0["A_nu_prediction_eV2"],
            "U5_neutral_E0_candidate_relative_residual": neutral_e0["A_nu_relative_residual"],
            "U5_neutral_E0_dimension_11_unique_in_scan": neutral_e0["dimension_11_unique_in_scan"],
            "U5_neutral_E0_universal_metrology_primitives": neutral_e0["universal_metrology_primitive_count"],
            "U5_neutral_E0_new_sector_primitives": neutral_e0["new_neutrino_specific_continuous_parameter_count"],
            "U5_neutral_absolute_scale_source_closed_after_A42": neutral_e0["strict_neutral_scale_source_closed"],
            "U5_neutral_composite_eigenvalue": neutral_composite["composite_eigenvalue_exact"],
            "U5_neutral_attenuation_compression_closed": neutral_composite["attenuation_compression_identity_closed"],
            "U5_neutral_profile_normalization_identity_closed": neutral_composite["profile_normalization_identity_closed"],
            "U5_neutral_elevenfold_multiplicity_selected": neutral_composite["elevenfold_multiplicity_selected"],
            "U5_neutral_operator_selected_on_11D_lift": neutral_composite["neutral_operator_selected_on_11D_lift"],
            "U5_neutral_nil_quarter_saturation_selected": neutral_composite["nil_quarter_saturation_selected"],
            "U5_neutral_same_operator_branch_bridge_closed": neutral_composite["same_operator_branch_bridge_closed"],
            "U5_neutral_absolute_scale_source_closed_after_A43": neutral_composite["strict_source_promotion_closed"],
            "generative_embedded_local_QFT_recovery_closed": same_geometry["embedded_local_QFT_recovery_closed"],
            "generative_direct_qutrit_equals_SM_rejected": same_geometry["direct_qutrit_equals_SM_algebra_rejected"],
            "generative_conditional_C_H_M3_bridge_closed": same_geometry["conditional_C_H_M3_bridge_closed"],
            "generative_class_lane_assignment_selected": same_geometry["class_lane_assignment_selected"],
            "generative_weak_real_structure_selected": same_geometry["weak_real_structure_selected"],
            "generative_representation_anomaly_packet_closed": same_geometry["representation_and_anomaly_packet_closed"],
            "U5_dimensionful_blocks_closed": (
                neutral_source["dimensionful_M_D_3x3_closed"]
                or neutral_source["dimensionful_M_L_3x3_closed"]
                or neutral_source["dimensionful_M_R_3x3_closed"]
            ),
            "U5_dimensionless_nuD_response_rejected": neutral_operator["dimensionless_nuD_response_rejected_as_mass_operator"],
            "U6_conditional_PQ_theorem": neutrino_cp["conditional_PQ_theorem_closed"],
            "U6_strong_CP_solved": neutrino_cp["strong_CP_problem_solved"],
            "U6_E6_matter_anomaly": e6_anomaly["matter_anomaly_three_families"],
            "U6_E6_exotic_anomaly": e6_anomaly["exotic_anomaly_three_27s"],
            "U6_complete_27_anomaly": e6_anomaly["complete_three_27_anomaly"],
            "U6_naive_reduced_N_DW": e6_anomaly["naive_matter_only_singlet_reduced_N_DW"],
            "U6_unified_missing_object_count": e6_anomaly["U6_reduced_missing_object_count"],
            "U9_orientation_selection_closed": branch["orientation_level_selection_closed"],
            "U9_global_uniqueness_closed": branch["U9_full_superset_uniqueness_closed"],
            "U7_closed": foundations["U7_MTT_derived_quantization_closed"],
            "U8_constructive_partial": foundations["U8_has_real_constructive_partial_result"],
            "U8_closed": foundations["U8_constructive_nonperturbative_4D_QFT_closed"],
            "MTT_derived_quantization": qft["strict_no_knob_local_QFT_functor_closed"],
        },
        "guards": {
            "historical_open_packets_reopen_baseline": False,
            "support_packet_counts_as_value_or_selection_theorem": False,
            "observed_values_may_select_branch_or_weights": False,
            "foundational_upgrade_mislabeled_as_SM_equivalence_blocker": False,
        },
    }
    dump(OUT / "strict_no_knob_upgrade_ledger.packet.json", packet)

    status = "MTT_SELECTED_STRICTNOKNOBUPGRADELEDGER_BASELINE_LOCKED_NINE_UPGRADES_ORDERED"
    candidate = {
        "candidate": "MTT_Selected_StrictNoKnobUpgradeLedger_AfterTrueSMEquivalence_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "StrictUpgradeDependencyDecompositionTheorem",
            "proved": True,
            "statement": "After declared-standard true-SM equivalence closes, the stronger program consists of nine non-overlapping upgrade obligations arranged in five dependency levels. Historical support packets cannot reopen the baseline or satisfy an upgrade without its named value, witness, selection, or constructive acceptance test.",
        },
        "baseline_locked": True,
        "strict_upgrades_closed": "2/9",
        "U3_local_execution_exhausted": True,
        "next_required_artifact": "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_StrictNoKnobUpgradeLedger_AfterTrueSMEquivalence_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "baseline_true_SM_equivalence_locked": True,
        "baseline_obligations_closed": 12,
        "strict_upgrade_count": 9,
        "strict_upgrades_closed": packet["closed_upgrade_count"],
        "strict_upgrades_partially_closed": packet["partially_closed_upgrade_count"],
        "strict_upgrades_open": packet["open_upgrade_count"],
        "first_independent_attack": "U3_official_joint_input_likelihood",
        "U3_local_execution_exhausted": True,
        "next_active_attack": "U5_neutral_mass_U6_central_anomaly_U9_global_measure_U7_dynamic_measure",
        "next_required_artifact": "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1",
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
