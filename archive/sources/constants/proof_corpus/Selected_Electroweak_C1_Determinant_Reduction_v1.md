---
title: Selected Electroweak C1 Determinant Reduction
author:
- Peter Nero
date: May 2026
---

# Claim

The selected electroweak C1 primitive-response problem reduces to one physical
source:

```text
selected index-weighted local determinant response.
```

This does not compute the determinant.  It removes two misleading standalone
slots from the previous scaffold.

# Accounting Principle

One-loop threshold data are not produced by group indices alone, nor by a
purely gravitational curvature scalar alone.  A non-universal gauge threshold
requires a gauge-factor-dependent determinant/spectrum/analytic-torsion
calculation.

Therefore the canonical primitive accounting is:

```text
local_determinant:
  selected determinant/analytic-torsion response,
  including gauge-factor weights and torsion-dependent operator data.

torsion_curvature:
  no standalone non-universal amplitude.

bundle_index:
  no standalone amplitude.
```

# Torsion-Curvature Slot

The selected C1 branch supplies

```text
Tr_grav R_+^2 = v1_tilde alpha_1.
```

This is a scalar curvature source.  By itself it is not labeled by
`U1`, `SU2`, and `SU3`.  The heterotic source says the tree-level gauge kinetic
function is universal:

```text
g^{-2} = Re S
```

up to threshold corrections, and that torsional effects enter through
higher-order `alpha'` and one-loop thresholds that are not computed there.

Thus direct torsion-curvature is either a universal normalization effect or an
input to the gauge-dependent determinant problem.  It is not a separate
non-universal primitive vector.

# Bundle-Index Slot

Topology and representation theory fix charges, anomalies, and beta-function
bookkeeping.  They do not by themselves determine a finite local threshold
amplitude.

In a determinant threshold calculation, group/Dynkin/charge indices weight the
operator determinants.  Without the selected determinant or spectrum, the
index data alone cannot produce `p_U1-p_SU2`.

Thus the standalone bundle-index vector is set to zero in the reduced
primitive accounting.  Its physical role is inside the selected
index-weighted determinant.

# Reduced Template

The determinant-only template is:

```text
certificates/selected_electroweak_c1_response_determinant_only.template.json
```

It fixes:

```text
torsion_curvature = (0,0,0),
bundle_index      = (0,0,0),
scheme_counterterm = (0,0,0),
basis_transport    = (0,0,0).
```

The sole missing physical vector is:

```text
local_determinant = (p_1,p_2,p_3).
```

For weak-angle closure, even this can be reduced to one scalar:

```text
lambda_12 = p_1 - p_2.
```

Then:

```text
Delta_G,12 = v1_tilde lambda_12/(4pi).
```

# Remaining Gate

The remaining gate is now:

```text
selected C1 local determinant / analytic torsion
  -> p_U1 - p_SU2.
```

The diagnostic target from Execution I corresponds to:

```text
p_U1 - p_SU2 = 2.194153126940556.
```

That number remains a target-response witness, not a prediction, until the
selected determinant calculation produces it.

# Certified Status

```text
PEW_ALPHA1_REDUCED_TO_SELECTED_LOCAL_DETERMINANT
```

