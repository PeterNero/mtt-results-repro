# MTT Selected MagnitudeBearingProjectionWeights or ThresholdRowsDerivation v1

Status: `MTT_SELECTED_MAGNITUDEBEARINGPROJECTIONWEIGHTS_OR_THRESHOLDROWSDERIVATION_BUILT_DIAGNOSTIC_BACKSOLVE_RANK_GAP_THRESHOLD_ROWS_OPEN`.

This artifact executes the diagnostic magnitude-weight backsolve and proves the
rank gap.

```text
diagnostic magnitude table emitted        : true
diagnostic table accepted as selection    : false
rank gap theorem proved                   : true
magnitude-bearing weights closed          : false
Yukawa magnitudes no-knob closed          : false
```

The selected source-normalized layer has rank `2` and
`4` typed source slots.  The charged diagonal Yukawa
layer has `9` generation-resolved magnitude rows, plus
`lambda_H`.  So the current source weights cannot determine the magnitude layer
without additional generation-resolved threshold/mass-scheme/profile source
rows.

Next artifact: `MTT_Selected_GenerationResolvedThresholdSourceRows_or_ProfileConventionClosure_v1`.
