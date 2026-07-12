# MTT Selected Route-C WeylPair SourceToC1 Transfer Map

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN`

This artifact defines the conditional transfer map from the source-level Weyl
carrier to the C1 packet columns:

```text
T(Z) = sector_route(u,e; I + Z)
T(X) = sector_route(d,nuD; I + X)
```

## Result

The transfer is exact as an algebraic map.  It reproduces the phase and shift
columns used by the conditional Weyl-pair `A` operator with zero residual up to
roundoff.

## Remaining Gap

The selected artifacts still do not emit the sector-routing rule itself.  The
next lemma must derive, from the selected q79/F,m=1 S3/GS Route-C source, why:

- `Z` routes to the `u,e` C1 response as `I + Z`,
- `X` routes to the `d,nuD` C1 response as `I + X`,
- the coefficient normalization is the one used by the conditional solve.

No observed SM constants, diagnostic labels, or lifted flags are used to select
that routing.

Next artifact: `MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1`.
