# Iwasawa Spectral Galerkin Operator Gate

## Purpose

The typed monad section recovery attempt triggered the non-invariant spectral
Galerkin fallback. This note sharpens that fallback into a finite input
contract.

The key point is simple:

```text
spectral fallback cannot start from an index or from the rank-one seed;
it must start from a selected operator D_E.
```

Once `D_E` is supplied, the computation is finite at each cutoff and auditable.
Without `D_E`, there is no honest spectral matrix to diagonalize.

## Admissible Sources For D_E

There are three admissible ways to supply the operator.

### R1: Corrected Non-Invariant Dolbeault Operator

Supply explicit non-invariant connection data on the selected
Iwasawa/Strominger branch and verify:

```text
barpartial_E^2 = 0,
Bianchi/Strominger compatibility,
HYM or controlled HYM residual,
not a sparse invariant typo repair.
```

This is the direct fallback route.

### R2: Typed Monad Sections

Supply the missing typed monad data:

```text
f_i in H^0(X, L_i tensor K1^{-1}),
g_i in H^0(X, K2 tensor L_i^{-1}),
g o f = 0,
exactness or controlled sheaf substitute.
```

This would reopen the primary Cech route and also define a spectral operator.

### R3: Direct Selected HYM Solve

Supply a validated symbolic or numerical HYM/Strominger solve in the fixed
topological sector:

```text
fixed Chern/gerbe/Bianchi sector,
connection residual bounds,
gauge fixing / horizontal condition,
self-adjoint or complex-elliptic operator package.
```

This is acceptable only if the residual and selection certificates are explicit.

## Galerkin Contract

Given a selected operator `D_E`, choose finite subspaces:

```text
B_N subset L2(bundle-valued forms/spinors on X)
```

with projection `P_N`. The basis must:

```text
respect the compact Iwasawa lattice,
include the left-invariant seed sector,
include non-invariant modes,
include bundle fiber data,
be L2-orthonormal or supply a Gram matrix.
```

Then form:

```text
L_N = P_N D_E^* D_E P_N
```

or the corresponding Dolbeault Laplacian matrix. The family projector is not a
choice; it is the Riesz projector onto an isolated low-spectrum cluster after a
gap is proved.

## Required Numerical Certificate

The finite spectral certificate must supply:

```text
basis index set B_N,
Gram matrix G_N,
operator matrix L_N,
low eigenpair table,
Riesz projector P_fam,N,
residual norms,
complement gap,
truncation-error bound.
```

The pass condition is:

```text
exactly three selected family modes,
anti-family modes absent or separated above the gap,
explicit Psi_1,Psi_2,Psi_3 representatives,
sector projections into Q,u,d,L,e,N,H,
dotD_alpha1 in the same basis,
reduced Green operator on the complement.
```

## Why This Is The Right Next Target

All previous shortcuts are blocked:

```text
literal A01: not integrable,
one-index repair: h1 = 2,
e3 torsion-support invariant branch: h1 = 2,
sparse h1 = 3 candidates: unselected and drop e3,
index c3 = 6: net chirality, not representatives,
rank-one seed: one tree-level cubic, not a full family basis.
```

Therefore the next genuine advance is not a new flavor texture. It is the
selected operator-plus-basis package:

```text
D_E, B_N, L_N, Riesz projector, gap/error bound.
```

Once that is supplied, the existing templates already know what to do with the
output: fill the selected cohomology data, then the zero-mode/dotD interface,
then the primitive C1 contractions.

## Verdict

The fallback is active, but the spectral computation is not yet executed. It is
now reduced to a finite, auditable operator problem:

```text
supply or construct one admissible selected operator D_E,
then build B_N and L_N.
```
