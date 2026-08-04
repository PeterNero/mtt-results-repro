---
abstract: |
  We formalize what it means to replace the Z_448 CP benchmark by the finite
  quotient actually selected by Modal Triplet Theory.  A derived quotient must
  be evaluated before Yukawa or phase fitting.  We define two tests: a
  Jarlskog-only test, which has a sine ambiguity, and a phase-branch test,
  which matches the CKM benchmark phase itself.  Scanning cyclic quotients
  Z_N up to N=1024 with exact leptonic -pi/2 available when N is divisible by
  four, Z_448 and its multiple Z_896 give the best phase-branch match to the
  CKM target.  Smaller quotients such as Z_68 remain useful coarse
  replacements, while Z_112, Z_224, Z_336, and Z_672 are significantly worse
  on the phase branch.  This does not derive Z_448; it gives an objective
  acceptance test for whatever finite quotient the recursive/shared-circle
  MTT calculation actually selects.
author:
- Peter Nero
date: May 2026
title: |
  Finite Quotient Replacement Criteria for MTT Flavor CP
---

# Purpose

The phrase

```text
replace Z_448 with the finite quotient MTT actually selects
```

means that the finite character group must come from the recursive
shared-circle, bundle, flux, nil, orbifold, and projector data before we compare
with CKM/PMNS.

This note gives the comparison rule.  Once a candidate finite quotient is
derived, we can ask:

1. does it contain a character approximating the CKM CP phase?
2. does it contain a character giving the leptonic benchmark phase
   `-pi/2`, or an acceptable replacement?
3. does it support the phase-sum rule?
4. does it do so without entry-local phase fitting?

# CKM benchmark branch

Using the corrected CKM benchmark angles

```text
s12 = 0.2250,
s23 = 0.0411,
s13 = 0.0036,
```

and target

```text
J_CKM = 2.9e-5,
```

the benchmark phase branch is

```text
delta_q = 1.107978573420 rad.
```

This number follows from

```text
J = c12 c23 c13^2 s12 s23 s13 sin(delta_q).
```

There is a sine ambiguity: `delta_q` and `pi - delta_q` give the same Jarlskog
invariant.  Therefore a quotient can pass a Jarlskog-only test while failing
the intended phase-branch test.

# Replacement tests

For a cyclic quotient `Z_N`, allowed phases are

```text
delta = 2 pi k / N.
```

## Test A: Jarlskog-only

Minimize

```text
|J(delta) - J_target|.
```

This is useful if only the CP-odd invariant is being tested.  It is weaker
because it accepts both sine branches.

## Test B: phase-branch

Minimize

```text
|delta - delta_q|.
```

This is stricter and should be used when the CKM phase convention is part of
the benchmark.

## Leptonic benchmark

The illustrative leptonic benchmark is

```text
delta_l = -pi/2.
```

A cyclic quotient gives this exactly when `N` is divisible by `4`.

# Scan result

The script

```text
finite_quotient_replacement_search.py
```

scans cyclic quotients up to `N=1024`.

The best phase-branch cyclic quotients with exact `-pi/2` are:

```text
N     k_q   delta_q       phase error     J_CKM
448    79   1.107972409   6.164e-06      2.89999108e-05
896   158   1.107972409   6.164e-06      2.89999108e-05
964   170   1.108030604   5.203e-05      2.90007528e-05
828   146   1.107904656   7.392e-05      2.89989303e-05
516    91   1.108081130   1.026e-04      2.90014838e-05
380    67   1.107824778   1.538e-04      2.89977742e-05
760   134   1.107824778   1.538e-04      2.89977742e-05
584   103   1.108164532   1.860e-04      2.90026903e-05
```

Thus, among cyclic quotients up to `1024`, `Z_448` remains the best small
phase-branch match with exact `-pi/2`, and `Z_896` is the immediate multiple
with the same effective phase.

# Selected comparison orders

Some relevant candidate orders behave as follows:

```text
N=68:   k_q=12,  phase error=8.188e-04, J error=1.184e-08
N=112:  k_q=20,  phase error=1.402e-02, J error=2.000e-07
N=224:  k_q=40,  phase error=1.402e-02, J error=2.000e-07
N=336:  k_q=59,  phase error=4.681e-03, J error=6.805e-08
N=448:  k_q=79,  phase error=6.164e-06, J error=8.920e-11
N=672:  k_q=119, phase error=4.669e-03, J error=6.724e-08
N=896:  k_q=158, phase error=6.164e-06, J error=8.920e-11
```

`Z_68` is a respectable coarse quotient.  `Z_448` is much sharper.  Several
orders that might look plausible from divisibility alone are worse once the
actual phase branch is imposed.

# Meaning for MTT

If MTT derives a finite quotient `Gamma_fl`, the decision rule is:

- if `Gamma_fl` contains `Z_448` or an equivalent cyclic subsystem, the current
  finite CP benchmark survives essentially unchanged;
- if it contains `Z_896`, the same character phase is available through a
  non-primitive lift;
- if it contains `Z_68`, the model gives a coarser but still viable CP target;
- if it contains another cyclic factor, run the replacement test;
- if it contains a product such as `Z_64 x Z_7`, test diagonal characters;
- if it contains only small torsion such as `Z_3`, the present CP benchmark
  fails at this corner.

# Product quotients

A finite abelian quotient need not be cyclic.  If

```text
Gamma_fl ~= Z_{d1} x ... x Z_{dr},
```

then characters are tuples.  A product can contain a cyclic diagonal subsystem
whose order is the least common multiple of the component orders.  For example,

```text
Z_64 x Z_7
```

contains a diagonal cyclic subsystem of order `448`.

Therefore the replacement test should be applied to the exponent and selected
diagonal characters of the full finite abelian group, not only to individual
factors.

# Bottom line

`Z_448` should not be imposed on MTT.  But it remains a strong benchmark: among
small cyclic quotients it is unusually good once the CKM phase branch and exact
leptonic `-pi/2` are both required.

The correct research posture is therefore:

```text
derive Gamma_fl first;
compute its character spectrum;
run the replacement criteria;
keep Z_448 only if Gamma_fl actually supports it.
```

