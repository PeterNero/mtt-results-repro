---
abstract: |
  We construct a concrete candidate for the quark second-order breakdown
  operator B_q.  The operator acts on top of the first-order q79/Z3 anchored
  bridge.  Its channel cost is not entry-wise: for the unique bridge
  b=-(i+j) mod 3, it compares one quark leg to the bridge role and the other
  leg to the retarded next role, modeling composite residual-strain
  distribution across redundancy channels.  A diagnostic using structural
  constants near the lens/nil gap data produces a CKM-shaped mixing matrix.
  This is not yet a proof of CKM closure, because the sector stiffnesses and
  breakdown coefficient must still be derived from the selected MTT
  localization operator.  It is the first explicit B_q candidate that moves
  the anchored seed from large/lepton-like mixing toward quark-like hierarchy.
author:
- Peter Nero
date: June 2026
title: |
  Quark Second-Order Breakdown Operator Candidate
---

# Purpose

The current diagnostics show:

```text
first-order anchored bridge seed -> large mixing,
scalar quark stiffness           -> still too mixed.
```

Therefore the quark sector needs a structured second-order breakdown layer:

```text
B_q.
```

This note constructs the first explicit candidate.

# First-Order Data

Use the first-order anchor profile:

```text
J = (J_0,J_1,J_2)
  = (0, lambda_nil/lambda_lens, 1).
```

The bridge rule is:

```text
b_ij = -(i+j) mod 3.
```

The q79 phase generator is:

```text
tau = exp(2 pi i 79/448).
```

# Second-Order Breakdown Cost

Define the quark breakdown cost:

```text
D_q(i,j,b)^2 =
  (J_i - J_b)^2
  + (1/2) (J_j - J_{b+1})^2,
```

with indices understood mod `3`.

Interpretation:

```text
first term:  one quark leg is compared to the bridge role;
second term: the other leg is compared to the retarded next role.
```

The `b+1` shift is the retarded/oriented survivor memory.  This is what makes
the operator second-order rather than a scalar stiffness multiplier.

# Candidate Quark Kernel

For sector `x in {u,d}`:

```text
C_x[b] = exp(-mu_x J_b) tau^{s_x b}.
```

Use:

```text
s_u=1,
s_d=2.
```

Then:

```text
Y_x[i,j] =
  C_x[b_ij]
  exp(-Lambda_q D_q(i,j,b_ij)^2).
```

This is not a general matrix.  It is determined by:

```text
J,
tau,
mu_u,
mu_d,
Lambda_q,
the retarded b -> b+1 orientation.
```

# Structural Diagnostic Values

The diagnostic uses:

```text
mu_u = 8,
mu_d = 2,
Lambda_q ~= 2.8.
```

These are not yet derived.  They are plausible structural targets:

```text
mu_u = 2^3      dyadic/up stiffness target,
mu_d = 2        lower dyadic/down stiffness target,
Lambda_q ~ lambda_lens - 3 lambda_nil
         ~= 3.57 - 0.75
         ~= 2.82.
```

The exact derivation of these constants remains open.

# Diagnostic Output

The check script computes:

```text
H_u = Y_u G_A^{-1} Y_u^*,
H_d = Y_d G_A^{-1} Y_d^*,
V = U_u^* U_d.
```

For the structural diagnostic constants, it obtains a CKM-shaped matrix:

```text
|V| approximately
[[0.972, 0.236, 0.009],
 [0.236, 0.971, 0.043],
 [0.019, 0.040, 0.999]].
```

This is qualitatively close to the CKM hierarchy, but it is not a closed MTT
prediction until the constants are selected upstream.

# Theorem: B_q Breaks the Scalar-Stiffness No-Go

The candidate `B_q` is not equivalent to multiplying the first-order anchor
profile by scalar stiffnesses.

Proof.  A scalar stiffness depends only on the bridge class:

```text
J_b.
```

The candidate `B_q` depends on:

```text
i, j, b_ij, b_ij+1.
```

Thus it distinguishes entries sharing the same bridge class by their
first-leg and second-leg role placements.  It is a structured localization
operator, not a scalar multiplier.

# What This Closes

```text
explicit B_q candidate                              CONSTRUCTED
entry-wise fitting still avoided                    CHECKED
scalar-stiffness no-go escaped structurally         CHECKED
CKM-shaped diagnostic possible                      CHECKED
```

# What Remains

```text
derive mu_u=8 from selected MTT data                 OPEN
derive mu_d=2 from selected MTT data                 OPEN
derive Lambda_q from selected Hessian/gap data       OPEN
derive retarded b -> b+1 channel orientation         OPEN
run exact CKM comparison after constants freeze      OPEN
extend B_q relation to color/redundancy formally     OPEN
```

# Bottom Line

The quark sector now has a concrete second-order breakdown candidate:

```text
first-order anchored bridge
+ retarded composite redundancy cost B_q.
```

This is the first candidate that has the right qualitative effect: it turns
the large-mixing anchored seed into a quark-like hierarchy without assigning
independent Yukawa entries.

