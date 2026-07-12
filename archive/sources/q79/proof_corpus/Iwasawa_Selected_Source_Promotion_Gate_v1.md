---
abstract: |
  We formulate an executable promotion gate for Iwasawa finite rho_E/D_E data.
  The gate separates validator prototypes from selected proof evidence.  At the
  rho_E-source level, mesh, metric, sector, and face-graph diagnostics must pass,
  and a finite table that is a face-graph coboundary cannot be promoted from
  rho_E data alone.  At the D_E-response level, the Route C residual, D_E,
  Riesz, Green, and dotD validators must pass, and the dotD source and
  horizontal response norms must be nonzero.  This keeps the noncommuting
  pure-gauge prototype useful as a validator stress test while forbidding it as
  selected SM evidence.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Selected Source Promotion Gate
---

# Purpose

The current finite `rho_E` stack can validate increasingly rich tables:

```text
scalar phase,
diagonal phase,
Fourier-rotated off-diagonal phase,
pure-gauge nonabelian tables.
```

The face-graph coboundary diagnostic then showed the important caution:

```text
noncommuting finite table values can still be pure gauge on the validator graph.
```

This note adds the promotion rule.  A finite artifact is not allowed to become
selected proof evidence merely because it passes a local validator.

# Promotion Packet

The executable packet schema is:

```text
IwasawaSelectedSourcePromotionPacket.v1.
```

It is consumed by:

```text
scripts/validate_iwasawa_selected_source_promotion.py
```

The packet must declare:

```text
target_level = rhoE_source or de_response,
source_kind = typed_Cech_monad_transition_data or finite_HYM_Strominger_solve,
selected_source_verified = true,
no_observed_flavor_inputs = true.
```

It must also explicitly reject the known shortcut modes:

```text
uses_execution_ii_benchmarks = false,
uses_observed_masses_or_mixings = false,
uses_diagnostic_h1_three_as_selected = false,
uses_pure_gauge_prototype_as_selected = false.
```

# rhoE Source Promotion

At the `rhoE_source` level the gate runs:

```text
validate_iwasawa_rhoE_mesh.py,
validate_iwasawa_rhoE_metric.py,
validate_iwasawa_sector_maps.py,
detect_iwasawa_face_graph_coboundary.py.
```

The source-level rule is deliberately strict:

```text
if face_graph_coboundary = true, rhoE_source promotion fails.
```

This does not say a future selected bundle must have a nontrivial finite face
graph in every discretization.  It says the finite `rho_E` table alone cannot
be the proof source if that finite table trivializes as:

```text
rho(source -> target) = U(source)^(-1) U(target).
```

# D_E Response Promotion

At the `de_response` level the gate additionally runs:

```text
validate_iwasawa_route_c_residuals.py,
validate_iwasawa_de_action.py,
validate_iwasawa_riesz_gap.py,
validate_iwasawa_reduced_green.py,
validate_iwasawa_dotd_response.py.
```

Here the correct surviving route is possible:

```text
a face-graph-coboundary rho_E table may still be part of a selected source
if the selected D_E/dotD response is nonzero and survives the horizontal
response validator.
```

The validator therefore computes from the dotD-response data:

```text
max source norm,
max horizontal response norm,
sectors with nonzero horizontal response.
```

It requires the source and response norms to be strictly positive above the
declared tolerance.

# Consequence

The pure-gauge nonabelian prototype remains useful, but only as this:

```text
a stress test proving the validators can carry noncommuting finite matrices.
```

It is not a selected SM proof source.

The next admissible candidate must be one of:

```text
1. a selected non-coboundary rho_E source from typed Cech/monad data, or
2. a selected finite HYM/Strominger D_E response whose dotD source and
   horizontal response norms are nonzero.
```

# What This Does Not Close

This gate does not construct:

```text
selected rho_E,
selected D_E,
selected dotD_alpha1,
primitive C1 contractions,
Yukawa matrices,
CKM angle magnitudes,
full SM closure.
```

It closes the promotion discipline needed before those data can be accepted.
