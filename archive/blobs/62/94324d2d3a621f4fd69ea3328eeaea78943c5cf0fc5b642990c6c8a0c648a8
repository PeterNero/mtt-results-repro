---
abstract: |
  We sharpen the Wilson-line route to the MTT order-448 CP character.  The
  corpus supports circle-bundle holonomy, finite subgroups of U(1) in flavor
  holonomy, phase data from Wilson-line/flat-connection parameters, and
  Wilson/orbifold projections in KK/string reductions.  Since every finite
  subgroup of U(1) is cyclic, an order-seven residual Wilson character is
  exactly the relation 7w=0.  A prime-companion scan over N=64p shows that
  p=7 is the first and by far best small prime companion to the dyadic order
  64 character for the CKM CP phase.  This does not prove the order-seven
  row, but it turns the Wilson route into a precise selection problem:
  derive a residual Z_7 Wilson/flat-connection character selected by the
  MTT projector, orbifold, or Lens x Nil flux data.
author:
- Peter Nero
date: May 2026
title: |
  Finite U(1) Wilson Selection and the Order-Seven CP Row
---

# Purpose

The Lens x Nil / Wilson scan showed that the strongest string/KK sevenfold
template is:

```text
w - f = 0,
7w = 0.
```

The corpus supports the first type of relation: flux, holonomy, Wilson-line,
and projection data can constrain phase sectors.  The missing piece is the
finite row:

```text
7w = 0.
```

This note asks: if the odd companion is a finite Wilson/holonomy subgroup of
`U(1)`, why order seven?

# Finite U(1) fact

Every finite subgroup of `U(1)` is cyclic:

```text
mu_N = {exp(2pi i k/N) : k=0,...,N-1} ~= Z_N.
```

Therefore an order-`N` residual Wilson phase is exactly the relation:

```text
Nw = 0.
```

In particular:

```text
order-seven Wilson line <=> 7w = 0.
```

This is why the row `7w=0` is the right algebraic target.

# Corpus support for the route

The corpus supports the Wilson route at the level of relation type:

- central-circle flavor degrees of freedom are line-bundle sectors over
  `S^1_cen`;
- consistency restricts central-circle flavor holonomy to a finite subgroup
  of `U(1)`;
- CKM/Yukawa phases can arise from circle-bundle holonomy;
- phase data can be encoded in Wilson-line or flat-connection parameters;
- KK reductions allow monodromies, Wilson lines, flux backgrounds, and
  orbifold/boundary projections;
- Lens x Nil flux examples give integer flux labels and isolated invariant
  loci.

The corpus does not yet state:

```text
the residual Wilson subgroup has order seven.
```

That remains the proof obligation.

# Prime companion scan

The script:

```text
odd_prime_companion_scan.py
```

tests prime-order odd companions:

```text
N = 64 p
```

where `64` is supplied by the dyadic shared-circle carry and `p` is a prime
finite Wilson/holonomy candidate.

It uses the same CKM benchmark convention as the previous phase scans.

Top ranked prime companions up to `p=127`:

```text
p   N     k    char_order  phase_error    J_error
  7   448   79        448    6.164e-06  8.920e-11
101  6464 1140       1616    1.327e-04  1.920e-09
109  6976 1230       3488    1.348e-04  1.951e-09
 73  4672  824        584    1.860e-04  2.690e-09
 67  4288  756       1072    2.155e-04  3.119e-09
```

Small prime companions:

```text
p   N     k    char_order  phase_error    J_error
  3   192   34         96    4.669e-03  6.724e-08
  5   320   56         40    8.421e-03  1.229e-07
  7   448   79        448    6.164e-06  8.920e-11
 11   704  124        176    1.281e-03  1.856e-08
 13   832  147        832    2.152e-03  3.107e-08
 17  1088  192         17    8.188e-04  1.184e-08
```

# Interpretation

If the missing odd factor is a prime finite subgroup of `U(1)`, then `p=7`
is singled out by the CP benchmark:

```text
dyadic 64 + prime 7 -> selected character 79/448.
```

It is not merely that seven appears somewhere in the corpus.  Rather:

```text
the CP phase lattice chooses p=7 as the first and best prime companion to the
dyadic order-64 row.
```

This strengthens the Wilson route:

```text
derive residual Wilson subgroup Z_7,
not arbitrary Z_p.
```

# What this does not prove

This scan does not prove MTT selects `Z_7`.

It proves a conditional:

```text
if the odd companion is a prime finite U(1) Wilson/holonomy subgroup,
then p=7 is the benchmark-selected candidate.
```

The actual proof must still derive:

```text
7w = 0
```

from one of:

- Wilson-line residual symmetry;
- orbifold/boundary projection;
- Lens x Nil flux congruence;
- finite coherent projector selection;
- torsion class in the relevant internal cohomology.

# Relation to family Z_3

The family `Z_3` holonomy is not the CP odd companion.  In the prime scan,
`p=3` gives:

```text
N=192,
phase_error=4.669e-03,
char_order=96.
```

So the known family holonomy must remain orthogonal to `chi_CP`, or else be
part of a larger ambient quotient whose selected CP character ignores the
family factor.

# Bottom line

The Wilson route is now:

```text
central-circle finite U(1) holonomy
  +
Wilson/flat-connection phase data
  +
dyadic carry Z_64
  +
benchmark-selected prime companion p=7
  =>
derive 7w=0 and ord(chi_CP)=448.
```

This is currently the cleanest string/KK-compatible route to the missing
sevenfold row.
