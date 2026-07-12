"""Run the lightweight verifier for the current MTT SM-closure frontier.

The full live-frontier verifier was frozen on 2026-07-09 as
`scripts/verify_frontier_frozen_2026_07_09.py`.  The older full-chain replay
remains frozen at `scripts/verify_full_frozen_2026_07_04.py`.

Use:
  python scripts/verify.py              # lightweight last-frontier verification
  python scripts/verify.py --full       # 2026-07-09 frozen frontier replay
  python scripts/verify.py --legacy-full # 2026-07-04 archived full-chain replay
"""

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
FROZEN_FRONTIER = ROOT / "scripts" / "verify_frontier_frozen_2026_07_09.py"
FROZEN_LEGACY = ROOT / "scripts" / "verify_full_frozen_2026_07_04.py"

AUDITS = [
    # Parameter policy guardrails.
    "sm_parity_closure_ledger_audit.py",
    "core_axioms_measured_parameter_interface_audit.py",
    "locked_breakthroughs_do_not_reopen_audit.py",
    "global_locked_breakthroughs_do_not_reopen_audit.py",
    "crossrepo_qasu3_payload_value_contract_import_audit.py",
    "current_true_sm_closure_consolidated_ledger_audit.py",
    # Locked consumed base: do not reopen these as active blockers.
    "selected_qutrit27matrixminimalclosure_or_strictpewupgrade_audit.py",
    "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_audit.py",
    "selected_latestah8pickmfrontier_or_nextstrictclosuretargets_audit.py",
    # Current closure standard and strict PEW/direct-K split.
    "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows_audit.py",
    "selected_strictpewdirectk_or_qasu3step10valueexecution_audit.py",
    "selected_fulls2noproxyrows_or_strictpewnormalizationpayload_audit.py",
    "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit_audit.py",
    "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision_audit.py",
    "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram_audit.py",
    # Last active value-row frontier.
    "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport_audit.py",
    "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission_audit.py",
    "selected_lockedbasefreeze_or_pewdirectkattackcontract_audit.py",
    "selected_retardedoverlapspectralpairing_or_independentquadraturevalues_audit.py",
    "selected_tschemenulldelta_reconciliation_or_lambdahlastrow_audit.py",
    "selected_lambdahlastrowpayload_or_strictdirectkclosure_audit.py",
    "selected_strictpewdenominatorsource_candidate_or_promotiongate_audit.py",
    "selected_strictpewdenominatorselectiontheorem_or_directkpromotion_audit.py",
    "selected_precisionequivalencerows_or_truesmclosureaudit_audit.py",
    "selected_precisiontransportcovariancerows_or_finaltruesmaudit_audit.py",
    "selected_acceptedprecisionsourcevalues_or_finaltruesmclosure_audit.py",
    "selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure_audit.py",
    "selected_finalprofilelikelihoodordynamicpayloadvalues_audit.py",
    "selected_phifinc1sourceemissionorfiniterowindependencetheorem_audit.py",
    "selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted_audit.py",
    "selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution_audit.py",
    "selected_finaldynamicgate_routea_reconciliation_or_valuepromotionnext_audit.py",
    "selected_postsourcevaluepromotionrows_or_trueprecisionexit_audit.py",
    "selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier_audit.py",
    "selected_valuesourceanchorrows_or_internalnoknobvalueemission_audit.py",
    "selected_valuesourceanchoremission_or_noknoblimitationtheorem_audit.py",
    "selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution_audit.py",
    "selected_rthetasourceruleemission_or_thresholdmatchingmassschemerows_audit.py",
    "selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit_audit.py",
    "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy_audit.py",
    "selected_internalnoknobvaluerows_or_fullcovarianceprofilelikelihoodexecution_audit.py",
    "selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission_audit.py",
    "selected_acceptedfulllikelihoodfunction_or_rthetacoefficientvaluerows_audit.py",
    "selected_rthetavalueevaluatorsourceprovenance_or_officiallikelihoodworkspace_audit.py",
    "selected_rthetacoefficientsourcerows_or_officiallikelihoodworkspace_audit.py",
    "selected_rthetarowownerformulavalueemitter_or_officiallikelihoodworkspace_audit.py",
    "selected_rthetathresholdresponsevectoremitter_or_officiallikelihoodworkspace_audit.py",
    "selected_lrowlocaltschemelambdah_sourceexecution_or_officiallikelihoodworkspace_audit.py",
    "selected_strictomegaacceptancebridge_or_hlambdavectorrowbridge_audit.py",
    "selected_omegavaluepayloadtransport_or_officiallikelihoodworkspace_audit.py",
    "selected_internalvrthetavaluepayloadoperator_or_officialfullprofileworkspace_audit.py",
    "selected_physicalprojectionnormalizationoperator_or_officialfullprofileworkspace_audit.py",
    "selected_magnitudebearingnormalizationfunctional_or_officialfullprofileworkspace_audit.py",
    "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness_audit.py",
    "selected_magprofilesourcescalar_or_officialfullprofileworkspace_audit.py",
    "selected_magprofilevaluefunctional_or_officialfullprofileworkspace_audit.py",
    "selected_precisionlayerfullcovariance_or_internaltransport_audit.py",
    "selected_precisiontransportvalueobject_or_finaltruesmequivalence_audit.py",
    "selected_productprecisionworkspaceacceptance_or_internaltransportpromotion_audit.py",
    "selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood_audit.py",
    "selected_renormalizedsmobservablefunctor_fromcommonschemeaction_audit.py",
    "selected_finalglobaltruesmclosureaudit_aftermultiloopprecision_audit.py",
    # Strict-upgrade program after declared-standard true-SM closure.
    "selected_officialjointlikelihoodtransport_or_declareddiagonalprofilefinality_audit.py",
    "selected_literalcechwitness_or_globalhymconnectioncoefficients_audit.py",
    "selected_ckmcentralestimatorretirement_or_predictionprofileclosure_audit.py",
    "selected_neutrinoandstrongcp_strictupgradeattack_audit.py",
    "selected_globalhymchernsequence_aposterioricertificate_audit.py",
    "selected_hymuniformspectralconvergenceandpatchingcertificate_audit.py",
    "selected_hymvalidatedfourierresidualtailbound_audit.py",
    "selected_neutralnilboundarymassfunctional_audit.py",
    "selected_neutraloperatorunificationandinventoryaudit_audit.py",
    "selected_neutralmassoperator_sourceemission_audit.py",
    "selected_neutraldimensionfulblocksandnormalization_audit.py",
    "selected_neutraloverlapkernelphysicalunitoractioncompleteness_audit.py",
    "selected_neutraloverlapkernelvaluesourceorphysicalunittheorem_audit.py",
    "selected_neutralgammanuactionrowsordiraccompleteness_audit.py",
    "selected_neutralfinitegammarowsoractioncostsource_audit.py",
    "selected_neutralactioncostprefactorordiracmajoranacompletion_audit.py",
    "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion_audit.py",
    "selected_neutralphysicalunitornilanchorprojector_audit.py",
    "selected_neutralspectralactionslopeorseesawsource_audit.py",
    "selected_protospinoralignmenttodiracmassreadout_audit.py",
    "selected_neutralradialsecondvariationandvevcoordinatetheorem_audit.py",
    "selected_neutralhiggsinsertionfunctorandradialcoordinatenormalization_audit.py",
    "selected_neutraleffectiveweightidentifiabilityreduction_audit.py",
    "selected_neutralcrtphasetypingandprotospinornildriftreduction_audit.py",
    "selected_neutralcommoncirclefactorizationandholonomyscalarreduction_audit.py",
    "selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget_audit.py",
    "selected_neutraltwoprimitiveprofilevalueclosure_audit.py",
    "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile_audit.py",
    "selected_neutraluniversale0attenuationcandidate_or_sourcelawfrontier_audit.py",
    "selected_neutralcompositespectralattenuationreduction_or_branchbridgetheorem_audit.py",
    "selected_samegeometryqutrittosmalgebrabridge_or_generativebasefrontier_audit.py",
    "selected_classlaneprojectorsandweakrealstructuresourcetheorem_audit.py",
    "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem_audit.py",
    "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit_audit.py",
    "selected_nativegaugeactiontofinitebimodule_or_directgenerativesmbaseclosure_audit.py",
    "selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure_audit.py",
    "selected_neutralalgebrasummandorequivalentaxiomrevision_audit.py",
    "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure_audit.py",
    "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization_audit.py",
    "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure_audit.py",
    "selected_gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure_audit.py",
    "selected_commonschemegaugekineticpayloadsearch_or_finiteprojectedthresholdcandidate_audit.py",
    "selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload_audit.py",
    "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload_audit.py",
    "selected_sectorresolvedinternalfluctuationspectra_or_nonuniversalgaugethresholdpayload_audit.py",
    "selected_su2finitescalebinding_and_su3adjointgaugehessiansource_audit.py",
    "selected_su2holomorphicprojection_and_su3p0brstnormalization_lock_audit.py",
    "selected_su2transportclosedfinitegaugerow_and_su3nativecolorsourcereduction_audit.py",
    "selected_su3adjointcentraltrivialfinitegaugerow_and_tenspectrumclosure_audit.py",
    "selected_e6centralgeneratorqcdanomalyaudit_audit.py",
    "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness_audit.py",
    "selected_quantizationandnonperturbativeqft_strictupgradeaudit_audit.py",
    "selected_strictnoknobupgradeledger_aftertruesmequivalence_audit.py",
    "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure_audit.py",
    "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure_audit.py",
    "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure_audit.py",
    "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit_audit.py",
    "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution_audit.py",
    "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion_audit.py",
    "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport_audit.py",
    "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation_audit.py",
    "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest_audit.py",
    "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction_audit.py",
    "selected_noknobvaluederivationkernel_or_sourceanchortheorem_audit.py",
    "selected_rthetavaluerows_or_universalsourceanchortheorem_audit.py",
    "selected_higherresponserthetafunctional_or_sourceanchortheorem_audit.py",
    "selected_rtheta_coefficientfunctional_or_universalanchorselection_audit.py",
    "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_audit.py",
    "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution_audit.py",
    "selected_step45_alpha1rthetarow_execution_attempt_or_coefficientmapfrontier_audit.py",
    "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution_audit.py",
    "selected_step47_alpha1rtheta_xi_argument_fill_or_internalvaluerows_audit.py",
    "selected_step48_xi_omega_payload_source_theorem_or_rtheta_value_rows_audit.py",
    "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution_audit.py",
    "selected_step59_higherresponse_contract_import_or_payloadexecution_audit.py",
    "selected_dynamicphifinc1payloadrows_or_higherresponseexecution_audit.py",
    "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution_audit.py",
    "selected_fulls2sectordensityoperator_or_phisectornnumericrows_audit.py",
    "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution_audit.py",
    "selected_hresponsetablevaluerows_or_directherm2valuerows_audit.py",
    "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows_audit.py",
    "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows_audit.py",
    "selected_pureweyllambdarepresentative_or_higherresponsescalarrows_audit.py",
    "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution_audit.py",
    "selected_internalrthetascalarrowemission_or_universalanchorselection_audit.py",
    "selected_crossblockcovariancevalues_or_rthetacoefficientexecution_audit.py",
    "selected_commonscalejacobian_or_rthetathresholdresponseexecution_audit.py",
    "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill_audit.py",
    "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution_audit.py",
    "selected_deltas2densitycorrectionsource_or_strictcskrows_audit.py",
    "selected_hresponsevaluesourcefunctional_or_directherm2rows_audit.py",
    "selected_hresponserowsourceemission_or_directherm2certificatepayload_audit.py",
    "selected_hradialthresholdscalarsource_or_tenkclosure_audit.py",
    "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection_audit.py",
    "selected_dynamicphifintracebinding_or_primitiverowformulaexecution_audit.py",
    "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport_audit.py",
    "phifin_bn_modelactive_equivalence_or_minimizer_trace_audit.py",
    "selected_fullsectorhymoperatorpayload_or_deltas2rowemission_audit.py",
    "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun_audit.py",
    "selected_huvprimitiveformula_or_finiteerrorboundexecution_audit.py",
    "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure_audit.py",
    "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows_audit.py",
    "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem_audit.py",
    "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction_audit.py",
    "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge_audit.py",
    "selected_physicalactionrestrictionclause_or_primitivekernelformula_audit.py",
    "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket_audit.py",
    "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution_audit.py",
    "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution_audit.py",
    "selected_phisectornsourcevalues_or_noknobcskrows_audit.py",
    "selected_sectorresponsedensitysource_or_noknobcskrowemission_audit.py",
    "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart_audit.py",
    "selected_visible_chern_weil_operator_source_audit.py",
    "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill_audit.py",
    "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade_audit.py",
    "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource_audit.py",
    "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows_audit.py",
    "selected_finitehfunctional_or_msourcevalueemission_audit.py",
    "selected_hradialscalephasesource_or_herm2hessianrows_audit.py",
    "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem_audit.py",
    "selected_hsectorquarticthresholdpayload_or_stricttenkclosure_audit.py",
    "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows_audit.py",
    "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue_audit.py",
    "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate_audit.py",
    "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun_audit.py",
    "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade_audit.py",
    "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit_audit.py",
    "selected_hradialactionnormvalue_or_hlambdathresholdrow_audit.py",
    "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda_audit.py",
    "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow_audit.py",
    "selected_alpha1_tangent_promotion_or_sector_routing_theorem_audit.py",
    "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem_audit.py",
    "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit_audit.py",
    "selected_herm2polarsourcecompletion_or_hresponserows_audit.py",
    "selected_hradialphasetracesource_or_finitehactionemission_audit.py",
    "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt_audit.py",
    "selected_hthresholdrgoperator_or_universalprimitivepolicy_audit.py",
    "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun_audit.py",
    "selected_nonsplit_rank2_or_routec_same_source_packet_audit.py",
    "selected_physicalsourcecertificatefill_or_routebindependentrunexecution_audit.py",
    "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution_audit.py",
    "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution_audit.py",
    "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow_audit.py",
    "selected_thresholdrows_or_diagonalprofilelimitationtheorem_audit.py",
    "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit_audit.py",
    "selected_samebranchgaugeactionsource_or_oneprimitivepolicy_audit.py",
    "selected_aewsourceoperator_or_thresholdconventionrows_audit.py",
    "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector_audit.py",
    "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun_audit.py",
    "selected_chernweilde_or_determinanttorsion_threeslotclosingrun_audit.py",
    "selected_detransition_or_determinanttorsion_twoslotclosingrun_audit.py",
    "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission_audit.py",
    "selected_firstsamesourceconnectionfieldemission_or_directhkrow_audit.py",
    "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem_audit.py",
    "selected_physicalactionsourcerule_or_independentprimitivekernelformula_audit.py",
    "selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission_audit.py",
    "selected_rtheta_physicalprojectionkernel_or_profileresponse_audit.py",
    "selected_samesourceconnectionvaluetable_or_directhkrow_audit.py",
    "selected_thresholdmassschemerows_or_precisionprofileupgrade_audit.py",
]

