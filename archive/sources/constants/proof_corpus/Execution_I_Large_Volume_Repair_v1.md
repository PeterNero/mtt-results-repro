---
title: Execution I Large-Volume Repair
author:
- Peter Nero
date: May 2026
---

# Claim

Execution I's ratio geometry admits a clean large-volume repair:

```text
t_a -> s t_a.
```

This preserves the ratio-level results while moving the absolute normalization
into the explicit normalization gate.

# Scaling Rules

For:

```text
tau_1 = t_2 t_3
tau_2 = t_1 t_3
tau_3 = t_1 t_2
Vol = t_1 t_2 t_3
```

the common rescaling gives:

```text
tau_a -> s^2 tau_a
Vol -> s^3 Vol.
```

Therefore:

```text
tau_i/tau_j is preserved,
t_i/t_j is preserved,
axion decay-constant ratios are preserved.
```

# Threshold Direction

The bulk threshold direction is:

```text
log(tau_a) - <log tau>.
```

Under `tau_a -> s^2 tau_a`:

```text
log(s^2 tau_a) - <log(s^2 tau)>
= log(tau_a) + 2 log(s) - (<log tau> + 2 log(s))
= log(tau_a) - <log tau>.
```

So the bulk threshold direction is preserved exactly.

# Example Repairs

Using the rounded Execution I values:

```text
t_1 = t_2 = 0.94
t_3 = 4.11
tau_3 = 0.8836
Vol = 3.631596
```

we get:

```text
s = 2  -> min(t) = 1.88, min(tau) = 3.5344, Vol = 29.052768
s = 5  -> min(t) = 4.7,  min(tau) = 22.09,  Vol = 453.9495
s = 10 -> min(t) = 9.4,  min(tau) = 88.36,  Vol = 3631.596
```

# Normalization Cost

Execution I uses:

```text
Vol/g_10^2 = K/(4pi).
```

If `K` is kept fixed while `Vol -> s^3 Vol`, then:

```text
g_10 -> s^(3/2) g_10.
```

So large-volume repair is not a new absolute prediction.  It is a valid
ratio-preserving representative, but it shifts the unsolved question into the
absolute normalization of `g_10` or volume.

# Certified Status

Certified:

```text
large-volume ratio repair,
axion-ratio preservation,
bulk-threshold direction preservation.
```

Not certified:

```text
selected s,
selected absolute volume,
selected g_10,
absolute f_a,
G_N or M_Pl.
```

The correct branch is therefore:

```text
use large-volume representatives for ratio/threshold consistency,
keep absolute constants behind the normalization gate.
```
