# Corrected A01 Candidate Scan for the Iwasawa Three-Family Complex

## Purpose

The previous Dolbeault extraction showed that the printed Iwasawa connection

```text
A_12 = e3,
A_13 = e1,
A_31 = -e2
```

is not integrable:

```text
(barpartial A + A wedge A)_12 = e1 wedge e2.
```

It also found a minimal one-index diagnostic repair, but that repair has
invariant cohomology

```text
(h0,h1,h2,h3) = (1,2,2,1),
```

not three families.  This note asks whether a nearby sparse corrected
left-invariant `A^(0,1)` could recover an integrable complex with `h1=3`.

## Finite Search Space

We scan the following deliberately small space:

```text
matrix slots: all off-diagonal entries A_ij in a 3 x 3 matrix,
form labels: e1, e2, e3,
coefficients: +/- 1,
sparsity: exactly three nonzero entries.
```

Thus there are

```text
choose(18,3) * 2^3 = 6528
```

candidate sparse signed connections.  For each candidate we construct the
finite invariant Dolbeault maps

```text
D_p : C^3 tensor Lambda^p <e1,e2,e3>
      -> C^3 tensor Lambda^(p+1) <e1,e2,e3>
```

using

```text
barpartial e1 = 0,
barpartial e2 = 0,
barpartial e3 = e1 wedge e2.
```

We retain only candidates with

```text
D_1 D_0 = 0,
D_2 D_1 = 0.
```

## Scan Result

The integrable candidates have the following invariant cohomology distribution:

```text
(h0,h1,h2,h3) = (1,2,2,1): 240 candidates
(h0,h1,h2,h3) = (1,3,3,1): 192 candidates
(h0,h1,h2,h3) = (1,4,5,2):  96 candidates
(h0,h1,h2,h3) = (2,5,4,1):  96 candidates
(h0,h1,h2,h3) = (0,0,0,0):  32 candidates
```

So `h1=3` candidates exist in the sparse invariant ansatz.

However, every `h1=3` candidate uses only the closed forms `e1,e2`; none uses
the torsion form `e3`.  The form multisets are exactly:

```text
(e1,e1,e1): 48 candidates
(e1,e1,e2): 48 candidates
(e1,e2,e2): 48 candidates
(e2,e2,e2): 48 candidates
```

There are no integrable `h1=3` candidates whose three nonzero entries use
`e1,e2,e3` once each.

## Distance from the Printed Matrix

Among the `h1=3` candidates, the minimum support symmetric distance from the
printed source support is

```text
4.
```

For two three-entry supports, distance `2` would mean a one-entry support
repair.  Distance `4` means the nearest `h1=3` candidates keep only one of the
three printed support entries.

Thus the desired three-family answer is not obtained by changing one printed
entry, moving the lower-left entry, or flipping a sign.

## Example Candidate, Not Selected

One simple integrable candidate is

```text
A_12 = e1,
A_13 = e1,
A_23 = e1.
```

It has

```text
(h0,h1,h2,h3) = (1,3,3,1).
```

But this candidate is not selected by the corpus.  It is also too degenerate
to inherit the printed Iwasawa torsion/flux role, because it uses only the
closed form `e1` and never the nontrivial `e3` direction.

## Consequence

The scan changes the status of the corrected-connection route:

```text
existence of sparse integrable h1=3 candidates: yes,
unique correction of printed A^(0,1): no,
one-entry repair to h1=3: no,
torsion-form e3 retained in h1=3 sparse candidates: no,
selected SM zero-mode basis from this scan: no.
```

Therefore the proof should not silently replace the printed matrix by a nearby
candidate.  The rigorous forward path is unchanged but sharper:

1. supply a corrected selected `A^(0,1)` from the source theory and verify it;
2. or supply the typed monad maps `f,g` and compute `H^1(X,E)` from the actual
   monad/cohomology sequence.

Until one of these is supplied, the Iwasawa route gives a rank-one E6 Yukawa
seed and topological net chirality support, not full selected SM matrices.
