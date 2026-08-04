# GEO.01 Covariant Projective-Module Bridge

**Date:** 2026-07-26
**Result:** universal geometry-to-operator construction closed conditionally

## What Changed

The missing continuum symbol is not a flat finite matrix. The correct exact
object is a smooth finite matrix-valued projector

```text
p_Q(x) in M_N(C-infinity(X6))
```

whose projective module carries the physical curved connection. By the
universal-connection theorem, every supplied unitary q79 HYM connection has
such a representation, and the connection, curvature, coupled differential,
adjoint, and Hessian form transport exactly.

This closes the universal construction at `10/10`.

## Important Type Correction

The `1<2<3` flag cannot live inside an irreducible stable HYM gauge bundle.
Parallel endomorphisms of such a bundle are scalar, so a rank-one or rank-two
projector would reduce the holonomy.

The flag instead belongs on a separate tensor factor:

```text
physical HYM module tensor lane factor tensor shared flat line.
```

This agrees with the current A45 separation of lane, family, and gauge data.

## Finite Matrix Rule

For a finite projector `P` and physical Hessian `H`, compute

```text
R = (I-P) H P.
```

- If `R=0`, `P H P` is an exact invariant restriction.
- If `R` is nonzero, the exact finite operator is the Feshbach-Schur map and
  includes the complementary Green-operator self-energy.

The rational witness has the same bare compression for two positive
Hessians, but one has residual norm squared `1/4`, self-energy `1/12`, and
effective first eigenvalue `11/12` rather than `1`.

## Current Status

```text
universal projective naturality:       10/10
physical q79 same-source instantiation: 0/3
B.GEO.01 overall:                       OPEN
```

The three physical rows are:

1. selected visible/hidden HYM endpoint connections from `B.HS.01`;
2. their explicit source-hashed `U_Q`, `p_Q`, and rank-102 complex map;
3. the transported finite subspace and either `R=0` or Feshbach equality.

Full-domain and continuum counts remain `0/4` and `1/9`.

## Why This Is Frontier Progress

There is no longer an unspecified "find a symbol map" problem. The exact
preprojection reference system, lane placement, and finite reduction law are
fixed. What remains is an endpoint-specific calculation that cannot be
performed before the physical HYM source exists.

No physical parameters, fits, or observed values were added.
