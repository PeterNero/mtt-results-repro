# MTT Selected C1ToBHuvProjectionTensor or FHuvRows v1

Status: `MTT_SELECTED_C1TOBHUVPROJECTIONTENSOR_OR_FHUVROWS_CONTRACT_CLOSED_HIGGS_SLOT_TENSOR_OPEN`

## Theorem

The required projection tensor is now precisely typed:

```text
T_C1<-Huv : span(B_Huv[H_u], B_Huv[H_d^dagger]) -> selected C1 variation coordinates
M_Huv = T_C1<-Huv^* (A^T A)_C1 T_C1<-Huv
```

Current data provide both sides of the interface, but not the tensor between
them:

- C1 variation routing: `['d', 'e', 'nuD', 'u']` with `72` rows
- Higgs source IDs: `['H_u', 'H_d^dagger']`
- Higgs rows inside the C1 72-slot routing: `0`

Therefore the existing C1 routing is matter-sector routing, not a Higgs
`B_Huv` projection tensor.  C2 Higgs source IDs, C3 diagonal HYM eigenlines, and
the compressed `A^T A` payload are all useful support but not substitutes for
`T_C1<-Huv`.

Accepted `F_Huv` rows: `0`.
Selected `s_beta` retained as projection support: `0.004701083905943647`.

Next artifact: `MTT_Selected_HiggsC1VariationSlotExtension_or_AmbientHessianRows_v1`
