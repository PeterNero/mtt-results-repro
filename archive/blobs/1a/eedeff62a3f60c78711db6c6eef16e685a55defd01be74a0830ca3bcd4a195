from __future__ import annotations

import argparse
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path


DEFAULT_REPORT = Path(r"C:\Users\nero_\Downloads\MTT_Master_Corrigendum_and_Revision_Plan.md")
DEFAULT_VAULT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
DEFAULT_TEX_ROOT = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
DEFAULT_THETA_CORRECTED = DEFAULT_TEX_ROOT / "18 Theta-Closure & Execution Program" / "_md_v3_corrected"

RISK_PATTERNS = {
    "right_inverse": re.compile(r"right[ -]inverse|global inverse|partial inverse", re.I),
    "dimension_geometry": re.compile(r"4\s*\+\s*3\s*\+\s*3\s*\+\s*3|10.?dimensional|10D|Y_?4|X_?6|central circle", re.I),
    "circle_lens_nil": re.compile(r"circle.{0,30}lens.{0,30}nil|lens.{0,30}circle|exhaustive", re.I),
    "fixed_point": re.compile(r"fixed point|contractiv|Lyapunov|spectral gap", re.I),
    "probability_born": re.compile(r"Born rule|Born weight|probability|basin measure", re.I),
    "qft_quantization": re.compile(r"BRST|Faddeev|path integral|LSZ|Feynman|quantization", re.I),
    "qg_gaussian": re.compile(r"Gaussian|Stieltjes|K.{0,4}ll.n|all-loop|UV.?finite|unitary quantum gravity", re.I),
    "five_tev": re.compile(r"(?:4\.2|5)\s*(?:\\,)?\s*TeV|\\?Lambda_?\{?12\}?(?!\d)", re.I),
    "sm_claim": re.compile(r"full Standard Model|derive.{0,40}Standard Model|unique.{0,30}Standard Model|SM parity|true SM", re.I),
    "flavor": re.compile(r"Yukawa|CKM|PMNS|Jarlskog|three famil|family number", re.I),
    "higgs": re.compile(r"Higgs|lambda_?H|quartic|electroweak symmetry breaking", re.I),
    "topology_charge": re.compile(r"hypercharge|charge quant|anomaly|forbidden operator", re.I),
    "iwasawa_hym": re.compile(r"Iwasawa|Fu.?Yau|HYM|Hermitian.Yang.Mills|Chern class|\\?c_?\{?[123]\}?(?!\d)", re.I),
    "prediction_language": re.compile(r"predict|derive|forced|inevitable|closed|proved|unique", re.I),
}

