# Physical Quotient Scheme Candidates v1

## Purpose

The stack determinant candidate table showed that the current proxy values
undershoot the hypercharge-normalized weak split.  This note tests the natural
physical-quotient corrections that can be named before the final selected
gauge-threshold operator is known.

It does not select any of them.

## Calculator

```text
scripts/compute_physical_quotient_scheme_candidates.py
```

The baseline stack values are:

```text
p_a    =  7.291801913769811,
p_c    =  2.442340583291322,
p_SU2  = -0.5980970589159109.
```

The hypercharge accounting remains:

```text
p_Y = p_a/36 + p_c/4,
lambda_12 = p_Y - p_SU2.
```

## Candidate Results

The current proxy table gives:

```text
lambda_12 = 1.411232257899014.
```

An equal half-determinant prefactor gives:

```text
lambda_12 = 0.705616128949507.
```

This is ruled out as a universal repair.

A uniform two-polarization multiplier gives:

```text
lambda_12 = 2.822464515798028.
```

This overshoots and is not selected.

Adjoint dimension weights:

```text
p_a -> 8 p_a,
p_SU2 -> 3 p_SU2,
p_c -> p_c
```

give:

```text
lambda_12 = 4.025276747852743.
```

This overshoots strongly.

Adjoint Casimir weights:

```text
p_a -> 3 p_a,
p_SU2 -> 2 p_SU2,
p_c -> p_c
```

give:

```text
lambda_12 = 2.41442942313547.
```

This is the strongest structural clue among the candidates tested here, but it
is still not selected and still not exact.

The formal de Rham vector/ghost check on `Q_c/SU2` gives:

```text
lambda_12 = -0.10274251975114274.
```

This is ruled out on this proxy branch.

## Interpretation

The missing correction is not a universal prefactor.  It behaves more like a
gauge heat-kernel/index-weight correction.

The adjoint Casimir clue is meaningful because gauge one-loop threshold
operators naturally carry representation-theoretic trace factors.  But this is
only a clue.  A no-knob proof must derive the weights from the selected
operator and physical quotient, not choose them by proximity to the diagnostic
witness.

## Next Gate

The next artifact should compute:

```text
selected physical quotient heat coefficients / index weights
```

for:

```text
Q_a,
Q_c,
SU2.
```

Then the stack determinants can be recomputed without proxy multipliers.

## Verdict

The best currently tested structural candidate is:

```text
adjoint Casimir weighting.
```

It is not closure.

Remaining proof gate:

```text
Selected_Physical_Quotient_Heat_Coefficients_v1.
```
