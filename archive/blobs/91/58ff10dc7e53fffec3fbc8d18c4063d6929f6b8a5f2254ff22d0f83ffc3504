---
abstract: |
  We execute the first small-N Route C source-level ansatz search after the
  selected-source promotion gate.  At mesh N=1, for scalar phase exponents over
  F2, F3, F5, and F7, the finite corner path-independence solution space has
  dimension 27.  The source-key-compatible face-graph coboundary image also has
  rank 27, and its equation residual count is zero.  Therefore every certified
  N=1 scalar phase solution is pure gauge at the source level.  Diagonal
  rank-three phase tables and constant-unitary conjugates inherit the same
  obstruction componentwise.  This does not rule out genuinely matrix-valued
  nonabelian transition data or selected D_E-response promotion.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa N=1 Phase Coboundary Obstruction
---

# Purpose

The selected-source promotion gate says:

```text
finite rho_E source promotion fails if the finite face table is a coboundary.
```

The next natural question is whether the small `N=1` scalar phase table branch
contains any non-coboundary flat source candidate.

This note answers that question for the certified prime phase fields:

```text
F2, F3, F5, F7.
```

# Calculation

The executable calculation is:

```text
scripts/analyze_iwasawa_n1_phase_coboundary_obstruction.py
```

It compares two finite vector spaces.

First, it builds the scalar phase corner equations from the existing mesh
validator:

```text
rho_E(g,target) = omega^phi(g,target) I_3.
```

For `N=1` this system has:

```text
unknown face values = 144,
corner equations = 905,
rank = 117,
flat solution dimension = 27.
```

Second, it builds source-key-compatible gauge potentials `U(node)`.  Source-key
compatibility identifies nodes that must give the same `(generator,target)`
table value.  At `N=1` this gives:

```text
source-key gauge components = 28,
component-size histogram = {1: 16, 4: 12}.
```

The induced coboundary map is:

```text
phi(source -> target) = u(target) - u(source).
```

It has:

```text
coboundary image rank = 27,
gauge kernel dimension = 1.
```

# Result

For each certified field:

```text
F2, F3, F5, F7,
```

the coboundary image has zero residual against every corner equation, and:

```text
dim(flat scalar phase solution space) = dim(source-key coboundary image) = 27.
```

Therefore:

```text
flat scalar phase solutions = source-key-compatible coboundaries.
```

# Consequence

The scalar phase branch cannot pass source-level promotion at `N=1`.

The diagonal rank-three phase branch is componentwise scalar, so it inherits
the same obstruction.

The Fourier-rotated phase branch is a constant-unitary conjugate of the
diagonal branch, so it also inherits the same obstruction.

In short:

```text
scalar, diagonal, and constant-rotated phase tables are useful validator tests,
but they cannot be selected rho_E source evidence at N=1.
```

# What This Does Not Rule Out

This is not a no-go theorem for MTT, Route C, or Iwasawa SM closure.  It does
not rule out:

```text
genuinely matrix-valued nonabelian transition data,
larger mesh searches,
typed Cech/monad transition data,
finite HYM/Strominger selected D_E response,
de_response promotion through nonzero dotD source and horizontal response.
```

# Correct Next Move

The next Route C search should leave the phase-table family:

```text
1. search genuinely matrix-valued non-coboundary finite transition data, or
2. construct selected D_E/dotD response data and pass de_response promotion.
```

This is progress because an entire attractive false route is now retired by an
executable rank computation rather than by intuition.
