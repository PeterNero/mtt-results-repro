---
abstract: |
  We close the representation-dictionary layer between the Iwasawa E6
  rank-one cubic and Standard Model Yukawa operators.  The MTT corpus supplies
  the normalized E6 27^3 seed and a downstream NCG/finite-algebra Standard
  Model target.  The missing bridge is the standard E6 -> SO(10) -> SU(5) ->
  SM branching dictionary.  This note records that dictionary, checks the
  dimension and charge balances, and identifies the SM Yukawa operator
  channels carried by the E6 cubic.  It does not yet select the physical light
  Higgs doublet, color-triplet decoupling, family kinetic metrics, correction
  channel weights, or RG/threshold matching.
author:
- Peter Nero
date: May 2026
title: |
  E6 to SM Yukawa Operator Dictionary for the Rank-One Seed
---

# Purpose

The Iwasawa seed certificate closed:

```text
E6 27^3 normalized cubic -> lambda_123 = 1 -> rank-one tree Yukawa seed.
```

The hard-leap operator audit then listed a missing input:

```text
selected_E6_to_SM_embedding.
```

The corpus does not appear to contain an explicit branching table for
`E6 -> SO(10) -> SU(5) -> SM`.  It does, however, contain:

```text
1. the Iwasawa E6 27^3 rank-one source;
2. an NCG finite-algebra route to the SM gauge, fermion, and Higgs content;
3. hypercharge and Yukawa-overlap statements in the Standard Model corner.
```

Therefore this note closes the representation dictionary, not the full physical
selection.  The distinction matters.

# Corpus Anchors

## Iwasawa rank-one source

The heterotic flux paper supplies three harmonic representatives:

```text
Psi_i in H^1(X,E), i=1,2,3,
```

and the normalized trilinear:

```text
lambda_123 = integral_X Omega wedge Tr(Psi_1 wedge Psi_2 wedge Psi_3) = 1
```

after chiral rephasing.  The same source states that the E6 `27^3` cubic
inherits this normalization and yields a rank-one tree-level Yukawa matrix.

## Downstream SM target

The NCG paper uses:

```text
A_F = C + H + M_3(C)
```

in the standard almost-commutative representation.  Its inner fluctuations
generate the SM gauge sector and the Higgs as a finite connection, with
unimodularity giving:

```text
U(1)_Y x SU(2)_L x SU(3)_c.
```

The closure-strain SM paper separately records that exact quantum numbers are
fixed structurally by the finite algebra route, while numerical Yukawas and
masses remain execution-level.

# Standard Branching Dictionary

The standard E6 branch used here is:

```text
E6 -> SO(10) x U(1)_psi
27 -> 16_1 + 10_-2 + 1_4.
```

The SO(10) branch is:

```text
SO(10) -> SU(5) x U(1)_chi
16_1  -> 10_-1 + bar5_3 + 1_-5,
10_-2 -> 5_2 + bar5_-2,
1_4   -> 1_0.
```

The SM assignments are:

```text
10_M   -> Q + u^c + e^c,
bar5_M -> d^c + L,
1_M    -> N^c,
5_H    -> H_u + color triplet,
bar5_H -> H_d + color antitriplet.
```

Dimension checks:

```text
16 + 10 + 1 = 27,
10 + 5 + 1 = 16,
5 + 5 = 10.
```

The E6 cubic channel:

```text
16_M 16_M 10_H
```

is neutral under `U(1)_psi`:

```text
1 + 1 - 2 = 0.
```

# SM Yukawa Operators

The `16_M 16_M 10_H` invariant contains the usual SU(5) Yukawa channels:

```text
10_M 10_M 5_H       -> up-type Yukawa:       Q u^c H_u
10_M bar5_M bar5_H  -> down-type Yukawa:     Q d^c H_d
10_M bar5_M bar5_H  -> charged-lepton:       L e^c H_d
bar5_M 1_M 5_H      -> Dirac-neutrino:       L N^c H_u
```

The `U(1)_chi` charge sums are:

```text
(-1) + (-1) + 2  = 0,
(-1) + 3 + (-2)  = 0,
3 + (-5) + 2     = 0.
```

The SM hypercharge sums are:

```text
Q u^c H_u:      1/6 - 2/3 + 1/2 = 0,
Q d^c H_d:      1/6 + 1/3 - 1/2 = 0,
L e^c H_d:     -1/2 + 1 - 1/2 = 0,
L N^c H_u:     -1/2 + 0 + 1/2 = 0.
```

Thus the representation-level operator dictionary is consistent.

# What This Closes

The dictionary closes the following layer:

```text
E6 27^3 rank-one cubic
-> standard 16_M 16_M 10_H branch
-> SM up, down, charged-lepton, and Dirac-neutrino Yukawa operator forms.
```

This means the Iwasawa rank-one seed can be carried into the standard SM
Yukawa operator language without a representation-theoretic obstruction.

# What Remains Open

This does not yet prove the physical mass spectrum.

The following fields remain open:

```text
projection/decoupling of color-triplet partners,
whether the rank-one seed is assigned to the top channel or a mixed channel,
post-breaking family kinetic metrics,
finite correction-channel sets,
channel weights A_gamma and S_gamma,
q79 restriction on each Yukawa channel,
canonical Yukawa matrices,
RG and threshold matching.
```

There is also a high-scale/low-scale Higgs issue.  The E6/SO(10) holomorphic
dictionary naturally contains `H_u` and `H_d` candidates inside `10_H`.  The
NCG/SM downstream target contains the physical Higgs finite connection.  The
map from the high-scale pair/candidates to the low-energy light Higgs doublet
is supplied by the follow-up single-Higgs channel projection:

```text
H_u -> H,
H_d -> H^\dagger.
```

The high-scale color-triplet projection/decoupling and the rank-one seed's
final sector assignment remain open.

# Theorem

#### Theorem

Assume the selected Iwasawa E6 cubic descends through the standard
`E6 -> SO(10) -> SU(5) -> SM` branch with matter in `16_M` and Higgs candidates
in `10_H`.  Then the normalized rank-one E6 cubic has a representation-level
image in the SM Yukawa operator dictionary:

```text
Q u^c H_u,
Q d^c H_d,
L e^c H_d,
L N^c H_u.
```

All these operators are gauge invariant under the SM gauge group.

#### Proof

The E6 branching gives `27 = 16_1 + 10_-2 + 1_4`.  The cubic
`16_M 16_M 10_H` is E6-admissible because the `U(1)_psi` charges sum to zero.
Branching further to SU(5) gives the three neutral channels:

```text
10_M 10_M 5_H,
10_M bar5_M bar5_H,
bar5_M 1_M 5_H.
```

Their `U(1)_chi` charge sums vanish.  Decomposing to the SM gives the four
listed Yukawa operator forms, and each has total hypercharge zero.  Therefore
there is no representation-theoretic obstruction to carrying the Iwasawa
rank-one E6 seed into SM Yukawa operator language.

# Bottom Line

One hard-leap field is now reduced:

```text
selected_E6_to_SM_embedding
```

is no longer a blank representation problem.  It is now:

```text
standard E6 -> SO(10) -> SU(5) -> SM operator dictionary formulated;
physical Higgs/channel selection still open.
```

So the proof frontier moves from "what SM operators does 27^3 even mean?" to:

```text
which Higgs/channel/kinetic/correction data does MTT select?
```
