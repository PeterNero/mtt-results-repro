---
abstract: |
  We add a diagnostic that attempts to trivialize a finite-mesh rho_E table on
  the validator face graph as rho(source->target)=U(source)^(-1)U(target).
  This separates validator capacity from physical content.  The pure-gauge
  nonabelian prototype has noncommuting face matrices, but the diagnostic finds
  a face-graph coboundary trivialization with 64 nodes, 192 boundary
  incidences, 144 unique face keys, and one connected graph component at N=1.
  The Fourier-rotated phase prototype also trivializes.  A deliberately
  corrupted cycle candidate is rejected.  Therefore noncommuting finite table
  data are not sufficient for selected SM closure; future candidates must pass
  this guardrail and still come from selected Cech/monad or HYM/Strominger
  source data with nontrivial D_E response.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Face-Graph Coboundary Diagnostic
---

# Purpose

The pure-gauge nonabelian prototype proved:

```text
the finite validator stack can carry noncommuting rho_E tables.
```

But noncommuting face matrices are not enough.  A table can be noncommuting and
still be a finite coboundary:

```text
rho(source -> target) = U(source)^(-1) U(target).
```

This note adds the diagnostic that detects that case.

# Diagnostic

The script:

```text
scripts/detect_iwasawa_face_graph_coboundary.py
```

loads a finite `rho_E` table, builds the same boundary face graph used by the
mesh validator, and tries to solve for node gauges:

```text
U(node).
```

For each boundary incidence it checks:

```text
rho_E(source -> target) = U(source)^(-1) U(target).
```

If all graph cycles are consistent, the table is a face-graph coboundary.

# N=1 Graph Counts

At `N=1`, the face graph has:

```text
closed nodes = 64,
boundary face incidences = 192,
unique face keys = 144,
connected graph components = 1.
```

These are different from the source-key equivalence components used to
construct the pure-gauge prototype.  The source-key equivalence enforced
well-defined `(generator,target)` values; the face graph diagnostic tests
whether those values are globally gauge-trivial on the finite graph.

# Prototype Results

The pure-gauge nonabelian prototype is detected as:

```text
face_graph_coboundary = true.
```

The Fourier-rotated phase prototype is also detected as:

```text
face_graph_coboundary = true.
```

A deliberately corrupted cycle candidate is detected as:

```text
face_graph_coboundary = false.
```

# What This Closes

This closes a false-positive guardrail:

```text
noncommuting finite rho_E values alone do not prove selected nontrivial bundle
data or physical family mixing.
```

Equivalently, noncommuting finite table data are not sufficient for selected
SM closure.

The diagnostic can now be used before promoting any future finite `rho_E`
candidate.

# What This Does Not Close

This diagnostic does not construct:

```text
selected rho_E,
selected D_E,
typed Cech/monad transition data,
HYM/Strominger residual solution,
Riesz/Green/dotD response,
primitive C1 contractions,
SM masses or CKM magnitudes.
```

# Correct Way Forward

The next candidate must do more than pass mesh, metric, and sector validators.
It must either:

```text
1. fail the face-graph coboundary diagnostic in a controlled way while still
   satisfying the selected source residuals, or
2. supply a selected D_E/HYM/Strominger response that is not erased by the
   finite graph trivialization.
```

The correct next source remains:

```text
typed Cech/monad data or a finite HYM/Strominger residual solve.
```

In short, the next admissible source must be not merely pure gauge.
