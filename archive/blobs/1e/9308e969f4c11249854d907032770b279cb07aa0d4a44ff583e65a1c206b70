---
abstract: |
  We test whether the proposed order-448 CP character survives when the
  already-derived Z_3 family holonomy is included in the same ambient finite
  carrier.  In the cyclic presentation Z_(64 p 3), requiring the CP character
  to be trivial on the family Z_3 factor amounts to selecting characters with
  label k divisible by 3.  A scan over odd prime companions p shows that p=7
  remains the top candidate: in Z_1344 the family-trivial lift k=237 has
  character order 448 and the same CKM phase error 6.164e-06.  The PMNS
  quarter-turn is also family-trivial: k_l=1008 gives -pi/2 mod 2pi and has
  character order 4.  Thus the family Z_3 can live in the ambient carrier
  without contaminating the selected CP character.
author:
- Peter Nero
date: May 2026
title: |
  Family-Orthogonal CP Character in the Ambient Z_1344 Carrier
---

# Purpose

The corpus already contains a central-circle family holonomy:

```text
Z_3.
```

The CP candidate needs an effective order-448 character:

```text
Z_64 x Z_7 ~= Z_448.
```

If both live in one ambient finite carrier, the natural product is:

```text
Z_64 x Z_7 x Z_3 ~= Z_1344.
```

This note tests whether the CP character can remain orthogonal to the family
factor.

# Family-trivial character condition

Use the cyclic ambient presentation:

```text
Z_(64 p 3).
```

The final factor `3` represents family holonomy.  A CP character that ignores
the family factor must be lifted from the quotient:

```text
Z_(64 p).
```

In the cyclic presentation this is implemented by:

```text
k = 0 mod 3.
```

The scan script is:

```text
family_orthogonal_cp_character_scan.py
```

# Scan result

For prime companions `p <= 127`, the top results are:

```text
p   N      k     char_order  phase_error    J_error
  7   1344   237        448    6.164e-06  8.920e-11
101  19392  3420       1616    1.327e-04  1.920e-09
109  20928  3690       3488    1.348e-04  1.951e-09
 73  14016  2472        584    1.860e-04  2.690e-09
 67  12864  2268       1072    2.155e-04  3.119e-09
```

Small prime companions:

```text
p   N      k     char_order  phase_error    J_error
  3    576   102         96    4.669e-03  6.724e-08
  5    960   168         40    8.421e-03  1.229e-07
  7   1344   237        448    6.164e-06  8.920e-11
 11   2112   372        176    1.281e-03  1.856e-08
 13   2496   441        832    2.152e-03  3.107e-08
```

# Interpretation

The family factor does not spoil the CP character.

For `p=7`:

```text
N = 64 * 7 * 3 = 1344,
k_q = 237 = 3 * 79,
gcd(237,1344)=3,
ord_N(k_q)=1344/3=448.
```

The phase is:

```text
2pi * 237/1344 = 2pi * 79/448.
```

So the ambient carrier sees `Z_1344`, while the CP observable sees exactly the
same order-448 character.

# Lepton quarter-turn check

The PMNS branch also survives the family-trivial lift.  In `Z_1344`:

```text
k_l = 1008,
2pi*k_l/1344 = 3pi/2 = -pi/2 mod 2pi,
k_l = 0 mod 3,
ord_N(k_l)=4.
```

Thus the lepton quarter-turn remains exact and family-orthogonal.

# Pairwise phase-sum closure

The topology-only phase-sum rule also survives:

```text
k_q  = 237,
k_l  = 1008,
k_31 = -(k_q+k_l) mod 1344 = 99.
```

Then:

```text
(k_q + k_l + k_31) mod 1344 = 0.
```

All three labels are family-trivial:

```text
237 = 0 mod 3,
1008 = 0 mod 3,
99 = 0 mod 3.
```

Their character orders are:

```text
ord(k_q)  = 448,
ord(k_l)  = 4,
ord(k_31) = 448.
```

Thus the pairwise line-bundle closure can be imposed inside the ambient
`Z_1344` carrier without activating the family `Z_3` factor.

# Consequence

This validates the refined statement:

```text
Gamma_fl may contain the family Z_3 factor,
but chi_CP factors through the quotient that ignores family Z_3.
```

Equivalently:

```text
Gamma_fl ~= Z_64 x Z_7 x Z_3
```

is compatible with:

```text
ord(chi_CP)=448.
```

# Bottom line

The family `Z_3` is not lost and does not compete with the sevenfold CP row.
It can live in the ambient carrier, while the selected CP character remains
family-trivial:

```text
Z_1344 ambient carrier,
Z_448 CP character,
Z_3 family character orthogonal to chi_CP.
```

This is the cleanest reconciliation of the known family holonomy with the
order-448 CP candidate.
