---
abstract: |
  We test several source theories for the missing weighted right-eigenchannel
  mass actions.  The test is deliberately conservative: numerical proximity is
  not counted as proof unless the theory uses only selected MTT data and fixes
  its eigenchannel labels before comparing with quark masses.  The battery
  shows that a Gaussian zero-mode base q_x^2 log(pi) is the best simple
  primitive, that benchmark flavor corrections are proxy data and therefore
  inadmissible as proof sources, and that the most promising non-proxy route is
  a finite right-channel operator whose eigenvalues add small width/instanton/
  nil corrections to the q_x^2 log(pi) base.
author:
- Peter Nero
date: June 2026
title: |
  Mass-Action Source Theory Battery for Weighted Right-Eigenchannel Closure
---

# Purpose

The selected finite B_q branch plus the weighted right-eigenchannel theorem
reduces the mass problem to four light-mode actions:

```text
A_u = (4.480058, 4.615899),
A_d = (1.158678, 1.526516).
```

This note tests candidate source theories for those numbers.

# Discipline

A source theory is proof-admissible only if:

```text
1. it uses selected MTT constants or operators;
2. it acts in the weighted right singular eigenchannels;
3. it fixes all channel labels before looking at quark masses;
4. it uses no observed masses, CKM entries, or printed benchmark Yukawa
   corrections as inputs.
```

Numerical closeness alone is not enough.

# Candidate Theories Tested

## Theory A: pure Gaussian zero-mode measure

Use:

```text
A_{x,a} = q_x^2 log(pi),
q_u=2,
q_d=1.
```

This gives:

```text
A_u = (4.578920, 4.578920),
A_d = (1.144730, 1.144730).
```

It is the strongest simple primitive, but it leaves family/eigenchannel
splitting unexplained.

## Theory B: Z3 family Laplacian splitting

Use the retained family carrier with a Z3 Laplacian correction:

```text
lambda_Z3 = (0,3,3).
```

This cannot split the two non-terminal light channels by itself because the
two nontrivial Z3 Laplacian eigenvalues are degenerate.  It can contribute a
common light-mode lift, but not the observed two-light-mode split.

## Theory C: nil finite-width correction

Use the same nil-survivor logic that produced the selected CP unit-lag branch,
but now as a finite-width correction after right-channel projection.

This is structurally admissible, but the concrete finite-width operator is not
yet supplied.  The battery therefore tests fixed primitive scales such as:

```text
lambda_nil,
lambda_nil/2,
lambda_nil/lambda_lens,
1/64,
1/7.
```

The result is diagnostic only: these scales can approximate the residuals, but
the eigenvalue labels still need to come from an actual selected operator.

## Theory D: old Execution II local corrections

The old benchmark used:

```text
F_22=1.18,
eta_d1=0.09,
eta_d2=0.07.
```

These are useful historical clues, but they are not proof-admissible here
because they were local benchmark inputs.  They may inspire the form of a
future source operator, but cannot be used as selected MTT derivations.

## Theory E: finite right-channel source operator

The most plausible route is:

```text
A_{x,a} = q_x^2 log(pi) + eig_a(R_x),
```

where `R_x` is a finite self-adjoint right-channel operator built from:

```text
width/flux data W,
allowed instanton or exceptional classes I,
nil-survivor finite-width corrections,
Higgs overlap normalization,
right-singlet line-bundle costs.
```

This is the correct shape because it can produce channel splitting while
preserving CKM, provided `R_x` is diagonal in the weighted right singular basis.

# Battery Result

The numerical ranking is:

```text
best simple structural primitive: q_x^2 log(pi);
best proof shape: q_x^2 log(pi) plus selected finite right-channel operator;
benchmark correction theory: rejected as proof source;
free per-channel integer search: diagnostic only, not a theorem.
```

# What This Closes

```text
several mass-action source theories tested       CHECKED
pure Gaussian base identified as best primitive  DIAGNOSTIC
Z3 Laplacian alone rejected for splitting        NO-GO
benchmark correction reuse rejected as proof     NO-PROXY
finite right-channel operator route selected     TARGET
```

# Remaining Proof Obligation

The next missing object is:

```text
R_x = selected finite right-channel source operator
```

with:

```text
eig_light(R_u) ~= (-0.098862, +0.036979),
eig_light(R_d) ~= (+0.013949, +0.381786),
```

relative to the `q_x^2 log(pi)` base.

That operator must be derived from the same selected MTT source map
`Sigma_MTT`, not reverse-engineered from the four mass actions.

# Bottom Line

The search did not close full SM masses, but it sharpened the next constructive
target.  The likely correct theory is not a new CKM mechanism and not a
family-basis prefactor.  It is a finite right-channel action operator:

```text
SelectedMassActionSource:
  Gaussian zero-mode base q_x^2 log(pi)
  + selected finite width/instanton/nil/Higgs right-channel operator.
```

