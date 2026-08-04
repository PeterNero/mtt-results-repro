# Selected U1/SU2 Source Response or Normalization Index Run v1

## Result

The normalization-index run has now been executed as a discovery-only scan.
It does not close electroweak coupling prediction.

The strongest source-motivated near hit remains:

```text
complex_nesting_or_shared_circle_2_3
residual = 0.03217098750290326
```

The strongest bounded rational target-near hit is:

```text
U1 = 20/23
SU2 = 2/17
residual = 1.4346814772636662e-05
```

That hit is rejected as proof data because it is target-discovered and has no
current source selector.

## Input Pieces

```text
U1 circle finite part = 2.442340583291322
SU2 effective sphere finite part = -0.5980970589159109
diagnostic target lambda_12 = 2.194153126940556
target role = diagnostic witness only, not an input to selection
```

## Source-Prior Candidates

- `GUT_hypercharge_3_5`: U1=3/5, SU2=1/1, lambda_12=2.0635014088907, residual=0.130652, source_prior=SOURCE_MOTIVATED_NOT_SELECTED
- `complex_nesting_or_shared_circle_2_3`: U1=2/3, SU2=1/1, lambda_12=2.22632411444346, residual=0.032171, source_prior=MOTIVATED_BY_PRIOR_DISCUSSION_NOT_SOURCE_SELECTED

## Bounded Rational Scan

- #1: U1=20/23, SU2=2/17, lambda_12=2.19413878012578, residual=1.43468e-05
- #2: U1=9/14, SU2=24/23, lambda_12=2.19417736812748, residual=2.42412e-05
- #3: U1=5/9, SU2=7/5, lambda_12=2.19419176208857, residual=3.86351e-05
- #4: U1=11/19, SU2=30/23, lambda_12=2.19411325207042, residual=3.98749e-05
- #5: U1=5/11, SU2=29/16, lambda_12=2.19420572987205, residual=5.26029e-05
- #6: U1=11/21, SU2=26/17, lambda_12=2.19405793625648, residual=9.51907e-05
- #7: U1=10/17, SU2=19/15, lambda_12=2.19426053930799, residual=0.000107412
- #8: U1=7/8, SU2=2/21, lambda_12=2.19400963503857, residual=0.000143492

## Source Obstructions

- `hypercharge_interface_status` = SELECTED_HYPERCHARGE_NORMALIZED_THRESHOLD_INTERFACE_BUILT_VALUES_OPEN
- `hypercharge_determinant_amplitudes_selected` = False
- `operator_block_status` = QA_QC_SU2_OPERATOR_BLOCK_SCAFFOLD_BUILT_VALUES_OPEN
- `selected_operator_values_closed` = False
- `selected_spectra_closed` = False
- `c1_interface_status` = PEW_ALPHA1_RESPONSE_INTERFACE_BUILT_VALUES_OPEN
- `numeric_electroweak_closure` = False

## Decision

```text
normalization_index_run_executed = true
promotable_index_found = false
I_1_filled = false
I_2_filled = false
K_gauge_filled = false
measured_electroweak_closure = false
can_close_now = false
```

Reason:

```text
All close rational indices are target-discovered or source-motivated only; no current source selects the U1/SU2 threshold weights, spectra, or K_gauge.
```

## Guardrails

- Do not promote the best rational scan hit without source selection.
- Do not promote 2/3 from numerical closeness or informal complex-nesting intuition.
- Do not promote 3/5 unless the MTT branch selects GUT-style hypercharge normalization as the threshold weight.
- Do not compare to measured electroweak closure until selected spectra, weights, mu_match, and RGE scheme are supplied.

## Next Required Object

```text
Selected_U1_SU2_Threshold_Index_Source_Selector_or_Operator_Spectrum_v1
```
