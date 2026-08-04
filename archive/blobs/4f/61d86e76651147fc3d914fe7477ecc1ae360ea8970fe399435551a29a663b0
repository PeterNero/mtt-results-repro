---
title: |
  Time-Oriented m=1 Green-Schwarz Gate
author: MTT proof reproduction program
---

# Question

Does the selected time-oriented `m=1` flat gerbe close the
Green-Schwarz/Bianchi input needed by the visible SM source route?

It closes a preservation statement, not the visible source statement.

# Calculation

The promoted `m=1` representative is flat:

```text
B_i = 0,
A_ij = 0,
g_ijk locally constant,
H = 0.
```

Therefore its de Rham curvature contribution is:

```text
Delta dH from m=1 flat torsion = 0.
```

So adding this flat torsion label cannot change the curvature equation:

```text
dH = Tr R_+^2 - Tr F^2
```

in any de Rham curvature basis.  It preserves an already closed
Green-Schwarz sector, but it cannot repair a missing or nonzero visible
curvature residual.

# Imported Closed Sector

The `Z7` Fu-Yau/Mukai charge-sector certificate already records:

```text
Green-Schwarz Bianchi identity verified: true
status: CLOSED_CHARGE_SECTOR
```

Because the `m=1` gerbe is flat, this closed charge-sector Bianchi equation is
preserved under the torsion extension.

# Visible Sector

The visible SM operator-source route still needs a selected same-branch packet
with:

```text
curvature basis,
dH coefficients,
Tr R_+^2 coefficients,
Tr F_visible^2 coefficients,
zero Bianchi residual,
selected visible source certificate,
projector-retention certificate.
```

The current Iwasawa curvature row helps but does not close the visible source:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
dH = -4 r3^2 alpha_1.
```

The actual visible gauge curvature and the map from this row to selected
`D_E`, `dotD`, zero modes, and C1 contractions are still open.

# Consequence

This prevents a hidden-knob mistake.  The flat gerbe is important as a torsion
holonomy/source label, but it is not a curvature dial.  Therefore:

```text
closed:  flat m=1 torsion preserves closed Bianchi sectors,
closed:  flat m=1 torsion cannot secretly cancel visible curvature residuals,
open:    selected visible Green-Schwarz curvature packet.
```

# Future Packet

The future fill-in slot is:

```text
certificates/time_oriented_m1_visible_green_schwarz_curvature.template.json
```

It is checked by:

```text
scripts/validate_time_oriented_m1_visible_green_schwarz_curvature.py
```

The validator computes:

```text
residual = dH - (Tr R_+^2 - Tr F_visible^2)
```

after all coefficient vectors are supplied by a selected same-branch source.

# Artifact

The executable constructor is:

```text
scripts/analyze_time_oriented_m1_green_schwarz_gate.py
```

It writes:

```text
candidate_data/time_oriented_m1_green_schwarz_gate.candidate.json
certificates/time_oriented_m1_green_schwarz_gate_certificate.json
```

# Verdict

The Green-Schwarz status is now sharper:

```text
TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN.
```

The next closing object is not another torsion-label argument.  It is a
selected visible bundle/operator-source curvature packet on the same
`q79/F,m=1` branch.
