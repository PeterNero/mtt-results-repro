---
abstract: |
  We state the clean conditional theorem now supported by the MTT order-448 CP
  program.  If the recursive shared-circle sector supplies a dyadic invariant
  factor 64, if the Fu-Yau/K3 fixed sector selects the positive Mukai charge
  block K_Mukai=[[2,1],[1,4]] with Smith form [7], and if the family Z3 factor
  lies in the kernel of the CP character, then the selected CP character has
  order 448.  The theorem separates the finite abelian arithmetic, which is
  proved, from the geometric selection assumptions, which remain the true open
  work.
author:
- Peter Nero
date: May 2026
title: |
  Conditional Selection Theorem for the MTT Order-448 CP Character
---

# Purpose

This note states the theorem we can honestly prove now.

It is deliberately conditional.  The arithmetic is proved; the geometric
selection hypotheses are not yet fully proved.

# Data

Assume a dyadic relation matrix `A_64` with:

```text
SNF(A_64)=[64].
```

Assume the Mukai odd block:

```text
K_Mukai =
[[2,1],
 [1,4]],
SNF(K_Mukai)=[7].
```

Assume an orthogonal family row:

```text
A_fam=[3].
```

Define:

```text
A_sel = block_diag(A_64,K_Mukai),
A_amb = block_diag(A_64,K_Mukai,A_fam).
```

# Theorem

If:

```text
1. the flavor CP character group is the unitary dual of coker(A_sel);
2. the family factor is orthogonal to chi_CP;
3. the physical CKM/PMNS CP labels are family-trivial lifts in coker(A_amb);
```

then:

```text
Gamma_CP,min ~= Z_448,
Gamma_amb ~= Z_1344,
Gamma_amb / Z_3-family ~= Z_448,
ord(chi_CP)=448.
```

# Proof

The invariant factors are:

```text
SNF(A_64)=[64],
SNF(K_Mukai)=[7].
```

Since:

```text
gcd(64,7)=1,
```

the block diagonal selected quotient has one cyclic invariant factor:

```text
SNF(A_sel)=[448].
```

Therefore:

```text
coker(A_sel) ~= Z_448,
Hom(coker(A_sel),U(1)) ~= Z_448.
```

Adding the family row gives:

```text
SNF(A_amb)=[1344],
```

because:

```text
gcd(64,7,3)=1.
```

The quotient map:

```text
pi: Z_1344 -> Z_448
```

has kernel:

```text
ker(pi)={0,448,896} ~= Z_3.
```

Thus the family factor is precisely the kernel of the ambient-to-selected CP
map.

The CKM label:

```text
k_q=237 mod 1344
```

has:

```text
gcd(237,1344)=3,
ord(k_q)=1344/3=448.
```

Equivalently:

```text
k_q=3*79,
79 mod 448 has order 448.
```

The lepton quarter-turn and closure labels:

```text
k_l=1008=3*336,
k_31=99=3*33
```

are also family-trivial, and downstairs:

```text
79+336+33=448=0 mod 448.
```

So the selected CP character has order:

```text
448.
```

# What the theorem proves

It proves:

```text
the finite abelian quotient arithmetic,
the ambient-to-selected family quotient,
the selected order of the CP character,
the compatibility of the CKM branch, PMNS quarter-turn branch, and closure row.
```

# What the theorem assumes

It assumes:

```text
the dyadic carry is actually derived from MTT shared-circle recursion,
the Mukai charge block is actually selected by the Fu-Yau/K3 fixed sector,
the CP labels are the unitary dual of the selected finite quotient,
the family Z3 factor is physically orthogonal to CP.
```

These are now the proof obligations.

# Interpretation

This theorem is the spine of the program.

It lets the remaining work split cleanly:

```text
Z64 theorem: derive A_64 from shared-circle recursion.
Z7 theorem: derive K_Mukai from Fu-Yau/K3 Mukai charge selection.
character theorem: identify CP labels with Hom(coker A_sel,U(1)).
family theorem: show the family Z3 lies in ker(pi).
```

The two active gate papers are:

```text
Shared_Circle_Z64_Carry_Gate_Theorem_v1.md
Mukai_Charge_Character_Selection_Gate_v1.md
```

They isolate the exact remaining non-arithmetic steps.

The combined character map is now explicit in:

```text
Selected_CP_Character_Dual_Map_v1.md
selected_cp_character_dual_check.py
```

It constructs:

```text
theta_CP =
(1/64,1/32,1/16,1/8,1/4,1/2,1/7,5/7),
```

with:

```text
ord(theta_CP)=448.
```

The physical labels are:

```text
79 theta_CP,
336 theta_CP,
33 theta_CP,
```

and they close in the character group.

The remaining numerator-selection caveat is recorded in:

```text
CP_Label_Normalization_and_Overlap_Selection_Gate_v1.md
```

The conditional theorem proves the order and character architecture.  It does
not by itself prove why the CKM primitive label is `79`; that requires an
overlap/selection theorem.

# Bottom line

The arithmetic part of the MTT order-448 CP program is ready.  The unfinished
work is geometric selection and physical realization.
