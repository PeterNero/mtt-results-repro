# MTT Selected PhaseLaneCurvatureResidualExactness or SourceCorrectionRows v1

Status: `MTT_SELECTED_PHASELANECURVATURERESIDUALEXACTNESS_OR_SOURCECORRECTIONROWS_BUILT_RANK1_SHAPE_INTEGER_CLUE_SOURCE_OPEN`

## Shape Theorem

The residual left by the seven-parameter curvature skeleton factors exactly as

`R_s,g = eta_s Q_g`

with

`Q = [-2, 3, -1]`.

This is not arbitrary.  `Q` is the affine-family complement on the selected
family spectrum: it has zero sum and zero dot product with the selected family
eigenvalues.  The max factorization error is
`8.142791996235133e-15`.

The fitted sector amplitudes are:

- `eta_u = 0.0004485420978386969`
- `eta_d = 0.00039655532120673264`
- `eta_e = -0.0005566935490755677`

## Compression Clues

The one-amplitude quark/lepton sign correction

`rho [1,1,-1] outer Q`

reduces the remaining worst multiplicative error to
`1.0002683256720037`.

The sharper small-integer correction

`rho [17,15,-21] outer Q`

reduces it to
`1.0000035565511363`.

This is an extremely strong fitted clue, but it is not a source theorem.

## Decision

Closed now:

- residual rank-1 structure,
- family-shape correction channel `Q=[-2,3,-1]`,
- exact reduction of the correction problem to sector amplitudes.

Still open:

- source derivation of `gamma`,
- source derivation of the `3/11` curvature ratio,
- source derivation of either `eta_s` or the one-amplitude integer sector
  vector `[17,15,-21]` plus `rho`.

Next required artifact: `MTT_Selected_SourceIntegerSectorAmplitudeTheorem_or_GammaCorrectionRows_v1`.
