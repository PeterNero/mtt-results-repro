---
abstract: |
  After obstructing the first constant rank-three scalar-central Wilson ansatz,
  we test whether the finite table-valued rho_E route is empty.  It is not.
  On the N=1 Iwasawa closed-cell mesh, scalar phase transition tables
  rho_E(g,target)=omega^phi(g,target) I_3 over F_3 give a linear corner
  cocycle system with 144 face-value unknowns, 905 path-independence equations,
  rank 117, and nullity 27.  The first nullspace basis vector has four
  nonzero face values and passes both the finite-mesh rho_E validator and the
  Hermitian metric validator with H=I.  This is a prototype only: scalar phases
  cannot supply the non-scalar rank-three family structure, sector maps, D_E,
  or SM Yukawa/CKM data.  Its value is methodological: Route C should now
  search table-valued, typed Cech/monad, or higher-carrier quotient data rather
  than a single constant Wilson matrix.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Scalar-Phase Mesh rho_E Prototype
---

# Purpose

The constant rank-three scalar-central Wilson ansatz is now obstructed.
That does not mean the finite `rho_E` branch is dead.  The finite-mesh
validator allows boundary-target tables:

```text
rho_E(g,target).
```

This note checks the smallest scalar table-valued version:

```text
rho_E(g,target) = omega^phi(g,target) I_3,
phi(g,target) in F_3.
```

It is intentionally modest.  It is not selected MTT bundle data.

# Linear Cocycles

For every corner node, the finite-mesh validator compares all reduction
orders.  In scalar phase form, matrix products become additive equations:

```text
sum phi(path A) = sum phi(path B) mod 3.
```

The solver:

```text
scripts/solve_iwasawa_scalar_phase_mesh.py
```

constructs exactly those equations from the same face maps used by:

```text
scripts/validate_iwasawa_rhoE_mesh.py.
```

For `N=1`, the system is:

```text
unknown face values = 144,
corner equations = 905,
rank = 117,
nullity = 27,
target mismatches = 0.
```

The unknowns split as:

```text
g1: 8,
g2: 8,
g3: 32,
g4: 32,
g5: 32,
g6: 32.
```

# Prototype Candidate

The first nullspace basis vector has:

```text
nonzero face entries = 4,
g1: 0,
g2: 0,
g3: 1,
g4: 1,
g5: 1,
g6: 1.
```

It has zero linear residuals:

```text
candidate row residuals = 0.
```

The generated prototype file is temporary in the audit, then checked by:

```text
scripts/validate_iwasawa_rhoE_mesh.py,
scripts/validate_iwasawa_rhoE_metric.py.
```

Both validators pass.  The metric check uses:

```text
H = I_3,
```

which is compatible because the prototype is unitary scalar phase data.

# What This Achieves

This proves a useful narrow fact:

```text
the table-valued finite rho_E route is not empty at mesh N=1.
```

It also demonstrates that the existing mesh and metric validators can accept a
nontrivial finite cocycle that is not merely the identity schema smoke test.

# What This Does Not Achieve

The prototype is scalar on the fiber:

```text
rho_E(g,target) proportional to I_3.
```

Therefore it does not provide:

```text
rank-three family splitting,
sector projections Q,u,d,L,e,N,H,
selected D_E,
Riesz/Green/dotD data,
primitive C1 response matrices,
Yukawa magnitudes,
CKM angles,
full SM closure.
```

It must not be promoted to selected data.

# Correct Way Forward

The immediate lesson is positive but disciplined:

```text
constant scalar-central rank-three Wilson carrier: retired,
table-valued finite rho_E branch: viable,
scalar table prototype: useful but not selected.
```

The next step is to add non-scalar structure by one of three routes:

```text
1. typed Cech/monad transition tables,
2. a higher auxiliary finite-Heisenberg carrier with a selected rank-three quotient,
3. a direct HYM/Strominger residual solve varying rho_E and H together.
```

Only a candidate from one of those routes should feed sector maps, `D_E`,
Riesz/Green response, and primitive C1 contraction blocks.
