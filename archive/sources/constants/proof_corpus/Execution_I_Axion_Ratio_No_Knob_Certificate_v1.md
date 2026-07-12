---
title: Execution I Axion Ratio No-Knob Certificate
author:
- Peter Nero
date: May 2026
---

# Claim

Execution I gives a ratio-level, no-knob axion result in the factorized
three-modulus corner.

The source uses:

```text
tau_1 = t_2 t_3
tau_2 = t_1 t_3
tau_3 = t_1 t_2
```

and:

```text
f_a proportional to 1/tau_a.
```

Therefore:

```text
f_2/f_1 = tau_1/tau_2,
f_3/f_1 = tau_1/tau_3.
```

# Computation

Execution I records:

```text
zeta_2/zeta_1 = 1
zeta_3/zeta_1 = 0.229 +/- 0.005
```

and identifies:

```text
tau_2/tau_1 = zeta_2/zeta_1
tau_3/tau_1 = zeta_3/zeta_1.
```

Because `f_a` is inverse in `tau_a`, the certified ratios are:

```text
f_2/f_1 = zeta_1/zeta_2 = 1
f_3/f_1 = zeta_1/zeta_3 = 1/0.229 = 4.366812227074236
```

Propagating the stated uncertainty:

```text
zeta_3/zeta_1 = 0.234 -> f_3/f_1 = 4.273504273504273
zeta_3/zeta_1 = 0.224 -> f_3/f_1 = 4.464285714285714
```

# What Is Certified

The ratio result is certified:

```text
selected zeta ratios
-> divisor-volume map
-> inverse axion normalization
-> axion decay-constant ratios.
```

No observed axion mass, coupling, or decay constant is used.

# What Is Not Certified

This certificate does not close absolute axion decay constants.  Absolute
`f_a` values still require the absolute-normalization gate described in the
dimensionful obstruction certificate.

This certificate also does not certify the source's large-volume EFT-control
sentence.  Execution I states that EFT control requires:

```text
t_a >> 1
```

but the executed numerical corner contains:

```text
t_1 = t_2 ~= 0.94.
```

So the ratio algebra is usable, while full large-volume control remains open.

# Correct Way Forward

To upgrade this sector, one must either:

```text
find a large-volume representative preserving the same ratios,
```

or:

```text
prove that corrections remain controlled in the t_1=t_2 ~= 0.94 corner.
```
