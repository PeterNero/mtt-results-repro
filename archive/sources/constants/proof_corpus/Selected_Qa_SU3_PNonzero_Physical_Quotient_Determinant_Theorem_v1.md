# Selected Qa/SU3 PNonzero Physical Quotient Determinant Theorem

## Purpose

This note closes the nonzero-central-momentum quotient rule for the compact Nil
Qa/SU3 determinant attempt.

The previous gates established:

```text
p0 ghost/measure correction = 0
Weitzenbock E is already included in the sourced Hodge one-form spectrum
```

So the remaining question is the `p != 0` BRST physical determinant.

## Selected Rule

For `p != 0`, the Nil Hodge complex is acyclic: there are no harmonic zero
modes in the central oscillator sector.  The BRST quotient therefore selects:

```text
longitudinal exact modes are gauge representatives,
scalar ghosts encode the Faddeev-Popov quotient Jacobian,
the physical bosonic block is the co-closed Hodge one-form block,
bosonic determinants enter with half-density weight.
```

Relative to the scalar external-component diagnostic already used in the Qa
reduction, the selected p-nonzero physical quotient response is:

```text
p_selected = p_nonzero_scalar - 1/2 p_nonzero_coclosed_oneform
```

Using the sourced co-closed identity:

```text
Y_+^{k,n} Y_-^{k,n} = (M_{k,n+1}^2)^2
```

this equals the finite part of the lowest scalar oscillator mode:

```text
p_selected = 0.9889753274739147
```

## Numerical Result

The compact Nil scalar diagnostic was:

```text
scalar total = 3.8540439660345185
```

The selected `p=0` correction is:

```text
0
```

The selected `p != 0` physical quotient response is:

```text
0.9889753274739147
```

Therefore:

```text
selected Qa = 4.8430192935084335
required Qa = 4.648486359430842
difference  = -0.19453293407759187  (required - selected)
```

In weak-split form:

```text
selected lambda_12 = 2.210364204780355
target lambda_12   = 2.194153126940556
residual           = +0.01621107783979925
```

## Verdict

The `p != 0` physical quotient rule is now selected and computed, but it does
not close Qa/SU3.  It overshoots by exactly the same lowest-mode excess already
visible in the co-closed quotient test.

So the remaining issue is not:

```text
p0 ghost measure,
Weitzenbock E,
or arbitrary quotient choice.
```

The remaining issue is one of:

```text
1. a source-selected finite coherent projector/Jacobian subtracting the lowest-mode excess,
2. a different selected Qa/SU3 operator than the compact Nil Hodge quotient,
3. an obstruction theorem saying this branch is not the final no-knob closure.
```

Next artifact:

```text
Selected_Qa_SU3_Final_Obstruction_or_Projector_Jacobian_Resolution_v1
```

