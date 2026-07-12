---
abstract: |
  We test the surviving ambient Z_1344 flavor carrier against the Majorana
  admissibility criterion.  The selected CP labels k_q=237, k_l=1008, and
  k_31=99 are all family-trivial and satisfy exact pairwise phase-sum closure,
  but none is a Majorana self-character.  The Majorana-admissible flat line
  weights in Z_1344 are only k=0 and k=672.  This is not a failure of the CP
  candidate; it is a necessary separation condition.  The CP overlap character
  may live in the order-448 family-orthogonal subsystem, while a right-handed
  neutral Majorana mass must live in a trivial, order-two, real, or pseudo-real
  neutral sector.
author:
- Peter Nero
date: May 2026
title: |
  Ambient Z_1344 Majorana and CP Compatibility Check
---

# Purpose

The current surviving ambient carrier is:

```text
Z_64 x Z_7 x Z_3 ~= Z_1344.
```

The selected CP character is required to ignore the family `Z_3` factor.
This note checks whether that same character can also be used as a Majorana
neutral mass character.

# Majorana criterion

For a flat character label `k` in `Z_N`, a Majorana self-identification is
allowed only if:

```text
2k = 0 mod N.
```

For `N=1344`, this gives:

```text
k = 0,
k = 672.
```

These are the only Majorana-admissible flat line weights in the ambient cyclic
presentation.

# Selected CP labels

The family-orthogonal CP labels are:

```text
k_q  = 237,
k_l  = 1008,
k_31 = 99.
```

They satisfy:

```text
(k_q+k_l+k_31) mod 1344 = 0.
```

They are all family-trivial:

```text
237 = 0 mod 3,
1008 = 0 mod 3,
99 = 0 mod 3.
```

Their orders are:

```text
ord(k_q)  = 448,
ord(k_l)  = 4,
ord(k_31) = 448.
```

# Majorana check

The script:

```text
ambient_z1344_majorana_check.py
```

reports:

```text
CKM CP k_q                 k= 237 order=448 Majorana_allowed=False
PMNS quarter-turn k_l      k=1008 order=4   Majorana_allowed=False
phase-sum partner k_31     k=  99 order=448 Majorana_allowed=False
trivial neutral            k=   0 order=1   Majorana_allowed=True
ambient two-torsion        k= 672 order=2   Majorana_allowed=True
```

# Interpretation

The CP labels should **not** be reused as Majorana mass characters.

This is not a contradiction.  It is the expected separation:

```text
CP overlap characters: order-448 family-trivial subsystem,
Majorana neutral character: trivial or two-torsion neutral subsystem.
```

The seesaw benchmark remains admissible only if the neutral sector uses:

```text
k_N = 0
```

or

```text
k_N = 672
```

or a higher-rank real/pseudo-real neutral bundle whose determinant satisfies
the same self-conjugacy condition.

# Constraint on future model building

The model must not identify:

```text
chi_CP = chi_Majorana.
```

Instead it should factor the flavor carrier into at least two roles:

```text
Gamma_fl -> Gamma_CP      for pairwise CP overlap phases,
Gamma_fl -> Gamma_N       for neutral real structure.
```

In the ambient `Z_1344` presentation:

```text
Gamma_CP sees k = 237,1008,99,
Gamma_N sees k = 0 or 672.
```

# Bottom line

The ambient `Z_1344` candidate passes the CP/family tests but imposes a clear
Majorana separation:

```text
CP character: family-trivial, not self-conjugate;
Majorana character: family-trivial, self-conjugate, k=0 or k=672.
```

This is exactly the right kind of constraint.  It prevents accidental reuse of
the CP phase as a neutrino Majorana mass character and keeps the no-proxy
program honest.
