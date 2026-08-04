---
abstract: |
  We make explicit the quotient map from the ambient Z_1344 carrier to the
  selected order-448 CP quotient.  In the cyclic presentation of
  Z_64 x Z_7 x Z_3, the family subgroup is the kernel of pi: Z_1344 -> Z_448,
  pi(x)=x mod 448.  An ambient character descends to the selected CP quotient
  exactly when its label is divisible by 3.  The labels k_q=237, k_l=1008,
  and k_31=99 are therefore pullbacks of the Z_448 labels 79, 336, and 33.
  This formalizes the claim that MTT may keep the family Z_3 in the ambient
  topology while the CP observable sees the finite quotient actually selected.
author:
- Peter Nero
date: May 2026
title: |
  Ambient-to-Selected Z_448 CP Quotient Map
---

# Purpose

The current architecture is:

```text
Z_64 x Z_7 x Z_3 ~= Z_1344.
```

The physical CP character should ignore the family `Z_3` factor and see:

```text
Z_64 x Z_7 ~= Z_448.
```

This note writes the quotient map explicitly.

# Quotient map

Use the cyclic presentation:

```text
Z_1344.
```

Define:

```text
pi: Z_1344 -> Z_448,
pi(x) = x mod 448.
```

The kernel is:

```text
ker(pi) = {0,448,896}.
```

This is exactly the order-three family subgroup.  Under the Chinese remainder
identification:

```text
Z_1344 ~= Z_64 x Z_7 x Z_3,
```

the element `448` is:

```text
448 = 0 mod 64,
448 = 0 mod 7,
448 = 1 mod 3.
```

So quotienting by `ker(pi)` removes only the family direction.

# Character descent criterion

An ambient character label `k` defines:

```text
chi_k(x) = exp(2pi i kx/1344).
```

It descends to `Z_448` exactly when it is trivial on the kernel:

```text
chi_k(448)=1.
```

This is equivalent to:

```text
exp(2pi i k/3)=1,
```

or:

```text
k = 0 mod 3.
```

Therefore family-trivial ambient labels are precisely pullbacks:

```text
k = 3r,
chi_k = pi^*(chi_r),
r in Z_448.
```

# CP labels

The selected labels satisfy the criterion:

```text
k_q  = 237  = 3*79,
k_l  = 1008 = 3*336,
k_31 = 99   = 3*33.
```

So the actual selected `Z_448` labels are:

```text
r_q  = 79,
r_l  = 336,
r_31 = 33.
```

They close both upstairs and downstairs:

```text
(237 + 1008 + 99) mod 1344 = 0,
(79 + 336 + 33) mod 448 = 0.
```

Their orders are preserved:

```text
ord_1344(237)  = ord_448(79)  = 448,
ord_1344(1008) = ord_448(336) = 4,
ord_1344(99)   = ord_448(33)  = 448.
```

# Reproducible check

The checker:

```text
ambient_to_selected_cp_quotient_map.py
```

reports:

```text
CKM CP             ambient k= 237 -> CP r= 79 order=448 pullback=True same_order=True kernel_trivial=True
PMNS quarter-turn  ambient k=1008 -> CP r=336 order=  4 pullback=True same_order=True kernel_trivial=True
phase-sum partner  ambient k=  99 -> CP r= 33 order=448 pullback=True same_order=True kernel_trivial=True
```

# Interpretation

This resolves the apparent tension:

```text
The ambient topology can contain Z_1344,
while the CP observable sees the selected quotient Z_448.
```

So the target statement should be:

```text
MTT selects a family-trivial CP character factoring through Z_448.
```

not:

```text
the full flavor topology must be exactly Z_448.
```

# Bottom line

The `Z_448` candidate has not been lost.  It has been localized:

```text
Z_448 = Z_1344 / Z_3-family.
```

The remaining proof obligation is to derive the rows that produce the ambient
carrier, especially the sevenfold finite row.  Once the ambient carrier exists,
the quotient map to the selected CP character is explicit and constraint-clean.
