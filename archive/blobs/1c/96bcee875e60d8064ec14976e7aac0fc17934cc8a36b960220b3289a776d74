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
    "selected_nonuniversalgaugeendomorphismsource_or_commonspectrumnogofinality_audit.py",
    "selected_samesourcegaugehessiancrossuse_or_sectorendomorphismvalueemission_audit.py",
    "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo_audit.py",
    "selected_finitekineticweightoperatorsource_or_circlelensnilzeromodegramexecution_audit.py",
    "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission_audit.py",
    "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission_audit.py",
    "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum_audit.py",
    "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission_audit.py",
    "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion_audit.py",
    "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission_audit.py",
    "selected_gaugekineticactionderivationandfrozenprofilevalidation_audit.py",
    "selected_normalizeddeterminantactionfrommtthessian_or_independentgaugeprofiletest_audit.py",
    "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation_audit.py",
    "selected_gaugeinsertionintertwinerandfinitematchingcondition_audit.py",
    "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains_audit.py",
    "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition_audit.py",
    "selected_chargedleptondualmetricsignandspectralactioncompleteness_audit.py",
    "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation_audit.py",
    "selected_fullanchordefecthessianactionownershipandspectatorcancellation_audit.py",
    "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion_audit.py",
    "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness_audit.py",
    "selected_closureshadowgaugeactionaxiomderivation_or_explicitadoptionandheldoutvalidation_audit.py",
    "selected_finitematchingcompletenessfromunifiedaction_or_explicitboundaryadoptionandheldoutvalidation_audit.py",
    "selected_phic1positivedensitypromotionfromclosedrouteasource_or_strictgaugerows_audit.py",
    "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation_audit.py",
    "selected_commonkineticnormalizationscalesymmetrynogo_and_crosssectoractionexit_audit.py",
    "selected_unitinstantonmodalactionquantumbridge_or_twistorcouplingsource_audit.py",
    "selected_posta89minimalparameterledger_and_nextfrontier_audit.py",
    "selected_neutraldeterminantlineapsoperator_and_native10dmassscale_audit.py",
    "selected_neutralrecursivesharedcirclediracdomainandspinbranchreduction_audit.py",
    "selected_neutrallensnildeterminantholonomyexecution_or_onescalefinality_audit.py",
    "selected_neutraloneholonomyonescaleontologyclosure_and_u5tierdecision_audit.py",
    "selected_postu5tierledger_and_u9globalbranchmeasure_audit.py",
    "selected_e6centralgeneratorqcdanomalyaudit_audit.py",
    "selected_fluxthresholdaxioncurrentanomalymatchingmap_audit.py",
    "selected_4dgreenschwarzaxionreductionandsurvivingcurrent_audit.py",
    "selected_axionqualityinstantonsuppressionbound_audit.py",
    "selected_q79multiaxionsupersetandhiddenblinddirection_audit.py",
    "selected_q79axioncouplinglatticeandns5worldsheetzeromodepacket_audit.py",
    "selected_q79hiddene8confinementandns5qualityamplitudecertificate_audit.py",
    "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution_audit.py",
    "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection_audit.py",
    "selected_q79twistedspectralgerbelifthymandbianchiexecution_audit.py",
    "selected_q79normalizedpoincaregerbeandpgl3prymreduction_audit.py",
    "selected_q79pgl3toprymgerbejacobianexecution_audit.py",
    "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution_audit.py",
    "selected_q79splittingconick3periodselectororexactgerbeexecution_audit.py",
    "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate_audit.py",
    "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution_audit.py",
    "selected_q79genus2lefschetzperiodreduction_audit.py",
    "selected_q79genus2criticalvalueandnodeisolation_audit.py",
    "selected_q79genus2basedpathsystemandmonodromycandidate_audit.py",
    "selected_q79genus2handlemonodromypromotion_audit.py",
    "selected_q79genus2localmonodromypromotion_audit.py",
    "selected_q79genus2distinguishedcutsystemandglobalrelation_audit.py",
    "selected_q79genus2integralsurfacecyclepresentation_audit.py",
    "selected_q79genus2certifiedthimbleperiodexecution_audit.py",
    "selected_q79genus2handleandlerayperiodexecution_audit.py",
    "selected_q79genus2normalfunctionbetaandintegralbranchexecution_audit.py",
    "selected_q79genus2delignebetaperiodandintegralbranchexecution_audit.py",
    "selected_q79aligneddivisornormalfunctionsourceandpgl3branchdiagnosis_audit.py",
    "selected_q79projectivelinechartcovarianceandellzerocontinuation_audit.py",
    "selected_q79picardlefschetzonesidedresidualregularization_audit.py",
    "selected_q79picardlefschetzintervalwallandbaselift_audit.py",
    "selected_q79validatedbetatransportandfiniteflatcontourhomotopy_audit.py",
    "selected_q79covariantperiodbranchcutsetandtightbetatransport_audit.py",
    "selected_q79alignmentcontinuousrootmonodromypromotion_audit.py",
    "selected_q79alignmenthandlesandglobalsurfacerelation_audit.py",
    "selected_q79alignmentintegralh2presentation_audit.py",
    "selected_q79alignmenteightbyninetytwoperiodexecution_audit.py",
    "selected_q79effectiveintegralbranchquotientandheightfourseed_audit.py",
    "selected_q79heightfourfrozencarrierrefinementandintervalcutset_audit.py",
    "selected_q79heightfoure32handleintervalandthimblecutset_audit.py",
    "selected_q79e32thimbleregularsingularreduction_audit.py",
    "selected_q79e32thimblehenselseedandfirstfullinterval_audit.py",
    "selected_q79e32clearancerankedsecondfullinterval_audit.py",
    "selected_q79e32clearancerankedbatchfrontier_audit.py",
    "selected_q79e32clearancerankedfourthfullinterval_audit.py",
    "selected_q79e32clearancerankedsuccessora140_audit.py",
    "selected_q79compacth1thimbleorientationgate_audit.py",
    "selected_q79e32clearancerankedappendchain_audit.py",
    "selected_q79projectivechartcovariante32intervaladapter_audit.py",
    "selected_q79e32physicalgeneratorzonotopetransport_audit.py",
    "selected_q79e32remainingappendandcarrierdecision_audit.py",
    "selected_q79heightfoursurvivorqueueande32priority_audit.py",
    "selected_q79e32primitivehandlebasisintervals_audit.py",
    "selected_q79heightfoursurvivore32decisions_audit.py",
    "selected_q79heightfourrefinede32decisions_audit.py",
    "selected_q79heightfourcomplexpgl3floatingboundary_audit.py",
    "selected_q79heightfourd087fullresiduemaininterval_audit.py",
    "selected_q79heightfourd087fullresidueinterval_audit.py",
    "selected_q79heightfourd087refinedfullresidueinterval_audit.py",
    "selected_q79heightfourd034refinedfullresidueinterval_audit.py",
    "selected_q79heightfourd041refinedfullresidueinterval_audit.py",
    "selected_q79heightfourd030refinedfullresidueinterval_audit.py",
    "selected_q79heightfourd062refinedfullresidueinterval_audit.py",
    "selected_q79heightfourdominantfivefullresiduerecomposition_audit.py",
    "selected_q79heightfourn3chaindecompositionfrontier_audit.py",
    "selected_q79heightfourd085refinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedsixfullresiduerecomposition_audit.py",
    "selected_q79heightfourd082zchartrefinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedsevenfullresiduerecomposition_audit.py",
    "selected_q79heightfourd021refinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedeightfullresiduerecomposition_audit.py",
    "selected_q79heightfourd047refinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedninefullresiduerecomposition_audit.py",
    "selected_q79heightfourd079zchartrefinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedtenfullresiduerecomposition_audit.py",
    "selected_q79heightfourd028refinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedelevenfullresiduerecomposition_audit.py",
    "selected_q79heightfourd015zchartrefinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedtwelvefullresiduerecomposition_audit.py",
    "selected_q79heightfourd057continuedpairrefinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedthirteenfullresiduerecomposition_audit.py",
    "selected_q79heightfourd032continuedpairrefinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedfourteenfullresiduerecomposition_audit.py",
    "selected_q79heightfourd027continuedpairrefinedfullresidueinterval_audit.py",
    "selected_q79heightfourcertifiedfifteenfullresiduerecomposition_audit.py",
    "selected_q79heightfourdynamictargetmanifest_audit.py",
    "selected_q79heightfourdynamiccertifiedprefixrecomposition_audit.py",
    "selected_q79heightfourrank3movingintervalblocks_audit.py",
    "selected_q79heightfourrank3fullresidualinterval_audit.py",
    "selected_q79heightfourcovarianthessianintegrandsource_audit.py",
    "selected_q79heightfourasymmetricprecisionbudgetlemma_audit.py",
    "selected_q79heightfourcanonicalcutoffinitializer_audit.py",
    "selected_q79fasttaylorruntime_equivalence_audit.py",
    "selected_q79stableaffinehessianruntime_inclusion_audit.py",
    "selected_q79heightfouraffinechainbasisreanchor_audit.py",
    "selected_q79heightfourbidirectionalmainhessian_audit.py",
    "selected_q79heightfourprecisionhessianmanifest_audit.py",
    "selected_q79heightfourd087farcutperiodsource_audit.py",
    "selected_q79heightfourd046farcutperiodsource_crosscheck_audit.py",
    "selected_q79heightfourd046farfullhessianinterval_audit.py",
    "selected_q79heightfourd065tailhessianinterval_audit.py",
    "selected_q79heightfourd082quadraturetailhessianinterval_audit.py",
    "selected_q79heightfouralltargettailhessianinterval_audit.py",
    "selected_q79heightfourd065mainfullhessianinterval_audit.py",
    "selected_q79heightfourrankthreebetahessianinterval_audit.py",
    "selected_q79heightfourrankthreehandlehessianinterval_audit.py",
    "selected_q79heightfourpgl3polydiskchartsource_audit.py",
    "selected_q79heightfourpgl3polydiskhessianintegrandsource_audit.py",
    "selected_q79heightfourpgl3centeredaffinehessiansource_audit.py",
    "selected_q79tracesplitclncarrierandworldinworldbridge_audit.py",
    "selected_q79signedsheetspinliftreduction_audit.py",
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
            "The post-A90 determinant-line typing audit then corrects the physical source scope: "
            "the selected internal topology is S1_cen x L(3,1) x Nil3, while 15 and 16 are "
            "Z64 cost/retarded labels rather than selected Lens parameters. The exact 1/240 "
            "identity is retained as the generic reciprocity remainder 1/(15*16), but cannot be "
            "called the eta invariant of the selected space. Provisional SL2Z completion has an "
            "infinite gamma_t family with Rademacher invariant 15+t. The native 10D action supplies "
            "a valid operator-construction domain but no selected metric, Dirac spectrum, Wilson "
            "line or numerical overlap. The strict determinant-line contract is therefore 2/10; "
            "the next constructive object is the twisted neutral Dirac family on the actual topology. "
            "The recursive-domain successor resolves that topology itself: the displayed S1_cen x "
            "L(3,1) x Nil3 is a reuse hierarchy, not a literal product. S1_cen is the lens fiber and "
            "the native internal manifold is X6=L(3,1)xNil3. It inventories four spin structures, "
            "constructs the smooth product neutral Dirac family 6/6, and proves that flat lens-fiber "
            "or nil-center characters cannot source a small nonzero phase. The determinant finality "
            "successor then separates det(E_nu), whose holonomy is det H_nu, from the analytic "
            "Bismut-Freed line Det(D_nu). Fixed SU3 data admit the full central lift torsor "
            "A_phi=A0+i phi alpha I3, proving exactly one irreducible holonomy coordinate. Finally, "
            "at the adopted one-holonomy plus one-scale profile standard, nonselfconjugate phi excludes "
            "Majorana blocks and |phi|<pi/6 selects normal ordering; all 36 A40 rows follow and the "
            "minimal PMNS count remains six. Strict no-knob U5 remains open at the holonomy value, "
            "absolute scale, nil-source promotion and covariance, but current-corpus phase search is frozen. "
            "The U9 measure successor closes the selected finite branch orbit at the same tier. "
            "Antiunitary invariance uniquely gives weights (1/2,1/2), while conditioning on the "
            "independently selected retarded orientation gives q79 probability one and the advanced "
            "orientation gives q369 probability one. A global probability law over every MTT carrier "
            "remains undefined at 0/6 required fields and is frozen rather than overclaimed. At the "
            "adopted tier the upgrade ledger is 4 closed, 4 partial and 1 dependency-blocked; the strict "
            "ledger remains 2/6/1. "
            "The same-geometry generative-base successor keeps the already closed embedded local-QFT "
            "recovery fixed and attacks the stronger source problem. It proves the closed qutrit algebra "
            "A_Q=M3(C)^3 is not directly the SM finite algebra by dimension and center invariants, then "
            "constructs an exact conditional reduction across its three class lanes: a rank-one corner "
            "gives C, a rank-two corner with symplectic antiunitary real structure gives H, and the full "
            "third lane gives M3(C). Physical lane/projector and weak-real-structure selection remain open "
            "before the chiral representation and anomaly table can be emitted. "
            "U6 is now advanced beyond the threshold no-go and the former 0/10 map. The selected "
            "compact oriented q79 heterotic background emits the model-independent B6 axion. "
            "Exact basic-form traces give I(E8->E6)=I(E6->SU3c)=1, hence k3=N_DW=1, while the "
            "pure-Qpsi identity remains anomaly-free by exact +12-12 Wess-Zumino matching. The "
            "canonical f_MI reduction formula is closed without a new axion parameter, although "
            "its absolute no-knob value remains subject to the dimensional-anchor guard. The U6 "
            "map is 9/10. Perturbative axion quality is exact, and the nonperturbative global-minimum "
            "test is reduced to three explicit M0/M1/M2 inequalities. A Fu-Yau Leray-Serre "
            "calculation supplies at least 20 model-dependent modes and 21 total pre-lifting axion "
            "candidates. The source-free E8xE8 reduction now closes the full structural rows "
            "k_vis=(1,+3d), k_hid=(1,-3d), and k_NS5=(1,0), with no flat-hidden assumption. "
            "The exact identity k_vis+k_hid=2k_NS5 rules out simultaneous hidden-and-NS5 "
            "cancellation while retaining QCD. The wrapped NS5 cycle, charge, and action formula "
            "S_NS5=2*pi/alpha_GUT are structurally 2/9, while selected numerical amplitudes remain "
            "0/9. Fu-Yau worldsheet lift/Pfaffian gates are exact, and worldsheet-only potentials "
            "cannot displace the primitive universal QCD angle. A101 repairs the source to the "
            "correct two-connection E8xE8 functional and closes the exact hidden-spectrum/confinement "
            "decision procedure. An exhaustive E8 Weyl/root computation gives the global characteristic "
            "minimum 30, ruling out complete hidden-E8 abelianization using only the two Fu-Yau circle "
            "curvatures in the smooth 24-unit source-free branch. It also identifies "
            "A_NS5=kappa/(16*pi*alpha_GUT) and closes the exact A98 parameter envelopes. A102 then "
            "constructs the exact minimal rank-one candidate allocation 9+11+4=24 and proves stable "
            "SU3 c2=9 and SU9 c2=11 HYM bundle existence. The affine-E8 A8 embedding gives "
            "SU(9)/Z3, branching 248=80+84+bar84, and the exact hidden cohomology check "
            "38+63+63=164; full SU9 holonomy would leave only a finite Z3 commutant. It also proves "
            "that a K3-pullback visible bundle has c3=0 and zero net four-dimensional chirality. "
            "A103 then proves full SU9 holonomy for every displayed stable hidden bundle, leaving "
            "only the finite Z3 commutant and no hidden gaugino condensate. It retires the invalid "
            "printed Iwasawa c3 source, constructs smooth shared-circle clutching bundles with "
            "c3=plus/minus6, and constructs the q79 determinant-zero degree-three spectral cover. "
            "A104 computes K_C^2=18, c2(C)=90, pg=9 and h11=74 and proves the integral "
            "dual-Poincare Dixmier-Douady class restricts to zero by delta.H=0, with H3(C,Z)=Z2 "
            "closing the torsion loophole. A105 fixes the zero-section Brauer normalization, uses "
            "determinant zero to kill the trace component, and reduces the analytic residue to an "
            "eight-dimensional Prym class Serre-dual to the eight-dimensional PGL3 alignment. "
            "A106 derives the marked K3 normal form w^2=G3^2+Q2 H4 directly from the lattice roots "
            "H+/-delta, with the exact 18-dimensional splitting-conic family count. It corrects the "
            "global gerbe-zero test to eight relative Deligne period congruences on an integral H2 "
            "branch and derives the residue basis, period table and full covariant 8x8 Jacobian. "
            "Thus the former 8 beta plus 64 Jacobian entries are outputs, not source rows. The "
            "remaining continuous geometric source is one 18-complex-dimensional marked K3 point "
            "plus one elliptic modulus; the eight PGL3 variables are solved coordinates. The prior "
            "tau=i Appell-Humbert packet is diagnostic only because no same-Fu-Yau crossuse theorem "
            "exists. A107 proves why: the single Chern pair (delta,0) has a parabolic SL2Z stabilizer "
            "with no order-four element, so a quarter-turn cannot preserve one Fu-Yau branch. The "
            "minimal lawful superset is the four-element orbit (delta,0),(0,delta),(-delta,0),(0,-delta). "
            "Conditionally selecting that parent makes the order-four action global, fixes tau=i and "
            "j=1728, and makes one gerbe-period execution sufficient for all four orientations. The "
            "strict source count remains 19 complex moduli; it drops to 18 only after a typed "
            "LensQuarterTurnToFuYauChernOrbitSourceTheorem. U9 retarded q79 selection is not silently "
            "reused for that new orbit. A108 then audits the printed Strominger selection theorem "
            "against its actual configuration space: X, J, E and topology are fixed, so it is only "
            "a conditional local field-selection result and contains no K3-period direction. Its OU "
            "term and epsilon^-2 fiber-gap arguments require correction before the fixed-field Hessian "
            "can be used unconditionally. Conditionally on a repaired invertible field block, A108 "
            "derives the exact K3 selector H_eff=H_pp-H_pu H_uu^-1 H_up on 36 real period directions. "
            "At conditional tau=i this joins the A106 eight-complex gerbe equations into a square "
            "52-real-equation system in the 36 K3-period and 16 PGL3 variables, with triangular "
            "determinant det(H_eff)*|det_C(D_A F)|^2 in the complex-linear case and the full "
            "16x16 realified gerbe determinant otherwise. Seven actual period-domain derivative fields "
            "remain unfilled, so no selected marked K3 or gerbe zero is invented. A109 takes the independent "
            "constructive branch and supplies one exact rational splitting-conic K3. Four separate projective "
            "ideal tests on all three affine charts reduce to the unit ideal, proving the conic and branch sextic "
            "smooth, the six Q2-G3 intersections reduced, and H4 nonzero there. The split curves realize the "
            "primitive lattice Gram(H,delta)=diag(2,-4). This fills 4/8 direct A106 model fields, or 5/8 only "
            "under the still-open Z4 tau=i bridge. It removes zero strict source moduli: the rational coefficients "
            "are an explicit existence/test witness, not an MTT-selected vacuum. A110 puts the square elliptic "
            "cubic and trial identity alignment on that carrier and proves the spectral surface smooth by an "
            "exact mutual-Gauss unit-ideal test on all nine product charts. It then constructs a nine-patch "
            "Cartier table for O(delta), verifies 72 inverse and 729 triple cocycle identities, and derives the "
            "unique Fu-Yau elliptic-torsor transitions plus the normalized Poincare formula "
            "alpha_ijk(ehat)=chi_ehat(n_ijk,0). The cocycle formula is now closed, but good-cover log values and "
            "all eight beta_C period rows remain zero. A111 replaces the vague surface-integration step by the exact "
            "projection C->E_i. Its fibers are genus-two curves u^2=f_ab(t), and the elliptic discriminant is "
            "P45(a)+b Q43(a). The degree-90 norm is square-free, so there are exactly 90 nodal fibers; their "
            "Euler contribution independently reproduces c2(C)=90 and b2(C)=92. A111 also emits all eight "
            "sl3 residue numerators and the explicit degree-zero splitting divisor D_delta on each fiber. The "
            "analytic gate is therefore one rank-four inhomogeneous genus-two Gauss-Manin/normal-function "
            "execution, not an unspecified good-cover search. A112 feeds the exact N90 to MPSolve with exact "
            "integer input and certifies 90 pairwise-disjoint isolating disks: 8 real roots and 41 nonreal "
            "conjugate pairs. Exact elliptic lifting gives b_j=-P45(a_j)/Q43(a_j), and the degree-one fiber "
            "subresultant gives t_j=-c0(a_j,b_j)/c1(a_j,b_j), with c1 proved nonzero on every critical value. "
            "Thus all 90 critical values and all 90 nodal points are now individually certified. A113 then uses "
            "the normalized square-torus uniformization with exact four-torsion base point (a,b)=(-i,1+i). It "
            "lifts the A112 disks to 90 disjoint torus balls and certifies one positive based meridian for each, "
            "plus the two A/B torus-handle paths that a genus-one base requires. A frozen FLINT transport computes "
            "90 candidate local matrices: every root permutation is a transposition, every recorded braid word "
            "replays exactly to an integral Sp4Z rank-one transvection, and the candidate vanishing cycles span "
            "all four H1 directions. They remain 0/90 promoted because their continuous local root trajectories "
            "were not saved. A114 separately certifies continuous disjoint root tubes over all 11,932 segments of "
            "the two nonlocal A/B torus-handle paths. An 80-digit interval projection certifies all 74 braid "
            "crossings and endpoint permutations; exact Birman-Hilden chain-twist replay promotes both resulting "
            "integral Sp4Z handle matrices. A115 then reconstructs all 90 local trajectories in a certified "
            "two-chart atlas, proves continuous disjoint root tubes over 300,428 local path segments, and "
            "interval-certifies 2,392 local braid crossings. Exact chart transport and chain-twist replay promote "
            "all 90 A113 transvections in the same frozen marking. The promoted inventory is therefore 90 local "
            "plus two handle actions. A116 cuts the base torus along A/B and certifies a 90-ray distinguished "
            "fan. Independent transport over those loops certifies 229,436 continuous root-tube segments and "
            "3,476 interval braid crossings, promoting all 90 distinguished positive PL factors. Their exact "
            "ordered product M90...M1 equals B^-1 A^-1 B A, closing the global integral H1 Gauss-Manin surface "
            "relation in the frozen marking. A117 supplies the preliminary rank reconciliation, and A118 "
            "executes all 90 primitive thimble columns with an independent floating rerun. A119 corrects the "
            "old direct-sum interpretation: period continuation selects central lifts +A,-B and aligns all "
            "90 endpoint-chord orientations. The handle-only Smith diagonal (1,1,1,3) becomes (1,1,1,1) in "
            "the full coupled thimble/handle relation lattice. A unimodular completion emits 82 pure-thimble "
            "plus 8 handle-supported primary columns. A primitive ambient fiber/horizontal Leray pair adds "
            "two exact-zero columns for the eight primitive sl3 residues. The exact rank-92 integral basis "
            "and full floating 8x92 period table are closed, with propagated two-run maximum column-scaled "
            "difference envelope 6.4785e-8. A120 then derives the exact balanced-sextic Mumford source and its "
            "inhomogeneous Gauss-Manin equation, executes the selected A/B lifts and 88 well-conditioned local "
            "meridians, and determines the two pole-adjacent translations uniquely from the exact affine surface "
            "relation. All 90 local translations are integral Picard-Lefschetz multiples, the exact affine "
            "boundary translation is [7,6,-4,7], every local singularity class vanishes, and the resulting global "
            "integral cocycle is nontrivial. This closes the selected normal-function source and affine cocycle, "
            "not by itself the normalized Deligne pairing. A121 uses A110's explicit (n_ijk,0) circle marking "
            "to prove the missing quotient-level transgression: DD(alpha)=delta cup u_A pairs by the torus "
            "bilinear relation to the complementary B-handle normal-function sweep, so beta_C=[R_B] modulo "
            "the A119 integral period image. All eight floating beta representative rows are emitted; their "
            "production/tight maximum difference is 5.922e-10. Interval enclosure, exact Z^92 membership, the "
            "beta zero/no-go decision and the PGL3 Jacobian remain open. A122 then closes the exact same-carrier "
            "aligned-divisor source: q_A roots and their implicit velocities must vary with the aligned sextic, "
            "and the identity specialization preserves A121. Pre-fix nonidentity beta/Jacobian values are retired. "
            "Four fresh full-rank corrected Jacobians reduce the identity beta norm from 5.110165 to 2.729845; "
            "two independent descents then show raw z-chart gaps near 0.005, and 12 additional path-guarded "
            "carriers find no zero. A123 proves exact covariance between the z- and y-elimination line charts "
            "for Q2,G3,H4,F6, the moving residue forms and all five reduced periods; the transition determinant "
            "is -1. The corresponding regular-chart gaps are 0.095842 and 0.127416, retiring the first apparent "
            "nodal wall as a coordinate artifact. Same-base-lift beta transport agrees across charts to 1.312e-5 "
            "at production tolerance. Three fresh-Jacobian and two guarded Broyden steps continue the ell=0 norm "
            "from 2.729845 to 2.357980 and localize a later genuine pair at projective separation about 0.01202. "
            "A124 solves that wall at maximum f/Ft residual 5.087e-12 with coupled-Jacobian minimum singular value "
            "11.0736, nonzero f_tt, regular y-chart scale 0.874035, q-divisor disjointness and a transverse nonzero "
            "Im(du*/ds). It proves the exact local vanishing state V_k=2*pi*i*t_*^k/sqrt(f_tt/2): the common "
            "inhomogeneous source cancels between the two continuations, so their beta difference is the endpoint "
            "homogeneous Gauss-Manin transport of V. Independent one-sided extrapolation gives selected/crossed "
            "norms 2.357163/2.788073. The transported and measured jumps have projective overlap "
            "0.999999999999962 and relative residual 2.747e-7 after a scale within 1.16e-5 of unity. The local "
            "formula is exact and the unit-jump execution is floating. A125 promotes the wall to Arb/ACB interval "
            "scope: a radius-1e-10 Krawczyk box has minimum strict-inclusion margin 6.385e-11, with whole-box "
            "lower bounds |f_tt|>518938.3935, |f_u|>32979.6834, |q_A(t*)|>0.2858552 and regular-chart scale "
            ">0.8740348452. Its certified Im(du*/ds) interval excludes zero. The interval bound "
            "|V_0|>0.012334923056187106 and invertibility of homogeneous Gauss-Manin transport prove a nonzero "
            "Picard-Lefschetz jump, so both one-sided beta limits cannot vanish. A125 also certifies the finite "
            "selected-side five-component Abel-Jacobi base lift with 599 path segments, 2995 ACB integrals, "
            "maximum component radius 9.366e-48 and opposite-sheet cancellation below 5.176e-64. A floating "
            "same-branch lower contour agrees with straight transport to 1.454e-8 and reduces conditioning by "
            "17.62. A126 certifies its local homotopy rectangle by argument-principle windings "
            "(0,0,0,-1,0): the one Q2 root exchange is harmless because O[t]/(Q2) remains finite flat and "
            "G3 is a unit, so the symmetric Cartier divisor and exact quotient-trace source extend. Order-28 "
            "defect-corrected transport then gives ||beta(1)||_2>2.2500100575 and excludes the frozen selected "
            "ell=0 branch. The broad lower strip is retired by reduction/divisor windings -4/-1. The global "
            "PGL3 no-go and exact integral-branch decision remain open. A127 tightens the same endpoint "
            "enclosure to ||beta||_2>2.3372259957 with component radius below 0.007061. It proves that "
            "A126's selected-alignment beta cannot be paired with A119's identity-alignment period table, "
            "while any independently certified endpoint integral basis is sufficient by GL(92,Z) basis "
            "invariance. It then computes the exact degree-30 dual sextic discriminant, reproduces A111 at "
            "identity, pulls it back through the selected interval alignment, isolates all 90 simple nodal "
            "critical values and their elliptic lifts, certifies a 90-meridian fan avoiding all three selected "
            "line-chart zeros, and computes 90 pointwise integral Picard-Lefschetz transvections in one common "
            "reciprocal branch chart. A128 then promotes all 90 local actions on that same selected carrier: "
            "1,052,626 path segments have disjoint Arb/ACB root tubes, while an independent 80-digit interval "
            "projection certifies every braid crossing and event order before exact integral PL replay. A129 "
            "certifies the two selected torus-handle transports and closes the exact punctured-torus relation "
            "M_90...M_1=B^-1 A^-1 B A with no fitted conjugation. A130 derives the handle central lifts +A,-B "
            "from certified winding numbers 6 and -5 of the reciprocal sextic leading coefficient. The coupled "
            "integer presentation has saturated vanishing-image Smith diagonal (1,1,1,1), full relation Smith "
            "diagonal (1,1,1,1), a unimodular 90-column primary completion, and a primitive Leray hyperbolic "
            "pair, closing an explicit rank-92 integral H2 basis on the selected carrier. A131 then executes "
            "all 90 selected thimbles in a period-blind A123 y/z atlas, synchronizes their numerical chord "
            "orientations to the A130 lattice, independently replays the interval-selected handle lifts, and "
            "assembles the full floating 8x92 period matrix. All 720 primitive entries have tighter reruns, "
            "the propagated primary column-scaled envelope is below 1.66e-9, and the 16 Leray entries vanish "
            "exactly. A132 then quotients the primitive rank-two Leray-null sublattice exactly, reducing the "
            "effective branch domain from Z92 to canonical Z90 coordinates. A fixed same-carrier Kannan grid "
            "emits a height-four continuation seed with maximum center residual 0.0055064 inside the current "
            "0.0070602 beta component radius; this is a discrete seed, not four fit parameters. Because the "
            "nonzero period errors are still two-run envelopes rather than interval bounds, the overlap is not "
            "promoted to exact membership. A133 then reruns the rigorous selected-side beta transport at order "
            "40 with maximum step 0.003, improving the component radius to 0.00216827 while preserving the "
            "center to about 1e-14. The E32 component has residual magnitude 0.00550639, so frozen-carrier "
            "separation now reduces to one selected complex period-combination enclosure with radius below "
            "0.00333813. The A131 two-run proxy is about 2.40e-8 and conditionally separates by 0.00333810, "
            "but it remains a convergence proxy rather than interval proof. That one combined-period interval "
            "is now split rigorously. A134 certifies the selected E32 handle contribution by direct algebraic-cut "
            "base periods and validated homogeneous Gauss-Manin transport: its interval radius is 4.985e-4 "
            "and its center agrees with A131 to 2.50e-10. After charging both terms, 2.83965e-3 of the strict "
            "budget remains for one weighted 71-thimble combination (primitive L1 norm 123). That weighted "
            "thimble interval is no longer approached through a raw fixed-frame norm. A135 replays the exact "
            "interval-certified local Picard-Lefschetz matrices on all 71 selected thimbles: every N=T-I has "
            "rank one and N^2=0, and its primitive image direction lies in ker(N) and is fixed by T. Hence the "
            "selected vanishing period is the log-free Frobenius branch, with explicit recurrence inverse "
            "(nI-R)^-1=(I+R/n)/n. A136 now instantiates that theorem on the first selected weighted thimble "
            "without a raw pole norm: interval Newton isolates the node and double root, a quantitative "
            "Weierstrass/Hensel disk certifies the log-free endpoint tail, and a six-dimensional homogeneous "
            "augmented frame certifies the ordinary main segment. Their oriented splice encloses E32(d004) "
            "with radius 1.436e-5, contains the independent A131 center without using it as a bound, and lies "
            "inside the 2.309e-5 A134 per-unit fallback. A137 then closes d061, a coefficient-minus-three row, "
            "using 384 desingularized tail segments and a final-radius segmented transport on the same radial "
            "homotopy class. Its full radius is 1.242e-5 and contains the independent A131 center. Two of 71 "
            "thimbles are thereby closed. A138 adds d019, a coefficient-plus-three row whose 1536-segment tail "
            "and final-radius main transport splice to a full radius 2.853e-7. The reusable batch ledger is now "
            "3/71 support and L1 weight 8/123. A139 append-only closes d028, coefficient plus two, with a "
            "384-segment tail, 134-step main transport and full radius 5.072e-6. The ledger is now 4/71 support "
            "and L1 weight 10/123. A140 then closes d020, coefficient minus three, with a 384-segment tail, "
            "100-step main transport and full radius 2.905e-6, while installing a reusable queue-head append "
            "builder. A141 uses that generic successor unchanged to close d062, coefficient plus one, with a "
            "384-segment tail, 125-step main transport and full radius 1.454e-6. A142 closes d021, coefficient "
            "minus three, after proving that the cutoff-nearest pair was not the vanishing pair and replacing "
            "that shortcut with a deep-seed, certified-node pair selector in both main and tail transports. Its "
            "384-segment tail and 115-step main transport splice to radius 6.163e-6. A143 applies the strengthened "
            "pair selector uniformly to d029, coefficient plus two, whose 384-segment tail and 135-step main "
            "transport splice to radius 2.635e-6. A144 closes the borderline d005 coefficient-minus-three row "
            "with a 120-digit, order-64, 165-step main transport: its main radius is 4.131e-7 and the full splice "
            "radius is 4.784e-6. A145 then closes d057, coefficient plus three, by replacing repeated rotated-box "
            "error inflation with an uncompressed physical-generator zonotope. At cutoff 2e-5, its 384-cell tail "
            "has radius 1.717e-6 and its 252-step main transport has radius 1.039e-5; the full splice radius is "
            "1.641e-5. Intermediate endpoint radii are not monotone, so aborted probes are not treated as no-go "
            "evidence. A146 reuses the same frozen zonotope builder on d037, coefficient minus two: its 235-step "
            "main radius is 8.254e-8 and its tail-dominated full radius is 7.755e-7. A147 closes d060, coefficient "
            "plus one, after a geometry-only scan selects a null-homotopic offset detour with critical clearance "
            "1.557e-2. Its main transport now consumes the tail-certified cutoff-period ball directly and gives "
            "main radius 8.267e-8 and full radius 5.634e-6. A148 applies the same source-reuse rule to d087, "
            "coefficient minus one: a 534-route geometry scan selects (0.25,0,0.74), its 139-step zonotope main "
            "radius is 4.921e-8, and its full radius is 4.366e-6. A149 and A150 use the same certified-tail "
            "handoff to close d011 and d086. A151 then executes the first complete native z-chart row, d048: "
            "A123 supplies the exact chart overlap, the L2 wall is interval-isolated, and a 68-step zonotope "
            "main transport splices to full radius 1.126e-7. The chart-parametric source is a byte-certified "
            "conservative extension: specializing it back to y reconstructs the recorded historical transport, "
            "augmented-main, and full-splice hashes exactly. A152 closes d088 after the default 48-cell tail is "
            "correctly rejected and the established 384-cell partition certifies radius 1.340e-8. A geometry-only "
            "scan accepts 527 of 1122 routes; the top route (0.35,0.01,0.82) supports a 128-step main radius "
            "4.061e-7 and full radius 5.877e-7. A153 then closes d033 on the selected radial-class route. Its "
            "171 accepted zonotope steps reject 84 noncontractive or locally over-budget proposals, cross the "
            "conditioning pocket without reboxing, and finish with main radius 6.326e-7; the tail-dominated full "
            "radius is 4.934e-6. A154 closes d035, coefficient plus one, after the geometry scanner selects the "
            "null-homotopic (0.2,0,0.74) route. Its 191 accepted steps reject 97 trial steps, finish with main "
            "radius 1.417e-6, and splice with the 384-cell tail to full radius 3.894e-6. A155 closes d063, "
            "coefficient plus two, on the scanner-selected (0.2,0.02,0.78) route with other-critical clearance "
            "1.653e-2. Its 100 accepted steps reject 17 trial steps, finish with main radius 3.431e-6, and splice "
            "to full radius 5.044e-6. A156 closes d026, coefficient minus one, on the scanner-selected "
            "null-homotopic (0.2,0,0.74) route. Its 148 accepted steps reject 46 trial steps, finish with main "
            "radius 1.331e-6, and splice with the 384-cell tail to full radius 1.893e-6. A157 closes d032, "
            "coefficient plus one, after the deeper radial selector identifies the correct near-node pair. The "
            "scanner-selected (0.45,-0.02,0.86) route has other-critical clearance 1.508e-2; 100 accepted steps "
            "reject 33 trial steps, finish with main radius 2.033e-7, and splice to full radius 2.355e-6. A158 "
            "then closes d030 and corrects the polygonal orientation gate: the 90-thimble synchronization theorem "
            "uses exactly the two compact-H1 holomorphic periods, while the three higher meromorphic rows retain "
            "puncture-lift dependence and cannot select the sign. On (0.25,0.02,0.86), the compact sign residual "
            "is 1.923e-10; 91 accepted steps reject 24 trials, finish with main radius 6.577e-8, and splice to "
            "full radius 1.463e-6. A159 closes d085, coefficient plus one, using the standard interval node pair "
            "and the tail-certified cutoff-period balls on the frozen (0.2,0,0.7) route. Its order-20 adaptive "
            "transport retains the unchanged local correction gate, accepts 148 steps, rejects 53 trials, gives "
            "main radius 1.190e-5, and splices to full radius 1.860e-5 with floating-center containment. The "
            "append-only ledger is now 24/71 support and L1 weight 45/123; 47 thimbles and the weighted sum "
            "remain open, with 2.593392e-3 strict budget remaining. A160 closes d010, coefficient plus one. "
            "The order-20 compressed frame completes but is rejected above the main-radius cap; the same frozen "
            "node, tail, (0.2,-0.01,0.65) route, precision, and local gate close with the uncompressed zonotope. "
            "Its 193 accepted steps and 102 rejected trials give main radius 9.198e-7 and full radius 4.561e-6, "
            "with floating-center containment. The ledger is now 25/71 support and L1 weight 46/123; 46 "
            "thimbles remain, with 2.588677e-3 strict budget. A161 closes d012, coefficient plus one, on the "
            "scanner-selected null-homotopic (0.32,0.01,0.86) route. Its order-20 uncompressed zonotope accepts "
            "190 steps, rejects 100 trials, gives main radius 5.744e-7, and splices with the 384-cell tail to "
            "full radius 2.308e-6 with independent-center containment. The ledger is now 26/71 support and L1 "
            "weight 47/123; 45 thimbles remain, with 2.586204e-3 strict budget. A162 closes d017, coefficient "
            "plus two, despite its more weakly conditioned node. The scanner-selected (0.45,0.01,0.86) route "
            "has critical clearance 1.073e-2; its order-20 zonotope accepts 182 steps, rejects 95 trials, gives "
            "main radius 3.832e-7, and splices to full radius 1.872e-6 with independent-center containment. The "
            "ledger is now 27/71 support and L1 weight 49/123; 44 thimbles remain, with 2.582458e-3 strict budget. "
            "A163 closes d051, coefficient minus two, through a narrow critical-value tube on the radial-class "
            "(0.2,0,0.74) representative. Its order-20 zonotope accepts 259 steps, rejects 153 guarded trials, "
            "gives main radius 1.179e-6, and splices to full radius 2.020e-6 with independent-center containment. "
            "The ledger is now 28/71 support and L1 weight 51/123; 43 thimbles remain, with 2.578408e-3 strict budget. "
            "A164 closes d055, coefficient plus one, on the scanner-selected (0.6,0.01,0.65) route. Its order-20 "
            "zonotope accepts 243 steps and rejects 145 guarded trials; the intermediate radius contracts under "
            "later transport to main radius 1.334e-6, then splices to full radius 4.648e-6 with independent-center "
            "containment. The ledger is now 29/71 support and L1 weight 52/123; 42 thimbles remain, with "
            "2.573559e-3 strict budget. "
            "A165 closes d034, coefficient minus three. Its standard 384-cell tail is correctly rejected for "
            "overlapping orientation intervals; a same-geometry 768-cell refinement closes the tail. On the "
            "intrinsically narrow-clearance radial-class (0.2,0,0.74) route, the order-20 zonotope accepts 288 "
            "steps, rejects 183 guarded trials, gives main radius 2.207e-6, and splices to full radius 8.648e-6 "
            "with independent-center containment. The ledger is now 30/71 support and L1 weight 55/123; the "
            "ranked y queue is exhausted, 40 native z rows plus the separate d047 partial remain, and the strict "
            "budget is 2.546770e-3. "
            "A166 then closes the first post-y native z row d059, coefficient plus three. Its node pair [0,1] "
            "has interval Jacobian lower bound 16.1299, the standard 384-cell tail closes at radius 3.220e-9, "
            "and all 1122 geometry-only routes are null-homotopic. On the ranked (0.2,0,0.82) route, the "
            "order-20 zonotope accepts 74 steps, rejects 21 guarded proposals, gives main radius 8.601e-8, "
            "and splices to full radius 1.249e-7 with independent-center containment. The ledger is now "
            "31/71 support and L1 weight 58/123; 39 untouched native z rows plus the d047 partial remain, "
            "the strict budget is 2.546395e-3, and d031 is the next frozen z head. "
            "A167 closes that native z row d031, coefficient minus two. Its node pair [4,5] has interval "
            "Jacobian lower bound 670.697, the 384-cell tail closes at radius 1.062e-8, and all 1122 route "
            "candidates are null-homotopic. On the ranked (0.2,0,0.65) route, the order-20 zonotope accepts "
            "132 steps, rejects 67 guarded proposals, gives main radius 1.816e-7, and splices to full radius "
            "2.675e-7 with independent-center containment. The ledger is now 32/71 support and L1 weight "
            "60/123; 38 untouched native z rows plus d047 remain, the strict budget is 2.545859e-3, and d039 "
            "is the next frozen z head. "
            "A168 closes d039, coefficient minus two, on native z pair [1,2]. Its node Jacobian lower bound is "
            "6.91386; the coarse tail partition is rejected and the 96-segment refinement closes at radius "
            "1.407e-6. The geometry scan accepts 815 of 1122 null-homotopic routes. On the ranked "
            "(0.45,-0.01,0.86) route, the order-20 zonotope accepts 103 steps, rejects 32 guarded proposals, "
            "gives main radius 1.088e-7, and splices to full radius 1.561e-6 with independent-center "
            "containment. The ledger is now 33/71 support and L1 weight 62/123; 37 untouched native z rows "
            "plus d047 remain, the strict budget is 2.542615e-3, and d014 is the next frozen z head. "
            "A169 closes d014, coefficient minus one, on native z pair [3,4]. Its node Jacobian lower bound is "
            "139.586; the 384-segment tail is rejected and its 768-segment refinement closes at radius "
            "1.155e-8. All 1122 route candidates are null-homotopic. On the ranked (0.2,0,0.65) route, the "
            "order-20 zonotope accepts 75 steps, rejects 23 guarded proposals, gives main radius 1.224e-7, "
            "and splices to full radius 1.846e-7 with independent-center containment. The ledger is now "
            "34/71 support and L1 weight 63/123; 36 untouched native z rows plus d047 remain, the strict "
            "budget is 2.542431e-3, and d075 is the next frozen z head. "
            "A170 closes d075, coefficient minus two, on native z pair [3,4]. Its node Jacobian lower bound is "
            "1.297686e6, and the 384-segment tail closes at radius 5.828e-6. The geometry scan accepts 606 "
            "of 1122 null-homotopic routes. On the ranked (0.2,0,0.65) route, the order-20 zonotope accepts "
            "149 steps, rejects 55 guarded proposals, gives main radius 2.127e-7, and splices to full radius "
            "6.129e-6 with independent-center containment. The ledger is now 35/71 support and L1 weight "
            "65/123; 35 untouched native z rows plus d047 remain, the strict budget is 2.529649e-3, and d018 "
            "is the next frozen z head. "
            "A171 closes d018, coefficient minus two, on native z pair [4,5]. Its node Jacobian lower bound is "
            "471609.663, and the 384-segment tail closes at radius 1.243e-6. The geometry scan accepts 1119 "
            "of 1122 null-homotopic routes. On the ranked (0.45,-0.01,0.86) route, the order-20 zonotope "
            "accepts 111 steps, rejects 55 guarded proposals, gives main radius 1.124e-7, and splices to full "
            "radius 1.402e-6 with independent-center containment. The ledger is now 36/71 support and L1 "
            "weight 67/123; 34 untouched native z rows plus d047 remain, the strict budget is 2.526744e-3, "
            "and d001 is the next frozen z head. "
            "A172 closes d001, coefficient plus one, on native z pair [0,1]. Its node Jacobian lower bound is "
            "3472.475, and the 384-segment tail closes at radius 5.465e-7. The geometry scan accepts 902 of "
            "1122 null-homotopic routes. On the ranked (0.55,0.03,0.86) route, the order-20 zonotope accepts "
            "117 steps, rejects 36 guarded proposals, gives main radius 4.584e-6, and splices to full radius "
            "7.030e-6 with independent-center containment. The ledger is now 37/71 support and L1 weight "
            "68/123; 33 untouched native z rows plus d047 remain, the strict budget is 2.519699e-3, and d046 "
            "is the next frozen z head. "
            "A173 closes d046, coefficient plus three, on native z pair [1,2]. Its node Jacobian lower bound is "
            "4.985; the 384-segment tail is rejected and the same-contour 768-segment refinement closes at "
            "radius 1.041e-6. The geometry scan accepts 495 of 1122 null-homotopic routes. On the ranked "
            "(0.45,0.02,0.70) route, the order-20 zonotope accepts 164 steps, rejects 66 guarded proposals, "
            "gives main radius 6.883e-7, and splices to full radius 2.014e-6 with independent-center containment. "
            "The ledger is now 38/71 support and L1 weight 71/123; 32 untouched native z rows plus d047 remain, "
            "the strict budget is 2.512759e-3, and d089 is the next frozen z head. "
            "A174 closes d089, coefficient minus one, on native z pair [1,2]. Its node Jacobian lower bound is "
            "82.940, and the 384-segment tail closes at radius 2.132e-9. All 1122 route candidates are "
            "null-homotopic. On the ranked (0.35,0,0.70) route, the order-20 zonotope accepts 71 steps, "
            "rejects 16 guarded proposals, gives main radius 2.935e-7, and splices to full radius 4.172e-7 "
            "with independent-center containment. The ledger is now 39/71 support and L1 weight 72/123; "
            "31 untouched native z rows plus d047 remain, the strict budget is 2.512341e-3, and d069 is the "
            "next frozen z head. "
            "A175 closes d069, coefficient minus two, on native z pair [3,4]. Its node Jacobian lower bound is "
            "859.513, and the 384-segment tail closes at radius 9.208e-7. The geometry scan accepts 526 of "
            "1122 null-homotopic routes. On the ranked (0.35,-0.02,0.70) route, the order-20 zonotope accepts "
            "138 steps, rejects 37 guarded proposals, gives main radius 3.048e-7, and splices to full radius "
            "1.352e-6 with independent-center containment. The ledger is now 40/71 support and L1 weight "
            "74/123; 30 untouched native z rows plus d047 remain, the strict budget is 2.509574e-3, and d050 "
            "is the next frozen z head. "
            "A176 closes d050, coefficient plus one, on native z pair [1,2]. Its node Jacobian lower bound is "
            "3.284; the 384-segment tail is rejected and the same-contour 768-segment refinement closes at "
            "radius 3.890e-10. The geometry scan accepts 992 of 1122 null-homotopic routes. On the ranked "
            "(0.20,-0.01,0.86) route, the order-20 zonotope accepts 92 steps, rejects 30 guarded proposals, "
            "gives main radius 1.259e-7, and splices to full radius 1.784e-7 with independent-center "
            "containment. The ledger is now 41/71 support and L1 weight 75/123; 29 untouched native z rows "
            "plus d047 remain, the strict budget is 2.509396e-3, and d066 is the next frozen z head. "
            "A177-A205 then close all 29 remaining native-z rows without changing the A134 fallback or weighted "
            "budget. A206 promotes the coefficient-four d047 hard row using its 768-segment refined tail and a "
            "proved containment reuse of the already-certified main transport. The ledger is exactly 71/71 support "
            "and L1 weight 123/123, with remaining weighted budget 2.344200e-3 and no ranked or partial row left. "
            "A207 applies the frozen A130/A131 canonical orientation signs to the raw holomorphic interval packets. "
            "The exact integer-weighted 71-thimble ball has radius 4.842494e-4 and contains the independent A131 "
            "center with displacement 2.677700e-6. Adding the certified handle gives cost 1.191874e-3 below the "
            "A133 strict budget 3.338125e-3. The final residual imaginary interval is strictly negative, giving the "
            "rigorous absolute-value lower bound 1.698084e-3. The frozen height-four carrier is therefore rejected "
            "in E32; no solution on another carrier is asserted. A208 then reconstructs the unchanged finite A132 "
            "Kannan grid and records all five height-four beta-enclosure rows: the published winner is unique under "
            "the recorded objective, A207 rejects exactly that row, and four finite-grid survivors remain. Their "
            "required thimble union is 86/90, with d006-d009 unused. The 15 newly required intervals close, including "
            "d041 at order 24 with full radius 1.130252e-6. A209 certifies four rigorous base cuts and all eight "
            "primitive A/B E32 handle columns; A210 aggregates every fixed-grid row. No additional row is separated "
            "under the reusable primitive-basis handle bounds, so ranks 2-5 remain E32-nonseparated rather than "
            "proved solutions. This finite-grid enumeration is not promoted to exhaustive Z90 height-four closure. "
            "The foundational FB1 "
            "successor then corrects the old inference from ranks 1,2,3 to a sourced nested flag. The connected "
            "q79 degree-three cover has finite locally free algebra A=pi_*O_C and the canonical trace split "
            "A=O direct-sum ker(Tr) of ranks 1+2. With one reused full A copy and the common shared-circle "
            "factor this gives the exact 1+2+3=6 CLN carrier with zero new continuous parameters. Transitive "
            "sheet monodromy forbids a global ordered-sheet flag. The sign-twisted permutation action lies in "
            "SO3. FB2 proves the actual sheet group is S3 and that its Spin3 preimage is the non-split binary "
            "dihedral group Dic_3 of order 12; exact quaternion braid generators lift locally with squares and "
            "Coxeter cube equal to the central -1. The remaining proto-spinor gate is now the finite global "
            "q79 relator-sign/w2 decision, branch-locus continuation, and selected world-in-world Q/Hessian "
            "intertwiner. These source corrections do not reopen the locked 27x27, Yukawa, EW, or profile values. "
            "The selected marked K3 and exact period zero, twisted spectral sheaf, inverse-Fourier-Mukai local "
            "freeness, balanced HYM, differential Bianchi identity and seven numerical NS5 inputs "
            "remain open; U6 is not declared fully closed. "
            "U9 closes the antiunitary branch orbit and "
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
