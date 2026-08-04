# MTT Selected q79 Genus-Two Distinguished Cut System and Global Surface Relation v1

## Claim class

This is a strict computational theorem about the integral first-homology
Gauss-Manin representation of the A111 q79 genus-two Lefschetz fibration. It
does not select the A109 marked K3, evaluate the eight Prym period rows, choose
an integral Deligne branch, prove the gerbe class zero, or close U6/strong CP.

## Inputs already promoted

The theorem consumes only previously audited data:

1. A112 isolates all 90 critical values and nodal fibers.
2. A113 fixes the regular base fiber at `w=(1+i)/4`, the genus-two homology
   marking `(a1,b1,a2,b2)`, and 90 positive local meridians.
3. A114 promotes the two torus-handle actions `A` and `B` in `Sp(4,Z)`.
4. A115 promotes all 90 local Picard-Lefschetz actions by continuous root tubes
   and interval-certified braid replay.

No A115 matrix is merely reordered here. New meridians in one distinguished
cut system are transported and certified independently.

## The cut-square fan

Cut the normalized base torus `C/(Z+iZ)` along the promoted handle carriers

```text
A: w(s)=(1+i)/4+s,
B: w(s)=(1+i)/4+i*s,
```

and use the square

```text
Q=[1/4,5/4] x [1/4,5/4].
```

The base point is the lower-left corner. A113's handle clearances imply that
no critical disk meets the boundary. Every critical disk has one canonical
lift in the open square. Join the base corner to each canonical center by a
straight radial arc and order the arcs by strictly increasing polar angle from
the positive `A` edge toward the positive `B` edge.

The constructor chooses a separate positive counterclockwise meridian radius
for every endpoint. Direct interval-margin guards give:

```text
minimum adjacent angle gap                    1.1352541417558593e-4
minimum direction determinant                 6.0043657733187951e-6
minimum arc-to-other-circle clearance         7.7488788260859795e-6
minimum segment-to-critical-disk clearance    9.6860985370269708e-6
minimum circle-to-critical-disk clearance     1.9372196909409908e-6
minimum pairwise circle clearance             5.8185915164763657e-3
minimum segment-to-elliptic-infinity clearance 6.5210853743846733e-2
```

All margins are strictly positive. Therefore the 90 radial arc interiors are
pairwise disjoint, meet only at the base point, remain inside the cut square,
and each terminal circle encloses exactly one certified critical disk. This is
an ordered distinguished cut system, not a root-id ordering proxy.

## Independent distinguished transport

For each of the 90 new meridians, FLINT/Arb isolates the six roots of the
hyperelliptic branch polynomial at every saved path point. The primary branch
chart is `s_0=1/t`; the already certified chart `s_minus1=1/(t+1)` is used on
the two paths where it is numerically preferable. The A115 chart-transition
matrices transport both charts to the same A114 homology marking.

The adaptive transport saves 229,526 points. A fourth-order elliptic-flow
Taylor enclosure plus an Arb Rouche test proves six pairwise-disjoint
continuous root tubes over all 229,436 path segments. An independent 80-digit
interval projection then certifies:

```text
distinguished meridians promoted              90/90
interval-certified braid crossings            3,476
segments containing multiple crossing events  135
minimum crossing-height lower bound            1.3650850334968336e-3
minimum projected endpoint separation          2.2616778351335668e-7
minimum same-segment event-parameter gap        5.6385191667263478e-3
vanishing-cycle span rank                       4
```

Every endpoint permutation is a transposition. Every replayed matrix is an
integral determinant-one symplectic rank-one unipotent matrix and has the
positive Picard-Lefschetz form

```text
M_j = I + v_j v_j^T J
```

for a primitive integral vanishing cycle `v_j`, up to sign. The sign convention
is the one measured by the counterclockwise path and frozen braid action; no
orientation is inferred from a desired global product.

## Global surface relation

The code uses a left action, so path concatenation reverses matrix order:

```text
M(gamma then delta)=M(delta) M(gamma).
```

The positively oriented cut-square boundary is the path

```text
A B A^-1 B^-1.
```

The radial fan gives the topological path relation

```text
A B A^-1 B^-1 = m_1 m_2 ... m_90.
```

Consequently its matrix form must be

```text
M_90 ... M_2 M_1 = B^-1 A^-1 B A.
```

Both sides are computed independently from the promoted factors. They agree
entry by entry:

```text
[[ 5,  4,  2,  6],
 [-1,  1,  3,  5],
 [-6, -4, -1, -5],
 [ 1,  2,  3,  6]].
```

Thus the 90 local factors and two handle actions define one globally
consistent integral `H_1` Gauss-Manin representation of the 90-punctured
torus. This is the representation needed to transport genus-two periods.

The standard surface presentation with commutators and puncture loops is used
in the literature on surface bundles and Lefschetz fibrations; see Endo,
Korkmaz, Kotschick, Ozbagci and Stipsicz,
[Commutators, Lefschetz fibrations and the signatures of surface bundles](https://www.maths.ed.ac.uk/~v1ranick/papers/ekkos.pdf).
The dependence of a monodromy factorization on the geometric basis, and its
change by Hurwitz moves, is reviewed by Degtyarev and Salepci,
[Products of pairs of Dehn twists and maximal real Lefschetz fibrations](https://arxiv.org/abs/1110.4093).

## Exact scope

Closed here:

- one certified 90-meridian distinguished cut system;
- 90 independently promoted distinguished positive PL factors;
- two previously promoted handle factors in the same marking;
- the exact global integral `Sp(4,Z)` surface relation;
- the global integral `H_1` Gauss-Manin representation required for period
  transport.

Not claimed here:

- faithfulness of the `Sp(4,Z)` representation on the full genus-two mapping
  class group;
- any numerical entry of the `8x92` Prym period table;
- an integral `Z^92` period branch;
- a selected gerbe zero or no-go;
- selection of the marked K3, the inverse Fourier-Mukai bundle, balanced HYM,
  differential Bianchi closure, or full U6/strong-CP closure.

## Next artifact

`MTT_Selected_q79GenusTwoEightPrymPeriodRowsAndIntegralBranch_v1` must transport
the eight A111 residue/normal-function rows through this now-global local
system, emit certified period values, and test the declared integral branch.
