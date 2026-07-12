---
abstract: |
  We strengthen the scalar phase mesh prototype by placing three independent
  finite scalar cocycles on the diagonal of a rank-three rho_E table.  At N=1
  over F_3, the underlying scalar system has 144 face values, 905 corner
  equations, rank 117, and nullity 27.  Using scalar nullspace basis vectors
  0,1,2 gives a diagonal rank-three prototype with 10 nonzero face values, all
  10 nonscalar across the fiber, and zero component residuals.  The generated
  candidate passes both the finite-mesh rho_E validator and the Hermitian metric
  validator with H=I.  This proves that the table-valued route can distinguish
  rank-three fiber components, but it still does not provide selected MTT
  rho_E, off-diagonal family mixing, sector maps, D_E, or SM closure.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Diagonal Phase Mesh rho_E Prototype
---

# Purpose

The scalar phase prototype showed that nontrivial table-valued finite cocycles
exist.  Its weakness is that it acts as:

```text
rho_E(g,target) = omega^phi(g,target) I_3.
```

This note tests the next simplest rank-three lift:

```text
rho_E(g,target) =
diag(omega^phi_1(g,target),
     omega^phi_2(g,target),
     omega^phi_3(g,target)).
```

Each diagonal component is an independent scalar finite-mesh cocycle.

# Construction

The constructor:

```text
scripts/construct_iwasawa_diagonal_phase_mesh.py
```

imports the scalar phase linear system and chooses nullspace basis vectors:

```text
0, 1, 2.
```

At `N=1`, the underlying system remains:

```text
unknown face values = 144,
corner equations = 905,
rank = 117,
scalar nullity = 27,
target mismatches = 0.
```

The three diagonal components have:

```text
component nonzero entries = [4,4,4],
component row residuals = [0,0,0].
```

The resulting diagonal table has:

```text
nonzero face values = 10,
nonscalar face values = 10.
```

The nonzero generator split is:

```text
g1: 0,
g2: 0,
g3: 3,
g4: 3,
g5: 2,
g6: 2.
```

# Validator Result

The audit emits the candidate into a temporary JSON file, then runs:

```text
scripts/validate_iwasawa_rhoE_mesh.py,
scripts/validate_iwasawa_rhoE_metric.py.
```

Both validators pass.

The Hermitian metric is:

```text
H = I_3.
```

This works because every diagonal entry is a unitary phase.

# What This Achieves

This closes a stronger prototype fact:

```text
the finite table-valued rho_E route supports non-scalar rank-three diagonal
fiber data at mesh N=1.
```

So the table-valued route is not merely a scalar identity-like toy.  It can
separate the three fiber components while satisfying finite corner cocycle and
metric compatibility gates.

# What This Still Does Not Achieve

The construction is diagonal.  Therefore it still does not supply:

```text
off-diagonal family mixing,
selected sector projectors,
selected D_E action,
Riesz/Green/dotD response,
primitive C1 contraction blocks,
Yukawa magnitudes or CKM angle magnitudes,
full SM closure.
```

It is not selected data and must not be used as a proxy for observed flavor.

# Correct Way Forward

This result changes the next search target:

```text
constant scalar-central Wilson data: obstructed,
scalar table cocycle: viable but too weak,
diagonal rank-three table cocycle: viable but still no off-diagonal response.
```

The next rigorous move is to seek nonabelian table data from one of:

```text
typed Cech/monad transition functions,
HYM/Strominger finite residual solve,
higher auxiliary carrier with selected rank-three quotient.
```

Only after such a source passes the same mesh and metric validators should it
feed sector maps, `D_E`, Riesz/Green, dotD, and C1 response matrices.
