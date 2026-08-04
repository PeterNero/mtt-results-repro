# Selected Qa/SU3 Mu-Independent Completion No-Go v1

## Purpose

This closes as much as possible of the remaining torsion/OU gate without
inventing data.

The previous artifact inserted the selected Iwasawa geometry into the real HYM
Chern block.  This note proves that any remaining completion term which is
positive and independent of `mu` cannot select `mu`.

## Pencil Identity

With the selected Iwasawa metric weights inserted, the real algebraic block has
the exact form

```text
H_weighted(mu) = mu A + mu^2 B.
```

This is forced by the source connection:

```text
B1, B2 scale as sqrt(mu),
B3 scales as mu.
```

The commutator Hessian therefore receives `mu` contributions from `B1,B2` and
`mu^2` contributions from `B3`.

Numerically, reconstructing `H(mu)` from `mu A + mu^2 B` gives max absolute
errors below machine precision.

The eigenvalues of `A` on the real `u(3)` slice are

```text
0, 0, 0.101428671, 0.101428671, 0.101428671,
0.101428671, 0.202857342, 0.202857342, 0.405714683.
```

The eigenvalues of `B` on the real `u(3)` slice are

```text
0, 0, 0.05072574, 0.05072574, 0.05072574,
0.05072574, 0.10145148, 0.10145148, 0.20290296.
```

So `A >= 0` and `B >= 0`.

After quotienting the central commutator zero mode, `H_Q(mu)` is positive
definite for `mu > 0`.

## Monotonicity

On the quotient,

```text
d/dmu log det H_Q(mu)
  = Tr[H_Q(mu)^-1 (A_Q + 2 mu B_Q)].
```

Since `H_Q(mu)` is positive definite and `A_Q + 2 mu B_Q` is positive
semidefinite and nonzero for `mu > 0`, this derivative is positive.

Therefore the metric-weighted algebraic determinant is strictly increasing in
`mu`.

## Consequence

Any positive completion term `C` that is independent of `mu` gives

```text
H_total(mu) = H_Q(mu) + C.
```

Its derivative is still

```text
H_total'(mu) = A_Q + 2 mu B_Q >= 0.
```

Thus a `mu`-independent positive torsional endomorphism, OU lift, or common
frame normalization cannot create an interior stationary point.

This rules out as the missing selector:

```text
any mu-independent positive semidefinite OU lift C,
any mu-independent positive semidefinite torsional endomorphism C,
any common positive scalar frame normalization,
any source term depending only on the selected Iwasawa radius R_* and r3 but not on mu.
```

## What Is Not Ruled Out

The remaining selector, if it exists, must be one of:

```text
mu-dependent curvature endomorphism from the non-flat HYM curvature F(mu),
mu-dependent OU weights through lambda_{n,k}^{(Hhat)}(mu),
a discrete admissibility or stability condition selecting a special mu,
a full zeta/heat determinant whose lower-order terms are explicitly mu-dependent.
```

This is a real narrowing: the remaining issue is not generic torsion or a
constant OU floor.  It must involve the `mu`-dependent part of the selected
operator.

## Verdict

```text
mu-independent torsion/OU completion can select mu: no
mu-independent completion gate closed: yes
full mu selection closed: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Mu_Dependent_Curvature_or_OU_Selector_v1
```
