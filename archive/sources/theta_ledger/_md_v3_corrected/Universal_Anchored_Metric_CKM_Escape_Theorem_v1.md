---
abstract: |
  We sharpen the anchored kinetic-metric route.  The pure Z3 bridge packet has
  commuting Hermitian left forms and therefore cannot produce CKM magnitudes.
  A non-circulant anchored metric from the transport/lens/nil role ordering
  breaks that common basis.  Direct computation shows that independent
  up/down metric scales are not required merely to escape the no-go: applying
  the same universal anchored metric to both bridge sectors already produces a
  nonzero Hermitian commutator when the selected up and down bridge weights
  differ.  Thus the next exact-magnitude problem is not to introduce separate
  metric knobs, but to derive the universal anchored metric scale and the
  bridge weights from Sigma_MTT.
author:
- Peter Nero
date: June 2026
title: |
  Universal Anchored Metric CKM-Escape Theorem
---

# Purpose

The anchored metric candidate left two possible worries:

```text
1. maybe CKM mixing requires independently tuned up/down kinetic metrics;
2. maybe the anchored metric only works because one sector was left unbroken.
```

This note closes both worries at the structural level.

# Setup

Let:

```text
Y_u,raw[i,j] = C_u[-(i+j) mod 3],
Y_d,raw[i,j] = C_d[-(i+j) mod 3].
```

Let the universal anchored family metric be:

```text
G_A = diag(exp(2sJ_0), exp(2sJ_1), exp(2sJ_2)),
J = (0, lambda_nil/lambda_lens, 1).
```

In normalized structural units set:

```text
s=1.
```

Then:

```text
J ~= (0, 0.070028, 1),
G_A ~= diag(1, 1.150338, 7.389056).
```

# Theorem: Universal Anchored Metric Escapes the Pure Bridge No-Go

For generic distinct selected bridge triples `C_u` and `C_d`, the Hermitian
forms:

```text
H_u = Y_u,raw G_A^{-1} Y_u,raw^*,
H_d = Y_d,raw G_A^{-1} Y_d,raw^*
```

need not commute.  Therefore a single universal anchored metric is sufficient
in principle to break the pure bridge common-family basis.

Proof.  The pure bridge no-go holds because, with identity or circulant
metrics, both Hermitian forms remain circulant and are diagonalized by the
same family Fourier matrix.  The anchored metric `G_A` is positive and
non-circulant in the family localization basis.  Multiplication by
`G_A^{-1}` does not preserve the family-circulant algebra.  Therefore the
normalized Hermitian forms are not generally circulant and need not commute.

The audit script supplies an explicit non-empirical finite example using
q79-character bridge weights.  It obtains:

```text
identity / identity commutator:       0
universal anchored / anchored:        nonzero
```

# Consequence

This removes a potential proxy knob.  We do not need to posit independent
up/down metric scales merely to make CKM mixing possible.

The remaining exact calculation is:

```text
derive s,
derive C_u[0..2],
derive C_d[0..2],
then compute CKM magnitudes.
```

The same universal metric may or may not be enough numerically.  That is a
calculation, not a new freedom.

# What This Closes

```text
pure bridge no-go escaped by one universal metric        PROVED/CHECKED
independent up/down metric scales not structurally needed PROVED
q79 phase algebra retained                               CHECKED
no CKM/mass data used                                    CHECKED
```

# What Remains

```text
derive universal scale s from MTT                         OPEN
derive bridge weights C_u,C_d from MTT                     OPEN
compute actual CKM magnitudes                              OPEN
test whether universal metric also works numerically       OPEN
extend to lepton and neutral sectors                       OPEN
```

# Bottom Line

The family-breaking mechanism can remain very lean:

```text
one q79/Z3 bridge skeleton
+ one universal anchored transport/lens/nil metric
```

is already enough to escape the mathematical no-CKM obstruction.  The hard
next step is numerical derivation from the selected source map, not adding new
sector-local knobs.

