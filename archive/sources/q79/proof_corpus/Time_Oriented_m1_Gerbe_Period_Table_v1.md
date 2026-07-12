---
title: |
  Time-Oriented m=1 Gerbe Period Table
author: MTT proof reproduction program
---

# Question

Can the time-oriented q79/F gerbe source be made more explicit than the label:

```text
m = 1?
```

Yes, at the finite quotient level.

# Construction

The selected finite quotient is:

```text
G = F_3^2.
```

For elements:

```text
g = (a,b),  h = (c,d),
```

the selected retarded representative is the period table:

```text
B_1(g,h) = -c b / 3  mod Z.
```

Equivalently, the holonomy is:

```text
Hol_1(g,h) = exp(2 pi i B_1(g,h)).
```

The script writes the complete 9-by-9 period and holonomy tables.

# Checks

The executable check verifies:

```text
normalization:       B_1(0,g)=B_1(g,0)=0,
finite Bianchi:     delta B_1 = 0 on all 729 triples,
commutator matrix:  [[0,1],[2,0]] over F_3,
rank:               2,
ordinary coboundary possible: false.
```

The commutator matrix is the qutrit Fourier/Heisenberg orientation selected by
the q79/F branch.  The antiunitary conjugate q369/F* is retained with:

```text
m = 2,
commutator matrix [[0,2],[1,0]].
```

# What This Closes

This closes the finite source-origin table:

```text
actual finite B-field period table on the selected quotient,
map from m=1 to the zeta_3 qutrit cocycle,
finite flat discrete Bianchi identity,
ordinary-bundle coboundary escape.
```

This is stronger than a lifted selected-source flag.  It is an explicit finite
table with a verified cocycle law.

# What This Does Not Close

This does not claim:

```text
full geometric Deligne/Cech representative on the Iwasawa/Strominger cover,
full heterotic Green-Schwarz embedding,
Freed-Witten verification on selected cycles,
twisted projector retention,
selected D_E,
selected dotD_alpha1,
Riesz/Green operator source,
primitive C1 contractions,
Yukawa magnitudes,
full SM closure.
```

# Consequence

The source-origin blocker is now narrower.  The finite gerbe period table is
no longer missing.  The remaining bridge is geometric/operator-theoretic:

```text
finite selected period table
  -> selected geometric Deligne/Cech or B-field representative
  -> Freed-Witten and projector retention
  -> selected D_E/dotD/Riesz/Green files.
```

# Artifact

The executable constructor is:

```text
scripts/construct_time_oriented_m1_gerbe_period_table.py
```

It writes:

```text
candidate_data/time_oriented_m1_gerbe_period_table.candidate.json
certificates/time_oriented_m1_gerbe_period_table_certificate.json
```

# Verdict

Closed:

```text
the selected q79/F, m=1 finite gerbe period table.
```

Open:

```text
the full selected visible operator-source packet.
```
