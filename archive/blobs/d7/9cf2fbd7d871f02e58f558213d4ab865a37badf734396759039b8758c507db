---
abstract: |
  We test whether the selected finite B_q branch that gives CKM-shaped mixing
  also closes quark mass/Yukawa singular-value ratios.  It does not.  The
  selected branch produces hierarchical canonical singular values, but the
  hierarchy is much too shallow for the up sector and still too shallow for the
  down sector compared with the existing benchmark targets in the corpus.
  Therefore the selected B_q branch should be read as a CKM-magnitude/
  localization branch, not as full no-proxy quark mass closure.  Full masses
  require an additional selected action-cost, prefactor, threshold, or RG
  normalization layer.
author:
- Peter Nero
date: June 2026
title: |
  Mass-Hierarchy Diagnostic for the Selected Finite B_q Branch
---

# Purpose

The selected finite B_q branch now fixes:

```text
q = 79 mod 448,
sigma = -1,
Lambda_q = lambda_lens - lambda_nil,
mu_u = 8,
mu_d = 2.
```

It gives CKM-shaped mixing.  This note checks whether it also gives the quark
Yukawa singular-value hierarchy.

# Selected Branch Canonical Singular Values

Because the selected B_q matrix is used with the anchored inverse metric,
the relevant canonical matrix is:

```text
Z_x = Y_x G_A^{-1/2}.
```

Using the selected branch, the normalized singular values of `Z_x` are:

```text
up:   (0.001998, 0.305143, 1)
down: (0.006371, 0.230106, 1)
```

# Corpus Benchmark Ratios

The existing execution benchmark in the corpus uses:

```text
(y_u,y_c,y_t) = (1.2e-5, 1.6e-3, 0.53),
(y_d,y_s,y_b) = (2.2e-4, 5.5e-3, 0.11).
```

Normalized:

```text
up:   (2.26e-5, 0.00302, 1),
down: (0.00200, 0.05000, 1).
```

# Diagnostic Result

The selected finite B_q branch is qualitatively hierarchical but not
mass-closed:

```text
up first ratio:   too large by about 80x,
up second ratio:  too large by about 101x,
down first ratio: too large by about 3.19x,
down second ratio:too large by about 4.60x.
```

# Interpretation

This is not a failure of the CKM branch.  It says the B_q localization branch
does not by itself contain all mass-generating data.

The missing mass layer must be one of:

```text
1. selected action costs per family role,
2. wavefunction prefactors from the full overlap kernel,
3. threshold/RG normalization from the matching scale,
4. Higgs-sector overlap normalization,
5. a further nil/instanton suppression not visible in CKM angles.
```

# What This Closes

```text
selected B_q branch gives CKM-shaped mixing          CHECKED
selected B_q branch alone does not close masses      PROVED-DIAGNOSTIC
additional selected mass layer required              IDENTIFIED
```

# What Remains

```text
derive action-cost/prefactor layer from Sigma_MTT     OPEN
derive absolute Yukawa singular values                OPEN
include RG and threshold normalization                OPEN
```

# Bottom Line

The selected finite B_q branch is a strong CKM-magnitude result, not full SM
mass closure.  The next no-proxy target is:

```text
SelectedMassLayer:
  B_q branch + action/prefactor/RG data
  -> quark singular values.
```
