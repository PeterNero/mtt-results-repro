# Iwasawa Invariant A01 Repair Obstruction

## Purpose

The selected `D_E` blocker had one remaining tempting shortcut:

```text
maybe the printed invariant A^(0,1) matrix is only missing a small term.
```

This note tests that shortcut directly. The result is a useful repair of the
proof strategy:

```text
the invariant A01 repair path should no longer be used as a proof source.
```

This does not refute the Iwasawa/monad program. It says that the selected
three-family operator must come from typed monad/Cech data or from a
non-invariant spectral/HYM construction.

## Literal Completion Search

The printed invariant data are:

```text
A_12 = e3,
A_13 = e1,
A_31 = -e2.
```

The earlier audit showed this literal matrix is not integrable:

```text
barpartial A + A wedge A != 0.
```

We now allow small signed invariant completions while preserving the printed
entries exactly. The search allows:

```text
all 3 x 3 entries,
diagonal and off-diagonal terms,
one-form labels e1,e2,e3,
coefficients +/-1,
one to four added entries.
```

The exhaustive candidate counts are:

```text
extra 1: 48
extra 2: 1104
extra 3: 16192
extra 4: 170016
```

The number of integrable completions found is:

```text
0.
```

So the printed invariant matrix is not repaired by a small signed invariant
completion that keeps the printed entries fixed.

Equivalently, the printed invariant matrix is not fixed by adding up to four signed invariant entries in this finite completion ansatz.

## Torsion-Support Search

The second question is whether another finite signed invariant torsion branch
could carry the desired three-family cohomology. We searched all signed
invariant matrices with:

```text
at least one e3 term,
diagonal and off-diagonal entries allowed,
one to five nonzero entries.
```

The integrable distributions are:

```text
1 entry: no integrable candidates
2 entries: no integrable candidates
3 entries: 48 candidates with h=(1,2,2,1)
4 entries: 384 candidates with h=(1,2,2,1)
5 entries: 960 candidates with h=(1,2,2,1)
```

In this finite ansatz:

```text
integrable + e3 support -> h1 = 2,
not h1 = 3.
```

That matches the earlier three-entry Maurer-Cartan gate and strengthens it
against diagonal signed completions.

## Consequence For Selected D_E

The invariant repair route is now retired as a current proof source:

```text
R1 corrected invariant A01: retired unless a new source supplies it.
R2 typed monad/Cech: primary route.
R3 non-invariant spectral Galerkin/HYM: fallback route.
```

This is a genuine tightening of the proof. It prevents us from treating an
unselected sparse repair as if it were the MTT-selected operator.

## What Remains

To construct the selected operator, we still need one of:

```text
typed monad sections f_i,g_i plus Cech/transition data,
or a selected non-invariant HYM/Strominger operator D_E with finite basis data.
```

The diagnostic Hodge pipeline is already ready. Once the selected source is
available, the computation is mechanical:

```text
build B_N,
assemble L_N,
compute the Riesz projector,
extract Psi_1,Psi_2,Psi_3,
then feed the dotD/C1 response interface.
```

## Verdict

This fixes the strategy, not the final selected matrix:

```text
do not continue trying to patch the invariant printed A01;
construct selected cohomology by typed monad/Cech methods,
or construct selected non-invariant spectral Galerkin data.
```

That is the correct way forward without losing rigor.
