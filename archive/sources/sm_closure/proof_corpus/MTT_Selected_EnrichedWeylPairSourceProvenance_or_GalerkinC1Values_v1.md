# MTT Selected EnrichedWeylPairSourceProvenance or GalerkinC1Values v1

Status: `MTT_SELECTED_ENRICHEDWEYLPAIRSOURCEPROVENANCE_OR_GALERKINC1VALUES_BUILT_STATIC_PROVENANCE_CLOSED_DYNAMIC_VALUES_OPEN`.

This closes the static enriched Weyl-pair provenance:

```text
Z / clock / phase -> u,e
X / shift         -> d,nuD
1_M = N^c         -> Dirac-neutrino shift side
finite trace transfer normalization selected
```

This is now source-tier data, not a target fit.  It uses the selected qutrit
Weyl carrier, active shift `(1,1)`, all six SM-slot functor arrows, and the
selected transported-projector trace normalization.

The dynamic C1 value tier remains open.  The conditional value run is still
ready:

```text
rank(A_conditional) = 2
condition number    = 1.0000000000000002
deltaTheta          = [1.0, 1.0000000000000002]
```

But `A_selected`, `b_selected`, and `deltaTheta_C1` are not promoted until the
dynamic transfer tensor, primitive C1 contractions, Hessian/source vector, or
honest selected Galerkin C1 values are emitted.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1`.
