---
title: "Visible Twisted D7 Equivariant Embedding Selector"
author: "Peter Nero"
date: "May 2026"
abstract: |
  The qutrit-symmetry selector reduced the twisted D7 choice to S3 under a
  symmetry-preserving embedding rule.  This note closes that selector-level
  rule using the MTT requirement that survivor labels be symmetry-compatible
  and that finite filters act on geometric content rather than coordinate
  artifacts.  Without an extra selected source that breaks the qutrit
  clock/shift exchange symmetry, the selected F3^2 active plane must embed in
  the unique equal-scale CY coordinate pair T1,T2.  Hence the minimal
  equivariant twisted D7 stack is S3.  The selected S3 Deligne/Cech or
  worldvolume-flux source remains open.
---

# Selector Principle

The corpus supplies two general admissibility principles:

```text
representation quantization = symmetry-compatible Lens survivor labeling,
filter geometric content, not coordinate artifacts.
```

It also requires nontrivial automorphism structure of descriptive data and
local overlap maps.  Therefore a branch selector cannot break an unbroken
finite automorphism merely by naming coordinates.  It needs either:

```text
an equivariant/natural embedding,
```

or:

```text
a selected source that explicitly breaks the symmetry.
```

# Application To The Qutrit Pair

The selected finite data supplies:

```text
clock line <e1>,
shift line <e2>,
Fourier transport exchanging clock and shift up to global orientation.
```

The executed CY corner supplies:

```text
t1 = t2,
t3 distinct.
```

Thus the only coordinate exchange symmetry compatible with the executed metric
is:

```text
T1 <-> T2.
```

The minimal equivariant embedding of the qutrit active plane is therefore:

```text
{e1,e2} -> {T1,T2}.
```

The finite twisted Chan-Paton rescue enumeration then gives:

```text
e1 -> T1, e2 -> T2  => twisted D7 = S3,
e1 -> T2, e2 -> T1  => twisted D7 = S3.
```

# Result

At selector level:

```text
minimal equivariant twisted D7 stack = S3.
```

The alternatives:

```text
S1 or S2
```

are not logically impossible, but they now require an extra selected source
that explicitly breaks clock/shift exchange symmetry and justifies embedding
one qutrit generator along T3.

# Remaining Work

This closes only the minimal equivariant selector.  It does not construct:

```text
selected S3 Deligne/Cech source,
selected S3 worldvolume flux or twisted Chan-Paton source,
Freed-Witten verification for that source,
visible operator source,
projector retention,
D_E, dotD, C1 contractions,
SM closure.
```

The next proof object is now sharply:

```text
selected S3 source packet.
```
