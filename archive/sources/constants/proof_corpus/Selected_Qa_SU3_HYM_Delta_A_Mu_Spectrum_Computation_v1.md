# Selected Qa/SU3 HYM Delta_A Mu Spectrum Computation

## Purpose

This note computes the first executable piece of the selected `Delta_A(mu)`
gate.

The full Strominger Hessian uses the bundle Yang-Mills Laplacian on
`u(E)`-valued 1-forms.  The corpus does not provide that complete operator.
However, the extracted HYM matrix data does force one algebraic invariant-band
block:

```text
H_alg(mu) = sum_i ad(B_i)^* ad(B_i)
```

on `End(C^3)`, where the `B_i` are the coefficient matrices in
`A^(0,1)`.

## Computed Block

On `End(C^3)`, the block has dimension 9.  The identity endomorphism is a
zero commutator mode.  The remaining eight complex adjoint directions are
positive in the sampled algebraic block.

Sample eigenvalues:

```text
mu = 0.25:
0, 0.09063535, 0.25, 0.25, 0.3125, 0.375, 0.5, 0.5625, 1.03436465

mu = 1:
0, 1, 1, 1.26794919, 2, 2, 3, 3, 4.73205081

mu = 4:
0, 4, 4, 8, 10.14359354, 20, 24, 36, 37.85640646
```

This confirms that the adjoint commutator block is nontrivial and positive
away from the identity zero mode.

## Why This Still Does Not Select Mu

The algebraic block alone is not the full `Delta_A`.  It excludes:

```text
real unitary u(E) slice,
Hermitian metric normalization,
Chern (1,0) conjugate connection pieces,
Iwasawa metric/radius weights,
torsional endomorphism and curvature terms,
gauge fixing and quotient of symmetry directions,
OU weights gamma_{n,k}^{-1},
full zeta/heat regularization.
```

The sampled log-det-prime of this block is monotone in the sampled `mu`
values, so the block by itself does not select an interior `mu`.  Treating it
as final would either choose a boundary or sneak in a normalization convention.

## Verdict

```text
Delta_A(mu) algebraic block computed: yes
full real Strominger Hessian computed: no
mu selected: no
numeric Qa/SU3 determinant: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_HYM_Full_Real_Delta_A_Hessian_With_OU_Weights_v1
```
