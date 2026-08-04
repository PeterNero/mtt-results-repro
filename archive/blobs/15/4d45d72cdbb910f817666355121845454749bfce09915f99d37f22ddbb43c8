---
abstract: |
  The raw family-basis label scan shows that simple proto-spinor/family labels
  do not directly satisfy the right-channel assignment tests.  This note
  identifies the correct projection mechanism: if a raw source label A is
  upstream of the selected weighted right-channel dynamics K, then the
  recordable right-channel observable after Schur/Riesz execution is its
  conditional expectation onto the commutant of K,
  E_K(A)=sum_a P_a A P_a.  This operator commutes with K, preserves the
  right-channel spectral projectors, and has trace labels
  Tr(P_a A).  Thus the remaining source problem becomes finite and explicit:
  find corpus-native raw labels A_u^spin, A_d^dyad, A_d^nil whose commutant
  projections have the required trace table.
author:
- Peter Nero
date: June 2026
title: |
  Schur-Riesz Commutant Projection for Right-Channel Label Observables
---

# Purpose

The dictionary scan found:

```text
raw family-basis labels do not directly commute with K_x.
```

But MTT observables are not raw pre-execution labels.  They are recordable
post-projection quantities.  Therefore the natural next mechanism is the
Schur/Riesz projection of raw labels into the selected right-channel commutant.

# Definition

Let:

```text
K_x = Z_x^* Z_x
```

with simple spectral projectors:

```text
P_{x,a}.
```

For a raw right-channel source label `A`, define:

```text
E_{K_x}(A) = sum_a P_{x,a} A P_{x,a}.
```

This is the conditional expectation of `A` onto the commutant of `K_x`.

# Theorem

For any self-adjoint raw source label `A`:

```text
E_K(A)
```

is self-adjoint and satisfies:

```text
[E_K(A),K]=0.
```

Moreover:

```text
Tr(P_a E_K(A)) = Tr(P_a A).
```

Thus the projected observable has exactly the same spectral trace labels as
the raw source, but is a valid right-channel observable.

# Proof

Since `P_a` are mutually orthogonal spectral projectors of `K`, every term
`P_a A P_a` maps the `a`-th eigenspace of `K` to itself.  Therefore the sum is
block-diagonal in the spectral decomposition of `K`, hence commutes with `K`.
If `A=A^*`, then each `P_a A P_a` is self-adjoint.  Finally:

```text
Tr(P_a E_K(A))
= Tr(P_a P_a A P_a)
= Tr(P_a A P_a)
= Tr(P_a A).
```

# Relevance to MTT

This projection is proof-admissible only if it is the selected execution rule:

```text
raw source label
-> coherent/Schur/Riesz reduction
-> right-channel recordable observable.
```

It is not admissible to choose `A` after looking at quark masses.

# Remaining Source Test

The final no-proxy task becomes:

```text
find raw corpus-native A_u^spin, A_d^dyad, A_d^nil
such that:

Tr(P_{u,1} A_u^spin) = -1,
Tr(P_{u,2} A_u^spin) = +1,

Tr(P_{d,1} A_d^dyad) = 1,
Tr(P_{d,2} A_d^dyad) = 0,

Tr(P_{d,1} A_d^nil) = 0,
Tr(P_{d,2} A_d^nil) = 1.
```

# What This Closes

```text
projection mechanism for right-channel observables       PROVED
raw-label noncommutation problem                         RESOLVED-SCHEMA
need for corpus-native raw labels                        SHARPENED
full assignment theorem                                  OPEN
```

# Bottom Line

The remaining mass-source proof is now:

```text
identify the raw source labels A
and prove Sigma_MTT executes E_K(A)=sum P_a A P_a.
```

That is the precise bridge from proto-spinor/dyadic/nil source data to the
right-channel trace table.

