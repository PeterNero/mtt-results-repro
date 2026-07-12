# MTT Selected AcceptedCommonScaleYukawaHiggsValues or ProfileLikelihoodExecution v1

Status: `MTT_SELECTED_ACCEPTEDCOMMONSCALEYUKAWAHIGGSVALUES_OR_PROFILELIKELIHOODEXECUTION_BUILT_VERSIONED_VALUES_AND_DIAGONAL_PROFILE_TRUE_EQUIVALENCE_OPEN`.

This artifact emits a versioned first-pass common-scale value packet:

```text
diag |Y_u(M_Z)| = [1.2914999471632702e-05, 0.007611476301629308, 1.02542721110437]
diag |Y_d(M_Z)| = [2.736712969930453e-05, 0.0005439508030307285, 0.02513014119878465]
diag |Y_e(M_Z)| = [2.915915642758639e-06, 0.0006029188694533759, 0.010139711484906938]
lambda_H(M_Z)  = 0.1470187677924554
```

It also attaches the diagonal profile execution:

```text
reduced chi2 = 1.000532029822045
max pull     = 2.2180357930900985
coarse pass  = True
```

Promotion decision:

```text
accepted as versioned value/profile packet: true
accepted for SM-parity replay: True
accepted for true precision equivalence: false
true SM equivalence: open
```

This does not promote first-pass values to true precision equivalence. The missing
rows are threshold matching, mass-scheme conversion, full correlated profile
likelihood, multi-loop convention values, and no-knob value-source derivation.

Next artifact: `MTT_Selected_CorrelatedThresholdProfileMatrix_or_YukawaHiggsPrecisionPromotion_v1`.
