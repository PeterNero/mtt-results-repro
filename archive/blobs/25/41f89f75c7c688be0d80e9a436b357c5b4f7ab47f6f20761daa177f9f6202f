---
abstract: |
  We construct the first genuinely noncommuting finite-mesh rho_E table in the
  Route C validator stack.  The construction is pure gauge:
  rho(source->target)=U(source)^*U(target), after quotienting source nodes that
  share the same (generator,target) face key.  At mesh N=1 this source-key
  equivalence has 28 components over 64 closed nodes.  Assigning block-unitary
  gauges from block diag(1,<Pauli X,Z>) gives 144 face values, 70 nonidentity
  values, 36 off-diagonal values, and max pairwise commutator 2.0.  The emitted
  candidate passes the rho_E mesh validator, Hermitian metric validator, and
  sector projection validator with H=I and a common rank-one Higgs line.  This
  proves the finite validator stack can carry noncommuting table data.  It does
  not prove selected MTT rho_E or physical flavor mixing, because the candidate
  is pure gauge.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Pure-Gauge Nonabelian Mesh rho_E Prototype
---

# Purpose

The Fourier-rotated phase prototype had off-diagonal entries but still
commuted.  The next question is sharper:

```text
can the finite rho_E validator stack carry genuinely noncommuting table data?
```

This note answers yes, while keeping the crucial guardrail:

```text
the candidate is pure gauge and unselected.
```

# Source-Key Equivalence

The finite-mesh validator looks up a face transition by:

```text
(generator,target).
```

For a pure-gauge construction:

```text
rho(source -> target) = U(source)^* U(target),
```

this lookup is well-defined only if all source nodes sharing the same
`(generator,target)` key have the same gauge value.

At `N=1`, the source-key equivalence has:

```text
closed nodes = 64,
face keys = 144,
equivalence components = 28,
component size histogram = {1:16, 4:12}.
```

This leaves enough freedom to choose noncommuting gauge values.

# Nonabelian Gauge Assignment

Use the block-unitary generators:

```text
A = block diag(1, X),
B = block diag(1, Z),
```

where `X,Z` are the Pauli swap and sign matrices on the last two fiber
coordinates.

These preserve the first line, but do not commute on the lower two-dimensional
block.

Assign component gauges cyclically from:

```text
I, A, B, A B.
```

Then emit:

```text
rho(source -> target) = U(source)^* U(target).
```

# Prototype Counts

The generated table has:

```text
face values = 144,
nonidentity face values = 70,
off-diagonal face values = 36,
max pairwise commutator = 2.0.
```

The nonidentity values split as:

```text
g1: 3,
g2: 3,
g3: 24,
g4: 24,
g5: 8,
g6: 8.
```

The off-diagonal values split as:

```text
g1: 2,
g2: 2,
g4: 24,
g6: 8.
```

# Validator Result

The audit writes a temporary candidate and runs:

```text
scripts/validate_iwasawa_rhoE_mesh.py,
scripts/validate_iwasawa_rhoE_metric.py,
scripts/validate_iwasawa_sector_maps.py.
```

All three pass.

The metric is:

```text
H = I_3.
```

The sector maps are:

```text
P_Q=P_u=P_d=P_L=P_e=P_N=I_3,
P_H=diag(1,0,0).
```

The Higgs line is valid because every block-unitary gauge preserves the first
fiber coordinate.

# What This Achieves

This closes a validator-capability result:

```text
finite mesh rho_E tables can be noncommuting and still pass mesh, metric, and
sector gates.
```

So the proof stack is not limited to abelian, diagonal, or merely
simultaneously diagonalizable test data.

# What This Does Not Achieve

The construction is pure gauge:

```text
rho(source -> target) = U(source)^* U(target).
```

Therefore the path independence is built in, and no selected HYM/Strominger
source has been found.  It does not provide:

```text
selected rho_E,
selected D_E,
physical family mixing,
nontrivial curvature response,
Riesz/Green/dotD data,
primitive C1 contractions,
Yukawa or CKM magnitude predictions,
full SM closure.
```

# Correct Way Forward

The next target is no longer "can the stack carry noncommuting matrices?"  It
can.

The next target is:

```text
find selected nonabelian transition data that are not merely pure gauge,
from typed Cech/monad maps or a finite HYM/Strominger residual solve.
```

Only then should the candidate feed `D_E`, Riesz/Green, dotD, and primitive C1
response matrices.
