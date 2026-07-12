---
title: Absolute Normalization Candidate Gate
author:
- Peter Nero
date: May 2026
---

# Purpose

This gate explores ways to select an absolute normalization without knobs.

The target is not to pick a number yet.  The target is to classify which routes
could honestly select one, and which routes are only calibrations, ratios,
bounds, or forbidden backsolves.

# Gate Rules

Allowed:

```text
selected MTT data,
topology,
flux integers,
action normalizations,
derived coherence/damping scale.
```

Forbidden:

```text
observed G_N,
observed M_Pl,
observed H0,
observed rho_DE,
observed absolute f_a,
the same target value being claimed as predicted.
```

# Candidate Routes

## A. Gauge Common Scale K

The corpus uses:

```text
K = alpha_r^{-1}/zeta_r,
Vol/g10^2 = K/(4pi).
```

This is useful, but it fixes only a combination.  It does not select `Vol` and
`g10` separately.

Status:

```text
CALIBRATES_COMBINATION_NOT_ABSOLUTE_NORMALIZATION
```

## B. Newton Backsolve

The roadmap says one can use:

```text
Vol G10^{-1} = G_N^{-1}.
```

This is fine for phenomenological calibration.  It is forbidden as a proof of
`G_N` or `M_Pl`, because it uses the target value.

Status:

```text
FORBIDDEN_FOR_PREDICTING_GN_OR_PLANCK_SCALE
```

## C. Theta Coherence Scale

A promising route is:

```text
finite projection / damping-selected coherence dynamics
-> Lambda_Theta
-> absolute scale.
```

This could become a true no-knob anchor if `Lambda_Theta` is derived rather
than identified with the conservative matching scale.

Status:

```text
PROMISING_OPEN_ROUTE
```

## D. Flux/Bianchi Alpha-Prime Route

The heterotic flux corpus contains equations of the form:

```text
dH = alpha'/4 (Tr R_+^2 - Tr F^2),
```

and examples where flux equations fix loci such as:

```text
r_3,
R_1/R.
```

This is highly relevant, but it does not yet select an absolute physical scale
unless `alpha'` or the string length is independently selected.

Status:

```text
PROMISING_BUT_REQUIRES_ALPHA_PRIME_OR_STRING_SCALE_ANCHOR
```

## E. Topological Flux Integer Minimization

This is the best structural route:

```text
selected flux/topology sector
-> scale-dependent MTT admissibility functional
-> unique positive minimizer
-> absolute normalization.
```

It would be no-knob if the functional and integer data are selected before any
target constant is evaluated.

Status:

```text
BEST_STRUCTURAL_RESEARCH_ROUTE
```

## F. Central-Circle Spectral Gap

The Theta corpus gives constraints like:

```text
lambda ~ 1/R1^2,
R1 <= 2.
```

This gives bounds, not a unique absolute value.  It becomes useful if combined
with another independent equation or minimization condition.

Status:

```text
BOUNDS_NOT_ABSOLUTE_SELECTION
```

## G. PQ/Axion Prior

A PQ-like axion prior could add a closure relation for:

```text
Vol,
g10,
G10.
```

But it is not no-knob unless the prior scale is itself selected, not taken from
an observed axion window.

Status:

```text
CONDITIONAL_PHENOMENOLOGICAL_PRIOR_NOT_NO_KNOB_YET
```

# Recommended Path

The right next path is:

```text
E + D + F
```

meaning:

```text
topological/flux integer minimization
+ heterotic Bianchi alpha-prime structure
+ central-circle spectral bounds.
```

This should be built as a new executable object:

```text
Selected_Normalization_Minimization_Functional_v1.
```

It must prove:

```text
selected inputs,
no target constants,
scale-dependent functional,
unique minimizer or finite candidate set,
normalization output.
```
