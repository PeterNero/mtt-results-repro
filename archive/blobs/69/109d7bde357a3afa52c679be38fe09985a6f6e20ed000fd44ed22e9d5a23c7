---
abstract: |
  We isolate the most promising route to the dyadic factor in the effective
  order-448 MTT flavor quotient.  Six independent binary memories do not give
  order-64 phase resolution; they give Z_2^6 with exponent 2.  The viable
  route is a recursive refinement of the single shared central circle in
  which each binary obstruction is a carry into the next refinement level.
  The finite relation matrix 2x_i=x_{i+1}, 2x_5=0 has Smith normal form
  Z_64.  This note explains why the route is compatible with the corpus,
  how it respects the shared-circle requirement, and what still has to be
  proved before it can be claimed as a derivation.
author:
- Peter Nero
date: May 2026
title: |
  Dyadic Carry Refinement Candidate for the Z_64 Flavor Factor
---

# Purpose

The dyadic part of the current CP target is:

```text
Z_64.
```

The corpus gives two tempting ingredients:

1. six internal filtered directions organized as `1+2+3`;
2. proto-spinorial `Z_2` loop memory from the spin double cover.

But neither ingredient alone gives an order-64 character.  This note records
the viable refinement:

```text
recursive shared-circle dyadic carry.
```

# What is ruled out

The group

```text
Z_2 x Z_2 x Z_2 x Z_2 x Z_2 x Z_2
```

has 64 elements, but exponent 2.  Its unitary characters only see binary
phases.  It cannot support the CKM branch with denominator 64.

Thus the dyadic route cannot be:

```text
six directions = six independent bits = Z_64.
```

That is a group-size error.

# Candidate relation matrix

Let `x_0,...,x_5` denote six refinement levels of the same central-circle
bookkeeping phase, not six independent circles.

Impose:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0.
```

Then:

```text
64 x_0 = 0.
```

The Smith normal form is:

```text
Z_64.
```

This is the exact algebraic difference between six independent binary memories
and one six-stage dyadic carry chain.

# Recursive topology interpretation

This also answers the recursive-topology concern.  The carrier need not be a
literal finite circle with only 64 points.  It can be an inverse refinement
tower of the shared circle:

```text
... -> Z_64 -> Z_32 -> Z_16 -> Z_8 -> Z_4 -> Z_2.
```

The finite quotient relevant to CP is then the projector-selected stage:

```text
Z_64.
```

If the tower continues above `64`, the CP observable must factor through the
order-64 character.  That is compatible with a recursive topology and avoids
claiming that the full topology is only finite.

# Why the shared circle matters

The central-circle paper says the circle is the unique shared coherence
bookkeeping channel:

```text
B_1 = S^1_cen,
B_2 = S^1_cen x F_2,
B_3 = S^1_cen x F_3.
```

Therefore the dyadic lift should not introduce six unrelated phase circles.
The correct carrier is one shared circle with recursive internal refinement.

This is exactly what the carry matrix encodes:

```text
x_0,...,x_5 are levels of one bookkeeping phase.
```

# Corpus support

The route is supported by the following corpus motifs:

- the Book's `1+2+3=6` filter hierarchy;
- the central circle as unique shared phase/bookkeeping structure;
- the central-circle appendix, where flavor degrees of freedom are line-bundle
  sectors over `S^1_cen` and consistency restricts the holonomy group to a
  finite subgroup of `U(1)`;
- the central-circle statement that relative phases along `S^1_cen`
  contribute directly to CP-violating phases and are globally correlated;
- the action-level statement that CKM phases arise from circle-bundle holonomy
  and Wilson-line data encoded in the circle connection;
- proto-spinorial `Z_2` return obstruction;
- refinement stability;
- bookkeeping records that are retained rather than erased;
- finite coherent projection as a selection of admissible modes.

These facts do not prove the carry matrix, but they make it the least
category-breaking way to get `Z_64`.

# Important caution from ProtoSpinor

ProtoSpinor also warns against using bare circle winding as the whole
argument.  In the proto-spinor analysis, `SO(2)`/circle winding gives an
integer class compatible with continuous refinement families.  The forced
finite obstruction is the three-dimensional spinorial `Z_2` memory.

Therefore the dyadic order-64 row should not be claimed as:

```text
circle winding alone implies Z_64.
```

The correct claim is:

```text
central-circle phase holonomy
  +
refinement-stable spinorial loop memory
  +
finite coherent/projector or Wilson-line selection
  =>
selected dyadic character.
```

This is why the carry matrix is a candidate theorem rather than an already
proved consequence of the existence of `S^1_cen`.

# What has to be proved

The missing theorem should have the form:

```text
Theorem.  In the flavor CP sector, the refinement-stable central-circle
projector identifies the six dyadic loop-memory levels by
2x_i = x_{i+1}, with terminal closure 2x_5=0.
```

Equivalently, one must derive the relation matrix from one of:

1. the evolve-project operator's finite spectral window;
2. central-circle holonomy refinement;
3. proto-spinor return memory under repeated admissible refinement;
4. a Wilson-line/orbifold remnant acting on the shared circle;
5. a string/flux compactification whose integral rows reduce to this matrix.

# Success criterion

The dyadic derivation succeeds if the actual MTT relation matrix has an
invariant factor divisible by `64`, or a selected character of dyadic order
`64`.

It fails if the only derived structure is independent `Z_2^6`.

# Bottom line

The best dyadic candidate is:

```text
one shared central circle
  +
six-stage recursive dyadic carry
  =>
Z_64 effective CP character.
```

This is compatible with recursive topology, respects the shared-circle
constraint, and avoids dimension numerology.  It remains a proof obligation,
but it is now a precise one.
