---
abstract: |
  We add an explicit nested-carrier option to the no-proxy flavor holonomy
  program.  The MTT corpus often speaks in terms of circle, lens, nil, central
  circle reuse, and effective carrier ranks, not merely literal dimensions.
  Therefore the previous six-direction motivation for the dyadic factor must
  not be over-privileged.  A live alternative is a recursive containment
  pattern in which a shared circle carrier sits inside a lens carrier, which in
  turn sits inside a nil carrier.  In shorthand this option is
  circle-on-1, lens-on-4, nil-on-7, or C_1 subset L_4 subset N_7.  This note
  treats those numbers as possible carrier-depth, closure-level, or quotient
  labels until the corpus supplies stronger geometric evidence.  The main
  result is cautious: nested labels alone do not produce a finite CP quotient.
  They become useful only after the corresponding closure, monodromy, flux,
  Wilson-line, orbifold, or projector rows are derived and inserted into the
  integer relation matrix.
author:
- Peter Nero
date: May 2026
title: |
  Nested Circle-Lens-Nil Carrier Options for the Effective Order-448 Flavor Target
---

# Purpose

The flavor closure program has been using the effective order-448 target as a
diagnostic for CP holonomy.  Earlier notes considered a source presentation

```text
Z_64 x Z_7
```

with the warning that, because `64` and `7` are coprime, the abstract Smith
normal form is cyclic:

```text
Z_64 x Z_7 is isomorphic to Z_448.
```

The value of the product notation is source-theoretic.  It asks whether MTT
derives a dyadic source and a sevenfold source before they combine into one
effective cyclic phase resolution.

This note adds the alternative raised in the research discussion:

```text
circle on 1, lens on 4, nil on 7.
```

The point is not to replace one guess with another.  The point is to prevent
the program from assuming a dimensional picture where the corpus really gives
recursive carrier structure.

# Corpus constraint

The corpus strongly supports the following structural ingredients:

1. a unique shared central circle `S^1_cen`;
2. a lens sector built over, or reusing, the central circle;
3. a nil sector built on reused circles;
4. a joint coherent projector over these carriers;
5. effective ranks or carrier roles associated with circle, lens, and nil.

It also contains a separate lower-bound argument that independent continuous
layer carriers require enough internal dimension.  That argument is useful,
but it does not license every later finite quotient to be read off from a
literal dimension count.

For flavor CP, the safer rule is:

> Use dimensions only when the paper is explicitly doing dimensional
> reduction.  For finite flavor holonomy, use the derived carrier relation
> matrix.

# The nested option

The possible nested carrier picture is

```text
C_1 subset L_4 subset N_7,
```

where:

- `C_1` denotes the unique shared circle base;
- `L_4` denotes a lens-level carrier, quarter-turn phase, fourth closure level,
  or fourfold incidence stage;
- `N_7` denotes a nil-level carrier, sevenfold closure, sevenfold monodromy, or
  sevenfold quotient stage.

There are three interpretations, and they must be kept separate.

# Interpretation A: literal dimensions

The statement could mean that the nil carrier is literally seven-dimensional,
contains a four-dimensional lens carrier, which contains a one-dimensional
circle.

This is the strongest reading and currently the least secure.  The corpus
search found repeated support for circle/lens/nil carriers and for effective
rank organization, but not a clean theorem that flavor CP requires a literal
seven-dimensional nil space containing a literal four-dimensional lens space.

Therefore this reading should remain possible, not assumed.

# Interpretation B: carrier-depth labels

The statement could mean that `1`, `4`, and `7` label positions in a recursive
bookkeeping hierarchy rather than manifold dimensions.  On this reading, nil
contains lens contains circle because the admissible description is assembled
by reuse:

```text
central circle -> lens-over-circle -> nil-over-reused-circles.
```

This fits the corpus better.  The central circle is not merely one coordinate;
it is the shared bookkeeping channel that every sector must respect.

# Interpretation C: quotient or congruence levels

The statement could mean that the carrier relation matrix has closure levels
or congruence moduli associated with `1`, `4`, and `7`.

For flavor CP this is the most directly testable interpretation.  One writes a
relation matrix

```text
A_nested
```

on carrier generators

```text
e_c, e_l, e_n, e_12, e_23, e_31
```

and computes

```text
Gamma_fl = coker A_nested.
```

The finite quotient is whatever the Smith normal form gives.

# Why labels alone are not enough

Containment rows such as

```text
e_l = 4 e_c,
e_n = 7 e_l
```

identify generators.  By themselves they do not make the quotient finite.  They
leave continuous or free character directions.

Finite holonomy appears only when some closure row is also derived, for example

```text
64 e_c = 0,
7 e_n = 0,
4 e_l = 0,
q_c e_c + q_l e_l + q_n e_n = 0,
```

or a more precise row coming from nil monodromy, flux quantization, a
Wilson-line remnant, an orbifold quotient, or projector periodicity.

