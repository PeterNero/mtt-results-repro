---
abstract: |
  We turn the correction-channel ledger, the E6-to-SM operator dictionary, and
  the single-Higgs projection into explicit finite Yukawa channel sets
  Gamma_u, Gamma_d, Gamma_e, and Gamma_nuD.  These sets are finite lists of
  admissible channel types: the projected E6 tree cubic plus selected-source
  correction classes from alpha-prime curvature, nonperturbative/instanton
  effects, flux-quantized Lens-Nil deformations, retained non-invariant modes,
  q79 holonomy insertions, and closure-strain basin deformations.  Kinetic
  metrics are deliberately not counted as overlap channels; they remain a
  separate canonical-normalization input.  This closes the finite-channel-set
  layer while leaving all channel weights, q79 restrictions, kinetic metrics,
  corrected Yukawa matrices, and RG/threshold matching open.
author:
- Peter Nero
date: May 2026
title: |
  Finite Channel Sets for the Rank-One Lift
---

# Purpose

The hard-leap certificate now has the representation and low-energy Higgs
layers formulated:

```text
E6 27^3 -> SM Yukawa operators,
H_u -> H,
H_d -> H^\dagger.
```

The next missing field is:

```text
finite_channel_sets.
```

This note defines those sets.  It does not compute the channel weights.

# Inputs

We use three already-audited inputs:

```text
1. Rank-one lift correction-channel ledger,
2. E6-to-SM Yukawa operator dictionary,
3. Single-Higgs channel projection.
```

The single-Higgs projected SM operator sectors are:

```text
u:    Q u^c H,
d:    Q d^c H^\dagger,
e:    L e^c H^\dagger,
nuD:  L N^c H.
```

# Channel-Type Convention

`Gamma_f` is the finite set of admissible channel types for sector `f`.

An element of `Gamma_f` records:

```text
sector,
SM operator,
source class,
coefficient status.
```

It does not record:

```text
A_gamma,
S_gamma,
chi_gamma,
family kinetic metric,
canonical Yukawa entry,
RG-matched value.
```

Those remain open.

# Common Source Set

The correction ledger supports the following overlap-channel source classes:

```text
C0_tree_rank_one_seed,
C1_alpha_prime_curvature,
C2_nonperturbative_instanton,
C3_flux_quantized_lens_nil,
C4_retained_non_invariant_modes,
C6_q79_holonomy_insertion,
C7_closure_strain_basin_deformation.
```

We deliberately exclude:

```text
C5_kinetic_metrics
```

from `Gamma_f`, because kinetic metrics act during canonical normalization
after overlap amplitudes are formed.  They are not additional overlap channels.

The later C3 Lens-Nil audit does not remove `C3_flux_quantized_lens_nil` from
these finite sets.  It only blocks using the old Lens-Nil coefficient formulas
as numerical weights until the nonclosed component-form and flux-square
defects are repaired.

# Finite Sets

Define:

```text
Gamma_u =
  {
    (u, Q u^c H, C0_tree_rank_one_seed),
    (u, Q u^c H, C1_alpha_prime_curvature),
    (u, Q u^c H, C2_nonperturbative_instanton),
    (u, Q u^c H, C3_flux_quantized_lens_nil),
    (u, Q u^c H, C4_retained_non_invariant_modes),
    (u, Q u^c H, C6_q79_holonomy_insertion),
    (u, Q u^c H, C7_closure_strain_basin_deformation)
  }.
```

```text
Gamma_d =
  {
    (d, Q d^c H^\dagger, C0_tree_rank_one_seed),
    (d, Q d^c H^\dagger, C1_alpha_prime_curvature),
    (d, Q d^c H^\dagger, C2_nonperturbative_instanton),
    (d, Q d^c H^\dagger, C3_flux_quantized_lens_nil),
    (d, Q d^c H^\dagger, C4_retained_non_invariant_modes),
    (d, Q d^c H^\dagger, C6_q79_holonomy_insertion),
    (d, Q d^c H^\dagger, C7_closure_strain_basin_deformation)
  }.
```

```text
Gamma_e =
  {
    (e, L e^c H^\dagger, C0_tree_rank_one_seed),
    (e, L e^c H^\dagger, C1_alpha_prime_curvature),
    (e, L e^c H^\dagger, C2_nonperturbative_instanton),
    (e, L e^c H^\dagger, C3_flux_quantized_lens_nil),
    (e, L e^c H^\dagger, C4_retained_non_invariant_modes),
    (e, L e^c H^\dagger, C6_q79_holonomy_insertion),
    (e, L e^c H^\dagger, C7_closure_strain_basin_deformation)
  }.
```

```text
Gamma_nuD =
  {
    (nuD, L N^c H, C0_tree_rank_one_seed),
    (nuD, L N^c H, C1_alpha_prime_curvature),
    (nuD, L N^c H, C2_nonperturbative_instanton),
    (nuD, L N^c H, C3_flux_quantized_lens_nil),
    (nuD, L N^c H, C4_retained_non_invariant_modes),
    (nuD, L N^c H, C6_q79_holonomy_insertion),
    (nuD, L N^c H, C7_closure_strain_basin_deformation)
  }.
```

These are finite sets:

```text
|Gamma_u| = |Gamma_d| = |Gamma_e| = |Gamma_nuD| = 7.
```

# Rank-One Seed Caveat

The tree source `C0_tree_rank_one_seed` is included in each sector because the
E6 cubic representation dictionary contains all four SM Dirac Yukawa operator
forms.

This does not mean the rank-one eigenvalue is already assigned to every sector.
The coefficient layer must still decide:

```text
which sector receives the nonzero rank-one tree projection,
which sectors are zero or suppressed at tree level,
which corrections lift the first two family eigenchannels.
```

Thus the finite channel sets are closed, while rank-one sector assignment and
weights remain open.

# Theorem

#### Theorem

Given the correction-channel ledger, the E6-to-SM operator dictionary, and the
single-Higgs channel projection, the admissible sector channel sets
`Gamma_u`, `Gamma_d`, `Gamma_e`, and `Gamma_nuD` are finite and can be chosen
as the four seven-element sets above.  These sets close the support of the
rank-one lift operator at channel-type level.

#### Proof

The E6-to-SM dictionary supplies the four SM operator sectors, and the
single-Higgs projection supplies their low-energy Higgs factors.  The
correction-channel ledger supplies a finite list of admissible overlap source
classes.  Taking the product of each SM sector with the admissible overlap
source list gives four finite sets.

The kinetic-metric source is not included in these sets because it acts after
overlap formation as canonical normalization.  Therefore no entry-wise
normalization knob is hidden inside `Gamma_f`.

Since each `Gamma_f` has seven explicit elements, the finite-channel-set layer
is closed.  The numerical values of `A_gamma`, `S_gamma`, `chi_gamma`, kinetic
metrics, corrected Yukawa matrices, and RG evolution remain uncomputed.

# Bottom Line

The hard-leap blocker is reduced again:

```text
finite_channel_sets            FORMULATED,
channel_weights                OPEN,
q79_channel_restriction        OPEN,
family_kinetic_metrics         OPEN,
delta_yukawa_matrices          OPEN,
canonical_yukawa_matrices      OPEN,
rg_threshold_matching          OPEN.
```

The follow-up q79 channel-restriction certificate now supplies the support rule:

```text
C6_q79_holonomy_insertion -> {79,369},
all non-C6 channels        -> {0}.
```

The next proof layer is:

```text
compute A_gamma, S_gamma, C6 orientation/nonzero status, and kinetic metrics
before any mass comparison.
```