CERTIFICATES = [
    "sm_parity_closure_ledger_certificate.json",
    "core_axioms_measured_parameter_interface_certificate.json",
    "locked_breakthroughs_do_not_reopen_certificate.json",
    "global_locked_breakthroughs_do_not_reopen_certificate.json",
    "crossrepo_qasu3_payload_value_contract_import_certificate.json",
    "current_true_sm_closure_consolidated_ledger_certificate.json",
    "selected_qutrit27matrixminimalclosure_or_strictpewupgrade_certificate.json",
    "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_certificate.json",
    "selected_latestah8pickmfrontier_or_nextstrictclosuretargets_certificate.json",
    "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows_certificate.json",
    "selected_strictpewdirectk_or_qasu3step10valueexecution_certificate.json",
    "selected_fulls2noproxyrows_or_strictpewnormalizationpayload_certificate.json",
    "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit_certificate.json",
    "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision_certificate.json",
    "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram_certificate.json",
    "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport_certificate.json",
    "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission_certificate.json",
    "selected_lockedbasefreeze_or_pewdirectkattackcontract_certificate.json",
    "selected_retardedoverlapspectralpairing_or_independentquadraturevalues_certificate.json",
    "selected_tschemenulldelta_reconciliation_or_lambdahlastrow_certificate.json",
    "selected_lambdahlastrowpayload_or_strictdirectkclosure_certificate.json",
    "selected_strictpewdenominatorsource_candidate_or_promotiongate_certificate.json",
    "selected_strictpewdenominatorselectiontheorem_or_directkpromotion_certificate.json",
    "selected_precisionequivalencerows_or_truesmclosureaudit_certificate.json",
    "selected_precisiontransportcovariancerows_or_finaltruesmaudit_certificate.json",
    "selected_acceptedprecisionsourcevalues_or_finaltruesmclosure_certificate.json",
    "selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure_certificate.json",
    "selected_finalprofilelikelihoodordynamicpayloadvalues_certificate.json",
    "selected_phifinc1sourceemissionorfiniterowindependencetheorem_certificate.json",
    "selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted_certificate.json",
    "selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution_certificate.json",
    "selected_finaldynamicgate_routea_reconciliation_or_valuepromotionnext_certificate.json",
    "selected_postsourcevaluepromotionrows_or_trueprecisionexit_certificate.json",
    "selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier_certificate.json",
    "selected_valuesourceanchorrows_or_internalnoknobvalueemission_certificate.json",
    "selected_valuesourceanchoremission_or_noknoblimitationtheorem_certificate.json",
    "selected_thresholdresponsefunctionalsourcerows_or_dynamicqasu3payloadvalueexecution_certificate.json",
    "selected_rthetasourceruleemission_or_thresholdmatchingmassschemerows_certificate.json",
    "selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit_certificate.json",
    "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy_certificate.json",
    "selected_internalnoknobvaluerows_or_fullcovarianceprofilelikelihoodexecution_certificate.json",
    "selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission_certificate.json",
    "selected_acceptedfulllikelihoodfunction_or_rthetacoefficientvaluerows_certificate.json",
    "selected_rthetavalueevaluatorsourceprovenance_or_officiallikelihoodworkspace_certificate.json",
    "selected_rthetacoefficientsourcerows_or_officiallikelihoodworkspace_certificate.json",
    "selected_rthetarowownerformulavalueemitter_or_officiallikelihoodworkspace_certificate.json",
    "selected_rthetathresholdresponsevectoremitter_or_officiallikelihoodworkspace_certificate.json",
    "selected_lrowlocaltschemelambdah_sourceexecution_or_officiallikelihoodworkspace_certificate.json",
    "selected_strictomegaacceptancebridge_or_hlambdavectorrowbridge_certificate.json",
    "selected_omegavaluepayloadtransport_or_officiallikelihoodworkspace_certificate.json",
    "selected_internalvrthetavaluepayloadoperator_or_officialfullprofileworkspace_certificate.json",
    "selected_physicalprojectionnormalizationoperator_or_officialfullprofileworkspace_certificate.json",
    "selected_magnitudebearingnormalizationfunctional_or_officialfullprofileworkspace_certificate.json",
    "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness_certificate.json",
    "selected_magprofilesourcescalar_or_officialfullprofileworkspace_certificate.json",
    "selected_magprofilevaluefunctional_or_officialfullprofileworkspace_certificate.json",
    "selected_precisionlayerfullcovariance_or_internaltransport_certificate.json",
    "selected_precisiontransportvalueobject_or_finaltruesmequivalence_certificate.json",
    "selected_productprecisionworkspaceacceptance_or_internaltransportpromotion_certificate.json",
    "selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood_certificate.json",
    "selected_renormalizedsmobservablefunctor_fromcommonschemeaction_certificate.json",
    "selected_finalglobaltruesmclosureaudit_aftermultiloopprecision_certificate.json",
    "selected_officialjointlikelihoodtransport_or_declareddiagonalprofilefinality_certificate.json",
    "selected_literalcechwitness_or_globalhymconnectioncoefficients_certificate.json",
    "selected_ckmcentralestimatorretirement_or_predictionprofileclosure_certificate.json",
    "selected_neutrinoandstrongcp_strictupgradeattack_certificate.json",
    "selected_globalhymchernsequence_aposterioricertificate_certificate.json",
    "selected_hymuniformspectralconvergenceandpatchingcertificate_certificate.json",
    "selected_hymvalidatedfourierresidualtailbound_certificate.json",
    "selected_neutralnilboundarymassfunctional_certificate.json",
    "selected_neutraloperatorunificationandinventoryaudit_certificate.json",
    "selected_neutralmassoperator_sourceemission_certificate.json",
    "selected_neutraldimensionfulblocksandnormalization_certificate.json",
    "selected_neutraloverlapkernelphysicalunitoractioncompleteness_certificate.json",
    "selected_neutraloverlapkernelvaluesourceorphysicalunittheorem_certificate.json",
    "selected_neutralgammanuactionrowsordiraccompleteness_certificate.json",
    "selected_neutralfinitegammarowsoractioncostsource_certificate.json",
    "selected_neutralactioncostprefactorordiracmajoranacompletion_certificate.json",
    "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion_certificate.json",
    "selected_neutralphysicalunitornilanchorprojector_certificate.json",
    "selected_neutralspectralactionslopeorseesawsource_certificate.json",
    "selected_protospinoralignmenttodiracmassreadout_certificate.json",
    "selected_neutralradialsecondvariationandvevcoordinatetheorem_certificate.json",
    "selected_neutralhiggsinsertionfunctorandradialcoordinatenormalization_certificate.json",
    "selected_neutraleffectiveweightidentifiabilityreduction_certificate.json",
    "selected_neutralcrtphasetypingandprotospinornildriftreduction_certificate.json",
    "selected_neutralcommoncirclefactorizationandholonomyscalarreduction_certificate.json",
    "selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget_certificate.json",
    "selected_neutraltwoprimitiveprofilevalueclosure_certificate.json",
    "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile_certificate.json",
    "selected_neutraluniversale0attenuationcandidate_or_sourcelawfrontier_certificate.json",
    "selected_neutralcompositespectralattenuationreduction_or_branchbridgetheorem_certificate.json",
    "selected_samegeometryqutrittosmalgebrabridge_or_generativebasefrontier_certificate.json",
    "selected_classlaneprojectorsandweakrealstructuresourcetheorem_certificate.json",
    "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem_certificate.json",
    "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit_certificate.json",
    "selected_nativegaugeactiontofinitebimodule_or_directgenerativesmbaseclosure_certificate.json",
    "selected_e6centralgeneratorqcdanomalyaudit_certificate.json",
    "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness_certificate.json",
    "selected_quantizationandnonperturbativeqft_strictupgradeaudit_certificate.json",
    "selected_strictnoknobupgradeledger_aftertruesmequivalence_certificate.json",
    "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure_certificate.json",
    "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure_certificate.json",
    "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure_certificate.json",
    "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit_certificate.json",
    "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution_certificate.json",
    "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion_certificate.json",
    "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport_certificate.json",
    "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation_certificate.json",
    "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest_certificate.json",
    "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction_certificate.json",
    "selected_noknobvaluederivationkernel_or_sourceanchortheorem_certificate.json",
    "selected_rthetavaluerows_or_universalsourceanchortheorem_certificate.json",
    "selected_higherresponserthetafunctional_or_sourceanchortheorem_certificate.json",
    "selected_rtheta_coefficientfunctional_or_universalanchorselection_certificate.json",
    "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_certificate.json",
    "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution_certificate.json",
    "selected_step45_alpha1rthetarow_execution_attempt_or_coefficientmapfrontier_certificate.json",
    "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution_certificate.json",
    "selected_step47_alpha1rtheta_xi_argument_fill_or_internalvaluerows_certificate.json",
    "selected_step48_xi_omega_payload_source_theorem_or_rtheta_value_rows_certificate.json",
    "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution_certificate.json",
    "selected_step59_higherresponse_contract_import_or_payloadexecution_certificate.json",
    "selected_dynamicphifinc1payloadrows_or_higherresponseexecution_certificate.json",
    "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution_certificate.json",
    "selected_fulls2sectordensityoperator_or_phisectornnumericrows_certificate.json",
    "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution_certificate.json",
    "selected_hresponsetablevaluerows_or_directherm2valuerows_certificate.json",
    "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows_certificate.json",
    "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows_certificate.json",
    "selected_pureweyllambdarepresentative_or_higherresponsescalarrows_certificate.json",
    "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution_certificate.json",
    "selected_internalrthetascalarrowemission_or_universalanchorselection_certificate.json",
    "selected_crossblockcovariancevalues_or_rthetacoefficientexecution_certificate.json",
    "selected_commonscalejacobian_or_rthetathresholdresponseexecution_certificate.json",
    "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill_certificate.json",
    "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution_certificate.json",
    "selected_deltas2densitycorrectionsource_or_strictcskrows_certificate.json",
    "selected_hresponsevaluesourcefunctional_or_directherm2rows_certificate.json",
    "selected_hresponserowsourceemission_or_directherm2certificatepayload_certificate.json",
    "selected_hradialthresholdscalarsource_or_tenkclosure_certificate.json",
    "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection_certificate.json",
    "selected_dynamicphifintracebinding_or_primitiverowformulaexecution_certificate.json",
    "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport_certificate.json",
    "phifin_bn_modelactive_equivalence_or_minimizer_trace_certificate.json",
    "selected_fullsectorhymoperatorpayload_or_deltas2rowemission_certificate.json",
    "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun_certificate.json",
    "selected_huvprimitiveformula_or_finiteerrorboundexecution_certificate.json",
    "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure_certificate.json",
    "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows_certificate.json",
    "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem_certificate.json",
    "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction_certificate.json",
    "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge_certificate.json",
    "selected_physicalactionrestrictionclause_or_primitivekernelformula_certificate.json",
    "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket_certificate.json",
    "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution_certificate.json",
    "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution_certificate.json",
    "selected_phisectornsourcevalues_or_noknobcskrows_certificate.json",
    "selected_sectorresponsedensitysource_or_noknobcskrowemission_certificate.json",
    "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart_certificate.json",
    "selected_visible_chern_weil_operator_source_certificate.json",
    "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill_certificate.json",
    "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade_certificate.json",
    "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource_certificate.json",
    "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows_certificate.json",
    "selected_finitehfunctional_or_msourcevalueemission_certificate.json",
    "selected_hradialscalephasesource_or_herm2hessianrows_certificate.json",
    "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem_certificate.json",
    "selected_hsectorquarticthresholdpayload_or_stricttenkclosure_certificate.json",
    "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows_certificate.json",
    "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue_certificate.json",
    "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate_certificate.json",
    "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun_certificate.json",
    "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade_certificate.json",
    "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit_certificate.json",
    "selected_hradialactionnormvalue_or_hlambdathresholdrow_certificate.json",
    "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda_certificate.json",
    "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow_certificate.json",
    "selected_alpha1_tangent_promotion_or_sector_routing_theorem_certificate.json",
    "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem_certificate.json",
    "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit_certificate.json",
    "selected_herm2polarsourcecompletion_or_hresponserows_certificate.json",
    "selected_hradialphasetracesource_or_finitehactionemission_certificate.json",
    "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt_certificate.json",
    "selected_hthresholdrgoperator_or_universalprimitivepolicy_certificate.json",
    "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun_certificate.json",
    "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json",
    "selected_physicalsourcecertificatefill_or_routebindependentrunexecution_certificate.json",
    "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution_certificate.json",
    "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution_certificate.json",
    "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow_certificate.json",
    "selected_thresholdrows_or_diagonalprofilelimitationtheorem_certificate.json",
    "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit_certificate.json",
    "selected_samebranchgaugeactionsource_or_oneprimitivepolicy_certificate.json",
    "selected_aewsourceoperator_or_thresholdconventionrows_certificate.json",
    "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector_certificate.json",
    "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun_certificate.json",
    "selected_chernweilde_or_determinanttorsion_threeslotclosingrun_certificate.json",
    "selected_detransition_or_determinanttorsion_twoslotclosingrun_certificate.json",
    "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission_certificate.json",
    "selected_firstsamesourceconnectionfieldemission_or_directhkrow_certificate.json",
    "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem_certificate.json",
    "selected_physicalactionsourcerule_or_independentprimitivekernelformula_certificate.json",
    "selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission_certificate.json",
    "selected_rtheta_physicalprojectionkernel_or_profileresponse_certificate.json",
    "selected_samesourceconnectionvaluetable_or_directhkrow_certificate.json",
    "selected_thresholdmassschemerows_or_precisionprofileupgrade_certificate.json",
]


