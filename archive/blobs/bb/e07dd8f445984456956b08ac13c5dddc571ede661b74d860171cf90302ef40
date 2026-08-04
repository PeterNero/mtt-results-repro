---
abstract: |
  We derive the nil-survivor execution principle used in the selected-kernel
  proof as a precise theorem schema.  If the coherent MTT sector contains a
  nilpotent execution operator N, a positive closure-strain functional whose
  zero set is the terminal nil survivor set, and a finite character quotient
  Gamma through which recordable CP labels factor, then the sharp execution
  kernel is the fiberwise minimum of the raw retarded overlap plus closure
  cost.  Equivalently, raw continuous pre-survivor data are reduced to
  discrete survivor labels by a zero-temperature/zero-width admissibility
  filter.  Applied to the CKM dyadic branch after the Z_64 quotient is
  supplied, primitive order-64 admissibility and retarded predecessor
  orientation force the unique survivor q_64=15.  This proves the projection
  mechanism needed by the selected-kernel theorem.  It does not by itself
  derive the Z_64 carry rows, the Mukai Z_7 block, or the exact MTT nil
  operator; those remain separate construction gates.
author:
- Peter Nero
date: May 2026
title: |
  Nil-Survivor Execution Theorem for the Selected CKM CP Branch
---

# Purpose

The selected-kernel paper reduced the remaining interpretive gap to:

```text
derive nil-survivor execution dynamically.
```

This paper proves the mathematical execution principle in the form needed for
the CKM CP branch.

The result is deliberately scoped:

```text
nilpotent coherent execution + finite CP quotient
=> survivor projection by sharp admissibility filtering.
```

It does not claim that nil alone derives:

```text
Z_64,
Z_7,
or the full order-448 quotient.
```

Those finite rows must still come from shared-circle carry and Mukai/Fu-Yau
selection.  Nil supplies the execution mechanism that turns upstream
continuous data into discrete recordable survivors.

# Definitions

## Nil execution operator

Let `H_coh` be the coherent sector after the MTT projection.  A nil execution
operator is an endomorphism:

```text
N: H_coh -> H_coh
```

such that:

```text
N^d = 0
```

for some finite depth `d`, while usually:

```text
N^(d-1) != 0.
```

The descending filtration is:

```text
H_coh = F^0 superset F^1 superset ... superset F^d = 0,
F^k = im N^k.
```

Terminal survivor states lie in the nil-stable sector:

```text
S_nil = ker N / null directions identified by coherent gauge redundancy.
```

## Closure-strain Lyapunov functional

A nil execution functional is a nonnegative closure cost:

```text
C_nil: H_coh -> R_{\ge 0}
```

with:

```text
C_nil(x)=0 exactly on terminal survivor representatives,
C_nil(x)>0 away from survivor basins.
```

Locally, near a survivor basin, it has positive quadratic normal form:

```text
C_nil(y,z)
= C_surv(y) + 1/2 z^T H_N z + O(||z||^3),
H_N > 0,
```

where `y` is a survivor coordinate and `z` is transverse nil-decaying data.

## Finite CP label map

Let:

```text
Gamma_CP
```

be the selected finite CP quotient.  The CP label map is:

```text
ell: S_nil -> Gamma_CP.
```

Recordable CP observables are functions of `ell`.

# Execution Kernel

Let:

```text
J_raw^ret(x)
```

be the raw retarded overlap/admissibility cost on the coherent pre-survivor
space.  The finite-width execution kernel is:

```text
K_epsilon(x)
= exp(-(J_raw^ret(x)+C_nil(x))/epsilon^2).
```

For a selected label `g in Gamma_CP`, define the label fiber:

```text
F_g = {x in H_coh : ell(pi_nil(x)) = g}.
```

The selected cost at finite width is the fiber reduction:

```text
J_epsilon(g)
= -epsilon^2 log integral_{F_g} K_epsilon(x) dmu_g(x).
```

In the sharp survivor limit:

```text
epsilon -> 0,
```

Laplace's principle gives:

```text
J_sel(g)
= min_{x in F_g} [J_raw^ret(x)+C_nil(x)].
```

# Theorem: Nil-Survivor Execution

Assume:

1.  `N` is nilpotent on the coherent sector;

2.  `C_nil` is nonnegative and has positive quadratic transverse Hessian near
    each survivor basin;

3.  the selected CP label map `ell` has finite image `Gamma_CP`;

4.  the raw retarded overlap cost is continuous on each relevant label fiber;

5.  each label fiber has at least one closure-admissible survivor
    representative or is excluded from the admissible label set.

Then the sharp execution kernel selects exactly the label or labels minimizing:

