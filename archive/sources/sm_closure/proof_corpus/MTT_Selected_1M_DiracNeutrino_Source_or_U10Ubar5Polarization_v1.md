# MTT Selected 1_M DiracNeutrino Source or U10/Ubar5 Polarization

Status: `MTT_SELECTED_1M_DIRAC_SOURCE_OR_U10UBAR5_POLARIZATION_GATE_BUILT_SOURCE_PROMOTION_OPEN`

This artifact attempts the next source-promotion gate after the structural
`1_M` Dirac-neutrino rule.

## Route A: SU(5)/E6 Polarization

Route A is the primary route.  The q79 finite transversality certificate gives,
under a selected-source hypothesis:

- `U_10 = I_3`,
- `U_bar5 = F`,
- retarded q79 orientation rather than the conjugate branch.

Together with the E6/SU(5) dictionary, this structurally gives:

- `10_M` clock/phase side: `u,e`,
- `bar5_M` shift side: `d`,
- `1_M=N^c` Dirac-neutrino shift side: `nuD`.

This route does not close yet because the selected source that emits the
ordered `10_M/bar5_M/1_M` packet is still absent.

## Route B: HYM / Zero-Mode Projectors

Route B tries to derive the same sector partition from selected zero-mode
projectors and the selected sector source map `rho_s`.  The current repo has
strong finite support: model-active projectors, ordered basis ids, rank/gap
checks, and End0 equivariance.  But these values are not yet promoted as
selected HYM/Strominger projectors, so this route also remains open.

## What This Achieves

The remaining proof object is now precise:

`Selected same-branch source emission of U_10, U_bar5, and the 1_M Dirac shift rule`.

The source must emit the sector route `u,e | d,nuD` and the overlap/transfer
normalization from the same branch.  Conditional transversality, model-active
projectors, diagnostic lifted flags, observed constants, and locked splitter
columns cannot promote the result.

Next artifact: `MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1`.