AUTHORITIES = [
    {
        "id": "A01",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Current_TrueSMClosure_ConsolidatedLedger_v1.md",
        "claim": "Current non-looping authority; locks the 27x27 matrix, Yukawa profile rows, Pi_CKM, PEW/direct-K, K-threshold and the accepted AH-equivalent lane.",
    },
    {
        "id": "A02",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_MultiLoopCommonSourcePrecisionTransport_or_OfficialJointLikelihood_v1.md",
        "claim": "Selected SMDR v1.3 multi-loop threshold/mass-scheme transport: 15 source coordinates to 8 MSbar rows, positive-definite 8x8 covariance, 36/36 entries and 15/15 BCT-WZH cross entries.",
    },
    {
        "id": "A03",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_RenormalizedSMObservableFunctor_FromCommonSchemeAction_v1.md",
        "claim": "Five-arrow perturbative observable functor on the embedded renormalized-SM branch; standard SM BRST/Faddeev-Popov quantization is imported, not derived from MTT.",
    },
    {
        "id": "A04",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_FinalGlobalTrueSMClosureAudit_AfterMultiLoopPrecision_v1.md",
        "claim": "Twelve of twelve obligations close embedded renormalized-SM equivalence at the adopted one-shared-physical-primitive/profile standard; no-knob and unique selection remain open.",
    },
    {
        "id": "A05",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_StrictNoKnobUpgradeLedger_AfterTrueSMEquivalence_v1.md",
        "claim": "Separates the closed 12/12 baseline from nine stronger upgrades: 2/9 closed, six partial, and one dependency-blocked. U2 literal Cech-HYM and U4 CKM prediction-profile are closed; this does not imply zero-knob global closure.",
    },
    {
        "id": "A06",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_OfficialJointLikelihoodTransport_or_DeclaredDiagonalProfileFinality_v1.md",
        "claim": "Declares the diagonal measured-input profile final for the current reproducible standard; no public 15-coordinate official joint likelihood was identified.",
    },
    {
        "id": "A07",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_LiteralCechWitness_or_GlobalHYMConnectionCoefficients_v1.md",
        "claim": "Closes the literal finite Cech witness (81 entries and 729 cocycle triples); literal global HYM connection coefficients remain open, so U2 is 1/2.",
    },
    {
        "id": "A08",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\README.md",
        "claim": "Reproducible q=79/order-448, finite-gerbe, CP-character and conjugate-branch proof history; use only rows promoted by A01/A04 for final SM claims.",
    },
    {
        "id": "A09",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-repro\README.md",
        "claim": "Frozen historical SM-parity capsule. Its true-equivalence=false statement is superseded by A02-A04, while its no-knob guard remains valid.",
    },
    {
        "id": "A10",
        "path": r"C:\Users\nero_\Downloads\MTT_Master_Corrigendum_and_Revision_Plan.md",
        "claim": "External full-corpus audit and durable correction specification, subject to the explicit successor decisions in this ledger.",
    },
    {
        "id": "A11",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus\Consolidated_Exact_Z64_to_q79_Closure_Theorem_v1.md",
        "claim": "Direct q=79 exact/charge theorem: q64=15, q7=2 and CRT give q=79 mod 448 on the selected exact branch, with its stated branch assumptions.",
    },
    {
        "id": "A12",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus\Q79_Theorem_Change_List_for_Paper_Updates_v1.md",
        "claim": "Detailed q79 narrative correction ledger. Its older full-SM-open statements remain authoritative for strict no-proxy q79 closure but are superseded by A04 for the weaker adopted profile-standard equivalence claim.",
    },
    {
        "id": "A13",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof\proof_corpus\GR_TT_Support_Final_Theorem_v1.md",
        "claim": "Closes internal exact-branch TT support on the Z64 helicity-2 carrier; physical Newton/Planck normalization and full stress-energy response remain open.",
    },
    {
        "id": "A14",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_CKMCentralEstimatorRetirement_or_PredictionProfileClosure_v1.md",
        "claim": "Closes U4 at the selected prediction-with-uncertainty standard. The three source rows have maximum profile displacement 2.36e-4 sigma; exact equality to a moving experimental central estimator is retired as an invalid closure requirement.",
    },
    {
        "id": "A15",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_GlobalHYMChernSequence_APosterioriCertificate_v1.md",
        "claim": "Types the global Chern sequence and certifies the finite projected HYM solution with residual 8.21e-13, coercivity margin 26.02, and error indicator 3.15e-14. Uniform continuum convergence and patchwise control remain open.",
    },
    {
        "id": "A16",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutrinoAndStrongCP_StrictUpgradeAttack_v1.md",
        "claim": "Selects the Dirac channel, restricts admissible Majorana self-characters to 0 and 672, and preserves the conditional PQ theorem and axion-ratio result. Absolute neutrino mass, unique neutrino ontology, and the selected central QCD-anomaly map remain open.",
    },
    {
        "id": "A17",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_BranchOrbitAndRetardedRepresentative_or_GlobalMeasureUniqueness_v1.md",
        "claim": "Closes the antiunitary orbit and selects the retarded q=79/F/m1 representative at orientation level. It does not prove uniqueness of the global MTT carrier measure.",
    },
    {
        "id": "A18",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_QuantizationAndNonperturbativeQFT_StrictUpgradeAudit_v1.md",
        "claim": "Records six conditional quantization results and four constructive finite-domain QFT results while preserving the missing capture-measure, BRST/gauge-orbit, continuum, and full four-dimensional existence obligations.",
    },
    {
        "id": "A19",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_HYMValidatedFourierResidualTailBound_v1.md",
        "claim": "Closes the selected rank-two continuum HYM witness by an exact weighted-theta Fourier-tail bound and Wiener contraction: Z=0.38508 and Y+Zr=0.00932703<r=0.01. Combined with A07/A15 patching, U2 literal witness families close 2/2; global uniqueness over all HYM branches and rank-three transfer are not claimed.",
    },
    {
        "id": "A20",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralNilBoundaryMassFunctional_v1.md",
        "claim": "Proves the neutral three-basin minimal-trace boundary theorem: if neutral nil-survivor saturation selects the trace-minimal positive spectrum, m_lightest=0 uniquely. NO/IO sums 0.058784/0.101001 eV are postchecks only. Source promotion, ordering selection, and Dirac-action completeness versus a separate Majorana operator remain open.",
    },
    {
        "id": "A21",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralOperatorUnificationAndInventoryAudit_v1.md",
        "claim": "Contracts the three neutral-mass source clauses to one selected complex-symmetric neutral operator. This predecessor checkpoint sources only the basis field (1/8) and rejects the dimensionless C1 nuD response as an absolute mass operator.",
    },
    {
        "id": "A23",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralMassOperator_SourceEmission_v1.md",
        "claim": "Successor to A21: imports the selected q79/F/m1 source id, literal HYM witness, selected Dirac route, Majorana self-character gate and no-observed-selector certificate. Neutral operator source-provenance inventory is now 4/8; dimensionful M_D/M_L/M_R blocks and absolute normalization remain open.",
    },
    {
        "id": "A24",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralDimensionfulBlocksAndNormalization_v1.md",
        "claim": "Successor to A23: proves the neutral dimensionful-block normal form and rejects benchmark seesaw matrices, observed neutrino splittings, conditional physical-unit bridges, and dimensionless C1 nuD as source selectors. The neutral inventory remains 4/8; the remaining exits are Dirac-complete M_D=v_u Y_nu, Majorana/seesaw blocks with k=0 or 672, or nil-boundary effective spectrum plus reconstruction.",
    },
    {
        "id": "A25",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralOverlapKernelPhysicalUnitOrActionCompleteness_v1.md",
        "claim": "Successor to A24: executes the neutral overlap-kernel/physical-unit/action-completeness gate. The selected overlap schema is support only, omega_gap_phys remains unselected, Dirac-only action completeness is not derived, neutral OK gates are 3/9, and accepted neutral exits remain 0/3 with no new U5 value rows.",
    },
    {
        "id": "A26",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1.md",
        "claim": "Successor to A25: promotes selected neutral carrier/projector and trace-Gram readiness. L, N^c, and H-as-Hu carrier projectors plus same-source trace-Gram/slot consistency are selected; neutral overlap OK gates advance to 5/9 and readiness to 6/12. No neutral value rows are emitted and accepted exits remain 0/3.",
    },
    {
        "id": "A27",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1.md",
        "claim": "Successor to A26: closes the selected typed L x N^c x H_u neutral trilinear carrier skeleton with nine structural Gamma_nu slots. Neutral overlap OK gates remain 5/9 and readiness advances to 7/13; finite Gamma_nu[i,j] channel sets, action costs, prefactors, retarded signs, Dirac-only completeness, and value rows remain open.",
    },
    {
        "id": "A28",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1.md",
        "claim": "Successor to A27: imports the selected same-source dynamic overlap theorem and closes all nine finite neutral channel rows as `Gamma_nu^chan=I3+X3`, with six active channels and three exact zeros. Neutral OK gates advance to 6/9 and readiness to 8/13. These are exact channel multiplicities, not physical neutrino masses; action costs, prefactors, retarded signs, physical units, absolute normalization, and Dirac/Majorana completion remain open.",
    },
    {
        "id": "A29",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1.md",
        "claim": "Successor to A28: closes the selected two-representative neutral relative-amplitude orbit. Diagonal coefficients are `1` and active cyclic-shift coefficients are `3/2 +/- i sqrt(3)/2`, with magnitude `sqrt(3)`, phase `+/-pi/6`, and spectrum `[1,4,7]`. Eighteen relative dimensionless rows close across the conjugate pair; the absolute action scale/prefactor, unique representative, physical unit, and Dirac/Majorana completion remain open.",
    },
    {
        "id": "A30",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1.md",
        "claim": "Successor to A29: promotes the complete same-source internal dimensionless `nuD` response. All 9/9 rows and 7/7 provenance fields close with `a_int=0.34195899479289005`; readiness advances to 9/14. This is not a physical Yukawa normalization or neutrino mass in eV, so physical value fields remain zero.",
    },
    {
        "id": "A31",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1.md",
        "claim": "Successor to A30: proves a common scale or physical unit cannot repair the selected `[1,4,7]` spectrum. Nil subtraction gives `[0,3,6]` and ratio `1/2`, incompatible with the downstream normal-ordering ratio `0.029805`. The scale-only route is retired; the minimal surviving route needs one selected non-affine spectral-action slope plus one universal scale, or a selected seesaw block.",
    },
    {
        "id": "A32",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1.md",
        "claim": "Successor to A31: executes the available source-motivated neutral candidates. The exact internal proper-time trial gives `0.227768`; q79/q369 give `0.067879`; q7/qmod is closest at `0.031881` but misses the `0.029805` postcheck by `0.002076`. CP/retarded characters cannot be reused as Majorana self-characters. The remaining object is a typed neutral circle/proper-time-to-mass-cost transfer or neutral real-structure functor.",
    },
    {
        "id": "A33",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_ProtoSpinorAlignmentToDiracMassReadout_v1.md",
        "claim": "Successor to A32: constructs a self-adjoint, chirally odd `6x6` operator from the selected rank-three `L/Nc` Weyl blocks and `I3+X3` transfer. `H1` is indefinite and therefore not the mass-squared Hessian. The coefficient-matched alignment trial has singular values `[0,a,2a]`, a nil zero mode and squared ratio `1/4`, but is not a selected VEV coordinate. The remaining source object is the radial second-variation/VEV theorem.",
    },
    {
        "id": "A34",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1.md",
        "claim": "Successor to A33: closes the exact formal Gram second variation with positive spectrum `[2,2,8]`, inventories the selected H radial values `tau_H` and `r_H`, and rejects their direct identity insertion into the neutral coordinate. At the adopted profile standard `v=246.219640 GeV` is the shared electroweak baseline and adds no neutrino-specific parameter, but is not a strict no-knob MTT derivation. The remaining object is the typed neutral Higgs-insertion functor and coordinate normalization.",
    },
    {
        "id": "A35",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1.md",
        "claim": "Successor to A34: closes the same-source rank-one `H:h0` insertion. Unit normalization fixes the dimensionless insertion magnitude to one and gives `dY_nu/dh_H=Gamma_nu^chan=I3+X3` for all nine typed neutral cells. The unselected carrier `U(1)` phase cancels from the positive Gram curvature `[2,2,8]`. Physical `S_gamma/A_gamma` and retarded-character weights, strict dimensionful VEV selection and Majorana completion remain open; dimensionful M_D/M_L/M_R remain open. The strict frontier is the action-weighted neutral response and dimensionful Dirac readout.",
    },
    {
        "id": "A36",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralEffectiveWeightIdentifiabilityReduction_v1.md",
        "claim": "Successor to A35: proves separate `A_gamma` and `S_gamma` are non-identifiable factorization-gauge variables in `W_gamma=A_gamma exp(-S_gamma) sign_gamma` and retires their independent row obligations. The combined same-source internal effective response is already selected, and conjugate representatives have identical mass-Gram spectra. The physical Dirac cutset is one selected non-affine shape coordinate plus one absolute scale.",
    },
    {
        "id": "A37",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralCRTPhaseTypingAndProtoSpinorNilDriftReduction_v1.md",
        "claim": "Successor to A36: proves `q7=2` is a `Z7` residue with local phase fraction `2/7` and q7-only CRT lift `128/448=2/7`, not `2/448`. The former `0.031881` clue is retired as mistyped. The proto-spinor three-basin nil-drift formula remains the correctly typed neutral shape family; genuine `phi_nu` and one absolute scale `mu_nu` remain open.",
    },
    {
        "id": "A38",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralCommonCircleFactorizationAndHolonomyScalarReduction_v1.md",
        "claim": "Successor to A37: derives the proto-spinor cosine orbit from selected `H_cen=diag(1,zeta3,zeta3^2)` through `H_nu(phi_nu)=exp(i phi_nu)H_cen`. It proves `phi_nu=(arg det H_nu)/3 mod 2pi/3`, reducing shape to one scalar. The operator-level neutral response, its phase value and anchored Hessian scale remain open.",
    },
    {
        "id": "A39",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralFiniteHeisenbergDeterminantNoGoAndSmoothLiftTarget_v1.md",
        "claim": "Successor to A38: checks all 27 finite Heisenberg elements and proves the promoted qutrit `rho_E` image lies in `SU(3)` with trivial determinant. It cannot source continuous `phi_nu`; determinant-trivial phases only permute the `Z3` orbit and retain exact degeneracy. The required source is a smooth determinant-line `U(1)` holonomy plus anchored scale.",
    },
    {
        "id": "A40",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralTwoPrimitiveProfileValueClosure_v1.md",
        "claim": "Successor to A39: at the explicitly declared normal-ordering Dirac profile with m_lightest=0, two measured mass-squared splittings uniquely calibrate phi_nu and A_nu and emit 36 neutral mass, Yukawa and matrix rows. This is measured-profile completion, not strict no-knob source selection.",
    },
    {
        "id": "A41",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralLensDedekindTransgression_or_OnePrimitiveProfile_v1.md",
        "claim": "Successor to A40: the selected retarded pair 16->15 gives the exact Lens/Dedekind mixed reciprocity residue 1/240. Conditional identification with the neutral determinant line gives phi_nu=pi/120 and reduces the splitting profile to one measured scale, with a 0.0233-sigma compatibility pull. The APS/Bismut-Freed operator and cancellation normalization remain open, and the hypothesis is target-ranked rather than pre-registered.",
    },
    {
        "id": "A42",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralUniversalE0AttenuationCandidate_or_SourceLawFrontier_v1.md",
        "claim": "Successor to A41: combines the existing one-anchor GR E0 family, selected N=448 and tau_int=log(448)/15, the conditional corpus 11D M-theory lift, and the A41 phase in the target-ranked trial mu_nu=E0*448^-11*exp(-tau_int/4). With measured G as the one universal metrology primitive, the resulting neutral Hessian amplitude agrees with A40 at about 18 ppm. Native MTT is 10D, so the physical neutral-operator lift identification, attenuation law, normalization and APS identification remain open.",
    },
    {
        "id": "A43",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_NeutralCompositeSpectralAttenuationReduction_or_BranchBridgeTheorem_v1.md",
        "claim": "Successor to A42: conditionally proves the exact 11D-lift compression 448^-11 exp(-tau_int/4)=exp(-tau_int*661/4) and proves 1/(1+r_nu) is the unit-trace normalization of the A41 shape. Native MTT has census 4+(1+2+3)=10; only the separate circle lift gives 11, and the native 10D formula misses A40 by 448^2 in A_nu. Strict promotion requires physical neutral-operator lift selection, nil saturation and a same-operator Z64/nil bridge.",
    },
    {
        "id": "A44",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_SameGeometryQutritToSMAlgebraBridge_or_GenerativeBaseFrontier_v1.md",
        "claim": "Locks the already-closed embedded renormalized-SM observable functor and attacks the stronger generative base. It proves A_Q=M3(C)^3 is not directly the SM finite algebra, then constructs an exact conditional three-lane reduction C plus H plus M3(C) using rank-one/rank-two/full corners and a quaternionic antiunitary real structure. Native selection of the lane projectors and weak real structure, followed by the chiral representation and anomaly table, remains open.",
    },
    {
        "id": "A22",
        "path": r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus\MTT_Selected_E6CentralGeneratorQCDAnomalyAudit_v1.md",
        "claim": "Computes the exact E6 Qpsi color-anomaly trace: three matter families contribute +12 and complete-27 exotics -12, so the full anomaly cancels. The matter-only/singlet diagnostic gives N_DW=3; strong-CP closure requires a selected flux/threshold axion-current anomaly-matching map.",
    },
]

