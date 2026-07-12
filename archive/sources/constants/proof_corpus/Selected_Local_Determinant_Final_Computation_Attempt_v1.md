# Selected Local Determinant Final Computation Attempt v1

## Purpose

This is the direct attempt to finish the electroweak C1 determinant
calculation from the strongest currently selected data.

The result is negative but useful: the present corpus gives a selected
first-gap and overlap scaffold, not the full determinant spectrum.  Therefore
the final number is not yet determined.

## Selected Data Used

For the q79 branch, the current selected scaffold contains:

```text
N = 79,
R1 = 0.5397189300902845,
(f2 R_lens)^2 = 0.280 R1,
c_nil = 1.439 R1.
```

The corresponding first-gap data are:

```text
lambda_U1   approximately 1/R1^2,
lambda_SU2 >= 2/(0.280 R1),
lambda_SU3 >= min(4 pi^2, 2 pi + 4 pi^2/c_nil^2).
```

These are enough to test admissibility.  They are not enough to evaluate:

```text
p_a = sum_j m_{a,j} w_{a,j} log(lambda_{a,j}/mu^2).
```

## Identifiability Test

The executable test is:

```text
scripts/test_local_determinant_identifiability.py
```

It builds two determinant inputs:

1. one first-gap proxy mode per gauge factor;
2. the same scaffold plus an additional admissible `SU2` higher mode.

Both inputs preserve the same selected first-gap and overlap data.  They give
different `lambda_12 = p_U1 - p_SU2`.

Therefore the selected first-gap scaffold does not determine the full local
determinant response.

## Why This Blocks The Final Number

The determinant is a spectral invariant of the full selected threshold
operator.  A lowest eigenvalue bound does not fix:

```text
higher eigenvalues,
multipities,
index weights,
bundle connection,
boundary conditions,
regularization prescription.
```

Different completions that share the same first gap can change the determinant
by finite amounts, including in the `U1-SU2` split.

## Verdict

The final electroweak determinant computation is not closed by the current
corpus.  The remaining object is exact:

```text
Selected_Gauge_Factor_Spectral_Table_v1
```

with:

```text
{lambda_{a,j}, m_{a,j}, w_{a,j}} for a in {U1, SU2, SU3}.
```

Once that table is selected independently of electroweak target values, the
existing calculator gives the final C1 contribution immediately.
