---
title: "Visible Chern-Weil Quantization Gate"
author: "Peter Nero"
date: "May 2026"
abstract: |
  The formal visible Chern-Weil row is algebraically trace-free, but a formal
  row is not yet an integral visible bundle source.  This note separates the
  absorbed Green-Schwarz normalization from the unabsorbed Chern-Weil
  normalization and records the exact quantization gate.  The existing
  u1=8*(2*pi)^2 C1 support row is conditionally consistent with an integer
  label, but it is not a selected visible bundle, sheaf, Chan-Paton, HYM, or
  Route-C source.
---

# Purpose

The previous packet proved:

```text
Tr F_visible^2 =
  (8*r3^2/(r1^2*r2^2) + 4*r3^2) alpha_1
```

has a formal trace-free rank-two realization.  The next question is stricter:

```text
Can this formal row be promoted to an integral/topological visible
Chern-Weil source?
```

# Normalization Split

The row above is written in the absorbed Green-Schwarz normalization:

```text
dH = Tr R_+^2 - Tr F_visible^2,
alpha_prime_over_4_absorbed = true.
```

But Chern-Weil quantization is not a real-number statement about this absorbed
coefficient alone.  It is a period statement after restoring the unabsorbed
Chern-Weil normalization:

This is the central distinction: absorbed Green-Schwarz normalization is not
the same datum as unabsorbed Chern-Weil normalization.

```text
absorbed visible coefficient:
  8*r3^2/(r1^2*r2^2) + 4*r3^2

unabsorbed Bianchi component:
  8*r3^2/(r1^2*r2^2) + (16/alpha_prime)*r3^2
```

So the correct gate is:

```text
P_alpha1*(8*r3^2/(r1^2*r2^2)+(16/alpha_prime)*r3^2)/C_Tr
  lies in the selected visible Chern-character lattice.
```

Here `P_alpha1` is the selected integral period of `alpha_1`, and `C_Tr` is
the selected trace and `2*pi` normalization.

The period normalization must be selected before this can be read as an
integer Chern-character condition.

# Existing Flux Row

The C1 support certificate already records:

```text
u1 = 8*(2*pi)^2,
u2 = u3 = 0,
u1 - v1 = (16/alpha_prime)*r3^2.
```

In the equal-radius specialization this gives:

```text
r3^2 = 8*(2*pi)^2 / (16/alpha_prime + 8/R^4).
```

Thus, if the period unit is `(2*pi)^2` and the trace convention matches, that
row has conditional integer label `8`.  If instead the source is normalized by
the common instanton unit `8*pi^2`, the same row has conditional label `4`.
This convention split is why the selected trace convention must be supplied
before the row becomes a topological charge claim.

This is useful: it shows no immediate quantization contradiction.  But it is
not a selected visible bundle.  The existing row records invariant Bianchi
support for the C1 curvature source, not a same-branch visible SM source with
transition data, stability, HYM/Route-C residual, or `D_E/dotD` data.

# What This Closes

This closes:

```text
formal-to-integral normalization gate formulated,
absorbed and unabsorbed rows separated,
existing integer flux row shown conditionally consistent,
no current integrality contradiction found.
```

# What Remains

The source problem is still open:

```text
selected alpha_1 integral period basis,
selected trace normalization,
selected alpha_prime restoration,
selected visible integral Chern character or K-theory class,
stable visible bundle/sheaf or Chan-Paton source,
source-derived Chern-Weil representative,
HYM or Route-C residual,
same-source D_E/dotD/Riesz/Green data,
coherent spectral projectors,
primitive C1 contractions.
```

So the row has passed the next consistency test, but it is not a selected
visible SM operator source yet.
