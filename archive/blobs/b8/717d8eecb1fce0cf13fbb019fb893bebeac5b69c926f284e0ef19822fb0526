---
abstract: |
  We close the Z64 certificate for the exact central-circle branch.  The
  certificate is not a new numerical fit: it is the canonical exact block
  already isolated by the shared-circle, spectral-projector, group-algebra,
  pure-circle, and exact Schur-collapse papers.  The finite carrier is
  K64=C[coker A64]~=C[Z64], with A64 the six-row dyadic carry matrix.  The
  primitive shift S is translation by the generator.  The selected exact
  Hessian block is the normalized central-circle tower operator L64=L_tower
  on the exact-order-64 tower sector, and the selected retarded kernel is
  Kret,64=S^{-1} (or its Hermitian symmetrization when a self-adjoint kernel
  is required).  Because this is the exact coherent central-circle branch,
  P_CP,64<=Pi_coh and [L,Pi_coh]=0, so the Schur correction vanishes.  Thus the
  Z64 exact-branch certificate is closed.  A stronger task remains only if one
  demands extraction of the same block from a larger non-exact MTT Hessian
  before imposing the exact central-circle branch.
author:
- Peter Nero
date: May 2026
title: |
  Z64 Exact Central-Circle Branch Certificate
---

# Purpose

The previous terminal certificate named the first remaining obligation:

```text
Z64 exact selected Hessian/kernel block.
```

This note fills that obligation for the exact central-circle branch.

It does not claim that every non-exact warped or mixed MTT branch has been
reduced.  It says:

```text
on the selected exact central-circle branch already isolated in the corpus,
the finite Z64 carrier, Hessian block, retarded kernel, coherent inclusion,
and Schur collapse are explicit.
```

# Carrier Data

Use the six-row dyadic carry matrix:

```text
A_64 =
[
  2 -1  0  0  0  0
  0  2 -1  0  0  0
  0  0  2 -1  0  0
  0  0  0  2 -1  0
  0  0  0  0  2 -1
  0  0  0  0  0  2
].
```

Then:

```text
coker A_64 ~= Z_64.
```

Define:

```text
G_64 := coker A_64,
K_64 := C[G_64].
```

Let `S` be translation by the generator `[x_0]`:

```text
S e_j = e_{j+1 mod 64}.
```

Then:

```text
S^64=I,
S^d != I for 0<d<64.
```

# Hessian Block

Let `H_64` be the exact-order-64 central-circle tower sector:

```text
H_64 = span{|d> : d_i>=2, product_i d_i=32}.
```

The selected exact branch is the pure central-circle tower:

```text
d_*=(2,2,2,2,2).
```

The normalized Hessian block is:

```text
L_64 = L_tower,
L_tower |d> = C(d)|d>,
C(d)=sum_i(d_i^2-1).
```

The spectral-projector theorem proves:

```text
C(d_*)=15,
C(d)>=24 for d!=d_*,
gap=9.
```

In physical units:

```text
L_64 = alpha L_tower,
alpha>0.
```

In normalized certificate units we set:

```text
alpha=1.
```

# Retarded Kernel

The selected nil-survivor retarded branch gives:

```text
16 -> 15.
```

On `K_64` this is:

```text
K_ret,64 = S^{-1}=S^63.
```

If a self-adjoint/Hermitian kernel is required, use:

```text
K_ret,64^H = (S+S^{-1})/2
```

with oriented retarded support selecting the `S^{-1}` side.  The primitive
support condition is unchanged because:

```text
gcd(64,63)=1.
```

# Coherent Inclusion and Exact Schur Collapse

In the exact central-circle branch:

```text
H_coh,64 = H_0 tensor K_64 tensor C|tau_64>
```

is retained by `Pi_coh`.  Therefore:

```text
P_CP,64 <= Pi_coh.
```

The exact block operator acts inside this retained coherent sector:

```text
[L,Pi_coh]=0.
```

Consequently the exact coherent-block Schur theorem gives:

```text
P_fl L Q = 0,
Q L P_fl = 0,
C_fl = 0,
E_Schur = 0.
```

# Certificate

The Z64 exact central-circle certificate is:

```text
carrier:             K_64=C[coker A_64]~=C[Z_64]
primitive shift:     S e_j=e_{j+1}
order(S):            64
relation SNF:        [64]
Hessian block:       L_64=alpha L_tower, alpha>0
retarded kernel:     K_ret,64=S^-1
coherent inclusion:  P_CP,64<=Pi_coh
commutator:          [L,Pi_coh]=0
Schur correction:    E_Schur=0
selected component:  q_64=15
```

# What This Closes

```text
Z64 exact central-circle branch certificate       CLOSED
selected q_64=15                                  CLOSED
Schur stability in exact branch                   CLOSED
```

# What This Does Not Claim

This does not close a stronger non-exact extraction problem:

```text
start with the full unprojected mixed MTT Hessian,
derive the exact central-circle branch without selecting it,
and prove all warp/mixing leakage bounds numerically.
```

That is no longer needed for the exact-branch q79 proof, but it remains a
useful robustness project.

# Bottom Line

The first terminal certificate is closed for the selected exact
central-circle branch:

```text
Z64 exact selected block -> q_64=15.
```
