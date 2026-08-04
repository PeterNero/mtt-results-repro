# Selected Hypercharge-Normalized Threshold Interface v1

## Purpose

The previous gate showed that physical U1 may be hypercharge, not the raw
circle determinant.  This note turns that into an executable accounting
interface.

The selected structural embedding from the ProtoSpinor three-stack corner is:

```text
Y = (1/6) Q_a - (1/2) Q_c.
```

For determinant or inverse-coupling threshold pieces:

```text
p_Y = (1/36) p_a + (1/4) p_c.
```

The electroweak C1 split is then:

```text
lambda_12 = p_Y - p_SU2,
Delta_G,12 = v1_tilde lambda_12/(4 pi).
```

## Executable Interface

The calculator is:

```text
scripts/compute_hypercharge_normalized_threshold.py
```

The open input template is:

```text
certificates/selected_hypercharge_normalized_threshold.template.json
```

It requires:

```text
stack_thresholds.Qa_SU3_stack,
stack_thresholds.Qc_circle_stack,
stack_thresholds.SU2_stack.
```

The calculator refuses the template until all three are supplied.

## Source Discipline

The corpus currently supports three different levels.

First, ProtoSpinor supports the three-stack structural embedding:

```text
U(3)_a x U(2)_b x U(1)_c,
Y = (1/6) Q_a - (1/2) Q_c.
```

Second, finite coherent projection says gauge-sector computations must preserve
the physical quotient/projector before modal weights are used.

Third, the heterotic/flux papers confirm that thresholds live in realization
level determinant or one-loop data.  They do not compute the electroweak
threshold amplitudes.

Therefore:

```text
hypercharge embedding is structurally selected,
determinant amplitudes are not yet selected.
```

## What This Fixes

The earlier scalar-proxy formula:

```text
lambda_12 = p_U1 - p_SU2
```

remains correct.  The improvement is that the selected U1 input should be
understood as:

```text
p_U1 = p_Y
```

if the physical hypercharge branch is used.

Thus the final weak split should be computed from:

```text
lambda_12 = (p_a/36 + p_c/4) - p_SU2.
```

## Forbidden Shortcut

Solving the diagnostic witness backward for `p_a`, `p_c`, or `p_SU2` is not a
no-knob derivation.  The inputs must come from:

```text
selected stack determinant,
selected physical quotient/projector,
selected threshold scheme,
selected topology/index weights.
```

Only after those are supplied may the value be compared to electroweak data.

## Verdict

This interface closes the accounting for the hypercharge-normalized threshold
gate.  It does not close the numerical electroweak prediction.

Remaining proof gate:

```text
Selected_Qa_Qc_SU2_Stack_Determinants_v1.
```
