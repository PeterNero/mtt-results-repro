# Selected Zero-Mode Basis and dotD Interface

## Purpose

The matrix-construction route ledger identified the next missing artifact:

```text
Selected Zero-Mode Basis and dotD Certificate.
```

This note formulates that artifact as an auditable interface.  It does not yet
claim the sector-resolved bases or the `dotD` operators.  It records exactly
what must be supplied before the C1 primitive contractions can be filled.

The goal is to turn:

```text
"find the zero modes"
```

into a finite checklist:

```text
sector slot -> selected operator -> kernel basis -> projector/Green operator
            -> dotD along alpha_1 -> horizontal response -> primitive blocks.
```

## Closed Inputs

The corpus already supplies:

```text
Iwasawa rank-one seed:
  three orthonormal harmonic representatives Psi_1, Psi_2, Psi_3,
  integral_X Omega wedge Tr(Psi_1 wedge Psi_2 wedge Psi_3) = 1,
  minimal rank-one representative E33.

Single-Higgs projection:
  H_u -> H,
  H_d -> H^dagger.

C1 driver:
  Tr_grav R_+^2 = v1_tilde alpha_1,
  v1_tilde = 8 r3^2/(r1^2 r2^2),
  alpha_2 = alpha_3 = 0.

C1 response rule:
  dotPsi_a,i = -G_a Q_a dotD_a Psi_a,i
  in the selected L2-horizontal gauge.
```

The important limitation is:

```text
Psi_1, Psi_2, Psi_3 are a normalized rank-one seed.
They are not yet the sector-resolved Q,u,d,L,e,N,H bases.
```

So the seed is a genuine input, but it cannot be copied into every SM sector
as if the representation split had already been computed.

## Sector Slots

The selected SM sectors require the following operator slots:

| Sector | Left slot | Right slot | Higgs projection |
|---|---|---|---|
| `u` | `Q` | `u` | `H` |
| `d` | `Q` | `d` | `H^dagger` |
| `e` | `L` | `e` | `H^dagger` |
| `nuD` | `L` | `N` | `H` |

The family slots are:

```text
Q, u, d, L, e, N.
```

Each family slot must have kernel dimension three in the selected branch.
The Higgs slot:

```text
H
```

is the one selected low-energy Higgs doublet carrier, with sector conjugation
handled by the sector projection rather than by adding a second Higgs knob.

## Required Data Per Slot

For each slot:

```text
a in {Q,u,d,L,e,N,H},
```

the future completed certificate must provide:

```text
D_a:
  selected zero-mode operator or elliptic complex,

domain_a:
  form degree, bundle, representation, and boundary or quotient condition,

ker D_a:
  kernel dimension and ordered basis,

Psi_a,i:
  selected representatives in the ordered basis,

K_a:
  L2 inner-product matrix before canonical normalization,

P_a:
  projector onto ker D_a,

Q_a:
  1 - P_a,

G_a:
  reduced Green operator on Q_a,

gap_a:
  positive complement gap or a rigorous finite-truncation bound,

dotD_a:
  derivative of D_a along the selected C1 alpha_1 deformation,

horizontal gauge:
  P_a dotPsi_a,i = 0.
```

The response is then forced:

```text
dotPsi_a,i = -G_a Q_a dotD_a Psi_a,i.
```

No entry of `dotPsi` is a tunable parameter.

## dotD Is Not A New Knob

The operator variation must be computed from:

```text
Theta(epsilon) = Theta_0 + epsilon deltaTheta_C1 + O(epsilon^2),
```

where:

```text
Hess_Xi(Theta0) deltaTheta_C1
  = -Pi_coh grad V_C1(Theta0)
```

and the source is the already selected C1 row:

```text
Tr_grav R_+^2 = v1_tilde alpha_1.
```

Therefore:

```text
dotD_a = d/depsilon D_a(Theta(epsilon)) at epsilon=0.
```

It is not valid to choose `dotD_a` to make a desired mass or CKM entry appear.

## Primitive Contraction Output

Once the slot data are supplied, each sector produces six primitive blocks:

```text
B_s,Theta,
B_s,L,
B_s,R,
B_s,H,
B_s,vertex,
B_s,basis.
```

In the horizontal gauge:

```text
B_s,basis = 0
```

unless a non-horizontal selected Gram-Schmidt convention is explicitly chosen.
If the explicit C1 Yukawa vertex is absent, then:

```text
B_s,vertex = 0
```

must be proved by the selected alpha-prime scheme.  It cannot be silently set
to zero.

The output target is:

```text
certificates/selected_c1_primitive_contractions.template.json
```

and the executable calculator is:

```text
scripts/compute_c1_response_matrices.py
```

## Iwasawa Galerkin First Pass

The fastest first attempt remains the Iwasawa invariant Galerkin route.  In
that pass, each representative is expanded in the selected finite invariant
form and bundle basis:

```text
Psi_a,i = sum_m c_a,i,m eta_a,m.
```

The same finite basis must also represent:

```text
D_a,
dotD_a,
P_a,
G_a.
```

This can close one of two useful outcomes:

```text
1. nontrivial primitive C1 blocks are computed exactly; or
2. the invariant subcomplex is proved insufficient, forcing non-invariant
   family modes into the next truncation.
```

Both outcomes are progress.  A rank-one-only invariant result would be an
obstruction, not a failure of the research program.

## Guardrails

The completed certificate must obey:

```text
no Execution II benchmark entries,
no observed masses or mixings,
no post-hoc fitted threshold factors,
no arbitrary modular weights,
no scalar Fourier central-circle modes masquerading as zero modes,
no q79 phases attached outside the selected channel-character rule,
no unproved zero primitive blocks.
```

The central-circle CP carrier is a finite coherent/deck character register, not
an untwisted scalar zero-mode tower.  That distinction must be preserved in
any proposed basis.

## Completion Gate

The zero-mode/dotD certificate is complete only when:

```text
all Q,u,d,L,e,N bases have dimension three,
the H carrier is selected and sector conjugation is specified,
all D_a and dotD_a are supplied from the same selected C1 deformation,
all P_a, Q_a, G_a and complement gaps are supplied,
the L2-horizontal gauge is enforced or the basis connection is supplied,
the primitive contraction file is filled without null entries,
the response calculator returns M_u, M_d, M_e, M_nuD,
the rank and CKM tests are evaluated before SM data comparison.
```

## Bottom Line

This interface closes the next layer of rigor.  It says exactly what it would
mean to have the selected zero modes and `dotD` operators needed for matrix
creation.

It does not compute the matrices yet.  But it removes ambiguity about what the
next successful computation must contain.
