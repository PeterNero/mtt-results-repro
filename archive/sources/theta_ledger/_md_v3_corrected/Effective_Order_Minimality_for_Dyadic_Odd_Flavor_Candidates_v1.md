---
abstract: |
  We test whether the effective order-448 CP character is uniquely tied to
  the quotient Z_64 x Z_7, or whether larger odd companions to the dyadic
  order-64 row can reproduce the same CKM phase.  A direct scan over
  N=64m shows that m=7 is the first companion that realizes the high-accuracy
  CKM branch.  Larger multiples of seven also realize the same phase, but
  only through a character whose order reduces back to 448.  Thus the
  benchmark selects an effective character order, not necessarily the full
  ambient group order.  This sharpens the claim: MTT must derive either a
  minimal quotient Z_448 (equivalently Z_64 x Z_7) or a larger finite quotient
  with a canonically selected order-448 character.
author:
- Peter Nero
date: May 2026
title: |
  Effective Order Minimality for Dyadic-Odd Flavor Candidates
---

# Purpose

The current flavor target is often written as

```text
Z_64 x Z_7 ~= Z_448.
```

That is the minimal clean presentation if the dyadic and sevenfold rows are
separate.  But the actual observable only sees a selected character.  This note
checks whether larger quotients

```text
Z_(64m)
```

can mimic the same CKM phase, and what that means for the claim.

# Reproducible check

The script

```text
dyadic_odd_factor_phase_scan.py
```

uses the same CKM benchmark convention as `complex_holonomy_benchmark_check.py`.
It scans

```text
N = 64 m,   1 <= m <= 64,
```

selects the nearest character

```text
delta_q(N,k)=2pi k/N,
```

and reports the phase error, Jarlskog error, and the order of the selected
character:

```text
ord_N(k) = N / gcd(k,N).
```

# Result

The top candidates are:

```text
m  N     k    char_order  phase_error    J_error
 7   448   79        448    6.164e-06  8.920e-11
14   896  158        448    6.164e-06  8.920e-11
21  1344  237        448    6.164e-06  8.920e-11
28  1792  316        448    6.164e-06  8.920e-11
35  2240  395        448    6.164e-06  8.920e-11
42  2688  474        448    6.164e-06  8.920e-11
49  3136  553        448    6.164e-06  8.920e-11
56  3584  632        448    6.164e-06  8.920e-11
63  4032  711        448    6.164e-06  8.920e-11
```

The small companions show why `m=7` is special as the first successful odd
companion:

```text
m  N     k    char_order  phase_error    J_error
 1    64   11         64    2.806e-02  4.173e-07
 2   128   23        128    2.103e-02  2.979e-07
 3   192   34         96    4.669e-03  6.724e-08
 4   256   45        256    3.512e-03  5.100e-08
 5   320   56         40    8.421e-03  1.229e-07
 6   384   68         96    4.669e-03  6.724e-08
 7   448   79        448    6.164e-06  8.920e-11
```

# Interpretation

The result is not:

```text
Only the ambient group Z_448 works.
```

The correct statement is:

```text
The selected character has effective order 448.
```

For `m=14`, the ambient group is `Z_896`, but the selected character is

```text
k = 158,   gcd(158,896)=2,
```

so its order is

```text
896 / 2 = 448.
```

Likewise, for every scanned multiple

```text
m = 7 r,
```

the selected character is a lift of the same rational phase

```text
79 / 448.
```

The extra ambient states do not improve the physical character.  They are
invisible unless MTT supplies additional observables that use them.

# Consequence for the quotient claim

The rigorous target should be phrased as:

```text
Gamma_fl contains a canonically selected unitary character chi_CP
with ord(chi_CP)=448.
```

If the quotient is minimal, then

```text
Gamma_fl ~= Z_448 ~= Z_64 x Z_7.
```

If the quotient is larger, then MTT must also derive a selection rule choosing
the order-448 diagonal character and explain why the remaining characters do
not enter CKM/PMNS CP.

# Relation to recursive topology

This is compatible with a recursive or profinite topology.  A recursive
central-circle tower may contain higher stages:

```text
... -> Z_(64*21) -> Z_(64*14) -> Z_(64*7).
```

But the physical CP observable can still be the finite character selected at
effective order `448`.  In that case, `Z_448` is the finite quotient seen by
the flavor sector, not necessarily the whole recursive carrier.

# Bottom line

The benchmark supports `448` as an effective character order.  It does not
force the full topology to stop at `448`, but it does force any larger or
recursive carrier to project canonically onto the same order-448 CP character.

This is a cleaner and more rigorous statement than treating `Z_448` as the
entire ambient topology.
