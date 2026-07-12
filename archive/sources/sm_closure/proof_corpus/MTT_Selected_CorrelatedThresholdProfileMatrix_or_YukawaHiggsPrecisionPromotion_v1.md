# MTT Selected CorrelatedThresholdProfileMatrix or YukawaHiggsPrecisionPromotion v1

Status: `MTT_SELECTED_CORRELATEDTHRESHOLDPROFILEMATRIX_OR_YUKAWAHIGGSPRECISIONPROMOTION_BUILT_SURROGATE_MATRIX_PRECISION_PROMOTION_OPEN`.

This artifact emits a surrogate correlated threshold/profile matrix family for
the independent weak-scale boundary basis:

```text
['lambda_Mt', 'y_t_Mt', 'g_2_Mt', 'g_Y_Mt', 'g_3_Mt']
```

The redundant hypercharge row `g_1_GUT_Mt` is removed because it is exactly
derived from `g_Y_Mt`. The declared stress matrices are positive definite:

```text
all positive definite = True
core reduced chi2 max = 2.4418973723143726
```

Promotion decision:

```text
surrogate precision scaffold closed: true
accepted for true precision equivalence: false
true SM equivalence: open
```

The remaining wall is real source data, not matrix arithmetic: threshold
matching values, mass-scheme conversions, a published/reconstructed profile
likelihood, multi-loop convention values, or a no-knob MTT derivation of those
same rows.

Next artifact: `MTT_Selected_ThresholdMassSchemeValues_or_CorrelatedLikelihoodSourceImport_v1`.
