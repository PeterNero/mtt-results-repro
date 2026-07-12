# MTT Selected MagProfileSourceScalar or OfficialFullProfileWorkspace v1

Status: `MTT_SELECTED_MAGPROFILESOURCESCALAR_OR_OFFICIALFULLPROFILEWORKSPACE_BUILT_PHASE_SOURCE_PROMOTED_MAGNITUDE_REPLAY_LOCKED`

## Promotion

The older `M_magprofile` gate said the phase split scalar was still unselected.
That is now superseded by the audited strict phase-antisymmetry theorem.

The selected source scalar is

`delta_c2 = -((q64+1)/q64) * s_beta = -0.005014489499673223`.

It uses only selected inputs: the q79/q64 central-circle branch, the retarded
overlap family, charged HYM/Strominger overlap rows, the charged-lepton
transpose sign, and the selected HYM projection scalar `s_beta`.

Thus one internal source scalar row is promoted, and the fitted
`c2_u-c2_e` split is retired as source data.

## Still Open

This does not reopen Yukawa magnitude closure.  The finite-replay Yukawa
magnitudes are already closed and locked at 9/9, with

`max |log residual| = 8.715792346058762e-14`.

The intermediate strict phase-scalar-only replay had left

`max |log residual| = 7.959463247076742e-09`.

That intermediate residual is consumed by the later finite-tail replay closure,
so it is not an active blocker.

The still-open layer is stronger: promote the full `M_magprofile` value
functional/source-payload rows, or import an official full-profile workspace.
That means one of:

- a full `M_magprofile` value functional emitting all ten magnitude-bearing
  rows before replay values enter,
- an official full-profile workspace.

Next required artifact:
`MTT_Selected_MagProfileValueFunctional_or_OfficialFullProfileWorkspace_v1`.
