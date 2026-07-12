---
abstract: |
  We scan two-factor finite abelian quotients for CKM phase-branch quality and
  exact leptonic -pi/2 compatibility.  The scan confirms that Z_64 x Z_7 is
  not an isolated coincidence but part of a broader effective-order pattern:
  small product presentations that match the CP benchmark at Z_448 quality
  contain a 64-type dyadic component and a component carrying a 7 denominator.
  Since 64 and 7 are coprime, Smith normal form combines the clean presentation
  Z_64 x Z_7 into the cyclic invariant factor Z_448.  This refines
  the target for recursive MTT quotient selection.  The theory need not derive
  literal Z_448 or uniquely Z_64 x Z_7; it must derive a finite abelian quotient
  whose selected character has effective phase resolution 448 on the CKM
  branch while preserving the exact pairwise phase-sum and the separate
  Majorana two-torsion condition.
author:
- Peter Nero
date: May 2026
title: |
  Product Quotient Scan and the Effective Order-448 Target in MTT Flavor CP
---

# Purpose

The product quotient criterion showed that the source presentation

```text
Z_64 x Z_7
```

matches the finite CP benchmark as well as cyclic `Z_448`.  Since `64` and `7`
are coprime, this product is abstractly isomorphic to `Z_448`; its value is
that it splits the source problem into a dyadic row and a sevenfold row.

This note asks whether that product is isolated or part of a larger pattern.

# Scan

The script

```text
finite_product_quotient_scan.py
```

scans two-factor products

```text
Z_d1 x Z_d2
```

with `d1,d2 <= 128` and product size at most `5000`.  It keeps products with:

- exact leptonic `-pi/2`;
- CKM phase-branch error below `1e-4`.

# Main pattern

The leading hits include:

```text
G             exponent   CKM weights   phase error      J error
Z_7 x Z_64       448     (2,57)        6.164e-06       8.920e-11
Z_64 x Z_7       448     (57,2)        6.164e-06       8.920e-11
Z_14 x Z_64      448     (4,57)        6.164e-06       8.920e-11
Z_28 x Z_64      448     (1,9)         6.164e-06       8.920e-11
Z_56 x Z_64      448     (9,1)         6.164e-06       8.920e-11
Z_64 x Z_28      448     (9,1)         6.164e-06       8.920e-11
Z_64 x Z_56      448     (1,9)         6.164e-06       8.920e-11
```

and related multiples such as:

```text
Z_7 x Z_128, Z_14 x Z_128, Z_21 x Z_64, Z_35 x Z_64, ...
```

These all share the same underlying feature: the diagonal character has access
to an effective denominator of `448` or a multiple.

# Interpretation

The important target is not the literal source presentation.  It is the
effective character resolution.

The refined target is:

```text
Tor coker A_rec contains a selected character x
whose order is 448 or a suitable multiple, and whose pairwise weights reproduce
the CP benchmark.
```

This means all of the following source presentations can be acceptable in
principle, provided their Smith normal form or selected character has the
required order:

- `Z_448`;
- `Z_64 x Z_7`;
- `Z_64 x Z_14`;
- `Z_64 x Z_28`;
- `Z_64 x Z_56`;
- larger products whose selected diagonal character descends to the same
  effective order-448 phase.

But the quotient must be derived.  The scan only tells us what to test.

# Why the dyadic factor matters

The exact leptonic benchmark `-pi/2` requires a factor divisible by `4`.

The high CKM phase accuracy found in the scan is much stronger: the best
product hits use a dyadic component with at least `64` resolution.  This makes
the `2^6` factor structurally interesting.  It may point toward:

- six internal filtered directions;
- repeated binary/projector closure;
- dyadic refinement of the shared circle;
- finite coherent compression levels;
- or an orbifold/Wilson-line remnant with a `2^6` component.

None of these is yet a derivation.  They are search locations.

# Why the seven factor matters

The `7` component is what turns `64` into effective order

```text
64 * 7 = 448.
```

Because the two factors are coprime, a quotient with invariant rows `64 e_2=0`
and `7 e_7=0` has Smith normal form `Z_448`.  The product notation is therefore
a source decomposition, not a distinct finite abelian group from `Z_448`.

The corpus does not yet exhibit a derived `Z_7` flavor quotient.  Therefore the
seven factor is currently the sharper mystery.

Possible sources remain:

- flux congruences;
- orbifold/discrete gauge quotient;
- nil lattice monodromy;
- Wilson-line remnant;
- global stability extremum.

# Consequence for proof strategy

The quotient proof can now be split into three independent tasks:

1. derive a dyadic component with at least `64` phase resolution;
2. derive a sevenfold or seven-denominator component;
3. prove that the selected pairwise CP channel couples them diagonally.

This is better than asking for `Z_448` in one piece.

# Majorana check

The Majorana condition is unchanged.  A neutral character `m` in the finite
abelian quotient must obey

```text
2m = 0.
```

For products with a `64` factor, the two-torsion is carried by the midpoint of
the dyadic component.  The CP character itself is not the Majorana character.

# Bottom line

The effective target is now:

```text
derive an effective order-448 CP character,
not necessarily a literal Z_448 group.
```

The product scan makes `Z_64 x Z_7` the clean minimal source decomposition,
but its Smith normal form is the cyclic invariant `Z_448`.  The real MTT result
may be any finite abelian quotient with the same selected phase resolution.
