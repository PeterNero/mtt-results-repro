---
abstract: |
  We audit the papers in "16 Strings, Flux, & M-Theory Encodings" for clues
  relevant to completing the MTT order-448 CP proof.  The folder does not
  contain an explicit Z_7 or order-seven Wilson line.  It does, however,
  contain three crucial structures: fixed topological/differential-cohomology
  sectors, HYM existence via stable bundles in Fu-Yau/Strominger settings, and
  integral flux/harmonic lattices.  The strongest replacement for the broken
  Lens-Nil coefficient block is a Fu-Yau/K3 lattice candidate: a primitive
  rank-two sublattice of H^2(K3,Z) with Gram [[-2,-1],[-1,-4]], whose negative
  is [[2,1],[1,4]] and whose Smith form is [7].
author:
- Peter Nero
date: May 2026
title: |
  Strings/Flux/M-Theory Corpus Clue Ledger for the Z_7 CP Row
---

# Scope

Folder checked:

```text
C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings
```

Files:

```text
Flux_Compactifications_in_Heterotic_String_Theory_v3.md
Modal_Triplet_Theory__From_MTT_to_Calabi__Yau_Compactifications.md
Modal_Triplet_Theory__From_MTT_to_M_theory.md
Modal_Triplet_Theory__From_MTT_to_String_Theory.md
Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md
Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md
When_Is_a_Configuration_Physical____Rethinking_the_Vacuum_Selection_Problem.md
```

# High-level result

The folder does **not** contain an explicit:

```text
Z_7,
order-seven Wilson line,
seven-torsion class,
or completed order-448 CP proof.
```

But it does contain the missing infrastructure:

```text
fixed topological sectors,
integral cohomology/flux lattices,
stable bundle -> HYM existence,
Fu-Yau/K3 admissible flux slice,
M-theory shifted flux quantization,
selection as admissibility/fixed point.
```

The best new candidate is:

```text
Fu-Yau/K3 determinant-seven lattice block.
```

# Paper-by-paper clues

## Flux compactifications paper

Useful clues:

```text
explicit monad construction,
K-theory/Chern character formulas,
stable bundle/HYM mechanism,
integer line-bundle data,
flux quantization and gerbe integrality.
```

Important correction:

```text
the Lens-Nil subcase is not usable as written for the Z_7 proof.
```

The audit found:

```text
d beta_1 != 0,
d beta_3 != 0,
F=f eta12+h sigma45 gives F^2=2fh beta_2.
```

So the Lens-Nil appendix needs repair before it can support any exact torsion
claim.

## MTT as a selection principle for heterotic flux compactifications

Useful clues:

```text
FCC = anomaly/primitivity/quantization system,
left-invariant torsional SU(3) slice,
selection as coherent-sector contraction,
componentwise anomaly system,
discrete admissible sectors.
```

Risk:

```text
it inherits the same Lens-Nil component formulas, so those parts need revision.
```

## Strominger/Heterotic flux system

This is one of the strongest support papers.

Useful clues:

```text
B-field as gerbe connection,
large gauge transformations,
fixed differential-cohomology class,
fixed topological sector,
stable bundle on Gauduchon metric -> HYM via Li-Yau,
Fu-Yau class as admissible flux slice,
unique local minimizer / selected fixed point.
```

This supports the framework needed for a real proof:

```text
choose exact integral topological data first,
then prove HYM/admissibility,
then take the unitary character quotient.
```

## M-theory bridge

Useful clues:

```text
shifted G_4 quantization,
integral degree-four cohomology lattice fixed by topological sector,
large gauge transformations,
tadpole/integrated charge constraints,
4D data determined by harmonic lattice and integral flux class.
```

This supports the general character-lattice strategy, but it does not by
itself select the number seven.

Potential future route:

```text
look for a determinant-seven intersection block in the M-theory harmonic or
torsion lattice.
```

## Calabi-Yau compactifications bridge

Useful clues:

```text
HYM bundles,
split bundle Laplacians,
commuting projectors,
CY corner and deformation from Lens/Nil baseline.
```

This supports the analytic and HYM side, but does not provide an explicit
sevenfold finite quotient.

## MTT to String Theory

Useful clues:

```text
Green-Schwarz anomaly cancellation,
torsional SU(3) slice,
HYM bundles,
Bianchi identity at the fixed point.
```

This is broad structural support, not an arithmetic source.

## Vacuum selection/admissibility paper

Useful clues:

```text
selection acts on admissible regions,
formal consistency is not enough,
stability and spectral separation are required.
```

This supports rejecting the broken Lens-Nil block rather than forcing it.

# Best candidate after the sweep

Use the K3 lattice in the Fu-Yau base.

Inside:

```text
U^2 subset H^2(K3,Z),
```

take:

```text
v = (-1,  0, -1, 1),
w = ( 1, -1, -1, 1).
```

Then:

```text
v^2 = -2,
w^2 = -4,
v.w = -1.
```

So:

```text
Gram(v,w) =
[-2 -1
 -1 -4],
```

and:

```text
K = -Gram(v,w) =
[2 1
 1 4].
```

Smith normal form:

```text
SNF(K)=[7].
```

This is currently the cleanest exact source of the `Z_7` matrix.

# Why Fu-Yau/K3 is stronger than Lens-Nil

The Fu-Yau/K3 candidate uses:

```text
an exact integral lattice intersection form.
```

The broken Lens-Nil route used:

```text
non-closed component forms,
approximate curvature coefficients,
and an inconsistent abelian flux square.
```

So the Fu-Yau/K3 route has a much better chance of becoming rigorous.

# Remaining proof gates

To finish the `Z_7` part through Fu-Yau/K3, prove:

```text
1. K3 realization:
   <v,w> is realized as a primitive (1,1) Picard sublattice in an admissible K3.

2. HYM/bundle realization:
   a stable or polystable holomorphic bundle in the Fu-Yau compactification
   has Chern/flux pairing K=[[2,1],[1,4]].

3. Bianchi compatibility:
   the Fu-Yau anomaly equation admits this topological data with the gerbe
   class fixed.

4. CP character identification:
   the family-trivial CP labels are Hom(coker K,U(1)).

5. MTT selection:
   the fixed-point/admissibility principle selects this block, not just allows it.
```

# Current recommendation

Retire the old Lens-Nil coefficient block as a proof source until its appendix
is corrected.

Carry forward the Fu-Yau/K3 determinant-seven lattice candidate as the primary
`Z_7` route.

