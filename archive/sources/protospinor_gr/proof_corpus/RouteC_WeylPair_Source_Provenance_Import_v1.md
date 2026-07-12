# Route-C Weyl-Pair Source Provenance Import v1

## Result

The source-level Weyl-pair provenance is now imported.

Closed at source level:

```text
g1 = Z phase generator
g2 = X shift generator
both have order 3
the selected q79/F,m=1 S3/GS gerbe supplies the central cocycle
active shift (1,1) has selected active-shift provenance
```

This is a real reduction: the remaining blocker is not whether the selected
source has the Weyl carrier. It does. The remaining blocker is the transfer map
from that carrier into the exact C1 response columns.

Still open:

```text
Z -> u,e = I + Z phase column
X -> d,nuD = I + X shift column
normalization in the same B_N/projector/dotD/zero-mode basis
promotion of conditional A_weylpair to selected A_selected
emission of b_selected
```

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_SOURCE_CARRIER_CLOSED_C1_TRANSFER_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1
```
