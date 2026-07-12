# Iwasawa Monad Map Data Gate for Three-Family Slots

## Purpose

This note carries the Iwasawa zero-mode program one step beyond the failed
literal Dolbeault extraction.  The previous audit tested the printed
connection

```text
barpartial_E = barpartial + A^(0,1)
```

and found that the literal matrix is not integrable, while the minimal
one-index diagnostic repair is integrable but has invariant h1 = 2 rather than
three.  Therefore the proof cannot use the printed 3x3 connection to fill the
three-family zero-mode slots.

The remaining source route is the monad route.  This note records exactly what
the monad route must supply before the Standard Model matrices can be computed.

## Source Monad

The Iwasawa flux source defines a two-step monad

```text
0 -> K1 -> direct_sum_i L_i -> K2 -> 0,
E = ker(g) / im(f).
```

The line-bundle Chern labels are

```text
L1 = -2 a + 0 b + 1 c
L2 = -1 a + 1 b - 1 c
L3 =  1 a - 1 b + 0 c
L4 =  1 a + 0 b - 1 c
L5 =  2 a + 1 b + 1 c
K1 =  1 a + 0 b + 0 c
K2 =  0 a + 1 b + 0 c
```

The Chern-character calculation is consistent at the topological level:

```text
c1(E) = 0,
c2(E) = 0,
int_X c3(E) = 6.
```

This is enough to support a net-chirality/index statement.  It is not enough
to construct the actual cohomology representatives, kinetic metric, projectors,
Green operators, or Yukawa matrices.

## Typed Map Check

In a monad, the map entries are not bare numbers unless the relevant Hom line
bundle is trivial.  The components have types

```text
f_i in H^0(X, L_i tensor K1^{-1}),
g_i in H^0(X, K2 tensor L_i^{-1}).
```

Thus scalar constant entries would be globally typed only when the corresponding
first Chern difference is zero.

For the source data:

```text
f_1: c1(L1 tensor K1^{-1}) = (-3,  0,  1)
f_2: c1(L2 tensor K1^{-1}) = (-2,  1, -1)
f_3: c1(L3 tensor K1^{-1}) = ( 0, -1,  0)
f_4: c1(L4 tensor K1^{-1}) = ( 0,  0, -1)
f_5: c1(L5 tensor K1^{-1}) = ( 1,  1,  1)

g_1: c1(K2 tensor L1^{-1}) = ( 2,  1, -1)
g_2: c1(K2 tensor L2^{-1}) = ( 1,  0,  1)
g_3: c1(K2 tensor L3^{-1}) = (-1,  2,  0)
g_4: c1(K2 tensor L4^{-1}) = (-1,  1,  1)
g_5: c1(K2 tensor L5^{-1}) = (-2,  0, -1)
```

None of these classes is zero.  Therefore the phrase "constant matrices in the
left-invariant frame" cannot, by itself, mean nonzero scalar entries between
the displayed global line bundles.  Either:

1. the entries are actually specified global holomorphic sections of the above
   Hom line bundles;
2. a local frame/transition-function convention is being suppressed; or
3. the monad data need correction.

In all three cases, the proof needs the actual typed sections, not just the
Chern labels.

## Consequence for SM Closure

The monad Chern data support the statement

```text
index/net chirality = 3.
```

They do not yet prove

```text
dim H^1(X,E) = 3 with selected representatives Psi_1,Psi_2,Psi_3,
```

nor do they provide the sector-resolved projections into

```text
Q, u, d, L, e, N, H.
```

Consequently the following objects remain unavailable:

```text
Psi_a,i,
L2 metrics,
P_a,
G_a,
dotD_a along selected C1 alpha_1,
primitive C1 response blocks,
no-proxy Yukawa matrices.
```

This is a productive obstruction.  It says the next missing datum is finite and
auditable: the typed monad maps.

## Correct Way Forward

There are two rigorous routes from here.

### Route A: Corrected Dolbeault Connection

Supply a corrected selected matrix A^(0,1), then verify:

```text
barpartial_E^2 = 0,
dim H^1(X,E) = 3,
the representatives are compatible with the selected HYM/Strominger branch,
the E6-to-SM slot projections are specified.
```

The previous diagnostic repair does not suffice because it gives h1 = 2.

### Route B: Typed Monad Sections

Supply explicit maps

```text
f_i in H^0(X, L_i tensor K1^{-1}),
g_i in H^0(X, K2 tensor L_i^{-1}),
```

with transition data or invariant-section representatives, and verify:

```text
g o f = 0,
monad exactness away from the expected cohomology,
E is locally free or the allowed sheaf singularities are controlled,
H^1(X,E) has the selected three-family basis,
cup/Yoneda products give the rank-one E6 seed,
C1 deformation derivatives dotD_a are computable in the same basis.
```

Once either route passes, the existing zero-mode/dotD interface can be filled
and the primitive C1 response matrices can be computed without benchmark
entries.

## Verdict

The current corpus has not yet closed the finite Iwasawa three-family slot
construction.  What it has achieved is narrower but valuable:

```text
topological three-net-family data: supported,
rank-one E6 cubic normalization: supported,
literal printed A^(0,1) as selected complex: falsified,
diagnostic repaired A^(0,1): integrable but h1 = 2,
monad route: blocked until typed maps f,g are supplied.
```

Therefore the next proof artifact should be a typed finite monad-map dataset
or a corrected selected Dolbeault connection.  Until then, full SM matrix
closure remains open.
