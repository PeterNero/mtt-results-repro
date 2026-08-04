# q79 Global Fitting Descent and Spectral Divisor Match Theorem v1

**Date:** 2026-08-03

**Status:** `GLOBAL_INTRINSIC_FITTING_SHEAF_DESCENT_AND_LOCAL_DETERMINANT_TO_GLOBAL_3H_PLUS_3D0_MATCH_CLOSED_EXACT_HIDDEN_P39_TOPOLOGICAL_ENDPOINT_CLOSED_LITERAL_OVERLAPS_HYM_AND_FINITE_INTERTWINER_OPEN`

**Executable packet:** `q79_global_fitting_descent_and_spectral_divisor_match.packet.json`

**Builder:** `build_q79_global_fitting_descent_and_spectral_divisor_match.py`

**Independent verifier:** `verify_q79_global_fitting_descent_and_spectral_divisor_match.py`

## 1. Result

Let

```text
S_HS in D^b(J,alpha)
```

be the already constructed global alpha-twisted Hartshorne-Serre transform.
Its local resolved differential is

```text
M_j=[[A_j,r I_3],[-t I_3,0]].
```

The preceding local theorem computed

```text
Fitt_0(coker M_j)=((r t)^3),
Fitt_1(coker M_j)=((r t)^2),
Fitt_2(coker M_j)=(r t),
Fitt_3(coker M_j)=(a,r,t),
Fitt_4(coker M_j)=R.
```

These ideals are not chart-dependent decorations. Each cohomology sheaf of
an alpha-twisted perfect complex has canonical ordinary Fitting ideal sheaves.
On an overlap, tensoring a local twisted module by the transition line is
locally tensoring by a free rank-one module. Fitting ideals are invariant
under module isomorphism, invertible row and column changes, stabilization,
and tensoring by such a line. The local ideals therefore glue even though the
module itself is alpha-twisted.

This closes intrinsic global Fitting descent. It does not emit literal BHT
overlap matrices or chain homotopies.

## 2. Exact local-to-global divisor match

For `j=0`, the matrix is equivalent to

```text
[[a,r],[-t,0]] direct-sum [[1,r],[-t,0]] direct-sum [[1,r],[-t,0]],
```

so

```text
det(M_0)=(r t)^3.
```

The source geometry identifies `r=0` with the Hartshorne-Serre plane-section
divisor of class `H`, while `t=0` is the Jacobian zero section `D0`. Hence the
zeroth Fitting divisor is

```text
3(H+D0)=3H+3D0.
```

This agrees exactly with two independent global calculations:

```text
virtual codimension-one class of S_HS = 3H+3D0,
det(S_HS)=O_J(3H+3D0).
```

Thus the resolved local cone is compatible with the global BHT object at the
determinant and support-class tier. This is stronger than the former
fiber-length coincidence and introduces no fitted parameter.

The reduced support is `H union D0`. The deepest rank-two germ is
`(a,r,t)`. The selected degree-two section `a` has the two distinct zeros
`(u,W)=(0,+3)` and `(0,-3)`, so this germ cuts a length-two reduced locus on
`H intersect D0` in the selected source chart.

## 3. Endpoint reclassification

The downstream two-circle/B-field transport already closes an actual smooth
determinant-one `P(3,9)` representative with the selected hidden topological
rows and the lens-selected zero torsion lift. Therefore the hidden rank-nine
endpoint is not wholly open.

Precisely:

```text
hidden W9 smooth-projective topological endpoint: CLOSED,
hidden W9 holomorphic locally-free/HYM promotion: OPEN,
common visible-hidden Gauduchon polystability: OPEN,
separate exact Chern-Weil split rows: OPTIONAL SUFFICIENT ROUTE,
basic total Chern-Weil representative or positive-metric theorem: OPEN,
literal BHT overlap matrices and homotopies: OPEN,
continuum-to-finite physical intertwiner: OPEN.
```

The visible `V3` construction is a separate source branch and is not produced
by this hidden Hartshorne-Serre cone.

## 4. What changed at the frontier

The former target bundled three different questions. They now separate as:

1. categorical global twisted object: closed by the BHT equivalence;
2. intrinsic global Fitting sheaves and their leading divisor: closed here;
3. literal overlap-chain execution: still open as a stronger certificate;
4. hidden topological endpoint: already closed downstream;
5. analytic HYM and finite physical transfer: still open and physically
   decisive.

The best next physical object is the already named selected holomorphic
nonpullback `V3/W9` worldsheet source. The finite harmonic-mode intertwiner is
strictly downstream. A literal good-cover chain atlas remains useful for
connection and holonomy calculations but is no longer required merely to
prove that the Fitting ideal sheaves exist.

## 5. Guardrails

This theorem does not claim:

- literal overlap matrices from symbolic `G_ij` labels;
- trivialization of the gerbe `alpha`;
- purity or WIT1 of `S_HS`;
- a balanced HYM connection;
- identification of the hidden source with the visible `V3` branch;
- a finite `27 x 27` physical mass matrix or Standard Model prediction;
- ultraviolet-complete quantum gravity.

## 6. Reproduction

```powershell
python ./build_q79_global_fitting_descent_and_spectral_divisor_match.py
python ./verify_q79_global_fitting_descent_and_spectral_divisor_match.py
```
