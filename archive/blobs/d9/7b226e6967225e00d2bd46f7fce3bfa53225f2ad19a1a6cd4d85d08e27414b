# Selected Qa Qc SU2 Operator Spectra or Heat Coefficients v1

## Purpose

The previous artifact built the operator block scaffold for:

```text
D_Qa, D_Qc, D_SU2.
```

This note carries forward the best current spectrum/heat data for those
blocks.  Qc and SU2 are now selected for weak-split accounting; Qa remains a
diagnostic SU3/Nil proxy.

## Calculator

```text
scripts/compute_selected_qaqcsu2_operator_spectra_or_heat_coefficients.py
```

## Current Candidate Table

### D_Qa

Status:

```text
DIAGNOSTIC_SU3_NIL_PROXY_NOT_SELECTED
```

Current unweighted finite-part candidate:

```text
p_a = 7.291801913769811.
```

With the conditional heat coefficient:

```text
C_A(SU3)=3,
p_a -> 21.875405741309436.
```

This remains the weak point.  It still depends on the proxy SU3/Nil
finite-part estimator, not an exact selected compact Nil or gauge-threshold
determinant.

### D_Qc

Status:

```text
SELECTED_QC_CIRCLE_GAUGE_BLOCK_ZETA_CLOSED_FOR_WEAK_SPLIT
```

The selected Qc circle gauge block is closed for weak-split accounting:

```text
p_c = 2 log(2 pi R1)
    = 2.442340583291322.
```

This uses three facts:

```text
Tr(T^2)=1,
abelian Faddeev-Popov ghosts decouple,
the q79 selected circle zeta determinant is exact.
```

What remains for Qc is only an absolute universal determinant normalization,
which is irrelevant to `lambda_12`.

### D_SU2

Status:

```text
SELECTED_SU2_SPHERE_GAUGE_BLOCK_ZETA_CLOSED_FOR_WEAK_SPLIT
```

The scalar-proxy sphere determinant is exact:

```text
p_SU2 = -4 zeta_R'(-1) + (2/3) log((f2 R_lens)^2)
       = -0.5980970589159109.
```

With the conditional heat coefficient:

```text
C_A(SU2)=2,
p_SU2 -> -1.1961941178318218.
```

This is now selected for weak-split accounting because:

```text
1. Theta II and Theta III select the flat/trivial constant SU2 threshold
   background at leading order,
2. the nonabelian FP operator reduces to -Delta_0 tensor ad(SU2),
3. the flat adjoint FP determinant is field-independent and is discarded or
   absorbed as quotient-measure normalization for gauge-kinetic thresholds.
```

What remains for SU2 is only absolute partition-function/vacuum normalization,
which is irrelevant to `lambda_12`.

## Candidate Hypercharge Accounting

Using the conditional heat-weighted candidate table:

```text
p_a   = 21.875405741309436
p_c   =  2.442340583291322
p_SU2 = -1.1961941178318218
```

gives:

```text
p_Y       = p_a/36 + p_c/4
          = 1.218235305303648
lambda_12 = p_Y - p_SU2
          = 2.41442942313547.
```

Against the diagnostic C1 witness:

```text
target lambda_12 = 2.194153126940556
residual         = 0.22027629619491407.
```

This comparison remains diagnostic only.

## What This Achieves

The live determinant problem is now localized:

```text
1. D_Qc and D_SU2 have exact zeta values.
2. D_Qc is now selected for weak-split accounting.
3. D_SU2 is now selected for weak-split accounting.
4. D_Qa/SU3/Nil does not yet have an exact selected zeta value.
5. The full physical quotient is still open because Qa/SU3/Nil is not selected.
```

## Verdict

The spectra/heat candidate table is built.

It is not electroweak closure.

The next true gate is:

```text
Exact_Selected_Nil_or_Gauge_Threshold_Heat_Coefficients_v1.
```
