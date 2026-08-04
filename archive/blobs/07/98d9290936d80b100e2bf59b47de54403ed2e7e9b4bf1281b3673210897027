# MTT Selected q79 Splitting-Conic K3 Period Selector or Exact Gerbe Execution v1

Status: `MTT_U6_Q79_FIXED_SECTOR_RECONCILED_PERIOD_SCHUR_AND_JOINT_GERBE_SYSTEM_CLOSED_NUMERIC_SOURCE_OPEN`

## Result

A108 does not reuse the old word *selection* as a substitute for the missing
K3 calculation. It proves the exact reduction that the current q79 branch
needs and corrects the scope of the older Strominger fixed-point paper.

The result is:

```text
old theorem: conditional local field selection inside fixed (X,J,E,topology),
new target: 36-real K3-period stationarity plus 16-real gerbe zero,
conditional tau=i system: 52 equations in 52 real unknowns.
```

## Fixed-sector theorem: exact scope

The printed configuration space first fixes a compact complex threefold `X`,
its complex structure `J`, a holomorphic bundle `E`, and the topological
sector. It then varies only `g,Phi,B,A`. Therefore its Hessian has no
Kodaira-Spencer direction and cannot select a point of the
18-complex-dimensional marked K3 period domain.

This agrees with the independent q79 fixed-sector reduction and with the
2026-07-11 corpus revision ledger: the old result is a conditional fixed-point
correspondence, not a global compactification selector.

## Rigor corrections needed before using the field block

The OU term is printed as

```text
T_OU=sum_a delta_a/(2 gamma_a),  gamma_a=kappa_a lambda_a-L.
```

If `lambda_a` varies, then

```text
dT_OU=-sum_a delta_a kappa_a d(lambda_a)/(2 gamma_a^2),
d2T_OU=sum_a delta_a kappa_a^2 d(lambda_a)^2/gamma_a^3
       -sum_a delta_a kappa_a d2(lambda_a)/(2 gamma_a^2).
```

The second variation is not automatically nonnegative. If `lambda_a` is held
fixed, both variations vanish and the term cannot lift moduli. The printed
claims that it is constant and that it lifts moduli therefore require a new,
explicit variation rule and a sign proof.

The Fu-Yau metric is also printed as `epsilon^(-2)g_T2+g_K3`. Its fiber
eigenvalues scale as `epsilon^2`, so they approach zero, not a uniform positive
constant. A genuinely small fiber uses `epsilon^2 g_T2`, or an independent
twist-induced gap must be proved.

Finally, block ellipticity of the principal symbol does not by itself prove a
positive full Hessian after lower-order couplings and constraints. A108 keeps
the old field result only as the explicit conditional package `C_Xi_fixed`:
a typed MTT-to-field map, a `C2` functional, Lyapunov compatibility, and a
boundedly invertible gauge-quotiented field Hessian `H_uu`.

## Conditional K3-period Schur theorem

Let `p` be 18 complex, hence 36 real, coordinates on the lattice-polarized K3
period domain, and let `u` denote the gauge-fixed Strominger fields. Extend the
functional to `Xi_ext(p,u)` and solve

```text
D_u Xi_ext(p,u_*(p))=0.
```

When `H_uu` is invertible, the implicit-function theorem gives

```text
D_p u_*=-H_uu^(-1) H_up,
W(p)=Xi_ext(p,u_*(p)),
H_eff=H_pp-H_pu H_uu^(-1) H_up.
```

Thus old fixed-field positivity is useful, but only as the block eliminated by
the Schur complement. It does not select `p`. The actual selector requires

```text
D_p W=0,
H_eff positive definite on all 36 real period directions.
```

An `18x18` Hermitian block is insufficient unless a separate complex-linear
reduction proves equivalence to the full real Hessian. A penalty centered at an
unsourced `p0` is also forbidden because it would hide 18 complex source knobs.

## Joint period-gerbe execution

Under the still-conditional Z4 Chern-orbit bridge, `tau=i`. Combine the period
equations with A106:

```text
G(p)=D_p W(p)=0                                      (36 real rows),
F_r(A,p,ell)=z_r(A,p)-sum_I Pi_rI(A,p) ell_I=0       (8 complex = 16 real rows),
ell in Z^92 fixed on one exact branch.
```

The unknowns are `p` (36 real) and `A in PGL3` (16 real): exactly 52. If `W`
is independent of `A`, the real Jacobian is block triangular. When `D_A F` is
complex-linear,

```text
det J_joint=det(H_eff) |det_C(D_A F)|^2.
```

If antiholomorphic derivatives occur, the correct test is instead the
determinant of the full `16x16` realification of `D_A F`; A108 does not assume
complex linearity for free.

This ties the new selector directly to the already-computed covariant gerbe
Jacobian. If `tau` is not selected, two more real unknowns and two same-source
elliptic equations are required.

## What is now closed, and what is not

Closed:

1. the exact fixed-sector/global-selection distinction;
2. the OU and fiber-gap correction conditions;
3. the K3-period Schur-complement theorem;
4. the correct 36-real dimension guard;
5. the square 52-real period-plus-gerbe system and determinant criterion.

Still open:

1. the seven actual same-source period derivative fields;
2. one selected stationary marked K3 point with positive `H_eff`;
3. an exact integral branch `ell` and gerbe zero at that point;
4. the downstream spectral sheaf, inverse Fourier-Mukai bundle, balanced HYM
   and same-branch Bianchi execution.

The alternative is constructive: insert explicit smooth coefficients
`Q2,G3,H4`, execute A106 exactly, and obtain an existence/no-go certificate.
That route tests the compactification but does not by itself prove unique MTT
vacuum selection.

No observed value and no fitted continuous parameter enters A108.

Next artifact: `MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1`.

## Primary references

- [de la Ossa and Svanes, Holomorphic Bundles and the Moduli Space of N=1 Supersymmetric Heterotic Compactifications](https://arxiv.org/abs/1402.1725)
- [Anderson, Gray and Sharpe, Algebroids, Heterotic Moduli Spaces and the Strominger System](https://arxiv.org/abs/1402.1532)
- [de Lazari, Lotay, Sa Earp and Svanes, Local descriptions of the heterotic SU(3) moduli space](https://arxiv.org/abs/2409.04382)
