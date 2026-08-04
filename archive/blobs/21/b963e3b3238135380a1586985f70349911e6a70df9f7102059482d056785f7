# MTT Selected q79 PGL3-to-Prym Gerbe Jacobian Execution v1

Status: `MTT_U6_Q79_GERBE_ZERO_REDUCED_TO_SPLITTING_CONIC_RELATIVE_PERIOD_SYSTEM_MARKED_SOURCE_OPEN`

## What A106 changes

A105 correctly found an eight-dimensional local obstruction problem, but its
open packet still made the marked K3, Poincare cocycle, gerbe coordinates and
all 64 Jacobian entries look like separate inputs. They are not. A106 derives
the geometry and the complete equation from a much smaller source object.

It also corrects the global zero condition. A topologically trivial
holomorphic gerbe is zero modulo the integral image in the exponential
sequence. Therefore the exact equation is a period congruence on a fixed
integral branch, not merely eight floating coordinates approximately equal to
zero.

## Splitting-conic K3 theorem

The A102 lattice is

```text
H^2=2, delta^2=-4, H.delta=0,
```

with `H` ample and `delta` primitive. Set

```text
R_+=H+delta,  R_-=H-delta.
```

Then

```text
R_+^2=R_-^2=-2,
H.R_+=H.R_-=2,
R_+.R_-=6.
```

K3 Riemann-Roch gives `chi(O(R_+/-))=1`. Since `H` is ample, `-R_+/-`
cannot be effective, so both roots are effective. Every lattice class has
`H`-degree in `2Z`; hence a degree-two root is generically irreducible. Each
is therefore a smooth rational curve.

The genus-two map is a double cover `pi:S->P2`. The two roots map
birationally to one conic `Q` and are exchanged by the deck involution:

```text
pi^*Q=R_+ + R_-=2H.
```

Consequently every generic marked model has the explicit normal form

```text
w^2=F6,
F6=G3^2+Q2 H4,
R_+={Q2=0,w=+G3},
R_-={Q2=0,w=-G3},
delta=R_+-H.
```

The count is

```text
5 (Q2) + 7 (G3 restricted to Q) + 15 (H4)
- 1 (overall scale) - 8 (PGL3) = 18,
```

exactly the period-domain dimension for a rank-two lattice-polarized K3.
Changing the lift `G3` by `Q2 L1` is absorbed into `H4`.

## Exact analytic-Brauer zero

For a good cover of `C`, choose logarithms

```text
a_ijk=(2 pi i)^-1 log(alpha_ijk|C).
```

A104 proved `DD(alpha|C)=0`. Its integral Cech 3-cocycle is therefore a
coboundary. Subtracting an integral 2-cochain gives an additive cocycle `b`
and

```text
beta_C=[b] in H^2(C,O_C)/image(H^2(C,Z)).
```

After A105's trace removal, the exact criterion is

```text
beta_C=0
iff b_tf=P_tf(e) for some e in H^2(C,Z).
```

The projected integral group is not automatically a discrete lattice. A
small numerical residual or an uncertified nearest-lattice answer cannot
prove this equality.

## Eight explicit residue rows

Let `X=(X0,X1,X2)^T` be the genus-two coordinates and let
`theta(z;tau)` be a basis of `H^0(E,O(3[0]))`. An alignment `A in PGL3`
defines

```text
s_A(X,z)=X^T A theta(z;tau).
```

For a traceless-matrix basis `T_r` of `pgl3`, set

```text
dot_s_r=X^T A T_r theta,
omega_r(A)=Res_C_A[(dot_s_r/s_A) Omega_K3 wedge dz].
```

On `w^2=F6`, one may take `Omega_K3=dx1 wedge dx2/w` on an affine chart.
The eight residues form the trace-free basis of `H^0(K_C)` dual to A105's
`H^2(K)` obstruction space. Thus no independent Prym basis rows are needed.

## Correct 8 by 8 system

Transport an integral basis `e_I`, `I=1,...,92`, of `H^2(C,Z)` by the
Gauss-Manin connection and define

```text
Pi_rI(A)=integral_C_A e_I wedge omega_r(A),
z_r(A)=integral_C_A b_A wedge omega_r(A).
```

On a fixed integral branch `ell in Z^92`, the eight exact equations are

```text
F_r(A,ell)=z_r(A)-sum_I Pi_rI(A) ell_I=0.
```

Their full covariant Jacobian is

```text
J_rs=nabla_s z_r-sum_I ell_I nabla_s Pi_rI.
```

Both terms are required because the integral periods and Hodge basis vary.
An exact `F=0` together with `det(J)!=0` selects an isolated local alignment.

## Source reduction and guardrails

The actual primitive continuous source is now:

```text
18 complex coordinates: one marked splitting-conic K3 period point,
 1 complex coordinate: the elliptic modulus tau,
 1 discrete sign:       delta <-> -delta.
```

The eight alignment coordinates are variables solved by the equations. The
eight gerbe coordinates, 92-column period table and 64 Jacobian entries are
derived outputs, not fitted rows.

The repository has a ready `tau=i` Appell-Humbert theta implementation. It
belongs to the Iwasawa `(2,-4,0)` model and may be used for a diagnostic run,
but no theorem identifies it with the elliptic fiber of this rank-one Fu-Yau
branch. A106 does not cross-promote it. It also preserves A102's warning that
the shared-circle-to-Fu-Yau source map itself remains conditional.

No measured Standard-Model value and no new fitted parameter enters A106.
The gerbe zero, twisted sheaf, inverse Fourier-Mukai bundle, balanced HYM and
differential Bianchi identity remain open.

Next artifact: `MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1`.

## Primary references

- [Brinzanescu, Halanay and Trautmann, Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Caldararu, Derived categories of twisted sheaves on elliptic threefolds](https://arxiv.org/abs/math/0012083)
- [Ferrari Ruffino, Relative Deligne cohomology and Cheeger-Simons characters](https://arxiv.org/abs/1401.0631)
- [Shimada, Z-splitting curves for double plane sextics](https://arxiv.org/abs/0903.3308)
