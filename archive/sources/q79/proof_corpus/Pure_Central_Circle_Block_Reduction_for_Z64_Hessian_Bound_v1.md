---
abstract: |
  We sharpen the remaining Hessian bound for the Z_64 projector.  The previous
  extraction wrote L_fl,MTT|H_64 = alpha L_tower + E with
  E=E_mix+E_Schur+E_cubic.  Reading the ProtoSpinor/worldsheet bridge and the
  MTT Foundation shows that, on the pure exact-order-64 central-circle tower
  sector, the circle block is quadratically matched exactly and mixed
  circle-lens/nil terms vanish at leading Hessian order, being absorbed into
  controlled higher-order remainder.  Since the Riesz projector uses the
  Hessian/second-variation operator, the cubic Taylor remainder is not part of
  the Hessian-level operator.  Thus the Hessian-level correction reduces to
  the Schur-Feshbach/noncoherent-mode term, plus any explicit warp or
  fixed-sector leakage correction.  Under exact base-only warping and fixed
  arithmetic sector, the pass condition becomes C_fl/lambda_Q < 9 alpha/2,
  where C_fl is the selected flavor coherent/noncoherent mixing product.
  This is a real tightening: the remaining proof no longer needs generic
  circle-lens/nil cross-block bounds, only the flavor-sector Schur constant,
  central-circle stiffness, and gap.
author:
- Peter Nero
date: May 2026
title: |
  Pure Central-Circle Block Reduction for the Z64 Hessian Bound
---

# Purpose

The previous Hessian extraction left the sufficient bound:

```text
||E_mix|| + C lambda_Q^{-1} + ||E_cubic|| < 9 alpha/2.
```

This paper asks whether all three correction terms really belong to the
Hessian-level Z_64 projector problem.

Answer:

```text
on the pure central-circle tower sector,
E_mix = 0 at leading Hessian order,
E_cubic = 0 for the Hessian operator itself.
```

So the Hessian-level condition reduces to:

```text
C lambda_Q^{-1} < 9 alpha/2
```

up to any explicit warp/noncommutation or arithmetic-sector leakage.

# Corpus Inputs

## ProtoSpinor/worldsheet block theorem

The ProtoSpinor/worldsheet bridge states that the local quadratic
admissibility burden decomposes schematically as:

```text
delta^2 J_ws = Q_C + Q_L + Q_N + Q_mix,
```

where `Q_mix` vanishes at the aligned normal form to leading order and is
absorbed into the controlled remainder.

It then states that in a circle-dominant perturbation:

```text
delta ell = 0,
delta n = 0,
```

the quadratic burden is governed by the circle block alone:

```text
delta^2 J_ws = Q_C + O(||delta Xi||^3),
Q_C = <delta c, H_C delta c> + O(||delta Xi||^3).
```

Finally, its combined local synthesis theorem says the carrier Hessian has
blockwise form:

```text
H_car ~ H_C op H_L op H_N
```

up to controlled cubic remainder.

## Foundation commutation and block structure

The MTT Foundation states that under base-only warping the vertical Laplacians
commute.  If fiber-dependent perturbations are present, the total projector
description persists with:

```text
O(epsilon_warp)
```

corrections.

The theta-closure paper also records a baseline metric ansatz that is
block-diagonal.

## Schur-Feshbach reduction

The theta-closure paper gives:

```text
L_eff = P_0 L P_0 - P_0 L Q (Q L Q)^(-1) Q L P_0,
```

and the bound:

```text
||P_0 L Q (Q L Q)^(-1) Q L P_0|| <= C lambda_Q^{-1}.
```

# Pure Central-Circle Tower Sector

The dyadic tower sector is:

```text
H_64 = span{|d> : d_i >= 2, product_i d_i = 32}.
```

It records only central-circle cover-degree refinements plus terminal
spinorial parity.

At the tangent/block level this means:

```text
delta ell = 0,
delta n = 0,
delta c != 0.
```

Therefore it is a pure circle-block sector in the sense of the
ProtoSpinor/worldsheet bridge.

# Lemma: Mixed Hessian Terms Vanish on H_64

Assume:

1.  the exact-order-64 dyadic CP sector is a fixed arithmetic central-circle
    sector;

2.  the local chart is alignment-controlled;

3.  the dyadic tower perturbations are pure central-circle perturbations:

    ```text
    delta ell = delta n = 0;
    ```

4.  mixed block couplings are treated as in the ProtoSpinor/worldsheet local
    bridge: absent at leading quadratic order or absorbed into controlled
    higher-order remainder.

Then the Hessian-level mixed correction vanishes on `H_64`:

```text
E_mix = 0.
```

## Proof

The mixed Hessian correction is the restriction of the circle-lens and
circle-nil blocks to the selected tangent sector:

