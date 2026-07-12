---
abstract: |
  We test whether the canonical anchored-bridge seed can become CKM-like by
  adding only scalar quark stiffness multipliers to the anchor profile.  The
  diagnostic scans bridge amplitudes C_u[b]=exp(-mu_u J_b) tau^b and
  C_d[b]=exp(-mu_d J_b) tau^(2b), with the universal anchored metric retained.
  This two-scale stiffness family remains large-mixing over the tested range
  and does not approach CKM-like hierarchy.  Therefore a scalar stiffness
  multiplier is not enough.  The next source must be selected localization
  separation, nonuniform bridge geometry, additional finite channel classes,
  or a more detailed theta/lens/nil/proto-spinor operator.
author:
- Peter Nero
date: June 2026
title: |
  Scalar Quark-Stiffness Diagnostic No-Go for the Anchored Bridge Seed
---

# Purpose

The canonical anchored seed gave large mixing.  The corpus says quarks are
stiff, partially anchored composite sectors.  The first mathematical test is:

```text
Can scalar quark stiffness alone make the anchored bridge seed CKM-like?
```

# Stiffness Family

Use:

```text
J = (0, lambda_nil/lambda_lens, 1).
```

For two scalar stiffnesses:

```text
mu_u, mu_d > 0,
```

define:

```text
C_u[b] = exp(-mu_u J_b) tau^b,
C_d[b] = exp(-mu_d J_b) tau^(2b).
```

The universal anchored metric is fixed:

```text
G_A^{-1} = diag(exp(-2J_b)).
```

No matrix entries are adjusted.

# Diagnostic Result

The scan over:

```text
0.1 <= mu_u, mu_d <= 12
```

does not produce a CKM-like matrix.  The best grid point in the audit remains
far from the quark target and still has large off-diagonal mixing.

Thus:

```text
scalar stiffness suppresses bridge weights,
but does not create the observed CKM hierarchy.
```

# Interpretation

This is another narrowing result:

```text
pure bridge symmetry: no CKM;
universal anchored seed: large mixing;
scalar quark stiffness: still large mixing.
```

Therefore the missing MTT source is more structured than one scalar stiffness.
The next viable sources are:

```text
sector-dependent localization centers,
nonuniform bridge geometry,
multiple selected channel classes,
anisotropic lens/nil wavefunction widths,
or an explicit proto-spinor localization operator whose eigenmodes are not
pure Z3 bridge modes.
```

# What This Closes

```text
scalar stiffness-only rescue                         TESTED
simple two-scale anchored bridge family              NOT CKM-LIKE
need for structured localization/channel source      IDENTIFIED
```

# What Remains

```text
derive selected localization centers                  OPEN
derive nonuniform bridge distances                    OPEN
derive additional finite channels if present          OPEN
compute CKM from frozen Sigma_MTT                     OPEN
```

# Bottom Line

Quark stiffness is real in the corpus, but it cannot enter as only one scalar
multiplier on the simple bridge profile.  The quark sector needs structured
selected geometry.