# First template check

The companion script

```text
nested_carrier_matrix_templates.py
```

tests the simplest possibilities.

The outputs are:

```text
Nested labels only
  torsion factors: none
  free rank: 3

Naive nested 4/7 closures
  torsion factors: [4]
  free rank: 2

Separated source rows 64e_c=0 and 7e_n=0
  torsion factors: [448]
  free rank: 3

Dyadic circle plus nil seven with naive containment
  torsion factors: [4]
  free rank: 2

Lens quarter-turn plus nil seven, no dyadic lift
  torsion factors: [28]
  free rank: 3
```

Thus:

1. `e_l=4e_c` and `e_n=7e_l` plus the CKM phase-sum row gives no finite torsion.
2. Naively adding `4e_l=0` and `7e_n=0` with those containment rows does not
   produce the desired order-448 quotient; nesting can collapse factors.
3. Separate source rows `64e_c=0` and `7e_n=0` do produce invariant factors
   equivalent to an effective `Z_448` phase quotient.
4. A lens quarter-turn plus a nil sevenfold closure gives at most order-28
   resolution before any dyadic lift is added.

Thus the nested option is promising only if it yields the right rows.  The
numbers `1`, `4`, and `7` are not a proof by themselves.

# Role of the shared circle

The shared circle remains central.  If the nil carrier contains the lens
carrier and the lens carrier contains the circle carrier, then the CP quotient
cannot be computed from the terminal nil or lens factor alone.  It must be
computed from the whole incidence diagram:

```text
S^1_cen -> L -> N
```

with all closure and projection rows included.

This is exactly where recursive topology matters.  A finite nil closure can
pull back to the circle.  A lens quarter-turn can impose a lepton CP
subquotient.  A projector row can preserve a diagonal combination rather than
the separate factors.

# Revised proof obligation

The correct next proof target is:

> Derive the integer relation matrix for the recursive circle-lens-nil flavor
> carrier, then compute its Smith normal form and character table.

In practice this means determining:

1. whether the nil carrier has a genuine sevenfold closure, monodromy, or
   quotient row;
2. whether the lens carrier contributes a genuine fourfold row, especially one
   capable of explaining the exact lepton `-pi/2` phase;
3. whether the shared circle receives a cyclic dyadic lift, a nested binary
   carry, or an equivalent projector/Wilson-line/orbifold row;
4. how the pairwise flavor lines `e_12,e_23,e_31` couple to the carrier rows;
5. whether the selected character reproduces the CKM branch near
   `delta_q = 1.107978573420` and the lepton branch at `delta_l = -pi/2`.

# What this changes

This widens the search space in a disciplined way.

The previous dyadic discussion should not be read as "MTT has six dimensions,
therefore Z_64."  That was already false if the six data are independent
binary memories.  The stronger and cleaner statement is:

> The flavor quotient needs an order-64 dyadic character, an order-7 character,
> or an equivalent order-448 diagonal character.  These may arise from nested
> circle-lens-nil carrier incidence rather than from a literal dimension count.

# Bottom line

The option

```text
C_1 subset L_4 subset N_7
```

does not violate the current setup.  It is in fact more faithful to the corpus
than a purely dimensional reading, provided we treat it as a recursive carrier
hypothesis until proven.

The correct way forward is to extract the actual nested incidence and closure
rows from MTT, compute

```text
Gamma_fl = coker A_nested,
```

and then test the finite characters.  If nil truly supplies a sevenfold row and
the shared circle supplies an order-64 lift, the effective `Z_448` target becomes
a derived quotient rather than a guessed denominator.

# Addendum: complex/orthogonal nesting

The most promising refinement is not to read `subset` as naive real
containment.  For flavor CP, the stronger candidate is complex orthogonal
nesting:

```text
C --J_L--> L --R_N--> N,
```

where `J_L^2=-1` is a lens quarter-turn and `R_N` is a nil rotor.  This aligns
the carrier picture with the complex Hilbert/Schrödinger layer of MTT and
avoids treating a quarter-turn as the integer relation `e_l=4e_c`.

The companion paper `Complex_Orthogonal_Nesting_for_MTT_Flavor_Holonomy_v1.md`
develops this version.  Its phase-lattice scan shows that lens order `4` plus
nil order `7` gives only exponent `28`, while dyadic order `64` plus nil order
`7` gives the effective exponent `448`.  Thus complex nesting improves the
interpretation, but the order-64 dyadic lift remains a real proof obligation.

Spacetime dimension should be included as an admissibility constraint, not as a
new quotient knob.  The effective base `Y_4` supplies spin/chirality,
Lorentzian dynamics, and the Schrödinger/unitary layer in which complex phase
rotation is meaningful.  The finite CP denominator must still come from the
selected unitary holonomy quotient on the recursive flavor carrier.