REPOSITORY_DECISIONS = [
    ("mtt-sm-parity-closure", "CURRENT PRIMARY", "Use A01-A07 and A14-A44 with their passing audits for SM numerical/profile and strict-upgrade claims. Historical open packets inside the same repo are provenance, not current status."),
    ("mtt-q79-proof-repro", "CURRENT FOR q79 EXACT BRANCH", "Use A11 for q=79 and A12 for detailed theorem corrections. Do not import old 'full SM open' language over A04 without specifying the stricter no-proxy scope."),
    ("mtt-sm-parity-repro", "HISTORICAL FROZEN CAPSULE", "Retain its SM-parity and no-knob guardrails. Its true-SM-equivalence=false line is superseded at the adopted profile standard by A02-A04."),
    ("mtt-qa-su3-packet-proof", "SUPPORT / STRICT-UPGRADE SOURCE", "Use only rows promoted into A01/A07. Raw source-augmentation, smooth HYM and operator-payload open packets do not reopen the accepted AH-equivalent/profile baseline."),
    ("mtt-individual-constants-source-search", "STRICT-UPGRADE EVIDENCE", "Use its Higgs/Huv underdetermination results when discussing zero-knob or UV-Higgs derivation. They do not negate the accepted profile/direct-K Higgs row in A01/A04."),
    ("mtt-nonsm-constants-no-knob", "STRICT-UPGRADE EVIDENCE", "Use for open absolute-normalization and non-SM constant claims; do not promote ratio/repair/conditional packets to predictions."),
    ("mtt-protospinor-gr-response-proof", "SCOPED GR SUCCESSOR", "Use A13 for internal exact-branch TT support only. Keep Newton/Planck normalization, full stress response and projection-only GR derivation open."),
    ("18 Theta-Closure & Execution Program", "FIRST-PASS CORRECTED SOURCE + LEGACY VERIFIER", "Start the ten paper revisions from tracked `_md_v3_corrected`, preserving its five material repairs. Then replace obsolete numerical authority with A01-A06 rather than preserving old benchmarks as predictions."),
]

