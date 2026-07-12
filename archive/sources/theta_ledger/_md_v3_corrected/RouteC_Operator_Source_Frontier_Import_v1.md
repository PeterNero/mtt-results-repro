# Route-C Operator-Source Frontier Import

Status: `IMPORTED_OPERATOR_SOURCE_FRONTIER_OPEN`

This imports the current post-cutset Route-C result from the sibling
`mtt-sm-parity-closure` repo into this paper workspace.

## What Is Closed

- The q79/F,m=1 source-level gerbe/Weyl carrier is closed at source level.
- The active deck shift `(1,1)` is forced for nonzero C1 response.
- The primitive-only fixed-fiber span is insufficient for the locked
  Weyl-pair splitter target.
- The enriched Weyl-pair conditional transfer is algebraically exact:
  phase-like `Z` routes to `u,e`, shift-like `X` routes to `d,nuD`.
- Alpha1/dotD are no longer the main final-source blockers in the latest
  actual-fill witness.

## What Is Not Closed

The selected operator-level source is still open.  Conditional Weyl-pair
algebra cannot be promoted to `A_selected` until MTT emits the same-source
operator/overlap packet, including selected routing, normalization, and
primitive contractions.

The same-source packet validator currently rejects the fill:

- required fields: 7
- selected emissions: 0
- support-only fields: 6
- missing hard field: selected `1_M` Dirac-neutrino routing

## Current Minimal Frontier

The first subpacket is now:

`MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1`

It reduces the proof to two live lanes:

1. Rank-2 non-split `V_alpha` L2/cohomology lane:
   selected branch orientation, Pic0/torsion character, raw transition data,
   and stability/source selection are still required.
2. Finite Route-C HYM/Strominger residual lane:
   actual selected rho_E, metric, D_E, residual, Riesz/Green, and dotD values
   from the same branch are still required.

Next required artifact:

`MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1`

This is not full SM closure.  It is a sharper proof frontier: source-level
selection is ahead of operator-level emission, and the next calculation must
promote one of the two lanes above without using observed masses, CKM, PMNS,
or CP as selectors.
