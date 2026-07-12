---
title: |
  Time-Oriented m=1 Visible Green-Schwarz Requirement
author: MTT proof reproduction program
---

# Purpose

The previous gate proved that the flat `m=1` torsion gerbe does not change the
de Rham Bianchi equation.  This note derives the exact visible gauge-curvature
row that would be required to fill the selected visible Green-Schwarz packet.

# Normalization

Use the coefficient convention already used by the validator:

```text
dH = Tr R_+^2 - Tr F_visible^2.
```

The invariant Iwasawa basis is:

```text
alpha_1 = a wedge b,
alpha_2 = a wedge c,
alpha_3 = b wedge c.
```

# Known Rows

The closed Iwasawa `R_+` support certificate gives:

```text
Tr R_+^2 = v1_tilde alpha_1,
v1_tilde = 8*r3^2/(r1^2*r2^2),
alpha_2 component = 0,
alpha_3 component = 0.
```

The same source records:

```text
dH = -4*r3^2 alpha_1.
```

# Derived Required Row

Solving the Bianchi equation gives:

```text
Tr F_visible^2 = Tr R_+^2 - dH
               = (8*r3^2/(r1^2*r2^2) + 4*r3^2) alpha_1.
```

Thus, in the invariant basis:

```text
Tr F_visible^2 =
[
  8*r3^2/(r1^2*r2^2) + 4*r3^2,
  0,
  0
].
```

This is a useful sharpening: the visible Green-Schwarz packet is not missing an
arbitrary three-component curvature vector.  It is missing one selected
`alpha_1` gauge-curvature coefficient, plus the proof that this coefficient is
realized by the selected visible SM bundle/operator source.

# What This Does Not Prove

The existing C1 source also records an invariant gauge-flux choice, but that is
not enough.  It is not yet a selected visible SM bundle, and it does not pass
the HYM/Route-C operator-source gate.

Therefore this note does not claim:

```text
selected visible bundle constructed,
visible Green-Schwarz packet verified,
selected D_E/dotD constructed,
projector retention proved,
full SM closure.
```

# Consequence

The next object is now concrete:

```text
selected visible source
  -> Chern-Weil row Tr F_visible^2
  -> coefficient 8*r3^2/(r1^2*r2^2) + 4*r3^2 on alpha_1
  -> zero visible Green-Schwarz residual
  -> source promotion can continue.
```

# Artifact

The executable derivation is:

```text
scripts/derive_time_oriented_m1_visible_gs_requirement.py
```

It writes:

```text
candidate_data/time_oriented_m1_visible_green_schwarz_requirement.candidate.json
certificates/time_oriented_m1_visible_green_schwarz_requirement_certificate.json
```

# Verdict

Closed:

```text
coefficient-level visible Tr F requirement in the invariant Iwasawa basis.
```

Open:

```text
selected visible HYM/Route-C source realizing that row.
```
