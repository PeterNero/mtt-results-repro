# Theta/Execution TeX Revision Manifest

Date: 2026-07-11

## Source Policy

The original ZIP files, `_work` TeX projects, `_md` conversions, and
`_md_v3_corrected` first-pass papers are immutable inputs to this revision.
All edits are made only in `revised_tex_vnext`.

For each paper, the revision order is:

1. read the original TeX section in context;
2. preserve every applicable correction from `_md_v3_corrected`;
3. remove the obsolete 4.2--5 TeV crossing/closure interpretation;
4. import only theorem rows accepted by the current authority ledger;
5. distinguish source theorem, conditional theorem, profile/replay,
   calibration, diagnostic, and held-out prediction;
6. compile and run claim/provenance checks before packaging a new ZIP.

## Version Map

| Previous project | New project | First-pass status |
|---|---|---|
| `A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v2` | `A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v3` | copied unchanged in first pass |
| `Superset_Determinations_in_Modal_Triplet_Theory_v2` | `Superset_Determinations_in_Modal_Triplet_Theory_v3` | copied unchanged in first pass |
| `Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2` | `Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v3` | copied unchanged in first pass |
| `Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2` | `Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v3` | materially corrected; preserve benchmark and Higgs fixes |
| `Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v2` | `Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v3` | copied unchanged in first pass |
| `Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry` | `Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry_v2` | materially corrected; preserve calibration language and arithmetic |
| `Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps` | `Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps_v2` | materially corrected; preserve dimensional and lens-layer clarification |
| `Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization` | `Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization_v2` | copied unchanged in first pass |
| `Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale` | `Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale_v2` | materially corrected; preserve conditional cosmology language |
| `Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle` | `Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle_v2` | materially corrected; preserve round-trip/non-circular split and scan fix |

## Current Numerical Authority

- The former 4.2--5 TeV gauge crossing is withdrawn.
- The selected replacement is SMDR v1.3 multi-loop matching/running at
  `Q=M_t=172.5590883453979 GeV`.
- The common-scheme gauge rows are
  `g_Y=0.3585945042245627`, `g_2=0.6475986707537685`, and
  `g_3=1.1634274089369543`.
- The full selected precision object has 8 rows, a positive-definite `8x8`
  covariance, 36/36 symmetric entries, and 15/15 BCT--WZH cross entries.
- The diagonal measured-input profile is the declared reproducible baseline;
  no official joint 15-coordinate likelihood is claimed.

## Current Closure Language

Permitted headline:

> MTT closes embedded renormalized-Standard-Model equivalence at the adopted
> one-shared-physical-primitive/profile standard on the selected branch.

Required adjacent limitation:

> This is an embedding/parity result with measured profile inputs and imported
> standard SM quantization. It is not zero-knob derivation, unique
> observed-branch selection, or a derivation of perturbative quantization from
> MTT.

## Authority Files

The authority identifiers and absolute paths are maintained in
`../MTT_CORPUS_REVISION_UPDATE_LEDGER_2026-07-11.md`. In this batch the primary
sources are A01--A07, with A11--A13 used only for q79 and scoped GR-TT claims.

## Revision Progress

| Project | Current result |
|---|---|
| Theta Closure I v2 | Multi-loop common-scheme profile transport inserted; overlap targets and covariance recomputed; obsolete gap/QG/cosmology scale chain removed |
| Theta Closure II v2 | Route-A geometry retargeted to the new profile; first-pass dimensional/lens clarification preserved; result classified as calibrated ansatz-level existence |
| Theta Closure III v2 | Obsolete profile replaced; Route-B result reclassified as a conditional representation-level cross-check; all shared Route-A inputs and the normalization bridge made explicit |
| Theta Closure IV v2 | Dimensionless volume coefficient updated and physical length restored; Newton prediction demoted to conditional scaling; obsolete few-TeV tensor bound withdrawn and tensor formula renormalized |
| Theta Closure V v2 | Weak-angle relation reduced to its exact same-scale identity; selected Mt-scale value emitted; former 5 TeV prediction withdrawn; genuine held-out source criterion stated |
| Execution I v3 | Rebuilt from current A01--A22 authority: gauge/precision, selected rank-two HYM, internal K-threshold, admitted physical rows, and strong-CP status separated; obsolete CY benchmark retired |
| Execution II v3 | Rebuilt from current charged-flavor, CKM, Higgs and A30--A31 neutral authorities; fitted matrices retired; profile-standard closure separated from strict magnitude/neutrino source frontier |
| Superset Determinations v3 | Rebuilt as the parameter-identifiability ledger; obsolete crossing/zeta/K/minimum-threshold/alpha-s chain retired; claim classes and strict-upgrade accounting installed |
| Geometry-Light v3 | Exact identities separated from assumptions and phenomenological bounds; principal-symbol wave-speed condition and no-internal-gap-cutoff guard added |
| Tiered Roadmap v3 | Rebuilt as the audited non-looping master status with the 12/12 profile baseline, nine strict upgrades, named next objects, and reproducibility contract |
| Batch status | All ten versioned TeX projects contextually revised; compilation and final packaging remain |
