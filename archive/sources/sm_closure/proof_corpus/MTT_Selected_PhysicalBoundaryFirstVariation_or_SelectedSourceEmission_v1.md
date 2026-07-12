# MTT Selected PhysicalBoundaryFirstVariation or SelectedSourceEmission v1

Status: `MTT_SELECTED_PHYSICALBOUNDARYFIRSTVARIATION_GATE_BUILT_SOURCE_EMISSION_OPEN`.

This artifact makes the active I11 physical gate executable.

```text
current physical source validator rejects     = True
conditional physical source witness validates = True
conditional I11 trace-map bridge validates    = True
```

Route A now requires one theorem-derived same-branch source packet:

- physical first-variation identity
- physical measure equals trace/Frobenius pairing
- phase `R_Z` source selection
- shift `R_X` source selection
- same-source `b_selected` emission
- no extra physical boundary/source term

Route B remains the parallel replacement path: independent selected Galerkin rows
with zero-mode bases, primitive contractions, response matrices, and C33/family
rank tests. The canonical finite C1 replay packet is only a post-emission check.

No observed constants, benchmark rows, locked target values, or residual replay
are used as selectors.

Next artifact: `MTT_Selected_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_IndependentGalerkinRows_v1`.
