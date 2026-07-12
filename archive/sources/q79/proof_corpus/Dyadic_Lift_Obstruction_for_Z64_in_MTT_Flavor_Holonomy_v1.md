---
abstract: |
  We test the tempting idea that the Z_64 factor in the effective order-448 CP
  target follows directly from six internal MTT directions or six binary
  closure memories.  It does not.  Six independent Z_2 memories give a group
  with 64 elements, but its exponent is only 2, so its characters have only
  binary phase resolution.  A Z_64 flavor factor requires a cyclic dyadic lift,
  nested refinement with carry, or a projector/Wilson-line/orbifold relation
  that produces an order-64 character.  The corpus supports a central-circle
  Z_3 family holonomy and a proto-spinorial Z_2 loop memory, but it does not
  yet derive an order-64 cyclic character.  This note sharpens the proof
  obligation for the dyadic part of the Z_64 x Z_7 target.
author:
- Peter Nero
date: May 2026
title: |
  Dyadic Lift Obstruction for Z_64 in MTT Flavor Holonomy
---

# Purpose

The product quotient target

```text
Z_64 x Z_7
```

requires a dyadic factor with order-64 phase resolution.

It is tempting to identify `64 = 2^6` with the six internal filtered
directions of MTT or with six binary closure/refinement choices.  This note
explains why that is not enough.

There is also a second reason for caution.  The MTT corpus often formulates
the internal structure as circle, lens, nil, central-circle reuse, and
effective carrier ranks.  For finite flavor holonomy, the six-direction count
should therefore be treated only as one motivation for a dyadic lift, not as
the definition of the quotient.

# What the corpus supports

The corpus supports:

1. a shared central circle `S^1_cen`;
2. a `Z_3` flavor-line holonomy over the central circle, producing three
   family sectors;
3. proto-spinorial `Z_2` loop memory from the Spin double-cover requirement;
4. refinement-stable loop bookkeeping;
5. finite coherent/projector selection.

These are real structural ingredients.  But none of them, as currently stated,
is an order-64 cyclic character.

# Group-size trap

Six independent binary memories give

```text
G = Z_2 x Z_2 x Z_2 x Z_2 x Z_2 x Z_2.
```

This group has

```text
|G| = 64.
```

But every element has order at most `2`, so

```text
exponent(G) = 2.
```

Its characters only produce phases `0` and `pi` along each binary component.
It cannot approximate the CKM CP phase with denominator `64`.

Therefore:

> `64` states are not the same as `Z_64` phase resolution.

# What would derive `Z_64`

A real `Z_64` derivation requires one of the following stronger structures.

## Cyclic dyadic lift

The shared circle may admit a cyclic refinement

```text
theta ~ theta + 2pi/64.
```

This would give an actual `Z_64` character group, but it must come from
projector periodicity, Wilson-line quantization, or a quotient relation.

## Nested binary refinement with carry

Six binary decisions can produce `Z_64` only if they are not independent.  They
must assemble into a cyclic counter:

```text
0 -> 1 -> 2 -> ... -> 63 -> 0.
```

Mathematically, this means the quotient is a nontrivial cyclic dyadic extension
rather than `Z_2^6`.

## Nested carrier incidence

The dyadic lift may also arise from the recursive carrier diagram itself,
rather than from literal dimension counting.  A live option is a containment
pattern

```text
C_1 subset L_4 subset N_7,
```

where the numbers are carrier-depth, closure-level, or quotient labels unless
a literal geometric-dimension theorem is supplied.  In that case the relevant
object is not six independent binary memories, but the Smith normal form of the
nested circle-lens-nil relation matrix.

## Orbifold or Wilson-line remnant

An orbifold, discrete gauge quotient, or Wilson-line remnant could impose

```text
64 e_c = 0
```

or an equivalent invariant factor in the Smith normal form.

## Projector periodicity

The coherent projector could preserve only every sixty-fourth central-circle
phase sector.  This would be a valid MTT source if it is derived from the
evolve-project dynamics or finite coherent compression.

# Relation to the known `Z_3`

The central-circle paper states that fermion families arise from a `Z_3`
holonomy of a flavor line bundle over `S^1_cen`.

This is important because it confirms that flavor holonomy can live on the
shared circle.  But it also means the currently explicit central-circle flavor
holonomy is `Z_3`, not `Z_64`.

Thus the dyadic proof must add a new layer:

```text
central-circle family holonomy: Z_3
additional CP dyadic resolution: Z_64 or equivalent
```

The two should not be conflated.

# Minimal algebraic tests

The following quotients are not equivalent for CP:

```text
Z_64       exponent 64
Z_2^6      exponent 2
Z_3 x Z_64 exponent 192
Z_3 x Z_2^6 exponent 6
```

Only groups whose exponent or selected diagonal character has sufficiently
large dyadic order can support the desired CKM phase resolution.

# Failure criterion

The dyadic part of the flavor target fails if the only derived binary data are
independent `Z_2` memories.  In that case the group may have 64 elements, but
it lacks order-64 characters.

# Success criterion

The dyadic part succeeds if the derived relation matrix contains an invariant
factor divisible by `64`, or if the selected diagonal character in the finite
abelian quotient has order divisible by `64`.

# Bottom line

The `64` factor is not automatic.  MTT must derive a cyclic dyadic lift, nested
binary carry structure, nested carrier-incidence quotient, or equivalent
projector/orbifold/Wilson-line quotient.

This is now the exact proof obligation for the dyadic side of the effective
order-448 CP target.
