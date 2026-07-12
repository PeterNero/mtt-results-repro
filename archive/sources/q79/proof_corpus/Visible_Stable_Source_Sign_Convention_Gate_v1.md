---
title: "Visible Stable-Source Sign Convention Gate"
author: "Peter Nero"
date: "May 2026"
abstract: |
  After the split-line HYM no-go, the remaining visible source must be
  genuinely nonabelian stable/sheaf data or a direct Route-C solve.  This note
  fixes the sign guardrail for that route.  A stable SU(r) HYM source with
  c1=0 must have nonnegative Gauduchon pairing of c2.  Therefore the positive
  visible Chern-Weil trace row cannot be read as positive mathematical ch2.
  In the anti-Hermitian convention it must instead mean c2=+4 alpha_1 and
  mathematical ch2=-4 alpha_1.  This keeps the nonabelian route alive while
  ruling out the wrong-sign wording.
---

# Purpose

The previous packets established:

```text
positive visible Chern-Weil trace row = 4 alpha_1 in 8*pi^2 units,
no finite split line-bundle or diagonal Cartan HYM source realizes it.
```

The remaining honest source classes are:

```text
selected nonabelian stable bundle/sheaf,
or selected Route-C HYM/Strominger solve.
```

Before constructing either one, the sign convention has to be fixed.  The
stable-source target is not just a row label; stable HYM sources obey a
positivity sign.

# Stable HYM Sign

For a stable locally-free or torsion-free `SU(r)` HYM source with `c1=0`, the
standard Bogomolov/Li-Yau sign package gives:

```text
integral_X c2(E) wedge J_G >= 0,
```

where `J_G` is the selected positive Gauduchon metric form.  On the selected
Iwasawa branch:

```text
P1 = integral_X alpha_1 wedge J_G > 0.
```

Also, for `c1=0`:

```text
ch2_math(E) = -c2(E).
```

In the standard anti-Hermitian Chern-Weil convention:

```text
ch2_math(E) = -(1/(8*pi^2)) Tr(F wedge F),
c2(E)       = +(1/(8*pi^2)) Tr(F wedge F).
```

# Wrong-Sign Branch

If the positive row were read as:

```text
ch2_math(E) = +4 alpha_1,
```

then:

```text
c2(E) = -4 alpha_1,
integral_X c2(E) wedge J_G = -4 P1 < 0.
```

That violates the stable HYM sign gate.  Thus a stable nonabelian source cannot
be asked to realize positive mathematical `ch2` on `alpha_1`.

# Admissible Stable-Source Wording

The live nonabelian target is instead:

```text
(1/(8*pi^2)) Tr(F wedge F) = +4 alpha_1,
c2(E) = +4 alpha_1,
ch2_math(E) = -4 alpha_1.
```

Then:

```text
integral_X c2(E) wedge J_G = +4 P1 > 0,
```

which passes the stable-source sign gate.

# Consequence

Going forward, the old phrase:

```text
ch2 label 4 on alpha_1
```

must be read as a trace/Chern-Weil label until the selected convention is made
explicit.  For the stable source theorem, the correct mathematical target is:

```text
c1(E)=0,
c2(E)=+4 alpha_1,
ch2_math(E)=-4 alpha_1.
```

# What This Closes

This closes:

```text
the sign convention guardrail for the stable nonabelian route,
the rejection of positive mathematical ch2 as the stable-source target,
the corrected wording: positive trace row = positive c2 row.
```

It does not construct the source.

# Remaining Source Target

The next theorem must provide one of:

```text
selected nonabelian stable bundle/sheaf with c1=0 and c2=+4 alpha_1,
or selected Route-C HYM/Strominger residual for the same trace row,
```

and then derive:

```text
same-source Chern-Weil representative,
D_E,
dotD_alpha1,
Riesz/Green,
coherent projectors,
primitive C1 contractions.
```
