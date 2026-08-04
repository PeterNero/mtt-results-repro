---
abstract: |
  We derive the finite up-sector residual label pattern needed by the
  right-channel mass source schema, conditional on identifying the up-sector
  right-channel light pair with the selected retarded spinorial return doublet.
  A spinorial return residue has two eigenvalues, -1 and +1.  Retarded
  predecessor orientation shifts the doublet by a common half-step offset.
  Multiplying by the already selected anchor scale J=lambda_nil/lambda_lens
  gives the light-channel labels (-3/2 J,+1/2 J).  This proves the label
  pattern from existing MTT ingredients once the concrete source map assigns
  the up light right channels to this spinorial doublet.
author:
- Peter Nero
date: June 2026
title: |
  Up-Sector Retarded Spinorial Right-Channel Label Theorem
---

# Purpose

The finite-label source schema needs:

```text
spec_light(R_u) = (-3/2 J, +1/2 J),
J = lambda_nil/lambda_lens.
```

This note derives that label pattern from two already-used structures:

```text
1. terminal spinorial return parity;
2. retarded predecessor half-step orientation.
```

# Inputs

The terminal spinorial return theorem proves that the selected dyadic tower
has a terminal spinorial parity:

```text
epsilon in {-1,+1}.
```

The anchored metric source fixes the dimensionless anchor scale:

```text
J = lambda_nil/lambda_lens.
```

The selected CKM branch uses retarded predecessor orientation.  At the level of
the light right-channel doublet, a retarded half-step offset is represented by:

```text
-1/2 I_light.
```

# Source Operator

Let `P_{u,1}` and `P_{u,2}` be the two light right-channel spectral projectors.
Define the spinorial sign operator:

```text
Xi_u = -P_{u,1} + P_{u,2}.
```

Then:

```text
spec(Xi_u) = {-1,+1}
```

on the light doublet.

The retarded spinorial source is:

```text
R_u = J(-1/2 I_light + Xi_u).
```

# Theorem

Assume:

1. the up-sector light right-channel pair is the selected retarded spinorial
   doublet;

2. the spinorial sign operator on that pair is `Xi_u`;

3. retarded predecessor orientation contributes the common half-step offset
   `-1/2 I_light`;

4. the dimensionless scale of the split is the selected anchor scale
   `J=lambda_nil/lambda_lens`.

Then:

```text
spec_light(R_u) = (-3/2 J, +1/2 J).
```

# Proof

The eigenvalues of `Xi_u` on the light doublet are `-1` and `+1`.  Therefore
the eigenvalues of:

```text
-1/2 I_light + Xi_u
```

are:

```text
-1/2 - 1 = -3/2,
-1/2 + 1 = +1/2.
```

Multiplying by `J` gives:

```text
(-3/2 J,+1/2 J).
```

# Status

```text
spinorial parity eigenvalues                     PROVED
retarded half-step operator form                  FORMULATED
up finite labels from those inputs                PROVED-CONDITIONAL
assignment of up light right channels to Xi_u     OPEN
```

# Bottom Line

The up-sector labels are no longer arbitrary numbers.  They are the finite
spectrum of:

```text
J(-1/2 I_light + spinorial parity).
```

The remaining extraction task is to show that `Sigma_MTT` assigns the up
weighted right-channel light pair to this retarded spinorial doublet.