def run_audit(script: str) -> tuple[int, str]:
    path = CORPUS / script
    if not path.exists():
        return 1, f"Missing audit: {path}"
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout


def run_frozen(path: Path) -> int:
    if not path.exists():
        print(f"Missing frozen verifier: {path}")
        return 1
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        stdout=sys.stdout,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode


def certificate_status() -> str:
    lines = ["Certificate status", "------------------"]
    for name in CERTIFICATES:
        path = CERTS / name
        if not path.exists():
            lines.append(f"{name}: MISSING")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        lines.append(f"{name}: {data.get('status', 'UNKNOWN')}")
    lines.append("")
    lines.append(f"Frozen frontier verifier: {FROZEN_FRONTIER}")
    lines.append(f"Legacy full verifier: {FROZEN_LEGACY}")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if "--full" in argv:
        return run_frozen(FROZEN_FRONTIER)
    if "--legacy-full" in argv:
        return run_frozen(FROZEN_LEGACY)

    parts = [
        "MTT lightweight last-frontier verification report",
        "================================================",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Corpus: {CORPUS}",
        "",
        "Scope: locked consumed base plus the post-EW precision/value-row frontier.",
        "Use --full for the 2026-07-09 frozen frontier replay.",
        "Use --legacy-full for the 2026-07-04 archived full-chain replay.",
        "",
    ]

    failures: list[str] = []
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
        parts.append(
            "Lightweight frontier checks passed. The consumed base is locked: "
            "27x27 matrix, AH-equivalent BN27 8/8 lane, Pi_CKM rows, CKM "
            "diagonal-profile admission, finite-replay Yukawa magnitudes, finite "
            "H scalar source, and the one-shared-physical-primitive standard are "
            "not active blockers. The old DynamicPhiFinC1PayloadRows target is "
            "now consumed into the deeper late-frontier ledger. "
            "The ten-row K_threshold ledger is now closed under the adopted "
            "one-shared-physical-primitive standard: "
            "9 selected Q_sel rows, 9 strict charged L_rowlocal rows, 9 selected "
            "source-native T_scheme=1 rows, 9 charged K_threshold rows, and "
            "1 H/lambda K row from the existing physical-normalization/direct-K "
            "certificate. The strict P_EW/direct-K blocker is now promoted by "
            "the denominator-selection theorem: "
            "D_EW=(q79+27-3)+lambda_12/((448/2)*448*pi), accepted strict P_EW "
            "rows = 1, accepted strict direct K_threshold.Omega_H.lambda rows = 1, "
            "and the strict zero-primitive K_threshold ledger is 10/10. The "
            "post-PEW precision ledger is rebuilt: precision policy, central "
            "replay, minimal PMNS oscillation policy, QCD theta slot policy, "
            "and tree local-QFT identity rows are closed. The precision "
            "transport/covariance easy-win subgates are now locked too: local "
            "RG benchmark/interface, 8x8 covariance target shape, proxy/operator "
            "slot inventory, admitted external threshold and mass-scheme replay "
            "lanes, diagonal replay tier, the typed no-knob kernel, and 11 "
            "already-executed support attempts. The Qa/SU3 source-slot layer is "
            "closed; the actual dynamic operator payload is now sharpened to the "
            "cross-repo 9-or-7 source-object/connection-value contract, with "
            "4/7 strict connection exports accepted by fresh raw-field validation "
            "and the counted AH-equivalent/projected Route-C lane closed at 8/8. Accepted "
            "precision source-value replay layers are now locked as well: "
            "8 replay/source-value classes are closed, including common-scale "
            "values at SM-parity tier, Higgs imported profile replay, 9 flavor "
            "policy rows, 8 operator source slots, dynamic Qa/SU3 first response, "
            "partial same-source payload, and the threshold response functional "
            "contract. The value-source promotion gate has now been executed "
            "across all three support routes: full profile likelihood, selected "
            "threshold response functional, and actual dynamic Qa/SU3 payload. "
            "All three routes have support closed, but promoted routes remain 0 "
            "and accepted true-equivalence precision rows remain 0. The final "
            "exit set is exactly: accepted full profile likelihood/official "
            "workspace, selected threshold response functional with VSD02 source "
            "rows, or actual dynamic Qa/SU3 payload values from selected "
            "post-source operator execution. The final profile/dynamic frontier is now "
            "reduced further: profile replay/surrogate support is present but "
            "full likelihood is open; dynamic values are ready with conditional "
            "Hessian values and primitive exactness, and the old "
            "source-rule/Galerkin gate is now consumed by later Route-A source "
            "promotion. The two-theorem frontier has its source-ownership "
            "acceptance criteria proved, finite rows are demoted to replay "
            "postchecks, the untransported BN shortcut is rejected, and the "
            "gauge-transported BN/PhiFin trace closes the selected Route-A "
            "source-promotion path. PSM-C1-02 unpatched source promotion is "
            "closed, A_selected, b_selected, and deltaTheta_C1 are promoted, "
            "and Route-B Galerkin export is not an active blocker for this "
            "gate. The post-source value-promotion row frontier is now "
            "re-executed too: admitted external threshold/profile replay closes "
            "4/5 value obligations and reaches 8/9 readiness, while internal "
            "no-knob value rows remain 0/5 and accepted true-equivalence "
            "precision rows remain 0. The internal Rtheta dynamic source "
            "blocker is also contracted by VSD01 source assembly: all 72 "
            "primitive rows are exact, formal 110-row assembly is closed, "
            "A/b/deltaTheta are promoted, but internal Rtheta scalar rows "
            "remain 0. The value-source-anchor row attempt is now executed "
            "against the closed contracts: 6 candidate source rows, 3 atomic "
            "routes, and 0 accepted internal coefficient/scalar/VSD02 rows. "
            "Full SM/no-knob "
            "closure remains open at the post-source gap. The post-source "
            "full-SM gap audit is now included: alpha1 driver, selected dotD "
            "source, honest dotD validator replay, and static matter-slot "
            "readout are closed. The same-source dynamic matter overlap packet "
            "is closed at first-response layer, dynamic Qa/SU3 first-response "
            "replay is closed, and the final value audit identifies the active "
            "wall: accepted common-scale Yukawa/Higgs values, threshold and "
            "mass-scheme values, full covariance/profile likelihood, and local "
            "QFT precision values. The value-wall chain is now included too: "
            "common-scale SM-parity replay, surrogate correlated threshold "
            "profile matrix, residual threshold/mass-scheme values, and source "
            "row audit are closed at their honest tiers, but accepted true-"
            "precision equivalence remains open. The value-source derivation "
            "cluster is now included: obligation kernel and external manifest "
            "are closed, same-branch threshold/mass-scheme readiness is 8/9, "
            "the final no-knob kernel is typed, the Rtheta basis map is closed, "
            "and the higher-response Rtheta functional contract fixes ten scalar "
            "row targets. Coefficient/payload execution remains open."
        )
        parts.append(
            "The latest Rtheta vector-emitter bridge is now included: charged "
            "L_rowlocal subfields are closed at 9/9 from the strict retarded-"
            "overlap trace rows, charged T_scheme=1 subfields are closed at "
            "9/9 from the source-native null-threshold rows, and the charged "
            "K_threshold rows are available at 9/9 inside the current "
            "E_Rtheta contract. At that intermediate bridge level Omega rows "
            "were not accepted yet; the next strict Omega/H-lambda bridge below "
            "consumes the H row-purpose formula identity while preserving the "
            "final scalar-value guard."
        )
        parts.append(
            "The strict Omega/H-lambda bridge has now advanced one level: the "
            "combined K_threshold-to-Omega algebraic bridge is closed for all "
            "ten slots, using Omega_i^src = D_fin[class(i)] * "
            "K_threshold.Omega_i * exp(-2*pi*n_i). The H/lambda row-purpose "
            "identity is closed at the row-id/formula level because the locked "
            "direct K_threshold.Omega_H.lambda row feeds the same Omega_H.lambda "
            "slot. This still does not accept final physical scalar rows: "
            "accepted profile value payload rows remain 0, internal scalar rows "
            "remain 0, and the next target is Omega value-payload/profile "
            "transport or an official likelihood workspace."
        )
        parts.append(
            "The Omega value-payload transport cutset is now built and audited. "
            "The old L_rowlocal/T_scheme/H-lambda formula blocker is no longer "
            "the active reason for rejection: the ten algebraic Omega source "
            "formula rows are available. The remaining strict exits are exactly "
            "two: an accepted official/full-covariance profile workspace, or a "
            "selected internal V_Rtheta value-payload operator emitting the ten "
            "physical Rtheta coefficient/profile scalar rows. Both exits remain "
            "unaccepted in the current inventory, so profile value payload rows, "
            "internal scalar rows, and true-equivalence precision rows remain 0."
        )
        parts.append(
            "The first internal V_Rtheta operator attempt is now audited as "
            "well: direct identity transport V_Rtheta^id(Omega)_i = Omega_i "
            "was tested on all ten slots and rejected as a physical value-"
            "payload operator. It passes the slot/formula/no-selector checks, "
            "but fails without a selected physical projection-normalization "
            "functional N_phys or an official full-profile workspace. The "
            "accepted identity-transport row count is 0 and final scalar rows "
            "remain 0; the next target is N_phys."
        )
        parts.append(
            "The N_phys projection-normalization split is now audited. The "
            "current frontier no longer treats Pi_Rtheta as open: the later "
            "value-evaluator packet closes Pi_Rtheta, selected dynamic operator "
            "ownership, the coefficient skeleton, and source-normalized unit "
            "sector weights. What remains open is the magnitude-bearing "
            "normalization/profile functional M_magprofile, or an official "
            "full-profile workspace. Unit source weights are not promoted into "
            "Yukawa/Higgs magnitudes; accepted scalar rows remain 0."
        )
        parts.append(
            "The M_magprofile promotion gate is now audited. Ten replay/profile "
            "scalar labels are available: nine charged Yukawa magnitudes and "
            "lambda_H. They remain replay/profile data, not no-knob source rows. "
            "A successor packet now imports the strict q64/s_beta phase-"
            "antisymmetry theorem and retires the stale 'phase scalar "
            "unselected' clause: one internal phase source scalar is accepted. "
            "This does not reopen Yukawa magnitudes, which remain locked at "
            "finite-replay/SM-parity tier 9/9 with residual 8.715792346058762e-14. "
            "A second successor packet closes the split M_magprofile value-"
            "payload layer at 10/10 rows: 9 charged finite-replay Yukawa rows "
            "plus 1 H/lambda strict direct-K row. The remaining target is no "
            "longer value-payload emission; it is true precision, namely full "
            "covariance/profile likelihood or internally selected threshold/"
            "mass-scheme transport into one common scheme. The precision split "
            "packet now closes the diagonal/readiness precision tier and locks "
            "the exact remaining object as PrecisionTransportValueObject: an "
            "8x8 covariance/profile value object with 36 symmetric unique "
            "entries or equivalent internal transport. Accepted full-covariance "
            "entries and true-equivalence precision rows remain 0."
        )
        parts.append(
            "The common-source precision successor retires the provisional "
            "direct-product independence rule and promotes an internally "
            "reconstructed first-pass 8x8 workspace. All 15 BCT-WZH cross "
            "entries are determined: 6 nonzero entries come from the executed "
            "MZ-to-Mt RG Jacobian and 9 are structural one-loop gauge-row "
            "zeros. The matrix is positive definite and no cross entries are "
            "missing. This is not yet multi-loop precision or a published/"
            "reconstructed joint likelihood; accepted true-equivalence "
            "precision rows remain 0."
        )
        parts.append(
            "The selected SMDR v1.3 successor now closes the multi-loop "
            "threshold/mass-scheme transport exit. Fifteen locked measured "
            "source coordinates are matched and run into eight full-SM MSbar "
            "coordinates at Q=Mt; the differentiated map emits a positive-"
            "definite 8x8 covariance with all 36 symmetric entries and all "
            "15 BCT-WZH cross entries nonzero and determined. Eight precision "
            "transport rows are accepted at the adopted diagonal-source/one-"
            "shared-primitive profile tier. The direct-K lambda postcheck is "
            "-1.0517 sigma. Official joint input correlations and strict no-"
            "knob derivation remain optional stronger upgrades; the final "
            "global true-SM closure audit is now closed below."
        )
        parts.append(
            "The renormalized-SM observable functor is now closed at the "
            "adopted parity/profile standard by the composition E_SM, standard "
            "BRST/Faddeev-Popov quantization, generating-functional derivatives, "
            "LSZ, and declared readout. The final global successor passes 12/12 "
            "obligations and closes true SM equivalence in the precise embedded-"
            "renormalized-SM sense at the one-shared-physical-primitive/profile "
            "standard. Full no-knob/unique-branch selection, official input "
            "correlations, strong-CP solution, absolute "
            "neutrino ontology, and derivation of quantization from MTT remain "
            "strictly stronger open programs."
        )
        parts.append(
            "The post-closure strict-upgrade program is now consolidated and "
            "executed once across all nine IDs. U4 CKM is resolved at the "
            "correct prediction-with-uncertainty standard, with 3 selected "
            "source rows and maximum profile displacement 2.36e-4 sigma; exact "
            "identity to a moving central estimator is retired. U2 closes "
            "2/2 literal witness families: the selected S3 Deligne-Cech table "
            "has 81 entries and all 729 cocycle triples pass, while the finite "
            "Chern/HYM sequence is finite-level stable and patches globally. "
            "Nested cutoffs 12/16/20/24/28 reach a final L2 difference 1.97e-14; "
            "the dealiased residual is 1.13e-10 with coercivity above 25.87. "
            "The exact weighted-theta Fourier tail and Wiener contraction then "
            "give Z=0.38508 and Y+Zr=0.00932703<r=0.01, closing continuum "
            "existence and local uniqueness; U2 literal witnesses are 2/2. "
            "U3 has a 15-coordinate, 3-authority source-block audit "
            "and frozen covariance replacement interface, but no public unified "
            "joint likelihood. U5 selects the Dirac channel, narrows Majorana "
            "characters to 0 or 672, and proves the three-basin minimal-trace "
            "formula conditionally gives m_lightest=0. Its former three source "
            "clauses are now one selected complex-symmetric neutral mass operator; "
            "the successor inventory is 4/8 with source id, neutral basis, "
            "Dirac/self-character gate, and no-observed-selector certificate "
            "closed. The dimensionful successor proves the remaining work has "
            "three lawful exits: Dirac-complete M_D=v_u Y_nu, Majorana/seesaw "
            "blocks with selected k=0 or 672, or nil-boundary effective spectrum "
            "plus reconstruction. The follow-up overlap/physical/action gate is "
            "now executed too, and the value-source pass promotes selected "
            "neutral carrier/projector and trace-Gram readiness. The next "
            "neutral Gamma_nu successor closes the typed L x N^c x H_u "
            "trilinear carrier skeleton with all nine structural 3x3 slots. "
            "The finite-channel successor imports the already selected same-source "
            "dynamic overlap theorem and proves Gamma_nu^chan=I3+X3: all nine "
            "finite rows are emitted, with six active channels and three exact "
            "zeros. Neutral overlap OK gates are now 6/9 and readiness subfields are "
            "8/13: L, N^c, and H-as-Hu carrier projectors, trace-Gram, "
            "same-source slot consistency, and the typed neutral trilinear "
            "skeleton, and finite channel sets are selected. All three exits remain unaccepted, physical "
            "omega_gap is still open, and Dirac-only action completeness is not "
            "derived. Finite Gamma_nu[i,j] channel sets are accepted, but no action costs, "
            "prefactors, retarded signs, or absolute value rows are accepted: dimensionful M_D/M_L/M_R blocks and absolute "
            "normalization remain open. The I3+X3 entries are exact channel "
            "multiplicities, not an absolute mass operator. The next successor also "
            "imports the selected second-order lambda orbit: the two neutral relative "
            "matrices have diagonal coefficient 1 and cyclic-shift coefficient "
            "3/2 plus or minus i*sqrt(3)/2, hence magnitude sqrt(3), phase orbit "
            "+/-pi/6, and spectrum [1,4,7]. This closes 18 relative dimensionless "
            "rows across two conjugate representatives, but no absolute value field, "
            "unique representative, or OK6 action-weight gate. A further same-source "
            "reconciliation closes all 9 internal dimensionless nuD H1 rows with "
            "a_int=0.34195899479289005 and 7/7 provenance fields; readiness is now "
            "9/14. This is not a physical Yukawa normalization or mass in eV, so "
            "physical value fields remain zero. The physical-unit/nil successor then "
            "proves a common scale cannot repair the selected [1,4,7] spectrum: nil "
            "subtraction gives [0,3,6] and ratio 0.5, versus the downstream NO "
            "postcheck ratio 0.029805. The simple scale-only route is retired. A "
            "minimal non-affine repair needs one sourced spectral-action slope plus "
            "one universal physical scale, or a selected seesaw block. The immediate "
            "spectral/seesaw successor executes the existing source-motivated candidates: "
            "the exact internal proper-time tau_int=log(448)/15 gives canonical trial "
            "ratio 0.227768, q79/q369 circle phases give 0.067879, q7/qmod gives the "
            "closest 0.031881, and pi/6 gives 0.5. None equals the 0.029805 downstream "
            "postcheck, and no neutral transfer law selects one. The CP/retarded character "
            "is also explicitly not the separately typed Majorana self-character. The "
            "generic fork is therefore sharpened to a neutral proper-time/circle-to-mass-cost "
            "transfer or a neutral real-structure functor. The proto-spinor successor then "
            "constructs the explicit 6x6 finite Dirac operator from the selected rank-three "
            "L/Nc Weyl blocks and full-rank I3+X3 transfer; it is self-adjoint and chirally "
            "odd. This closes finite Dirac encoding existence, not Dirac-only completeness. "
            "The selected H1 has eigenvalues approximately [-1.36784,-0.683918,+0.683918] "
            "and is therefore not a positive mass-squared Hessian. The coefficient-matched "
            "alignment trial has singular values [0,a,2a], an automatic nil zero mode, and "
            "squared splitting ratio 1/4; it is diagnostic because the radial VEV coordinate "
            "is not selected. The radial successor closes the exact formal Gram second "
            "variation with positive spectrum [2,2,8] and imports the independently selected "
            "H radial values tau_H=4.018017 and r_H=391.391403. Direct identity insertion of "
            "either H coordinate fails the neutral hierarchy, proving that a typed H-to-neutral "
            "normalization is required. The rank-one Higgs-insertion successor now closes that "
            "normalization: all nine typed neutral cells use the same normalized H:h0 carrier, "
            "dY_nu/dh_H=I3+X3 exactly, the insertion magnitude is one, and its unselected U(1) "
            "carrier phase cancels from the positive Gram curvature [2,2,8]. At the adopted "
            "profile standard v=246.219640 GeV is "
            "the shared electroweak baseline and adds no neutrino-specific knob; it remains a "
            "measured profile coordinate, not a strict no-knob MTT derivation. The exact next "
            "object is the action-weighted neutral Higgs response and dimensionful Dirac readout: "
            "the effective-weight successor proves that separate A_gamma and S_gamma are "
            "factorization-gauge variables, retires them as independent obligations, and imports "
            "the already-selected combined internal response. The conjugate representatives have "
            "identical mass-Gram spectra. The reduced physical cutset is now one source-selected "
            "non-affine neutral shape operator plus one same-scheme absolute scale; branch phase is "
            "needed separately only for CP-sensitive neutral observables. "
            "The CRT phase-typing successor then removes the apparent q7/448 near-hit: q7=2 is "
            "a Z7 residue with local fraction 2/7 and q7-only CRT lift 128/448=2/7, not 2/448. "
            "Thus the 0.031881 neutral-ratio clue was produced by mixing a residue numerator with "
            "the full modulus and is retired as a source candidate. The proto-spinor three-basin "
            "nil-drift formula remains the correctly typed neutral shape family; its genuine "
            "holonomy phi_nu and one absolute scale mu_nu are the two remaining physical coordinates. "
            "The common-circle factorization successor closes the previously missing transfer: the "
            "selected H_cen=diag(1,zeta3,zeta3^2) generates the proto-spinor cosine orbit through "
            "H_nu(phi_nu)=exp(i phi_nu)H_cen, and phi_nu=(arg det H_nu)/3 modulo 2pi/3. "
            "Thus only one shape scalar remains, but its value and the anchored Hessian scale are open "
            "because the operator-level neutral response H_nu is not emitted by the source-level packet. "
            "The later finite Stone-von Neumann rhoE promotion does not close that value: all 27 "
            "finite Heisenberg elements have determinant one, so the image lies in SU(3) and its "
            "determinant character is trivial. Determinant-trivial phases merely permute the Z3 "
            "orbit and retain exact twofold degeneracy. The required phase source is therefore the "
            "smooth determinant-line U(1) holonomy beyond the finite shadow, plus the anchored scale. "
            "At the explicit normal-ordering Dirac profile with m_lightest=0, the two measured "
            "oscillation splittings now calibrate phi_nu and A_nu analytically and fill all 36 "
            "neutral numerical rows: mass squares, absolute masses, Dirac Yukawa singular values, "
            "M_D, Y_nu, and the flavor mass-squared matrix. This is a two-primitive measured-profile "
            "execution, not a strict source theorem; ontology/order selection, covariance, smooth "
            "determinant-line holonomy, and the anchored scale remain open at the no-knob tier. "
            "The Lens/Dedekind successor then uses the independently selected retarded pair 16->15 "
            "and proves the exact reciprocity residue 12[s(15,16)+s(16,15)]+3-15/16-16/15=1/240. "
            "Its conditional determinant-line phase is phi_nu=pi/120 and predicts the mass-splitting "
            "ratio 0.02978657, only 0.0233 diagonal-profile sigma from the locked value; conditional "
            "neutral mass execution therefore drops from two measured splitting coordinates to one "
            "scale coordinate. This hypothesis was target-ranked, not pre-registered, and strict "
            "promotion still requires the neutral APS/Bismut-Freed operator, spin/orientation, and "
            "counterterm-cancellation identification. The absolute scale remains subject to the proved "
            "one-dimensional metrology no-go. The universal-E0 successor then tests the existing "
            "GR one-anchor family against the neutral scale. The target-ranked 11D trial "
            "mu_nu=E0*448^-11*exp(-tau_int/4), normalized by the A41 ratio, matches the A40 "
            "Hessian amplitude at about 18 ppm using the measured Newton constant as the one shared "
            "metrology primitive. Exponent 11 is uniquely nearest in the declared dimension scan, "
            "but strict promotion still requires a selected elevenfold attenuation and proper-time "
            "normalization theorem; no neutrino-specific parameter has been added. The composite-"
            "spectrum successor compresses the entire attenuation exactly to exp(-tau_int*661/4): "
            "eleven cost-15 contributions plus a quarter nil contribution. It also proves that "
            "1/(1+r_nu) is the unit-trace normalization of the diameter-normalized A41 shape, and "
            "the native corpus census is 4+(1+2+3)=10, with a conditional M-theory lift to 11. "
            "The 18 ppm match belongs only to that lifted hypothesis; the native 10D version is "
            "larger in A_nu by 448^2=200704. Source promotion remains open "
            "because the corpus does not replicate the cost-15 block over those dimensions, the "
            "neutral operator has not been selected on the lift, the nil quarter is only a benchmark saturation, and the GR audit forbids combining the "
            "Z64 and nil values without a selected same-operator branch bridge. "
            "The same-geometry generative-base successor keeps the already closed embedded local-QFT "
            "recovery fixed and attacks the stronger source problem. It proves the closed qutrit algebra "
            "A_Q=M3(C)^3 is not directly the SM finite algebra by dimension and center invariants, then "
            "constructs an exact conditional reduction across its three class lanes: a rank-one corner "
            "gives C, a rank-two corner with symplectic antiunitary real structure gives H, and the full "
            "third lane gives M3(C). Physical lane/projector and weak-real-structure selection remain open "
            "before the chiral representation and anomaly table can be emitted. "
            "U6 has the conditional PQ theorem and "
            "axion ratios. The exact E6 Qpsi color anomaly is +12 from matter and "
            "-12 from complete-27 exotics, so it cancels; the matter-only/singlet "
            "diagnostic gives N_DW=3. The remaining U6 object is one selected flux/"
            "threshold axion-current anomaly-matching map. U9 closes the antiunitary branch orbit and "
            "retarded q79 representative, but not the global carrier measure. "
            "U7 and U8 retain real conditional operator/constructive results "
            "without overclaiming first-principles quantization or full 4D "
            "nonperturbative QFT. The strict ledger is now 2 closed, 6 partial, "
            "and 1 dependency-blocked; the declared 12/12 baseline remains locked."
        )
        parts.append(
            "Deep frontier expansion is now included as well. The verifier carries "
            "the late support/no-go/value-emission leaves through Rtheta "
            "owner/projection, threshold mass-scheme readiness, H response/Herm(2)/"
            "radial/HK rows, HRG source tests, superseded EW diagnostics, full-sector HYM/delta-S2/"
            "CSK rows, same-source connection tables, visible Chern-Weil/DE/HYM "
            "source slots, and PSM-C1-02 physical action source attempts. The "
            "current honest leaves are: the cross-repo Qa/SU3 9-or-7 payload "
            "contract for selected source-object or typed Cech-HYM/projective "
            "connection values, currently 4/7 on the strict connection route "
            "with the counted AH-equivalent lane 8/8 closed; "
            "BCTFormulaImport_or_SelectedThresholdRowDerivation and "
            "RThetaSelectedRouteCGalerkinSolve_or_DiagonalProfileTheorem for true "
            "precision/profile rows; optional AEW/physical-prefactor packets only "
            "as superseded cross-checks, not active blockers; "
            "SameSourceConnectionValueTable/first same-source field or typed "
            "Cech-HYM connection values for the direct-HK path; and physical "
            "action/source-rule or independent primitive rows for unpatched "
            "finite-C1 promotion. Across these leaves, accepted new strict "
            "scalar/value rows remain zero; the newly closed material is source "
            "ownership, support, contracts, exact no-go guards, and narrowed "
            "execution gates."
        )
        result = 0

    text = "\n".join(parts)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(text + "\n", encoding="utf-8")
    print(text)
    return result


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
