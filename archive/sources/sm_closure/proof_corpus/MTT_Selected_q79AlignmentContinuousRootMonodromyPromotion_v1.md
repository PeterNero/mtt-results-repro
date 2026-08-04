# MTT Selected q79 Alignment Continuous Root Monodromy Promotion v1

## Result

A127 constructed the selected-alignment genus-two fibration, isolated its 90
simple nodal fibers, fixed an ordered 90-meridian fan, and computed 90
pointwise Picard-Lefschetz candidates. A128 supplies the missing continuous
argument. It certifies six pairwise-disjoint analytic root tubes over every
segment of every selected meridian and therefore promotes all 90 candidate
braids and integral symplectic matrices to actual monodromy actions.

No observed Standard-Model value is used. This closes one finite analytic
layer of the q79 compactification calculation; it does not select the frozen
alignment from primitive MTT data and does not yet decide the integral period
branch.

## Stored trajectories

The A127 worker was upgraded to preserve, for each selected meridian,

```text
w                         sampled base points
roots                     six consistently labelled reciprocal-chart roots
root_radius_uppers        pointwise ACB isolation radii
```

The trajectory hash is carried by the individual monodromy packet and the
batch packet. The regenerated inventory contains 90 trajectories and
1,052,716 sampled points. All paths use the same reciprocal branch coordinate

```text
s = 1/(t-(2+3i)).
```

Thus no chart-conjugation matrix is needed between local actions.

## Selected interval coefficient flow

The selected binary sextic has interval coefficients that are sparse
polynomials in the square-elliptic coordinates `(a,b)`. A128 reduces them
modulo

```text
b^2 = a^3-a
```

and differentiates them along the exact normalized elliptic flow

```text
D = 2 b d/da + (3 a^2-1) d/db.
```

For each base segment, the first three derivatives are evaluated at its
midpoint and the fourth derivative is evaluated on an Arb rectangle enclosing
the full segment. Taylor's theorem then encloses every reciprocal-sextic
coefficient over the entire segment, including the uncertainty inherited from
the selected alignment.

## Continuous Rouché tubes

For a recorded strand with disk center `c`, write the enclosed translated
sextic as

```text
q(u)=q0+q1*u+...+q6*u^6,  u=s-c.
```

A radius `R` is accepted only when the interval inequality

```text
inf |q1| R > sup |q0| + sum_(k=2)^6 sup |qk| R^k
```

is strict. Rouché's theorem then proves that the disk contains exactly one
root for every base point in that segment. The six accepted disks are also
required to be pairwise disjoint. Since the disks are convex and contain both
recorded endpoint balls, the recorded strand and the unique analytic strand
are isotopic inside that disk. Adaptive certificate subdivision is used where
one coefficient box is too broad; no failed segment is omitted.

The completed batch is

```text
selected meridians                         90
continuous root-tube certificates          90
base-path segments certified        1,052,626
minimum relative Rouché margin       2.8947210966454535e-7
minimum pairwise tube separation     1.0135915872645353e-5
```

The unusually dense `selected_057` path is included in full. Its 380,720
segments are certified rather than replaced by a coarser diagnostic.

## Monodromy promotion theorem

For each path, the certified root-tube isotopy identifies the polygonal braid
with the braid of the analytic roots. A separate 80-digit Arb replay certifies
every projected endpoint order, crossing parameter, crossing height, and the
order of simultaneous candidate events. It reproduces every stored word and
exact Birman-Hilden matrix. Across the 90 local paths and two handle paths it
certifies 3,797 crossings; the global lower bounds for projected endpoint
separation, crossing height, and same-segment event ordering are respectively
`1.8736687590666978e-8`, `1.1072490942851253e-5`, and
`3.4243806689188854e-5`.

Exact replay in the common marked basis `(a1,b1,a2,b2)` therefore gives the
actual integral Picard-Lefschetz action. Independently checked for every local
row,

```text
M^T J M = J,
det(M)=1,
rank(M-I)=1,
(M-I)^2=0,
```

and the endpoint root permutation is one transposition. All 90 matrices are
promoted. There are 32 distinct matrices, and the combined image of all
`M-I` has rank four, so the selected vanishing system reaches every direction
of the genus-two fiber `H1`.

## Exact remaining chain

A128 removes the continuous-root-tube qualifier from the selected local
monodromies. The next finite topological layer is now:

1. execute and certify the selected `A` and `B` torus-handle monodromies;
2. verify the ordered punctured-torus surface relation in the same marking;
3. build a primitive rank-92 endpoint `H2` basis from thimbles, handle lifts,
   and the two Leray-edge classes;
4. integrate the same eight selected residue rows over that basis;
5. decide exact integral-period membership of the already certified beta.

The selected handle carriers have already been isolated: their minimum
clearances from the 90 critical balls, elliptic poles, and the three selected
line-chart zeros are all positive. They are computation inputs, not yet
promoted handle monodromies.

Next artifact:
`MTT_Selected_q79SelectedAlignmentHandleMonodromyGlobalRelationAndIntegralH2Basis_v1`.
