"""Run reproducibility checks for the MTT SM-parity closure repo."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"
REPORT = ROOT / "reports" / "verification_report.txt"
AUDITS = [
    "sm_parity_closure_ledger_audit.py",
    "core_axioms_measured_parameter_interface_audit.py",
    "sm_sector_embedding_interface_audit.py",
    "qm_qft_gr_recovery_interface_audit.py",
    "empirical_equivalence_ledger_audit.py",
    "no_knob_upgrade_backlog_audit.py",
    "actual_selected_sm_packet_anomaly_audit.py",
    "sm_equivalence_superset_strategy_controller_audit.py",
    "sm_equivalence_measured_replay_admission_audit.py",
    "sm_equivalence_measured_parameter_replay_manifest_audit.py",
    "sm_equivalence_reference_source_registry_audit.py",
    "sm_equivalence_reference_data_values_fill_audit.py",
    "sm_equivalence_tree_level_replay_seed_audit.py",
    "sm_equivalence_ckm_gauge_pmns_convention_fill_audit.py",
    "sm_equivalence_mixing_and_gauge_replay_audit.py",
    "sm_equivalence_common_rg_and_empirical_audit_audit.py",
    "sm_equivalence_rgpolicy_covariance_and_observable_suite_audit.py",
    "sm_equivalence_commonscale_value_transport_and_final_packet_certificate_audit.py",
    "sm_equivalence_crossrepo_qasu3_status_import_audit.py",
    "inverse_superset_reconstruction_audit.py",
    "inverse_superset_search_spec_audit.py",
    "inverse_qa_su3_first_search_run_audit.py",
    "selected_qa_su3_finite_cochain_construction_plan_audit.py",
    "selected_qa_su3_operator_source_import_audit.py",
    "selected_qa_su3_color_bundle_connection_endomorphism_interface_audit.py",
    "selected_qa_su3_same_source_visible_color_operator_packet_audit.py",
    "selected_qa_su3_ordered_valpha_pic0_source_repair_audit.py",
    "selected_terminal_monad_lane_pic0_quotient_source_audit.py",
    "selected_pic0_invariance_or_gerbe_twisted_de_source_audit.py",
    "selected_s3_class_restriction_projector_retention_audit.py",
    "selected_smooth_s3_twisted_source_lift_audit.py",
    "selected_s3_differential_cohomology_source_certificate_audit.py",
    "selected_visible_green_schwarz_operator_source_audit.py",
    "selected_routec_hym_operator_pipeline_audit.py",
    "selected_routec_hym_value_search_audit.py",
    "routec_selected_source_origin_way_forward_audit.py",
    "routec_selected_source_origin_lemma_audit.py",
    "finite_emission_morphism_phifin_audit.py",
    "selected_nonidentity_rhoe_transition_source_audit.py",
    "projective_gerbe_rhoe_source_promotion_audit.py",
    "selected_visible_chern_weil_operator_source_audit.py",
    "selected_nonsplit_rank2_or_routec_same_source_packet_audit.py",
    "same_source_symmetry_breaking_source_audit.py",
    "selected_orientation_carrying_de_dotd_source_audit.py",
    "selected_source_origin_and_alpha1_driver_audit.py",
    "selected_phifin_alpha1_payload_audit.py",
    "selected_spectral_galerkin_projector_retention_data_audit.py",
    "selected_routec_strominger_galerkin_solve_spec_audit.py",
    "selected_routec_strominger_galerkin_first_run_audit.py",
    "selected_routec_source_selector_and_basis_theorem_audit.py",
    "selected_routec_source_provenance_or_basis_certificate_audit.py",
    "selected_phifin_payload_or_bn_basis_emission_audit.py",
    "selected_routec_r1_source_or_r4_bn_basis_fill_audit.py",
    "selected_routec_selected_primitive_emission_search_audit.py",
    "selected_routec_nonidentity_rhoe_bn_construction_audit.py",
    "selected_routec_smooth_bn_galerkin_lift_audit.py",
    "selected_routec_de_action_on_smooth_bn_audit.py",
    "selected_source_paper_integration_manifest_audit.py",
    "selected_source_paper_appendix_drafts_audit.py",
    "selected_routec_sector_projectors_dotd_on_smooth_bn_audit.py",
    "selected_routec_c1_primitive_response_on_smooth_bn_audit.py",
    "selected_routec_noninvariant_c1_primitive_search_audit.py",
    "selected_routec_primitive_source_selection_audit.py",
    "selected_routec_fiberclass_observable_invariance_or_gaugefix_audit.py",
    "selected_routec_higherorder_fullresponse_flavor_splitting_audit.py",
    "selected_routec_first_correction_search_or_galerkin_run_audit.py",
    "selected_routec_correction_source_emission_or_selected_galerkin_values_audit.py",
    "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve_audit.py",
    "selected_routec_selected_c1_response_operator_emission_audit.py",
    "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_audit.py",
    "selected_routec_basis_transport_primitive_source_theorem_audit.py",
    "selected_routec_basis_transport_primitive_source_proof_or_counterexample_audit.py",
    "selected_routec_weylpair_basis_transport_or_vertex_source_theorem_audit.py",
    "selected_routec_weylpair_aselected_assembly_or_source_proof_audit.py",
    "selected_routec_weylpair_source_provenance_lemma_audit.py",
    "selected_routec_weylpair_source_to_c1_transfer_map_audit.py",
    "selected_routec_weylpair_sector_routing_source_lemma_audit.py",
    "selected_routec_weylpair_sector_charge_or_chirality_certificate_audit.py",
    "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem_audit.py",
    "selected_routec_hybrid_matter_slot_galerkin_source_packet_audit.py",
    "selected_routec_selected_operator_source_and_overlap_tensor_packet_audit.py",
    "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet_audit.py",
    "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_audit.py",
    "selected_routec_samesource_matter_slot_overlap_operator_packet_audit.py",
    "selected_routec_samesource_operatorpacket_fill_or_nogo_audit.py",
    "selected_routec_sourceemission_minimal_subpacket_attack_plan_audit.py",
    "selected_routec_operatorsourceidentity_subpacket_audit.py",
    "selected_routec_rank2_l2_or_routec_residual_fill_audit.py",
    "selected_routec_stability_hym_or_routec_residual_source_audit.py",
    "selected_routec_global_destabilizer_enumeration_or_selected_residual_audit.py",
    "selected_routec_selected_ah_goodcover_promotion_hym_certificate_audit.py",
    "selected_routec_ah_source_selection_or_routec_selected_residual_audit.py",
    "selected_routec_equalradius_gauduchon_hym_bridge_audit.py",
    "selected_routec_hym_operator_values_gate_audit.py",
    "selected_hym_connection_to_finite_operator_extraction_audit.py",
    "selected_hym_gaugefixed_connection_or_galerkin_solve_audit.py",
    "selected_hym_adjoint_transfer_functor_audit.py",
    "selected_hym_adjoint_galerkin_first_coefficient_solve_audit.py",
    "selected_end0_basis_differential_table_or_bn_identification_audit.py",
    "selected_end0_direct_differential_table_from_ah_ext_forms_audit.py",
    "selected_normalized_ext_local_form_table_audit.py",
    "selected_ext_l2_theta_quadrature_table_audit.py",
    "selected_ext_overlap_hym_hodge_projector_table_audit.py",
    "selected_nonlinear_hym_correction_coefficient_solve_audit.py",
    "selected_full_exps_hym_newton_replay_audit.py",
    "selected_hym_operator_payload_extraction_from_diagonal_replay_audit.py",
    "selected_end0_de_payload_from_diagonal_hym_audit.py",
    "selected_riesz_green_dotd_from_diagonal_end0_de_audit.py",
    "selected_t1t2_covariant_green_and_transfer_probe_audit.py",
    "selected_offdiagonal_ext_control_or_sector_transfer_audit.py",
    "selected_physical_dotd_alpha1_or_end0_sector_routing_audit.py",
    "selected_alpha1_tangent_promotion_or_sector_routing_theorem_audit.py",
    "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill_audit.py",
    "selected_end0_to_sector_functor_source_and_value_packet_audit.py",
    "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct_audit.py",
    "selected_sector_zero_mode_adjointtriplet_realization_theorem_audit.py",
    "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill_audit.py",
    "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem_audit.py",
    "selected_sector_zero_mode_source_payload_search_or_emission_attempt_audit.py",
    "selected_sectorcharge_gram_transfernormalization_packet_audit.py",
    "selected_sectorcharge_1m_dirac_rule_attempt_audit.py",
    "selected_1m_dirac_source_or_u10ubar5_polarization_audit.py",
    "selected_u10ubar5_1m_samebranch_emission_attempt_audit.py",
    "selected_matterslot_transversality_readout_functional_audit.py",
    "selected_matterslot_grading_or_sectionring_readout_audit.py",
    "selected_terminalmonad_matterslot_sectionring_source_selector_audit.py",
    "selected_terminalmonad_baseorder_ahbinding_smslotmap_audit.py",
    "selected_terminalmap_sourceprinciple_or_smslotfunctor_audit.py",
    "terminaladmissible_principle_promotion_or_smslotfunctor_audit.py",
    "terminaladmissible_axiominsertion_and_smslotfunctor_audit.py",
    "selected_smslotfunctor_valueemission_or_axiompatch_audit.py",
    "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues_audit.py",
    "selected_smslotfunctor_sixarrow_source_emission_audit.py",
    "selected_smslotfunctor_polarization_overlap_source_emission_audit.py",
    "selected_smslotfunctor_overlapkernel_source_emission_audit.py",
    "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger_audit.py",
    "selected_matterslot_readout_backimport_from_smslotfunctor_audit.py",
    "selected_dynamic_overlapkernel_or_c1primitive_source_emission_audit.py",
    "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission_audit.py",
    "selected_primitivefibershift_or_typedretardedselector_sourcetheorem_audit.py",
    "selected_crossrepo_alpha1_driver_replay_import_audit.py",
    "selected_visible_routec_phifin_alpha1_derivative_bridge_audit.py",
    "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_audit.py",
    "selected_c1_frontier_after_alpha1_import_audit.py",
    "selected_stationaryprojector_dotd_integrated_frontier_audit.py",
    "selected_primitivec1_or_weylpair_sectorrouting_sourceemission_audit.py",
    "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_audit.py",
    "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_audit.py",
    "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_audit.py",
    "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_audit.py",
    "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_audit.py",
    "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission_audit.py",
    "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_audit.py",
    "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun_audit.py",
    "selected_primitivevertex_source_or_basistransport_selectiontheorem_audit.py",
    "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun_audit.py",
    "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket_audit.py",
    "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission_audit.py",
    "selected_residual_weylpolynomial_source_theorem_attempt_audit.py",
    "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill_audit.py",
    "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill_audit.py",
    "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution_audit.py",
    "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun_audit.py",
    "selected_enrichedweylpairsourceprovenance_or_galerkinc1values_audit.py",
    "selected_dynamicc1transfertensor_or_galerkinc1values_audit.py",
    "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest_audit.py",
    "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run_audit.py",
    "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution_audit.py",
    "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun_audit.py",
    "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate_audit.py",
    "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution_audit.py",
    "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution_audit.py",
    "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch_audit.py",
    "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom_audit.py",
    "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve_audit.py",
    "selected_c1defectfunctionalsource_or_independentquadraturedatafill_audit.py",
    "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable_audit.py",
    "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues_audit.py",
    "selected_i10_payloadcertificate_or_independentquadraturevaluesfill_audit.py",
    "selected_stromingertracec1firstvariation_or_quadratureexecutionplan_audit.py",
    "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun_audit.py",
    "selected_tracemapandbasisvalues_or_primitiverowsexecution_audit.py",
    "selected_primitiverowsexecution_or_dynamicdotdtracebinding_audit.py",
    "selected_dynamicc1proofcycle_condensation_or_cycleexit_audit.py",
    "selected_cycleexit_minimizertrace_or_independentquadraturerows_audit.py",
    "selected_firstvariationboundary_or_primitivequadraturerows_valuefill_audit.py",
    "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution_audit.py",
    "selected_c1variationprinciplederivation_or_quadratureenginerun_audit.py",
    "selected_physicalvariationprinciplesource_or_quadraturekernelvalues_audit.py",
    "selected_c1kernelvaluesexecution_or_physicalsourcepromotion_audit.py",
    "selected_c1measurepairing_or_physicalactionidentity_audit.py",
    "selected_c1tracemeasurepromotion_or_actionboundaryproof_audit.py",
    "selected_physicalc1actionidentity_or_samesourcebselectedemission_audit.py",
    "selected_physicalactionsourceemission_or_honestgalerkinreplacement_audit.py",
    "selected_routeaemission_or_routebgalerkinrows_execution_audit.py",
    "selected_physicalmeasure_or_finitegalerkinpromotion_audit.py",
    "selected_physicalmeasureidentity_or_routeaemissionclosure_audit.py",
    "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation_audit.py",
    "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation_audit.py",
    "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation_audit.py",
    "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration_audit.py",
    "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation_audit.py",
    "selected_phifinc1_actionrestriction_or_boundarysource_emission_audit.py",
    "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement_audit.py",
    "selected_physicalactionrestrictionemission_or_independentgalerkinrows_audit.py",
    "selected_physicalsourceemissionvalues_or_honestgalerkinexecution_audit.py",
    "selected_routeaphysicalemissionvalues_or_routebrowexecution_audit.py",
    "selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission_audit.py",
    "selected_dynamicphifintracebinding_or_primitiverowformulaexecution_audit.py",
    "selected_physicalactionrestrictionclause_or_primitivekernelformula_audit.py",
    "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows_audit.py",
    "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution_audit.py",
    "selected_physicalactionsourcerule_or_independentprimitivekernelformula_audit.py",
    "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows_audit.py",
    "selected_dynamicc1transferprimitivetensorhessian_or_independentrows_audit.py",
    "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution_audit.py",
    "selected_phifinc1dynamictransferidentityproof_or_firstindependentrowformularun_audit.py",
    "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource_audit.py",
    "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource_audit.py",
    "selected_firstrowprovenancepromotion_or_allrowsweylexecution_audit.py",
    "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource_audit.py",
    "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem_audit.py",
    "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun_audit.py",
    "selected_physicalsourcecertificatefill_or_routebindependentrunexecution_audit.py",
    "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap_audit.py",
    "selected_routeb_quadratureindependencefill_or_selectedbasisgap_audit.py",
    "selected_routeb_selectedbasisindependencefill_or_rowsourcegap_audit.py",
    "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill_audit.py",
    "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate_audit.py",
    "selected_primitivekernelslotcoverage_or_variationhessiangap_audit.py",
    "selected_variationoperatorshapecompatibility_or_hessiansourcegap_audit.py",
    "selected_hessiancountertermsource_bvector_theoremtemplate_audit.py",
    "selected_phifinc1emission_or_independenthessianquadraturesource_audit.py",
    "selected_finalsourceemission_bestcurrentfill_or_nogowitness_audit.py",
    "selected_finalsourceemission_actualfill_or_nogowitness_audit.py",
    "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution_audit.py",
    "selected_routeb_independentquadraturepayload_schema_or_executionworkorder_audit.py",
    "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap_audit.py",
    "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract_audit.py",
    "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure_audit.py",
    "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset_audit.py",
    "selected_physicalphifinc1action_or_independentrowkernelsource_theorem_audit.py",
    "selected_sourcetheorem_push_attempt_or_minimalnewlemma_audit.py",
    "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel_audit.py",
    "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom_audit.py",
    "selected_phifinc1actionkernel_theorem_attempt_or_i10binding_audit.py",
    "selected_i10bindingstack_gate_or_firstvariationcertificate_audit.py",
    "selected_i11firstvariationcertificate_fill_or_quadraturetable_audit.py",
    "selected_i11tracemap_dynamicextension_or_firstvariationgap_audit.py",
    "selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap_audit.py",
    "selected_i11tracemap_transportdotdimport_or_boundaryc1gap_audit.py",
    "selected_i11_c1coordinatechart_or_physicalsourcegap_audit.py",
    "selected_i11_physicalsource_valueclosure_or_fiveclausegap_audit.py",
    "selected_i11_routeb_nearmiss_or_rowsourcetheorem_audit.py",
    "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback_audit.py",
    "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation_audit.py",
    "selected_physicalboundaryfirstvariation_or_selectedsourceemission_audit.py",
    "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation_audit.py",
    "selected_finalsmparitygapmatrix_or_closureattempt_audit.py",
    "selected_commonscaleyukawahiggstransport_or_finalreplayaudit_audit.py",
    "selected_rgengineexecution_or_selectedsmpacketcertificateintegration_audit.py",
    "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration_audit.py",
    "selected_centralvaluetolerancepolicyexecution_or_fullcovarianceprofile_audit.py",
    "selected_finalintegratedempiricalreplayaudit_or_remainingtwogates_audit.py",
    "selected_acceptedrgtransportvalues_or_qasu3sourcepacket_audit.py",
    "selected_qasu3sourcepacket_or_finalsmparityclosure_audit.py",
    "selected_true_sm_equivalence_frontier_after_smparityclosure_audit.py",
    "selected_precisionempiricalreplaysuite_or_trueequivalence_audit.py",
    "selected_latest_smparityclosure_status_or_trueequivalencefrontier_audit.py",
    "selected_finalintegratedsmparityreplayaftersourceidentitypatch_audit.py",
    "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor_audit.py",
    "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance_audit.py",
    "selected_thresholdpolerunningmaps_or_covarianceprofile_audit.py",
    "selected_polethresholdresidualvalues_or_covarianceprofile_audit.py",
    "selected_fullcovarianceprofile_or_multiloopconventionaudit_audit.py",
    "selected_correlatedprofilevalues_or_localqftobservablevalues_audit.py",
    "selected_localqftobservablerows_or_finaltruesmequivalencegap_audit.py",
    "selected_precisionqftobservablerows_or_actualqasu3packet_audit.py",
    "selected_precisionobservablepromotionpolicy_or_loopqftvalues_audit.py",
    "selected_loopqcddecayproxyvalues_or_fullprecisionqft_audit.py",
    "selected_runningmasshiggsdecayproxy_or_precisionwidths_audit.py",
    "selected_higgsdecayresidualaudit_or_precisionpromotion_audit.py",
    "selected_multiloophiggsqqformula_or_fullwidthpolicy_audit.py",
    "selected_completehiggschannelledger_or_totalwidthpolicy_audit.py",
    "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay_audit.py",
    "selected_higgsprecisionsidecars_or_uniformformularows_audit.py",
    "selected_higgscovarianceprofilecontract_or_uniformformularows_audit.py",
    "selected_higgsuniformkernelrows_or_fullchannelvalues_audit.py",
    "selected_higgssskernelrow_or_remainingchannels_audit.py",
    "selected_higgsggkernelrow_or_electroweakrows_audit.py",
    "selected_higgsgammagammakernelrow_or_remainingew_audit.py",
    "selected_higgsewbenchmarkpolicy_or_fullformulas_audit.py",
    "selected_higgsprecisionpromotionmatrix_or_operatorprofile_audit.py",
    "selected_higgspromotionpriority_or_correlatedprofileblueprint_audit.py",
    "selected_higgsgammagammacorrection_or_qcdthresholdrows_audit.py",
    "selected_higgsqcdthresholdrows_or_correlatedprofilefill_audit.py",
    "selected_higgssupersetqcdrepaircontroller_or_values_audit.py",
    "selected_higgsqcdrepairvalues_or_profilecovarianceblock_audit.py",
    "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment_audit.py",
    "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay_audit.py",
    "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade_audit.py",
    "selected_higgscomputedchannelrefresh_or_totalwidthreplay_audit.py",
    "selected_higgsremainingewformularows_or_precisiontotalwidth_audit.py",
    "selected_higgsewformulakernelexecution_or_precisionimportrows_audit.py",
    "selected_higgstenchannelcovarianceprofile_or_branchingreplay_audit.py",
    "selected_higgsprecisionrows_or_fullcorrelatedprofile_audit.py",
    "selected_higgsprecisionvaluefill_or_profileconventionimport_audit.py",
    "selected_higgsprofileconventiondatafile_or_precisionrowvalues_audit.py",
    "selected_higgsacceptedprofileimport_or_rowvaluereplacement_audit.py",
    "selected_higgsexternalprofilepacketfill_or_rowformulavalues_audit.py",
    "selected_higgsexternalprofiledata_or_routeaformularows_audit.py",
    "selected_higgshomogeneousprofile_or_routeaformulacovariance_audit.py",
    "selected_higgsofficialprofile_or_routeaformuladifferentiation_audit.py",
    "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport_audit.py",
    "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood_audit.py",
    "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision_audit.py",
    "selected_higgsrouteaderivativeengineexecution_or_precisiondecision_audit.py",
    "selected_higgsqcdrouteaderivativerows_or_precisiondecision_audit.py",
    "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision_audit.py",
    "selected_higgsoffshellzgammaroutea_or_precisionimportdecision_audit.py",
    "selected_higgsfinalsmparityprofilepolicy_or_remainingrouteakernels_audit.py",
    "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy_audit.py",
    "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor_audit.py",
    "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade_audit.py",
    "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill_audit.py",
    "selected_latest_trueequivalencefrontier_or_valueemissioncutset_audit.py",
    "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch_audit.py",
    "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining_audit.py",
    "selected_qasu3candidatepayloadfill_or_profilesourceacquisition_audit.py",
    "selected_orderedvalphapic0source_or_profileworkspaceimport_audit.py",
    "selected_terminalsourceswitch_or_operatorpic0gerbede_audit.py",
    "selected_visibleoperatorpayload_or_routechymresidual_audit.py",
    "selected_hymconnectionextraction_or_sourceoriginlemma_audit.py",
    "selected_postsmparity_trueequivalence_sourceupgrade_kernel_audit.py",
    "selected_postsmparity_sourcetheorembundle_or_trueequivalence_exitmatrix_audit.py",
    "selected_trueequivalence_currentfrontier_after_externalrg_smslot_audit.py",
    "selected_precisionprofileloopvalues_or_actualqasu3operatorpayload_currentexecution_audit.py",
    "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt_audit.py",
    "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill_audit.py",
    "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues_audit.py",
    "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem_audit.py",
    "selected_covarianceprofilepayload_or_qasu3selectedslotvalues_audit.py",
    "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof_audit.py",
    "selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure_audit.py",
    "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure_audit.py",
    "selected_secondqasu3operatorslotclosure_or_productionprofileimport_audit.py",
    "selected_thirdqasu3operatorslotclosure_or_pic0gerbereplacement_audit.py",
    "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource_audit.py",
    "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill_audit.py",
    "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun_audit.py",
    "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun_audit.py",
    "selected_chernweilde_or_determinanttorsion_threeslotclosingrun_audit.py",
    "selected_detransition_or_determinanttorsion_twoslotclosingrun_audit.py",
    "selected_transitionpayload_or_heattorsionresponse_onegateattack_audit.py",
    "selected_tracepayload_or_fullhymoperatoremission_audit.py",
    "selected_heattorsionresponse_finalgate_audit.py",
    "selected_smparityfrozenboundary_or_postsmparityfrontier_audit.py",
    "selected_dynamicqasu3_or_c1response_postsourcefrontier_audit.py",
    "selected_postsmparity_workbreakdown_labels_audit.py",
    "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest_audit.py",
    "selected_psm_c1_01_sourceruleemission_or_psm_c1_04_bselectedsidecar_audit.py",
    "selected_psm_c1_01_unpatchedsourcelemma_or_routeb_rowkernelexecution_audit.py",
    "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction_audit.py",
    "selected_psm_c1_02_physicalselectionlemma_or_psm_c1_04_hessiansourcerows_audit.py",
    "selected_psm_c1_06_sectorrows_or_replayindependencecertificate_audit.py",
    "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport_audit.py",
    "selected_honestkernelexport_rowsourcefill_or_sourceidentityderivationattempt_audit.py",
    "selected_primitiverows_sourcepromotion_or_independentformuladerivation_audit.py",
    "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill_audit.py",
    "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource_audit.py",
    "selected_psm_c1_02_physicalactionidentity_or_honestquadratureemission_audit.py",
    "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion_audit.py",
    "selected_psm_c1_02_selectedsourcepromotionpacket_audit.py",
    "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport_audit.py",
    "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill_audit.py",
    "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill_audit.py",
    "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill_audit.py",
    "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource_audit.py",
    "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill_audit.py",
    "selected_psm_c1_02_sourceidentitylemma_derivation_attempt_audit.py",
    "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel_audit.py",
    "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision_audit.py",
    "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution_audit.py",
    "selected_psm_c1_02_localreplayreconciliation_or_unpatchedkernelexecutionplan_audit.py",
    "selected_psm_c1_02_unpatchedkernelexecutionplan_or_honestgalerkinexport_audit.py",
    "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport_audit.py",
    "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket_audit.py",
    "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution_audit.py",
    "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution_audit.py",
    "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution_audit.py",
    "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource_audit.py",
    "selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource_audit.py",
    "selected_psm_c1_02_variationalprojectionbridge_or_rowsource_audit.py",
    "selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma_audit.py",
    "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem_audit.py",
    "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables_audit.py",
    "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run_audit.py",
    "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues_audit.py",
    "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision_audit.py",
    "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion_audit.py",
    "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit_audit.py",
    "selected_differentiatedphifinc1_axiom_derivation_attempt_or_minimalobstruction_audit.py",
    "selected_phifinc1_physicalvariation_sourcetheorem_proof_attempt_or_countermodel_audit.py",
    "selected_routec_weylvariation_sourceprinciple_or_kernelclosure_audit.py",
    "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion_audit.py",
    "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution_audit.py",
    "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution_audit.py",
    "selected_localdynamicc1paperappendix_or_unpatchedkernelexecutionplan_audit.py",
    "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun_audit.py",
    "selected_finitec1sourceidentitytheorem_or_newindependentrows_audit.py",
    "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission_audit.py",
    "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill_audit.py",
    "selected_samesourcephifinc1emission_or_independentrowsactualfill_audit.py",
    "selected_physicalphifinc1actionidentity_or_independentrowsourceexport_audit.py",
    "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable_audit.py",
    "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof_audit.py",
    "selected_independentquadratureruleandhessianbsource_or_routeaactionidentity_audit.py",
    "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation_audit.py",
    "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation_audit.py",
    "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof_audit.py",
    "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor_audit.py",
    "selected_physicaldotd_sectorrouting_after_hymfirstsolve_audit.py",
    "selected_zero_mode_basis_from_hym_projector_source_theorem_audit.py",
    "selected_hym_projector_zeromode_basis_value_emission_audit.py",
    "selected_hym_projector_source_promotion_route_a_audit.py",
    "phifin_bn_modelactive_equivalence_or_minimizer_trace_audit.py",
    "selected_gauge_transported_bn_phifin_trace_audit.py",
    "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset_audit.py",
    "selected_transport_conjugation_validator_replay_audit.py",
    "selected_transportreplay_imported_or_u10ubar5_1m_source_audit.py",
    "selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay_audit.py",
    "selected_finite_projector_source_promotion_audit.py",
    "selected_dotd_alpha1_transport_derivative_probe_audit.py",
    "selected_alpha1_source_strength_normalization_theorem_audit.py",
    "selected_alpha1_source_strength_value_emission_attempt_audit.py",
    "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt_audit.py",
    "selected_samesource_alpha1_normalization_pin_down_kernel_audit.py",
    "selected_samesource_alpha1_normalization_packet_fill_attempt_audit.py",
    "selected_samesource_alpha1_normalization_sourceidentity_partial_fill_audit.py",
    "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt_audit.py",
    "visible_routec_sourceidentity_or_typedbn_derivative_contract_audit.py",
    "visible_routec_sourceidentity_or_typedbn_derivative_partial_fill_audit.py",
    "visible_routec_phifin_alpha1_derivative_fill_audit.py",
    "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution_audit.py",
]


def run_audit(script: str) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, script], cwd=CORPUS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout


def certificate_status() -> str:
    lines = ["Certificates", "============", ""]
    for path in sorted(CERTS.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        lines.append(f"{path.name}: {data.get('status', 'UNKNOWN')}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parts = [
        "MTT SM-parity closure verification report",
        "========================================",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Corpus: {CORPUS}",
        "",
    ]
    failures = []
    for script in AUDITS:
        code, output = run_audit(script)
        parts.append(f"## {script}")
        parts.append("")
        parts.append(output.rstrip())
        parts.append("")
        if code != 0:
            failures.append(script)
    parts.append(certificate_status())
    if failures:
        parts.append(f"Verification result: FAIL ({', '.join(failures)})")
        result = 1
    else:
        parts.append("Verification result: PASS")
        parts.append("SM-parity ledger, measured-parameter interface, SM sector embedding interface, QM/QFT/GR recovery interface, empirical equivalence ledger, corpus-backed no-knob upgrade backlog, selected SM packet/anomaly audit, inverse superset reconstruction protocol, inverse search spec, inverse Qa/SU3 first search run, selected Qa/SU3 finite cochain construction plan, operator-source import audit, color-bundle connection/endomorphism interface, same-source visible/color operator packet attempt, ordered VAlpha/Pic0 source repair, terminal monad lane Pic0 quotient audit, Pic0 invariance/gerbe-twisted D_E source reduction, selected S3 class restriction/projector retention, selected smooth S3 twisted-source lift reduction, selected S3 differential-cohomology source certificate, selected visible Green-Schwarz/operator-source gate, Route-C/HYM operator pipeline gate, selected Route-C/HYM value search, Route-C source-origin way-forward hunt, Route-C source-origin lemma reduction, Phi_fin finite emission schema, selected non-identity rho_E transition-source reduction, projective gerbe rho_E S3-source promotion, selected visible Chern-Weil/operator-source reduction, selected non-split rank-two or Route-C same-source packet reduction, same-source symmetry-breaking source reduction, selected orientation-carrying D_E/dotD source reduction, selected source-origin/alpha1-driver reduction, selected Phi_fin alpha1 payload attempt, selected spectral Galerkin/projector-retention reduction, selected Route-C/Strominger Galerkin solve spec, first-run manifest, source-selector/basis cutset theorem, dual provenance/basis closure attempt, Phi_fin/B_N emission contracts, strict R1/R4 fill attempt, selected primitive emission search, first non-identity rhoE numerical packet, smooth B_N Galerkin scaffold, finite D_E action matrix layer, selected-source paper integration manifest, selected-source paper appendix drafts, sector projectors/dotD on smooth B_N, canonical C1 primitive response on smooth B_N, non-invariant C1 primitive candidate search, primitive source-selection/fiber-rule audit, fiber-class observable-invariance/gauge-fix attempt, higher-order/full-response flavor-splitting criterion, first correction/Galerkin parallel run, correction source-emission audit, selected DeltaTheta C1 solve gate, selected C1 response-operator emission audit, smart C1 rebuild iteration, basis-transport primitive source theorem slot, primitive-only counterexample, Weyl-pair basis-transport/vertex source gate, conditional Weyl-pair A assembly, Weyl-pair source provenance reduction, conditional source-to-C1 transfer map, sector-routing source attempt, sector charge/chirality certificate attempt, matter-slot/block-sector theorem reduction, hybrid matter-slot Galerkin packet attempt, selected operator-source/overlap packet audit, selected C1 routing/normalization/overlap source attempt, selected matter-slot charge/overlap-normalization theorem attempt, same-source matter-slot/overlap operator packet contract, same-source operator-packet fill/no-go attempt, source-emission minimal subpacket attack plan, operator-source identity subpacket reduction, rank-two L2 cohomology fill checkpoint, stability/HYM central-neutral subtheorem, reduced AH global rank-one line enumeration, reflexive-hull/conditional HYM bridge, selected ordered AH/Cech source-layer promotion, equal-radius Gauduchon HYM existence bridge, selected HYM operator-value extraction gate, HYM-connection-to-finite-operator extraction contract, selected gauge-fixed HYM/Galerkin solve gate, selected HYM adjoint-transfer functor, first adjoint-Galerkin coefficient solve attempt, dual End0 table/B_N identification attempt, direct End0 AH/Ext form-table attempt, normalized Ext local-form table, selected Ext L2 theta quadrature table, eta_00 overlap/Hodge/projector table, first trace-free HYM correction solve, diagonal exp(S) HYM replay, diagonal HYM operator payload extraction, diagonal End0 D_E payload extraction, protected diagonal End0 Riesz/Green/dotD extraction, T1/T2 covariant Green versus transfer probe, selected row-model off-diagonal Ext control, selected Ext-density dotD tangent extraction, alpha1 promotion theorem slot, alpha1 value-fill no-go, End0-to-sector functor contract, sector zero-mode tensor skeleton, universal End0 tensor-product carrier, sector zero-mode adjoint-triplet representation theorem, End0 action/routing value-fill attempt, sector source-action/routing cutset theorem, sector source-payload emission attempt, selected zero-mode-basis HYM-projector bridge theorem, finite HYM-projector zero-mode value emission, Route A source-promotion attempt, gauge-transported Phi_fin trace, symbolic transport-conjugation validator replay, dotD alpha1 transport-derivative probe, alpha1 source-strength normalization theorem, alpha1 source-strength value emission attempt, same-source alpha1 normalization pin-down kernel, exact alpha1 normalization packet fill attempt, and alpha1 source-identity/retarded-kernel two-lane attempt are built; measured inputs are downstream typed parity data or discovery-only inverse-search data; formal lifts are diagnostic only; finite SU(5) transversality and conditional C1 transfer are exact, rank-two H1/nonzero Ext now passes under the terminal section principle, V_alpha is stable at the selected equal-radius Gauduchon metric, abstract HYM existence is bridged, the rank-2-to-rank-3 mismatch is reduced by the no-knob End_0(V_alpha) functor, eta_00 now has exact AH transition factors, unit L2 norm, harmonic row status, Hodge/Lambda row data, a rank-one projector, a T3 trace-free correction, a converged diagonal exp(S) replay, determinant-one diagonal metric/connection summaries, an induced End0 operator formula D_E=d+ad(du*T3), a protected T3 zero-mode Riesz projector plus zero-mean Green operator, a pure-gauge T1/T2 covariant Green theorem, zero T1/T2 projection for the selected row-model Ext source, a linearized HYM Ext-density tangent with dotD Frechet replay, a rank-19 carrier with six adjoint triplets plus a Higgs singlet, a proof that the adjoint/singlet representation type is forced once selected End0 sector actions are emitted, a conditional invariant-Gram normalization lemma, a proof that closure must come through either selected rho_s source action or selected matter-slot routing source payload, a concrete canonical rho_candidate source map matching the selected diagonal End0 T3 lane, a theorem proving exactly how same-source HYM projectors would promote it, a finite model-active projector packet with rank 3 matter projectors, rank 1 Higgs projector, positive gap, ordered zero-mode basis ids, End0-equivariance, a gauge-transported functional selected Phi_fin trace, a symbolic finite validator replay for selected projector/Riesz/Green/source identities, the transported dotD source formula dU/dalpha=-(du/dalpha)ad(T3)U, the theorem that alpha1_driver_verified is equivalent to same-branch source-strength normalization du/dalpha1=h_ext, a conditional unit candidate lambda_alpha1=1 with ||h_ext||_L2=0.03961411527057935, an executable five-field acceptance kernel for promoting it, a filled candidate packet with lambda_alpha1=1 and N_alpha1(h_ext)=1 that fails final validation only on selected-source/provenance gates, and a two-lane proof attempt showing the common remaining object is a selected visible/Route-C source certificate with same-branch alpha1 derivative or an equivalent typed B_N retarded derivative; the next minimal gate is that certificate/typed derivative.")
        parts.append("The SM-equivalence CKM/gauge/PMNS convention fill is built: CKM and PMNS seed matrices are replay-ready with unitarity checks, the gauge packet fixes the M_Z-scale normalization formulas, and alpha_em(M_Z), covariance/profile policy, RG transport, and empirical replay remain open.")
        parts.append("The visible Route-C source identity / typed B_N derivative contract is now executable: it provides a dual-lane template and validator binding the selected source-identity lane and typed retarded-derivative lane to the already-filled alpha1 packet. The next minimal gate is filling either Lane A selected source identity or Lane B typed B_N retarded derivative.")
        parts.append("The finite projector source-promotion theorem is now named explicitly: the emitted B_N projector values promote to selected stationary source data only after exact transport conjugation P_s^sel=U P_s^model U^-1; the raw untransported packet remains unpromoted, and dotD_alpha1 plus matter-slot routing remain open.")
        parts.append("The partial fill promotes the stationary Lane A visible/Route-C source identity and visible operator source by symbolic transport-conjugation theorem; the remaining minimal Lane A blockers are Phi_fin alpha1 payload, same-branch alpha1 derivative, and honest dotD replay.")
        parts.append("The visible Route-C Phi_fin alpha1 derivative fill attempt executes that next gate and proves the exact obstruction: the dotD transport formula is available, but selected Phi_fin alpha1 payload values and theorem-derived h_ext alpha1-driver normalization are still absent, so the validator must remain open without lifted flags.")
        parts.append("The Phi_fin alpha1 payload / typed B_N retarded execution artifact imports the same-branch alpha1 bridge: alpha1 derivative and honest dotD replay are retired as active blockers, while the full validator remains open exactly because selected dynamic Phi_fin/C1 payload values are not emitted.")
        parts.append("The same-source alpha1 normalization packet now imports that theorem-derived source identity; its remaining validator failures are source-strength coordinate, selected normalization functional or typed transfer, tangent selection, and sector dotD equality.")
        parts.append("The alpha1 source-strength/transfer fill attempt tests both legal routes and identifies the next cutset as selected sector charge/chirality plus selected sector Gram/transfer normalization before a typed B_N alpha1 tangent and honest dotD replay can be emitted.")
        parts.append("The sector-charge/Gram-transfer packet proves the Gram scalar is conditionally fixed after selected rho_s, but transfer normalization remains unpromoted until selected sector charge/chirality or selected zero-mode/rho_s source emission is supplied.")
        parts.append("The sector-charge / 1_M Dirac-neutrino attempt imports the E6/SU(5) dictionary structurally: 1_M=N^c and bar5_M 1_M 5_H -> L N^c H_u route nuD to the non-10/shift candidate with d, while selected U10/Ubar5 polarization and selected 1_M source emission remain open.")
        parts.append("The selected 1_M Dirac source / U10-Ubar5 polarization gate now compares two legal promotion routes: Route A has exact q79 SU(5) finite support U10=I3, Ubar5=F plus the structural 1_M rule, and Route B has model-active HYM projector support; both reduce to same-branch selected source emission.")
        parts.append("The same-branch U10/Ubar5/1M emission attempt imports the selected stationary rho_s/projector/Riesz/Green source as closed, so the remaining blocker is sharpened to a selected matter-slot transversality readout functional rather than generic source promotion.")
        parts.append("The matter-slot transversality readout attempt proves a useful no-go: selected stationary rho_s invariants are identical across u,d,e,N, so rho_s alone cannot emit the 10M/bar5M/1M split; the next object is a selected matter-slot grading or section-ring readout.")
        parts.append("The matter-slot grading/section-ring readout attempt ranks the typed monad/Cech/section-ring lane as primary: central-circle neutrality forces L3-K2=(1,-2,0) inside the terminal lane and monad sufficiency proves validator readiness, but terminal lane selection, base order, Pic0/operator discipline, and the map to SM matter slots remain open.")
        parts.append("The terminal-monad matter-slot source-selector reduction imports the q79 two-switch table and ordered-layer Pic0 quotient: Pic0 is no longer the ordered-source blocker at the Chern/H1/ordinary-curvature layer, so the next gate is selected terminal lane, base order, AH/Cech binding, and the section-ring-to-SU5/E6 slot map; operator-layer Pic0 still reopens.")
        parts.append("The terminal-monad base-order/AH-binding/SM-slot-map gate separates constructed support from selected proof: diagnostic base order, AH automorphy/Yoneda multiplication, and q79 SU(5)/E6 slot support all exist, but none is promotable without the three-gate cutset of terminal map source principle, selected AH/Cech binding, and selected section-ring-to-SM-slot functor.")
        parts.append("The terminal-map source-principle/SM-slot-functor gate imports q79's TerminalAdmissibleSectionSourcePrinciple conditionally: under that explicit principle the terminal source, base order, ordered-source validator, and h1=8 Ext packet close; unconditional MTT closure still requires promoting or deriving the principle, or emitting the selected SM-slot functor directly.")
        parts.append("The terminal admissible-section principle-promotion audit collects corpus support for section selection, nil survivors, refinement stability, and minimal saturation, then drafts the exact terminal uniqueness axiom needed for unconditional promotion while retaining the parallel selected SM-slot-functor route.")
        parts.append("The terminal admissible-section axiom insertion / SM-slot functor package is insertion-ready: target paper placements and theorem text are fixed, and the selected SM-slot functor now has a precise domain, codomain, and six required arrows; values remain open.")
        parts.append("The selected SM-slot functor value-emission / axiom-patch gate proves the current frontier exactly: Route A is ready to apply as an axiom patch and would make terminal-source replay unconditional after insertion/derivation, while Route B direct value emission remains blocked by the six selected functor arrows, overlap normalization, and same-source consistency; no SM-slot values are claimed.")
        parts.append("The terminal axiom patch is now applied inside the local proof spine and verified in the four target corpus papers: terminal source g3/L3-K2, L=(1,-2,0), L^2=(2,-4,0), c2=(4,0,0), base order, and the h1=8 Ext packet are axiom-backed without observed constants; selected SM-slot six-arrow source emission remains open.")
        parts.append("The selected SM-slot six-arrow source-emission artifact closes the first three arrows from the axiom-backed terminal section-ring source: 10_M -> u,e, bar5_M -> d, and 1_M=N^c -> nuD; q79 U10/Ubar5 source outputs, overlap/transfer normalization, and full same-source consistency remain open.")
        parts.append("The selected SM-slot polarization source-emission artifact closes A4: with selected 10_M/bar5_M/1_M labels emitted, finite q79 transversality promotes U10=I3 and Ubar5=F on the retarded q79 branch; A5 overlap/transfer normalization and A6 same-source consistency remain open.")
        parts.append("The selected SM-slot finite overlap-kernel source-emission artifact closes A5 and A6 at the static source level: transported-projector trace Gram normalization and the selected unit Ext row make all six SM-slot functor source arrows emitted. The dynamic physical overlap kernel, D_E/Riesz/Green/dotD, alpha1 driver, primitive C1 contractions, and full SM data remain open.")
        parts.append("The selected SM-slot downstream payload ledger imports that static closure into the old seven-field C1 blocker contract: selected sector routing Z/clock -> u,e, X/shift -> d,nuD, the 1_M=N^c Dirac-neutrino rule, and finite trace transfer normalization are discharged at the static tier, while dynamic operator values, source-to-C1 overlap, primitive contractions, b_selected/Hessian normalization, and A_selected promotion remain open.")
        parts.append("The selected dynamic overlap-kernel / C1-primitive reduction proves the remaining wall is dynamic rather than label-theoretic: after static sector closure, the next minimal value-emission target is either a typed B_N retarded derivative or alpha1 source-strength theorem, selected End0-to-sector values, dynamic overlap/Hessian normalization with b_selected, or selected primitive/vertex response values.")
        parts.append("The typed B_N retarded-derivative / primitive-response value-emission artifact tests both remaining lanes: the typed retarded lane remains support-only under the validator, while the primitive lane emits exact rank-3 fixed-fiber candidate values at active shift (1,1) for fiber shifts 0, 1, and 2; selection of one fiber shift, a typed retarded selector, A_selected, and b_selected remains open.")
        parts.append("The primitive fiber-shift / typed-retarded selector theorem closes the honest quotient version of the selector: active shift (1,1) is selected, fixed fiber shifts 0,1,2 form a selected quotient class for current C1 spectral observables, and shift 0 is only a computation representative; absolute fiber origin, typed retarded selector, A_selected, b_selected, and full flavor splitting remain open.")
        parts.append("The cross-repo alpha1 driver replay import checks the sibling proof repos and imports the useful closure from GR/protospinor: N_alpha1(h_ext)=1, du/dalpha1=h_ext, selected_dotD_source_verified=true, alpha1_driver_verified=true, and honest dotD replay PASS for the same q79/F,m=1 oriented source spine. This retires alpha1/dotD replay as the active blocker here, keeps the local primitive fiber quotient theorem intact, and leaves primitive C1 contractions, higher-order/full-response matrices, A_selected, and b_selected open.")
        parts.append("The primitive-class C1 observable / higher-order source-emission artifact fills the previous frontier: the selected active (1,1) quotient class emits a valid current C1 spectral-observable layer, but YY* is scalar in every sector, so it is not flavor closure. The next needed values are selected higher-order/full-response matrices, A_selected, b_selected, deltaTheta_C1, and sector response matrices.")
        parts.append("The C1 frontier-after-alpha1 artifact collapses the active blocker set: alpha1/dotD replay is retired, the primitive fiber quotient and scalar-layer no-go are retained, and the next proof object is selected primitive C1 contractions or selected higher-order/full-response matrices with same-source Weyl-pair sector routing and normalization. Conditional Weyl transfer remains exact but unpromoted.")
        parts.append("The primitive-C1 / Weyl-pair sector-routing source-emission reduction imports the later SM-slot functor ledger to close static Weyl routing: Z/clock routes to u,e; X/shift routes to d,nuD; 1_M=N^c sits on the shift/Dirac-neutrino side; finite trace transfer normalization is selected. Sector routing is therefore no longer the C1 blocker; dynamic overlap tensor, primitive contractions, A_selected, and b_selected remain open.")
        parts.append("The primitive-C1 contractions / dynamic-overlap tensor source-emission artifact builds the routed contraction envelope from closed alpha1/dotD replay, static Weyl routing, the 1_M shift-side rule, finite trace transfer, and fixed-fiber primitive candidates. Promotion is correctly rejected because honest Galerkin primitive contractions, dynamic overlap tensor, Hessian/b_selected, A_selected, sector response matrices, and deltaTheta_C1 are still not emitted.")
        parts.append("The dynamic-overlap / Hessian / Galerkin C1 value-emission audit emits the exact current quotient-layer C1 value packet and proves its limitation: every fixed-fiber representative and sector has YY*=0.116935954119764 I_3, so it is a valid current spectral-observable layer but cannot produce Yukawa hierarchy, CKM/PMNS mixing, or CP. The next object must be non-scalar dynamic overlap, Hessian/full-response, or honest Galerkin C1 data from the same source.")
        parts.append("The non-scalar dynamic-overlap / full-response correction value-emission packet constructs the internally locked Weyl-pair correction: u/e receive I+Z, d/nuD receive I+X, deltaTheta=(1,1), mass-split traceless norms are positive, CKM/PMNS commutator norms are nonzero, and Im Tr([Hu,Hd]^3) is nonzero. It remains conditional because same-source dynamic source-to-C1 transfer, Hessian normalization, A_selected, b_selected, and honest Galerkin C1 value fill are still open.")
        parts.append("The Weyl-pair dynamic-overlap source-promotion / honest Galerkin C1 gate makes that boundary executable: source-level Z/X carrier, active shift, static Z->u,e and X->d,nuD routing, the 1_M shift rule, and static trace normalization are closed; the remaining cutset is exactly selected dynamic transfer/Hessian/A_selected/b_selected/sector matrices, or honest selected Galerkin C1 contractions with zero-mode bases, primitive 3x3 terms, linear response matrices, and C33/nonzero-family-rank tests.")
        parts.append("The dynamic transfer/Hessian/b_selected value-fill gate fixes the 72-real coordinate system and computes the conditional Weyl-pair Gram data exactly: A^T A=12 I_2, A^T b=(12,12), ||b||^2=24, and deltaTheta=(1,1). Thus the remaining blocker is selected same-source dynamic transfer/Hessian/b_selected identity or honest Galerkin C1 contraction emission, not a search-space or conditioning problem.")
        parts.append("The same-source dynamic-transfer identity / Galerkin C1 contractions emission gate puts the remaining proof in normal form: if selected Phi_fin^C1 sends Z and X to the phase/shift columns with the same Hessian normalization, then A_selected, b_selected, and deltaTheta_C1=(1,1) follow; if an honest Galerkin run emits different values, that selected equation must replace the conditional Weyl packet.")
        parts.append("The PhiFinC1 dynamic-transfer proof/Galerkin run gate imports the symbolic transport-conjugation result: stationary projectors/Riesz/Green/rho_s are selected-source verified, but stationary transport alone cannot prove the C1 dynamic transfer identity; the live object is differentiated PhiFinC1 with primitive overlap contractions or an honest Galerkin C1 run.")
        parts.append("The differentiated PhiFinC1 primitive-overlap/Galerkin gate attaches the theorem-derived alpha1/dotD driver, proves the transport-only canonical C1 lane is zero and cannot emit the phase/shift columns, imports the non-invariant rank-3 fixed-fiber candidates only as unselected support, and emits the exact primitive-overlap template that a selected vertex/basis-transport theorem or honest Galerkin run must fill.")
        parts.append("The primitive-vertex/basis-transport source-selection theorem now emits the same-branch source selector for the differentiated template: selected qutrit Weyl carrier, active shift (1,1), fixed-fiber quotient, static Z->u,e and X->d,nuD route, trace normalization, and alpha1/dotD driver are attached; primitive overlap values, A_selected, b_selected, and deltaTheta_C1 remain open.")
        parts.append("The primitive-overlap value-emission / honest Galerkin run gate attaches that selector to the differentiated template and proves the pure fixed-fiber primitive replay cannot emit the Weyl-pair dynamic columns: I+Z has residual norm squared 4 per sector and I+X has residual norm squared 2 per sector against the fixed-fiber span. The next value packet must therefore supply a selected differentiated vertex, basis-transport correction, Hessian counterterm, or honest Galerkin C1 run.")
        parts.append("The differentiated-vertex / Hessian-counterterm residual value packet computes the exact orthogonal completion left by that no-go: phase residual norm squared 4 per sector, shift residual norm squared 2 per sector, total routed residual norm squared 12, with projection plus residual reconstructing the conditional I+Z/I+X packet exactly. This is diagnostic until the same-branch residual source theorem or honest Galerkin C1 emission is supplied.")
        parts.append("The residual-completion source-promotion / honest Galerkin C1 emission gate converts that diagnostic residual into a minimal typed source-packet template. Under the SM-parity lens, either a same-branch residual source theorem or a selected honest Galerkin C1 emission would close the dynamic packet interface; neither is currently selected, and no observed flavor constants are used as selectors.")
        parts.append("The residual Weyl-polynomial source theorem attempt proves the residuals are exact low-degree polynomials in the selected qutrit Weyl carrier: R_X=(I+X-2X^2)/3 and R_Z=(2I+2Z-X-X^2+e^{i*pi/3}ZX+e^{-i*pi/3}ZX^2)/3. Lane A is now reduced to selecting the canonical trace-orthogonal residual projector or falling back to honest Galerkin C1 emission.")
        parts.append("The canonical residual projector / honest Galerkin C1 value-fill gate constructs the unique trace/Frobenius orthogonal projector from the selected fixed-fiber quotient: P_fixed has rank 3, Q_residual has rank 6, both are self-adjoint idempotents, and Q_residual replays R_Z/R_X exactly. Physical Phi_fin^C1 application of this projector or an honest selected Galerkin run remains open.")
        parts.append("The PhiFinC1 residual-projector application / honest Galerkin execution gate proves the guardrail: canonical Q_residual is not enough for physical promotion, and existing stationary transport-only Phi_fin^C1 cannot emit the residual columns because the one-response C1 matrices are zero. The next proof object is a differentiated residual-projector source rule, selected basis-transport/vertex/Hessian source, or honest Galerkin C1 execution.")
        parts.append("The differentiated residual-projector source-rule / honest Galerkin C1 execution gate formalizes the next proof object and ranks the enriched Weyl-pair basis-transport/vertex source as the primary route: its conditional A has rank 2 and deltaTheta=(1,1), but selected source emission, b_selected, and physical value promotion remain open.")
        parts.append("The Weyl-pair source-emission / honest Galerkin C1 execution value-run gate attempts the primary promotion and blocks it honestly: the conditional value run is ready with rank 2, condition number 1, and deltaTheta=(1,1), but phase/shift source emissions, A_selected, and b_selected are still not theorem-derived.")
        parts.append("The enriched Weyl-pair source-provenance / Galerkin C1 values gate promotes the static source-tier provenance: selected Z/clock routes to u,e, selected X/shift routes to d,nuD, the 1_M=N^c Dirac-neutrino rule and finite trace transfer normalization are closed; dynamic C1 transfer, primitive contractions, A_selected, and b_selected remain open.")
        parts.append("The dynamic C1 transfer-tensor / Galerkin C1 values gate carries closed static source provenance, stationary projector/Riesz/Green support, and alpha1/dotD replay into the frontier; the conditional 72-real tensor normal form has rank 2 and deltaTheta=(1,1), but selected non-invariant primitive tensor, Hessian/source vector, or honest Galerkin values remain open.")
        parts.append("The dynamic C1 transfer-tensor / Galerkin C1 values acceptance manifest is built: Lane A same-source dynamic Phi_fin^C1 transfer and Lane B honest Galerkin C1 execution are locked to the same 72-real target objects A_selected, b_selected, deltaTheta_C1, and sector response matrices; values remain open and observed constants remain forbidden as selectors.")
        parts.append("The dynamic C1 transfer-tensor value-emission / honest Galerkin C1 run gate attempts the strict 72-real acceptance target against current Lane A and Lane B sources: A^T A=12 I_2, A^T b=(12,12), deltaTheta_C1=(1,1), closed support, and exact conditional rank-2 linear algebra are not the blocker; the remaining cutset is selected differentiated Phi_fin^C1/primitive tensor plus b_selected and sector matrices, or an honest selected Galerkin C1 execution.")
        parts.append("The primitive C1 tensor / Hessian source-map or honest Galerkin C1 execution gate constructs the minimal same-branch source-map candidate: Z/clock maps to the R_Z residual source, X/shift maps to the R_X residual source, with canonical Q_residual support and exact if-selected A^T A=12 I_2, A^T b=(12,12), deltaTheta=(1,1); the selected-source bits and b_selected remain open.")
        parts.append("The source-map selection theorem / honest Galerkin C1 value-run gate tests promotion of that candidate: terminal/static source selection, exact Weyl-polynomial residuals, and canonical Q_residual uniqueness are closed support, but they do not yet prove the physical differentiated Phi_fin^C1 application rule or b_selected; if supplied, the dynamic packet would close exactly, otherwise the honest Galerkin route remains the replacement path.")
        result = 0
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(parts)
    REPORT.write_text(text + "\n", encoding="utf-8")
    print(text)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
