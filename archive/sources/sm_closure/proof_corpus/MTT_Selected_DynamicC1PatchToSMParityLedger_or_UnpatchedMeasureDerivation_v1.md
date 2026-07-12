# MTT Selected DynamicC1PatchToSMParityLedger or UnpatchedMeasureDerivation v1

Status: `MTT_SELECTED_DYNAMICC1PATCHTOSMPARITYLEDGER_OR_UNPATCHEDMEASUREDERIVATION_BUILT_PATCHED_LEDGER_UPDATED`.

The patched dynamic C1 closure is now imported into the SM-parity ledger layer:

```text
patched dynamic C1 no longer blocks parity = True
patched A_selected                         = [[12.0, 0.0], [0.0, 12.0]]
patched b_selected                         = [12.0, 12.0]
patched deltaTheta_C1                      = [1.0, 1.0]
full SM parity closed now                  = False
unpatched no-knob dynamic C1 closed        = False
```

This is a meaningful SM-parity checkpoint, not a no-knob claim. The next step is
to integrate this with the final empirical/replay ledger and keep the unpatched
measure derivation as a separate upgrade target.

Next artifact: `MTT_Selected_PatchedDynamicC1EmpiricalReplayIntegration_or_NoKnobDerivation_v1`.
