# q79 Finite Root-Stack Reynolds TT Hessian and Direct Operator Exit v1

Date: 2026-07-15

Status:
`Q79_FINITE_ROOTSTACK_REYNOLDS_TT_HESSIAN_CLOSED_EXACT_ONE_SCALE_CONTINUUM_BALANCED_HYM_NOT_CLAIMED`

## Theorem

Use the already selected finite q79 full-monodromy symbol

```text
W_fin = R^3_D direct-sum R^3_E
```

with the diagonal sheet action of `S3`. Let

```text
P_Haar = (1/6) sum_{g in S3} rho(g).
```

The exact group average is

```text
P_Haar = diag((1/3) 11^T, (1/3) 11^T).
```

It is symmetric, idempotent, and rank two. Its image is exactly the two
trivial sheet/edge trace modes.

Define the normalized finite closure-defect action

```text
S_fin(w) = kappa_fin/(4|S3|) sum_g ||w-rho(g)w||^2.
```

Direct differentiation gives

```text
H_fin = kappa_fin (I-P_Haar).
```

Thus the normalized shape has spectrum

```text
0 with multiplicity 2,
1 with multiplicity 4.
```

The four positive directions are the two copies of the standard `S3`
representation. In an orthonormal standard vector in each lane, the physical
multiplicity block is exactly

```text
H_std = kappa_fin I2,
h_DE = 0,
h_DD = h_EE = kappa_fin > 0.
```

The previously constructed root-independent `J_DE` commutes with both
`P_Haar` and `H_fin`. No dimensionless coefficient is fitted. Only the single
overall action normalization `kappa_fin` remains.

## Why this is selected rather than guessed

The q79 cusp/root-stack theorem supplies the full `S3` sheet monodromy. The
spectral-symbol theorem supplies the two permutation copies `D` and `E`. On a
finite group orbit, normalized Haar counting is the unique invariant
probability trace. The displayed action is the corresponding mean squared
failure of global sheet closure, so its Hessian is an exact finite-source
object, not a continuum quadrature approximation.

This uses the same finite-projected-source standard already proved for the MTT
HYM program: finite trace and projected operations are exact on the selected
finite algebra.

## Type guard

The existing nonlinear one-row HYM replay is a genuine rank-2 extension
calculation. The q79 spectral visible carrier is rank 3. Therefore the rank-2
solution cannot simply be relabeled as the missing rank-3 Fu-Yau HYM block.
This theorem avoids that type error by calculating directly on the selected
finite root-stack symbol.

## Exact scope

Closed now:

```text
finite q79 direct-operator Hessian,
the projected 2x2 TT block,
J_DE invariance at the finite source tier,
zero dimensionless Hessian fits,
one and only one overall action normalization.
```

Not claimed:

```text
construction of the nonzero-Chern inverse Fourier-Mukai visible bundle,
the balanced continuum Fu-Yau HYM connection or Hessian,
selection of the finite exit over every continuum completion,
the numerical Newton scale.
```

The old `2/11` Fourier-Mukai count therefore remains correct for the continuum
route, but it no longer blocks the finite projected q79 operator exit.
