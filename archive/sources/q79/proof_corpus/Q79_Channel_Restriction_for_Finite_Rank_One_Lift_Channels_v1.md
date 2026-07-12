---
abstract: |
  We formulate the q79 channel restriction on the finite channel sets for the
  rank-one lift.  The selected CP character is q=79 in Z_448, with conjugate
  label -79=369 mod 448.  The finite channel sets already contain a dedicated
  holonomy source class C6_q79_holonomy_insertion in each sector.  The
  no-proxy restriction is therefore: non-holonomy channel types carry the
  trivial character, while only the C6 holonomy channels may carry chi_79 or
  chi_79^{-1}.  This closes the q79-support rule without computing orientations,
  weights, kinetic metrics, corrected Yukawa matrices, or RG matching.
author:
- Peter Nero
date: May 2026
title: |
  q79 Channel Restriction for Finite Rank-One Lift Channels
---

# Purpose

The finite channel sets are now explicit:

```text
Gamma_u, Gamma_d, Gamma_e, Gamma_nuD.
```

Each contains seven channel types:

```text
C0 tree rank-one seed,
C1 alpha-prime curvature,
C2 nonperturbative/instanton,
C3 flux-quantized Lens-Nil,
C4 retained non-invariant modes,
C6 q79 holonomy insertion,
C7 closure-strain basin deformation.
```

The next missing hard-leap field is:

```text
q79_channel_restriction.
```

This note closes the support rule for which channel types may carry the
selected CP character.

# Selected Character

The selected branch fixes:

```text
Gamma_CP ~= Z_448,
q = 79 mod 448.
```

The inverse/conjugate label is:

```text
-q = 448 - 79 = 369 mod 448.
```

The corresponding characters are:

```text
chi_79        = exp(2 pi i 79/448),
chi_79^{-1}  = exp(-2 pi i 79/448) = exp(2 pi i 369/448).
```

# Restriction Rule

The finite channel sets contain exactly one holonomy channel type per sector:

```text
u:C6,
d:C6,
e:C6,
nuD:C6.
```

The restriction rule is:

```text
C6_q79_holonomy_insertion:
  allowed labels = {79, 369}.

All other channel source classes:
  allowed label = {0}.
```

Equivalently, CP activity is not an independent phase attached to an arbitrary
entry or source.  If a channel is CP-active through the selected branch, it must
appear as the C6 holonomy insertion in the finite channel set.

# Sector Table

The allowed character labels are:

```text
Gamma_u:
  u:C0 -> {0}
  u:C1 -> {0}
  u:C2 -> {0}
  u:C3 -> {0}
  u:C4 -> {0}
  u:C6 -> {79,369}
  u:C7 -> {0}

Gamma_d:
  d:C0 -> {0}
  d:C1 -> {0}
  d:C2 -> {0}
  d:C3 -> {0}
  d:C4 -> {0}
  d:C6 -> {79,369}
  d:C7 -> {0}

Gamma_e:
  e:C0 -> {0}
  e:C1 -> {0}
  e:C2 -> {0}
  e:C3 -> {0}
  e:C4 -> {0}
  e:C6 -> {79,369}
  e:C7 -> {0}

Gamma_nuD:
  nuD:C0 -> {0}
  nuD:C1 -> {0}
  nuD:C2 -> {0}
  nuD:C3 -> {0}
  nuD:C4 -> {0}
  nuD:C6 -> {79,369}
  nuD:C7 -> {0}
```

# What This Closes

This closes the q79-support rule:

```text
the only CP-active channel type is C6,
the only nontrivial labels allowed are 79 and 369,
all non-C6 channel types are character-trivial at support level.
```

This also prevents smuggling an empirical CKM phase into an arbitrary
coefficient.

# What Remains Open

This certificate does not compute:

```text
which of chi_79 or chi_79^{-1} occurs in each sector,
whether the C6 coefficient is zero or nonzero in each sector,
the weights A_gamma and S_gamma,
post-breaking family kinetic metrics,
DeltaY matrices,
canonical Yukawa matrices,
RG and threshold matching.
```

Those are coefficient and orientation questions, not support questions.

# Theorem

#### Theorem

Given the selected q79 branch and the finite channel sets, the no-proxy CP
restriction on rank-one lift channels is:

```text
allowed_label(gamma) =
  {79,369}, if source_class(gamma)=C6_q79_holonomy_insertion,
  {0},      otherwise.
```

#### Proof

The terminal q79 branch fixes the finite CP character in `Z_448` with label
`79`.  Its conjugate is `369`.  The finite channel-set certificate contains a
dedicated holonomy-insertion source class `C6_q79_holonomy_insertion`, and no
other channel source class is defined as a holonomy character insertion.

Therefore, to preserve the no-proxy discipline, nontrivial CP character labels
may enter only through C6.  Non-C6 channels are assigned the trivial character
at support level.  The sign/orientation and coefficient of C6 remain open for
the subsequent weight and kinetic-metric calculation.

# Bottom Line

The hard-leap blocker is reduced again:

```text
q79_channel_restriction        FORMULATED,
channel_weights                OPEN,
family_kinetic_metrics         OPEN,
delta_yukawa_matrices          OPEN,
canonical_yukawa_matrices      OPEN,
rg_threshold_matching          OPEN.
```

The next calculation is the first coefficient layer:

```text
compute or constrain A_gamma and S_gamma for the finite, q79-restricted
channels.
```

