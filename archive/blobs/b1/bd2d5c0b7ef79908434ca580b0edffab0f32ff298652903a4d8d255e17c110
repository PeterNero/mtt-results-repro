---
abstract: |
  We test whether the pure finite qutrit/C6 part of the block-factorized route
  can itself supply the CKM heavy-link entries.  With a trivial Higgs line, the
  finite qutrit invariant rule allows nontrivial matter pairs only in conjugate
  orientations 1+2 or 2+1.  Computing the invariant bilinear support for those
  two pairings gives the diagonal identity matrix.  Hence the pure finite
  qutrit/C6 support has zero (1,3) and (2,3) heavy-link entries.  This retires
  the C6-only route for leading CKM heavy links and relocates the search to
  selected differential response, selected basis transport, or a selected
  support operator beyond the pure finite pairing.
author:
- Peter Nero
date: May 2026
title: |
  Qutrit C6 Pure Heavy-Link Support
---

# Purpose

The heavy-link packet asks for:

```text
Delta_v = Delta_t + chi_q Delta_c.
```

The previous fill attempt showed that no selected `Delta_t` or `Delta_c`
values are present.  This note asks a more structural question:

```text
Can pure finite qutrit/C6 support supply Delta_c?
```

# Finite Setup

The block-factorized packet has:

```text
rank-three qutrit family block,
ordinary rank-one Higgs line.
```

For SM Yukawa pairs with the trivial Higgs line, the finite qutrit rule is:

```text
s_left + s_right = 0 mod 3.
```

Thus nontrivial matter pairs are:

```text
1+2,
2+1.
```

# Support Calculation

Let `M_ij` be a finite family support matrix.  The common shift constraint
makes support depend on:

```text
i - j mod 3.
```

The clock constraint permits an entry only if:

```text
s_left i + s_right j = 0 mod 3.
```

For the conjugate pair `1+2`, this becomes:

```text
i - j = 0 mod 3.
```

For the conjugate pair `2+1`, it gives the same condition.  Therefore the
unique invariant support for each conjugate nontrivial pair is:

```text
[[1,0,0],
 [0,1,0],
 [0,0,1]].
```

The CKM heavy-link entries are:

```text
(1,3), (2,3).
```

For the diagonal support:

```text
M_13 = 0,
M_23 = 0.
```

# Consequence

For pure finite qutrit/C6 support in the aligned qutrit family basis:

```text
c_u = (0,0),
c_d = (0,0),
Delta_c = c_d - c_u = (0,0).
```

So pure finite qutrit/C6 support cannot close:

```text
Delta_t + chi_q Delta_c != (0,0)
```

unless `Delta_t` is supplied by some other selected source.

# What This Retires

This retires the tempting shortcut:

```text
global q79 phase + qutrit finite pairing -> CKM heavy-link support.
```

The q79 phase remains the CP-active finite character, but the pure finite
qutrit pairing does not place it in the heavy-link entries.

# What Is Not Ruled Out

The calculation does not rule out:

```text
selected differential response,
selected non-invariant basis transport,
selected C6 support operator beyond the pure finite pairing,
character-trivial C1 or other channel heavy links.
```

Those are now the live sources for the missing heavy-link packet.

# Next Source

The next practical route is:

```text
compute Delta_t from selected C1 primitive contractions,
or compute selected basis transport/non-invariant Galerkin data that rotates
the diagonal finite support into the physical heavy-link basis.
```

That means the solution is no longer to search harder for a pure C6 number.
The solution is to construct the selected differential/basis data that produces
the heavy-link entries.
