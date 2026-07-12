# MTT Selected Finite-Part Coefficient External/Corpus Clue Scan v1

## Scope

This scan looks for support for the open object:

```text
MTT_Selected_FinitePartCoefficientSourceRule_or_DirectRadialOperator_v1
```

The current internal family is:

```text
tau_H(k) = 4 + (x1_l2/y1_l2)/(3 - k*s_beta)
k_required = 3.579582815935827
best small rational near miss = 25/7
```

## Corpus Result

Exact support found:

- No pre-existing corpus source emits `25/7` as the selected finite-part
  coefficient.
- No pre-existing corpus source emits `k_required = 3.579582815935827`.
- The only exact `25/7` support is the new near-miss/no-go packet, which keeps
  accepted source rows at `0`.

Strong route support found:

- `routec_selected_source_origin_paper_lemma.packet.json` proves the conditional
  source-origin lemma: if `Phi_fin` is constructed as a functorial
  Galerkin/Cech trace of the selected Strominger/HYM minimizer, then finite
  residual, `rho_E`, metric, `D_E`, Riesz/Green, `dotD`, and C1 payloads become
  theorem-derived selected-source data.
- `routec_hym_operator_values_gate_import.packet.json` says abstract HYM
  existence is no longer the blocker. The blocker is extraction of finite
  `rho_E`, `D_E`, Riesz/Green, `dotD`, and C1/overlap matrices from the selected
  HYM connection.
- `selected_hym_correction_and_gauge_projector_value_table.packet.json` emits
  an honest first trace-free HYM correction in the selected `T3` direction with
  sub-`1e-12` residual, but does not yet emit the full nonlinear HYM connection
  or full finite gauge projector.
- The Obsidian corpus supports the same route through the Strominger/HYM,
  balanced metric, heat-kernel, spectral-action, and coherent-kernel papers.

## External Clues

External sources do not provide a ready-made `25/7` constant. They do support
three exact derivation mechanisms:

1. Balanced/Bergman/HYM route.
   Balanced metrics on stable vector bundles approximate Hermitian-Einstein/HYM
   metrics; finite-dimensional balanced embeddings and generalized Donaldson
   algorithms are the external analogue of the current finite Galerkin packets.

2. Bergman-kernel coefficient route.
   Tian-Yau-Zelditch/Lu/Xu type expansions produce exact curvature-polynomial or
   graph-formula coefficients. This is the most plausible source of a rational
   finite coefficient if `25/7` is real and not a mesh-window artifact.

3. Heat/zeta finite-part route.
   Heat-kernel and zeta finite parts give exact local-invariant coefficients for
   determinant/threshold functionals. This is the cleanest external analogue of
   `K_threshold.Omega_H.lambda` or a direct radial operator.

## Decision

`25/7` must stay quarantined. The numerator coincidence

```text
25 = mesh + 1 = 2*theta_series_cutoff + 1
```

means it may encode finite-window arithmetic, but it is not yet a selected
source coefficient.

## Correct Next Construction

Build the source theorem in one of two ways:

1. Bergman/HYM finite coefficient route:
   - define the selected finite coefficient as a normalized Bergman/Hilbert
     coefficient of the selected q79/F,m=1 HYM branch;
   - compute it from the same `E_H^UV` finite basis, trace, and HYM metric;
   - show either exact equality to `k_required` or a rigorous certified bound;
   - prove the result is independent of mesh/window.

2. Heat/zeta radial operator route:
   - define a selected H-sector Laplace-type/threshold operator on the same
     HYM/Strominger source;
   - compute its zeta/heat finite part;
   - export `tau_H` or `r_H` directly, bypassing rational coefficient fitting.

## Guardrail

External literature may define the proof technology, but MTT closure still
requires the coefficient or direct radial scalar to be emitted from the selected
q79/F,m=1 source, not imported as an external numerical constant.
