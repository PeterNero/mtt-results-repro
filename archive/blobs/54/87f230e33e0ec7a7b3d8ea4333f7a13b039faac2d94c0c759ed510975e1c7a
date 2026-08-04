---
title: Non-SM Constants No-Knob Ledger
author:
- Peter Nero
date: May 2026
abstract: |
  This ledger starts a clean non-SM constants program.  Its purpose is not to
  claim that MTT already predicts every physical constant, but to classify which
  constants are unit conventions, which are structurally constrained, which are
  conditional predictions, and which remain open.  The strongest current
  non-SM result is the Theta IV tensor-ratio bound.  The strongest current
  obstruction is the absolute normalization needed for Newton's constant and
  other dimensionful constants.
---

# Rule

The allowed workflow is:

```text
selected MTT/MMT data
-> encoding dictionary
-> target observable.
```

The forbidden workflow is:

```text
target observed value
-> hidden normalization or benchmark fit
-> claimed prediction.
```

# Status Classes

```text
CLOSED
CONDITIONAL
STRUCTURAL
OPEN
FORBIDDEN_AS_UNIT_CONVENTION
```

# Initial Ledger

## Unit Conventions

The constants:

```text
c, hbar, k_B
```

are not prediction targets.  They define unit conversions.  A future paper may
explain why relativistic, quantum, or thermal descriptions use them, but that is
not the same as numerically predicting them.

Status:

```text
FORBIDDEN_AS_UNIT_CONVENTION
```

## Primordial Tensor Ratio

Theta IV gives the cleanest current non-SM candidate:

```text
Lambda_Theta ~ mu_Theta = 5 TeV
```

with admissibility:

```text
H < Lambda_Theta
```

and standard tensor scaling:

```text
r ~ H^2 / M_Pl^2.
```

This yields:

```text
r <= 10^-30 to 10^-29
```

for:

```text
Lambda_Theta in [3,10] TeV.
```

Status:

```text
CONDITIONAL
```

This is no-knob once the coherence-scale identification is accepted, but the
identification itself must remain visible.

## Newton Constant

Theta IV derives:

```text
Vol(X_int) ~= 31.8 R1^3
```

and:

```text
1/G_N ~= 31.8 R1^3 / G_10.
```

This is strong structure, but not an absolute prediction of `G_N` until MTT
selects:

```text
G_10 / R1^3
```

without using the observed Newton constant as the backsolve.

Status:

```text
STRUCTURAL
```

## Closure Scale

The current repo uses:

```text
mu_Theta = 5 TeV
```

as a conservative matching scale, with:

```text
I2/I1 = 0.560,
I3/I1 = 0.229,
lambda_* = 0.25.
```

This is currently a scaffold/matching datum, not yet a standalone prediction of
an observed non-SM constant.

Status:

```text
STRUCTURAL
```

## Axion Decay Constants

Execution I contains the next promising non-SM sector: axion normalization and
decay-constant ratios from Kahler geometry.

The first audit should separate:

```text
ratio claims,
absolute f_a claims,
threshold-profile realization,
volume/string-normalization assumptions.
```

Status:

```text
STRUCTURAL
```

until executable ratio audits are added.

## Late-Time Dark Energy and Hubble Constant

The current q79 proof repo does not yet contain a closed selected source for:

```text
Lambda_cosm,
rho_DE,
H0.
```

These require:

```text
selected vacuum-energy functional,
late-time cosmological solution,
renormalization prescription,
initial-condition or attractor theorem.
```

Status:

```text
OPEN
```

# First Program

1. Audit the Theta IV tensor bound.
2. Audit the Theta IV Newton-constant structure.
3. Audit Execution I axion ratios and threshold claims.
4. Create templates for the missing absolute-normalization and cosmology data.
5. Only then attempt numerical non-SM predictions.

