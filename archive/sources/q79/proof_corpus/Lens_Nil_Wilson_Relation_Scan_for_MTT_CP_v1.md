---
abstract: |
  We carry the sevenfold MTT CP candidates one step closer to execution by
  scanning Lens x Nil / Wilson-line relation matrices with explicit generators
  for the shared circle, nil survivor, Wilson phase, and flux label.  The scan
  confirms that corpus-supported relation types such as flux integrality,
  shared-circle/nil locking, Wilson-flux congruence, and bare monodromy do not
  by themselves create finite seven-torsion.  A sevenfold CP factor appears
  only when one adds a genuine finite row: nil seven, Wilson seven, or terminal
  nil closure.  When any of these successful sevenfold templates is combined
  with the six-stage dyadic carry, the torsion contains [448].  Including the
  known Z_3 family holonomy enlarges the ambient torsion to [1344], while a
  selected CP character of order 448 remains available.
author:
- Peter Nero
date: May 2026
title: |
  Lens x Nil / Wilson Relation Scan for the MTT CP Character
---

# Purpose

This note moves from abstract sevenfold templates to a more physical generator
set suggested by the corpus:

```text
c  shared central-circle phase,
n  nil survivor / nil terminal phase,
w  Wilson-line phase,
f  integer flux label reduced to a phase congruence,
z  already-known family Z_3 character.
```

The associated reproducibility script is:

```text
lens_nil_wilson_relation_scan.py
```

# Corpus-supported relation types

The corpus supports the following relation *types*:

- central-circle phase holonomy;
- finite subgroup of `U(1)` for flavor holonomy;
- CKM/Yukawa phases from circle-holonomy/Wilson-line data;
- Lens x Nil flux quantization and isolated integer-flux loci;
- monodromies, Wilson lines, and orbifold projections in KK/string reductions;
- nil termination and discrete survivorship.

The corpus does **not** yet provide an explicit:

```text
Z_7,
L(7,*),
order-seven Wilson line,
seven-torsion class,
or mod-7 congruence.
```

Therefore the order-seven row remains the new hypothesis to derive.

# Scan results

## Flux labels alone

Relation:

```text
f = 0.
```

Result:

```text
torsion factors: none
free rank: 3.
```

Interpretation:

```text
flux integrality labels admissible sectors but does not itself create a
sevenfold phase character.
```

## Shared-circle/nil lock alone

Relation:

```text
c - n = 0.
```

Result:

```text
torsion factors: none
free rank: 3.
```

Interpretation:

```text
locking c and n places the CP phase in the right carrier, but no finite
quotient appears until a terminal/finiteness row is added.
```

## Wilson-flux congruence alone

Relation:

```text
w - f = 0.
```

Result:

```text
torsion factors: none
free rank: 3.
```

Interpretation:

```text
flux can select or constrain Wilson data, but a finite Wilson order is still
needed.
```

## Nil monodromy alone

Relation:

```text
n - 7c = 0.
```

Result:

```text
torsion factors: none
free rank: 3.
```

Interpretation:

```text
bare monodromy is not enough.  This candidate remains downgraded as a
standalone route.
```

# Successful sevenfold templates

## Shared-circle/nil lock plus nil seven

Relations:

```text
c - n = 0,
7n = 0.
```

Result:

```text
torsion factors: [7]
exponent: 7.
```

This is the strongest MTT-native sevenfold hypothesis.  It says the CP phase
lives on the shared circle but is finitely closed by nil survivorship.

## Wilson-flux congruence plus Wilson seven

Relations:

```text
w - f = 0,
7w = 0.
```

Result:

```text
torsion factors: [7]
exponent: 7.
```

This is the strongest string/KK route.  It says integer flux selection fixes an
admissible Wilson character, and the residual Wilson line has order seven.

The finite-`U(1)` Wilson scan strengthens this route.  Since every finite
subgroup of `U(1)` is cyclic, an order-`p` residual Wilson subgroup is a row
`pw=0`.  Scanning prime companions `N=64p` shows that `p=7` is the first and
best small prime companion to the dyadic order-64 row:

```text
p=7, N=448, k=79, phase_error=6.164e-06, J_error=8.920e-11.
```

Thus the Wilson route has a quantitative target:

```text
derive residual Wilson subgroup Z_7, not arbitrary Z_p.
```

## Nil monodromy plus terminal nil closure

Relations:

```text
n - 7c = 0,
n = 0.
```

Result:

```text
torsion factors: [7]
exponent: 7.
```

This rescues the monodromy candidate, but only with a terminal nil closure row.

# Combined with dyadic carry

When each successful sevenfold template is combined with the six-stage dyadic
carry, the scan gives:

```text
dyadic + nil lock/seven       torsion factors: [448]
dyadic + Wilson-flux/seven    torsion factors: [448]
dyadic + monodromy/terminal   torsion factors: [448]
```

The free ranks in the script output come from unused continuous generators in
the template basis.  They are not part of the finite selected CP character.
The finite torsion part relevant to CP is the `[448]` factor.

# Family Z_3 ambient check

Adding the known family holonomy:

```text
z: 3z = 0
```

to the dyadic plus sevenfold carrier gives:

```text
torsion factors: [1344]
exponent: 1344.
```

The selected CP character can still have order `448`.  For instance:

```text
N = 1344,
k = 237,
gcd(k,N)=3,
ord_N(k)=448.
```

Thus the full ambient carrier may include family `Z_3`, while `chi_CP`
projects past it.

# Ranking after this scan

The viable sevenfold routes now rank:

```text
1. c - n = 0, 7n = 0        shared-circle/nil finite closure
2. w - f = 0, 7w = 0        flux-selected order-seven Wilson line
3. n - 7c = 0, n = 0        monodromy plus terminal nil closure
4. direct 448e = 0          diagonal fallback
```

Downgraded or rejected as standalone:

```text
f = 0                       flux label only
c - n = 0                   lock only
w - f = 0                   congruence only
n - 7c = 0                  bare monodromy
dimension seven             carrier clue only
hypercharge/beta seven      unrelated numerology
```

# New proof target

The next proof should derive one of the successful finite rows from actual MTT
data:

```text
7n = 0
```

from nil terminal survivorship, or

```text
7w = 0
```

from Wilson/orbifold/flux selection, or

```text
n = 0
```

as terminal closure in the monodromy template.

Without one of those rows, there is no sevenfold CP factor.

# Bottom line

We now know exactly what must be found:

```text
not merely flux,
not merely monodromy,
not merely nil,
but a finite order-seven row tied to the CP phase carrier.
```

Once that row is derived, the dyadic carry matrix immediately lifts it to the
effective order-448 CP character.