REPORT_CLAUSE_DECISIONS = [
    ("Parts I-II: status vocabulary and dependency order", "APPLIES", "Use unchanged. New successors alter downstream status, not the distinction among theorem, embedding, calibration, replay and prediction."),
    ("Part III.1-3: 4+6 geometry, symbols, time/scale", "APPLIES", "No numerical successor proves a different coordinate decomposition. The central circle remains bundle/phase data rather than an extra seventh fiber coordinate."),
    ("Part III.4-9: commutation, gaps, signs, fixed points, locality and maps", "APPLIES", "These are mathematical typing and hypothesis corrections upstream of all calculation repositories."),
    ("Part III.10-12: probability, reduced density dynamics, signature", "APPLIES", "A03 imports standard SM quantization but does not derive the missing MTT basin-trace/Born or signature-selection theorems."),
    ("Part III.13 and P0.4-P0.5: external Gaussian QG and all-loop finiteness", "APPLIES", "A03 is perturbative SM observable equivalence, not a constructive QG or all-loop finiteness theorem."),
    ("P0.1: right-inverse obstruction", "APPLIES", "No later repository restores the invalid inference from noninjectivity to absence of a right inverse."),
    ("P0.2: 4.2-5 TeV execution chain", "APPLIES WITH REPLACEMENT", "Withdraw the old crossing and dependent calibrations. A02 replaces precision running/matching at Q=Mt; it does not validate the old scale."),
    ("P0.3: explicit Iwasawa bundle", "APPLIES WITH SELECTED SUCCESSOR", "The old nonclosed Chern representative remains invalid. A07 closes the finite literal Cech witness, A15 closes Chern patching, and A19 closes continuum existence/local uniqueness for the selected rank-two q79/F/m1 HYM witness. This does not rehabilitate the withdrawn old representative or prove rank-three/global-branch uniqueness."),
    ("P0.6 and Groups 3-4: Foundation/Fixed-Points corrections", "APPLIES", "The calculation repositories consume portions of this spine but do not repair the source papers automatically."),
    ("Groups 6-9: QM, probability, measurement and Bell", "APPLIES WITH AUDITED PARTIAL RESULTS", "A18 preserves six conditional quantization results, but A03/A18 do not prove the MTT basin-trace equality, capture measure, outcome rule or global selection measure."),
    ("Group 7: QFT and amplitudes", "APPLIES WITH SUCCESSOR", "A03 closes the standard perturbative observable functor on the embedded SM branch. Rewrite derivation claims so BRST/Faddeev-Popov, Green functions and LSZ are explicitly imported parity structure."),
    ("Groups 10 and 13: proto-spinor/topology/SM", "APPLIES WITH SUCCESSOR", "Uniqueness and representation-input cautions remain. A01-A04 add a scoped numerical parity/profile theorem, not a unique no-knob derivation of particles. A11 fixes q=79 on its exact branch."),
    ("Group 11 and proto-spinor GR response", "APPLIES WITH SCOPED A13", "A13 closes internal exact-branch TT support, not Newton/Planck normalization, full stress response or projection-only derivation of Einstein gravity."),
    ("Group 12: quantum gravity", "APPLIES WITH AUDITED PARTIAL RESULTS", "A18 records finite-domain constructive results but neither the SM observable functor, multi-loop SMDR transport nor A13/A18 closes full continuum QG, positivity or asymptotic completeness."),
    ("Group 16: string/flux", "APPLIES WITH A07/A15/A19", "Keep embedding/reconstruction language and the Iwasawa withdrawal; add the verified finite Cech result, Chern patching, and selected rank-two continuum HYM theorem while retaining rank-three and all-branch uniqueness guards."),
    ("Group 18: Theta and execution", "PARTLY SUPERSEDED", "The old numerical tables remain invalid where tied to 5 TeV or fitted matrices. Replace matching observables with A01-A06 and preserve replay/profile labels."),
    ("Part XII: final status", "APPLIES WITH ONE ADDITION", "Its unique/no-knob/foundational open list remains correct. Add the newly closed embedded renormalized-SM equivalence result at the declared profile standard."),
]

