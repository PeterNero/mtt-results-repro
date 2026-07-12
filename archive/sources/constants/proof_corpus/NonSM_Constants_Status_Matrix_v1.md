---
title: Non-SM Constants Status Matrix
author:
- Peter Nero
date: May 2026
---

# Purpose

This matrix summarizes the current state of the no-knob non-SM constants
program after the tensor, axion, threshold, EFT-control, and large-volume repair
audits.

# Status Matrix

| Sector | Status | Current Result | Next Gate |
|---|---|---|---|
| Tensor ratio `r` | `CONDITIONAL_NO_KNOB` | `r <= 1.56e-30` to `1.74e-29` for `Lambda_Theta in [3,10] TeV` | Derive `Lambda_Theta` rather than identify it with the conservative matching scale |
| Axion decay-constant ratios | `RATIO_NO_KNOB` | `f2/f1=1`, `f3/f1=4.366812227074235` | Derive absolute `f_a` normalization without target-value backsolve |
| Threshold profile | `STRUCTURAL_CONSISTENCY` | Exceptional vector is about `2.34%` of the reported bulk vector | Derive `c_I` from selected topology, flux, or curvature data |
| EFT status | `OPEN_NORMALIZATION` | Ratio geometry works, but `min(t)=0.94` and `min(tau)=0.8836` block full large-volume control | Use repair or finite-volume correction bounds |
| Large-volume repair | `REPAIR_CERTIFIED` | `t_a -> s t_a` preserves ratios and bulk threshold direction; `s=5` gives `min(t)=4.7`, `min(tau)=22.09` | Select `s` or `g10` from independent MTT data |
| Newton/Planck normalization | `OPEN_NORMALIZATION` | `1/G_N ~= 31.8 R1^3/G10` is structure, not an absolute value | Supply selected `G10/R1^3` or equivalent anchor |
| Unit conventions | `FORBIDDEN_UNIT_CONVENTION` | `c`, `hbar`, and `k_B` are not prediction targets | None |

# What We Have

The strongest current non-SM outputs are:

```text
conditional tensor bound,
axion decay-constant ratios,
large-volume repair preserving ratio/threshold structure.
```

These are meaningful because each comes with an executable audit and a clear
boundary against hidden fitting.

# Main Blocker

The main blocker is now sharply isolated:

```text
selected absolute normalization.
```

This includes:

```text
g10,
absolute volume,
R1,
absolute f_a,
G_N / M_Pl,
H0,
rho_DE.
```

None of these may be selected from the observed target value.

# Correct Next Step

The next proof object should be an absolute-normalization candidate gate:

```text
selected MTT data
-> selected normalization anchor
-> encoding dictionary
-> target dimensionful observable.
```

The gate must reject:

```text
observed target constant
-> selected normalization
-> claimed prediction.
```
