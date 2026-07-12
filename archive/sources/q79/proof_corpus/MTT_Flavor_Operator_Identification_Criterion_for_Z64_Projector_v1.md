---
abstract: |
  We turn the last Z_64 projector gap into a precise operator-identification
  theorem.  The MTT corpus already supplies a shared central circle, Fourier
  circle spectrum, bounded Riesz coherent projectors, and the need for fixed
  arithmetic sectors.  On the exact-order-64 central-circle tower sector, the
  spectral tower operator has a simple lowest eigenvalue at cost 15 and the
  next admissible tower begins at cost 24, giving gap 9.  Therefore any actual
  MTT flavor closure-strain operator of the form alpha L_tower + E, with
  alpha>0 and ||E|| < 9 alpha / 2, has the same selected Riesz projector label:
  the five-step D_2 tower with terminal spinorial parity.  This proves the
  analytic stability and identification criterion.  It does not yet provide
  the concrete MTT Hessian block or the correction bound; those are now the
  exact remaining physical computation.
author:
- Peter Nero
date: May 2026
title: |
  MTT Flavor Operator Identification Criterion for the Z64 Projector
---

# Purpose

The previous spectral projector paper constructed:

```text
P_fl = (1/2pi i) integral_gamma (z-L_tower)^(-1) dz
```

and proved that `L_tower` selects:

```text
(D_2,D_2,D_2,D_2,D_2) + terminal spinorial parity.
```

The remaining question was:

```text
why is L_tower the actual MTT flavor closure operator?
```

This paper proves the exact criterion needed for that identification.  It
separates:

```text
mathematical stability of the projector: proved here,
concrete extraction of the MTT Hessian block: still open.
```

# Corpus Inputs

The relevant MTT inputs are already present in the corpus:

1.  the internal bundles contain one shared central circle:

    ```text
    B_n|_y ~= S^1_cen x Sigma_n;
    ```

2.  the central circle has Fourier characters:

    ```text
    chi_n(z)=z^n;
    ```

3.  the circle Laplacian gives:

    ```text
    -Delta_c chi_n = (n^2/R_c^2) chi_n;
    ```

4.  coherent projectors are Riesz projectors under bounded geometry and a
    spectral gap;

5.  arithmetic flavor claims must be made inside a fixed integral sector before
    extending scalars to `R` or `C`.

The last point is essential.  A real Riesz projector may move vectors inside a
finite-dimensional real space, but it cannot be allowed to change the discrete
cover-degree sector unless an admissibility boundary is crossed.

# Exact-Order-64 Tower Sector

Let:

```text
A_64 = {d=(d_0,...,d_{m-1}) : d_i >= 2 and product_i d_i = 32}.
```

Terminal spinorial parity contributes the final factor `2`, so each
`d in A_64` gives exact dyadic order:

```text
2 product_i d_i = 64.
```

Let:

```text
H_64 = direct sum_{d in A_64} C |d>.
```

The tower operator is:

```text
L_tower |d> = C(d) |d>,
C(d) = sum_i (d_i^2 - 1).
```

The spectral projector paper proved:

```text
d_* = (2,2,2,2,2),
C(d_*) = 15,
C(d) >= 24 for every d != d_*.
```

Thus:

```text
Delta_tower = 24 - 15 = 9.
```

# Actual MTT Operator Normal Form

The required identification is not literal equality in the full Hilbert space.
It is equality on the fixed exact-order-64 central-circle tower sector up to
controlled corrections:

```text
L_fl,MTT | H_64 = alpha L_tower + E,
alpha > 0.
```

Here:

- `alpha` is the central-circle closure-strain stiffness scale;
- `E` contains Schur-reduced lens/nil mixing, metric renormalization,
  overlap-kernel curvature, and other higher-order corrections that remain
  after restricting to the exact-order-64 central-circle tower sector.

In normalized tower units one sets `alpha=1`.  In physical units the stability
threshold scales with `alpha`.

# Theorem: Perturbative Identification of the Z64 Projector

Assume:

1.  the exact-order-64 central-circle tower sector `H_64` is a fixed arithmetic
    coherent sector;

2.  the actual MTT flavor closure-strain operator restricted to this sector has
    the form:

    ```text
    L_fl,MTT | H_64 = alpha L_tower + E,
    alpha > 0;
    ```

3.  the correction is self-adjoint and bounded by:

    ```text
    ||E|| < 9 alpha / 2;
    ```

4.  the coherent flavor projector is the Riesz projector around the lowest
    closure-strain eigenvalue in this sector.

Then the actual MTT coherent flavor projector selects the same discrete tower
label as `L_tower`:

```text
(2,2,2,2,2),
```

and therefore:

```text
R = D_2^*,
five dyadic refinement steps,
terminal spinorial parity at the sixth record,
Gamma_2 ~= Z_64.
```

## Proof

For the unperturbed operator `alpha L_tower`, the selected eigenvalue is:

```text
lambda_* = 15 alpha.
```

