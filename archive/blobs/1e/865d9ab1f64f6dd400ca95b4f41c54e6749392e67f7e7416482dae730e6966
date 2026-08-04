---
abstract: |
  We formulate the next no-proxy flavor object after the Iwasawa rank-one
  Yukawa seed: a finite correction-channel ledger for lifting the tree-level
  rank-one texture to three-family flavor.  The corpus supports a disciplined
  list of admissible correction sources: alpha-prime/higher-derivative
  curvature terms, nonperturbative or instanton terms, flux-quantized
  Lens-Nil deformations, post-breaking kinetic metrics, q79 holonomy
  characters, and closure-strain basin geometry.  These are not yet evaluated
  coefficients.  The result closes the correction-search space at ledger level
  and rules out entry-local charm lifts, instanton factors, phases, widths, or
  distances as fundamental inputs.
author:
- Peter Nero
date: May 2026
title: |
  Rank-One Lift Correction-Channel Ledger for No-Proxy Flavor
---

# Purpose

We now have three linked pieces:

```text
q79 branch        -> finite CKM CP character,
Theta scaffold    -> fixed scale/overlap/gap environment,
Iwasawa seed      -> lambda_123 = 1 and rank-one tree Yukawa.
```

The next problem is the rank-one lift:

```text
Y_tree rank 1  ->  Y_full rank 3 with CKM/PMNS and mass hierarchies.
```

This note does not compute the lift.  It does something narrower and useful:
it identifies the finite list of correction sources allowed by the corpus and
states the no-proxy rule for using them.

# Closed Seed

The Iwasawa flux construction gives:

```text
lambda_123 = 1,
rank(Y_tree) = 1.
```

The minimal representative is:

```text
Y_seed =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 1]].
```

This gives one order-one heavy-family eigenvalue before entry-wise fitting.

# Allowed Correction Channels

The corpus supports the following correction classes.

## C1: Higher-Derivative Curvature Corrections

The heterotic flux source states that the constructed backgrounds solve the
Hull-Strominger system at order `alpha_prime`, and that at order
`alpha_prime^2` one expects curvature-squared terms, a non-constant dilaton,
or warp-factor corrections.

No-proxy use:

```text
allowed only through the selected alpha_prime expansion and curvature data.
```

Open data:

```text
actual alpha_prime^2 corrected overlap integrals.
```

The follow-up C1 audit sharpens this status.  C1 support is retained in every
Dirac sector, and its q79 character is trivial.  The selected torsional
curvature source is admissible, using the R_+ / Green-Schwarz / Strominger
fixed-point corpus.  What remains missing is the selected insertion operator
`O_C1`, the fixed alpha_prime scheme, corrected zero modes, and the evaluated
overlap/action data.  Thus C1 is an admissible source, not yet a numerical
coefficient block.

## C2: Nonperturbative or Instanton Corrections

The Iwasawa source explicitly says that small higher-derivative or
nonperturbative corrections may lift the rank-one tree seed into a hierarchical
mass structure.

No-proxy use:

```text
allowed only when the instanton sector, action, zero modes, and determinant
prefactor are selected before comparison to masses.
```

Open data:

```text
instanton action, determinant prefactor, and channel selection.
```

## C3: Flux-Quantized Lens-Nil Deformations

The Lens-Nil flux construction supplies integer fluxes `(f,h)` and two anomaly
equations fixing the ratio `R1/R`.  Flux quantization holds, and the invariant
sector has no continuous Lens-Nil moduli beyond the stated scale freedom.

The later Lens-Nil audits found that the old coefficient block cannot be used
as a numeric proof source as written: the relevant component forms are not
closed and the old abelian flux-square decomposition is invalid.  Thus C3
remains a finite support class, but its numerical coefficient extraction is
retired until the Lens-Nil block is repaired.

No-proxy use:

```text
allowed as a discrete correction source tied to integer flux data only after
the Lens-Nil component block is repaired.
```

Open data:

```text
repaired Lens-Nil flux block,
which flux sectors couple to which Yukawa overlap channels.
```

## C4: Non-Invariant Mode Corrections

The flux construction deliberately works in the left-invariant truncation and
states that a full non-invariant moduli analysis is beyond its scope.

