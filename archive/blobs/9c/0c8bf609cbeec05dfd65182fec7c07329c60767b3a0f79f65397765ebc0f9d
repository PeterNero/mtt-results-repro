---
title: Execution I Threshold Profile Structural Certificate
author:
- Peter Nero
date: May 2026
---

# Claim

Execution I gives a structural threshold-profile consistency check.

The bulk threshold direction is:

```text
Delta_a^bulk = delta (log tau_a - <log tau>)
```

with:

```text
delta = -25.2 +/- 0.5.
```

The exceptional sector is:

```text
Delta_a^exc = sum_I c_I chi_a^(I).
```

# Executed Exceptional Vector

Execution I chooses:

```text
chi_1 = (1, -1, 0)
chi_2 = (0, 1, -1)
c_1 = 0.31
c_2 = -0.27
```

Therefore:

```text
Delta_exc = 0.31(1,-1,0) - 0.27(0,1,-1)
          = (0.31, -0.58, 0.27).
```

This vector has:

```text
sum_a Delta_a^exc = 0.
```

So it preserves the overall scale `K`.

# Smallness Check

Execution I reports:

```text
Delta_bulk ~= (-12.3, -12.3, 24.9).
```

The executable audit computes:

```text
||Delta_exc|| = 0.7109149034870489
||Delta_bulk|| = 30.37416665523517
||Delta_exc|| / ||Delta_bulk|| = 0.02340524800421211
```

This supports the paper's claim that the exceptional correction is at the
few-percent level.

# No-Knob Status

This is not certified as a new no-knob prediction.

The reason is simple: Execution I says the exceptional coefficients are obtained
by solving for exact matching at two scales.  Unless a later source derives
`c_1` and `c_2` directly from selected topology or flux data, they should be
treated as consistency coefficients, not as independently predicted constants.

# Certified Status

The certified claim is:

```text
selected threshold ansatz
-> small exceptional vector
-> scale-preserving structural consistency.
```

The not-yet-certified claim would be:

```text
selected topology/flux data
-> c_1, c_2
-> threshold profile prediction.
```

# Remaining Closure Step

To upgrade the sector, supply a source-certified derivation of the exceptional
charge vectors and coefficients from selected geometry, topology, flux, or
localized curvature data, without fitting the target threshold profile.
