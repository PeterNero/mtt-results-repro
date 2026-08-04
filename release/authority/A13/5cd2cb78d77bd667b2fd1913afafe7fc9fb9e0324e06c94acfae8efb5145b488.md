# Equivariant Central Circle TT Support Theorem v1

## Algebraic Theorem

Let `U_TT` be the real helicity-2 carrier

```text
U_TT : span{TT_plus, TT_cross} -> |d_*> tensor span{c_2,s_2} subset C[Z64].
```

Here `c_2,s_2` are the real `k=2/k=62` character pair. The cyclic `Z64` shift
restricts to spin-2 rotation on this plane, so `U_TT` is the same-angle
equivariant carrier.

If the actual adjoint TT co-shape map factors as

```text
B^*P_TT = U_TT C
```

for an invertible `2 x 2` TT normalization matrix `C`, then

```text
Pi_exact64 B^*P_TT = B^*P_TT.
```

## Proof

The script verifies the finite character calculation directly.

1. The `k=2` real character vectors `c_2,s_2` are orthonormal in `C[Z64]`.
2. The `Z64` shift restricts to rotation by the spin-2 sampled angle on
   `span{c_2,s_2}`.
3. The orthogonal projector `Pi_exact64` fixes the image of `U_TT`.
4. Therefore it fixes every rank-two co-shape map of the form `U_TT C`.

This closes the algebraic part of the equivariant selector.

## What Remains

The actual source-level statement is still open:

```text
The metric shape map B=DG(Psi*)Pi_coh has adjoint TT support
B^*P_TT = U_TT C
```

on the selected exact GR/QG branch, for an invertible TT normalization `C`, and
with the same central-circle angle as the exact `Z64` shift.

This is strictly smaller than the previous missing premise. We no longer need
to assume the exact support identity directly. We only need to source or compute
same-angle equivariance/factorization of the actual shape map; the support
identity then follows by finite linear algebra.

## Consequence If The Remaining Source Gate Closes

```text
support(J_TT)=|d_*> tensor span{c_2,s_2}
lambda_GR,TT=15
```

in normalized internal exact-branch units.
