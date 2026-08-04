# MTT Selected PhaseLaneCurvatureClue or YukawaReductionDiagnostic v1

Status: `MTT_SELECTED_PHASELANECURVATURECLUE_OR_YUKAWAREDUCTIONDIAGNOSTIC_BUILT_FITTED_CLUE_SOURCE_OPEN`

This is a fitted diagnostic, not a selected-source proof.

## Finding

The earlier blanket statement "all charged sectors are second order" is only
an interpolation-domain statement.  The more physical clue is lane-specific:

- phase lane: `u,e` via `phase_packet_I_plus_Z`
- shift lane: `d` via `shift_packet_I_plus_X`

The fitted quadratic curvatures are:

- `c2_u = -2.7988392926293733`
- `c2_e = -2.7938246889934457`
- `c2_d = -0.7646877778512665`

The phase-lane average is

`gamma_phase = -2.7963319908114093`

with

`c2_u - c2_e = -0.005014603635927539`.

Forcing `u` and `e` to share one phase curvature gives worst multiplicative
Yukawa error

`1.0015089908530137`.

The shift-lane curvature ratio is

`c2_d / gamma_phase = 0.27346101262796685`

whose best small rational with denominator <= 40 is `3/11`.  The
seven-parameter model

`c2_u = c2_e = gamma`, `c2_d = (3/11) gamma`

has worst multiplicative Yukawa error

`1.0016714760085947`.

## Decision

This rejects the simple "quarks only are second order, leptons are first order"
fit on the current selected family spectrum.  The better clue is:

`phase packet = strong second-order curvature`

`shift packet = weaker curvature close to 3/11 of phase curvature`

This can reduce the fitted charged-Yukawa description from 9 exact coefficients
to a very accurate 7-parameter near-law, but it is not exact and it uses the
observed/profile Yukawa rows as fitted data.  It must not be promoted as a
no-knob result until the ratio and curvature are emitted by selected MTT source
data before empirical replay.

Next required artifact: `MTT_Selected_PhaseLaneCurvatureSourceRelation_or_SevenParameterYukawaReduction_v1`.
