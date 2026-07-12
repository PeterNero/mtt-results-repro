# Hypercharge Embedding Gate v1

## Purpose

The scalar-proxy weak split used the raw circle determinant as the U1 entry.
The corpus gives a more structured possibility: physical U1 may mean
hypercharge after the admissible three-stack projection, not the primitive
circle stack by itself.

The relevant source is the ProtoSpinor three-stack corner:

```text
U(3)_a x U(2)_b x U(1)_c,
Y = (1/6) Q_a - (1/2) Q_c.
```

For inverse-coupling or threshold contributions this gives the linear
combination:

```text
p_Y = (1/36) p_a + (1/4) p_c.
```

## Clarification

The previous conclusion remains algebraically correct:

```text
lambda_12 = p_U1 - p_SU2.
```

Nil/SU3 does not enter after the selected U1 threshold `p_U1` is already
known.

But the hypercharge embedding changes the selection problem.  If the selected
U1 is physical hypercharge, then:

```text
p_U1 = p_Y = (1/36) p_a + (1/4) p_c,
```

and the SU3/Nil-side stack can enter indirectly through the selection of
`p_Y`.

## Executable Check

The calculator is:

```text
scripts/compute_hypercharge_embedding_gate.py
```

Using the exact circle and SU2 sphere pieces:

```text
p_c   =  2.442340583291322,
p_SU2 = -0.5980970589159109.
```

The hypercharge branch without the `Q_a` term gives:

```text
p_Y = 0.6105851458228305,
lambda_12 = 1.2086822047387416.
```

This undershoots the diagnostic witness by:

```text
-0.9854709222018143.
```

Using the current proxy SU3 finite-part estimator:

```text
p_a(proxy) = 7.291801913769811,
p_Y = 0.813135198983103,
lambda_12 = 1.411232257899014.
```

This still undershoots by:

```text
-0.7829208690415419.
```

Because the SU3 value is a proxy finite part with unit weights and a fitted
subtraction basis, it cannot be promoted to a prediction.

## Diagnostic Required Value

If the hypercharge embedding is the correct U1 selection rule, then the
diagnostic target would require:

```text
p_a = 35.47695319926532.
```

This number is target-derived and therefore forbidden as proof data.  It is
useful only as a scale diagnostic for the exact Nil/stack determinant.

## Correct Next Gate

The next computation is no longer just:

```text
circle U1 versus sphere SU2.
```

It is:

```text
selected Q_a stack determinant,
selected Q_c stack determinant,
hypercharge-normalized threshold scheme,
then p_Y - p_SU2.
```

This is exactly where the shared-circle and recursive topology warnings matter:
the raw circle may be a component of `Q_c`, while physical hypercharge is a
quotient-compatible linear combination selected after admissibility lifting.

## Verdict

The hypercharge embedding gate is built.

It does not close electroweak normalization.  It improves the map of the
remaining problem:

```text
Nil/SU3 stays retired from the already-selected lambda_12 formula,
but it is back in play for selecting physical p_U1 = p_Y.
```

Remaining proof gate:

```text
Selected_Hypercharge_Normalized_Gauge_Threshold_Determinant_v1.
```
