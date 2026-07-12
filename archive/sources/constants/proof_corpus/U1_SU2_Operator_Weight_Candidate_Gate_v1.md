# U1/SU2 Operator-Weight Candidate Gate v1

## Purpose

The exact scalar-proxy weak split is now closed, but it is not the final
electroweak threshold:

```text
lambda_12(scalar unit weights) = 3.040437642207233,
lambda_12(diagnostic witness) = 2.194153126940556.
```

This note builds the next gate: the selected U1/SU2 gauge-threshold operator
and topology/index weights.

The purpose is not to fit the diagnostic witness.  It is to separate:

```text
source-motivated operator/weight candidates
from
reverse-engineered weights that are forbidden as no-knob proof data.
```

## Exact Inputs

The closed exact scalar pieces are:

```text
p_U1  =  2.442340583291322,
p_SU2 = -0.5980970589159109.
```

Therefore:

```text
lambda_12 = p_U1 - p_SU2 = 3.040437642207233.
```

The selected C1 bridge gives:

```text
Delta_G,12 = v1_tilde lambda_12/(4 pi).
```

With the selected `v1_tilde`, the scalar-proxy result is:

```text
Delta_G,12 = 0.09814073590416784.
```

## Candidate Checks

The executable candidate checker is:

```text
scripts/compute_u1_su2_operator_weight_candidates.py
```

It evaluates the following non-final candidates.

### Scalar unit weights

This is the already closed scalar-proxy result:

```text
lambda_12 = 3.040437642207233.
```

It overshoots the diagnostic witness by:

```text
0.8462845152666771.
```

Thus unit scalar weights are not the final threshold operator.

### Equal half-determinant prefactor

Applying a formal one-loop half determinant equally gives:

```text
lambda_12 = 1.5202188211036165.
```

This undershoots the witness.  It is a useful sanity check because the missing
object is not merely a universal prefactor.

### GUT-style U1 normalization check

The common hypercharge normalization check:

```text
w_U1 = 3/5,
w_SU2 = 1
```

gives:

```text
lambda_12 = 2.063501408890704.
```

This is closer than the scalar unit result, but still not closure.  It can
become admissible only if the MTT branch independently selects this U1
normalization in the threshold operator.

### Two-thirds U1 diagnostic

The simple rational check:

```text
w_U1 = 2/3,
w_SU2 = 1
```

gives:

```text
lambda_12 = 2.226324114443459,
Delta_G,12 = 0.0718623805729687.
```

This is close to the diagnostic witness, but it is not a proof.  The value
`2/3` must not be imported merely because it is close.  It would need a source
theorem, for example from complex nesting, shared-circle projection, charge
normalization, or a selected gauge-fixed threshold operator.

### Formal de Rham vector/ghost check

For ordinary Hodge spectra:

```text
det' Delta_1(S1) = det' Delta_0(S1),
det' Delta_1(S2) = det' Delta_0(S2)^2.
```

The formal gauge-fixed combination:

```text
1/2 log det Delta_1 - log det Delta_0
```

therefore gives:

```text
lambda_12 = -1.221170291645661.
```

This is not viable as the selected threshold operator.  It is retained as a
negative check: the final operator is not the naive de Rham vector/ghost
determinant on the scalar proxy geometry.

## Forbidden Reverse Engineering

If one solves directly for weights from the diagnostic target, one obtains:

```text
w_U1 = 0.6534944712230856, with w_SU2 = 1,
w_SU2 = -0.4149618404755606, with w_U1 = 1.
```

These numbers are forbidden as proof data because they are target-derived.

The rational scan likewise finds near hits, for example:

```text
w_U1 = 5/9, w_SU2 = 7/5
```

with residual about `3.86e-5`.  This is diagnostically interesting but
mathematically unusable unless those weights are selected before any
electroweak comparison.

## Correct Way Forward

The next theorem must select the operator and weights independently.  The
promising source routes are:

```text
1. shared-circle projection:
   derive whether the U1 circle determinant is reduced by an orientation,
   real/complex, or shared-boundary quotient;

2. complex nesting:
   derive whether the U1 threshold uses a complex-line normalization different
   from the scalar real-mode count;

3. hypercharge/topology normalization:
   prove whether the selected MTT branch fixes a U1 charge normalization such
   as 3/5, 2/3, or another rational from topology rather than fitting;

4. gauge-fixed threshold operator:
   replace scalar Laplacians with the actual gauge-threshold Laplace-type
   operator, including ghosts, bundle endomorphism terms, and index weights.
```

Only after one of these routes source-certifies the operator and weights may
the result be compared with the electroweak diagnostic witness.

## Verdict

The U1/SU2 operator-weight gate is now executable and audited.

The strongest current clue is:

```text
2/3 U1 weighting is close, but not selected.
```

The strongest rigorous conclusion is:

```text
scalar unit weights are false as final closure,
universal half-prefactor is false as final closure,
naive de Rham vector/ghost determinant is false as final closure.
```

Remaining proof gate:

```text
Selected_U1_SU2_Gauge_Threshold_Operator_and_Weights_v1.
```