No-proxy use:

```text
allowed only after the coherent projector retains the relevant non-invariant
mode and its gap/leakage bound is proved.
```

Open data:

```text
retained non-invariant zero modes and leakage bounds.
```

## C5: Kinetic Metrics and Canonical Normalization

The QFT corpus fixes the principle: harmonic representatives are normalized
with the internal `L2` metric, and dimensional reduction gives canonically
normalized gauge, fermion, and scalar kinetic terms.  After representation
breaking, however, the family kinetic matrix still has to be computed for the
selected modes.

No-proxy use:

```text
allowed as a global canonical-normalization matrix, not entry-wise rescaling.
```

Open data:

```text
post-breaking family kinetic metrics.
```

## C6: q79 Holonomy Characters

The q79 branch supplies the finite CP character.  It may enter overlap channels
as `chi_gamma`, but not as a tunable phase.

No-proxy use:

```text
allowed only through the selected q79 character and its channel restriction.
```

Open data:

```text
which admissible Yukawa channels carry q79, q79 powers, or trivial character.
```

## C7: Closure-Strain Basin Geometry

The ProtoSpinor/closure-strain corpus gives a qualitative stiffness ordering:

```text
D_q(g,h) >> D_l(g,h) >> D_nu(g,h)    for g != h.
```

This structurally explains why CKM is small and PMNS is large, but it does not
compute numerical mixing angles.

No-proxy use:

```text
allowed only after the sector metrics G_q, G_l, and G_nu are evaluated from
the selected closure functional.
```

Open data:

```text
numerical basin representatives and sector-induced metrics.
```

# Proxy Inputs Now Ruled Out

The corrected flavor benchmark used local flavor inputs such as:

```text
charm lift factor,
instanton corrections,
single holonomy phase.
```

Those are acceptable benchmark placeholders.  They are not acceptable final
theory inputs.  In the no-proxy lift, each must be replaced:

```text
charm lift factor          -> selected correction eigenvalue,
instanton corrections      -> selected instanton channel calculation,
single holonomy phase      -> q79 finite character restriction,
wavefunction distances     -> selected basin/overlap geometry,
widths and thresholds      -> selected flux, kinetic, and gap data.
```

# Ledger Theorem

#### Theorem

Given the Theta/q79 scaffold and the Iwasawa rank-one seed, any no-proxy
rank-one lift in the current corpus must be assembled from the finite channel
ledger:

```text
C1 alpha-prime curvature corrections,
C2 nonperturbative/instanton corrections,
C3 flux-quantized Lens-Nil deformations,
C4 retained non-invariant modes,
C5 canonical kinetic metrics,
C6 q79 holonomy characters,
C7 closure-strain basin geometry.
```

Entry-local Yukawa edits, independent phases, independent distances, and
entry-local rescalings are proxy inputs, not selected correction data.

#### Proof

The Iwasawa seed gives the rank-one tree texture.  The heterotic flux source
identifies higher-order `alpha_prime`, nonperturbative, flux-quantized, and
non-invariant deformation directions.  The QFT source fixes the canonical
normalization and threshold principle.  The q79 terminal branch fixes the
finite CP character.  The closure-strain source gives the sector stiffness
ordering controlling qualitative mixing.

These sources exhaust the correction mechanisms presently visible in the
corpus that can affect flavor without inserting individual matrix entries.
Therefore any final no-proxy flavor derivation must compute a correction
operator from these channels or add a new corpus theorem that extends this
ledger.

# Next Computation

The next executable object should be:

```text
RankOneLiftOperatorCertificate:
  input:
    Y_seed
    Theta scaffold
    q79 character
    selected SM embedding
  channels:
    finite list C_i with actions, prefactors, and characters
  output:
    DeltaY_u, DeltaY_d, DeltaY_e, DeltaY_nu
    kinetic matrices
    canonically normalized Yukawas
    CKM/PMNS and mass ratios
  discipline:
    all channel data frozen before comparison.
```

# Bottom Line

We have not yet derived the full fermion spectrum.  But the target has become
much less vague:

```text
rank-one seed closed,
allowed lift channels finite,
entry-wise flavor knobs ruled out.
```

The next leap is to compute the selected lift operator.
