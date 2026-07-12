# Route-C Weyl-Pair SourceToC1 Transfer Import v1

## Result

The conditional source-to-C1 transfer map is now imported.

It is exact as algebra:

```text
T(Z) = sector_route(u,e; I + Z)
T(X) = sector_route(d,nuD; I + X)
phase residual = 0
shift residual = 0
```

The remaining blocker is not the transfer calculation. It is the selected source
of the sector-routing rule and normalization:

```text
why Z routes to u,e as I + Z
why X routes to d,nuD as I + X
why the coefficient normalization is the conditional-solve normalization
```

Until that is proved, the conditional transfer map cannot be promoted to
selected `A_selected`, and `b_selected` remains open.

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_IMPORTED_CONDITIONAL_EXACT_ROUTING_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1
```
