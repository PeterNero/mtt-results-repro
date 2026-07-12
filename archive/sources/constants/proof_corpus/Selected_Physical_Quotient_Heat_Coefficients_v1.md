# Selected Physical Quotient Heat Coefficients v1

## Purpose

The physical quotient scan found one non-accidental-looking clue: adjoint
Casimir weights move the hypercharge-normalized weak split much closer to the
diagnostic electroweak witness.  This note computes that clue as a conditional
heat-coefficient model and records exactly why it is not yet closure.

## Calculator

```text
scripts/compute_selected_physical_quotient_heat_coefficients.py
```

The model uses the heat-coefficient weights:

```text
Q_a / SU3 stack       C_A(SU3) = 3
Q_c / circle stack    normalized abelian trace = 1
SU2 stack             C_A(SU2) = 2
```

These are source-motivated because gauge one-loop determinants carry
representation and trace factors.  The local corpus already says that the
final coupling thresholds are execution-level computations, not values already
present in the papers.  It also records that the selected local determinant
interface must include multiplicities and representation/index weights.

## Computation

The current base stack values are:

```text
p_a    =  7.291801913769811
p_c    =  2.442340583291322
p_SU2  = -0.5980970589159109
```

After the conditional heat weights:

```text
p_a    = 21.875405741309436
p_c    =  2.442340583291322
p_SU2  = -1.1961941178318218
```

The hypercharge accounting is unchanged:

```text
p_Y       = p_a/36 + p_c/4
lambda_12 = p_Y - p_SU2
Delta_G12 = v1_tilde lambda_12 / (4 pi)
```

This gives:

```text
p_Y       = 1.218235305303648
lambda_12 = 2.41442942313547
Delta_G12 = 0.07793413589076988
```

Compared with the diagnostic C1 witness:

```text
target lambda_12   = 2.194153126940556
residual lambda_12 = 0.22027629619491407
```

## Interpretation

This is stronger than the previous proxy table because the correction has the
right type: a gauge heat-kernel trace/index factor, not a universal
normalization knob.  It also preserves the hypercharge embedding:

```text
p_Y = p_a/36 + p_c/4.
```

However, it is not closure.  The weights are not selected by the MTT physical
quotient in the current proof corpus.  They are the natural Casimir candidate
that the final operator derivation should either prove, modify, or reject.

## Required Next Gate

The next gate is:

```text
Selected_Gauge_Threshold_Operator_Heat_Kernel_Theorem_v1
```

It must derive, without using measured electroweak data as input:

```text
1. the heat coefficients for Q_a, Q_c, and SU2,
2. the finite stack determinants in the same physical quotient,
3. the retarded-kernel derivative/normalization used by the C1 response.
```

Only then can the residual be evaluated as a theorem rather than as candidate
proximity.

## Verdict

The conditional Casimir heat-coefficient model is computed and audited.

It is not a new no-knob electroweak prediction.

Remaining blocker:

```text
derive the selected heat coefficients and stack determinants from the actual
gauge-threshold operator and physical quotient.
```