HIGH_IMPACT_UPDATES = [
    ("Index v8 ZIP", "main.tex L17-343, especially SM L219-230, QFT L143-155, QG L205-218, execution L327-342", "Regenerate summaries and status labels last from revised papers.", "A01-A10"),
    ("Book v9", "L10-124 claim discipline; L393-438 reader map; L622-840 FCC/QG claims; every group summary and final outlook", "Add corrigendum conventions and current scoped closure; remove stale closed/derived summaries.", "A01-A10"),
    ("From MTT to Standard Model v2 ZIP", "main.tex abstract L27-45; intro L47-64; gauge L85; matter L102; families L137; Higgs L162; Yukawa L190; RGE L646; predictions L711; conclusion L721", "Major new version. Replace 'rigorous derivation of the full SM' with the A04 embedding/equivalence theorem and separate structural inputs, profile rows and strict upgrades.", "A01,A02,A03,A04,A05,A06,A08,A10"),
    ("Tiered Roadmap v2", "abstract L2; Tier 1 L128; Tier 3 L197; Tier 4 L272; TOE matrix L391; milestones L476; conclusion L558", "Replace completed old tiers with a two-standard ledger: closed profile/parity baseline and open strict upgrades.", "A01-A06,A10"),
    ("Superset Determinations v2", "RGE/crossings L117-186; zeta L187-252; K L258-301; alpha_s L345-366; identifiability L480; conclusion L661", "Withdraw 5 TeV-derived values. Insert SMDR transport and covariance only for the observables it actually computes.", "A02,A06,A10"),
    ("Execution I v2", "inputs L173; thresholds L325-456; moduli L457-560; axion L561-615; one-loop thresholds L616-662; conclusion L698", "Retain old geometry only as historical/calibration material unless independently revalidated; replace threshold/mass-scheme claims with A02 where applicable.", "A01,A02,A05,A06,A10"),
    ("Execution II v2", "corrected source: abstract L2-19; quarks/Yukawa/CKM L119-206; leptons/PMNS L207-316; Higgs L317-377; input ledger L378-402; executable benchmark check L420-474; conclusion L475", "Use A20-A21/A23-A44. A40-A43 govern the neutral profile and conditional scale candidates. A44 preserves the closed embedded QFT recovery while adding the exact conditional qutrit-class-lane to SM finite-algebra bridge and its source-selection guard.", "A01,A02,A04,A05,A06,A08,A10,A14,A16,A20,A21,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38,A39,A40,A41,A42,A43,A44"),
    ("Theta Closure I-V", "use `_md_v3_corrected`; each abstract, numerical target/RG section, theorem-status summary and conclusion; corrected Theta I specifically L186-363 and L791-994", "Preserve first-pass claim/arithmetic corrections, remove old crossing targets, and label overlap normalization as calibration unless promoted by A01-A06.", "A01,A02,A05,A06,A10"),
    ("Proto-spinor and Closure-Strain papers", "proto-spinor scope L29-109 and main theorem L589; Closure-Strain Higgs L633-726, Yukawa L727-792, families L989, quarks L1173, mixing L1383, CP L1468, status L1737", "Keep carrier/encoding results conditional. Import selected numerical rows as downstream evidence; do not use them to prove unique Higgs, families or particle ontology.", "A01,A04,A05,A11,A12,A13,A10"),
    ("QFT/amplitude papers", "QFT curved-spacetime quantization L243-337 and conclusion L620; amplitudes action/parameters L206-298, LSZ L523-609, BRST L738-813, completeness L982-1066", "State the A03 five-arrow functor explicitly and mark standard quantization/action as imported parity structure.", "A03,A04,A05,A10"),
    ("Flux Compactifications v3", "abstract L2; bundle/Chern/stability construction throughout; Iwasawa Yukawa L293; conclusion L378", "Withdraw the invalid old bundle construction, then add A07 finite Cech, A15 Chern patching/stability, and A19 selected rank-two continuum HYM as a distinct successor theorem. Do not claim rank-three transfer or uniqueness over all HYM branches.", "A07,A08,A10,A15,A19"),
    ("Topology/SM constraint papers", "abstracts, charge/hypercharge/anomaly theorems, family/Higgs/axion claims and conclusions", "Separate supplied SM representation/anomaly checks from selected output; cross-reference A04 only as scoped embedded equivalence and A22 for the exact E6 Qpsi anomaly cancellation and remaining flux/threshold matching obligation.", "A01,A04,A05,A10,A22"),
    ("Quantum-gravity papers", "abstracts, Gaussian propagator/finiteness theorems, BRST/unitarity sections and conclusions", "Apply P0.4-P0.5 unchanged. Do not infer QG closure from A03.", "A03,A05,A10"),
]


def normalize(name: str) -> str:
    name = re.sub(r"\.(?:md|zip)$", "", name, flags=re.I)
    name = re.sub(r"\s+/\s+v\d+$", "", name, flags=re.I)
    name = re.sub(r"\s+\(1\)$", "", name)
    return re.sub(r"[^a-z0-9]", "", name.lower())


