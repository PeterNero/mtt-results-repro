# MTT Selected q79 Explicit-Model Relative-Deligne Gerbe Zero or No-Go Execution v1

Status: `MTT_U6_Q79_EXPLICIT_SMOOTH_SPECTRAL_SURFACE_AND_TORSOR_POINCARE_CECH_FORMULA_CLOSED_BETA_PERIOD_OPEN`

## New exact spectral carrier

Use the A109 K3 and the square elliptic cubic

```text
E_i: b^2 c=a^3-a c^2,
Delta=64,
j=1728.
```

The coordinates `[a:b:c]` form the degree-three basis. At the trial identity
alignment, define

```text
C: x*a+y*b+z*c=0 in K3 x E_i.
```

This is an exact constructive surface, not a selected alignment.

## Spectral-surface smoothness theorem

If `C` were singular, the Lagrange equation for its bilinear section would
give `0=2 lambda w`. The case `w!=0` forces the projective elliptic vector to
vanish, so every singular point must have `w=0`. Euler's identities reduce the
remaining system to

```text
F6(X)=0,
E_i(e)=0,
e parallel grad F6(X),
X parallel grad E_i(e).
```

Exact Groebner reduction over `QQ` gives basis `[1]` on all nine product
charts. Therefore `C` is smooth. Its A104 invariants are consequently
`K_C^2=18`, `c2=90`, `p_g=9`, and `h11=74`.

## Explicit O(delta) transitions

Write `delta=R_plus-H_x`. Cover a neighborhood of `R_plus` by

```text
R1: w+G3 != 0, local equation Q2,
R2: H4 != 0,   local equation w-G3,
```

and use `R0=S-R_plus` with local equation one. The A109 no-triple theorem
proves these cover `R_plus`, while

```text
(w-G3)/Q2=H4/(w+G3)
```

on the overlap. Refine with the three projective charts for `H_x`. This gives
nine local divisor equations `d_i` and exact transitions

```text
g_ij=d_j/d_i.
```

The generated table passes all 72 ordered inverse checks and all 729 triple
cocycle checks exactly.

## Fu-Yau torsor and Poincare gerbe

On a simply connected good-cover refinement choose `Log(g_ij)` and set

```text
t_ij=(2 pi i)^-1 Log(g_ij) mod (Z+tau Z).
```

The triple sums `n_ijk` are the integer Cech cocycle representing `delta`, so
these are the transitions of the unique elliptic torsor with Chern pair
`(delta,0)`. Existence uses that `delta` is algebraic of type `(1,1)`;
uniqueness uses `H^1(K3,O)=0`.

The zero-section-normalized Poincare bundles differ on double overlaps by the
degree-zero line bundle of `t_ij`. Their scalar triple cocycle is

```text
alpha_ijk(e_hat)=chi_ehat(n_ijk,0),
alpha_ijk(0)=1.
```

This is the missing explicit Cech formula. It reproduces
`DD(alpha)=delta cup u`, whose restriction to `C` is already integrally zero.

## Remaining analytic calculation

A110 does not confuse a cocycle formula with its analytic-Brauer value. The
remaining work is now:

1. refine the nine patches to a good cover of `C` and fix logarithm branches;
2. evaluate `n_ijk`, `alpha_ijk|C`, and the additive cocycle `b`;
3. compute the eight residue pairings `z_r` and the `8x92` integral period
   matrix;
4. find `ell in Z^92` with `z=Pi ell`, or prove exact nonmembership;
5. certify the covariant `8x8` alignment Jacobian at any zero.

The identity alignment and `tau=i` are constructive trial data. They are not
promoted as MTT-selected values, and zero strict source moduli are removed.

Next artifact: `MTT_Selected_q79ExplicitSpectralCechBetaPeriodEvaluation_v1`.
