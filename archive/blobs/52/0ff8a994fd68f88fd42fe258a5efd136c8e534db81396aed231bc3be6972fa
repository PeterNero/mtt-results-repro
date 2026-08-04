---
abstract: |
  We sharpen the B_q breakdown coefficient after deriving the color-singlet
  Schur source of the 1/2 term.  The color redundancy contribution may be
  represented either externally, by a multiplicity factor in the gap
  coefficient, or internally, by Schur-reducing the hidden color-completion
  channels.  Once B_q uses the internal Schur completion, the remaining
  primitive breakdown gap is lambda_lens - lambda_nil.  Keeping
  lambda_lens - 3 lambda_nil would double count the color-redundancy
  contribution.  This selects the reduced color-gap branch conditionally on
  the adopted internal B_q source.
author:
- Peter Nero
date: June 2026
title: |
  No-Double-Counting Gap Selection Lemma for the Quark B_q Operator
---

# Purpose

The old B_q diagnostic used:

```text
Lambda_q = lambda_lens - 3 lambda_nil.
```

After the color-singlet source theorem, B_q already contains color redundancy
through the Schur coefficient:

```text
(1/2)(J_j - J_{b+sigma})^2.
```

This note states the corresponding gap-accounting rule.

# Two Equivalent Accounting Schemes

There are two ways to encode color redundancy in the effective quark breakdown
cost.

## External Multiplicity

One can keep the operator first-order and put the color multiplicity into the
coefficient:

```text
Lambda_external = lambda_lens - 3 lambda_nil.
```

This treats three nil/color channels as an external subtraction.

## Internal Schur Completion

Alternatively, one can integrate out the hidden color-neutral completion
channels.  Then the color multiplicity is not an external coefficient.  It is
represented by the effective Schur cost:

```text
delta^2 -> delta^2/2.
```

In that case the remaining coefficient should be the primitive lens-to-nil
gap:

```text
Lambda_internal = lambda_lens - lambda_nil.
```

# Lemma: No Double Counting

Assume:

1.  the quark B_q operator is sourced by internal color-singlet Schur
    completion;

2.  the hidden color redundancy contribution has already been integrated out
    into the effective coefficient `1/2`;

3.  `Lambda_q` multiplies the remaining primitive lens/nil breakdown gap after
    hidden color completion.

Then:

```text
Lambda_q = lambda_lens - lambda_nil.
```

Using

```text
Lambda_q = lambda_lens - 3 lambda_nil
```

in the same internally Schur-reduced B_q operator double counts the nil/color
redundancy contribution.

# Proof

By assumption 1, the color-neutral hidden channels are part of the effective
operator construction, not an external multiplicity left to be applied later.
By assumption 2, their minimization has already changed the residual from
`delta^2` to `delta^2/2`.  Therefore the color-redundancy multiplicity has
already acted on the cost.

The coefficient `Lambda_q` now multiplies the primitive gap between the lens
interface role and the nil survivor role.  That primitive gap is:

```text
lambda_lens - lambda_nil.
```

Subtracting `3 lambda_nil` would apply a color-channel count after the color
channels have already been Schur-reduced.  That is double counting.

Hence:

```text
Lambda_q = lambda_lens - lambda_nil.
```

# Numerical Consequence

With the current gap values:

```text
lambda_lens = 3.57,
lambda_nil  = 0.25,
```

the selected internal-completion branch gives:

```text
Lambda_q = 3.32.
```

The older external-count branch gives:

```text
Lambda_q = 2.82.
```

The reduced color-gap diagnostic shows that, after the predecessor orientation
lock selects `sigma=-1`, the internal-completion branch improves the up-stiff
diagnostic:

```text
old external branch residual            about 0.018795
internal reduced-gap predecessor branch about 0.014322
```

Again, the proof is the accounting lemma.  The diagnostic is only a consistency
check.

# What This Closes

```text
Lambda_q = lambda_lens - lambda_nil if B_q uses internal Schur completion  PROVED-CONDITIONAL
lambda_lens - 3 lambda_nil retired for internally completed B_q            RETIRED
gap source no longer a free fit after B_q source is fixed                  SUPPORTED
```

# What Remains

```text
derive mu_u and mu_d from selected Hessian blocks      OPEN
derive absolute normalization/prefactors               OPEN
compute no-proxy singular values and RG flow           OPEN
```

# Bottom Line

The selected internal-completion B_q branch is now:

```text
sigma = -1,
Lambda_q = lambda_lens - lambda_nil.
```

The remaining finite flavor branch is therefore mainly the up/down stiffness
selection:

```text
mu_u, mu_d.
```

