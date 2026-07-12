---
abstract: |
  After auditing the original Lens-Nil appendix, we propose a repaired
  determinant-seven source using closed integral two-forms rather than the
  non-closed beta_1,beta_3 component pair.  On the Lens-Nil algebra, the closed
  two-forms u_1=e12, u_2=e13, v_1=e45, v_2=e46 support integral line-bundle
  Chern classes c1(L1)=u1+2v1+v2 and c1(L2)=u2+v1+4v2.  Their Chern character
  ch_2(L1)+ch_2(L2)=1/2(c1(L1)^2+c1(L2)^2) has exact coefficient matrix
  [[2,1],[1,4]] on the closed four-form basis u_i wedge v_j.  Thus an exact
  closed integral Lens-Nil source for the Z_7 matrix exists, but HYM/primitivity
  and MTT selection remain open.
author:
- Peter Nero
date: May 2026
title: |
  Repaired Lens-Nil Closed Flux Candidate for the Z_7 CP Row
---

# Purpose

The original Lens-Nil appendix cannot prove the determinant-seven block as
written because:

```text
beta_1,beta_3 are not closed,
F=f eta12+h sigma45 squares to beta_2, not beta_1,beta_3.
```

This note asks whether Lens-Nil can still supply the desired exact integer
matrix after repair.

The answer is:

```text
Yes, as a closed integral Chern-character candidate.
```

But not yet:

```text
Yes, as a fully admissible HYM/MTT-selected flux sector.
```

# Closed two-form basis

With the stated Lens-Nil structure equations, the following coordinate
two-forms are closed:

```text
e12, e13, e23, e45, e46, e56.
```

Choose:

```text
u1 = e12,
u2 = e13,
v1 = e45,
v2 = e46.
```

Then all four forms:

```text
u1 v1 = e1245,
u1 v2 = e1246,
u2 v1 = e1345,
u2 v2 = e1346
```

are closed.

# Integral line-bundle classes

Define two integral first Chern classes:

```text
c1(L1) = u1 + 2 v1 + v2,
c1(L2) = u2 + v1 + 4 v2.
```

Since all basis two-forms are closed:

```text
d c1(L1)=0,
d c1(L2)=0.
```

The second Chern character source is:

```text
ch_2(L1)+ch_2(L2)
= 1/2 c1(L1)^2 + 1/2 c1(L2)^2.
```

The factor `1/2` is important: for a line bundle,

```text
ch_2(L)=1/2 c1(L)^2.
```

Because two-forms commute under wedge product, this removes the raw factor `2`
from cross terms.

# Resulting matrix

Expanding gives:

```text
ch_2(L1)+ch_2(L2)
= 2 u1v1 + 1 u1v2 + 1 u2v1 + 4 u2v2.
```

So the coefficient matrix on the closed four-form basis is:

```text
K_closed =
[2 1
 1 4].
```

Smith normal form:

```text
SNF(K_closed) = [7].
```

Thus:

```text
Hom(coker K_closed, U(1)) ~= Z_7.
```

# What this repairs

This avoids both old problems:

```text
1. the forms used are closed;
2. the flux contribution is a true Chern-character expansion of integral
   line-bundle classes.
```

So the determinant-seven matrix is no longer tied to the inconsistent
`dH=W_1 beta_1+W_3 beta_3` formula.

# What remains open

This is still only a candidate.

To finish the proof, we must show:

```text
1. the line-bundle classes can be represented by admissible HYM connections
   in the Lens-Nil coherent sector;
2. primitivity/slope conditions are satisfied or can be repaired by choosing
   a stable higher-rank bundle with the same ch_2 matrix;
3. the coherent MTT selection principle actually selects this closed
   determinant-seven character matrix;
4. the family Z_3 remains orthogonal to this sector.
```

# Current value

This is a substantial salvage:

```text
the original Lens-Nil coefficient block is blocked,
but an exact closed integral Lens-Nil determinant-seven block exists.
```

The next proof step is now HYM/admissibility, not exterior-calculus consistency.

# HYM gate result

The first HYM gate check is:

```text
repaired_lens_nil_hym_gate_check.py
```

For the displayed SU(3) structure with real pairs:

```text
(1,2), (3,6), (4,5),
```

the invariant closed primitive `(1,1)` two-form space is only:

```text
span(e45 - e12).
```

Therefore the simple two-line-bundle classes above do **not** by themselves
give an invariant HYM proof.  They are closed and integral, and their `ch_2`
has the desired determinant-seven matrix, but they fail the displayed
type/primitivity gate.

This means the repair needs one of:

```text
1. a stable higher-rank bundle whose Chern-Weil representative has the same
   closed ch_2 matrix while satisfying HYM;
2. a modified admissible SU(3) structure where the required closed forms are
   type (1,1) and primitive;
3. a different Z_7 source outside this Lens-Nil flux block.
```