```text
E_mix ~ H_cL + H_cN + adjoints.
```

But on the pure central-circle sector:

```text
delta ell = 0,
delta n = 0.
```

The ProtoSpinor/worldsheet bridge says that under this condition the
quadratic burden is governed by the circle block alone:

```text
delta^2 J = Q_C + O(||delta Xi||^3).
```

Thus no mixed quadratic term remains in the Hessian.  Any chart-coupling effect
is higher order and belongs to the nonlinear remainder, not to the Hessian
operator.  Hence:

```text
E_mix = 0
```

at Hessian level.

# Lemma: Cubic Remainder Is Not a Hessian Operator Term

The Riesz projector in the Z_64 proof is built from the second-variation
operator:

```text
L_fl,MTT = Hessian(J) restricted to H_64.
```

The cubic Taylor remainder:

```text
O(||delta Xi||^3)
```

does not contribute to the Hessian at the alignment reference.

Therefore, for the Hessian-level projector:

```text
E_cubic = 0.
```

If one later wants a full nonlinear finite-amplitude selection theorem, then
one must add a separate small-amplitude bound on the cubic remainder.  That is
not part of the Hessian-level Riesz projector.

# Theorem: Reduced Hessian Bound

Assume:

1.  the dyadic CP sector is the fixed exact-order-64 pure central-circle tower
    sector `H_64`;

2.  the aligned local bridge is blockwise in the ProtoSpinor/worldsheet sense;

3.  base-only warping gives exact commuting vertical Laplacians, or any warp
    leakage is tracked separately;

4.  the Schur-Feshbach remainder satisfies:

    ```text
    ||E_Schur|| <= C lambda_Q^{-1};
    ```

5.  the circle Hessian stiffness is:

    ```text
    alpha > 0.
    ```

Then the Hessian-level flavor operator has:

```text
L_fl,MTT | H_64 = alpha L_tower + E_Schur,
```

and the Z_64 projector is selected if:

```text
C lambda_Q^{-1} < 9 alpha/2.
```

If warp leakage is present with norm `epsilon_warp`, the sufficient condition is:

```text
C lambda_Q^{-1} + epsilon_warp < 9 alpha/2.
```

## Proof

The previous extraction theorem gave:

```text
L_fl,MTT | H_64 = alpha L_tower + E_mix + E_Schur + E_cubic.
```

By the pure-block lemma:

```text
E_mix = 0.
```

By the Hessian-level lemma:

```text
E_cubic = 0.
```

Thus:

```text
L_fl,MTT | H_64 = alpha L_tower + E_Schur.
```

The Schur-Feshbach bound gives:

```text
||E_Schur|| <= C lambda_Q^{-1}.
```

The operator-identification criterion requires:

```text
||E_Schur|| < 9 alpha/2.
```

Therefore it is enough that:

```text
C lambda_Q^{-1} < 9 alpha/2.
```

The optional warp term is additive by the triangle inequality.  This proves
the theorem.

# Consequence

The remaining Z_64 Hessian gate is now:

```text
lambda_Q > 2C/(9 alpha)
```

or, with warp leakage:

```text
C lambda_Q^{-1} + epsilon_warp < 9 alpha/2.
```

In normalized tower units `alpha=1` and exact commuting/block conditions:

```text
C_fl/lambda_Q < 4.5.
```

# What Remains Open

The corpus does not yet give:

```text
C_fl = ||P_fl L Q|| ||Q L P_fl|| for the flavor Schur-Feshbach block,
lambda_Q for the selected flavor slab,
alpha for the central-circle closure stiffness,
epsilon_warp if the exact base-only/block-diagonal ansatz is relaxed.
```

But it no longer needs a generic bound on circle-lens/nil cross terms for the
pure dyadic tower sector.

# Gate Status

```text
pure circle block theorem found                         CORPUS-SUPPORTED
mixed terms vanish at leading Hessian order             PROVED
cubic remainder excluded from Hessian operator          PROVED
reduced Hessian operator alpha L_tower + E_Schur        PROVED
reduced pass condition C_fl/lambda_Q < 9 alpha/2        PROVED
compute alpha                                           OPEN
compute flavor mixing product C_fl                      OPEN
compute selected lambda_Q                               OPEN
bound warp leakage if base-only warping is relaxed      OPEN IF NEEDED
```

# Bottom Line

The correction inequality has tightened from:

```text
||E_mix|| + C lambda_Q^{-1} + ||E_cubic|| < 9 alpha/2
```

to the Hessian-level condition:

```text
C lambda_Q^{-1} < 9 alpha/2
```

under the pure central-circle, blockwise aligned, fixed-sector assumptions.

This is the next real narrowing of the proof.

The following Schur-gap reduction rewrites the live target as:

```text
C_fl / (alpha lambda_Q) < 9/2.
```
