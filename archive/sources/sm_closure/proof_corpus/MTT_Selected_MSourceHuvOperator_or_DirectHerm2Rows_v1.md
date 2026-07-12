# MTT Selected MSourceHuvOperator or DirectHerm2Rows v1

Status: `MTT_SELECTED_MSOURCEHUVOPERATOR_OR_DIRECTHERM2ROWS_CONTRACT_RECONCILED_VALUE_ROWS_OPEN`

## Theorem

The active domain now makes the full `M_source` route exact:

```text
M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2
H_uv = B_Huv^* M_source B_Huv
```

Active support:

- `B_Huv` source-orthonormal lift: `True`
- `R_H` restriction closed in the value-source functional: `True`
- Herm(2) row extractors closed: `True`

Current execution:

- selected `H_response` table rows: `0`
- selected `M_source` entries: `0`
- direct `Huu,Hud,Hdd` rows: `0`
- accepted certificates: `0`

The selected diagonal HYM metric remains support only.  It cannot be promoted to
`M_source` or direct Herm(2) rows because `B_Huv^*G_QB_Huv=I_2` is the source
inner-product normalization, not a Higgs mass/strain Hessian.

Next artifact: `MTT_Selected_HResponseTableValueRows_or_DirectHerm2ValueRows_v1`
