---
abstract: |
  We compute the pure C6 q79 holonomy block after the common-holonomy branch
  reduction.  The surviving C6 branch is no longer four independent channel
  signs.  It is a single global phase, either label 79 on all four C6 channels
  or its conjugate label 369 on all four channels.  The phase has zero flat
  action and unit modulus.  This removes another flavor-fitting knob.  It also
  shows that C6 alone cannot determine masses or mixing magnitudes; physical CP
  effects require selected nonzero C6 support matrices that interfere with
  other noncommuting blocks.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa C6 Global Phase Block
---

# Input

The common-holonomy branch-pair certificate leaves:

```text
[79, 79, 79, 79],
[369, 369, 369, 369],
```

in the channel order:

```text
u:C6, d:C6, e:C6, nuD:C6.
```

The closed exact/charge branch selects:

```text
q = 79 mod 448.
```

The inverse label is:

```text
-79 = 369 mod 448.
```

# Phase Values

The pure C6 holonomy factor is:

```text
chi_q = exp(2*pi*i*q/448).
```

For `q=79`:

```text
chi_79 = 0.4464767119915629 + 0.8947952534793661 i,
angle  = 63.48214285714286 degrees.
```

For the conjugate label:

```text
chi_369 = 0.44647671199156314 - 0.894795253479366 i,
angle   = -63.48214285714285 degrees.
```

Thus:

```text
chi_369 = conjugate(chi_79),
|chi_79| = |chi_369| = 1,
S_C6 = 0,
exp(-S_C6) = 1.
```

# Closed

This closes the pure phase block:

```text
C6 orientation signs are not independent by channel,
all surviving C6 channels share one phase per branch,
the two branches are global conjugates,
the pure flat action is zero,
the phase is unit modulus.
```

# Consequence

This is a useful tightening, but also a constraint:

```text
C6 phase alone cannot set mass or mixing magnitudes.
```

If the same global phase multiplies every selected support identically, it can
be removed by field rephasing.  Therefore physical CP requires:

```text
nonzero selected C6 support matrices,
interference with C0/C1/... blocks,
noncommutation in the resulting Yukawa/Hermitian forms.
```

# Still Open

The missing numerical data are now sharper:

```text
C6 amplitudes A_gamma,
C6 nonzero matrix support,
selected D_E/dotD orientation convention,
primitive C1 contractions,
Yukawa magnitudes.
```
