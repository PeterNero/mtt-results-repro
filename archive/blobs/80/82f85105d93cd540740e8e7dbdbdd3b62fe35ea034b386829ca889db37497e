# Invariant Maurer-Cartan Torsion Branch Gate for Iwasawa A01

## Purpose

The corrected-A01 scan found sparse integrable `h1=3` candidates, but all of
them avoided the Iwasawa torsion form `e3`.  This note checks the opposite
route: keep the torsion direction and ask whether the finite invariant
connection route can still supply three families.

## Invariant Maurer-Cartan Equations

For a left-invariant bundle connection

```text
A = A1 e1 + A2 e2 + A3 e3
```

with

```text
barpartial e1 = 0,
barpartial e2 = 0,
barpartial e3 = e1 wedge e2,
```

integrability is equivalent to

```text
A3 + [A1,A2] = 0,
[A1,A3] = 0,
[A2,A3] = 0.
```

So any nonzero `e3` term is not free: it must be a central commutator of the
closed-form matrices `A1,A2`.  The natural torsion-retaining correction is the
three-dimensional Heisenberg pattern

```text
A1 = E12,
A2 = E23,
A3 = -E13.
```

This is integrable because `[E12,E23]=E13`.

## Cohomology of the Heisenberg Pattern

For the canonical Heisenberg pattern, the finite invariant Dolbeault maps have
ranks

```text
rank D0 = 2,
rank D1 = 5,
rank D2 = 2,
```

and hence

```text
(h0,h1,h2,h3) = (1,2,2,1).
```

Thus the most natural torsion-preserving finite repair lands on the same
cohomology dimensions as the earlier one-index diagnostic repair: it is
integrable, but it is not a three-family invariant complex.

## Exhaustive Three-Entry Torsion-Support Scan

We also scan the same finite ansatz used in the corrected-A01 candidate scan:

```text
matrix slots: off-diagonal 3 x 3 entries,
form labels: e1,e2,e3,
coefficients: +/- 1,
nonzero entries: exactly three.
```

Restricting to candidates with at least one `e3` entry, the only integrable
form multiset is

```text
(e1,e2,e3),
```

with

```text
48 candidates.
```

Every one of those integrable torsion-support candidates has

```text
(h0,h1,h2,h3) = (1,2,2,1).
```

There are no integrable three-entry signed torsion-support candidates with
`h1=3`.

## Consequence

Within this finite invariant ansatz, the corrected-connection route bifurcates:

```text
closed-form degenerate branches can give h1=3, but they drop e3;
torsion-support branches keep e3, but give h1=2.
```

That is a strong diagnostic.  It does not prove that every possible selected
Iwasawa bundle has `h1 != 3`; it proves that the simple left-invariant
three-entry correction route cannot provide the selected three-family basis.

The proof should therefore move to one of the stronger inputs:

1. a corrected selected `A^(0,1)` with more structure than the three-entry
   invariant ansatz;
2. explicit typed monad maps `f,g` and the resulting cohomology sequence;
3. non-invariant modes selected by the full HYM/Strominger operator.

Until one of those is supplied, the torsion-preserving finite invariant branch
supports only an integrable two-family invariant cohomology, not SM closure.
