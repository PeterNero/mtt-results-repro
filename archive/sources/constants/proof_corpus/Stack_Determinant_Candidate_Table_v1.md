# Stack Determinant Candidate Table v1

## Purpose

The hypercharge-normalized gate now asks for:

```text
p_a,
p_c,
p_SU2.
```

This note builds the strongest current candidate table.  It is not a closure
claim.  It separates exact scalar-proxy pieces from the still-open selected
gauge-threshold determinants.

## Candidate Table

The current entries are:

```text
p_a    =  7.291801913769811    proxy SU3 finite part,
p_c    =  2.442340583291322    exact circle scalar-proxy zeta,
p_SU2  = -0.5980970589159109   exact sphere scalar-proxy zeta.
```

The calculator is:

```text
scripts/compute_stack_determinant_candidate_table.py
```

## Hypercharge Accounting

Using:

```text
p_Y = p_a/36 + p_c/4,
lambda_12 = p_Y - p_SU2,
```

the candidate table gives:

```text
p_Y = 0.813135198983103,
lambda_12 = 1.411232257899014,
Delta_G,12 = 0.045552446266046334.
```

The diagnostic witness is:

```text
lambda_12 = 2.194153126940556.
```

So the residual is:

```text
-0.7829208690415419.
```

## Interpretation

This is a strong negative result for the current proxy table.

If the exact scalar-proxy `p_c` and `p_SU2` entries were kept, the diagnostic
witness would require:

```text
p_a = 35.47695319926532.
```

The current proxy `p_a` is:

```text
p_a = 7.291801913769811.
```

The gap is:

```text
28.185151285495508.
```

This number must not be used as proof data.  It only says that the exact
selected `Q_a` stack determinant, the physical quotient, or the threshold
operator/weight scheme must differ substantially from the proxy.

## What Is Closed

The accounting is closed:

```text
(p_a,p_c,p_SU2) -> p_Y -> lambda_12 -> Delta_G,12.
```

The exact scalar-proxy circle and sphere zeta pieces are closed.

## What Is Not Closed

The following are still open:

```text
1. selected Q_a/SU3 stack determinant;
2. proof that scalar circle equals selected Q_c gauge-threshold determinant;
3. proof that scalar sphere equals selected SU2 gauge-threshold determinant;
4. physical quotient/projector and ghost/gauge operator correction;
5. topology/index weights in the same threshold scheme.
```

## Verdict

The candidate table is executable and useful, but it does not close
electroweak normalization.

The next proof step is no longer vague:

```text
replace the proxy p_a and scalar p_c/p_SU2 entries with selected
gauge-threshold determinants in one physical quotient scheme.
```
