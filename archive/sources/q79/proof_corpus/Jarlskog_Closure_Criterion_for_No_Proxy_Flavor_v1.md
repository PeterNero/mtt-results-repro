---
abstract: |
  We close the basis-invariant CP test that the eventual no-proxy Yukawa
  matrices must pass.  Once selected canonical matrices Y_u and Y_d have been
  computed, define H_u=Y_uY_u^\dagger and H_d=Y_dY_d^\dagger.  For three
  generations with nondegenerate up and down spectra, CKM CP violation is
  equivalent to Im det([H_u,H_d]) being nonzero.  This criterion uses no
  observed masses or CKM angles to choose the matrices; it only specifies the
  invariant to evaluate after the selected overlap calculation is done.
author:
- Peter Nero
date: May 2026
title: |
  Jarlskog Closure Criterion for No-Proxy Flavor
---

# Purpose

The current proof chain has separated:

```text
rank:        C33(M_s) != 0,
orientation: Delta_v != (0,0),
phase source: q = 79 mod 448.
```

The next CP question is sharper:

```text
given selected canonical Y_u and Y_d, is CKM CP violation actually nonzero?
```

This note closes the invariant criterion for that question.  It does not
compute the matrices.

# Setup

Let the selected no-proxy calculation eventually produce canonical quark
Yukawa matrices:

```text
Y_u,
Y_d.
```

Define:

```text
H_u = Y_u Y_u^dagger,
H_d = Y_d Y_d^dagger,
C = [H_u,H_d].
```

The matrices `H_u` and `H_d` are Hermitian, so `C` is anti-Hermitian and
traceless.

# Criterion

For three generations with nondegenerate up-sector and down-sector spectra,
the CKM CP-violation gate is:

```text
Delta_CP := Im det([H_u,H_d]) != 0.
```

Equivalently, since `C` is traceless:

```text
det(C) = Tr(C^3)/3.
```

The standard Jarlskog factorization says that `Delta_CP` is proportional to:

```text
J_CKM
* product_{i<j}(m^2_{u,i}-m^2_{u,j})
* product_{i<j}(m^2_{d,i}-m^2_{d,j}).
```

Thus, after nondegenerate spectra are established, nonzero `Delta_CP` is the
basis-invariant CP test.

# Theorem

#### No-Proxy Jarlskog Closure Criterion

Assume the selected no-proxy construction has produced canonical `Y_u,Y_d`.
If the spectra of `H_u=Y_uY_u^dagger` and `H_d=Y_dY_d^dagger` are
nondegenerate, then quark-sector CKM CP violation is nonzero if and only if:

```text
Im det([H_u,H_d]) != 0.
```

This is the final matrix-level CP gate.  The q79 phase supplies the selected
finite CP character, but the selected Yukawa matrices still must make this
invariant nonzero.

#### Proof

The Jarlskog determinant identity for three generations gives:

```text
det([H_u,H_d])
  = const * i * J_CKM
    * product_{i<j}(m^2_{u,i}-m^2_{u,j})
    * product_{i<j}(m^2_{d,i}-m^2_{d,j}),
```

with convention-dependent sign in the constant.  Under nondegenerate spectra,
the mass-difference products are nonzero.  Therefore the determinant is
nonzero exactly when the Jarlskog invariant is nonzero.  Since `[H_u,H_d]` is
anti-Hermitian, its determinant is purely imaginary in the three-dimensional
case, so the imaginary part supplies the real CP-odd scalar test.

# No-Proxy Rule

This criterion must be applied only after `Y_u` and `Y_d` are obtained from:

```text
selected overlap entries,
selected channel actions,
selected q79 characters,
selected kinetic metrics,
selected RG/threshold matching.
```

It cannot be used backwards to choose matrix entries from observed masses,
observed CKM angles, or benchmark matrices.

# What This Closes

```text
basis-invariant CKM CP success test,
nondegenerate-spectrum requirement,
separation of q79 phase source from full matrix CP violation,
guardrail against fitting Jarlskog data into the matrices.
```

# What Remains Open

```text
selected Y_u,
selected Y_d,
canonical kinetic metrics,
singular values and nondegeneracy,
Delta_CP value,
CKM angle magnitudes,
RG and threshold matching.
```

# Next Calculation

The first quark-sector computation now has three nested targets:

```text
1. C33_u and C33_d for full rank,
2. Delta_v for leading up/down noncommutation,
3. Im det([H_u,H_d]) for selected CP violation.
```

The first two can be checked on the leading response matrices.  The third
requires the canonical selected matrices.
