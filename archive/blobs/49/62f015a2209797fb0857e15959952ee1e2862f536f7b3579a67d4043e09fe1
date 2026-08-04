---
abstract: |
  We formulate the selected C1 curvature insertion operator for the no-proxy
  rank-one Yukawa lift.  The operator is not an entry-wise curvature knob.  It
  is the linear response of the selected raw Yukawa overlap functional under
  the selected alpha-prime deformation of the R_+ Strominger/MTT fixed point.
  The formula includes the deformation of the background, Riesz-projector
  response of the zero modes, and a separation rule: if curvature changes only
  matter kinetic metrics, the effect belongs to C5 canonical normalization,
  not to a raw C1 Yukawa entry.  This closes the formal meaning of O_C1 while
  leaving numerical C1 weights open.
author:
- Peter Nero
date: May 2026
title: |
  C1 Curvature Insertion Formula for Rank-One Lift
---

# Purpose

The previous C1 audit proved that C1 is an admissible source class.  It did
not define the actual insertion operator.

This note closes the next layer:

```text
What exactly is O_C1?
```

The answer is:

```text
O_C1 is the first variation of the selected Yukawa overlap functional along
the selected alpha-prime/R_+ curvature deformation of the MTT fixed point.
```

It is not a scalar factor inserted into individual Yukawa entries.

# Selected Scheme

The C1 scheme is fixed as far as the corpus currently permits:

```text
connection:      R_+ or R^+, the Bismut/Hull torsional connection,
field strength:  Hhat = dB - alpha_prime/4(omega3(A)-omega3(omega_plus)),
background:      selected Strominger/MTT fixed point,
gauge:           fixed gauges, orthogonal to symmetry directions.
```

The remaining scheme ambiguity is the local field-redefinition convention at
higher alpha-prime order.  This is not optional bookkeeping: without it,
different representatives of the same physical background may move
contributions between the raw overlap and canonical normalization.

# Raw Yukawa Functional

For a sector `s`, write the raw selected overlap schematically as:

```text
Y_s^raw(Theta)_{ij}
  = Integral_X Omega_Theta wedge d_s(
      Psi_{L,i}^{(s)}
      wedge Psi_{R,j}^{(s)}
      wedge H_s
    ).
```

Here `d_s` denotes the E6/SM tensor contraction for the sector after the
single-Higgs projection, and the fields are selected zero-mode representatives.

The C1 channel is character-trivial:

```text
chi_{s,C1} = 1.
```

# Selected C1 Deformation

Let `epsilon` denote the selected C1 curvature-deformation parameter.  The
background is:

```text
Theta(epsilon) = Theta0 + epsilon deltaTheta_C1 + O(epsilon^2).
```

The selected first-order deformation is not arbitrary.  In fixed gauges it is
defined by the linearized selection equation:

```text
Hess_Xi(Theta0) deltaTheta_C1
  = - Pi_coh grad V_C1(Theta0),
```

orthogonal to symmetry directions.  The positive Hessian and bounded projector
results in the Strominger/MTT corpus make this a well-posed linear-response
problem once `V_C1` and the Hessian blocks are supplied.

# Zero-Mode Response

Let `D_a(epsilon)` be the selected elliptic zero-mode operator for a matter or
Higgs species `a`, and let `P_a(epsilon)` be the Riesz projector onto its
selected zero-mode subspace.  For a contour `Gamma_a` enclosing the zero
cluster and no other spectrum:

```text
P_a(epsilon)
  = (1/(2*pi*i)) Integral_Gamma_a (z - D_a(epsilon))^(-1) dz.
```

Thus:

```text
dotP_a
  = -(1/(2*pi*i)) Integral_Gamma_a
      (D_a - z)^(-1) dotD_a (D_a - z)^(-1) dz.
```

The zero-mode response is:

```text
dotPsi_a = dotP_a Psi_a + GramSchmidt_a,
```

where the Gram-Schmidt term keeps the selected `L2` family basis normalized to
first order.

# C1 Insertion Formula

The selected C1 insertion is the derivative:

```text
O_C1[Y_s]_{ij}
  := d/depsilon |_{epsilon=0}
     Y_s^raw(
       Theta(epsilon),
       P_L(epsilon) Psi_{L,i},
       P_R(epsilon) Psi_{R,j},
       P_H(epsilon) H_s
     ).
```

