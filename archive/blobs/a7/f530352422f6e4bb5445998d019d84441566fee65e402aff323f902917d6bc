---
abstract: |
  We test the sharpest currently available no-proxy route for the missing CKM
  heavy-link numbers.  Pure qutrit/C6 support is diagonal and gives
  Delta_c=(0,0).  A common Fourier rotation is also only gauge: it cancels in
  B_left^dagger I B_right.  However, the E6-to-SM dictionary separates the
  up channel 10_M x 10_M from the down channel 10_M x bar5_M.  If selected
  zero-mode data prove a relative qutrit Fourier transport between the 10_M
  and bar5_M family slots, then the down channel receives exact nonzero
  heavy-link entries while the up channel remains diagonal.  This gives a
  precise candidate for the reduced C1 basis_connection slot, not selected SM
  closure.
author:
- Peter Nero
date: May 2026
title: |
  SU(5) Qutrit Basis Transport Heavy-Link Candidate
---

# Purpose

The current leading CKM bottleneck is:

```text
Delta_t = (M_d13-M_u13, M_d23-M_u23).
```

The pure qutrit/C6 support calculation gave:

```text
Delta_c = (0,0).
```

So the useful next question is not "can a global Fourier rotation make
off-diagonal entries?"  That was already rejected as pure gauge in the
Fourier-rotated rho_E prototype.  The useful question is:

```text
can selected sector-relative basis transport distinguish 10_M from bar5_M?
```

# Calculation

Use the finite diagonal invariant support:

```text
I_3.
```

Let the physical support in two sector bases be:

```text
M(left,right)=B_left^dagger I_3 B_right.
```

Let:

```text
F_jk = omega^(j k)/sqrt(3),     omega=exp(2*pi*i/3),     j,k=0,1,2.
```

Two control cases close first:

```text
B_10=B_bar5=I_3      -> Delta_t=(0,0),
B_10=B_bar5=F        -> Delta_t=(0,0).
```

The second line is the important guardrail.  A common Fourier transport is only
a shared basis choice.  It does not create physical CKM data.

# SU(5) Split

The E6/SU(5) operator dictionary gives:

```text
up:    10_M x 10_M       -> Q u^c H_u,
down:  10_M x bar5_M     -> Q d^c H_d.
```

Now test the representation split:

```text
B_10=I_3,
B_bar5=F.
```

Then:

```text
M_u = B_10^dagger B_10 = I_3,
M_d = B_10^dagger B_bar5 = F.
```

Therefore:

```text
Delta_t = (F_13, F_23)
        = (1/sqrt(3), omega^2/sqrt(3)).
```

Numerically:

```text
Delta_t = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i).
```

The inverse convention:

```text
B_bar5=F^*
```

gives the conjugate second entry:

```text
Delta_t = (1/sqrt(3), omega/sqrt(3)).
```

# What This Achieves

This is the first exact candidate in the current branch that does all of the
following:

```text
uses no observed masses,
uses no CKM benchmark entries,
does not revive the retired Lens-Nil proof source,
does not contradict the pure C6 diagonal-support obstruction,
does not mistake common Fourier gauge for physical mixing,
uses the actual E6/SU(5) split between up and down Yukawa operators.
```

It also supplies an executable nonselected fixture for:

```text
scripts/compute_c1_heavy_link_delta_t.py.
scripts/compute_ckm_heavy_link_gate.py.
```

If the sector transport is later selected, the reduced C1 packet would put the
above two numbers into the down-sector `basis_connection` heavy-link slot, with
the up-sector slot zero.  With the already proved pure-C6 value
`Delta_c=(0,0)`, the full heavy-link gate then reads:

```text
Delta_v = Delta_t + chi_79 Delta_c = Delta_t != (0,0).
```

# What This Does Not Achieve

This is not selected MTT data yet.

It does not prove:

```text
selected B_10 and B_bar5 basis maps,
whether the transport is a finite basis choice or a C1 linear response,
the selected overlap-kernel prefactor,
canonical kinetic normalization,
full 3x3 Yukawa matrices,
CKM angle magnitudes,
the Jarlskog invariant,
full SM closure.
```

# Correct Way Forward

The next lemma is now very sharp:

```text
Sector Transport Selection Lemma.
The selected monad/Cech/Galerkin zero-mode construction derives
B_10=I_3 and B_bar5=F, or the conjugate convention, for the same q79 branch.
```

If that lemma is proved from the selected zero-mode/bundle data, this candidate
ceases to be a fixture and becomes a fill for the reduced heavy-link packet.
The remaining numerical work would then be the selected normalization,
canonical kinetic metrics, and full matrix/Jarlskog calculation.
