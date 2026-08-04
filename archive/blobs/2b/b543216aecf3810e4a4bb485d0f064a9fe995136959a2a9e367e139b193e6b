---
title: Execution I EFT Control Status
author:
- Peter Nero
date: May 2026
---

# Claim

Execution I's factorized Kähler corner is algebraically useful for ratio-level
claims, but full large-volume EFT control is not yet certified.

# Executed Values

Execution I records:

```text
t_1 = t_2 ~= 0.94
t_3 ~= 4.11
```

and:

```text
tau_1 = t_2 t_3 ~= 3.86
tau_2 = t_1 t_3 ~= 3.86
tau_3 = t_1 t_2 ~= 0.88
```

The executable audit recomputes:

```text
tau_1 = 3.8634
tau_2 = 3.8634
tau_3 = 0.8836
tau_3/tau_1 = 0.2287104622871046
t_3/t_1 = 4.372340425531915
```

So the ratio geometry is consistent with the claimed `zeta_3/zeta_1 ~= 0.229`.

# Control Status

The source contains a local control statement:

```text
t_3 >> 1,
tau_1,tau_2 = O(1),
moderately anisotropic but controlled internal geometry.
```

But it also later summarizes the EFT regime as:

```text
t_a >> 1.
```

The executed values do not support the stronger statement:

```text
min(t_a) = 0.94
min(tau_a) = 0.8836.
```

Therefore full large-volume control is open.

# Certified Status

The following remains certified:

```text
ratio geometry,
axion decay-constant ratios,
threshold structural consistency.
```

The following is not certified:

```text
suppression of all alpha-prime corrections,
suppression of all loop/localized corrections,
absolute-volume prediction,
full controlled string compactification.
```

# Repair Options

1. Large-volume rescaling:

```text
t_a -> s t_a, with s >> 1.
```

This preserves ratios, but changes absolute volume and therefore requires a
separate normalization certificate.

2. Finite-volume control:

```text
derive explicit correction/error bounds at t_1=t_2 ~= 0.94.
```

This would certify the existing corner without rescaling.

3. Alternative selected corner:

```text
find a source-selected geometry with the same ratio data and all relevant cycles large.
```

This must come from a selection rule, not target fitting.
