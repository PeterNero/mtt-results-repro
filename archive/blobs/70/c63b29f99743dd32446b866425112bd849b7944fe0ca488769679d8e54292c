# C1 Finite Response Matrix Reduction Theorem

## Purpose

This note advances the selected C1 response program as far as the current
corpus allows. It does not claim the numerical C1 matrices. Instead, it closes
the finite-dimensional reduction:

```text
selected primitive contractions -> M_u,C1, M_d,C1, M_e,C1, M_nuD,C1.
```

Thus the remaining missing object is no longer an informal "matrix." It is a
specific list of primitive 3x3 contractions.

## Inputs Already Closed

The selected Iwasawa C1 driver is:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
alpha_2 = alpha_3 = 0.
```

The selected heterotic/Strominger paper supplies the operator-level source in
the Green-Schwarz part of `Xi`, and it supplies the Hessian principal blocks:
twisted Laplacians in the metric/dilaton and B-field directions, the
Yang-Mills Laplacian in the bundle direction, and positive OU weights on
residual moduli when present.

The Iwasawa seed supplies the normalized rank-one tree overlap:

```text
lambda_123 = integral_X Omega wedge Tr(Psi_1 wedge Psi_2 wedge Psi_3) = 1
```

after chiral rephasing.

## Finite C1 Response Reduction Theorem

Fix a sector:

```text
s in {u, d, e, nuD}.
```

Let the selected raw Yukawa functional be:

```text
Y_s_raw(Psi_L, Psi_R, H_s; Theta).
```

Let `deltaTheta_C1` solve the selected linearized fixed-point equation:

```text
Hess_Xi(Theta0) deltaTheta_C1
  = - Pi_coh grad V_C1(Theta0).
```

For each matter or Higgs zero-mode operator `D_a`, choose the selected
L2-horizontal gauge:

```text
P_a dotPsi_a,i = 0.
```

Then the zero-mode response is:

```text
dotPsi_a,i = - G_a Q_a dotD_a Psi_a,i,
```

where `G_a` is the reduced Green operator on the complement of the zero-mode
space and `Q_a=1-P_a`.

The finite C1 response matrix is:

```text
M_s,C1 = B_s,Theta
       + B_s,L
       + B_s,R
       + B_s,H
       + B_s,vertex
       + B_s,basis.
```

Entrywise:

```text
(B_s,Theta)_ij =
  partial_Theta Y_s_raw(Psi_L,i, Psi_R,j, H_s; Theta0)[deltaTheta_C1],

(B_s,L)_ij =
  -Y_s_raw(G_L Q_L dotD_L Psi_L,i, Psi_R,j, H_s; Theta0),

(B_s,R)_ij =
  -Y_s_raw(Psi_L,i, G_R Q_R dotD_R Psi_R,j, H_s; Theta0),

(B_s,H)_ij =
  -Y_s_raw(Psi_L,i, Psi_R,j, G_H Q_H dotD_H H_s; Theta0),

(B_s,vertex)_ij =
  selected explicit higher-derivative C1 Yukawa vertex, if present,

(B_s,basis)_ij =
  selected basis-transport or Gram-Schmidt correction in the named tree basis.
```

In the horizontal gauge the basis term is zero. If a different selected
Gram-Schmidt convention is used, `B_s,basis` must be supplied explicitly rather
than absorbed into the other terms.

## Proof

Differentiate the raw trilinear overlap along the selected one-parameter C1
branch. The derivative splits by the Leibniz rule into: direct background
variation, left zero-mode variation, right zero-mode variation, Higgs
zero-mode variation, and any explicit selected higher-derivative vertex.

The zero-mode variation follows from differentiating:

```text
D_a(epsilon) Psi_a,i(epsilon) = 0.
```

At first order:

```text
D_a dotPsi_a,i + dotD_a Psi_a,i = 0.
```

Restricting to the complement of the kernel and imposing the horizontal gauge
gives:

```text
dotPsi_a,i = -G_a Q_a dotD_a Psi_a,i.
```

Substitution into the differentiated trilinear overlap gives the stated six
finite 3x3 terms. The Riesz projector formula already recorded in the C1
insertion certificate gives the same result in contour form.

## Executable Gate

The calculator:

```text
scripts/compute_c1_response_matrices.py
```

expects the primitive contractions in:

```text
certificates/selected_c1_primitive_contractions.template.json
```

after every null is replaced by a selected 3x3 matrix. It then computes:

```text
M_u,C1, M_d,C1, M_e,C1, M_nuD,C1,
C33(M_u), C33(M_d), C33(M_e), C33(M_nuD),
Delta_v = (M_d13-M_u13, M_d23-M_u23).
```

## What This Does And Does Not Prove

This closes the finite assembly step. It proves that once the primitive
contractions are supplied, there is no remaining discretion in the finite C1
response matrices.

It does not prove the C1 matrices are nonzero. It does not prove rank lift. It
does not prove CKM noncommutation. Those claims require actual selected
primitive contractions from `deltaTheta_C1`, the full Hessian inverse, the
sector `dotD` operators, and the sector zero-mode bases.

## Next Required Data

The next task is to compute or supply:

```text
theta_overlap_variation,
left_zero_mode_response,
right_zero_mode_response,
higgs_zero_mode_response,
explicit_vertex,
basis_connection,
```

as 3x3 matrices for each sector `u,d,e,nuD`.
