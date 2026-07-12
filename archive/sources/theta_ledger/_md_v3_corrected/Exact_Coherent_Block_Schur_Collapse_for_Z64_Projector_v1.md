---
abstract: |
  We close the reduced Schur gate for the exact Z_64 coherent-block branch.
  The previous bound required C_fl/(alpha lambda_Q)<9/2, where
  C_fl=||P_fl L Q||||Q L P_fl||.  After the Flavor-QG projector
  compatibility lemma, the exact blockwise regime gives P_fl<=Pi_coh and
  [L,Pi_coh]=0.  Therefore the coherent/noncoherent off-block maps vanish:
  P_fl L Q=0 and Q L P_fl=0, with Q=I-Pi_coh.  Hence C_fl=0, E_Schur=0, and
  the Z_64 Riesz projector selection inequality holds automatically for any
  alpha>0 and any positive excluded-sector gap.  In the approximate
  warp/noncommuting case, if ||[L,Pi_coh]||<=epsilon, then
  C_fl<=epsilon^2 and the remaining condition is
  epsilon^2/(alpha lambda_Q)+epsilon_warp/alpha<9/2.  This closes the exact
  Schur branch and converts the non-exact branch into a small-commutator
  estimate.
author:
- Peter Nero
date: May 2026
title: |
  Exact Coherent-Block Schur Collapse for the Z64 Projector
---

# Purpose

The reduced Z_64 Hessian gate was:

```text
C_fl / (alpha lambda_Q) < 9/2,
C_fl = ||P_fl L Q|| ||Q L P_fl||.
```

This looked like a remaining numerical bound.  But after the projector
compatibility lemma, there is an exact branch where the Schur term collapses.

# Setup

Let:

```text
Pi = Pi_coh,
Q = I - Pi.
```

Let `L` be the selected flavor closure operator used in the Hessian/Riesz
problem.

Assume the exact blockwise coherent regime:

```text
[L,Pi] = 0.
```

Assume the finite Z_64 flavor projector is a coherent subprojector:

```text
P_fl Pi = Pi P_fl = P_fl.
```

This is exactly the conclusion of the Flavor-QG projector compatibility lemma
once the finite Wilson/deck carrier is retained by `Pi_coh` and the Riesz
contour encloses only coherent-sector flavor spectrum.

# Lemma: Off-Block Maps Vanish

Under the setup assumptions:

```text
P_fl L Q = 0,
Q L P_fl = 0.
```

## Proof

Since `P_fl=P_fl Pi`,

```text
P_fl L Q = P_fl Pi L Q.
```

But `[L,Pi]=0` implies that `L` preserves both `Ran(Pi)` and `Ran(Q)`.
Equivalently:

```text
Pi L Q = 0.
```

Hence:

```text
P_fl L Q = 0.
```

Similarly, since `P_fl=Pi P_fl`,

```text
Q L P_fl = Q L Pi P_fl.
```

Again `[L,Pi]=0` implies:

```text
Q L Pi = 0.
```

Therefore:

```text
Q L P_fl = 0.
```

This proves the lemma.

# Theorem: Exact Schur Collapse

Under the same assumptions:

```text
C_fl = ||P_fl L Q|| ||Q L P_fl|| = 0.
```

Consequently:

```text
E_Schur
= P_fl L Q (Q L Q)^(-1) Q L P_fl
= 0.
```

Therefore the reduced Z_64 gate:

```text
C_fl / (alpha lambda_Q) < 9/2
```

holds automatically for:

```text
alpha > 0,
lambda_Q > 0.
```

## Proof

The off-block maps vanish by the lemma.  Hence their product norm is zero, and
the Schur-Feshbach operator contains the zero factor on both sides.  Since:

```text
0 < 9/2,
```

the strict reduced inequality is satisfied whenever `alpha` and `lambda_Q` are
positive.

# Gap Bridge to lambda_*

If the selected flavor complement is the QG noncoherent complement:

```text
Q = I - Pi_coh,
```

and the QG internal block has:

```text
Q L Q >= lambda_* Q,
```

then:

```text
lambda_Q >= lambda_*.
```

This is the precise lambda bridge.  In the exact Schur-collapse branch it is
needed only to ensure invertibility of the excluded block; the numerator is
already zero.

# Approximate Version

If exact commutation is relaxed to:

```text
||[L,Pi]|| <= epsilon_comm,
```

then:

```text
||P_fl L Q|| <= epsilon_comm,
||Q L P_fl|| <= epsilon_comm.
```

Indeed:

```text
Pi L Q = [Pi,L] Q,
Q L Pi = Q [L,Pi] Pi.
```

Using `||P_fl||=||Pi||=||Q||=1` gives the two bounds.

Therefore:

```text
C_fl <= epsilon_comm^2.
```

The reduced gate is then implied by:

```text
epsilon_comm^2/(alpha lambda_Q) < 9/2.
```

If there is an additional tracked warp leakage `epsilon_warp`, the sufficient
condition is:

```text
epsilon_comm^2/(alpha lambda_Q) + epsilon_warp/alpha < 9/2.
```

# Relation to Previous Papers

This does not contradict the Schur-gap reduction paper.  That paper identified
the correct general Schur constant:

```text
C_fl = ||P_fl L Q|| ||Q L P_fl||.
```

The present paper uses the later projector-compatibility theorem to evaluate
that constant in the exact coherent block regime:

```text
C_fl = 0.
```

Thus the exact branch is stronger than the conservative baseline floor
criterion:

```text
C_fl < 9 alpha/8.
```

It satisfies it trivially.

# Gate Status

```text
P_fl <= Pi_coh under compatibility assumptions        PROVED
[L,Pi_coh]=0 exact block condition                    ASSUMED/MTT-BLOCK
off-block maps vanish in exact branch                 PROVED
C_fl=0 in exact branch                                PROVED
E_Schur=0 in exact branch                             PROVED
C_fl/(alpha lambda_Q)<9/2 in exact branch             PROVED
lambda_Q>=lambda_* when Q block is the QG complement  PROVED-CONDITIONAL
approximate commutator bound C_fl<=epsilon_comm^2     PROVED
actual Hessian/kernel exact-block verification        OPEN
```

# Bottom Line

For the exact coherent finite-carrier branch, the reduced Schur gate is closed:

```text
P_fl <= Pi_coh and [L,Pi_coh]=0
=> C_fl = 0
=> q_64 tower selection is stable.
```

The only remaining version of the Schur problem is the non-exact branch, where
one must bound the commutator or warp leakage.
