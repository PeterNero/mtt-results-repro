---
abstract: |
  We construct the coherent flavor projector needed to complete the Z_64
  dyadic gate, under a concrete spectral minimal-cover model compatible with
  the MTT gap principle.  The central-circle Hilbert space has Fourier
  characters chi_n with Laplacian cost proportional to n^2.  A connected
  finite circle cover D_d(z)=z^d has character pullback n -> dn and therefore
  spectral cover cost increasing with d^2.  Among exact-order-64 towers with
  terminal spinorial parity, the refinement degrees must multiply to 32.
  The additive Laplacian cover cost is uniquely minimized by five elementary
  degree-two covers: D_2,D_2,D_2,D_2,D_2.  The associated six record levels
  carry cumulative classes x_0,...,x_5 and terminal parity 2x_5=0, hence
  coker A ~= Z_64.  The Riesz projector around this isolated lowest eigenvalue
  is the coherent flavor projector P_fl.  Thus P_fl dynamically selects
  R=D_2^*, level-six parity placement, and the Z_64 dyadic tower, provided the
  MTT flavor closure-strain generator has the stated central-circle
  Laplacian-cover normal form.
author:
- Peter Nero
date: May 2026
title: |
  Spectral Flavor Projector Construction for the Z64 Dyadic Tower
---

# Purpose

The last remaining dyadic task was:

```text
construct P_fl directly
and show P_fl selects D_2^*, six records, and terminal spinorial parity.
```

This paper gives that construction under a concrete spectral closure-strain
model.

The model uses only standard MTT ingredients:

```text
shared central circle S^1_cen,
Fourier character spectrum,
positive spectral gap,
Riesz projector selection,
spinorial terminal parity,
exact order-64 CP requirement,
no-proxy/minimal bottleneck selection.
```

# Central-Circle Spectrum

Let:

```text
H_c = L^2(S^1_cen).
```

Use the normalized Fourier characters:

```text
chi_n(z)=z^n,
n in Z.
```

The circle Laplacian satisfies:

```text
-Delta_c chi_n = (n^2/R_c^2) chi_n.
```

Thus higher character degree costs more spectral energy.  Up to the common
factor `R_c^{-2}`, the degree cost is:

```text
E(n)=n^2.
```

# Compatibility Caveat

This Fourier calculation is a closure-strain cost model for shared-circle
cover/refinement degrees.  It is not the claim that nonzero scalar Fourier
characters belong to the untwisted scalar circle Laplacian kernel.

For compatibility with the QG/coherent projector, the physical `Z_64` CP labels
must be represented by a retained finite Wilson/deck character carrier:

```text
K_64 ~= C[Z_64],
```

with the scalar central-circle zero mode supplying the shared coherence channel.
The tower operator below then acts on finite carrier/refinement labels, while
the coherent projector retains the carrier block.

# Cover-Degree Cost

A connected finite circle refinement is:

```text
D_d(z)=z^d,
d in Z_{>0}.
```

It acts on characters by:

```text
D_d^* chi_n = chi_{dn}.
```

So a refinement step of degree `d` sends a unit character to a degree-`d`
character and has relative Laplacian cost:

```text
c(d)=d^2-1.
```

The subtraction makes the trivial degree-one cover cost zero.

For a tower of refinements with degrees:

```text
d_0,d_1,...,d_{m-1},
```

define the additive cover cost:

```text
C_tower(d_0,...,d_{m-1})
= sum_i (d_i^2-1).
```

This is the Schur-reduced central-circle closure-strain cost for the cover
degrees.

# Exact Order-64 Constraint

Terminal spinorial parity contributes order two:

```text
2x_terminal=0.
```

If the refinement degrees are `d_i`, the dyadic order is:

```text
N = 2 product_i d_i.
```

Exact order `64` therefore requires:

```text
product_i d_i = 32.
```

# Admissible Elementary Towers

Spin compatibility requires nontrivial dyadic refinement degrees:

```text
d_i >= 2.
```

The no-proxy/minimal bottleneck rule excludes inserting irrelevant degree-one
records.

Thus the exact-order-64 admissible degree sequences are ordered factorizations
of:

```text
32
```

by integers at least `2`.

# Lemma: Unique Minimal-Cost Tower

Among all ordered factorizations of `32` into integers at least `2`, the cost:

```text
sum_i (d_i^2-1)
```

is uniquely minimized by:

```text
(2,2,2,2,2).
```

## Proof

For any integer `ab` with `a,b >= 2`,

```text
(ab)^2 - 1 > (a^2 - 1) + (b^2 - 1).
```

Indeed:

```text
(ab)^2 - 1 - (a^2 - 1) - (b^2 - 1)
= a^2b^2 - a^2 - b^2 + 1
= (a^2-1)(b^2-1)
> 0.
```

Therefore splitting a composite degree into two nontrivial factors strictly
lowers the cover cost.  Repeatedly splitting any factor of `32` larger than
`2` strictly lowers the cost until every factor is `2`.

Since:

```text
32 = 2^5,
```

the unique fully split tower is:

```text
(2,2,2,2,2).
```

This proves uniqueness.

# Construction of the Projector

Let `A_64` be the finite set of exact-order-64 admissible towers:

```text
A_64 = {ordered degree sequences d_i >= 2 : 2 product_i d_i = 64}.
```

Define the tower Hilbert space:

```text
H_tower = direct sum_{d in A_64} C |d>.
```

Define the tower closure generator:

```text
L_tower |d> = C_tower(d) |d>.
```

