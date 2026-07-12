# MTT Selected CharmCRunDecInputPolicy or RThetaMassSchemeDerivation v1

Status: `MTT_SELECTED_CHARMCRUNDECINPUTPOLICY_OR_RTHETAMASSSCHEMEDERIVATION_BUILT_POLICY_SWEEP_NO_SELECTED_REPAIR`.

This artifact tests whether the BCT profile wall is only a charm CRunDec input
policy issue.

```text
current EFT profile p-value       : 0.02386956100195133
best grid charm mass              : 0.6719738598372106 GeV
best grid EFT profile p-value     : 0.07280094084234212
best grid selected                : false
table substitution profile p-value: 0.999993614860048
selected Rtheta rows closed       : false
```

The sweep finds repair candidates, but selecting the best one by residual would
be target fitting.  The next step must either explicitly choose empirical table
substitution as a non-no-knob profile layer, prove an independent CRunDec policy,
or derive the selected Rtheta rows.

Next artifact: `MTT_Selected_CharmTableSubstitution_or_SelectedRThetaRowsDecision_v1`.
