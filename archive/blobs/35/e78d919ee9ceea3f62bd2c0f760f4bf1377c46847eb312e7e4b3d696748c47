# MTT Selected q79 Genus-Two Normal Function Beta and Integral Branch Execution v1

Status: `MTT_U6_Q79_EXACT_MUMFORD_SOURCE_AND_COMPLETE_SELECTED_INTEGRAL_AFFINE_NORMAL_FUNCTION_COCYCLE_CLOSED_BETA_PERIOD_BRANCH_OPEN`

## Exact algebraic source

On the A110/A111 trial carrier, write

```text
C_(a,b): u^2=f_(a,b)(t)=g_(a,b)(t)^2+q_(a,b)(t) h_(a,b)(t),
q_(a,b)(t)=-(t^2+b t+a),
b^2=a^3-a.
```

The degree-zero divisor normal function is

```text
D_delta=P_1+P_2-P_infinity_plus-P_infinity_minus,
P_i=(r_i,g_(a,b)(r_i)),
r_i^2+b r_i+a=0.
```

It now has an exact balanced even-sextic Mumford source. Let

```text
Q=t^2+b t+a,
V=g_(a,b) mod Q,  deg(V)<2.
```

Exact Groebner reduction in the ideal

```text
(Q, b^2-a^3+a)
```

gives

```text
g-V = 0 mod Q,
f-V^2 = 0 mod (Q,b^2-a^3+a).
```

Thus `(Q,V)` is not a fitted Abel-Jacobi coordinate: it is the exact algebraic
section whose two finite points are the selected `u=+g` intersections. The
two marked infinity points fix the degree-zero convention.

## Inhomogeneous Gauss-Manin equation

For the five affine de Rham forms

```text
omega_k=t^k dt/u, k=0,...,4,
```

the same reduction engine used in A118/A119 computes

```text
partial_w omega_k=d(R_k/u)+sum_j A_kj omega_j.
```

For a moving chain with boundary `D_delta`, its Abel-Jacobi lift `nu` obeys

```text
d nu_k/dw
 = sum_j A_kj nu_j
 + sum_(Q(r)=0) [R_k(r)/g(r)+r^k (dr/dw)/g(r)].
```

The two infinity contributions to the exact term cancel because both infinity
sheets occur with coefficient minus one. This also regularizes the affine
`k=2,3,4` entries. The physical coordinates are `nu_0,nu_1`.

An explicit base lift is constructed by cancelling common opposite-sheet
tails at one outer point and inserting one branch-point winding to reach
`u=+g` at both Q-roots. Independent production and tight runs select the
handle translations

```text
n_A=( 2,-2,3,-5),
n_B=( 1,-1,0, 0)
```

in the frozen `(a1,b1,a2,b2)` basis. They also emit the sixteen floating
relative periods obtained by integrating the eight A111 residue rows along
the A and B handle paths.

## All 90 local translations

Eighty-eight distinguished meridians are continued directly. Every rounded
translation is an integral multiple of the already certified
Picard-Lefschetz vanishing vector:

```text
n_i=m_i v_i.
```

The maximum coordinate distance from the selected integer vector is below
`2.7e-6`. Meridians 43 and 45 lie next to an elliptic-uniformization pole;
direct affine continuation there is ill-conditioned and is not accepted.

A119 independently selected the physical central lifts

```text
A_phys=+A_braid,
B_phys=-B_braid.
```

For affine pairs, use

```text
(M_2,n_2) o (M_1,n_1)=(M_2 M_1, M_2 n_1+n_2).
```

The exact surface word is

```text
A B A^-1 B^-1 = m_1 ... m_90.
```

Its handle side has translation `(7,6,-4,7)`. Substituting the 88 direct
rows on the meridian side gives four exact integer equations with the unique
solution

```text
m_43=1,
m_45=0.
```

After substitution, both the linear matrix and translation parts agree
exactly. The multiplier census is

```text
-1: 1 row,
 0: 35 rows,
 1: 42 rows,
 2: 11 rows,
 3: 1 row.
```

## Cohomological meaning

Every local translation lies in `image(M_i-I)`. Therefore the normal function
has zero local singularity class at all 90 nodal fibers and extends as an
admissible algebraic normal function.

The full 92-generator affine system is not a common coboundary: the exact
linear system

```text
n_gamma=(M_gamma-I)c
```

has no solution even over the rationals. This is not a failure. It shows that
the normal function carries the genuine global integral Leray class of the
nontrivial splitting divisor rather than being an accidentally constant
Jacobian section.

## What remains open

This artifact closes the previously unspecified normal-function source and
its complete affine monodromy. It does not identify affine monodromy with the
analytic Deligne coordinate.

The remaining map is now precise:

```text
complete affine normal-function cocycle
  -> normalized Poincare/Deligne pairing functional
  -> z_8
  -> test z_8=Pi_(8x92) ell, ell in Z^92.
```

Global cocycle nontriviality alone does not prove `beta_C!=0`, and local
admissibility alone does not prove `beta_C=0`. An exact Deligne pairing or a
rigorously separated period calculation is still required. No measured
Standard-Model value, fitted observable, or new continuous source parameter
is used.

Next artifact:
`MTT_Selected_q79GenusTwoDeligneBetaPeriodAndIntegralBranchExecution_v1`.

## Primary computational references

- Li, Lian and Yau, *Picard-Fuchs Equations for Relative Periods and Abel-Jacobi Map for Calabi-Yau Hypersurfaces*, arXiv:0910.4215.
- Laporte and Walcher, *Monodromy of an Inhomogeneous Picard-Fuchs Equation*, arXiv:1206.1787.
- Molin and Neurohr, *Computing period matrices and the Abel-Jacobi map of superelliptic curves*, arXiv:1707.07249.
- Brinzanescu, Halanay and Trautmann, *Vector bundles on non-Kahler elliptic principal bundles*, arXiv:1008.3365.
