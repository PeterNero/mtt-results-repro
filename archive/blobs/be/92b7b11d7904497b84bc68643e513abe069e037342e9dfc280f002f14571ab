# G3D Physical Spectral-Object Cutset

**Date:** 2026-08-03

**Status:** `EXACT_REDUCTION_PHYSICAL_MODULES_AND_SLOPE_BOUNDS_OPEN`

## What G3D Removed

The common q79 HYM chamber is no longer an independent nonlinear search. For
the balanced ray

\[
\omega_t=\sqrt t\,\pi^*\omega_H+t^{-1/2}i\zeta\wedge\bar\zeta,
\]

the q79 lattice fixes the conservative fiber gaps

\[
a_V=2,
\qquad
a_W=\frac23.
\]

After a selected spectral object excludes degree-zero proper subobjects, only
a certified upper bound `M_E` for its `omega_1` subsheaf slopes is needed. The
exact thresholds simplify to

```text
visible rank-3 module:        t_V* = 1 + M_V
hidden direct rank-9 module:  t_W* = 1 + 12 M_W
hidden 3 x rank-3 orbit:      t_W* = 1 + 3 M_W
```

Any rational `common_t` strictly above the applicable two thresholds proves a
nonempty common stable or polystable chamber. It is an existence witness, not
a measured parameter or a claim that this value is the final Fu-Yau metric.

## Visible Construction

The exact upstream support is

\[
C_V\in|9H+3D_0|.
\]

Smooth finite-flat members exist, and inverse BHT of an admissible twisted line
is automatically locally free of rank three. The determinant baseline is
already fixed. A promotable visible object must now supply, from the eta9
source hash:

1. one selected smooth irreducible determinant-zero member `C_V`;
2. a trivialization of the restricted transform gerbe on `C_V`;
3. the twisted line `L_V=L_0 tensor Q`, with the required norm-zero Prym row;
4. the exact pushforward rows
   `j_*Q=12H^2-9 gamma*x` and `j_*(Q^2)=-66H^2D0`;
5. the physical visible Chern, determinant and equivariant-descent certificate;
6. an exact or interval-certified fixed-metric slope bound `M_V`.

The promoted eta9 characteristic-zero factorization helps select the first
three rows, but it still lacks the detecting meridian, period image, Deligne
decision and `U_eta9`.

## Hidden Construction

The physical target is a twisted projective rank-nine `P(3,9)=SU(9)/Z3`
object with its selected Chern and torsion rows. The known support
`3H+3D0` is the support of a degree-three transformed object. It does not by
itself certify physical `W9`.

Two routes remain admissible.

### Route H9

Construct one global alpha-twisted length-nine spectral module or perfect
complex whose generalized BHT/Hori image has the physical rank-nine,
determinant, Chern and projective-group rows. Prove local freeness after the
declared transform, irreducibility or stability, equivariant descent and a
certified `M_W`. The threshold is `1+12 M_W`.

### Route H3x3

Construct three globally holomorphic stable rank-three factors with a unitary
qutrit permutation/multiplier and prove that their projective descent has the
physical `P(3,9)` Chern rows. This is stronger than observing a fiberwise
length-nine qutrit module. The ordinary three-copy orbit recorded in the q79
atlas has the wrong Chern character and is rejected. If the correct equivariant
orbit exists, the threshold improves to `1+3 M_W`, where `M_W` bounds every
factor.

## Computing the Slope Bound

`M_E` need not come from an HYM solution. Once a module is explicit:

1. choose a source-defined smooth Hermitian reference metric on its finite-flat
   pushforward or transformed complex;
2. compute the Chern curvature and contract it with `omega_1`;
3. use the Chern-Weil subsheaf projection inequality, dropping the nonpositive
   second-fundamental-form term;
4. enclose the largest eigenvalue over a certified finite coordinate cover;
5. round the resulting upper interval endpoint outward to a rational `M_E`.

An exact Harder-Narasimhan calculation may replace this curvature enclosure.
The certificate must name the method, source artifact and interval or exact
proof. Choosing a convenient uncaptured number is not accepted.

## Physical Packet Exit

Submit one packet conforming to
`state/ust_g3d_common_gauduchon_chamber.schema.json`. It must contain exactly
one visible rank-three row and one hidden rank-nine row, the same source hash,
physical topology matches, canonical gaps, certified slope bounds and one
strict rational `common_t`. Validate it with:

```powershell
python verify_ust_g3d_common_gauduchon_chamber.py --candidate <packet>
```

Only after this passes should the endpoint be promoted through G3A and used to
evaluate the already fixed six-row physical operator `K`.

## Frozen Exclusions

- Do not substitute the aggregate rank-12 monad for `V3 direct-sum W9`.
- Do not substitute the degree-three hidden transform for physical `W9`.
- Do not accept an ordinary three-copy orbit without the physical Chern rows.
- Do not solve a second free-standing HYM PDE after a G3D packet passes.
- Do not infer a slope bound from rank, index or Chern data alone.
- Do not use observed particle values to choose the module, bound or `t`.
