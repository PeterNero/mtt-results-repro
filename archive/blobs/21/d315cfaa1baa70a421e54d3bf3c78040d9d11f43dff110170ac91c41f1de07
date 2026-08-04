"""Run the fast frontier verifier for the MTT SM-parity closure repo.

The active frontier verifier was frozen on 2026-07-04 as
`scripts/verify_full_frozen_2026_07_04.py`.  This active verifier is kept small
so current frontier calculations do not spend two minutes replaying stable
legacy audits on every iteration.

Use:
  python scripts/verify.py        # fast frontier verification
  python scripts/verify.py --full # delegate to frozen full-chain verification
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
FROZEN_FULL = ROOT / "scripts" / "verify_full_frozen_2026_07_04.py"

AUDITS = [
    # Stable guardrails retained in every frontier run.
    "sm_parity_closure_ledger_audit.py",
    "core_axioms_measured_parameter_interface_audit.py",
    "sm_equivalence_superset_strategy_controller_audit.py",
    "selected_smparityfrozenboundary_or_postsmparityfrontier_audit.py",
    "selected_postsmparity_workbreakdown_labels_audit.py",
    # Live frontier: dynamic payload handoff, qutrit-Weyl carrier, and supersession check.
    "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap_audit.py",
    "selected_hrgconsumervaluesource_or_largethresholdtransportmap_audit.py",
    "selected_qutritweylcarriertheorem_or_hymoverlapvaluesourcegate_audit.py",
    "frontier_supersession_check_2026_07_04_audit.py",
    "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging_audit.py",
    "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows_audit.py",
    "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate_audit.py",
    "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt_audit.py",
    "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem_audit.py",
    "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill_audit.py",
    "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap_audit.py",
    "selected_rovaluesource_or_nonhiggsmapexecution_audit.py",
    "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector_audit.py",
    "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem_audit.py",
    "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap_audit.py",
    "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem_audit.py",
    "selected_strictrhrgsourceconstruction_or_independentvalidationoracle_audit.py",
    "selected_rhrgdeterminantindexcandidate_or_externalvalidationtarget_audit.py",
    "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun_audit.py",
    "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum_audit.py",
    "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution_audit.py",
    "selected_hresponsevaluesourcefunctional_or_directherm2rows_audit.py",
    "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun_audit.py",
    "selected_hradialscalephasesource_or_herm2hessianrows_audit.py",
    "selected_herm2polarsourcecompletion_or_hresponserows_audit.py",
    "selected_herm2orientationphasetracesource_or_directhresponseemission_audit.py",
    "selected_nondiagonalhuvhessiansource_or_directherm2rows_audit.py",
    "selected_fhuvsecondvariationsource_or_directherm2rowpayload_audit.py",
    "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution_audit.py",
    "selected_c1tobhuvprojectiontensor_or_fhuvrows_audit.py",
    "selected_higgsc1variationslotextension_or_ambienthessianrows_audit.py",
    "selected_ehuvc1variationoperators_or_ambienthessianrestrictionrows_audit.py",
    "selected_hsectordynamicc1extension_or_directhuvrows_audit.py",
    "selected_msourcehuvoperator_or_directherm2rows_audit.py",
    "selected_hresponsetablevaluerows_or_directherm2valuerows_audit.py",
    "selected_hresponserowsourceemission_or_directherm2certificatepayload_audit.py",
    "selected_huvprimitiveformula_or_finiteerrorboundexecution_audit.py",
    "selected_finitehfunctional_or_msourcevalueemission_audit.py",
    "selected_hradialphasetracesource_or_finitehactionemission_audit.py",
    "selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows_audit.py",
    "selected_hpolarfieldpromotion_or_finitehactionderivation_audit.py",
    "selected_hrgvaluemapforh_or_complexrotatedhphasecertificate_audit.py",
    "selected_hphasesignselector_lenscircle_or_hrgvaluemap_audit.py",
    "selected_hrgradialnormlaw_or_value_source_derivation_audit.py",
    "selected_hradialactionnormvalue_or_hlambdathresholdrow_audit.py",
    "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue_audit.py",
    "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun_audit.py",
    "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution_audit.py",
    "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem_audit.py",
    "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows_audit.py",
    "selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution_audit.py",
    "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision_audit.py",
    "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport_audit.py",
    "selected_combinedthresholdkernelkrows_sourcetheorem_audit.py",
    "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport_audit.py",
    "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport_audit.py",
    "selected_dynamicretardedoverlapderivativerows_or_tschemelambdahsourceexecution_audit.py",
    "selected_rowwisescalarretardedoverlapquadraturevalues_or_tschemelambdahsourceexecution_audit.py",
    "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure_audit.py",
    "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload_audit.py",
    "selected_thresholddeltarows_or_lambdahpayloadexecution_audit.py",
    "selected_lambdahpayloadexecution_or_tenkthresholdclosure_audit.py",
    "selected_hsectorquarticthresholdpayload_or_stricttenkclosure_audit.py",
    "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem_audit.py",
    "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows_audit.py",
    "selected_hradialthresholdscalarsource_or_tenkclosure_audit.py",
    "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure_audit.py",
    "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem_audit.py",
    "selected_hthresholdrgoperator_or_universalprimitivepolicy_audit.py",
    "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun_audit.py",
    "selected_hthresholdcyclebreakcutset_or_tenthkrowfrontier_audit.py",
    "selected_tenthhthresholdkrowsource_or_largethresholdrgprimitivetheorem_audit.py",
    "selected_hkthresholdsourceobject_or_rghessiantransportconstruction_audit.py",
    "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow_audit.py",
    "selected_heteroticstromingersourceoperatortorsion_or_directhkrow_audit.py",
    "selected_projectiverhoesmoothoperatorsourcevalues_or_directhkrow_audit.py",
    "selected_smoothdomaincoverorcomplementkernelsourceleaf_or_directhkrow_audit.py",
    "selected_coverhomotopy_or_smootheqasourcecertificate_or_physicalgaugeanchor_audit.py",
    "selected_flattorsionsmoothpromotion_or_selectedbundleabn27source_or_physicalomega0_audit.py",
    "selected_bn27connectionsourcevalues_or_physicalalphaactionunitdeterminanttable_or_directhkrow_audit.py",
    "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow_audit.py",
    "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow_audit.py",
    "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow_audit.py",
    "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow_audit.py",
    "selected_heteroticstromingersourceoperator_or_localsystemtorsion_or_fullfourierorbit_or_directhkrow_audit.py",
    "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow_audit.py",
    "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow_audit.py",
    "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow_audit.py",
    "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow_audit.py",
    "selected_samesourceconnectionvaluetable_or_directhkrow_audit.py",
    "selected_directhkthresholdrow_currentexit_or_radialsource_audit.py",
    "selected_hradialsourcevalue_or_directnhexecution_audit.py",
    "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse_audit.py",
    "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction_audit.py",
    "selected_honeparameterexecutionledger_or_strictfinitehsourcerows_audit.py",
    "selected_strictfinitehsourcerowconstruction_or_nonhiggshrgprediction_audit.py",
    "selected_qutrit27numericalpush_or_matrixrowfrontier_audit.py",
    "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier_audit.py",
    "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier_audit.py",
    "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier_audit.py",
    "selected_hradialtransportmap_or_dynamicphifinc1consumer_audit.py",
    "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer_audit.py",
    "selected_tauhc1scalarexport_or_galerkinmetricfrontier_audit.py",
    "selected_hangularc1metricsearch_or_hweightedgalerkinpayload_audit.py",
    "selected_hymmetricmomenttauhsearch_or_finitepartexport_audit.py",
    "selected_hweightedfinitepartcoefficientsearch_or_meshwindownogo_audit.py",
    "selected_bergmanhymcoefficient_or_heatzetaradialoperator_dualattempt_audit.py",
    "selected_bergmanhymdenominator7_or_exactnessobstruction_audit.py",
    "selected_bergmanhymnextcorrection_or_exactradialoperator_supersetattempt_audit.py",
    "selected_finitecutoffexactnessroutes_or_projectedsourceprinciple_audit.py",
    "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof_audit.py",
    "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule_audit.py",
    "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit_audit.py",
    "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit_audit.py",
    "selected_aewsourceoperator_or_thresholdconventionrows_audit.py",
    "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda_audit.py",
    "selected_samebranchgaugeactionsource_or_oneprimitivepolicy_audit.py",
    "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade_audit.py",
    "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit_audit.py",
    "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem_audit.py",
    "selected_strictpewsourcetheorem_or_smprecisionclosurecutset_audit.py",
    "selected_strictpewdirectkrowemissionattempt_or_gaugeactionnormalizationsource_audit.py",
    "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload_audit.py",
    "selected_firstpewgaugeactionnormalizationvalue_or_directkcertificaterun_audit.py",
    "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun_audit.py",
    "selected_physicalnormalizationsourceaxiom_or_directkcertificate_audit.py",
    "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade_audit.py",
    "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource_audit.py",
    "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation_audit.py",
    "selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill_audit.py",
    "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient_audit.py",
    "selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues_audit.py",
    "selected_firstsamesourceconnectionfieldemission_or_directhkrow_audit.py",
    "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate_audit.py",
    "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables_audit.py",
    "selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill_audit.py",
    "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution_audit.py",
    "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables_audit.py",
    "selected_qasu3_selectedmonaddevalues_or_bn27strictsourcetheorem_audit.py",
    "selected_primitivemonadvalueselector_theorem_or_fulldeoperatorvalues_audit.py",
    "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues_audit.py",
    "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables_audit.py",
    "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart_audit.py",
    "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity_audit.py",
    "selected_sourceemissionstatementpromotion_after_anpolicy_audit.py",
    "selected_routecinternality_splitownership_or_samebranchidentity_audit.py",
    "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject_audit.py",
    "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject_audit.py",
    "selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym_audit.py",
    "selected_geometric_cechhym_obligation_reduction_after_onepremise_audit.py",
    "selected_cech_ah_representative_or_hymende_values_audit.py",
    "selected_hymende_operatorsector_cutset_after_ahlane_audit.py",
    "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard_audit.py",
    "selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues_audit.py",
    "selected_fullsector_bn27_hymende_validator_payload_audit.py",
    "selected_hym_projector_sourcepromotion_or_fullstrominger_operator_value_audit.py",
    "selected_routec_strominger_sourceflags_or_samesource_visibleoperator_audit.py",
    "selected_fullsector_visible_offdiag_source_or_bn27finalrow_audit.py",
    "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance_audit.py",
    "selected_strictglobalcechhym_or_truesmafterah8_audit.py",
    "selected_literalwitness_or_precisionvalues_afterah8_audit.py",
    "selected_internalvaluerows_afterah8_or_literalglobalwitness_audit.py",
    "selected_magnitudebearingrows_after_postah8_dynamicimport_audit.py",
    "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge_audit.py",
    "selected_heavylinkvectors_after_policybridge_or_ckmlaw_audit.py",
    "selected_heavylinkvaluesource_search_or_ckmanglelaw_audit.py",
    "selected_sectortransportselectionlemma_su5qutritheavylink_audit.py",
    "selected_ckmanglelaw_fromselectedheavylinks_or_flavorobservablereplay_audit.py",
    "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution_audit.py",
    "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure_audit.py",
    "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution_audit.py",
    "selected_ckmsectorpairweightsourcetheorem_or_fullflavorgalerkinrun_audit.py",
    "selected_ckmweightscalarevaluator_or_selectedflavorgalerkinvalues_audit.py",
    "selected_zeromodegramsectorcontractionpayload_or_eckmweightrows_audit.py",
    "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution_audit.py",
    "selected_eckmweightrowcertificates_or_ckmangleclosuredecision_audit.py",
    "selected_kckmtraceassemblyrule_or_oneprincipleckmclosure_audit.py",
    "selected_pickmclosurecosttracefunctional_or_angleweightrows_audit.py",
    "selected_pickmsourcederivationclauses_or_ckmpredictionupgrade_audit.py",
    "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates_audit.py",
    "selected_pickmnumeratorbranchretentionprinciple_or_weightrows_audit.py",
    "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure_audit.py",
    "selected_qutrit27matrixminimalclosure_or_strictpewupgrade_audit.py",
    "selected_qcdthetapolicy_or_strictpewcountreduction_audit.py",
    "selected_neutrinomassmajoranapolicy_or_precisionprofiletable_audit.py",
    "selected_precisionprofiletable_or_truesmequivalenceaudit_audit.py",
    "selected_qasu3operatorpayload_or_strictpewprecisionexit_audit.py",
    "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows_audit.py",
    "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit_audit.py",
    "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap_audit.py",
    "selected_spectralyukawaresponsebasis_or_coefficientsourcewall_audit.py",
    "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger_audit.py",
    "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem_audit.py",
    "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy_audit.py",
    "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption_audit.py",
    "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge_audit.py",
    "selected_yukawageometryadaptedbasiscompression_or_nineslotwall_audit.py",
    "selected_phaselanecurvatureclue_or_yukawareductiondiagnostic_audit.py",
    "selected_phaselanecurvaturesourcerelation_or_sevenparameteryukawareduction_audit.py",
    "selected_phaselanecurvatureresidualexactness_or_sourcecorrectionrows_audit.py",
    "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula_audit.py",
    "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure_audit.py",
    "selected_yukawaboundederrorcertificate_or_residualoperatorfrontier_audit.py",
    "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure_audit.py",
    "selected_phaseantisymmetrycurvaturescalarsource_or_finalyukawamagnitudeclosure_audit.py",
    "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness_audit.py",
    "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_audit.py",
    "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows_audit.py",
    "selected_strictpewdirectk_or_qasu3step10valueexecution_audit.py",
    "selected_fulls2noproxyrows_or_strictpewnormalizationpayload_audit.py",
    "selected_ckmpmnsrows_or_higgsthresholdstrictpewexit_audit.py",
    "selected_ckmcovarianceprofileorhigherorderresidualclosure_or_pmnshiggspewrows_audit.py",
    "selected_pmnsrunningmassrows_or_higgsthresholdstrictpewexit_audit.py",
    "selected_higgsthresholdstrictpewexit_or_selectedsourcerows_audit.py",
    "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit_audit.py",
    "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision_audit.py",
    "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram_audit.py",
    "selected_corpuspaperrevisionpacket_or_strictnoknobupgradeexecution_audit.py",
    "selected_latestah8pickmfrontier_or_nextstrictclosuretargets_audit.py",
    "selected_massratioorientationlawsearch_or_finitephaseckmclue_audit.py",
    "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget_audit.py",
    "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem_audit.py",
    "selected_commoncirclebundlecskfunctional_or_phiflavornrefinement_audit.py",
    "selected_commoncirclesectorresponseexecution_or_csktracerows_audit.py",
    "selected_phisectornsourcevalues_or_noknobcskrows_audit.py",
    "selected_sectorresponsedensitysource_or_noknobcskrowemission_audit.py",
    "selected_fulls2sectordensityoperator_or_phisectornnumericrows_audit.py",
    "selected_deltas2densitycorrectionsource_or_strictcskrows_audit.py",
    "selected_fullsectorhymoperatorpayload_or_deltas2rowemission_audit.py",
    "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade_audit.py",
    "selected_activeledger_dotdc1supersession_or_valuelayerfrontier_audit.py",
    "selected_corpusflavorcoefficienttheorem_scan_or_rthetaprovenancefrontier_audit.py",
    "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure_audit.py",
    "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission_audit.py",
    "selected_rtheta_sectortransferbnbasis_or_pikernelclosure_audit.py",
    "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure_audit.py",
    "selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem_audit.py",
    "selected_rtheta_primitivec1overlap_or_pinoneedtheorem_audit.py",
    "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_audit.py",
    "selected_rtheta_thresholdrows_or_profileconventionsourceclosure_audit.py",
    "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest_audit.py",
    "selected_thresholdmatchingrowspostpi_or_massschemesourcerows_audit.py",
    "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation_audit.py",
    "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy_audit.py",
    "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport_audit.py",
    "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission_audit.py",
    "selected_lockedbasefreeze_or_pewdirectkattackcontract_audit.py",
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


def certificate_status() -> str:
    names = [
        "sm_parity_closure_ledger_certificate.json",
        "core_axioms_measured_parameter_interface_certificate.json",
        "sm_equivalence_superset_strategy_controller_certificate.json",
        "selected_smparityfrozenboundary_or_postsmparityfrontier_certificate.json",
        "selected_postsmparity_workbreakdown_labels_certificate.json",
        "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap_certificate.json",
        "selected_hrgconsumervaluesource_or_largethresholdtransportmap_certificate.json",
        "selected_qutritweylcarriertheorem_or_hymoverlapvaluesourcegate_certificate.json",
        "frontier_supersession_check_2026_07_04_certificate.json",
        "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging_certificate.json",
        "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows_certificate.json",
        "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate_certificate.json",
        "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt_certificate.json",
        "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem_certificate.json",
        "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill_certificate.json",
        "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap_certificate.json",
        "selected_rovaluesource_or_nonhiggsmapexecution_certificate.json",
        "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector_certificate.json",
        "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem_certificate.json",
        "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap_certificate.json",
        "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem_certificate.json",
        "selected_strictrhrgsourceconstruction_or_independentvalidationoracle_certificate.json",
        "selected_rhrgdeterminantindexcandidate_or_externalvalidationtarget_certificate.json",
        "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun_certificate.json",
        "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum_certificate.json",
        "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution_certificate.json",
        "selected_hresponsevaluesourcefunctional_or_directherm2rows_certificate.json",
        "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun_certificate.json",
        "selected_hradialscalephasesource_or_herm2hessianrows_certificate.json",
        "selected_herm2polarsourcecompletion_or_hresponserows_certificate.json",
        "selected_herm2orientationphasetracesource_or_directhresponseemission_certificate.json",
        "selected_nondiagonalhuvhessiansource_or_directherm2rows_certificate.json",
        "selected_fhuvsecondvariationsource_or_directherm2rowpayload_certificate.json",
        "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution_certificate.json",
        "selected_c1tobhuvprojectiontensor_or_fhuvrows_certificate.json",
        "selected_higgsc1variationslotextension_or_ambienthessianrows_certificate.json",
        "selected_ehuvc1variationoperators_or_ambienthessianrestrictionrows_certificate.json",
        "selected_hsectordynamicc1extension_or_directhuvrows_certificate.json",
        "selected_msourcehuvoperator_or_directherm2rows_certificate.json",
        "selected_hresponsetablevaluerows_or_directherm2valuerows_certificate.json",
        "selected_hresponserowsourceemission_or_directherm2certificatepayload_certificate.json",
        "selected_huvprimitiveformula_or_finiteerrorboundexecution_certificate.json",
        "selected_finitehfunctional_or_msourcevalueemission_certificate.json",
        "selected_hradialphasetracesource_or_finitehactionemission_certificate.json",
        "selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows_certificate.json",
        "selected_hpolarfieldpromotion_or_finitehactionderivation_certificate.json",
        "selected_hrgvaluemapforh_or_complexrotatedhphasecertificate_certificate.json",
        "selected_hphasesignselector_lenscircle_or_hrgvaluemap_certificate.json",
        "selected_hrgradialnormlaw_or_value_source_derivation_certificate.json",
        "selected_hradialactionnormvalue_or_hlambdathresholdrow_certificate.json",
        "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue_certificate.json",
        "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun_certificate.json",
        "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution_certificate.json",
        "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem_certificate.json",
        "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows_certificate.json",
        "selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution_certificate.json",
        "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision_certificate.json",
        "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport_certificate.json",
        "selected_combinedthresholdkernelkrows_sourcetheorem_certificate.json",
        "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport_certificate.json",
        "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport_certificate.json",
        "selected_dynamicretardedoverlapderivativerows_or_tschemelambdahsourceexecution_certificate.json",
        "selected_rowwisescalarretardedoverlapquadraturevalues_or_tschemelambdahsourceexecution_certificate.json",
        "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure_certificate.json",
        "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload_certificate.json",
        "selected_thresholddeltarows_or_lambdahpayloadexecution_certificate.json",
        "selected_lambdahpayloadexecution_or_tenkthresholdclosure_certificate.json",
        "selected_hsectorquarticthresholdpayload_or_stricttenkclosure_certificate.json",
        "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem_certificate.json",
        "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows_certificate.json",
        "selected_hradialthresholdscalarsource_or_tenkclosure_certificate.json",
        "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure_certificate.json",
        "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem_certificate.json",
        "selected_hthresholdrgoperator_or_universalprimitivepolicy_certificate.json",
        "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun_certificate.json",
        "selected_hthresholdcyclebreakcutset_or_tenthkrowfrontier_certificate.json",
        "selected_tenthhthresholdkrowsource_or_largethresholdrgprimitivetheorem_certificate.json",
        "selected_hkthresholdsourceobject_or_rghessiantransportconstruction_certificate.json",
        "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow_certificate.json",
        "selected_heteroticstromingersourceoperatortorsion_or_directhkrow_certificate.json",
        "selected_projectiverhoesmoothoperatorsourcevalues_or_directhkrow_certificate.json",
        "selected_smoothdomaincoverorcomplementkernelsourceleaf_or_directhkrow_certificate.json",
        "selected_coverhomotopy_or_smootheqasourcecertificate_or_physicalgaugeanchor_certificate.json",
        "selected_flattorsionsmoothpromotion_or_selectedbundleabn27source_or_physicalomega0_certificate.json",
        "selected_bn27connectionsourcevalues_or_physicalalphaactionunitdeterminanttable_or_directhkrow_certificate.json",
        "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow_certificate.json",
        "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow_certificate.json",
        "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow_certificate.json",
        "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow_certificate.json",
        "selected_heteroticstromingersourceoperator_or_localsystemtorsion_or_fullfourierorbit_or_directhkrow_certificate.json",
        "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow_certificate.json",
        "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow_certificate.json",
        "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow_certificate.json",
        "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow_certificate.json",
        "selected_samesourceconnectionvaluetable_or_directhkrow_certificate.json",
        "selected_directhkthresholdrow_currentexit_or_radialsource_certificate.json",
        "selected_hradialsourcevalue_or_directnhexecution_certificate.json",
        "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse_certificate.json",
        "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction_certificate.json",
        "selected_honeparameterexecutionledger_or_strictfinitehsourcerows_certificate.json",
        "selected_strictfinitehsourcerowconstruction_or_nonhiggshrgprediction_certificate.json",
        "selected_qutrit27numericalpush_or_matrixrowfrontier_certificate.json",
        "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier_certificate.json",
        "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier_certificate.json",
        "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier_certificate.json",
        "selected_hradialtransportmap_or_dynamicphifinc1consumer_certificate.json",
        "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer_certificate.json",
        "selected_tauhc1scalarexport_or_galerkinmetricfrontier_certificate.json",
        "selected_hangularc1metricsearch_or_hweightedgalerkinpayload_certificate.json",
        "selected_hymmetricmomenttauhsearch_or_finitepartexport_certificate.json",
        "selected_hweightedfinitepartcoefficientsearch_or_meshwindownogo_certificate.json",
        "selected_bergmanhymcoefficient_or_heatzetaradialoperator_dualattempt_certificate.json",
        "selected_bergmanhymdenominator7_or_exactnessobstruction_certificate.json",
        "selected_bergmanhymnextcorrection_or_exactradialoperator_supersetattempt_certificate.json",
        "selected_finitecutoffexactnessroutes_or_projectedsourceprinciple_certificate.json",
        "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof_certificate.json",
        "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule_certificate.json",
        "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit_certificate.json",
        "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit_certificate.json",
        "selected_aewsourceoperator_or_thresholdconventionrows_certificate.json",
        "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda_certificate.json",
        "selected_samebranchgaugeactionsource_or_oneprimitivepolicy_certificate.json",
        "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade_certificate.json",
        "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit_certificate.json",
        "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem_certificate.json",
        "selected_strictpewsourcetheorem_or_smprecisionclosurecutset_certificate.json",
        "selected_strictpewdirectkrowemissionattempt_or_gaugeactionnormalizationsource_certificate.json",
        "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload_certificate.json",
        "selected_firstpewgaugeactionnormalizationvalue_or_directkcertificaterun_certificate.json",
        "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun_certificate.json",
        "selected_physicalnormalizationsourceaxiom_or_directkcertificate_certificate.json",
        "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade_certificate.json",
        "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource_certificate.json",
        "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation_certificate.json",
        "selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill_certificate.json",
        "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient_certificate.json",
        "selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues_certificate.json",
        "selected_firstsamesourceconnectionfieldemission_or_directhkrow_certificate.json",
        "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate_certificate.json",
        "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables_certificate.json",
        "selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill_certificate.json",
        "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution_certificate.json",
        "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables_certificate.json",
        "selected_qasu3_selectedmonaddevalues_or_bn27strictsourcetheorem_certificate.json",
        "selected_primitivemonadvalueselector_theorem_or_fulldeoperatorvalues_certificate.json",
        "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues_certificate.json",
        "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables_certificate.json",
        "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart_certificate.json",
        "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity_certificate.json",
        "selected_sourceemissionstatementpromotion_after_anpolicy_certificate.json",
        "selected_routecinternality_splitownership_or_samebranchidentity_certificate.json",
        "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject_certificate.json",
        "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject_certificate.json",
        "selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym_certificate.json",
        "selected_geometric_cechhym_obligation_reduction_after_onepremise_certificate.json",
        "selected_cech_ah_representative_or_hymende_values_certificate.json",
        "selected_hymende_operatorsector_cutset_after_ahlane_certificate.json",
        "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard_certificate.json",
        "selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues_certificate.json",
        "selected_fullsector_bn27_hymende_validator_payload_certificate.json",
        "selected_hym_projector_sourcepromotion_or_fullstrominger_operator_value_certificate.json",
        "selected_routec_strominger_sourceflags_or_samesource_visibleoperator_certificate.json",
        "selected_fullsector_visible_offdiag_source_or_bn27finalrow_certificate.json",
        "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance_certificate.json",
        "selected_strictglobalcechhym_or_truesmafterah8_certificate.json",
        "selected_literalwitness_or_precisionvalues_afterah8_certificate.json",
        "selected_internalvaluerows_afterah8_or_literalglobalwitness_certificate.json",
        "selected_magnitudebearingrows_after_postah8_dynamicimport_certificate.json",
        "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge_certificate.json",
        "selected_heavylinkvectors_after_policybridge_or_ckmlaw_certificate.json",
        "selected_heavylinkvaluesource_search_or_ckmanglelaw_certificate.json",
        "selected_sectortransportselectionlemma_su5qutritheavylink_certificate.json",
        "selected_ckmanglelaw_fromselectedheavylinks_or_flavorobservablereplay_certificate.json",
        "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution_certificate.json",
        "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure_certificate.json",
        "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution_certificate.json",
        "selected_ckmsectorpairweightsourcetheorem_or_fullflavorgalerkinrun_certificate.json",
        "selected_ckmweightscalarevaluator_or_selectedflavorgalerkinvalues_certificate.json",
        "selected_zeromodegramsectorcontractionpayload_or_eckmweightrows_certificate.json",
        "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution_certificate.json",
        "selected_eckmweightrowcertificates_or_ckmangleclosuredecision_certificate.json",
        "selected_kckmtraceassemblyrule_or_oneprincipleckmclosure_certificate.json",
        "selected_pickmclosurecosttracefunctional_or_angleweightrows_certificate.json",
        "selected_pickmsourcederivationclauses_or_ckmpredictionupgrade_certificate.json",
        "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates_certificate.json",
        "selected_pickmnumeratorbranchretentionprinciple_or_weightrows_certificate.json",
        "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure_certificate.json",
        "selected_qutrit27matrixminimalclosure_or_strictpewupgrade_certificate.json",
        "selected_qcdthetapolicy_or_strictpewcountreduction_certificate.json",
        "selected_neutrinomassmajoranapolicy_or_precisionprofiletable_certificate.json",
        "selected_precisionprofiletable_or_truesmequivalenceaudit_certificate.json",
        "selected_qasu3operatorpayload_or_strictpewprecisionexit_certificate.json",
        "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows_certificate.json",
        "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit_certificate.json",
        "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap_certificate.json",
        "selected_spectralyukawaresponsebasis_or_coefficientsourcewall_certificate.json",
        "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger_certificate.json",
        "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem_certificate.json",
        "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy_certificate.json",
        "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption_certificate.json",
        "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge_certificate.json",
        "selected_yukawageometryadaptedbasiscompression_or_nineslotwall_certificate.json",
        "selected_phaselanecurvatureclue_or_yukawareductiondiagnostic_certificate.json",
        "selected_phaselanecurvaturesourcerelation_or_sevenparameteryukawareduction_certificate.json",
        "selected_phaselanecurvatureresidualexactness_or_sourcecorrectionrows_certificate.json",
        "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula_certificate.json",
        "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure_certificate.json",
        "selected_yukawaboundederrorcertificate_or_residualoperatorfrontier_certificate.json",
        "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure_certificate.json",
        "selected_phaseantisymmetrycurvaturescalarsource_or_finalyukawamagnitudeclosure_certificate.json",
        "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness_certificate.json",
        "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_certificate.json",
        "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows_certificate.json",
        "selected_strictpewdirectk_or_qasu3step10valueexecution_certificate.json",
        "selected_fulls2noproxyrows_or_strictpewnormalizationpayload_certificate.json",
        "selected_ckmpmnsrows_or_higgsthresholdstrictpewexit_certificate.json",
        "selected_ckmcovarianceprofileorhigherorderresidualclosure_or_pmnshiggspewrows_certificate.json",
        "selected_pmnsrunningmassrows_or_higgsthresholdstrictpewexit_certificate.json",
        "selected_higgsthresholdstrictpewexit_or_selectedsourcerows_certificate.json",
        "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit_certificate.json",
        "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision_certificate.json",
        "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram_certificate.json",
        "selected_corpuspaperrevisionpacket_or_strictnoknobupgradeexecution_certificate.json",
        "selected_latestah8pickmfrontier_or_nextstrictclosuretargets_certificate.json",
        "selected_massratioorientationlawsearch_or_finitephaseckmclue_certificate.json",
        "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget_certificate.json",
        "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem_certificate.json",
        "selected_commoncirclebundlecskfunctional_or_phiflavornrefinement_certificate.json",
        "selected_commoncirclesectorresponseexecution_or_csktracerows_certificate.json",
        "selected_phisectornsourcevalues_or_noknobcskrows_certificate.json",
        "selected_sectorresponsedensitysource_or_noknobcskrowemission_certificate.json",
        "selected_fulls2sectordensityoperator_or_phisectornnumericrows_certificate.json",
        "selected_deltas2densitycorrectionsource_or_strictcskrows_certificate.json",
        "selected_fullsectorhymoperatorpayload_or_deltas2rowemission_certificate.json",
        "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade_certificate.json",
        "selected_activeledger_dotdc1supersession_or_valuelayerfrontier_certificate.json",
        "selected_corpusflavorcoefficienttheorem_scan_or_rthetaprovenancefrontier_certificate.json",
        "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure_certificate.json",
        "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission_certificate.json",
        "selected_rtheta_sectortransferbnbasis_or_pikernelclosure_certificate.json",
        "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure_certificate.json",
        "selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem_certificate.json",
        "selected_rtheta_primitivec1overlap_or_pinoneedtheorem_certificate.json",
        "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_certificate.json",
        "selected_rtheta_thresholdrows_or_profileconventionsourceclosure_certificate.json",
        "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest_certificate.json",
        "selected_thresholdmatchingrowspostpi_or_massschemerows_certificate.json",
        "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation_certificate.json",
        "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy_certificate.json",
        "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport_certificate.json",
        "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission_certificate.json",
        "selected_lockedbasefreeze_or_pewdirectkattackcontract_certificate.json",
    ]
    lines = ["Certificate frontier status", "---------------------------"]
    for name in names:
        path = CERTS / name
        if not path.exists():
            lines.append(f"{name}: MISSING")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        lines.append(f"{name}: {data.get('status', 'UNKNOWN')}")
    lines.append("")
    lines.append(f"Frozen full verifier: {FROZEN_FULL}")
    lines.append("Run `python scripts\\verify.py --full` for the archived full-chain replay.")
    return "\n".join(lines)


def run_full() -> int:
    if not FROZEN_FULL.exists():
        print(f"Missing frozen full verifier: {FROZEN_FULL}")
        return 1
    proc = subprocess.run(
        [sys.executable, str(FROZEN_FULL)],
        cwd=ROOT,
        text=True,
        stdout=sys.stdout,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode


def main(argv: list[str]) -> int:
    if "--full" in argv:
        return run_full()

    parts = [
        "MTT fast frontier verification report",
        "=====================================",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Corpus: {CORPUS}",
        "",
        "Scope: stable guardrails plus live frontier/supersession checks. Use --full for the 2026-07-04 frozen replay.",
        "Frozen replay is at scripts/verify_full_frozen_2026_07_04.py.",
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
            "Fast frontier checks passed. Current frontier is "
            "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_"
            "TSchemeLambdaHExecution_v1. The locked-base contract freezes the "
            "27x27 qutrit-Weyl matrix package, AH-equivalent BN27 lane, Pi_CKM "
            "rows, CKM diagonal-profile admission, finite-replay charged-Yukawa "
            "magnitude rows, and one-shared-physical-primitive standard as "
            "consumed results. The live strict upgrade is PEW/direct-K: derive "
            "P_EW from same-branch source data or emit direct "
            "K_threshold.Omega_H.lambda from selected rowwise scalar "
            "retarded-overlap / T-scheme / lambda_H payload rows. Current "
            "strict P_EW/direct-K rows remain 0. "
            "The selected qutrit-Weyl carrier/HYM gate is promoted, the 2026-07-04 "
            "supersession check is machine-audited, and the finite 27x27 qutrit "
            "spectral package plus nine charged normalized HYM/Strominger overlap "
            "kernel rows are now audited. The H/lambda wall is tier-separated: "
            "strict no-knob remains 9/10, while the controlled one-parameter "
            "H layer is parameterized 10/10 with lambda_H as calibration, not "
            "prediction. HRG cross-use has been validated internally with exact "
            "dynamic-C1 residuals, and the strict R_H^RG/oracle packet now proves "
            "that those rows do not constitute independent validation: strict source "
            "count remains 0 and independent validation rank is 0. The determinant/index "
            "candidate matrix binds the latest Higgs projection data and selected s_beta "
            "to the R_H^RG contract, but accepts 0 strict determinant/index candidates. "
            "The H-sector determinant/RG operator contract is now defined on the selected "
            "B_Huv/P_H domain. The static H-sector heat logdet is imported as support "
            "with value 43.802475498298655, but it is not promoted to the dynamic "
            "R_H^RG value source. The H-response source-row packet fixes the minimal "
            "direct Herm(2) row/certificate table and executes it with 0 emitted rows; "
            "the H-response value-source functional contract is now closed and all "
            "current F_H, direct Herm(2), M_source, and C5/C6 lanes have been "
            "rechecked with 0 accepted value-source routes. The first finite H "
            "functional/direct Herm(2) emission run is now executed: selected s_beta "
            "and the radial-collapse reduction are retained. The H radial/phase "
            "packet now splits strict radial source into A_EW/RG, intrinsic H quartic "
            "K, or strict R_H^RG routes, separates the controlled HRG calibration "
            "lane, and closes the Herm(2) polar reconstruction law. The trace-free "
            "Herm(2) polar contract is now closed and m0 is retired only for the "
            "trace-free threshold block; static/dynamic matter-orientation packets "
            "are rechecked and rejected as Higgs Omega phase sources. The C1-C6 "
            "projection bridge is now retired as an s_beta/projection blocker, but "
            "is explicitly not a direct Herm(2) Huv value source; direct H-response "
            "emission still has 0 accepted rows. The non-diagonal Huv source "
            "contract is now closed: a source can enter only by selected F_H "
            "second variation, selected M_source+R_H values, or direct certified "
            "Herm(2) rows. Diagonal HYM, projection C1-C6, matter same-source "
            "blocks, full-route formula-only support, direct-row replay, and the "
            "polar reconstruction law were all rechecked with 0 accepted "
            "non-diagonal Huv sources. The F_Huv restriction criterion is now "
            "closed: F_Huv(z)=F_C1(B_Huv z) and "
            "M_Huv=B_Huv^*Hess(F_C1)_selectedB_Huv on the selected two-Higgs "
            "domain. The local C1/Weyl premise bridge is kept separate from "
            "strict no-knob closure, and the row execution still emits 0 F_Huv "
            "or direct Herm(2) rows. The F_Huv projection attempt now imports "
            "the strict dynamic C1 payload: A^T A=12 I_2, A^T b=(12,12), "
            "and b_selected is source-promoted in the active ledger. But this "
            "is a compressed C1 normal matrix, not the ambient 27x27 "
            "Hess(F_C1) on B_Huv. The forbidden naive A^T A -> Huv promotion "
            "was tested and rejected because it is scalar with zero trace-free "
            "non-diagonal block. The next frontier is the source-owned "
            "C1-to-B_Huv projection tensor or ambient Hessian entries needed "
            "to execute B_Huv^*Hess(F_C1)_selectedB_Huv. The C1-to-B_Huv "
            "tensor contract is now closed and the current 72-slot C1 routing "
            "has been audited against the Higgs source IDs: it routes matter "
            "sectors u,d,e,nuD and contains 0 H_u/H_d^dagger Higgs slots. "
            "The Higgs C1 variation-slot extension and ambient Hessian-row "
            "contracts are now closed: the minimum legal T_C1<-E_H^UV object "
            "has four slots (H_u/H_d^dagger by phase_R_Z/shift_R_X), and once "
            "selected it would execute as M_Huv=12 T^*T because the active C1 "
            "normal matrix is 12 I_2. Current execution emits 0 selected Higgs "
            "C1 slots, 0 ambient Hessian restriction rows, and 0 F_Huv rows. "
            "The active dynamic Phi_fin/C1 source payload is now imported into "
            "the Higgs frontier: phase_R_Z and shift_R_X are selected 3x3 C1 "
            "source matrices, A^T A=12 I_2, and stale C1 source/Galerkin replay "
            "is retired for this branch. H7B1M remains valid after this update "
            "only as a target-mismatch theorem: the C1 target sectors are still "
            "u,d,e,nuD and contain 0 H/H_u/H_d^dagger codomain rows. Thus the "
            "remaining non-looping target is a selected H-sector dynamic C1 "
            "extension Eval_EHuv_C1 or direct source-owned Huv rows. H7B1N/Z "
            "have now been reconciled with the active repo: HYM-grid existence "
            "is retired as a blocker, and active C2/C3/B_Huv supersede older "
            "missing E_H^UV basis, metric-binding, and B_Huv clauses. The "
            "direct route now has the two-column source-orthonormal B_Huv lift "
            "available, but emits 0 M_source rows and 0 direct Huu/Hud/Hdd "
            "Herm(2) rows. The M_source contract is now reconciled with the "
            "active domain: M_source=sym(R_H^*H_responseR_H) and "
            "Huv=B_Huv^*M_sourceB_Huv. Active B_Huv/R_H/domain and Herm(2) "
            "row extractors are closed, while selected H_response rows, "
            "M_source entries, and direct Huu/Hud/Hdd rows all remain 0. "
            "The diagonal HYM metric was rechecked and remains kinematic "
            "support, not a Higgs mass/strain Hessian. The H_response table "
            "value-row and direct Herm(2) value-row interfaces have now been "
            "executed directly: the H_response side requires 7 rows/certificates "
            "and accepts 0, while the direct Herm(2) side requires 8 "
            "rows/certificates and accepts 0. Diagonal HYM, the compressed "
            "A^T A=12 I_2 C1 normal matrix, the polar law, static H logdet, "
            "controlled HRG/lambda calibration, and the selected s_beta "
            "projection bridge were rechecked as non-sources. Thus the next "
            "row-source/certificate layer has been fixed and split correctly: "
            "B_Huv supplies same-branch source IDs, source orthonormality, finite "
            "exactness support, and quotient support, and the Herm(2) codomain "
            "is closed, but these are not final row certificates. Required "
            "payload slots are 8, support slots available are 4, accepted final "
            "payload slots remain 0, accepted value rows remain 0, and accepted "
            "final certificates remain 0. The direct closure attack is now "
            "mathematically decided: the same B_Huv support admits distinct "
            "non-scalar Herm(2) completions, for example diag(1,-1) and "
            "[[0,1],[1,0]], which yield different Huu,Hud,Hdd rows. Thus "
            "B_Huv support cannot select the value rows. The next target is "
            "selected finite H-sector functional F_H, selected same-source "
            "Hermitian M_source values, or selected primitive H-response kernel "
            "K_H with row-level exactness/error bounds. That inventory has now "
            "been executed: strict F_H, M_source, and K_H routes accept 0 value "
            "rows. The selected s_beta polar angle is retained and reduces the "
            "row problem to r_H, sigma_D, phi_Omega, m0/quotient trace, and "
            "row certificates. The controlled HRG radial calibration remains "
            "useful minimal-parameter support, but is not promoted to strict "
            "no-knob source rows. The H radial/phase/trace source or finite-H "
            "action theorem now executes that narrowed target directly: selected "
            "s_beta is retained, controlled HRG radial support is recorded but "
            "not counted as a strict source, accepted strict polar fields remain "
            "0/4, accepted value rows remain 0, accepted row certificates remain "
            "0, and no selected finite-H action/second variation is emitted. "
            "The H polar-field numerical completion attempt now emits the smallest "
            "controlled Herm(2) candidate: r_H=391.39140285811936, sigma_D=+1, "
            "phi_Omega=pi/2, m0=0, Huu=26.835536563225222, "
            "Hud=i*390.47033716866446, and Hdd=-26.835536563225222. "
            "It is Hermitian, trace-free, non-scalar, and reconstructs selected "
            "s_beta exactly to roundoff, but strict no-knob row acceptance remains "
            "0 because the HRG radial value, T3 orientation, complex phase, and "
            "trace theorem are not yet promoted as same-source H row certificates. "
            "The first promotion attempt now succeeds for two of those fields: "
            "m0=0 is promoted for the trace-free Huv/threshold block, and "
            "sigma_D=+1 is promoted as the ordered B_Huv/T3 orientation convention. "
            "It also emits the exact controlled finite-H quadratic action whose "
            "second variation gives the controlled Herm(2) rows. Strict closure "
            "is therefore reduced to r_H and phi_Omega: derive/admit the HRG "
            "radial value from a typed same-source value map and promote the "
            "complex-rotated pi/2 phase from a selected c-twist period/finite "
            "quotient or direct Higgs-row phase theorem. The two-gate HRG/phase "
            "attack now keeps r_H strict-open: the typed HRG consumer map still "
            "has 0 strict source rows, and the expanded invariant scan found no "
            "accepted exact source identity. Its best diagnostic near miss is "
            "sqrt2*z448/phi with relative error about 4.47e-4 and is not "
            "promoted. The phase side partially promotes: complex-rotated "
            "c-twist support reduces phi_Omega from a continuous phase to the "
            "imaginary axis {+pi/2,-pi/2}. The lens-circle H phase-sign selector "
            "now promotes the +i branch in the selected q79/F,m=1 finite-Weyl "
            "orientation while retaining the q369/F*,m=2 antiunitary conjugate "
            "as the -i branch. This does not use the retired Lens-Nil numerical "
            "weight block. The strict frontier is reduced to the HRG radial "
            "value source or an independent selected finite-H radial action scale. "
            "The H radial norm-law packet now closes the meaning of that scalar: "
            "with s_beta, trace-free quotient, T3 orientation, and +i phase fixed, "
            "H_tf(r)=r[[sqrt(s_beta),i sqrt(1-s_beta)],[-i sqrt(1-s_beta),"
            "-sqrt(s_beta)]], and r_H=sqrt(Tr(H_tf^2)/2)=||H_tf||_F/sqrt(2). "
            "The numeric norm value is not emitted: typed HRG/R_H^RG, H/lambda "
            "K_threshold, and determinant/RG routes all still accept 0 value rows. "
            "The H radial action-norm value cutset now closes the exact payload "
            "contract: strict no-knob H scalar closure can enter only through "
            "selected N_H=Hess(F_H)[U_H,U_H] on the fixed unit ray, direct "
            "K_threshold.Omega_H.lambda, or the split pair "
            "L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda. Current "
            "execution still emits 0 accepted scalar value rows, and the "
            "controlled r_H=391.39140285811936 layer remains calibration-tier "
            "support only. The next packet must emit a numeric source or formal "
            "selected source operator, not another status-only restatement. "
            "That formal operator is now emitted: RO.q79F1.Omega_H.lambda is "
            "defined on the selected q79/F,m=1 27x27 qutrit carrier as "
            "P_H Pi0^perp G_E(delta_{Omega_H.lambda}D_E)Pi0^perp P_H, with "
            "the same Riesz/Green/projector normalization as the charged rows. "
            "The H-sector T_scheme slot is separated from the charged T_scheme=1 "
            "shortcut, and a direct radial Hessian alternative N_H=Hess(F_H)[U_H,U_H] "
            "is also contracted. Numeric Galerkin entries, H-sector scheme value, "
            "or direct N_H remain open; accepted H scalar value rows remain 0. "
            "The H-lambda finite Galerkin execution packet now backimports Step74: "
            "projector/sector/Pi/operator-domain blockers are retired for the active "
            "frontier, and all ten rows are operator-domain ready. The H row still "
            "emits 0 accepted L_rowlocal, T_scheme, lambda_H payload, Omega, or "
            "internal scalar rows; direct selected N_H also remains 0. The live "
            "target is therefore row-local threshold/value rows or lambda_H "
            "prefactor execution, not another domain-readiness proof. That target "
            "has now been executed through the row-local, quadrature, trace, "
            "anchor, internal/external, combined-K, threshold-delta, LambdaH, "
            "H-sector quartic, direct-H, radial D-term, EW-boundary/RG, intrinsic "
            "quartic, and H-threshold/RG policy packets. The non-looping result is "
            "strict 9/10 K-threshold closure: nine charged rows are selected by the "
            "source-native null-threshold identity, while the H/lambda row still "
            "has 0 accepted strict source payloads. The H-threshold cycle-break "
            "cutset is now audited: the next artifact must emit direct "
            "K_threshold.Omega_H.lambda, selected large-threshold/RG transport, "
            "or a universal primitive promoted by cross-use prediction. The "
            "cycle-break exits have now been executed: universal primitive promotion "
            "is rejected at the current source level because accepted non-Higgs "
            "cross-use targets remain 0, reducing the strict frontier to two "
            "source objects: direct K_threshold.Omega_H.lambda or selected "
            "large-threshold/RG transport. Path #2 has now imported the latest "
            "Qa/SU3 electroweak determinant chain: internal p_a, lambda_12, "
            "Delta_G12, same-scheme SU2/Qc, and the typed hypercharge threshold "
            "map are closed upstream. This retires the internal threshold and "
            "same-scheme SU2 blockers for the H RG route, but physical "
            "gauge/action normalization, mu_match, RG scheme, selected R_H^RG, "
            "and the Omega_H.lambda transport certificate remain open. The physical "
            "gauge/action layer now selects the heterotic/Strominger threshold-kernel "
            "route as the strict primary path and fills only the tree-level f=S slot; "
            "the value frontier is reduced to a source-selected HYM/monad Delta_A(mu) "
            "spectrum/finite part or a source-selected local-system torsion computation. "
            "The heterotic/Strominger source-operator torsion audit now contracts that "
            "branch further: the HYM invariant-block mu selector is refuted, the gerbe "
            "lane is partial support, and projective-rhoE finite internal quotient, "
            "operator payload, selected finite packet, and internal finite part are "
            "closed as support. Physical smooth operator source values, E_Qa or "
            "equivalent threshold finite response, threshold normalization, R_H^RG, "
            "and direct K_threshold.Omega_H.lambda remain open. The projective-rhoE "
            "smooth-value audit then contracts the first smooth leaf: finite "
            "representative-to-cocycle, finite character table, internal values, "
            "no-double-count policy, abstract Z3 shadow, and finite nerve scaffold "
            "are closed as support; what remains is selected smooth good-cover/domain "
            "data or a direct smooth complement-domain/kernel theorem, before smooth "
            "transition tables, E_Qa, physical normalization, or R_H^RG can close. "
            "The S1 source-leaf audit now builds the chart-atlas/Deligne-Cech "
            "equation packet, closes dH=0 and conditional local-potential support, "
            "locks the direct finite internal boundary and internal complement "
            "quotient, and imports oriented-PhiFin exact-table plus BN signed-operator "
            "support. The live exits are selected cover/homotopy local Cech values, "
            "smooth E_Qa/positive finite-part source certificate, physical gauge "
            "action anchor with mu_match and RG scheme, or direct H K-row emission. "
            "The cover/smooth-EQa/physical-anchor audit then contracts those exits: "
            "exact B=6 e5 wedge e6 with dB=H and formal Z3 flat-torsion transition "
            "support are closed but smooth transition functions are open; C_tau "
            "orientation and BN27 PhiFin table support are closed but selected bundle "
            "A/F_A or direct BN27 source ownership is open; physical matching is "
            "reduced to Omega0/K_phys plus the local determinant threshold vector "
            "and fixed matching/RG scheme. The flat-torsion/BN27/Omega0 audit then "
            "contracts the next layer: flat-torsion/projective transition validators "
            "and the direct finite internal rhoE operator payload are closed as "
            "support, BN27 validator dependencies reduce to either six source-emission "
            "statements or eight selected connection-table families, U1/Y Route-C "
            "promotes the finite D_E/Riesz/Green gap layer only as local support, "
            "and the physical route reduces to alpha_phys/action-unit plus a selected "
            "determinant/spectral table. Direct S_QaSU3^BN27 source ownership, "
            "selected connection values, A_selected/b_selected, lambda_12, physical "
            "Omega0/K_phys, local determinant table, and direct K_threshold.Omega_H.lambda "
            "remain open. The BN27-connection/determinant-table audit then executes "
            "that value layer: the BN27 side now has a minimal source-identity "
            "transport packet and probes all 11 source-object fields plus 8 "
            "connection-value fields, but fills 0 of each. The determinant side "
            "has log(2008) finite support, proves the U1/Y quotient determinant "
            "lemma with logdet 29.201650332199108, and constructs the concrete "
            "factorized A_base tensor I_3 quotient operator, but selected finitepart "
            "policy, determinant index weights, determinant scale, hypercharge/index "
            "weights, typed convention map, selected p_a/lambda_12, physical "
            "alpha/action-unit or Omega0/K_phys, and direct K_threshold.Omega_H.lambda "
            "remain open. The source-identity/finitepart-policy audit then closes "
            "the internal determinant side further: source-identity transport reduces "
            "to the single source_branch_identity leaf with operator co-emission and "
            "no-lift replay conditionally ready; internal finitepart policy, quotient "
            "index weights, and mu=1 determinant units promote p_a^int=29.201650332199108; "
            "the typed hypercharge convention map is structurally closed and records "
            "conditional lambda_12=2.6179362173268497 and Delta_G12=0.08450302790361214. "
            "These are not physical closure: BN27 source_branch_identity, Qa-stack p_a "
            "source emission or direct U1Y row promotion, physical gauge/action anchor, "
            "lambda_12, electroweak matching, and direct K_threshold.Omega_H.lambda "
            "remain open. The source-branch/Qa-stack physical-anchor audit then "
            "separates the two sides cleanly: the BN27 source_branch_identity leaf "
            "is attempted and current-source no-go is proved, with a repair packet "
            "for source amendment or same-source connection values; the Qa-stack "
            "side closes internal p_a, typed hypercharge, Qc/SU2 weak-split rows, "
            "same-scheme SU2 cancellation, internal lambda_12=2.6179362173268497, "
            "and internal Delta_G12=0.08450302790361214. Physical electroweak closure "
            "is now reduced to gauge/action normalization, mu_match, and RG/threshold "
            "scheme, while direct K_threshold.Omega_H.lambda remains the independent "
            "strict exit. The electroweak gauge-kinetic/RG and BN27 repair audit "
            "then selects the strict physical electroweak route as the "
            "B_flux/Strominger threshold kernel and retains the conditional interface "
            "1/g_Qa^2(mu_match)=K_gauge*log(2008), while leaving K_gauge, mu_match, "
            "and RG/threshold scheme open. In parallel, BN27 source-owned logdet "
            "promotion now has a conditional implication DAG and source amendment "
            "template, but still needs direct carrier/source theorem or selected "
            "connection export. Thus the active constructive frontier is selected "
            "heterotic/Strominger electroweak threshold kernel values, BN27 direct "
            "carrier/source theorem, or direct K_threshold.Omega_H.lambda. The "
            "Strominger-kernel/BN27-carrier audit then contracts the theorem/value "
            "targets: EW kernel values reduce to either a source-selected HYM/monad "
            "Laplace-type threshold operator finite part or a source-selected "
            "acyclic local-system torsion computation; BN27 direct carrier emission "
            "closes only the orientation functor from the 11-label rhoE shadow and "
            "proves that positive magnitude needs the full oriented positive Fourier "
            "orbit, since the shadow product 16 is short of the full 9600*9600 by "
            "multiplier 5760000. The source-operator/full-Fourier gate then tightens "
            "the branch further: ordinary rank-one torsion is closed negative for "
            "selected q64, compact Nil scalar and scalar SU3-center shortcuts are "
            "rejected, and the source-certified Endomorphism_E or equivalent "
            "Laplace-type threshold operator becomes the primary value route. The "
            "full positive Fourier orbit is now selected at 27-mode D_E gap-layer "
            "scope and rhoE-to-BN orientation is closed, while log(92160000) remains "
            "an exact relative trace identity pending same-source orientation-magnitude "
            "co-emission. The orientation/endomorphism finitepart packet then closes "
            "the next signed layer: finite projective rhoE source values and internal "
            "log(2008) finitepart are closed at internal scope; the 27x11 embedding "
            "intertwines rhoE characters but not the selected positive Phi_fin "
            "Laplacian finitepart; C_tau is selected as the BN signed central-rank "
            "operator and P^T C_tau P closes the signed operator identity. Its chiral "
            "positive convention has logdet 0 and eta 0, so it supplies orientation "
            "but not nonzero threshold magnitude. The oriented Phi_fin table is exact, "
            "with log(92160000) and full positive log(884736000000), but it remains "
            "support-only until a finite rhoE-to-oriented-BN functor, smooth E_Qa "
            "representative, or direct H K row is emitted. The finite-rhoE/oriented-BN "
            "frontier then closes the orientation functor only and closes BN27 direct "
            "finitepart arithmetic log(92160000) relative to source ownership. It "
            "builds the source-owned logdet minimal emission packet and conditional "
            "implication DAG, rejects a bare S_QaSU3^BN27 source name as proof, and "
            "collapses the six-validator export problem to source_branch_identity or "
            "selected connection values. The source-identity transport proof reduces "
            "to that single leaf, and the current-source no-go proves all three "
            "source-branch clauses have support but zero emitted clauses. The "
            "source-amendment/connection-values packet then locks this to values: "
            "the heterotic Qa/SU3 branch certificate is closed, the amendment "
            "template has 11 source-object fields with 0 filled, the "
            "connection-values template has 8 fields with 0 filled, 27-mode D_E "
            "gap/Riesz/Green export support is closed, selected trace equality is "
            "closed only at gap-layer scope, and the active connection-witness "
            "contract has three legal routes with 29 missing leaves. The exact "
            "next object is typed Cech/HYM/projective connection witness values or "
            "direct H K row. The typed Cech/HYM/projective gate then rechecks all "
            "three legal routes against the latest local packets: Cech/trace is "
            "only D_E gap-layer support, HYM/Galerkin is only diagonal/model-active "
            "support, and Route-C/HYM is only an extraction-contract scaffold. "
            "All old support is rejected as final selected connection values. The "
            "exact next object is a same-source connection-value table with 8 "
            "fields, or direct H K row. That table is now built: source_id and "
            "carrier_or_cover_id are present as support labels, but the validator "
            "accepts 0/8 final same-source connection values. The first non-label "
            "field to attack is transition_or_connection_representative, or a "
            "same-source certificate for q79/F,m=1. The independent direct "
            "K_threshold.Omega_H.lambda exit is now re-executed from this frontier: "
            "phase/direction prerequisites are closed (m0=0, sigma_D=+1, q79/F,m=1 "
            "+i, and the radial norm law), so the remaining direct blocker is "
            "source-owned r_H, direct N_H=Hess(F_H)[U_H,U_H], the selected "
            "L_rowlocal/T_scheme split pair, or direct K_threshold.Omega_H.lambda "
            "with row-level certificate. The H radial/direct-N_H blocker is then "
            "executed: strict no-knob source emission remains open, but the "
            "controlled/minimal one-parameter lane closes with UP-RET-OVERLAP.HRG, "
            "r_H=391.39140285811936, and N_H=r_H^2=153187.23023124668, yielding a "
            "conditional 10/10 H K layer. This calibrates lambda_H; it does not "
            "predict lambda_H and is not strict no-knob closure. "
            "The strict finite-H/source versus UP-RET-OVERLAP.HRG cross-use "
            "blocker is now executed as a decision theorem: strict finite-H "
            "source routes accept 0 value rows, non-Higgs HRG cross-use accepts "
            "0 targets, and the available controlled H lane is explicitly a "
            "one-parameter lane rather than no-knob closure. "
            "The H one-parameter adoption policy / finite-H construction fork "
            "is now audited: UP-RET-OVERLAP.HRG is available only as one "
            "declared, counted H-threshold/RG parameter, while strict no-knob "
            "closure remains reduced to selected F_H, M_source, K_H, or "
            "R_H^RG source rows. "
            "The H one-parameter execution ledger is now closed at the "
            "minimal-H standard: exactly one H parameter is spent, conditional "
            "H K closure is 10/10, strict finite-H source rows remain 0, and "
            "lambda_H remains calibrated rather than predicted. "
            "The selected 27x27 qutrit-Weyl package has now been pushed "
            "numerically: spectral diagnostics close, the selected charged rows "
            "extract a stable 2:1:1 profile across u,d,e, and pure matrix "
            "functionals still emit no H/lambda row. "
            "The radial transport branch now isolates the H scalar as "
            "r_H=pi^4*tau_H with tau_H=4.018017196377461. Integer tau_H=4 "
            "and tau_H=-logdet(D_211) are rejected as strict source values, "
            "while the one-parameter H lane is reparametrized without changing "
            "the counted parameter total. Strict no-knob closure therefore "
            "requires unpatched Phi_fin^C1 source emission, honest selected "
            "Galerkin C1 tau export, typed HRG consumer emission, or direct "
            "K_threshold.Omega_H.lambda. "
            "A bounded finite-C1 scalar export test then rejects C1 shape "
            "invariants as a tau_H source: the best C1-only family is exactly "
            "tau_H=4 with the same 0.448% residual, so the missing coefficient "
            "must come from an H-weighted selected Galerkin/metric/kernel payload "
            "or another same-source radial operator. "
            "Selected s_beta has now also been imported as clean H angular data "
            "and tested with C1 metric diagnostics; the best near miss is "
            "4*sqrt(1+2*s_beta) with relative residual about 1.85e-4, but zero "
            "angular/C1 rows are accepted because no same-source H-weighted "
            "metric integral emits that expression. The exact next payload is "
            "therefore H-weighted Galerkin metric/kernel rows or a direct radial "
            "operator. The selected HYM grid has now been replayed directly for "
            "metric moments; accepted metric-moment tau_H source rows remain 0, "
            "but the sharpest structural clue is the anisotropy/angular finite "
            "part 4+(x1_l2/y1_l2)/(3-4*s_beta), with relative residual about "
            "2.97e-6. This is retained only as a finite-part theorem target. "
            "The H-weighted coefficient inverse problem has now also been "
            "executed: tau_H(k)=4+(x1_l2/y1_l2)/(3-k*s_beta) requires "
            "k=3.579582815935827 for exact internal match, and the small "
            "source-window rational scan finds k=25/7 with relative residual "
            "about 5.76e-8. It remains quarantined, because 25 equals mesh+1 "
            "and 2*theta_series_cutoff+1 in the current replay window and no "
            "selected finite-part coefficient source rule emits it. "
            "The dual Bergman/HYM versus heat/zeta attempt then executes both "
            "routes: the Bergman/window route recovers k=25/7 as "
            "(2*theta_cutoff+1)/(CY_dim+End0_rank+trace_unit)=25/(3+3+1), "
            "while the flat heat/zeta proxy is weaker, with best simple proxy "
            "k=4 at relative residual about 2.97e-6. Accepted source rows "
            "remain 0; the next theorem must prove the Bergman/HYM denominator "
            "and exactness/error certificate or emit the selected H-sector "
            "heat/zeta radial operator directly. "
            "The denominator-7 follow-up now proves the structural count "
            "CY_dim+End0_rank+trace_unit=3+3+1=7, but also proves the "
            "exactness obstruction: k=25/7 is not k_required, the tau_H "
            "residual is nonzero, and an error certificate cannot close strict "
            "no-knob scalar promotion unless it is tied to a selected exact "
            "continuum/source object or correction term. "
            "A superset next-correction attempt now finds a source-native "
            "half-density interaction candidate: k=25/7 + sqrt(3)*s_beta + "
            "(log<exp(-2u)>-log<exp(2u)>)/8 - "
            "s_beta*(<exp(-u)>-<exp(u)>)/2. This gives tau_H residual below "
            "the selected Galerkin replay floor, but strict promotion remains "
            "blocked until the half-density interaction source rule or direct "
            "H-sector radial operator is analytically derived. "
            "The finite-cutoff exactness route split is now explicit: ordinary "
            "continuum bandlimit/trapezoid exactness is blocked for the current "
            "nonlinear exp(u) replay, and homogeneous Bergman exactness is not "
            "available for nonconstant u. The viable exactness route is to prove "
            "a FiniteProjectedHYMSourcePrinciple: MTT selects the finite "
            "projected algebra A_N with P_N, star_N, exp_N, Delta_N/Green_N, "
            "and Tr_N as source data, so the cutoff computation is exact for "
            "the selected finite source object rather than an approximation to "
            "an unprojected continuum object. "
            "That finite projected source principle is now constructed from the "
            "existing qutrit-Weyl rank-27 carrier and finite spectral package: "
            "A_N=C^3_class tensor M_3(C), H_N has dimension 27, Tr_N is the "
            "normalized Frobenius trace, star_N is represented by finite matrix "
            "multiplication, exp_N is a finite matrix/finite algebra exponential, "
            "and Delta_N/Green_N use the selected transported projector/Green "
            "rules. Thus automatic finite-cutoff exactness is closed for A_N "
            "source functionals; the remaining open object is the H scalar "
            "functional/half-density interaction source rule inside A_N. "
            "That H scalar source rule is now emitted as a finite A_N trace "
            "functional: k_H(A_N)=25/7+sqrt(3)*s_beta+"
            "(log Tr_N exp_N(-2u_N)-log Tr_N exp_N(2u_N))/8-"
            "s_beta*(Tr_N exp_N(-u_N)-Tr_N exp_N(u_N))/2. It emits "
            "tau_H^A_N=4.018017196377423 and r_H^A_N as strict finite-source "
            "values, with controlled tau_H retained only as downstream "
            "comparison; the remaining H frontier is lambda_H/K_threshold "
            "payload transport and full closure audit. "
            "Controlled empirical/"
            "minimal calibration lanes are available but remain non-no-knob. "
            "The strict physical-prefactor fork is now audited: current "
            "same-branch packets emit 0 accepted P_EW/direct-H strict rows, "
            "so P_EW is not promoted as strict source data; the H/lambda lane "
            "is instead exported as a minimal one-shared-physical-primitive "
            "seed for the full-SM parameter ledger. That ledger is now built: "
            "the active non-neutrino SM-like count is 18 excluding QCD "
            "theta_bar, and the minimal PMNS oscillation extension count is "
            "24 excluding QCD theta_bar; strict P_EW, QCD theta_bar, absolute "
            "neutrino/Majorana policy, precision covariance/thresholds, true "
            "equivalence, and no-knob closure remain open. The strict P_EW/"
            "SM precision cutset is now locked: current strict P_EW/direct-K "
            "accepted rows remain 0, so no count reduction is available now; "
            "if strict P_EW closes the counts would become 17/23 excluding "
            "QCD theta_bar, while admitting QCD theta_bar adds one slot. The "
            "next non-duplicative artifact is QCD theta policy or strict P_EW "
            "count reduction, with precision profile and selected Qa/SU3 "
            "source payload retained as later true-equivalence exits. The QCD "
            "theta policy is now closed at the conservative ledger level: "
            "theta_bar_QCD is admitted as one topological CP slot, giving "
            "19/25 counts including QCD theta_bar, or 18/24 if strict P_EW "
            "later closes. This does not select theta_bar, does not predict "
            "theta_bar=0, and does not solve strong CP. The neutrino policy "
            "layer is now tiered and audited: minimal PMNS oscillation replay "
            "gives 25 including QCD theta_bar, conditional Dirac massive "
            "neutrinos give 26, and conditional Majorana massive neutrinos "
            "give 28, or 24/25/27 respectively if strict P_EW later closes. "
            "Absolute mass, Dirac Yukawa scale, Majorana phases, and neutrino "
            "ontology are not selected source data yet. The precision-profile "
            "frontier table is now built: MSbar/M_Z policy, central-value "
            "tiering, versioned common-scale values, threshold/mass-scheme "
            "audits, local-QFT precision attempts, full-loop proxy inventory, "
            "and Qa/SU3 Step8/Step9 reductions are classified together. "
            "Accepted true-equivalence rows remain 0, so covariance/profile "
            "likelihood, threshold/mass-scheme source rows, local-QFT "
            "observables, actual selected Qa/SU3 payload values, strict P_EW/"
            "direct-K, and neutrino absolute source remain open. The Qa/SU3/"
            "strict-PEW fork is now audited: Step8 closes all 8 operator "
            "source slots at the source-slot layer and Step9 closes the "
            "non-looping C1 support/frontier reduction. Step10 Route A is now "
            "imported from the active ledger: the premise-free physical "
            "Phi_fin^C1 source rule promotes A_selected, b_selected, "
            "deltaTheta_C1, and sector response matrices, superseding stale "
            "source-rule-open wording. The first selected dynamic matter/"
            "overlap value rows are now accepted for the u/e phase response "
            "after replaying the old first-row rejection against the active "
            "same-source packet. The selected dynamic packet also closes the "
            "family-resolving operator and proves the sector-blind/universal "
            "eigenprofile no-go: magnitudes need selected sector projection "
            "weights, higher-response coefficients, or threshold response rows. "
            "The later sector-transfer/overlap-derivative reconciliation now "
            "retires the stale Step73 transfer/dotD blockers for the current "
            "K/Omega attempt; re-execution still emits 0 scalar source rows, "
            "so the active value wall is selected rowwise L_rowlocal values, "
            "T_scheme rows, and the lambda_H payload. "
            "Full S2 value rows, no-proxy Yukawa/CKM/PMNS/Higgs rows, and "
            "RO.value_source remain open. "
            "Strict P_EW/direct-K remains parallel and open with 0 accepted rows. "
            "Run `python scripts\\verify.py --full` "
            "for the frozen 2026-07-04 replay."
        )
        result = 0

    text = "\n".join(parts)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(text + "\n", encoding="utf-8")
    print(text)
    return result


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
