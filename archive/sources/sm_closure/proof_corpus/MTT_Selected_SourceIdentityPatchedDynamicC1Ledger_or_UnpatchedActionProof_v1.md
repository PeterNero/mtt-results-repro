# MTT Selected SourceIdentityPatchedDynamicC1Ledger or UnpatchedActionProof v1

Status: `MTT_SELECTED_SOURCEIDENTITYPATCHEDDYNAMICC1LEDGER_OR_UNPATCHEDACTIONPROOF_BUILT_PATCHED_LEDGER_STRENGTHENED`.

The strengthened dynamic C1 ledger now imports both sides of the patched/local result:

```text
strict source rows validated       = True
primitive/source rows              = 72
sector rows                        = 36
hessian/source rows                = 2
patched A_selected                 = [[12.0, 0.0], [0.0, 12.0]]
patched b_selected                 = [12.0, 12.0]
patched deltaTheta_C1              = [1.0, 1.0]
full SM parity closed now          = False
unpatched no-knob dynamic C1 closed = False
```

So dynamic C1 is no longer a patched SM-parity source-or-value blocker. The remaining no-knob upgrade is still the unpatched selected-action proof.

Next artifact: `MTT_Selected_FinalIntegratedSMParityReplayAfterSourceIdentityPatch_v1`.
