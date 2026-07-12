---
abstract: |
  We run a consolidated constraint battery for the surviving ambient Z_1344
  flavor carrier.  The test combines the recursive dyadic carry, the sevenfold
  finite row, the family Z_3 factor, the CKM benchmark phase, the PMNS
  quarter-turn branch, pairwise phase-sum closure, family-triviality, and
  Majorana admissibility.  The candidate passes all checks.  This supports the
  refined architecture in which the ambient carrier is Z_64 x Z_7 x Z_3 ~= Z_1344,
  while the selected CP character has effective order 448 and is separated
  from the neutral Majorana character.
author:
- Peter Nero
date: May 2026
title: |
  Ambient Z_1344 Constraint Battery for MTT Flavor CP
---

# Purpose

The current best ambient candidate is:

```text
Gamma_fl,amb ~= Z_64 x Z_7 x Z_3 ~= Z_1344.
```

The intended physical CP character is not the whole ambient carrier.  It is a
family-trivial character with effective order:

```text
ord(chi_CP)=448.
```

This note records a combined consistency test for that statement.

# Battery script

The executable check is:

```text
ambient_z1344_constraint_battery.py
```

It uses:

```text
N = 1344,
k_q  = 237,
k_l  = 1008,
k_31 = 99.
```

These are the family-trivial lifts of the selected `Z_448` labels:

```text
79, 336, 33.
```

# Finite relation matrix

The test combines:

```text
six-stage dyadic carry  -> Z_64,
sevenfold finite row    -> Z_7,
family holonomy row     -> Z_3.
```

The Smith normal form calculation gives:

```text
torsion factors: [1344]
exponent: 1344
free rank: 0
```

This verifies that the ambient product can be represented as one cyclic
carrier because:

```text
gcd(64,7)=gcd(64,3)=gcd(7,3)=1.
```

# CP labels

The selected labels have:

```text
ord(k_q)  = 448,
ord(k_l)  = 4,
ord(k_31) = 448.
```

They close under the pairwise phase-sum rule:

```text
(237 + 1008 + 99) mod 1344 = 0.
```

They are all family-trivial:

```text
237  = 0 mod 3,
1008 = 0 mod 3,
99   = 0 mod 3.
```

# Numerical check

Using the same CKM benchmark convention as the earlier scans:

```text
delta_q = 2pi * 237/1344
        = 2pi * 79/448
        = 1.107972409079.
```

The script reports:

```text
phase_error = 6.164e-06,
J_error     = 8.920e-11.
```

The lepton branch is exact:

```text
k_l = 1008 = 3N/4,
delta_l = 3pi/2 = -pi/2 mod 2pi,
ord(k_l)=4.
```

# Majorana separation

The same battery confirms:

```text
CP labels are not Majorana self-characters: PASS
trivial neutral is Majorana-admissible:     PASS
two-torsion neutral is Majorana-admissible: PASS
neutral two-torsion is family-trivial:      PASS
```

Thus the model must keep two roles separate:

```text
Gamma_CP: family-trivial order-448 CP overlap character,
Gamma_N:  trivial or two-torsion neutral real-structure character.
```

# Result

The full pass/fail block is:

```text
ambient finite torsion is Z_1344                           PASS
selected CKM character order is 448                        PASS
selected lepton branch has order 4                         PASS
lepton branch is -pi/2 mod 2pi                             PASS
pairwise phase-sum closes                                  PASS
all CP labels are family-trivial                           PASS
CP labels are not Majorana self-characters                 PASS
trivial neutral is Majorana-admissible                     PASS
two-torsion neutral is Majorana-admissible                 PASS
neutral two-torsion is family-trivial                      PASS
```

# Interpretation

This is the strongest consistency result so far.

It does not prove that MTT derives the missing sevenfold row.  It proves that
once the dyadic carry, sevenfold row, and family row are supplied, the resulting
ambient structure is internally coherent:

```text
ambient carrier:       Z_1344,
selected CP quotient:  Z_448,
family factor:         Z_3 orthogonal to chi_CP,
neutral Majorana role: k=0 or k=672.
```

# Bottom line

The candidate survives the current constraint battery.  The remaining hard
problem is now sharply isolated:

```text
derive the Z_7 row from MTT nil/Wilson/flux/projector data.
```

If that row is derived, the rest of the ambient `Z_1344` architecture already
passes the available quotient, phase, family, and Majorana compatibility tests.
