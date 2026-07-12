---
abstract: |
  We formulate the low-energy Higgs-channel projection needed after the
  E6-to-SM Yukawa operator dictionary.  The MTT corpus supplies two independent
  constraints: the NCG/finite-algebra Standard Model target contains a Higgs
  multiplet as a finite connection, while the closure-alignment corpus states
  that a connected admissible domain has at most one global Higgs-like radial
  relaxation mode.  Therefore the low-energy SM projection uses one complex
  Higgs doublet H with Y=+1/2, identifies the E6/SU(5) up-type candidate
  H_u with H, and identifies the down/lepton candidate H_d with the conjugate
  doublet H^\dagger.  This closes the low-energy Higgs doublet embedding for
  the rank-one operator program.  It does not compute the Higgs mass, VEV,
  color-triplet decoupling, kinetic metrics, correction coefficients, or RG
  matching.
author:
- Peter Nero
date: May 2026
title: |
  Single-Higgs Channel Projection for the E6 Rank-One Seed
---

# Purpose

The E6-to-SM dictionary formulated the representation-level operators:

```text
Q u^c H_u,
Q d^c H_d,
L e^c H_d,
L N^c H_u.
```

The next missing field in the hard-leap certificate is:

```text
higgs_doublet_embedding.
```

This note closes the low-energy embedding, not the Higgs mass or the full
high-scale doublet/triplet problem.

# Corpus Anchors

## NCG finite connection

The NCG paper uses the almost-commutative finite algebra:

```text
A_F = C + H + M_3(C),
```

and states that inner fluctuations of the finite Dirac operator generate the
SM gauge potentials and a Higgs multiplet as a finite connection.  The finite
Dirac operator encodes the Yukawa matrices.

Thus the downstream target is the Standard Model finite-connection Higgs
sector, not a free multi-Higgs fit.

## Unique alignment mode

The ProtoSpinor and closure-strain papers state that, on a connected admissible
domain, there is at most one global alignment reference up to
redundancy-equivalence.  Consequently there is at most one Higgs-like radial
closure-relaxation mode associated to that reference.

This rules out using two independent low-energy Higgs alignment references as
flavor knobs.

# Projection Rule

Let:

```text
H : SU(2)_L doublet with Y = +1/2.
```

In left-chiral SM Yukawa notation, define the projected E6/SU(5) Higgs-channel
dictionary:

```text
H_u  -> H,
H_d  -> H^\dagger.
```

Since `SU(2)` doublets are pseudoreal, the conjugate doublet carries the needed
weak transformation type, with opposite hypercharge.

The low-energy Yukawa channels become:

```text
Q u^c H,
Q d^c H^\dagger,
L e^c H^\dagger,
L N^c H.
```

# Gauge Checks

Using:

```text
Y(Q)=1/6,
Y(u^c)=-2/3,
Y(d^c)=1/3,
Y(L)=-1/2,
Y(e^c)=1,
Y(N^c)=0,
Y(H)=1/2,
Y(H^\dagger)=-1/2,
```

the hypercharge sums are:

```text
Q u^c H:           1/6 - 2/3 + 1/2 = 0,
Q d^c H^\dagger:  1/6 + 1/3 - 1/2 = 0,
L e^c H^\dagger: -1/2 + 1 - 1/2 = 0,
L N^c H:          -1/2 + 0 + 1/2 = 0.
```

Thus one Higgs doublet and its conjugate are enough for all four Dirac Yukawa
operator forms.

# What This Closes

The low-energy Higgs doublet embedding is now formulated:

```text
higgs_doublet_embedding:
  physical_doublet: H with Y=+1/2
  up_type_channel: H_u -> H
  down_type_channel: H_d -> H^\dagger
  charged_lepton_channel: H_d -> H^\dagger
  dirac_neutrino_channel: H_u -> H
```

This is exactly the Standard Model single-Higgs projection compatible with:

```text
NCG finite connection,
unique MTT alignment reference,
SM hypercharge invariance.
```

# What Remains Open

This does not yet prove the full flavor spectrum.

Still open:

```text
color-triplet projection or decoupling from the high-scale E6/SU(5) multiplets,
which sector receives the rank-one seed before corrections,
the Higgs VEV and Higgs mass prediction,
finite correction-channel sets Gamma_u,d,e,nuD,
channel weights A_gamma and S_gamma,
q79 channel restriction chi_gamma,
family kinetic metrics,
canonical Yukawa matrices,
RG and threshold matching.
```

# Theorem

#### Theorem

Assume the downstream target is the MTT-derived NCG Standard Model finite
connection and the connected-domain alignment uniqueness theorem applies.
Then the E6-to-SM rank-one seed admits a single-Higgs low-energy projection:

```text
H_u -> H,
H_d -> H^\dagger,
```

where `H` is the unique physical SM Higgs doublet with `Y=+1/2`.
The resulting up, down, charged-lepton, and Dirac-neutrino Yukawa operators are
SM gauge invariant.

#### Proof

The NCG source supplies the downstream Standard Model Higgs as a finite
connection.  The alignment source forbids an independent second global Higgs
alignment reference on a connected admissible domain.  Therefore the
low-energy channel projection must use one physical Higgs doublet and its
conjugate rather than two independent Higgs relaxation modes.

Substituting `H_u -> H` and `H_d -> H^\dagger` in the formulated E6-to-SM
operator dictionary gives the four listed Dirac Yukawa operators.  Their
hypercharge sums vanish, and `SU(2)` pseudoreality supplies the conjugate
doublet channel.  Hence the low-energy Higgs doublet embedding is
representation-consistent and compatible with the MTT uniqueness constraint.

# Bottom Line

The hard-leap blocker has been reduced again:

```text
selected_E6_to_SM_embedding       FORMULATED,
higgs_doublet_embedding           FORMULATED,
selected coefficients/metrics/RG  OPEN.
```

The next proof layer is no longer "which Higgs doublet?"  It is:

```text
which selected weights, q79 orientations, and kinetic metrics lift the
rank-one seed?
```
