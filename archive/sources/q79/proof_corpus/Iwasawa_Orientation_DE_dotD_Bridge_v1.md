---
title: |
  Iwasawa Orientation to D_E/dotD Bridge
author: MTT proof reproduction program
---

# Iwasawa Orientation to D_E/dotD Bridge

The four-route torsion-label selector left a small but important ambiguity:

```text
m in {1,2}.
```

This note checks what depends on that choice and whether the current selected
operator data already choose one branch.

## Result

The current proof package reduces the orientation question to one global
conjugate pair:

```text
m=1  <->  q=79   <->  current qutrit/SU(5) orientation F,
m=2  <->  q=369  <->  conjugate qutrit/SU(5) orientation F*.
```

The two packets are:

```text
Branch A:
  m=1,
  Q,L have orientation 1,
  u,d,e,N have orientation 2,
  C6 labels are [79,79,79,79].

Branch B:
  m=2,
  Q,L have orientation 2,
  u,d,e,N have orientation 1,
  C6 labels are [369,369,369,369].
```

The finite coupling rule is the same in both packets:

```text
s_left + s_right = 0 mod 3.
```

So the two packets are not two unrelated solutions.  They are the same
nontrivial structure under global complex conjugation unless a selected
operator package breaks that equivalence.

## What Depends On The Branch

The following are orientation-sensitive:

```text
C6 holonomy phase sign,
q=79 versus q=369 CP character convention,
SU(5) qutrit transport F versus F*,
complex signs of C1/C6 interference blocks,
CP-odd observables such as the Jarlskog sign.
```

The following are not changed merely by replacing the branch by its complex
conjugate:

```text
three-family rank count,
finite invariant-pairing support,
pure flat torsion zero-action statement,
Yukawa singular values under exact antiunitary conjugation,
CKM angle magnitudes under exact antiunitary conjugation.
```

This is why the correct interpretation is:

```text
one nontrivial structure up to global conjugation,
not two independent physical universes.
```

## Why Existing Data Do Not Select Yet

The selected `D_E` source hunt is still negative.  The selected zero-mode and
`dotD` interface defines the contract, but every sector slot is still open.  The
SU(5) qutrit packet validates the finite algebra and detects orientation `F`,
but it is explicitly an unselected fixture.

Therefore the current stack cannot honestly promote `m=1` over `m=2`.

## The Required Selector

A branch-selecting operator package must provide:

```text
one selected torsion label m,
the corresponding global CP label q=79 or q=369,
sector orientations on Q,u,d,L,e,N,H,
selected D_E domains and bundle data on those oriented sectors,
dotD_alpha1 as the derivative of the same selected D_E branch,
Riesz gap, reduced Green, horizontal response, and primitive C1 contractions.
```

The key rule is:

```text
dotD_alpha1 cannot choose a sign independently.
It must be the derivative of the same selected D_E branch.
```

Once this is supplied, there are three possible rigorous outcomes:

```text
1. the selected retarded/operator package fixes m=1 and q=79;
2. the selected retarded/operator package fixes m=2 and q=369;
3. the package proves both are antiunitarily equivalent, so only CP-odd signs differ.
```

## Next Step

Route C should be extended so its residual certificate carries one of the two
branch packets above.  Then the two conjugate packets should either be run
through the existing `D_E`, Riesz, Green, and `dotD` validators, or related by a
proved antiunitary equivalence.

That is the first place where the `m=1` versus `m=2` question can become a
selected mathematical fact rather than a convention.
