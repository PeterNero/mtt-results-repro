---
abstract: |
  We convert the product-quotient CP target Z_64 x Z_7 into a source ledger.
  The corpus supports the general mechanisms needed for finite quotient
  selection: Wilson-line/flat-connection data, orbifold/boundary projections,
  flux integer systems, left-invariant Diophantine compactification equations,
  and a discrete gauge-flavor bottleneck.  It does not yet contain a derived
  Z_7 row, a derived Z_64 row, or a proof that these factors couple through
  the pairwise flavor phase-sum as a diagonal order-448 character subsystem.
  This note identifies plausible origins for each factor, states what would
  count as a derivation, and makes the failure criteria explicit.
author:
- Peter Nero
date: May 2026
title: |
  Factor Source Ledger for the Z_64 x Z_7 MTT Flavor Target
---

# Purpose

The product quotient

```text
Z_64 x Z_7
```

matches the CP benchmark as well as cyclic `Z_448` under a diagonal character.
This makes it a first-class replacement target.

But it is still only a target until both factors are selected by MTT data.
This note asks:

> Where could the `64` and `7` factors come from, and what would prove that
> they are not proxy choices?

# What the corpus already supports

The corpus supports the following mechanisms in principle.

## Discrete gauge-flavor bottleneck

The parameter-closure corpus identifies holonomy phases and localization
patterns as the remaining gauge-flavor bottleneck.  Mixing matrices are
derived, not fundamental.  Independent phase fitting is forbidden.

Therefore a finite flavor quotient is allowed only as a selected bottleneck,
not as a phenomenological insertion.

## Wilson-line and flat-connection data

The corpus allows Wilson-line or flat-connection data as phase-like holonomy
features.  These are exactly the kind of data that can produce finite
characters after quotienting, orbifolding, flux quantization, or projector
selection.

## Orbifold and boundary projections

The execution-level Calabi-Yau corner uses a factorized toroidal orbifold or
its crepant resolution as a controlled existence corner.  The KK and projection
papers also state that orbifolds/boundaries project modes and that Wilson
lines, flux backgrounds, and geometric asymmetries can break symmetries.

Thus orbifold/discrete quotient rows are admissible candidates.

## Flux integer systems

The heterotic flux papers provide integer flux data, e.g. Lens x Nil flux
integers `(f,h)` and Iwasawa integer choices such as `(1,2),(-1,-2)`.
These currently fix anomaly/radius data and discrete invariant loci.  They do
not yet give a flavor character quotient, but they are legitimate sources for
integer rows in `A_rec`.

## FCC as Diophantine selection

The KK/FCC corpus frames compactification constraints as finite algebraic and
Diophantine systems with integer data.  This is exactly the mathematical form
needed for a Smith-normal-form quotient.

# Factor `64`

The factor

```text
64 = 2^6
```

is naturally suggestive in MTT because the internal carrier has six filtered
directions and repeated binary closure/refinement/projector choices can
produce dyadic quotients.

However, this is only a motivation.  A real derivation of `Z_64` requires one
of the following:

1. a recursive shared-circle relation matrix whose Smith normal form contains
   a `64` factor;
2. a projector periodicity condition of order `64`;
3. an orbifold/discrete gauge remnant with a `Z_64` component;
4. a Wilson-line quotient reduced to `64` allowed phases;
5. a flux/projector Diophantine row whose invariant factor is `64`.

Moreover, the six-direction reading is not the only live route.  The corpus
often phrases the internal structure as a recursive circle-lens-nil carrier
with a unique shared central circle.  A nested carrier hypothesis such as

```text
C_1 subset L_4 subset N_7
```

could produce the dyadic factor through incidence, closure, or projector rows
rather than through literal dimension counting.  The test is again the Smith
normal form of the derived relation matrix.

At present, the corpus does not provide an explicit `Z_64` row.

# Factor `7`

The factor

```text
7
```

is not currently singled out by the corpus search.  This is important.  It
means `Z_7` cannot be assumed as a hidden pre-existing MTT motif.

A real derivation of `Z_7` requires one of the following:

1. an orbifold/discrete gauge quotient with order `7`;
2. a flux congruence row producing a `7` invariant factor;
3. a nil lattice or monodromy quotient with order `7`;
4. a Wilson-line remnant reduced to seven allowed phases;
5. a global closure/stability extremum selecting a sevenfold quotient.

The nested-carrier option makes item 3 more concrete: the sevenfold factor may
come from the nil carrier if nil supplies a genuine sevenfold closure,
monodromy, or quotient row.  It should not be inferred merely from the label
`nil on 7`.

At present, none of these has been exhibited.

# Diagonal coupling

Even if `Z_64` and `Z_7` are separately derived, the CP benchmark requires a
selected diagonal character.  In the diagnostic search:

```text
G = Z_64 x Z_7
CKM weights = (57, 2)
lepton weights = (48, 0)
```

The effective CKM phase is

```text
2 pi (57/64 + 2/7) mod 2pi.
```

This means that a full MTT derivation must show not merely that both factors
exist, but that the pairwise overlap channel selects the diagonal combination.

The diagonal selection should come from:

- pairwise line-bundle phase-sum closure;
- overlap-channel admissibility;
- projector compatibility;
- or a common flux/orbifold constraint tying the factors together.

# What would count as success

The `Z_64 x Z_7` replacement target succeeds if the derived recursive relation
matrix `A_rec` has

```text
Tor coker A_rec
```

containing a product subsystem equivalent to `Z_64 x Z_7`, and the selected
pairwise character map sends the flavor CP channel to the diagnostic weights
or an equivalent tuple with the same phase.

Minimum proof items:

1. derive a `64` invariant factor;
2. derive a `7` invariant factor;
3. prove they survive the coherent quotient;
4. prove the selected CP character is diagonal across them;
5. prove the pairwise phase-sum rule is exact;
6. keep the Majorana two-torsion condition separate.

# What would count as failure

The `Z_64 x Z_7` target fails if:

1. no `7` factor appears in the selected quotient;
2. the only `64` source is a numerological reading of six internal directions;
3. the factors appear but are projected into separate sectors that cannot
   couple diagonally;
4. the diagonal weights must be inserted by hand;
5. the derived quotient has only small torsion, e.g. `Z_3`;
6. the derived quotient has a different character spectrum that cannot
   reproduce CKM CP without proxy phase fitting.

# Immediate computation

The next computation should build candidate `A_rec` matrices from actual
integer data:

1. shared-circle rows;
2. lens torsion;
3. Lens x Nil flux rows `(f,h)`;
4. Iwasawa flux rows from `(1,2),(-1,-2)`;
5. orbifold/resolution quotient rows, if available;
6. Wilson-line finite-remnant rows, if available;
7. projector diagonal rows.

Then compute Smith normal forms and test whether `64` and `7` appear as
invariant factors or as a product subsystem with exponent `448`.

# Bottom line

`Z_64 x Z_7` is a better target than demanding literal `Z_448`, but it also
separates the problem cleanly:

```text
derive 64;
derive 7;
derive their diagonal CP coupling.
```

The corpus currently supports the mechanisms but not the specific factors.
That is exactly where the next proof has to land.
