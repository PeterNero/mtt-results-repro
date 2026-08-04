---
title: |
  Time-Oriented m=1 Freed-Witten Cycle Gate
author: MTT proof reproduction program
---

# Question

Can the conditional m=1 flat gerbe promotion be pushed through
Freed-Witten consistency?

Not fully yet, because the selected cycles or branes are not supplied.  But the
3-torsion gerbe-restriction part is now completely finite and executable.

# Finite Restriction Theorem

The active quotient is:

```text
F_3^2.
```

The m=1 commutator form is:

```text
omega((a,b),(c,d)) = a d - b c mod 3.
```

For a selected cycle `Y`, let:

```text
I_Y = image(pi1(Y) -> F_3^2).
```

Then:

```text
DD(B)|_Y = 0  iff  rank_F3(I_Y) <= 1.
```

Equivalently:

```text
inactive or one-line active image: passes the 3-torsion gerbe part,
full active F_3^2 image: fails the 3-torsion gerbe part.
```

# Why

For finite abelian groups, U(1)-valued 2-cocycle classes are classified by
alternating bicharacters.  The m=1 form is symplectic on F_3^2.  Therefore the
restriction class is trivial exactly on isotropic subgroups.  In F_3^2, the
isotropic subgroups are the zero subgroup and the four lines.

# Sample Restrictions

The executable check records:

```text
inactive kernel cycle: DD(B)|Y = 0,
g1 line cycle:        DD(B)|Y = 0,
g2 line cycle:        DD(B)|Y = 0,
diagonal line cycle:  DD(B)|Y = 0,
full g1,g2 image:     DD(B)|Y != 0.
```

# Freed-Witten Gate

The full condition on each selected cycle remains:

```text
W3(Y) = 0,
DD(B)|_Y = 0.
```

The 3-torsion m=1 class cannot cancel a 2-primary W3 obstruction.  Thus W3 or
spinC evidence must be supplied separately for each selected cycle.

# Validator

The validator is:

```text
scripts/validate_time_oriented_m1_selected_cycle_restrictions.py
```

It consumes:

```text
certificates/time_oriented_m1_selected_cycle_restrictions.template.json
```

A future filled packet must list each selected cycle, its image in F_3^2, and a
W3=0 or spinC certificate.  The validator computes the DD(B) restriction and
refuses any full-rank active image.

# What This Closes

This closes:

```text
DD(B) restriction decision procedure for the m=1 flat gerbe,
isotropic-image criterion rank <= 1,
full active F_3^2 obstruction,
future selected-cycle packet schema and validator.
```

# What This Does Not Close

This does not claim:

```text
selected cycles supplied,
Freed-Witten verified,
selected projector retention,
selected D_E/dotD/Riesz/Green files,
full SM closure.
```

# Consequence

The next data cannot be a floating statement like "Freed-Witten holds."  It
must be a finite selected-cycle packet:

```text
cycle id,
selected-source certificate,
image in F_3^2,
DD(B)|Y computed zero,
W3(Y)=0 or spinC certificate.
```

Only then can the twisted-source promotion gate honestly mark
Freed-Witten/projector retention as selected evidence.

# Artifact

The executable constructor is:

```text
scripts/analyze_time_oriented_m1_freed_witten_cycle_gate.py
```

It writes:

```text
candidate_data/time_oriented_m1_freed_witten_cycle_gate.candidate.json
certificates/time_oriented_m1_freed_witten_cycle_gate_certificate.json
```

# Verdict

Closed:

```text
the finite m=1 Freed-Witten DD(B) restriction gate.
```

Open:

```text
the actual selected cycle list and W3/spinC certificates.
```
