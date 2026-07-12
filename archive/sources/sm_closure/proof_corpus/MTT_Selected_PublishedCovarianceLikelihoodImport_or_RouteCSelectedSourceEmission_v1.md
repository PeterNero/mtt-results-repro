# MTT Selected PublishedCovarianceLikelihoodImport or RouteCSelectedSourceEmission v1

Status: `MTT_SELECTED_PUBLISHEDCOVARIANCELIKELIHOODIMPORT_OR_ROUTECSELECTEDSOURCEEMISSION_BUILT_EXTERNAL_REPLAY_CLOSED_TRUE_EQ_SOURCE_OPEN`.

This pushes the current external-profile layer home at the declared replay tier.

```text
external profile coordinates admitted : 8
external replay tier closed           : true
published 8x8 likelihood imported     : false
Route-C selected source rows emitted   : false
true SM equivalence closed             : false
```

The move mirrors the earlier SM-parity closure rule: admitted external/central
replay can close the replay tier without selecting sources.  The active frontier
is now true-equivalence value-source work: import/reconstruct the 8x8 likelihood
or emit selected Route-C/no-knob rows.

Next artifact: `MTT_Selected_ExternalProfileReplayFrozenBoundary_or_TrueEquivalenceValueSourceCutset_v1`.
