---
abstract: |
  We derive the exact remaining mass-layer requirements after the selected
  finite B_q branch.  The B_q branch gives CKM-shaped mixing but leaves the
  canonical weighted quark singular values too shallow.  The missing layer must
  add extra suppressions of order 4.5--4.6 log units in the up sector and
  1.15--1.55 log units in the down sector for the two lighter modes, while
  preserving the selected left-mixing geometry.  A simple family-basis
  non-terminal prefactor can improve singular values but spoils CKM; therefore
  the selected mass layer must be a more constrained action/prefactor/RG
  structure, not a blunt diagonal suppression.
author:
- Peter Nero
date: June 2026
title: |
  Selected Mass-Layer Requirements After the Finite B_q Branch
---

# Purpose

The selected finite B_q branch now gives:

```text
|V_CKM| shaped correctly,
but quark singular-value ratios too shallow.
```

This note converts that statement into quantitative requirements for the next
selected mass layer.

# B_q Canonical Singular Ratios

Use the canonical weighted matrices:

```text
Z_x = Y_x G_A^{-1/2}.
```

The selected finite B_q branch gives normalized singular values:

```text
up:   (0.00199788, 0.30514312, 1),
down: (0.00637144, 0.23010582, 1).
```

The corpus benchmark ratios are:

```text
up:   (0.00002264, 0.00301887, 1),
down: (0.00200000, 0.05000000, 1).
```

# Required Extra Actions

If a missing action layer multiplies the lighter modes by extra factors

```text
exp(-A_{x,1}), exp(-A_{x,2}),
```

then the required log actions are:

```text
A_{u,1} ~= ln(0.00199788 / 0.00002264) ~= 4.480,
A_{u,2} ~= ln(0.30514312 / 0.00301887) ~= 4.616,

A_{d,1} ~= ln(0.00637144 / 0.00200000) ~= 1.159,
A_{d,2} ~= ln(0.23010582 / 0.05000000) ~= 1.527.
```

Thus the missing layer is approximately sector-level:

```text
A_u ~= 4.55,
A_d ~= 1.34,
```

with smaller family splitting inside each sector.

# Simple Family-Basis Prefactor Test

The simplest candidate is:

```text
P_x = diag(exp(-A_x), exp(-A_x), 1)
```

applied on the right family basis of the selected B_q Yukawa matrix.

A scan finds approximate best values:

```text
A_u ~= 4.45,
A_d ~= 1.675.
```

This improves singular values, but it damages CKM:

```text
V_cb grows to about 0.136,
CKM residual grows to about 0.137.
```

Therefore the mass layer cannot be just a blunt non-terminal family-basis
prefactor.

# Mass-Layer Constraint

The selected mass layer must satisfy three constraints:

```text
1. supply the extra light-mode actions above;
2. preserve the selected left-mixing geometry of the B_q branch;
3. come from Sigma_MTT action costs, wavefunction prefactors, Higgs overlap,
   threshold data, or RG normalization, not from observed masses.
```

# Viable Source Classes

The next candidates are:

```text
1. right-singlet action costs aligned with selected right eigenchannels;
2. holomorphic/instanton prefactors in the overlap kernel;
3. Higgs-sector overlap normalization that affects singular values more than
   left mixing;
4. RG/threshold factors that are sector- and family-dependent;
5. nil-survivor finite-width prefactors after sharp CKM projection.
```

# What This Closes

```text
required extra mass actions quantified                 CHECKED
simple family-basis prefactor rejected                 TESTED-NO-GO
mass layer must preserve CKM left geometry             IDENTIFIED
```

# Bottom Line

The next no-proxy target is not another CKM operator.  It is:

```text
SelectedMassLayer:
  approximately A_u ~= 4.55, A_d ~= 1.34 on light modes,
  with CKM-preserving alignment.
```
