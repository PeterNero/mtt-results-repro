# q79 Degree-Two K3 Fu-Yau Torsion GLSM Base Theorem v1

Date: 2026-07-16

## Exact advance

The q79 worldsheet program now has an explicit smooth K3 representative, not
only an abstract `H^2=2` lattice.  Let

```text
Q2 = x*z - y**2
G3 = -2*x**3 - 2*x**2*z + x*y**2 + x*y*z + 2*x*z**2 - y**3 - 2*y*z**2 - z**3
H4 = -x**4 - 2*x**3*y - x**2*y**2 + 2*x**2*y*z + x**2*z**2 - x*y**3 - 2*x*y**2*z - 2*x*y*z**2 + 2*x*z**3 - y**4 - y**3*z + y*z**3 + 2*z**4
F6 = G3^2 + Q2 H4
```

and define

```text
X_K3: w^2 = F6(x,y,z) in P(1,1,1,3).
```

Exact Groebner checks on the affine chart `z=1`, the line at infinity, and
the remaining projective point show that the branch sextic is smooth.  The K3
also avoids the only ambient weighted-projective orbifold point.

## Incidence GLSM

The determinantal presentation

```text
M = [[w-G3, Q2],
     [H4,   w+G3]]
```

obeys `det(M)=w^2-F6`.  The common-zero locus `Q2=G3=H4=0` is empty, so `M`
has rank one everywhere on the K3 and its projectivized kernel is isomorphic
to the double sextic.

This gives the two-parameter GLSM charge table

```text
field       x  y  z  w  s  t  p1  p2
U(1)_H      1  1  1  3  0  1  -3  -4
U(1)_L      0  0  0  0  1  1  -1  -1
```

with constraint bidegrees `(3,1)` and `(4,1)`.  Both charge sums vanish.  At
the paired `(2,2)` locus, the chiral and Fermi gauge-anomaly matrices cancel
exactly, and gauge invariance of `W=p1 E1+p2 E2` proves `sum E_i J_i=0` for
both gauge factors by the weighted Euler identity.

## The Fu-Yau class is visible in the gauge lattice

In the ambient Chow ring,

```text
H^4=0,
L(L+H)=0,
integral H^3 L = 1/3.
```

Intersecting with the K3 class `(3H+L)(4H+L)` gives

```text
H^2=2,
H.L=2,
L^2=-2.
```

The splitting-conic component is `R_minus=L`, hence

```text
delta = H-L,
H.delta = 0,
delta^2 = -4.
```

This is exactly the primitive minimal nonzero anti-self-dual class in A102.
The active rank-one Fu-Yau pair is `(delta,0)`: the first circle is twisted by
the divisor vector `(1,-1)` in the GLSM gauge basis, while the second marked
shared circle has zero shift.  This retains the topology
`P_delta x S1_shared` rather than replacing it by a two-twisted-circle model.

## q79 arithmetic retained

The same `H^2=2` gives

```text
a=(5,H,0), b=(7,3H,1),
Gram(a,b)=[[2,1],[1,4]], det=7.
```

The imported source-free K3 reference allocation is exactly

```text
c2(V3)+c2(W9)-delta^2 = 9+11+4 = 24,
NS5 charge = 0.
```

No fitted continuous parameter was added.

## What this does not close

This is a real W8 advance, but it is not yet the full q79 heterotic worldsheet.
The following objects remain required:

1. visible and hidden heterotic Fermi charge matrices on this `U(1)^2` GLSM;
2. holomorphic non-pullback bundle `E/J` maps with `c3=+/-6`;
3. torsion-multiplet axial couplings and the local `2x2` anomaly matrix;
4. the differential Bianchi identity after non-pullback circle clutching;
5. the exact IR `(0,2)` SCFT, GSO projection, and seven analytic characters;
6. the strict MTT theorem selecting the shared circle as the untwisted Fu-Yau
   factor.

In particular, the exact integrated identity `9+11+4=24` must not be confused
with the still-missing local GLSM anomaly cancellation matrix.

## Primary sources

- [Degree-two K3 surfaces as double sextics](https://arxiv.org/abs/1808.00351)
- [Lattice-polarized K3 period geometry](https://arxiv.org/abs/alg-geom/9502005)
- [Fu-Yau anomaly solutions](https://arxiv.org/abs/hep-th/0604137)
- [Linear models for flux vacua](https://arxiv.org/abs/hep-th/0611084)
- [Torsion GLSM target-space duality](https://arxiv.org/abs/1107.0714)
