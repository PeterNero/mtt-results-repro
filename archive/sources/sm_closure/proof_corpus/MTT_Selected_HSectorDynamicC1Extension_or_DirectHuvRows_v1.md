# MTT Selected HSectorDynamicC1Extension or DirectHuvRows v1

Status: `MTT_SELECTED_HSECTORDYNAMICC1EXTENSION_OR_DIRECTHUVROWS_BHUV_EHUV_BINDING_IMPORTED_MSOURCE_OR_DIRECTROWS_OPEN`

## Theorem

H7B1N's two-route cutset is imported, but updated against the active repo.
The older constants-side missing-basis/metric/`B_Huv` clauses are partly
superseded here:

- finite `E_H^UV` source labels: `['H_u', 'H_d^dagger']`
- source IDs: `{'H_d_dagger': 'Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0', 'H_u': 'Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0'}`
- selected diagonal HYM binding on `E_H^UV`: `True`
- symbolic source-orthonormal `B_Huv` lift emitted: `True`

The H-sector dynamic C1 route is still absent:

- current C1 target sectors: `['d', 'e', 'nuD', 'u']`
- H/Huv C1 rows: `0`

The direct Huv route is now sharper.  We no longer need to search for the
two-column Higgs lift; the active blocker is:

```text
M_source on B_Huv, or direct certified Huu,Hud,Hdd rows.
```

Current emitted `Huv` rows: `0`.

Next artifact: `MTT_Selected_MSourceHuvOperator_or_DirectHerm2Rows_v1`
