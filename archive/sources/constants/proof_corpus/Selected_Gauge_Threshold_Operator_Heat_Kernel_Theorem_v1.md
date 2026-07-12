# Selected Gauge Threshold Operator Heat Kernel Theorem v1

## Purpose

The previous gate computed the Casimir heat-coefficient branch.  This note
tests whether that branch can be promoted from source-motivated candidate to
selected MTT theorem.

It cannot yet be promoted.  But the remaining theorem is now reduced to four
precise obligations.

## Theorem Shape

If MTT supplies, from the same selected branch:

```text
1. gauge-factor-resolved threshold operator blocks for Q_a, Q_c, and SU2,
2. physical-quotient trace/index weights,
3. finite zeta/heat determinant parts p_a, p_c, p_SU2,
4. the C1 retarded-kernel derivative/normalization for this source,
```

then the hypercharge-normalized electroweak weak split is executable:

```text
p_Y       = p_a/36 + p_c/4
lambda_12 = p_Y - p_SU2
Delta_G12 = v1_tilde lambda_12 / (4 pi)
```

This would be a no-knob theorem because the electroweak target would enter
only after the selected operator data are computed.

## Corpus Alignment

The general MTT machinery is present.  The measurement/selection corpus uses a
positive elliptic operator whose principal part is a direct sum of
Laplace-type operators and then applies the coherent projector.

The string/heterotic corpus supplies the correct trace conventions:

```text
Tr is the gauge adjoint trace,
Tr(T^2)=1 for abelian generators.
```

The same string/heterotic source also states that one-loop thresholds are not
computed there.

The local determinant interface in this repo already gives the executable
determinant accounting:

```text
p_a = sum_j m_{a,j} w_{a,j} log(lambda_{a,j}/mu^2).
```

Therefore the home for the theorem is correct, but the selected operator
blocks and spectra are not yet supplied.

## Obligation Status

### O1: Selected Gauge-Threshold Operator

Status:

```text
OPEN
```

The corpus supplies a general positive elliptic/Laplace-type smoothing
operator.  It does not yet supply the gauge-fixed threshold operators:

```text
D_Qa, D_Qc, D_SU2.
```

The missing data include ghost treatment, bundle endomorphism terms,
physical-domain choices, and boundary/quotient conditions.

### O2: Heat Trace / Index Weights

Status:

```text
CONDITIONAL_CANDIDATE
```

The current candidate is:

```text
Q_a / SU3 stack       C_A(SU3) = 3
Q_c / circle stack    normalized abelian trace = 1
SU2 stack             C_A(SU2) = 2
```

These coefficients have the right type: they are trace/index data, not a
tunable electroweak parameter.  But they must still be derived from the
selected physical-quotient trace.

### O3: Finite Stack Determinants

Status:

```text
OPEN
```

The scalar circle/sphere finite parts and SU3 proxy are useful diagnostics.
They are not yet the selected gauge determinant finite parts.

### O4: Retarded-Kernel C1 Normalization

Status:

```text
INTERFACE BUILT, VALUE OPEN
```

The C1 response interface supplies:

```text
v1_tilde = 0.405623467693425.
```

But the selected derivative of the retarded overlap kernel acting on the
gauge-threshold determinant source remains open.

## Current Numeric Candidate

Using the conditional Casimir heat coefficients gives:

```text
lambda_12 = 2.41442942313547
Delta_G12 = 0.07793413589076988
residual  = 0.22027629619491407
```

This is not a prediction.  It is a candidate branch awaiting operator
selection.

## Correct Way Forward

The next constructive artifact should be:

```text
Selected_Qa_Qc_SU2_Gauge_Threshold_Operator_Blocks_v1
```

It should define, before numerical electroweak comparison:

```text
D_Qa  = selected gauge-fixed threshold block on the Q_a/SU3 stack,
D_Qc  = selected abelian/circle threshold block with Tr(T^2)=1,
D_SU2 = selected gauge-fixed threshold block on the SU2 stack.
```

For each block it must state:

```text
principal Laplace-type part,
bundle representation,
ghost/subtraction rule,
endomorphism or curvature term,
physical quotient/projector,
domain and normalization,
spectral or heat-coefficient data.
```

## Verdict

The selected gauge-threshold heat-kernel theorem is reduced but not proved.

The general MTT operator machinery aligns with the plan.  The corpus does not
yet close the gauge-factor-resolved threshold operator or finite determinant
values.

Remaining true gate:

```text
construct the selected Qa, Qc, and SU2 gauge-threshold operator blocks and
compute their finite determinant parts in the same physical quotient.
```
