---
abstract: |
  We isolate the next normalization problem in the MTT order-448 CP program.
  Constructing an order-448 character theta_CP fixes the denominator and the
  finite character group, but it does not by itself derive the CKM numerator
  79.  The cyclic group has automorphisms, and many primitive labels have
  order 448.  After fixing the PMNS quarter-turn label 336 and imposing
  phase-sum closure, there remain 192 primitive CKM labels with primitive
  phase-sum partners.  The CKM/Jarlskog benchmark selects q=79 on the chosen
  phase branch, while q=145 gives the same sine/Jarlskog value on the
  complementary branch.  Thus finite topology has reached the admissible label
  lattice; the remaining task is an overlap/selection theorem deriving q=79
  from MTT dynamics rather than fitting it.
author:
- Peter Nero
date: May 2026
title: |
  CP Label Normalization and Overlap-Selection Gate
---

# Purpose

The character algebra now gives:

```text
theta_CP of order 448.
```

But a cyclic group of order `448` has many primitive generators and many
primitive labels.  Therefore the finite quotient alone does not yet prove the
specific CKM numerator:

```text
79.
```

This note isolates that final normalization gate.

# Exact finite constraints

Work in:

```text
Z_448.
```

The lepton quarter-turn branch fixes:

```text
l=336,
ord(l)=4,
2pi*l/448 = 3pi/2 = -pi/2 mod 2pi.
```

Phase-sum closure imposes:

```text
q + l + r = 0 mod 448.
```

So once `q` is chosen:

```text
r = -(q+336) mod 448.
```

The CKM and phase-sum partner branches should both have order `448`:

```text
ord(q)=448,
ord(r)=448.
```

# Scan result

The scan:

```text
cp_label_normalization_scan.py
```

finds:

```text
192 primitive q labels with primitive phase-sum partners.
```

So exact finite topology has not uniquely selected `q=79`.

# CKM branch

Using the current CKM/Jarlskog benchmark, the best phase-branch label is:

```text
q=79,
l=336,
r=33.
```

It gives:

```text
delta_q = 2pi*79/448 = 1.107972409079,
phase_error = 6.164e-06,
J_error = 8.920e-11.
```

The closure is exact:

```text
79+336+33=448=0 mod 448.
```

# Complementary branch caveat

The Jarlskog invariant depends on:

```text
sin(delta).
```

Therefore the complementary phase:

```text
pi - delta
```

can give the same `J` value.  The scan reflects this: `q=145` has the same
Jarlskog error but lies on the complementary phase branch:

```text
2pi*145/448 = 2.033620244511.
```

Thus the physical phase convention or overlap orientation must select the
branch, not merely the sine.

# What is proved

```text
Z_448 denominator/order is proved conditionally on the selection gates.
PMNS quarter-turn label 336 is exact.
Phase-sum closure fixes r once q is chosen.
q=79 is the best CKM phase-branch label.
```

# What is not proved

Finite topology alone has not yet proved:

```text
q=79.
```

It has proved the admissible finite character lattice.  The remaining theorem
must select a particular primitive label from that lattice.

# Candidate MTT selection principles for q=79

Possible routes:

```text
1. overlap functional:
   compute the CKM overlap phase from localized mode geometry and show its
   nearest admissible character is 79;

2. action/minimization:
   derive a discrete phase-selection functional on Z_448 whose minimizer is 79
   on the physical branch;

3. discriminant/central-circle orientation:
   show the orientations of theta_64 and theta_7 fix the branch and primitive
   label;

4. threshold/renormalized overlap:
   derive a small correction target that selects q=79 rather than neighboring
   primitive labels 75,81,83;

5. empirical calibration:
   treat 79 as the measured overlap label after deriving the denominator and
   exact closure constraints.
```

The strongest final proof needs route 1 or 2.

# Gate status

```text
finite group supplies denominator 448                      PASS
lepton quarter-turn fixes label 336 in chosen orientation  PASS
phase-sum partner is determined once q is chosen           PASS
finite topology uniquely fixes q=79                        FAIL
CKM/Jarlskog benchmark selects q=79                        NUMERICAL PASS
MTT derives q=79 from overlap/selection dynamics           OPEN
```

# Bottom line

The proof frontier has moved again.

The denominator is no longer the main mystery:

```text
448 is structurally accounted for by Z_64 carry + Mukai Z_7 discriminant group.
```

The remaining numerical theorem is:

```text
derive the primitive label q=79 from MTT overlap/selection dynamics.
```

This is a smaller and cleaner problem than deriving `448` from scratch.
