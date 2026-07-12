---
abstract: |
  We carry the sevenfold candidates forward by testing small integer relation
  matrices with Smith normal form.  The results separate genuine seven-torsion
  from look-alikes.  A monodromy relation n=7c alone leaves a free phase and
  does not produce a finite character; it needs terminal closure or a finite
  Wilson/projector row.  Integer flux labels by themselves also do not produce
  seven-torsion unless they induce a congruence.  The clean sevenfold sources
  are: 7n=0, shared-circle/nil locking plus 7n=0, flux-Wilson congruence plus
  7w=0, or a direct diagonal order-448 row.  Including the already-known Z_3
  family holonomy in the same ambient quotient gives exponent 1344, so the CP
  character must either live on a separate factor or be selected to ignore the
  family factor.
author:
- Peter Nero
date: May 2026
title: |
  Sevenfold Relation Matrix Templates for MTT Flavor
---

# Purpose

The previous note identified the sevenfold problem:

```text
Find a legitimate MTT finite relation whose odd part has order 7.
```

This note turns that into explicit Smith-normal-form templates.

The associated reproducibility script is:

```text
sevenfold_relation_template_scan.py
```

# Main lesson

Not every occurrence of `7` produces a finite sevenfold character.

The relation

```text
n - 7c = 0
```

does **not** produce `Z_7`.  It leaves one free phase direction.  A finite
sevenfold character appears only after a terminal closure, Wilson-line,
orbifold, projector, or torsion row is added.

# Template scan

## Pure sevenfold row

Relation:

```text
7n = 0.
```

Smith normal form:

```text
torsion factors: [7]
exponent: 7
free rank: 0
```

This is the cleanest possible sevenfold source.

## Monodromy without terminal closure

Relation:

```text
n - 7c = 0.
```

Smith normal form:

```text
torsion factors: none
exponent: 1
free rank: 1
```

This is crucial: monodromy-by-seven does not itself give a finite quotient.
It only relates two continuous/infinite phase labels.

## Monodromy with terminal nil closure

Relations:

```text
n - 7c = 0,
n = 0.
```

Smith normal form:

```text
torsion factors: [7]
exponent: 7
free rank: 0
```

Interpretation:

```text
nil termination closes the nil generator;
the shared circle inherits sevenfold closure through the monodromy relation.
```

This is a strong candidate if the nil carrier can supply the terminal row.

## Shared-circle/nil lock plus nil seven

Relations:

```text
c - n = 0,
7n = 0.
```

Smith normal form:

```text
torsion factors: [7]
exponent: 7
free rank: 0
```

Interpretation:

```text
the CP phase lives on the shared circle but is locked to a nil sevenfold
survivor.
```

This is probably the most MTT-native sevenfold template.

## Integer flux labels alone

Relations:

```text
f = 0,
h = 0.
```

Smith normal form:

```text
torsion factors: none
exponent: 1
free rank: 0
```

This deliberately trivial example records a conceptual warning:
integer flux labels are not automatically finite phase characters.  Flux data
become relevant when they induce a congruence, a Wilson-line remnant, or a
torsion class.

## Flux-Wilson congruence

Relations:

```text
w - f = 0,
7w = 0.
```

Smith normal form:

```text
torsion factors: [7]
exponent: 7
free rank: 0
```

This is the best template for the heterotic/KK route:

```text
integer flux selection fixes an admissible Wilson-line character,
and the residual Wilson line has order seven.
```

# Interaction with the existing Z_3 family holonomy

The central-circle corpus already has a `Z_3` family holonomy.  If this is put
in the same ambient finite quotient as the sevenfold CP source, then:

```text
Z_3 x Z_7 ~= Z_21.
```

The SNF scan gives:

```text
torsion factors: [21]
exponent: 21
```

With the dyadic carry:

```text
Z_64 x Z_3 x Z_7 ~= Z_1344.
```

The scan gives:

```text
torsion factors: [1344]
exponent: 1344
```

This does not kill the `448` result.  It says that if family `Z_3` belongs to
the same ambient quotient, the CP observable must be a selected character of
order `448` inside the larger ambient group.

For example:

```text
N = 1344,
k = 237,
gcd(237,1344)=3,
ord_N(k)=1344/3=448.
```

Thus the CP character can ignore the family factor while the full carrier still
contains it.

# Combined dyadic/seven templates

The strongest dyadic candidate is the six-stage carry matrix:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0.
```

Adding a pure sevenfold row gives:

```text
torsion factors: [448]
exponent: 448
```

This remains the minimal clean candidate:

```text
Z_64 x Z_7 ~= Z_448.
```

Adding the family `Z_3` row gives:

```text
torsion factors: [1344]
exponent: 1344.
```

That is an ambient-carrier candidate, not a minimal CP quotient.  It is allowed
only if the CP character is selected to have order `448`.

# Ranking after template scan

The sevenfold routes now rank as follows.

```text
1. shared-circle/nil lock plus nil seven row        strongest MTT-native
2. flux-Wilson congruence plus order-seven Wilson   strongest string/KK route
3. monodromy plus terminal nil closure              viable if terminal row derived
4. direct diagonal order-448 row                    valid fallback
5. bare monodromy n=7c                              insufficient
6. integer flux labels without congruence           insufficient
7. dimension-seven carrier alone                    insufficient
```

# New proof obligation

The next theorem should not merely say that Lens x Nil has integer fluxes.
It must derive one of:

```text
c - n = 0, 7n = 0,
w - f = 0, 7w = 0,
n - 7c = 0, n = 0,
448e = 0,
```

or an equivalent relation matrix whose Smith normal form has an invariant
factor divisible by seven and whose selected CP character has order `448`
after combining with the dyadic row.

# Bottom line

The sevenfold candidate has advanced from a clue-list to a finite-relation
program.  The cleanest final pathway is now:

```text
dyadic shared-circle carry:        Z_64
nil/Wilson sevenfold finite row:   Z_7
selected CP character:             order 448
family Z_3, if included:           ambient factor ignored by chi_CP
```

This is stricter, more rigorous, and safer than saying "nil is on seven" or
"M-theory has X_7."
