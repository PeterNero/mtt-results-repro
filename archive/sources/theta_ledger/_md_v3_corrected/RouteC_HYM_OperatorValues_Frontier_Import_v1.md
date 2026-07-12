# Route-C HYM Operator-Values Frontier Import

Status: `IMPORTED_HYM_OPERATOR_VALUES_FRONTIER_OPEN`

This imports the deepest audited Route-C progress currently found in the
`mtt-sm-parity-closure` repo after the operator-source frontier.

## What Advanced

- The selected rank-2 L2/cohomology input closes:
  `h1=8`, a nonzero Ext class is selected, and the non-split `V_alpha` input is
  available without observed flavor data.
- The ordered source layer is promoted for the Chern/H1/ordinary-curvature
  layer, with Pic0 quotienting only at that layer.
- The reduced Appell-Humbert global destabilizer enumeration is proved:
  the Hom-to-L destabilizer case is empty and the Hom-to-Q case reduces to the
  six central-neutral candidates already obstructed.
- The rank-one torsion-free destabilizer reduction is proved: destabilizing
  rank-one torsion-free subsheaves reduce to reflexive line hulls.
- The equal-radius Gauduchon/HYM bridge closes the abstract existence bridge,
  but not the concrete operator values.

## Current Frontier

The abstract existence/stability side is no longer the main blocker.  The next
theorem must extract finite operator data from the selected HYM connection:

```text
selected V_alpha + selected equal-radius metric + selected HYM connection
  -> selected cover/basis/quadrature
  -> rho_E, metric, D_E, Riesz/Green, dotD, C1/overlap matrices
```

The next required artifact is:

`MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1`

## What Remains Open

- selected HYM connection/operator values
- same-source `D_E`, Riesz/Green, and dotD
- operator-layer Pic0 or holonomy-sensitive quotient
- same-source Chern-Weil/Green-Schwarz row
- primitive C1 contractions and overlap matrices
- full no-knob Standard Model closure

This is still not a full proof of SM closure.  It is a major reduction: the
problem has moved from "does the selected bundle/stability picture exist?" to
"compute the selected HYM-derived finite operator matrices from the same
source."