Equivalently, the first variation has the schematic expansion:

```text
delta_C1 Y_s^raw
  =
    Integral_X delta_C1(Omega,measure,dilaton)
      wedge d_s(Psi_L wedge Psi_R wedge H)

  + Integral_X Omega
      wedge d_s(dotPsi_L wedge Psi_R wedge H)

  + Integral_X Omega
      wedge d_s(Psi_L wedge dotPsi_R wedge H)

  + Integral_X Omega
      wedge d_s(Psi_L wedge Psi_R wedge dotH_s)

  + explicit higher-derivative Yukawa vertex term,
    if and only if the selected effective action contains such a term.
```

This is the raw C1 Yukawa insertion.  Its channel weight is:

```text
W_{s,C1,ij} = A_{s,C1,ij} exp(-S_{s,C1}),
```

with trivial character.

# Kinetic Separation Rule

There is an important trap here.  If the selected alpha-prime curvature
deformation changes only the `L2` metrics of the matter fields, and does not
change the raw holomorphic/cohomological overlap or add an explicit selected
Yukawa vertex, then that effect is not a raw C1 Yukawa entry.

It belongs to:

```text
C5 kinetic metrics and canonical normalization.
```

This prevents double counting and prevents a hidden entry-wise fit.

# Theorem

#### C1 Linear-Response Insertion Theorem

On the current Theta/q79/Iwasawa branch, the selected C1 insertion operator is
well-defined at formal linear-response level as the first variation of the
selected raw Yukawa overlap under the selected R_+ alpha-prime curvature
deformation, with zero-mode projectors varied by the Riesz formula and
kinetic-only effects assigned to C5.

#### Proof

The C1 source audit retains C1 in every Dirac sector and proves that its q79
character is trivial.  The channel-weight extraction protocol requires every
non-tree channel to enter through a selected insertion operator, selected
zero-mode overlaps, and selected action/cost data.

The strings/flux corpus selects the torsional `R_+`/`R^+` connection and the
Green-Schwarz corrected field `Hhat`.  The Strominger/MTT selection corpus
gives fixed gauges, bounded twisted projectors, and a positive Hessian near
the selected fixed point.  Therefore a selected curvature deformation is, at
formal level, the solution of the linearized Hessian equation above, once the
explicit higher-alpha-prime functional is supplied.

The selected matter and Higgs modes are zero modes of elliptic operators with
bounded projectors.  Standard Riesz-projector differentiation gives the
first-order variation of the selected zero-mode subspaces.  Differentiating
the raw overlap functional gives the displayed operator `O_C1`.

Because canonical normalization is a separate `C5` datum in the finite
channel-set certificate, purely kinetic changes must be kept outside the raw
C1 overlap channel.  This proves the formal insertion rule and the separation
rule.  Numerical C1 weights remain open because `V_C1`, the Hessian blocks,
the operators `dotD_a`, and the selected zero-mode bases have not yet been
evaluated.

# What This Closes

```text
O_C1 formal definition,
R_+ scheme source,
linearized Hessian response form,
Riesz projector response form,
kinetic separation rule,
trivial C1 character.
```

# What Remains Open

```text
selected local field-redefinition scheme,
explicit V_C1 functional,
explicit Hess_Xi blocks,
explicit dotD_a operators,
deltaTheta_C1,
zero-mode response integrals,
C1 A_gamma values,
C1 S_gamma values,
family kinetic metrics,
canonical Yukawa matrices,
RG and threshold matching.
```

# Next Calculation

The next executable object should supply:

```text
C1CurvatureLinearDataCertificate:
  V_C1
  Hess_Xi blocks
  dotD_L, dotD_R, dotD_H
  selected zero-mode basis
  C1 overlap integrals
```

That is the point where C1 either produces nonzero light-family lift
coefficients or fails as a lift source.

Follow-up status: the Iwasawa Rplus support row is now closed.  On the
selected invariant Iwasawa branch:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
alpha_2 = alpha_3 = 0.
```

Thus the remaining linear-response calculation starts from a single invariant
`alpha_1` curvature row.

Follow-up rank status: for the induced response matrix `M_C1^(alpha1)`, the
leading full-rank test is now:

```text
C33(M_C1) = M11*M22 - M12*M21 != 0.
```

The insertion chain therefore needs the four light-family contractions first:
`M11`, `M12`, `M21`, and `M22`.