```text
J_sel(g)
= min_{x in F_g} [J_raw^ret(x)+C_nil(x)].
```

If the minimum is unique, the survivor label is unique.

## Proof

Nilpotence gives a finite termination filtration:

```text
H_coh -> im N -> ... -> im N^(d-1) -> 0.
```

The positive transverse Hessian of `C_nil` makes non-survivor directions
strictly costly near the terminal sector.  Thus as `epsilon -> 0`, the weight:

```text
exp(-(J_raw^ret+C_nil)/epsilon^2)
```

concentrates on the lowest-cost survivor representatives in each finite label
fiber.  Laplace's principle yields:

```text
-epsilon^2 log integral_{F_g}
exp(-(J_raw^ret+C_nil)/epsilon^2)
-> min_{x in F_g} [J_raw^ret(x)+C_nil(x)].
```

Since `Gamma_CP` is finite, minimizing over labels is an ordinary finite
minimum.  A strict minimum gives a unique survivor label.

This proves the theorem.

# Corollary: Selected Kernel

Under the theorem assumptions, the physical CP kernel is:

```text
K_sel(g)
= fiber reduction of K_raw^ret over F_g.
```

It is not the raw pre-survivor kernel unless the raw kernel is already constant
on every execution fiber.

Therefore the selected-kernel principle follows from nil-survivor execution.

# Application to CKM Dyadic CP

Now assume the dyadic finite quotient has already been derived:

```text
Gamma_64 = Z_64.
```

The lepton/lens branch is the quarter-turn:

```text
l_64=16.
```

Primitive quark CP admissibility requires:

```text
q_64 in Z_64^* = {1,3,5,...,63}.
```

Retarded shared-circle orientation restricts the quark branch to the
pre-quarter side:

```text
q_64 < 16
```

on the selected local lift.  Thus the admissible retarded primitive set is:

```text
P_- = {1,3,5,7,9,11,13,15}.
```

In the sharp nil-survivor limit, with positive Schur-reduced closure cost:

```text
J_sel(p)
= 1/2 kappa_q (p-16)^2,
kappa_q>0.
```

The unique minimizer is:

```text
p=15.
```

Hence:

```text
q_64=15.
```

# CKM q=79 Consequence

The odd Mukai component supplies:

```text
q_7=2.
```

Then CRT gives:

```text
q=15 mod 64,
q=2  mod 7,
q=79 mod 448.
```

Thus:

```text
nil-survivor execution + Z_64 + Z_7 + retarded orientation
=> q=79.
```

# What Nil Does and Does Not Derive

Nil execution derives the projection mechanism:

```text
continuous pre-survivor data -> discrete survivor labels.
```

It does not by itself derive the label group:

```text
Z_64 x Z_7.
```

For this reason, the correct division of labor is:

```text
shared-circle recursion -> Z_64,
Mukai/Fu-Yau discriminant -> Z_7,
nil execution -> survivor projection on the selected quotient,
retarded orientation -> predecessor side,
positive closure cost -> nearest primitive survivor.
```

This prevents an overclaim: the known nil evidence strongly supports three
family basins, but it does not automatically generate the sevenfold odd CP
factor or the dyadic order-64 carry.

# Remaining Dynamic MTT Gate

To make this fully dynamic rather than theorem-schematic, MTT must supply the
actual nil execution data:

```text
N_MTT,
H_coh,
C_nil,
ell: S_nil -> Gamma_CP,
```

and prove:

```text
N_MTT^d=0,
C_nil has positive transverse Hessian,
ell has finite selected image,
the CKM branch admissible set is primitive order-64,
the central-circle orientation is retarded.
```

The present theorem proves that these data are sufficient.

# Gate Status

```text
nilpotent termination implies finite-depth execution filtration       PROVED
positive transverse closure cost gives survivor concentration         PROVED
finite CP label map gives discrete recordable labels                  PROVED
sharp filter reduces raw kernel to selected survivor cost             PROVED
dyadic primitive retarded survivor is q_64=15                         PROVED
CRT with q_7=2 gives q=79                                             PROVED
actual MTT nil operator N_MTT supplied                                OPEN
Z_64 carry rows derived from shared-circle recursion                  OPEN
Mukai Z_7 promoted to selected geometry                               OPEN
```

# Bottom Line

The nil-survivor step is now mathematically controlled:

```text
nilpotence + positive closure cost + finite CP quotient
=> sharp survivor projection.
```

This upgrades the selected-kernel proof.  The remaining foundational task is
not to justify survivor projection abstractly; it is to identify the concrete
MTT nil operator and the finite quotient rows that feed it.
