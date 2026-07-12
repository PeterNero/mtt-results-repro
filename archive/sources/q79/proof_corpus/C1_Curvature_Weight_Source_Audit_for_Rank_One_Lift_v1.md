---
abstract: |
  We audit C1, the alpha-prime/higher-derivative curvature source, as a
  possible no-proxy source for lifting the Iwasawa rank-one Yukawa seed.  The
  result is positive but deliberately limited.  C1 is retained in the finite
  rank-one-lift channel sets, has trivial q79 character, and is supported by
  corpus data: the Green-Schwarz Bianchi identity, the selected torsional
  R_+ connection, the Strominger fixed-point selection functional, and
  curvature-gap control.  However, the corpus does not yet supply the selected
  C1 insertion operator, alpha-prime scheme, corrected zero modes, or overlap
  integrals.  Therefore C1 is admissible as a source class but still cannot
  provide numerical A_gamma or S_gamma weights.
author:
- Peter Nero
date: May 2026
title: |
  C1 Curvature Weight-Source Audit for Rank-One Lift
---

# Purpose

After retiring the unrepaired C3 Lens-Nil coefficient block, we ask whether
C1 can serve as the next controlled source of nontrivial rank-one-lift
weights.

The question is not:

```text
Can we invent small curvature entries?
```

The no-proxy question is:

```text
Does the corpus select a curvature source class, and if so what still has to
be computed before it becomes a numerical Yukawa weight?
```

# C1 Channel Support

The finite rank-one-lift channel set contains C1 in each Dirac sector:

```text
u:C1,
d:C1,
e:C1,
nuD:C1.
```

The q79 restriction certificate assigns trivial character to every non-C6
source class.  Hence:

```text
chi_C1 = 1.
```

C1 is therefore not a CP phase source.  It can affect magnitudes and matrix
structure only through its selected curvature insertion and overlap
functional.

# Corpus Support

The strings/flux corpus gives several independent clues that C1 is a genuine
source class.

First, the heterotic Green-Schwarz identity contains the torsional curvature:

```text
dH = alpha'/4 (Tr R_+^2 - Tr F^2)
```

up to the sign convention used for the gauge and gravitational terms.

Second, the Strominger and selection papers select the torsional connection:

```text
R_+ or R^+.
```

This matters because C1 is not a generic curvature knob.  If used, it must be
the selected torsional curvature source in the same scheme as the fixed point.

Third, the flux papers explicitly state that at higher alpha-prime order one
expects curvature-squared terms, and possibly non-constant dilaton or warp
corrections.  They also state that these effects are not evaluated in the
current construction.

Fourth, the fixed-point/OU estimates include a curvature remainder:

```text
gamma = kappa lambda - L - Delta_curv.
```

So curvature is already present as a controlled remainder in the selection
framework, not as an external phenomenological adjustment.

# What Is Closed

The following is now closed:

```text
C1 support is finite.
C1 is retained in Gamma_u, Gamma_d, Gamma_e, Gamma_nuD.
C1 has trivial q79 character.
C1 is an admissible selected curvature source.
C1 is not blocked by the C3 Lens-Nil retirement.
```

This is enough to keep C1 on the table as the next source candidate.

# What Is Still Open

The following is not closed:

```text
selected alpha-prime scheme,
selected C1 insertion operator O_C1,
C1 prefactors A_gamma,
C1 action/costs S_gamma,
alpha-prime corrected zero modes,
family kinetic metrics,
canonical Yukawa matrices,
RG and threshold matching.
```

In particular, C1 cannot yet be used to assign numerical entries to
`DeltaY_u`, `DeltaY_d`, `DeltaY_e`, or `DeltaY_nu`.

# C1 Admissibility Theorem

#### Theorem

On the current Theta/q79/Iwasawa branch, C1 is an admissible no-proxy
rank-one-lift source class, but it is not yet a numerical coefficient source.

#### Proof

The finite channel-set certificate includes C1 in each sector.  The q79
restriction certificate assigns the trivial character to every non-C6 source,
so C1 cannot carry the q79 phase.  The weight-extraction protocol allows C1
only through the selected alpha-prime order or curvature action, plus the
selected channel insertion and zero-mode overlap data.

The strings/flux corpus supplies the required source class: the
Green-Schwarz Bianchi identity involves the torsional curvature `R_+`, the
Strominger/MTT selection setup fixes the torsional connection, and the
higher-alpha-prime discussion identifies curvature-squared/dilaton/warp
terms as the next correction layer.  Thus C1 is not an arbitrary entry-wise
flavor knob.

However, no paper in the current corpus gives the selected C1 insertion
operator, corrected zero modes, overlap integrals, or numerical action
functional.  Therefore the admissibility of C1 is closed, while its numerical
weight extraction remains open.

# Consequence

C1 now has a sharper role than before:

```text
C1 can be pursued before repairing C3,
but only by deriving O_C1 and the corrected overlap integrals.
```

If those data supply two nonzero light-family eigenchannels, C1 could be part
of the rank-one lift.  If they do not, C1 remains an admissible but inert
correction class for flavor.

Follow-up status: the formal linear-response definition of `O_C1` is now
formulated in the C1 curvature insertion paper.  What remains open is not the
meaning of `O_C1`, but the explicit data needed to evaluate it:

```text
V_C1,
Hess_Xi blocks,
dotD_a operators,
zero-mode basis,
overlap integrals.
```

# Next Calculation

The next C1 calculation should produce:

```text
C1CurvatureInsertionCertificate:
  scheme:
    selected R_+ alpha-prime scheme
    local field-redefinition convention

  operator:
    O_C1 acting on the selected family zero modes

  overlap:
    A_{s,C1,ij}
    S_{s,C1}
    corrected kinetic metrics

  output:
    DeltaY_s^{C1}
```

Only after that certificate exists can C1 be used in the no-proxy mass and
mixing calculation.
