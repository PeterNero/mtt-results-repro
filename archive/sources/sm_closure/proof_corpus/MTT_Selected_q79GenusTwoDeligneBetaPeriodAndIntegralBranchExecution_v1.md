# MTT Selected q79 Genus-Two Deligne Beta Period and Integral Branch Execution v1

Status: `MTT_U6_Q79_NORMALIZED_DELIGNE_TRANSGRESSION_FUNCTIONAL_AND_FLOATING_BETA_VECTOR_CLOSED_INTEGRAL_BRANCH_OPEN`

## What A121 closes

A120 constructed the exact divisor normal function and its complete integral
affine cocycle, but correctly stopped before identifying affine monodromy with
the analytic Brauer coordinate. A121 supplies that missing map. It derives the
normalized Deligne/Leray transgression on the frozen torus marking and emits
the resulting eight-component floating representative.

It does not infer integral-period membership from a nearest-lattice search.

## The circle source is already marked

The A110 Fu-Yau transitions are

```text
t_ij=(2 pi i)^-1 Log(g_ij) mod (Z+i Z),
```

and their triple sums enter the normalized Poincare gerbe as

```text
alpha_ijk(e_hat)=chi_ehat(n_ijk,0).
```

Thus the first component is not an unfixed exchange convention. In the A114
square-torus marking, let `A` be translation by `1`, `B` translation by `i`,
and let `u_A` be the integral one-form with periods

```text
integral_A u_A=1,  integral_B u_A=0.
```

The selected source is therefore

```text
DD(alpha)=delta cup u_A.
```

This agrees with the standard torus T-duality rule that the leading flux is
the sum of the dual fiber generators tensored with the corresponding Chern
classes.

## Deligne-Leray transgression theorem

Let `nu(w)` be A120's Abel-Jacobi lift of

```text
D_delta=P_1+P_2-infinity_+-infinity_-
```

on the genus-two fiber. Write each A111 holomorphic two-form as a fiber form
times the base differential. Pairing its fiber factor with `nu` gives a
scalar one-form `eta_r` on the cut base. A120's accumulated relative periods
are exactly

```text
R_A,r=integral_A eta_r,
R_B,r=integral_B eta_r.
```

The Deligne cup/transgression paired with the `r`th Serre-dual form is

```text
z_r=integral_E u_A wedge eta_r.
```

On the oriented torus `A dot B=+1`, the bilinear relation gives

```text
z_r
 = (integral_A u_A)(integral_B eta_r)
   -(integral_B u_A)(integral_A eta_r)
 = R_B,r.
```

This equality is an equality in the period quotient, not an assertion that
one chosen chain lift is absolute. A change of Abel-Jacobi lift changes
`eta_r` by an integral fiber-period one-form. A change of local puncture
correction adds an integral thimble period. A120 proves that every local
singularity class vanishes and that the corrected polygon edges satisfy the
exact affine surface relation. All such changes therefore lie in the A119
integral `H2` period image. Consequently

```text
beta_C = [R_B] in C^8 / Pi(H^2(C,Z)).
```

An overall orientation reversal sends both sides to their negatives and does
not alter the zero criterion.

## Executed beta representative

In the A119 form order

```text
(E12,E13,E21,E23,E31,E32,H1,H2),
```

the production representative is

```text
(-0.7932409419622393 +1.5928867303543435 i,
 -0.6000973339293562 +1.0244433985443602 i,
  0.7464812276454289 +0.0107095445201776 i,
 -1.0921895073587358 -0.0641526034609616 i,
 -1.3259268714584889 -1.1599787825265824 i,
  2.2412996866905490 +1.9250391357116778 i,
  1.4162084844866227 -1.7143562803874568 i,
 -1.6767219668098750 -0.4409389868330373 i).
```

The independent tighter-tolerance run changes no component by more than

```text
5.922e-10.
```

Both A119 and A120 use

```text
da/(2b)=period_length dw,
```

so the beta representative and the `8x92` period matrix have the same common
normalization. This is reproducible floating convergence, not an interval
enclosure.

## The remaining exact decision

The analytic gerbe is zero exactly when

```text
z_8=Pi_(8x92) ell,  ell in Z^92.
```

The projection of a rank-92 integral group into 16 real period coordinates
is not assumed discrete. Therefore none of the following is accepted as a
proof:

- a small floating residual;
- a nearest-lattice vector;
- the visibly nonzero displayed representative;
- the nontrivial A120 affine cocycle by itself.

Lawful exits are an exact Cech trivializing cochain, exact algebraic/CM period
identities, or validated period enclosures together with a branch-height or
separation theorem. Only after a zero branch is fixed may the same source be
differentiated in the eight `PGL3` directions and its covariant Jacobian be
certified.

No observed Standard-Model value, fitted target, or new continuous source
parameter enters A121.

Next artifact:
`MTT_Selected_q79GenusTwoIntegralBranchOrPGL3GerbeNoGoExecution_v1`.

## Primary references

- Dove and Schick, *A new approach to topological T-duality for principal torus bundles*, arXiv:2104.05984.
- Bunke, Rumpf and Schick, *The topology of T-duality for T-bundles*, arXiv:math/0501487.
- Ferrari Ruffino, *Relative Deligne cohomology and Cheeger-Simons characters*, arXiv:1401.0631.
- Li, Lian and Yau, *Picard-Fuchs Equations for Relative Periods and Abel-Jacobi Map for Calabi-Yau Hypersurfaces*, arXiv:0910.4215.
