# MTT Selected PSM C1 01 SourceRuleEmission or PSM C1 04 bSelectedSidecar v1

Active labels: `PSM-C1-01` and `PSM-C1-04`.

This artifact separates the patched and unpatched statuses.

Patched lane:

- the explicit local `DifferentiatedPhiFinC1ResidualProjectorAxiom` supplies the
  physical application rule
- `R_Z`, `R_X`, `b_selected`, `A_selected`, `deltaTheta_C1=[1,1]`, and sector
  response matrices are available inside the patched proof spine
- the Route-A strict validator passes for the patched payload

Unpatched lane:

- `PSM-C1-01` remains open
- `PSM-C1-04` remains open
- Route A still needs the five strict fields:
  physical action restriction, zero extra boundary/source, phase `R_Z`, shift
  `R_X`, and same-source `b_selected`
- Route B still needs independent row-kernel/Galerkin source execution

So this is progress, but not an unpatched true-equivalence closure.

Next artifact: `MTT_Selected_PSM_C1_01_UnpatchedSourceLemma_or_ROUTE_B_RowKernelExecution_v1`.