def parse_report(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: list[dict] = []
    group = "Corpus-wide"
    i = 0
    while i < len(lines):
        line = lines[i]
        group_match = re.match(r"^# Group\s+([^—]+)—\s*(.+)$", line)
        if group_match:
            group = f"Group {group_match.group(1).strip()} - {group_match.group(2).strip()}"
        paper_match = re.match(r"^## `([^`]+)`", line)
        if not paper_match:
            i += 1
            continue
        start = i
        name = paper_match.group(1)
        i += 1
        block: list[str] = []
        while i < len(lines) and not re.match(r"^## `|^# Group\s+", lines[i]):
            block.append(lines[i])
            i += 1
        text = "\n".join(block)
        disposition = re.search(r"\*\*Disposition:\*\*\s*([^\n]+)", text)
        priority = re.search(r"\*\*Priority:\*\*\s*([^\n]+)", text)
        required: list[str] = []
        in_required = False
        for item in block:
            if item.strip() == "### Required changes":
                in_required = True
                continue
            if in_required and item.startswith("### "):
                in_required = False
            if in_required and item.startswith("- "):
                required.append(item[2:].strip())
        entries.append(
            {
                "report_name": name,
                "group": group,
                "report_line": start + 1,
                "disposition": disposition.group(1).strip() if disposition else None,
                "priority": priority.group(1).strip() if priority else None,
                "required_changes": required,
            }
        )
    return entries


def read_zip_main(path: Path) -> tuple[str, str]:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        entry = "main.tex" if "main.tex" in names else next(n for n in names if n.endswith(".tex"))
        return entry, archive.read(entry).decode("utf-8")


def source_lines(target: dict) -> list[str]:
    path = Path(target["path"])
    if target["source_kind"] == "zip_tex":
        _, text = read_zip_main(path)
        return text.splitlines()
    return path.read_text(encoding="utf-8-sig").splitlines()


def locate(lines: list[str]) -> dict:
    headings = []
    abstract = []
    conclusions = []
    risk_hits: dict[str, list[dict]] = defaultdict(list)
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("#") or re.match(r"\\(?:sub)*section\*?\{", stripped):
            headings.append({"line": number, "text": stripped[:240]})
            if re.search(r"conclusion|outlook|summary", stripped, re.I):
                conclusions.append({"line": number, "text": stripped[:240]})
        if re.search(r"abstract:\s*\||\\begin\{abstract\}", stripped, re.I):
            abstract.append({"line": number, "text": stripped[:240]})
        for key, pattern in RISK_PATTERNS.items():
            if pattern.search(stripped):
                risk_hits[key].append({"line": number, "text": stripped[:280]})
    return {
        "abstract": abstract,
        "headings": headings,
        "conclusions": conclusions,
        "risk_hits": dict(risk_hits),
    }


def overlays_for(target: dict) -> list[str]:
    path = target["path"].lower()
    overlays = ["A10"]
    if "0 index corpus" in path or "book on modal triplet" in path:
        overlays += ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21", "A22", "A23", "A24", "A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33", "A34", "A35", "A36", "A37", "A38", "A39", "A40", "A41", "A42", "A43", "A44"]
    if "18 theta-closure" in path:
        overlays += ["A01", "A02", "A04", "A05", "A06", "A08", "A09", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21", "A22", "A23", "A24", "A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33", "A34", "A35", "A36", "A37", "A38", "A39", "A40", "A41", "A42", "A43", "A44"]
    if "standard model" in path or "protospinor" in path:
        overlays += ["A01", "A02", "A04", "A05", "A06", "A08", "A09", "A11", "A12", "A14", "A15", "A16", "A17", "A19", "A20", "A21", "A22", "A23", "A24", "A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33", "A34", "A35", "A36", "A37", "A38", "A39", "A40", "A41", "A42", "A43", "A44"]
    if "protospinor" in path or "general relativity" in path:
        overlays += ["A13"]
    if "quantum field theory" in path:
        overlays += ["A03", "A04", "A05", "A18"]
    if "quantum mechanics" in path or "measurement" in path:
        overlays += ["A03", "A05", "A18"]
    if "strings, flux" in path:
        overlays += ["A07", "A08", "A11", "A12", "A15", "A17", "A19"]
    if "quantum gravity" in path:
        overlays += ["A03", "A05", "A18"]
    return list(dict.fromkeys(overlays))


def status_decision(target: dict) -> str:
    path = target["path"].lower()
    if "flux_compactifications_in_heterotic" in path:
        return "APPLIES_WITH_SUCCESSOR: old Iwasawa bundle construction remains withdrawn; add A07 finite Cech closure, A15 Chern patching/stability, and A19 selected rank-two continuum HYM while retaining rank-three and all-branch uniqueness guards."
    if "18 theta-closure" in path:
        return "PARTLY_SUPERSEDED: old 5 TeV chain remains invalid; replace numerical claims with A01-A06 where the observable and scope match."
    if "from_mtt_to_standard_model" in path:
        return "MAJOR_REWRITE: replace full derivation language with A04 embedded renormalized-SM equivalence and A05 strict-upgrade guardrails."
    if "quantum field theory" in path:
        return "APPLIES_WITH_SUCCESSOR: imported-SM perturbative observable equivalence is now closed by A03; MTT-derived quantization and nonperturbative QFT remain open."
    if "standard model" in path or "protospinor" in path:
        return "APPLIES_WITH_SUCCESSOR: representation/uniqueness cautions remain; add the scoped parity/profile results from A01-A06."
    return "APPLIES: no audited successor removes the external report's correction; use any listed authority only within its stated scope."


def anchor_summary(locations: dict) -> list[str]:
    anchors: list[str] = []
    anchors.extend(f"L{x['line']} {x['text']}" for x in locations["abstract"][:1])
    anchors.extend(f"L{x['line']} {x['text']}" for x in locations["conclusions"][:2])
    priority_keys = ["five_tev", "sm_claim", "flavor", "higgs", "iwasawa_hym", "right_inverse", "qg_gaussian", "qft_quantization"]
    for key in priority_keys:
        hits = locations["risk_hits"].get(key, [])
        if hits:
            x = hits[0]
            anchors.append(f"L{x['line']} [{key}] {x['text']}")
    if not anchors and locations["headings"]:
        x = locations["headings"][0]
        anchors.append(f"L{x['line']} {x['text']}")
    return anchors[:10]


def build(report: Path, vault: Path, tex_root: Path, theta_corrected: Path) -> dict:
    report_entries = parse_report(report)
    markdown_files = sorted(vault.rglob("*.md"))
    zip_targets = [
        tex_root / "0 Index Corpus" / "Modal_Triplet_Theory__Corpus_Index_and_Reference_v8.zip",
        tex_root / "13 Standard Model & Topology-Only Constraints" / "Modal_Triplet_Theory__From_MTT_to_Standard_Model_v2.zip",
    ]
    targets = []
    theta_first_pass_total = 0
    theta_first_pass_changed = 0
    for path in markdown_files:
        target_path = path
        source_kind = "markdown"
        lineage = None
        if path.parent.name == "18 Theta-Closure & Execution Program":
            corrected = theta_corrected / path.name
            if corrected.exists():
                theta_first_pass_total += 1
                changed = corrected.read_bytes() != path.read_bytes()
                theta_first_pass_changed += int(changed)
                target_path = corrected
                source_kind = "markdown_corrected_intermediate"
                lineage = {
                    "prior_authoring_path": str(path),
                    "first_pass_corrected_path": str(corrected),
                    "materially_changed_in_first_pass": changed,
                    "next_revision_must_start_from_first_pass": True,
                }
        target = {"name": path.name, "path": str(target_path), "source_kind": source_kind, "group": path.parent.name}
        if lineage:
            target["source_lineage"] = lineage
        targets.append(target)
    targets.extend(
        {"name": p.name, "path": str(p), "source_kind": "zip_tex", "group": p.parent.name}
        for p in zip_targets
    )
    by_normalized: dict[str, list[dict]] = defaultdict(list)
    for target in targets:
        by_normalized[normalize(target["name"])].append(target)

    unmatched_report = []
    mapped_report_ids: set[int] = set()
    for index, entry in enumerate(report_entries):
        candidates = by_normalized.get(normalize(entry["report_name"]), [])
        if not candidates and "corpusindexandreference" in normalize(entry["report_name"]):
            candidates = [t for t in targets if "corpusindexandreference" in normalize(t["name"])]
        if not candidates and entry["report_name"].endswith("_v8.md"):
            stem = normalize(entry["report_name"].replace("_v8.md", "_v11.md"))
            candidates = by_normalized.get(stem, [])
            if candidates:
                entry["obsolete_version_folded_into_latest"] = True
        if len(candidates) != 1:
            unmatched_report.append({**entry, "candidate_count": len(candidates)})
            continue
        target = candidates[0]
        target.setdefault("report_entries", []).append(entry)
        mapped_report_ids.add(index)

    papers = []
    for target in targets:
        lines = source_lines(target)
        locations = locate(lines)
        entries = target.get("report_entries", [])
        required = []
        for entry in entries:
            required.extend(entry["required_changes"])
        paper = {
            **{k: v for k, v in target.items() if k != "report_entries"},
            "line_count": len(lines),
            "external_report": {
                "covered": bool(entries),
                "entries": entries,
                "combined_required_changes": list(dict.fromkeys(required)),
                "current_applicability": status_decision(target),
            },
            "authority_overlays": overlays_for(target),
            "exact_locations": locations,
            "revision_anchor_summary": anchor_summary(locations),
        }
        if not entries:
            if "book on modal triplet" in target["path"].lower():
                paper["external_report"]["coverage_note"] = "Omitted by external report; must receive all corpus-wide corrections and all current authority summaries."
            elif "from_mtt_to_standard_model" in target["path"].lower():
                paper["external_report"]["coverage_note"] = "Omitted by external report; this is a P0 major rewrite because its title, abstract and conclusions claim a full rigorous derivation."
        papers.append(paper)

    return {
        "schema": "MTTCorpusRevisionUpdateLedger.v1",
        "date": "2026-07-11",
        "status": "CONSOLIDATED_FOR_NEXT_VERSION_EDITING_NOT_YET_APPLIED",
        "canonical_authoring_policy": {
            "markdown_root": str(vault),
            "theta_first_pass_override_root": str(theta_corrected),
            "theta_first_pass_override_is_next_revision_base": True,
            "zip_only_sources": [str(p) for p in zip_targets],
            "other_generated_or_repo_copies_are_not_edit_targets": True,
        },
        "counts": {
            "target_papers": len(papers),
            "markdown_papers": len(markdown_files),
            "zip_only_papers": len(zip_targets),
            "theta_first_pass_papers": theta_first_pass_total,
            "theta_first_pass_materially_changed": theta_first_pass_changed,
            "theta_first_pass_copied_unchanged": theta_first_pass_total - theta_first_pass_changed,
            "external_report_paper_entries": len(report_entries),
            "papers_covered_by_external_report": sum(p["external_report"]["covered"] for p in papers),
            "papers_missing_from_external_report": sum(not p["external_report"]["covered"] for p in papers),
            "unmatched_report_entries": len(unmatched_report),
        },
        "authorities": AUTHORITIES,
        "repository_decisions": [
            {"repository": repo, "role": role, "use_rule": rule}
            for repo, role, rule in REPOSITORY_DECISIONS
        ],
        "report_clause_decisions": [
            {"report_scope": scope, "verdict": verdict, "relation_and_action": action}
            for scope, verdict, action in REPORT_CLAUSE_DECISIONS
        ],
        "high_impact_updates": [
            {"paper_family": paper, "exact_locations": locations, "required_update": update, "authorities": authorities}
            for paper, locations, update, authorities in HIGH_IMPACT_UPDATES
        ],
        "external_report_global_decision": {
            "durable": [
                "map typing and right-inverse correction",
                "canonical 4+6 geometry and central-circle bundle convention",
                "fixed-point source repairs and locality hypotheses",
                "probability/Born measure requirements",
                "external Gaussian versus positive spectral-representation guard",
                "all-loop finiteness withdrawal",
                "old 5 TeV chain withdrawal",
                "old nonclosed Iwasawa Chern-class construction withdrawal",
                "calibration/replay/prediction vocabulary",
            ],
            "successor_modified": [
                "Numerical running is no longer simply pending: A02 supplies selected multi-loop SMDR transport at the declared profile tier.",
                "SM parity/profile work is no longer merely a benchmark: A04 closes embedded renormalized-SM equivalence at the declared one-shared-primitive/profile standard.",
                "QFT observable equivalence is closed on the embedded branch by A03, but quantization is imported rather than MTT-derived.",
                "The literal finite Cech witness is closed by A07; the literal global HYM connection remains open.",
                "The finite projected HYM connection is quantitatively stable by A15; only uniform continuum convergence and patchwise control remain before literal global-HYM closure.",
                "A19 consumes the A15 continuum remainder: the exact weighted-theta tail and Wiener contraction close continuum existence/local uniqueness and selected rank-two literal Cech-HYM witnesses 2/2.",
                "The diagonal profile is the declared reproducible baseline by A06; an official joint likelihood remains externally unavailable.",
                "CKM is closed at the selected prediction-with-uncertainty standard by A14; exact equality to a moving central estimator is not an additional physical theorem obligation.",
                "The retarded representative q=79/F/m1 is selected inside its antiunitary orbit by A17; global carrier-measure uniqueness remains open.",
                "A20 proves the neutral minimal-trace boundary formula conditionally fixes m_lightest=0; A21 contracts its three source clauses to one selected complex-symmetric neutral mass operator, A23 advances its source-provenance inventory to 4/8 fields, A24 proves the remaining dimensionful-block normal form with three lawful exits while keeping value rows open, A25 executes the overlap/physical/action gate at 3/9 OK gates and 0/3 accepted exits, A26 promotes neutral projector/Gram readiness to 5/9 OK gates and 6/12 subfields, and A27 closes only the typed L x N^c x H_u structural Gamma_nu carrier with nine 3x3 slots and 7/13 readiness.",
                "A38-A40 complete the neutral two-primitive profile-value route: the common-circle cosine orbit reduces shape to phi_nu, finite rho_E is proved determinant-trivial, and two explicitly declared measured oscillation primitives fill all 36 neutral numerical rows.",
                "A41 proves the exact Lens/Dedekind mixed reciprocity residue 1/240 for the selected retarded pair 16->15. Conditional APS determinant-line identification gives phi_nu=pi/120 and reduces the neutral splitting profile to one scale input, but the operator/counterterm normalization is open and the target-ranked hypothesis is not yet a prediction.",
                "A42 gives a sharply typed conditional absolute-scale candidate: one shared measured E0 fixed through G and the M-theory 11D lift reproduce the A40 neutral amplitude at about 18 ppm. Native MTT is 10D, and the physical neutral-operator lift identification and source law remain open.",
                "A43 conditionally compresses the lifted attenuation to the composite eigenvalue 661/4 and proves the A41 profile denominator is a unit-trace normalization. Native 10D misses by 448^2 in A_nu; lift selection, cost replication, nil saturation and the same-operator Z64/nil bridge remain open.",
                "A44 locks the embedded local-QFT recovery as already closed and proves an exact conditional same-geometry finite-algebra bridge from the three qutrit class lanes to C plus H plus M3(C). Physical projector/lane and weak real-structure selection, representation emission and anomaly execution remain open.",
                "A22 computes the exact E6 Qpsi color anomaly: +12 matter and -12 complete-27 exotics cancel. The naive matter-only/singlet value N_DW=3 is diagnostic only, and the selected flux/threshold anomaly-matching map remains open.",
            ],
            "still_open": [
                "zero-primitive/no-knob empirical derivation",
                "global carrier-measure uniqueness beyond the selected retarded orientation representative",
                "rank-three HYM sector transfer and uniqueness over all HYM branches beyond the closed selected rank-two witness",
                "strict no-knob neutral source selection: A41 supplies the exact 1/240 phase candidate, while A42-A43 supply a conditional 11D-lift E0 candidate at 18 ppm and composite 661/4 reduction; native MTT is 10D and fails this scale, so MTT must first select the physical neutral operator on the lift, then prove APS normalization, nil saturation, cost replication and the common-circle/nil same-operator bridge; ontology/order selection and covariance also remain open",
                "same-geometry generative SM base: A44 closes the conditional qutrit-class-lane algebra reduction but must select its rank-one/rank-two/full projectors and quaternionic weak real structure from native 10D geometry before emitting the chiral representation and anomaly table",
                "selected flux/threshold axion-current anomaly-matching map with nonzero QCD anomaly and quality/EDM control",
                "MTT derivation of quantization/Born/record rules",
                "constructive nonperturbative four-dimensional QFT",
            ],
        },
        "unmatched_report_entries": unmatched_report,
        "papers": papers,
    }


def render_markdown(data: dict) -> str:
    lines = [
        "# MTT Corpus Revision Update Ledger",
        "",
        "**Status:** consolidated for the next-version editing pass; source papers are not modified by this step.",
        "",
        "## Scope and source authority",
        "",
        f"This ledger resolves **{data['counts']['target_papers']} papers**: "
        f"{data['counts']['markdown_papers']} Markdown authoring files and "
        f"{data['counts']['zip_only_papers']} ZIP-only TeX sources. The external report covers "
        f"{data['counts']['papers_covered_by_external_report']} papers; the omitted book and dedicated MTT-to-SM paper are added here.",
        "",
        "The Obsidian corpus is the default Markdown authoring source. The ten Theta/Execution papers are the exception: their next versions must start from the tracked `_md_v3_corrected` first-pass copies, because five contain material repairs not propagated to the vault. Other generated Markdown inside calculation repositories is evidence or conversion output, not a paper-edit target. The index and dedicated MTT-to-SM paper remain ZIP-only and must be revised through `main.tex` or converted before editing.",
        "",
        f"The first Theta pass covered **{data['counts']['theta_first_pass_papers']}/10** papers: **{data['counts']['theta_first_pass_materially_changed']}** were materially corrected and **{data['counts']['theta_first_pass_copied_unchanged']}** were copied unchanged. It corrected claim discipline, selected arithmetic, dimensional conventions and benchmark reproducibility, but retained the 5 TeV calibration and predates A01-A07.",
        "",
        "## Authority order",
        "",
    ]
    for authority in data["authorities"]:
        lines.append(f"- **{authority['id']}** `{authority['path']}`: {authority['claim']}")
    lines += [
        "",
        "## Repository disposition",
        "",
        "| Repository | Role | Publication use rule |",
        "|---|---|---|",
    ]
    for row in data["repository_decisions"]:
        lines.append(f"| `{row['repository']}` | **{row['role']}** | {row['use_rule']} |")
    lines += [
        "",
        "## External report decision",
        "",
        "### Applies unchanged",
        "",
    ]
    lines.extend(f"- {item}" for item in data["external_report_global_decision"]["durable"])
    lines += ["", "### Modified by audited successors", ""]
    lines.extend(f"- {item}" for item in data["external_report_global_decision"]["successor_modified"])
    lines += ["", "### Still open", ""]
    lines.extend(f"- {item}" for item in data["external_report_global_decision"]["still_open"])
    lines += [
        "",
        "### Clause-by-clause applicability",
        "",
        "| Report scope | Verdict | Relation to current theorems and revision action |",
        "|---|---|---|",
    ]
    for row in data["report_clause_decisions"]:
        lines.append(f"| {row['report_scope']} | **{row['verdict']}** | {row['relation_and_action']} |")
    lines += [
        "",
        "## Mandatory paper language",
        "",
        "Use this exact headline for the current numerical result:",
        "",
        "> MTT closes embedded renormalized-Standard-Model equivalence at the adopted one-shared-physical-primitive/profile standard on the selected branch.",
        "",
        "Always append this limitation in the same abstract or conclusion:",
        "",
        "> This is an embedding/parity result with measured profile inputs and imported standard SM quantization. It is not zero-knob derivation, unique observed-branch selection, or a derivation of perturbative quantization from MTT.",
        "",
        "For the old numerical execution chain, state:",
        "",
        "> The former 4.2-5 TeV crossing and dependent threshold calibration are withdrawn. The replacement precision calculation uses the selected SMDR multi-loop transport at Q=Mt with an explicit diagonal measured-input profile.",
        "",
        "For the neutral numerical profile, state:",
        "",
        "> All 36 neutral numerical rows are filled from two explicitly declared measured mass-squared splittings at the normal-ordering Dirac profile with m_lightest=0. This is profile execution, not a strict MTT source derivation of the two primitive values, ontology, ordering or covariance.",
        "",
        "For flux/Iwasawa papers, state:",
        "",
        "> The former nonclosed Iwasawa Chern representative is not used. A finite literal Cech witness, Chern patching, and a selected rank-two continuum HYM representative are now verified by independent successor theorems. Rank-three sector transfer and uniqueness over all HYM branches remain open.",
        "",
        "## Revision order",
        "",
        "1. Patch the Foundation and Fixed-Points spine using the durable corrigendum blocks.",
        "2. Patch map typing, locality, probability and QFT/QG scope before importing numerical successors.",
        "3. Rebuild the dedicated MTT-to-SM paper, Execution I/II, the tiered roadmap and all Theta-Closure papers around A01-A07 and A14-A44.",
        "4. Patch proto-spinor and topology papers so structural encodings are separated from selected numerical outputs.",
        "5. Patch strings/flux papers with the Iwasawa withdrawal plus the A07 finite-Cech, A15 Chern-patching, and A19 selected continuum HYM successors.",
        "6. Update the book and index last so they summarize only revised papers.",
        "",
        "## High-impact replacement matrix",
        "",
        "| Paper or family | Exact locations | Required update | Authority |",
        "|---|---|---|---|",
    ]
    for row in data["high_impact_updates"]:
        lines.append(
            f"| {row['paper_family']} | {row['exact_locations']} | {row['required_update']} | {row['authorities']} |"
        )
    lines += [
        "",
        "## Per-paper update map",
        "",
    ]
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in data["papers"]:
        grouped[paper["group"]].append(paper)
    for group in sorted(grouped):
        lines += [f"### {group}", ""]
        for paper in sorted(grouped[group], key=lambda item: item["name"]):
            report_entries = paper["external_report"]["entries"]
            dispositions = ", ".join(filter(None, (e["disposition"] for e in report_entries))) or "ADD TO REVISION PLAN"
            priorities = ", ".join(filter(None, (e["priority"] for e in report_entries))) or "P0/P1 review"
            lines += [
                f"#### `{paper['name']}`",
                "",
                f"- **Source:** `{paper['path']}` ({paper['source_kind']}, {paper['line_count']} lines)",
                f"- **Disposition / priority:** {dispositions}; {priorities}",
                f"- **Current decision:** {paper['external_report']['current_applicability']}",
                f"- **Authority overlays:** {', '.join(paper['authority_overlays'])}",
                "- **Exact edit anchors:** " + ("; ".join(paper["revision_anchor_summary"]) or "title, abstract/front matter and conclusion"),
            ]
            note = paper["external_report"].get("coverage_note")
            if note:
                lines.append(f"- **Coverage note:** {note}")
            changes = paper["external_report"]["combined_required_changes"]
            if changes:
                lines.append("- **Required changes:**")
                lines.extend(f"  - {change}" for change in changes)
            lines.append("")
    lines += [
        "## Validation before editing is declared complete",
        "",
        "- Every revised paper must have a new version filename and an explicit supersedes note.",
        "- Every numerical table must cite a packet/certificate and state whether it is source-derived, profile/replay, calibration or held-out prediction.",
        "- No historical `open` packet may override A01-A07 or A14-A44; no successor may erase its own scope guard.",
        "- Run the relevant repository verifier and a corpus-wide search for the corrigendum patterns after each revision group.",
        "- Update the book and index only after all paper revisions pass their checks.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--tex-root", type=Path, default=DEFAULT_TEX_ROOT)
    parser.add_argument("--theta-corrected", type=Path, default=DEFAULT_THETA_CORRECTED)
    parser.add_argument("--json-output", type=Path, default=Path("revision_update_ledger.json"))
    parser.add_argument("--markdown-output", type=Path, default=Path("MTT_CORPUS_REVISION_UPDATE_LEDGER_2026-07-11.md"))
    args = parser.parse_args()
    data = build(args.report, args.vault, args.tex_root, args.theta_corrected)
    args.json_output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.markdown_output.write_text(render_markdown(data) + "\n", encoding="utf-8")
    print(json.dumps(data["counts"], indent=2))


if __name__ == "__main__":
    main()
