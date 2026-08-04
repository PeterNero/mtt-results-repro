---
title: Selected Electroweak Local Projection Gate
author:
- Peter Nero
date: May 2026
---

# Claim

The local/exceptional part of the selected electroweak threshold kernel reduces
to a two-coefficient trace-free projection problem.

This closes the projection algebra, but it does not yet close the numerical
electroweak prediction.

# Source Form

Execution I writes the exceptional threshold sector as

```text
Delta_a^exc = sum_I c_I chi_a^(I),
```

where the `chi_a^(I)` are fixed topological charge vectors associated with
exceptional divisors or localized curvature, and the coefficients `c_I` are
still to be determined.

The same source imposes

```text
sum_a chi_a^(I) = 0.
```

Thus the exceptional sector is trace-free and cannot change the common gauge
normalization slot `K` or `kappa_EW`.  It can only split the gauge factors.

# Selected Two-Direction Basis

The threshold certificate uses the two independent trace-free directions

```text
chi_1 = (1, -1, 0)
chi_2 = (0, 1, -1).
```

Therefore a general local exceptional correction in this basis is

```text
Delta_alpha^exc(c1,c2)
  = c1 (1,-1,0) + c2 (0,1,-1)
  = (c1, -c1 + c2, -c2).
```

The electroweak `1-2` split is consequently

```text
Delta_alpha,1^exc - Delta_alpha,2^exc = 2 c1 - c2.
```

In the inverse-coupling convention used by the electroweak kernel,

```text
Delta_G,12^exc = (2 c1 - c2) / (4 pi).
```

# Execution I Diagnostic Value

Execution I uses

```text
c1 = 0.31,
c2 = -0.27.
```

This gives

```text
Delta_alpha^exc = (0.31, -0.58, 0.27),
Delta_alpha,12^exc = 0.89,
Delta_G,12^exc = 0.07082394967589342.
```

This is a useful diagnostic and matches the prior electroweak kernel candidate
audit.  It is not a no-knob prediction, because these coefficients are not
independently selected by the current corpus.

# What This Closes

The following parts are now closed:

```text
trace-free exceptional plane
selected two-direction basis
local electroweak 1-2 projection formula
conversion from Delta_alpha to Delta_G
```

The following part remains open:

```text
selected geometry/flux/curvature/torsion/determinant data
  -> c1, c2
  -> numeric local electroweak threshold split.
```

# Consequence for Full Electroweak Closure

The electroweak kernel has the form

```text
G_a(MZ)
  = kappa_EW zeta_a
  + Delta_a^bulk
  + Delta_a^exc(c1,c2)
  + b_a/(8 pi^2) log(mu_Theta/MZ).
```

The bulk threshold direction found so far has equal first and second entries.
Therefore the direct local source of the electroweak `1-2` split is the
exceptional projection

```text
(2 c1 - c2)/(4 pi).
```

To turn this into a strict no-knob electroweak prediction, the next proof must
compute `c1` and `c2` from selected localized data rather than importing them
from matching.

# Certified Status

```text
ELECTROWEAK_LOCAL_PROJECTION_FORMULA_CLOSED_COEFFICIENTS_OPEN
```

