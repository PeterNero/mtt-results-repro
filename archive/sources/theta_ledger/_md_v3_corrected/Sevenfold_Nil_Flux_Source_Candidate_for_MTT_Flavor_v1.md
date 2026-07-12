---
abstract: |
  We audit possible sources of the sevenfold factor in the effective
  order-448 MTT flavor quotient.  The corpus strongly supports nil
  termination, discrete survivorship, Lens x Nil flux selection, Wilson-line
  and orbifold projections, and an M-theory X_7/G_2 carrier.  It does not yet
  explicitly derive a Z_7 flavor quotient.  The strongest route is therefore
  not dimension counting but an integer flux, monodromy, Wilson-line,
  orbifold, or diagonal projector row whose Smith normal form contributes a
  factor divisible by seven.  This note records the viable candidates and
  rejects several misleading sevens.
author:
- Peter Nero
date: May 2026
title: |
  Sevenfold Nil/Flux Source Candidate for the MTT Flavor Quotient
---

# Purpose

The effective CP target needs an odd companion to the dyadic order-64
character.  The minimal successful companion in the benchmark scan is:

```text
7.
```

The task is to find a legitimate MTT source for a row of the form:

```text
7 e_n = 0
```

or a diagonal equivalent that gives a selected character of order `7` in the
odd part.

# What the corpus already supports

The corpus supports the following ingredients.

## Nil termination gives discrete survivorship

ProtoSpinor connects nil termination with quantization:

```text
continuous rebalancing fails -> isolated neutrality anchors survive.
```

This supports a finite quotient, but it does not specify `7`.

## Nil carries family/generation data

The closure-strain and central-circle material connect nil/lens/circle
geometry with family structure, Yukawa overlap restrictions, and sector
stiffness.  The explicit family holonomy already present is `Z_3`.

This supports placing flavor data in the nil/lens/circle carrier, but it does
not turn `3` families into a `Z_7` CP phase row.

## Lens x Nil flux equations select discrete loci

The heterotic flux papers give the strongest constructive precedent:

```text
X_6 = L(3,1) x (Gamma \ Nil_3),
```

with left-invariant torsional `SU(3)` data, abelian integer fluxes, and
componentwise anomaly equations.  The equations fix discrete ratios such as
`R_1/R` for integer flux data.

This is exactly the kind of machinery that could produce a sevenfold finite
row, if the integer flux/anomaly matrix has an invariant factor divisible by
`7`.

## Wilson lines, orbifolds, and monodromy can project modes

The KK and string/corner papers explicitly allow:

```text
monodromies / Wilson lines / orbifold projections.
```

These can create finite phase sectors without adding new continuous freedom.
They are live sources for the missing sevenfold row.

The action-level closure-geometry paper is especially relevant here: it says
that complex phases in Yukawas and CKM mixing arise from circle-bundle
holonomy, and that phase data can be encoded as Wilson-line parameters in the
connection `A`.  This supports looking for a finite Wilson-line character,
but does not select order seven by itself.

## M-theory supplies an X_7 carrier clue

The M-theory bridge uses:

```text
X_7 = B^6 x S^1
```

or a more general `G_2`-structure space, with shifted integral `G_4`
quantization.  It says 4D data are fixed by `X_7`, harmonic lattices, and
integral flux classes.

This is relevant carrier evidence, but dimension seven is not order seven.

# Candidate sevenfold sources

## Candidate A: nil monodromy row

The nilmanifold has nontrivial integral structure constants.  A compact
quotient can impose a finite monodromy on a central or fiber direction.

Desired output:

```text
7 e_n = 0.
```

Status: plausible, not yet derived from the current nil lattice.

## Candidate B: Lens x Nil flux/anomaly invariant factor

The componentwise anomaly system can be written as an integer relation matrix
after choosing integral bases for flux, curvature, and torsion data.

Desired output:

```text
SNF(A_LensNil) has an invariant factor divisible by 7.
```

Status: strongest concrete route, because the corpus already works with
integer fluxes and fixed discrete loci.

Current limitation: the explicit Lens x Nil equations use integer fluxes
`(f,h)` and fix the ratio `R_1/R`, but they do not yet display a finite
seven-torsion row.  The equations are evidence for discreteness and integer
selection, not a proof of `Z_7`.

## Candidate C: Wilson-line remnant

A Wilson line around the shared circle or a nil/lens cycle could have order
seven:

```text
W^7 = 1.
```

Desired output:

```text
phase sectors are identified modulo 7.
```

Status: viable if a specific cycle and gauge embedding are supplied.

This candidate is strengthened by the corpus statement that CKM phases can be
encoded in circle-holonomy/Wilson-line data.  The missing ingredient is a
specific order-seven residual Wilson line or a Wilson-line constraint whose
selected character has order seven.

## Candidate D: orbifold/discrete gauge projection

A torus/orbifold or CY-corner projection can impose a finite residual
character.  The corpus already uses orbifold/projector language as a valid
selection mechanism.

Desired output:

```text
the surviving CP character is constrained by a Z_7 residue.
```

Status: viable, but must be derived from the actual orbifold action.

## Candidate E: M-theory G_4 integrality on X_7

Shifted `G_4` quantization can generate congruence conditions.  A sevenfold
condition could arise if the relevant integral lattice or torsion class has
order seven.

Desired output:

```text
H^4(X_7,Z)_tors or the selected flux lattice contributes a 7-torsion row.
```

Status: carrier clue only until a concrete `X_7` topology is specified.

## Candidate F: direct diagonal projector row

The sevenfold factor might not appear separately.  A combined dyadic/nil/flux
projector could produce:

```text
448 e = 0.
```

or a larger finite quotient with a selected order-448 character.

Status: valid fallback, but less explanatory.

# Rejected sources

The following should not be used as a derivation of the sevenfold factor.

## Hypercharge numerator

The topology-only hypercharge solution contains a rational coefficient such as

```text
y_3 = -7/18.
```

This is not a `Z_7` holonomy quotient.

## QCD beta coefficient

The one-loop Standard Model coefficient

```text
b_3 = -7
```

is representation/RG data, not a sevenfold flavor character.

## Dimension seven by itself

The M-theory `X_7` carrier is important, but:

```text
dimension 7 != order 7.
```

It becomes relevant only if the topology, flux lattice, torsion class, or
projector relation produces seven-torsion.

# Correct proof target

The sevenfold part succeeds if we can derive one of:

```text
SNF(A_odd) contains [7],
SNF(A_total) contains an invariant factor divisible by 7,
ord(chi_odd)=7 for the selected character,
ord(chi_CP)=448 for the selected diagonal character.
```

It fails if the only evidence is the occurrence of the word or number
"seven" without a finite relation.

# Recommended next calculation

The next concrete calculation should build the integer relation matrix for
the Lens x Nil flux/anomaly example:

```text
A_LensNil =
  [integral curvature rows]
  [integral flux rows]
  [Bianchi/anomaly rows]
  [Wilson/orbifold rows, if present].
```

Then compute:

```text
SNF(A_LensNil).
```

Search not for the symbol `7`, but for:

```text
an invariant factor divisible by 7.
```

# Bottom line

The best sevenfold route is:

```text
nil/Lens x Nil/string-flux integrality
  +
monodromy/Wilson/orbifold/projector selection
  =>
7-torsion or selected order-7 character.
```

This is compatible with the corpus and with recursive/shared-circle topology,
but it remains less proven than the dyadic carry matrix.  It is now a clear
finite-relation problem rather than a numerological search for sevens.
