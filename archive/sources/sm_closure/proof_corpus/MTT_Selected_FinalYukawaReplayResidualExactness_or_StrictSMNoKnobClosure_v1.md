# MTT Selected FinalYukawaReplayResidualExactness or StrictSMNoKnobClosure v1

Status: `MTT_SELECTED_FINALYUKAWAREPLAYRESIDUALEXACTNESS_BUILT_FINITE_REPLAY_YUKAWA_CLOSED_TRUE_SM_OPEN`

## Tail Rows

After the strict q64/s_beta phase-antisymmetry scalar, two finite tail rows are
emitted.

Endpoint-conjugate row:

`[27,6,-26]` with coefficient

`epsilon_theta * s_beta^2 * (q64+1)/(q64*q_mod) = 9.826390233522832e-11`.

Z7 mixed row:

`[0,1,-21/5]` with coefficient

`epsilon_theta * s_beta^3 / (q64*7-q7) = 1.883666766188459e-12`.

Neither coefficient is fitted from the residual.

## Replay Result

The final max log residual is

`8.715792346058762e-14`.

The imported selected HYM replay floor is

`8.208178923714022e-13`.

The final residual/floor ratio is

`0.10618423924554335`.

Therefore finite-replay Yukawa magnitude exactness is accepted for the current
finite projected source standard.

## Guardrail

This is not analytic zero residual, and it is not global true SM no-knob
closure.  It closes the Yukawa magnitude replay layer at the finite projected
source/replay standard.  The global ledger still has non-Yukawa rows to audit.

Next required artifact: `MTT_Selected_TrueSMNoKnobClosure_GlobalLedger_or_RemainingNonYukawaRows_v1`.
