# MTT Selected q79 Alignment Eight-by-Ninety-Two Period Execution v1

## Result

A131 evaluates the eight primitive alignment-residue forms on the exact
rank-92 integral `H2` basis constructed in A130.  Every nonzero column is
computed on the same selected endpoint carrier as the A126/A127 beta.

The result is a floating `8x92` period matrix with a complete two-run error
envelope.  The first 90 columns are floating primary periods and the final two
Leray-edge columns are exact zero.  This closes period-matrix construction; it
does not by itself decide the exact integer equation `z_beta=Pi*ell`.

## Selected residue engine

The unchanged A118 Gauss-Manin reduction and thimble quadrature are reused,
but the residue map is replaced by the exact A123 alignment-dependent map.
For `L=A(a,b,1)^T` and `v=A M(a,b,1)^T`, the two projective charts use

```text
y chart: c=-L1(v0 L1-v1 L0), m=-L1(v2 L1-v1 L2),
z chart: c= L2(v0 L2-v2 L0), m= L2(v1 L2-v2 L1),
residue=c I0+m I1.
```

The eight generators are `E12,E13,E21,E23,E31,E32,H1,H2`.  No identity-
alignment residue row is silently inherited.

## Period-blind projective atlas

The `y` chart is badly conditioned on several selected radial paths.  A fixed
257-point Chebyshev endpoint-clustered scan evaluates only the equilibrated
Gauss-Manin reduction condition in the A123 `y/z` atlas.  It never evaluates
a period value.  The resulting deterministic atlas selects

```text
42 y-chart columns,
48 z-chart columns.
```

This removes every high-precision fallback solve.  Across all 90 production
columns, the maximum equilibrated reduction condition is about `4.03e7` and
the maximum reduction residual is below `2.68e-10`.  In particular, the two
previously difficult paths `d45` and `d74` become regular in the `z` chart.

The A123 five-period transition fixes the common orientation on chart
overlaps.  The rejected sign is separated by a large residual ratio; no
period magnitude or observed value enters chart selection.

## Ninety primitive thimbles

All 90 selected thimbles are executed.  A second run uses cutoff `3e-6`, 100
working decimal digits, and tighter ODE tolerances.  It independently compares
all 720 primitive complex entries.  The maximum column-scaled difference is

```text
2.1717463262818513e-9.
```

After projection through the thimble part of the exact A130 basis, the maximum
scaled difference is `6.1808759454005203e-10`.

## Canonical integral orientation

A130 orients each Picard-Lefschetz vector by requiring its first nonzero
coordinate to be positive.  The numerical thimble engine instead orients the
endpoint chord by root labels.  These conventions differ by 40 column signs.

The four A130 unimodular pivot columns `1,2,4,5` determine a marked base-period
matrix.  Enumerating the eight pivot-sign gauges after fixing `sigma_1=+1`
gives one compatible sign vector.  On the two holomorphic period rows,

```text
sigma_i p_i^hol = P_marked^hol v_i
```

holds for all 90 columns with maximum scaled residual
`8.5999644472263976e-9`.  The next sign assignment has residual greater than
one, a separation ratio above `1.34e8`.  The normalized Riemann matrix is
symmetric to `2.33e-10`, and its imaginary eigenvalues are positive.

Only the two holomorphic rows are used for compact-`H1` orientation.  The three
higher meromorphic rows retain puncture-at-infinity lift data and are not
misrepresented as compact-homology invariants.

## Handle columns

Both certified torus-handle paths select the `y` chart using a period-blind
condition scan over every certified trajectory node.  Starting from the
synchronized marked fiber, the selected A129 actions produce eight primitive
handle-cylinder columns.  Independent period continuation recovers the A130
interval-selected central lifts:

```text
A: +1, scaled endpoint residual 2.47e-10,
B: -1, scaled endpoint residual 4.79e-10.
```

A tighter 110-digit rerun supplies the handle error envelope.

## Integral assembly and Leray edge

Let `T` be the `8x90` primitive thimble table, `sigma` the canonical sign
vector, `H` the `8x8` handle table, and `U` the exact A130 `98x90` primary
basis.  The emitted matrix is

```text
Pi = [ (T diag(sigma) | H) U | 0_(8x2) ].
```

The last two columns vanish exactly because the eight traceless incidence
residues span the primitive holomorphic two-form subspace, whereas the A130
fiber and adjusted horizontal Leray classes are dual to ambient restrictions.

Propagating every primitive two-run difference through `abs(U)` gives maximum
primary column-scaled envelope

```text
1.654861e-9.
```

## Strict frontier

Closed here:

1. the selected-carrier `8x90` primitive thimble table;
2. canonical orientation against the exact A130 lattice;
3. all eight selected handle periods and independent central-lift replay;
4. the complete floating `8x92` matrix on an exact integral basis;
5. exact zero of the 16 Leray-edge entries.

Still open:

1. interval enclosures for the 720 nonzero period entries;
2. an exact or height-bounded decision of `z_beta=Pi*ell`;
3. selection of a nonzero integral branch, if one exists.

No observed Standard Model value is used.
