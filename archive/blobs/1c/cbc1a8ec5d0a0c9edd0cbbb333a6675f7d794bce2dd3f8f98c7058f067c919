---
title: |
  Selected Matter Source: Two-Path Exploration
author: MTT proof reproduction program
---

# Target

The selected matter-slot source gate made the remaining problem exact:

```text
derive the selected source for
10_M   = clock-polarized qutrit slot,
bar5_M = shift-polarized qutrit slot.
```

There are two honest routes left.

# Path A: Selected HYM/Strominger Source

This route tries to replace the Route C smoke residuals with an actual selected
HYM/Strominger source.  Its job is to justify selectedness:

```text
selected background,
retarded q79/F branch,
selected D_E,
selected dotD_alpha1,
selected projector retention.
```

What is already strong:

```text
the Fu-Yau/Strominger charge sector is closed for the q79 terminal branch,
the Route C q79/F branch packet exists,
rho_E mesh, rho_E metric, and sector-map validators pass honestly,
the lifted selected-flag smoke packet shows the algebra can pass.
```

What is still missing:

```text
the Route C residual is not a selected solve,
D_E/Riesz/Green/dotD validators fail honestly without selected-source flags,
the closed Z7 charge sector does not by itself produce the 10_M/bar5_M
zero-mode bases.
```

So Path A is necessary, but not sufficient alone.

# Path B: Spectral Galerkin Zero Modes

This route computes the actual matter-slot data once a selected operator is
available:

```text
family zero modes,
L2 metrics,
Riesz projector,
reduced Green operator,
dotD response,
U_10 and U_bar5.
```

What is already strong:

```text
the spectral Galerkin template exists,
Riesz/Green/dotD validators exist,
the left-invariant attempt proves the invariant seed is only rank one,
so the need for sector-resolved or non-invariant data is explicit.
```

What is still missing:

```text
selected D_E,
kernel dimension three,
positive complement gap,
truncation error bound,
sector projection maps,
dotD_alpha1 and reduced Green data.
```

So Path B is computationally concrete, but it cannot justify selectedness by
itself.

# Coupled Conclusion

Neither path closes alone from the current repo state.

The correct next route is hybrid:

```text
Path A supplies selected HYM/Strominger origin for D_E.
Path B uses that selected D_E to compute the zero modes and matter-slot
transport.
Then the selected matter-slot source validator can be rerun.
```

In short:

```text
selectedness first, spectral computation second.
```

# Executable Artifact

The route comparison is produced by:

```text
scripts/explore_selected_matter_source_two_paths.py
```

It writes:

```text
candidate_data/selected_matter_source_two_path_exploration.candidate.json
certificates/selected_matter_source_two_path_exploration_certificate.json
```

# Guardrail

This exploration does not claim full SM closure, selected `D_E`, or a selected
ordered SU(5) packet.  It only identifies the right combined route and the
first missing packet:

```text
selected HYM/Strominger operator/source packet for D_E.
```
