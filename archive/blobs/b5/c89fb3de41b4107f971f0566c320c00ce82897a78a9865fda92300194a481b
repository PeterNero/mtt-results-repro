---
title: |
  Time-Oriented m=1 Deck/Cech Lift
author: MTT proof reproduction program
---

# Question

Can the finite selected m=1 gerbe period table be attached to the Iwasawa deck
generators, rather than floating only as an abstract F_3^2 table?

Yes, at the finite deck-quotient/Cech level.

# Construction

Use the active quotient map:

```text
pi(g1) = (1,0),
pi(g2) = (0,1),
pi(g3) = pi(g4) = pi(g5) = pi(g6) = (0,0).
```

Then pull back the already certified finite period table:

```text
B_deck(g,h) = B_1(pi(g), pi(h)),
B_1((a,b),(c,d)) = -c b / 3 mod Z.
```

So only the g1/g2 magnetic square carries the nontrivial third-root torsion
holonomy.  The other deck generators lie in the kernel of this finite torsion
quotient.

# Checks

The executable check verifies:

```text
finite m=1 input table closed: true,
generator-level delta B_deck = 0 on 216 triples,
active quotient delta B_1 = 0 on 729 triples,
pullback matches every finite table entry,
g3..g6 have trivial periods against every generator,
rho(g1) rho(g2) = zeta_3 rho(g2) rho(g1) in the qutrit carrier.
```

The generator period entries include:

```text
B_deck(g1,g2) = 0,
B_deck(g2,g1) = 2/3,
commutator(g1,g2) = 1 mod 3.
```

This is exactly the q79/F clock-shift orientation.

# What This Closes

This closes:

```text
deck generator to F_3^2 quotient map,
finite Cech 2-cocycle on the active deck quotient,
deck pullback of the time-oriented m=1 period table,
compatibility with the qutrit clock-shift projective commutator,
triviality of inactive deck generators in this torsion quotient.
```

The full deck quotient cocycle follows by pullback functoriality:

```text
delta(pi^* B_1) = pi^*(delta B_1) = 0.
```

# What This Does Not Close

This does not claim:

```text
smooth geometric Deligne/Cech representative on the selected cover,
heterotic Green-Schwarz embedding with curvature terms,
Freed-Witten verification on selected cycles,
twisted projector retention for visible SM sectors,
selected D_E,
selected dotD_alpha1,
Riesz/Green operator source,
primitive C1 contractions,
Yukawa or CKM magnitudes,
full SM closure.
```

# Consequence

The previous finite selected period table is now anchored to the deck
generators used by the projective magnetic carrier.  The remaining bridge is
not a finite-cocycle problem anymore; it is the geometric/operator-source
promotion:

```text
finite deck/Cech pullback
  -> smooth selected Deligne/Cech or B-field representative
  -> Freed-Witten and projector retention
  -> selected D_E/dotD/Riesz/Green files.
```

# Artifact

The executable constructor is:

```text
scripts/construct_time_oriented_m1_deck_cech_lift.py
```

It writes:

```text
candidate_data/time_oriented_m1_deck_cech_lift.candidate.json
certificates/time_oriented_m1_deck_cech_lift_certificate.json
```

# Verdict

Closed:

```text
the finite q79/F,m=1 deck/Cech pullback.
```

Open:

```text
the smooth selected visible operator-source packet.
```
