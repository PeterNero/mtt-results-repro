---
abstract: |
  We make the selected MTT CP character explicit in the character-dual group
  of the combined dyadic carry and Mukai Z7 blocks.  The dyadic generator is
  theta_64=(1,2,4,8,16,32)/64 and the Mukai discriminant generator is
  theta_7=(1/7,5/7).  Their direct sum theta_CP=(theta_64,theta_7) solves the
  selected relation matrix and has order lcm(64,7)=448.  The physical labels
  79, 336, and 33 multiply theta_CP to give the CKM branch, the PMNS
  quarter-turn branch, and the phase-sum partner.  These labels close in the
  character group and lift to family-trivial ambient labels 237, 1008, and 99
  in Z1344.  The finite-character identification is now closed once the
  factor quotients are selected.  The Mukai character identification and
  fixed-sector MTT selection reduction are now closed once a
  Bianchi-compatible Fu-Yau/Mukai sector supplies A_P.  The remaining open
  steps are actual Z64 Hessian/kernel extraction and global Fu-Yau/Mukai
  topological-sector realization.
author:
- Peter Nero
date: May 2026
title: |
  Selected CP Character-Dual Map for the Order-448 Quotient
---

# Purpose

The previous notes proved the two factors separately:

```text
theta_64 from the shared-circle carry,
theta_7 from the Mukai discriminant group.
```

This note combines them into the actual selected CP character.

# Dyadic character

For the six-stage carry:

```text
2x_0-x_1=0,
2x_1-x_2=0,
2x_2-x_3=0,
2x_3-x_4=0,
2x_4-x_5=0,
2x_5=0,
```

the character generator is:

```text
theta_64 =
(1/64, 1/32, 1/16, 1/8, 1/4, 1/2).
```

It has order:

```text
64.
```

# Mukai character

For the Mukai block:

```text
K_Mukai =
[[2,1],
 [1,4]],
```

the discriminant/character generator is:

```text
theta_7=(1/7,5/7).
```

It has order:

```text
7.
```

# Selected CP generator

Define:

```text
theta_CP = (theta_64, theta_7).
```

Explicitly:

```text
theta_CP =
(1/64,1/32,1/16,1/8,1/4,1/2,1/7,5/7).
```

Since:

```text
gcd(64,7)=1,
```

we get:

```text
ord(theta_CP)=448.
```

# Physical labels

The selected physical labels are:

```text
CKM branch:          79 theta_CP,
PMNS quarter-turn:   336 theta_CP,
phase-sum partner:   33 theta_CP.
```

Their orders are:

```text
ord(79 theta_CP)=448,
ord(336 theta_CP)=4,
ord(33 theta_CP)=448.
```

They close because:

```text
79 + 336 + 33 = 448 = 0 mod 448.
```

Therefore:

```text
79 theta_CP + 336 theta_CP + 33 theta_CP = 0.
```

# Ambient family-trivial lift

Add the family factor:

```text
Z_3.
```

The ambient cyclic labels are:

```text
237  = 3*79,
1008 = 3*336,
99   = 3*33.
```

They are all divisible by `3`, so they are trivial on the family kernel.

Equivalently, in the product character vector:

```text
(theta_CP,0_family),
```

the family coordinate is zero.

# What is proved

```text
theta_CP solves the selected relation matrix,
theta_CP has order 448,
the physical labels are multiples of theta_CP,
the phase-sum relation closes in the character group,
the ambient lifts are family-trivial.
```

# What remains open

The remaining factor-selection work is now split:

```text
MTT must extract the Z_64 carry quotient from the actual selected
Hessian/kernel.

The global Fu-Yau/Strominger sector must supply the Mukai Z_7 quotient as
fixed Chern/Mukai data.
```

Once those quotients are supplied, the physical CP character is their unitary
dual generator by the finite-character observability theorem.  Thus the
remaining work is:

```text
theta_64 from actual shared-circle carry extraction,
theta_7 from global Fu-Yau/Mukai topological-sector realization,
```

and proving the CKM/PMNS overlap sector uses the diagonal combination
`theta_CP`.

# Executable check

The check:

```text
selected_cp_character_dual_check.py
```

verifies:

```text
SNF(selected relation matrix)=[448],
SNF(ambient relation matrix)=[1344],
ord(theta_64)=64,
ord(theta_7)=7,
ord(theta_CP)=448,
phase-sum closure,
family-trivial ambient lifts.
```

# Bottom line

The selected CP character is now explicit:

```text
chi_CP = theta_CP = (theta_64, theta_7).
```

The finite character algebra and character-identification step are complete.
The remaining proof is to extract the dyadic quotient from the actual MTT
operator and to construct/select the global Fu-Yau/Mukai sector, rather than
choosing either factor after the fact.

# Label-normalization caveat

There is one more selection layer after `theta_CP` is constructed.  The finite
group fixes the denominator/order, but it does not by itself derive the CKM
numerator `79`.  A cyclic group of order `448` has many primitive labels.

The successor note:

```text
CP_Label_Normalization_and_Overlap_Selection_Gate_v1.md
```

checks this explicitly.  With the lepton quarter-turn fixed at:

```text
l=336,
```

and phase-sum closure:

```text
q+l+r=0 mod 448,
```

there are still `192` primitive `q` labels whose partner `r` is also primitive.
The CKM/Jarlskog benchmark selects:

```text
q=79,
r=33,
```

on the chosen phase branch, but a future MTT overlap/selection theorem must
derive that numerator rather than fit it.