Every other exact-order-64 tower has eigenvalue at least:

```text
lambda_next = 24 alpha.
```

So the unperturbed gap is:

```text
Delta = lambda_next - lambda_* = 9 alpha.
```

Let:

```text
r = ||E||.
```

By the standard finite-dimensional spectral perturbation bound, the selected
eigenvalue of `alpha L_tower + E` lies inside:

```text
[15 alpha - r, 15 alpha + r],
```

while every competitor eigenvalue lies outside the lower bound:

```text
[24 alpha - r, infinity).
```

These intervals are disjoint exactly when:

```text
15 alpha + r < 24 alpha - r,
```

equivalently:

```text
r < 9 alpha / 2.
```

Under this condition the lowest eigenvalue remains isolated.  Therefore the
Riesz projector around it is well-defined and has the same rank as the
unperturbed projector.

Now vary continuously:

```text
L(t) = alpha L_tower + tE, 0 <= t <= 1.
```

The same gap estimate holds for all `t`, so the Riesz projector cannot cross
or exchange with a competitor tower.  Since the arithmetic sector is fixed, the
discrete tower label cannot jump under this continuous perturbation.  Hence
the selected label remains:

```text
(2,2,2,2,2).
```

Each selected step is the pullback of the degree-two circle cover:

```text
D_2^* chi_n = chi_{2n}.
```

Thus the cumulative carry rows are:

```text
x_{i+1}=2x_i, i=0,...,4.
```

Terminal spinorial parity gives:

```text
2x_5=0.
```

Therefore:

```text
coker A_64 ~= Z_64.
```

This proves the theorem.

# What This Proves

This closes the analytic part of the operator-identification problem:

```text
if L_fl,MTT = alpha L_tower + E with ||E|| < 9 alpha/2,
then the actual MTT Riesz projector selects the Z_64 dyadic tower.
```

In normalized units:

```text
alpha = 1,
||E|| < 4.5.
```

# Updated Extraction Status

The follow-up extraction attempt found the correct MTT normal form:

```text
L_fl,MTT | H_64 = alpha L_tower + E,
E = E_mix + E_Schur + E_cubic,
||E_Schur|| <= C lambda_Q^{-1}.
```

The subsequent pure central-circle block reduction sharpens this on the fixed
exact-order-64 tower sector:

```text
E_mix = 0,
E_cubic = 0,
L_fl,MTT | H_64 = alpha L_tower + E_Schur.
```

So the remaining missing data are narrower.  One must compute or derive:

1.  the exact-order-64 central-circle arithmetic sector `H_64`;

2.  the central-circle Hessian stiffness `alpha`;

3.  the flavor-sector mixing product `C_fl` and selected noncoherent gap
    `lambda_Q`;

4.  the bound:

    ```text
    C_fl / (alpha lambda_Q) < 9 / 2.
    ```

    If base-only warping is relaxed, replace this by:

    ```text
    C_fl / (alpha lambda_Q) + epsilon_warp/alpha < 9 / 2.
    ```

This is now a sharply finite operator calculation, not an open-ended search for
another quotient.

# Relation to Recursive Topology

If the full topology contains a longer recursive tower, this theorem applies
to the selected exact-order-64 sector after either:

```text
1. an admissibility restriction to H_64,
```

or:

```text
2. a canonical descent from Z_{2^L} to the physical order-64 CP character.
```

Without such a restriction or descent, the theorem does not exclude larger
dyadic carriers.  It proves stability of the order-64 projector once the
physical CP sector is the exact-order-64 tower sector.

# Gate Status

```text
shared central circle exists                              CORPUS-SUPPORTED
circle Fourier/Laplacian cover law                        PROVED
Riesz coherent projector framework                         CORPUS-SUPPORTED
fixed arithmetic sector requirement                        IDENTIFIED
L_tower spectral gap equals 9                              PROVED
perturbative projector stability for ||E|| < 9 alpha/2      PROVED
Hessian normal form L_fl,MTT=alpha L_tower+E                PROVED*
symbolic E decomposition                                    PROVED*
pure central-circle reduction E_mix=E_cubic=0               PROVED**
compute alpha, C_fl, and lambda_Q                           OPEN
prove reduced Schur correction bound                        OPEN
```

`*` See `MTT_Flavor_Hessian_Block_Extraction_Attempt_for_Z64_Projector_v1.md`.
`**` See `Pure_Central_Circle_Block_Reduction_for_Z64_Hessian_Bound_v1.md`.

# Bottom Line

We have proved the right theorem:

```text
actual MTT flavor operator = scaled tower operator + small correction
=> same Z_64 projector.
```

The remaining work is a concrete Hessian extraction:

```text
L_fl,MTT | H_64 = alpha L_tower + E,
E = E_Schur,
C_fl / (alpha lambda_Q) < 9/2.
```

If that bound is established, the dyadic `Z_64` branch is fully selected by
the MTT coherent flavor operator.
