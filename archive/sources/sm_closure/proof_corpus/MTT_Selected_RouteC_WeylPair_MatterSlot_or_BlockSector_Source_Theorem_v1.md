# MTT Selected Route-C WeylPair MatterSlot or BlockSector Source Theorem

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_MATTERSLOT_OR_BLOCKSECTOR_SOURCE_THEOREM_REDUCED_TO_HYBRID_GALERKIN_PACKET`

Goal:

```text
Z -> u,e
X -> d,nuD
```

This theorem is not closed yet.  It is reduced to one hybrid packet.

## Route A: High-Scale Matter Slots

The SU(5)/E6 route gives the right structural dictionary:

```text
u,e   -> 10_M clock/phase side
d     -> bar5_M shift side
nuD   -> 1_M singlet, needing a Dirac-neutrino shift rule
```

But q79's selected matter-slot transversality attempt still fails selected
source validation.  The finite `I_3/F` algebra is not the blocker; the selected
zero-mode basis, L2 metrics, projector retention, and same-branch `D_E/dotD`
source are.

## Route B: Block-Sector Route

The honest selected block data gives left/right coherence.  It does not source
the monolithic SU(5) tensor, and it does not split the right-family sectors into
`u,e` versus `d,nuD`.  Therefore Route B needs sector-resolved C1/dotD response
data, not just the current Phi_fin orientation table.

## New Clue

The q79 D7 equivariant selector says clock/shift exchange symmetry is preserved
unless a selected source breaks it.  This helps select the active S3 stack, but
it does not assign matter slots by itself.  For matter routing, the symmetry
must be represented by selected zero modes or broken by a selected operator
source.

## Correct Next Object

Build the hybrid packet:

```text
selected HYM/Strominger source
  -> selected D_E, Riesz/Green, dotD
  -> selected Galerkin zero modes and L2 metrics
  -> selected 10_M/bar5_M/1_M or u,d,e,N sector routing
  -> Weyl-pair A_selected normalization
```

Next artifact: `MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1`.