The lemma shows that the lowest eigenvalue is isolated and simple, with
eigenvector:

```text
|2,2,2,2,2>.
```

Let `gamma` be a small contour enclosing only this lowest eigenvalue.  Define:

```text
P_fl
= (1/2pi i) integral_gamma (z-L_tower)^{-1} dz.
```

Then:

```text
im P_fl = C |2,2,2,2,2>.
```

This is the coherent flavor projector onto the minimal exact-order-64 dyadic
tower.

# Theorem: Dynamic Selection of the Z64 Tower

Assume:

1.  the flavor CP dyadic sector is represented by exact-order-64 shared-circle
    refinement towers with terminal spinorial parity;

2.  the Schur-reduced central-circle closure-strain generator has the additive
    Laplacian cover-degree normal form:

    ```text
    C_tower = sum_i (d_i^2-1);
    ```

3.  the coherent flavor projector is the Riesz projector onto the isolated
    lowest closure-strain eigenvalue in this exact-order sector.

Then:

```text
P_fl selects the tower (2,2,2,2,2).
```

Equivalently:

```text
R = D_2^*,
six record levels x_0,...,x_5,
terminal spinorial parity at x_5,
Gamma_2 ~= Z_64.
```

## Proof

By the unique minimal-cost lemma, the exact-order-64 tower `(2,2,2,2,2)` has
strictly lower closure cost than every other admissible tower.  Therefore its
eigenvalue is isolated in `L_tower`.  The Riesz projector around that
eigenvalue has image exactly the span of this tower.

For each degree-two step:

```text
D_2^* chi_n = chi_{2n},
```

so the cumulative carry classes obey:

```text
x_{i+1}=2x_i, i=0,...,4.
```

Terminal spinorial parity gives:

```text
2x_5=0.
```

Therefore:

```text
x_5=32x_0,
64x_0=0,
coker A ~= Z_64.
```

This proves the theorem.

# What Has Now Been Proved

The dynamic projector construction is complete under the stated spectral
normal form:

```text
P_fl = Riesz projector onto the unique lowest exact-order-64 tower.
```

It selects:

```text
D_2^*,
five degree-two refinement steps,
six record levels,
terminal parity at level six,
Z_64.
```

# Remaining Identification Gate

The final remaining task is not algebraic.  The operator-identification
criterion is now proved in:

```text
MTT_Flavor_Operator_Identification_Criterion_for_Z64_Projector_v1.md.
```

It says that the abstract closure generator `L_tower` is sufficient for the
actual MTT flavor closure-strain operator whenever the latter has the
restricted form:

Required identification:

```text
L_fl,MTT restricted to exact-order-64 central-circle towers
= alpha L_tower + E,
||E|| < 9 alpha / 2.
```

In normalized tower units this is `||E|| < 4.5`.  Under that bound, the Riesz
projector is stable and selects the same discrete tower label.

# Spectral Gap

The minimal tower cost is:

```text
C(2,2,2,2,2)=5(2^2-1)=15.
```

The nearest compressed exact-order-64 competitor is:

```text
(2,2,2,4),
```

with cost:

```text
3(2^2-1)+(4^2-1)=24.
```

So the tower selection gap is:

```text
Delta_tower = 9.
```

Any controlled correction with operator norm less than `Delta_tower/2` leaves
the selected Riesz projector unchanged.

# Consequence for q=79

With:

```text
Gamma_2 ~= Z_64,
```

the already-proved chain gives:

```text
q_64=15.
```

Together with:

```text
q_7=2,
```

CRT gives:

```text
q=79 mod 448.
```

# Gate Status

```text
circle Fourier spectrum gives degree cost n^2                  PROVED
finite cover D_d acts as n -> dn                               PROVED
exact order64 requires product degrees 32                      PROVED
additive Laplacian cost uniquely selects five D_2 steps         PROVED
Riesz projector onto lowest tower selects D_2^* tower           PROVED
terminal parity at sixth record gives Z_64                     PROVED
operator-identification stability criterion                    PROVED*
Hessian normal form L_fl,MTT=alpha L_tower+E                    PROVED**
pure central-circle reduction E_mix=E_cubic=0                  PROVED***
Schur constant reduced to mixing product C_fl                  PROVED****
compute alpha, C_fl, and lambda_Q                               OPEN
prove reduced Schur correction bound                            OPEN
```

`*` See `MTT_Flavor_Operator_Identification_Criterion_for_Z64_Projector_v1.md`.
`**` See `MTT_Flavor_Hessian_Block_Extraction_Attempt_for_Z64_Projector_v1.md`.
`***` See `Pure_Central_Circle_Block_Reduction_for_Z64_Hessian_Bound_v1.md`.
`****` See `Schur_Gap_Constant_Reduction_for_Z64_Projector_v1.md`.

# Bottom Line

The fully explicit projector is:

```text
P_fl
= (1/2pi i) integral_gamma (z-L_tower)^{-1} dz,
```

where `L_tower` is the central-circle cover-degree closure generator.

It dynamically selects:

```text
(D_2,D_2,D_2,D_2,D_2)
+ terminal spin parity
=> Z_64.
```

The last remaining physical computation is to extract the actual MTT
closure-strain block.  The pure central-circle reduction sharpens the target
to:

```text
L_fl,MTT | H_64 = alpha L_tower + E_Schur
```

and prove:

```text
C_fl / (alpha lambda_Q) < 9/2.
```

If fiber-dependent warp leakage is admitted, the condition becomes:

```text
C_fl / (alpha lambda_Q) + epsilon_warp/alpha < 9/2.
```
