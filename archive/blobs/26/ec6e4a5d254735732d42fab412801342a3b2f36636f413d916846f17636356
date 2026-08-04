# Iwasawa Non-Invariant Galerkin Execution Protocol

## Purpose

The invariant `A01` repair route is now retired as a proof source. The typed
monad/Cech route remains primary, but the current corpus does not supply the
typed sections. Therefore the active fallback is:

```text
non-invariant spectral Galerkin.
```

This note turns that fallback into an executable finite protocol. It does not
pretend the selected operator is already present. It says exactly what must be
fed in, how the matrices are built, and what inequality certifies three
selected family modes.

## Operator Source Gate

The protocol accepts only a selected operator source:

```text
typed monad/Cech data plus induced HYM or Dolbeault-Hodge operator,
corrected selected non-invariant A^(0,1) with integrability and residuals,
direct selected HYM/Strominger solve with gauge fixing and residuals.
```

It rejects:

```text
literal printed invariant A01,
small invariant repair of printed A01,
unselected sparse h1=3 diagnostic candidate,
rank-one Yukawa seed alone,
observed flavor data.
```

So the protocol keeps the credibility guardrail: no hidden fitting knob is
allowed to masquerade as `D_E`.

## Hilbert Space

Work in:

```text
H = L2(Omega^{0,*}(X,E))
```

or the sector-resolved bundle-valued spinor replacement. The operator is:

```text
D_E,
L_E = D_E^* D_E,
```

or the corresponding Dolbeault Laplacian. The input data must include:

```text
compact Iwasawa lattice or fundamental-domain boundary conditions,
bundle transition law or verified global-frame equivariance,
Hermitian metric and volume form,
gauge fixing or horizontal condition.
```

## Finite Basis

Choose nested finite spaces:

```text
V_N subset H,
P_N -> I strongly.
```

Two concrete basis implementations are admissible:

```text
1. deck-equivariant spectral/Fourier basis on the compact Iwasawa quotient;
2. finite-element or spectral-element basis on a fundamental domain with
   periodic/deck constraints.
```

The basis must include:

```text
left-invariant seed sector,
non-invariant modes,
bundle fiber basis,
sector labels for Q,u,d,L,e,N,H.
```

It must pass:

```text
G_N positive definite,
compact quotient identifications respected,
not only the invariant subspace,
no scalar central-circle Fourier mode treated as an untwisted zero mode.
```

## Matrix Construction

For a finite basis `b_i`, build:

```text
G_N[i,j] = <b_i,b_j>,
K_N[i,j] = <D_E b_i, D_E b_j>.
```

Then solve the generalized eigenproblem:

```text
K_N v = lambda G_N v.
```

If the basis is orthonormal, this reduces to:

```text
L_N = K_N.
```

For a `G_N`-orthonormal family eigenvector matrix `V_fam`, the finite family
projector is:

```text
P_fam,N = V_fam V_fam^* G_N.
```

The reduced Green operator on the complement is:

```text
G_red,N = sum_{lambda_j outside family} lambda_j^{-1} v_j v_j^* G_N.
```

This is the object needed by the `dotD` and C1 response machinery.

## Gap And Error Rule

Let the computed family cluster obey:

```text
lambda_1 <= lambda_2 <= lambda_3 <= epsilon_low,
lambda_4 >= gamma_gap.
```

Let the total certified error be:

```text
eta_total = eta_basis + eta_operator_residual + eta_quadrature + eta_HYM.
```

The pass rule is:

```text
epsilon_low + eta_total < tau < gamma_gap - eta_total
```

for some `tau > 0`.

Then the Riesz projector below `tau` has rank three and is stable under the
certified errors. This is the finite statement we need before claiming selected
family representatives.

## Outputs If The Gate Passes

The successful certificate must output:

```text
kernel_dimension = 3,
Psi_1,Psi_2,Psi_3 as G_N-orthonormal representatives,
anti-family absence or separation by the certified gap,
sector maps Q,u,d,L,e,N,H,
dotD_alpha1 in the same basis,
reduced Green operator,
E6 cubic or sector overlap tensor.
```

Those outputs fill:

```text
iwasawa_selected_cohomology_data.template.json,
selected_zero_mode_basis_dotd_interface_certificate.json,
selected_c1_primitive_contractions.template.json.
```

## Verdict

The selected numerical or symbolic values are still open. But the fallback is
no longer vague. The next concrete task is:

```text
fill this protocol with one selected D_E source and a first finite
non-invariant basis V_N.
```

If the gap/error inequality passes, the three selected family modes are
certified. If it fails, the failure is also informative: it tells us whether
the issue is operator selection, basis size, residual control, or absence of a
three-mode cluster.
