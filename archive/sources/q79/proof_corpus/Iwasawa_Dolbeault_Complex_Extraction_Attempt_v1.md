# Iwasawa Dolbeault Complex Extraction Attempt

## Purpose

This note pushes the Iwasawa Galerkin program one step further.  The previous
attempt showed that the rank-one Iwasawa seed alone cannot fill the
sector-resolved `Q,u,d,L,e,N,H` slots.  The natural next computation is to
extract the finite left-invariant Dolbeault complex from the explicit source:

```text
barpartial_E = barpartial + A^(0,1).
```

The result is important:

```text
the literal A^(0,1) matrix printed in the corpus is not integrable under the
Iwasawa barpartial rules.
```

So it cannot yet be used as the selected zero-mode complex for SM closure.

## Source Data

Use the left-invariant anti-holomorphic basis:

```text
e1 = bar(omega^1),
e2 = bar(omega^2),
e3 = bar(omega^3).
```

The Iwasawa structure gives:

```text
barpartial e1 = 0,
barpartial e2 = 0,
barpartial e3 = e1 wedge e2.
```

The corpus prints:

```text
A^(0,1) =
[[0,           mu e3,       sqrt(mu) e1],
 [0,           0,           0],
 [-sqrt(mu)e2, 0,           0]].
```

It then states that:

```text
barpartial_E^2 = 0.
```

## Literal Integrability Check

For a left-invariant holomorphic structure, the integrability gate is:

```text
barpartial A + A wedge A = 0.
```

The `(1,2)` entry of the literal matrix is:

```text
A_12 = mu e3.
```

Therefore:

```text
barpartial A_12 = mu e1 wedge e2.
```

But with the literal matrix:

```text
(A wedge A)_12 = 0.
```

So:

```text
(barpartial A + A wedge A)_12 = mu e1 wedge e2 != 0.
```

The finite linear-algebra check confirms this.  With `mu=1`, the maps have:

```text
d0: rank 3,
d1: rank 6,
d2: rank 2,
d1*d0: nonzero,
d2*d1: nonzero.
```

Thus the literal printed data do not define a cochain complex.  Any cohomology
numbers computed from those maps are invalid.

## Minimal Index-Repair Candidate

There is an obvious one-index repair candidate:

```text
move -sqrt(mu) e2 from A_31 to A_32.
```

Then:

```text
A_13 wedge A_32 = sqrt(mu)e1 wedge (-sqrt(mu)e2)
                = -mu e1 wedge e2,
```

which cancels `barpartial A_12`.

This repaired candidate is:

```text
A_repair^(0,1) =
[[0,      mu e3,      sqrt(mu) e1],
 [0,      0,          0],
 [0,     -sqrt(mu)e2, 0]].
```

For this candidate, the finite invariant Dolbeault maps satisfy:

```text
d1*d0 = 0,
d2*d1 = 0.
```

With `mu=1`, the ranks are:

```text
rank d0 = 2,
rank d1 = 5,
rank d2 = 2.
```

The invariant cohomology dimensions are:

```text
h0 = 1,
h1 = 2,
h2 = 2,
h3 = 1.
```

This candidate is useful as a diagnostic, but it is not selected.  Even if
accepted, its invariant `h1=2` is not the three-family `H^1(X,E)` input needed
by the zero-mode slot interface.

## Consequence

The extraction does not yet fill the zero-mode slots.  It reveals a sharper
fork:

```text
1. the printed A^(0,1) matrix contains a typo or missing entry;
2. the three-generation claim uses the full monad/cohomology rather than this
   literal invariant 3x3 connection alone;
3. non-invariant cohomology classes are essential.
```

Any of these can still be compatible with the wider program, but none permits
us to fill:

```text
Q,u,d,L,e,N,H
```

from the literal invariant complex today.

## What Is Closed By This Attempt

This attempt closes the following:

```text
literal A01 integrability: FAIL,
minimal one-index repair integrability: PASS as an unselected diagnostic,
minimal one-index repair invariant h1: 2,
zero-mode slot fill from literal A01: BLOCKED,
primitive C1 blocks from this data: BLOCKED.
```

## Correct Next Step

The next step is to obtain a selected holomorphic bundle complex that really
squares to zero and has the correct family data.  There are two rigorous ways:

```text
1. correct or confirm the A^(0,1) matrix in the Iwasawa source, then recompute
   the invariant cohomology;
2. extract the full monad maps f and g and compute H^1(X,E) from the actual
   monad/cohomology sequence rather than from the printed 3x3 connection.
```

Only after that can we derive the E6-to-SM sector projection maps and continue
to `dotD` and primitive C1 contractions.

## Bottom Line

We pushed the calculation as far as the current printed source allows.  The
literal invariant Dolbeault operator fails the first gate:

```text
barpartial_E^2 = 0.
```

So the current corpus does not yet contain a usable selected invariant
Dolbeault complex for the SM matrices.  This is a productive obstruction: it
shows exactly what must be corrected or supplied next.
