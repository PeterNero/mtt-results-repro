---
title: |
  Time-Oriented m=1 Visible Green-Schwarz Curvature Closure
author: MTT proof reproduction program
---

# Purpose

This closes the visible Green-Schwarz equation at the curvature level for the
time-oriented `q79/F,m=1` branch.

It does not close the stronger visible SM operator-source problem.

# Source

The selected Iwasawa invariant curvature certificate supplies:

```text
Tr R_+^2 = 8*r3^2/(r1^2*r2^2) alpha_1,
dH = -4*r3^2 alpha_1,
alpha_2 = alpha_3 = 0.
```

The source is selected only at curvature/coherent-projection level:

```text
coherent invariant Iwasawa branch: closed,
Bianchi component support: closed,
operator source D_E/dotD: open.
```

# Packet

The selected curvature packet is:

```text
certificates/time_oriented_m1_visible_green_schwarz_curvature.selected.json
```

It uses the invariant basis:

```text
alpha_1 = a wedge b,
alpha_2 = a wedge c,
alpha_3 = b wedge c.
```

and the symbolic rows:

```text
dH                       = [-4*r3^2, 0, 0],
Tr R_+^2                 = [8*r3^2/(r1^2*r2^2), 0, 0],
Tr F_visible^2 required  = [8*r3^2/(r1^2*r2^2) + 4*r3^2, 0, 0],
residual                 = [0, 0, 0].
```

# Validator

The visible-curvature validator now supports this symbolic Iwasawa row mode by
comparing the packet against the derived requirement certificate:

```text
time_oriented_m1_visible_green_schwarz_requirement_certificate.json.
```

This avoids pretending the row is a decimal/numeric fit.  It is an exact
symbolic Chern-Weil requirement in the selected invariant basis.

# What This Closes

```text
selected visible Green-Schwarz curvature packet,
zero symbolic Bianchi residual,
curvature-level source from selected Iwasawa invariant row.
```

# What Remains Open

```text
selected visible SM operator source,
projector retention for visible zero modes,
selected D_E/dotD/Riesz/Green files,
primitive C1 contractions,
Yukawa and CKM magnitudes,
full SM closure.
```

# Artifact

The constructor is:

```text
scripts/close_time_oriented_m1_visible_gs_curvature.py
```

It writes:

```text
candidate_data/time_oriented_m1_visible_green_schwarz_curvature_closure.candidate.json
certificates/time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json
certificates/time_oriented_m1_visible_green_schwarz_curvature.selected.json
```

# Verdict

Closed:

```text
TIME_ORIENTED_M1_VISIBLE_GS_CURVATURE_CLOSED_OPERATOR_SOURCE_OPEN.
```

The next remaining object is not the curvature equation.  It is the selected
visible operator-source package that turns this curvature row into retained
projectors, `D_E`, `dotD`, Green/Riesz data, and primitive C1 contractions.
