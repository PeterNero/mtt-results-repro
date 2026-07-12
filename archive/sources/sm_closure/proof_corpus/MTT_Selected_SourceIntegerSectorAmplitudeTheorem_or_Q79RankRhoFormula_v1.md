# MTT Selected SourceIntegerSectorAmplitudeTheorem or Q79RankRhoFormula v1

Status: `MTT_SELECTED_SOURCEINTEGERSECTORAMPLITUDETHEOREM_BUILT_Q79_RANK_RHO_FORMULA_PPM_EXACTNESS_OPEN`

## Derived Source Form

The q79 branch supplies `q64=15`, `q7=2`, and `q=448`.  The qutrit
packet supplies carrier rank `3` and quotient-projector rank
`2`.

These selected integers reconstruct the fitted correction vector exactly:

`[17,15,-21] = [q64+q7, q64, -(q64+carrier_rank*q7)]`.

They also reconstruct the previous curvature-ratio clue:

`3/11 = carrier_rank/(q64-projector_rank*q7)`.

The strongest scalar source candidate found is

`rho = epsilon_theta * s_beta * carrier_rank * projector_rank * q64^2 / q`

which gives

`rho = 2.6454590873348714e-05`.

The previous fitted value was `2.6454565457534828e-05`, so the relative difference is
`9.60734506394445e-07`.

## Execution

Using the source-formula `rho` and the sector vector above leaves:

- max log residual: `3.5578410246936334e-06`
- worst multiplicative Yukawa error: `1.0000035578473538`

That is essentially the same ppm-level residual as the fitted integer trial, but
now the vector, the `3/11` ratio, and `rho` all come from the same selected
q79/qutrit/theta/Higgs finite-reduction data.

## Guardrail

This is not yet full strict Yukawa closure.  The finite projected
curvature-amplitude law is constructed here as the exact next theorem target;
it still needs an independent same-source HYM/variational derivation or an
exactness/error certificate for the remaining ppm residual.

Next required artifact: `MTT_Selected_FiniteProjectedCurvatureAmplitudeLaw_or_YukawaExactnessClosure_v1`.
