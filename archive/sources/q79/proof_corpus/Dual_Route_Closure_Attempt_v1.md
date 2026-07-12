---
abstract: |
  We try both continuations after the SU(5) block-orientation split.  Route A,
  the high-scale SU(5)/E6 whole-multiplet tensor route, remains blocked because
  no selected source currently proves coherent 10_M and bar5_M polarizations.
  Route B, the block-factorized sector-resolved route, is not blocked
  structurally: the current Route C dotD coefficients define a rank-two complex
  linear map from five selected u-versus-d overlap differences to the two CKM
  heavy-link entries Delta_t.  Thus the block route can in principle generate
  CKM leading noncommutation, but the selected overlap/C1 primitive values are
  still absent.
author:
- Peter Nero
date: May 2026
title: |
  Dual Route Closure Attempt
---

# Purpose

After the route split, two honest continuations remain.

Route A:

```text
prove a selected high-scale SU(5)/E6 source
where 10_M and bar5_M are coherent whole multiplets.
```

Route B:

```text
keep the block-factorized SM sector split
Q,L versus u,d,e,N,
then compute selected sector-resolved C1/dotD/overlap contractions.
```

This note tries both.

# Route A Result

Route A still has the same selected-source blocker:

```text
finite tensor available = true,
selected high-scale source closed = false,
block packet sources monolithic tensor = false.
```

Therefore Route A does not close now.  The conditional tensor remains valid,
but it is not selected MTT data.

# Route B Linear Map

For the q79 branch, the heavy-link dependence has the form:

```text
Delta_t13 =
  L0 * A_left_delta
  + R2 * B_right_row1_delta
  + H  * C_higgs_row1_delta

Delta_t23 =
  L1 * A_left_delta
  + R2 * B_right_row2_delta
  + H  * C_higgs_row2_delta.
```

The five difference variables are:

```text
A_left_delta,
B_right_row1_delta,
B_right_row2_delta,
C_higgs_row1_delta,
C_higgs_row2_delta.
```

The computed complex linear map has:

```text
rank = 2,
nullity = 3.
```

The conjugate q369 branch has the conjugate coefficient matrix and the same
rank.

# Meaning

The universal equal-overlap block case gives:

```text
Delta_t = (0,0).
```

But the sector-resolved block route is not forced to stay there.  If selected
geometry supplies non-identical up/down overlap differences, the rank-two map
can reach both heavy-link directions.

The algebraic witnesses in the candidate file show reachability only.  They are
not predictions and are not selected values.

# Remaining Object

The first remaining numeric object is now:

```text
five complex selected u-d overlap-difference slots
for the heavy links,
or an equivalent selected primitive C1 heavy-link packet.
```

Concretely, Route B needs selected values for:

```text
A_left_delta,
B_right_row1_delta,
B_right_row2_delta,
C_higgs_row1_delta,
C_higgs_row2_delta,
```

plus any selected theta, explicit-vertex, or basis-connection differences if
those are nonzero in the selected operator gauge.

# Status

This closes:

```text
Route A blocker identified,
Route B linear dependency computed,
Route B structural nonzero CKM heavy-link possible,
universal equal-overlap zero case confirmed.
```

Still open:

```text
selected high-scale SU(5)/E6 source,
selected Route B overlap differences,
selected C1 heavy-link packet,
Yukawa magnitudes,
full SM closure.
```

# Guardrail

Do not use the algebraic witnesses as predictions.  They prove that Route B
has enough structural rank, not that the selected universe chooses those
numbers.
