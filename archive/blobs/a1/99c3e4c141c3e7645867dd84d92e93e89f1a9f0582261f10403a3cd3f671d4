---
abstract: |
  We turn the recursive/shared-circle flavor holonomy program into a relation
  ledger.  The corpus supplies several structural rows for the quotient matrix:
  the common central circle S^1_cen, bare lens torsion, pairwise phase-sum
  closure, flux quantization, possible Wilson-line remnants, nil lattice data,
  and coherent-projector compatibility.  However, it does not yet supply a
  derived integer relation whose Smith normal form contains Z_448.  This paper
  separates known rows from missing rows and gives the exact calculation needed
  next.  The conclusion is disciplined: the shared circle keeps a large finite
  quotient possible, but deriving the CP benchmark requires computing the
  recursive integer relation matrix A_rec from selected flux, bundle, nil, and
  projector data.
author:
- Peter Nero
date: May 2026
title: |
  Candidate Relation Ledger for Recursive MTT Flavor Holonomy
---

# Purpose

The previous note established that the finite flavor character group should be
computed as

```text
Gamma_fl = coker A_rec.
```

This paper identifies what is already known about `A_rec` from the MTT corpus
and what still has to be computed.

# Generators

Use the carrier generator vector

```text
e = (e_c, e_l, e_n, e_12, e_23, e_31),
```

where:

- `e_c` is the shared central-circle character;
- `e_l` is the lens-over-circle character;
- `e_n` is the nil-over-reused-circle character;
- `e_12, e_23, e_31` are the pairwise flavor overlap characters.

# Known structural rows

## Pairwise phase sum

The topology-only overlap-bundle condition gives

```text
e_12 + e_23 + e_31 = 0.
```

As a matrix row:

```text
(0, 0, 0, 1, 1, 1).
```

This row is secure.

## Bare lens torsion

The terminal lens factor `L(3,1)` contributes

```text
3 e_l = 0.
```

As a row:

```text
(0, 3, 0, 0, 0, 0).
```

This row is secure for the bare lens factor, but it is not the full recursive
quotient.

## Shared-circle reuse

The corpus states that every internal bundle uses the common central circle:

```text
B_n|_y ~= S^1_cen x Sigma_n.
```

This means lens and nil characters are not independent of central-circle
bookkeeping.  The expected relation type is

```text
e_l - a_l e_c = 0,
e_n - a_n e_c = 0.
```

Rows:

```text
(-a_l, 1, 0, 0, 0, 0),
(-a_n, 0, 1, 0, 0, 0).
```

The existence of shared-circle coupling is secure.  The integers `a_l, a_n`
are not yet computed.

# Missing but required rows

## Nil lattice rows

The nil sector can impose lattice and commutator constraints, but the relevant
flavor-lifted nil relation has not yet been extracted.  The expected row type is

```text
(b_c, b_l, b_n, 0, 0, 0).
```

These integers must come from the chosen nil lattice and its compatible flat
bundle data.

## Flux rows

The heterotic/Lens x Nil corpus contains integer fluxes, and flux quantization
is part of the admissible data.  A flux row has the expected type

```text
(q_c, q_l, q_n, q_12, q_23, q_31).
```

For a large finite CP quotient such as `Z_448`, this is one of the most likely
places for the necessary order to enter.  But no corpus row currently states
`448 e_c = 0` or an equivalent derived relation.  Such a row must be computed,
not inserted.

## Wilson-line or orbifold rows

A continuous central-circle phase can become finite if an orbifold, discrete
gauge remnant, or Wilson-line quotient survives the coherent projector.  The
expected row type is again an integer relation among the carrier generators.

This remains open.

## Projector compatibility rows

The joint coherent projector may preserve only diagonal combinations of circle,
lens, and nil carrier directions.  This can create additional integer
relations, especially when the recursive carrier is required to close after a
finite number of returns.

This is likely important, but not yet computed.

# What the known rows imply

Using only the secure terminal rows

```text
3 e_l = 0,
e_12 + e_23 + e_31 = 0,
```

the quotient has torsion `Z_3` and a free part.  This does not derive the
finite CP benchmark.

If shared-circle rows are added with known integers `a_l, a_n`, then lens
torsion pulls back onto the central circle:

```text
3 a_l e_c = 0.
```

Thus shared-circle recursion can amplify the visible consequence of lens
torsion, but the amplification is controlled by `a_l`.  Without a derived
`a_l`, this remains a template.

If an independently derived row

```text
448 e_c = 0
```

or an equivalent diagonal relation appears from flux/projector/orbifold data,
then the `Z_448` target becomes plausible.  But this row is not currently in
the corpus.

# Candidate quotient tests

The next calculation should evaluate the Smith normal form for a family of
candidate matrices:

## Minimal known matrix

```text
A_known =
[
  (0, 3, 0, 0, 0, 0),
  (0, 0, 0, 1, 1, 1)
].
```

Expected torsion: `Z_3`.

## Shared-circle matrix

```text
A_shared(a_l,a_n) =
[
  (-a_l, 1, 0, 0, 0, 0),
  (-a_n, 0, 1, 0, 0, 0),
  (0, 3, 0, 0, 0, 0),
  (0, 0, 0, 1, 1, 1)
].
```

This tests how central-circle reuse changes the quotient.

## Flux/projector matrix

```text
A_full =
[
  shared-circle rows,
  lens torsion row,
  nil lattice rows,
  flux rows,
  Wilson/orbifold rows,
  pairwise phase-sum row,
  projector diagonal rows
].
```

This is the actual no-proxy object.  It is not yet known.

# Criteria for success

The recursive quotient program succeeds if:

1. `A_full` is derived from MTT data without fitting CKM or PMNS;
2. `Tor coker A_full` contains a cyclic `Z_448` subsystem, or another finite
   subsystem reproducing the CP benchmark;
3. the pairwise weights project to `(79,-112,33)` or an equivalent phase-sum
   triple;
4. the neutral sector has two-torsion or a higher-rank real/pseudo-real
   structure suitable for Majorana mass;
5. the same quotient also constrains the allowed Yukawa overlap channels.

# Criteria for failure

The `Z_448` target fails if:

1. the derived `A_full` has only small torsion such as `Z_3`;
2. the derived torsion has no character approximating the CKM CP phase at the
   required precision;
3. the only way to get `Z_448` is to insert `448` as a phenomenological row;
4. the neutral sector lacks a Majorana-admissible real structure and no
   Dirac/higher-operator replacement is supplied.

# Bottom line

The shared circle means we must not stop at terminal manifold torsion.  The
right calculation is recursive and quotient-theoretic.  But the standard of
proof is also clear: `Z_448` must appear in the Smith normal form of a derived
relation matrix.  Until that matrix is computed, `Z_448` remains a finite CP
target, not a theorem.

