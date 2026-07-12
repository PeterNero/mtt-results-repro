---
abstract: |
  We derive the finite down-sector residual label pattern needed by the
  right-channel mass source schema, conditional on identifying the down-sector
  light right-channel pair with the selected dyadic survivor-width channel and
  the selected nil half-channel.  The exact Z64 branch supplies the dyadic
  projector normalization 1/64.  The nil/color Schur-completion logic supplies
  half-channel nil costs; a three-half-channel nil completion gives
  3/2 lambda_nil.  Thus the down labels are (1/64,3/2 lambda_nil) once the
  concrete source map assigns the first light channel to the dyadic survivor
  projector and the second to the nil half-channel projector.
author:
- Peter Nero
date: June 2026
title: |
  Down-Sector Dyadic/Nil Right-Channel Label Theorem
---

# Purpose

The finite-label source schema needs:

```text
spec_light(R_d) = (1/64, 3/2 lambda_nil).
```

This note derives the label values from selected MTT ingredients:

```text
1. the exact Z64 dyadic branch;
2. nil-survivor half-channel completion.
```

# Dyadic Survivor-Width Label

The exact Z64 central-circle branch supplies character projectors:

```text
E_q = (1/64) sum_{r=0}^{63} exp(-2 pi i q r/64) U_64^r.
```

The coefficient:

```text
1/64
```

is the intrinsic normalized dyadic survivor-width scale of the selected
order-64 carrier.

Thus a right-channel source supported on the selected dyadic survivor-width
projector contributes:

```text
(1/64) P_dyad.
```

# Nil Half-Channel Label

The color-singlet Schur-completion theorem already uses hidden half-channel
completion:

```text
delta^2 -> delta^2/2.
```

For a nil survivor role, the conservative nil floor is:

```text
lambda_nil.
```

Three nil half-channels therefore contribute:

```text
3 * (1/2 lambda_nil) = 3/2 lambda_nil.
```

This is the smallest nontrivial threefold nil completion compatible with the
quark color/nil redundancy count and half-channel Schur accounting.

# Source Operator

Let `P_dyad` and `P_nil` be the two light down-sector weighted right-channel
spectral projectors selected by the dyadic survivor-width and nil half-channel
labels.  Define:

```text
R_d = (1/64) P_dyad + (3/2 lambda_nil) P_nil.
```

# Theorem

Assume:

1. the first down light right channel is selected by the order-64 dyadic
   survivor-width projector;

2. the second down light right channel is selected by the three-half-channel
   nil completion projector;

3. the source operator is diagonal in the weighted right-channel basis.

Then:

```text
spec_light(R_d) = (1/64, 3/2 lambda_nil).
```

# Proof

By assumption 1, the dyadic light projector carries the normalized order-64
projector weight `1/64`.

By assumption 2, the nil light projector carries three half-channel nil costs:

```text
3*(lambda_nil/2)=3/2 lambda_nil.
```

Since the projectors are orthogonal and diagonal in the weighted right-channel
basis, the light spectrum of `R_d` is exactly:

```text
(1/64,3/2 lambda_nil).
```

# Status

```text
dyadic 1/64 projector scale                         IMPORTED/PROVED
nil half-channel accounting                         IMPORTED/PROVED-SCHEMA
down finite labels from those inputs                PROVED-CONDITIONAL
assignment of down light channels to dyadic/nil     OPEN
```

# Bottom Line

The down-sector labels are not free real parameters.  They have a compact MTT
reading:

```text
first light channel  -> dyadic survivor-width 1/64,
second light channel -> three nil half-channels 3/2 lambda_nil.
```

The remaining extraction task is to prove that `Sigma_MTT` assigns the down
weighted right-channel light projectors to those two selected sources.

