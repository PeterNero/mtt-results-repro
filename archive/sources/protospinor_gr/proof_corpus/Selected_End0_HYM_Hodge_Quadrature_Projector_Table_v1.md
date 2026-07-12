# Selected End0 HYM/Hodge/Quadrature/Projector Table v1

## Result

The equal-radius Hodge/Lambda and theta quadrature side of the End0 table is
built.

The selected Ext row has exact norm:

```text
||eta_00||^2 = 1/sqrt(32)
eta_00^unit = 32^(1/4) * eta_00
```

The Lambda convention is:

```text
Lambda(i*ea wedge ebar_b) = delta_ab
Lambda(i*e1 wedge ebar1 - i*e2 wedge ebar2) = 0
Lambda(i*e2 wedge ebar2 - i*e3 wedge ebar3) = 0
```

The End0 operator template is now:

```text
barpartial_End0 = barpartial_Iwasawa + ad(A_split_AH + eta_00^unit + HYM_correction)
```

## Boundary

This does not emit selected nonabelian HYM correction coefficients and does not
emit the numerical gauge projector. Those depend on the selected HYM
linearization and metric inner product. The full oriented Hodge-star/wedge sign
table is also left as the next table refinement, because the HYM primitive
equation only needs the Lambda contractions fixed here.

Status:

```text
SELECTED_END0_HODGE_QUADRATURE_TABLE_BUILT_HYM_PROJECTOR_VALUES_OPEN
```

Next:

```text
MTT_Selected_HYM_Correction_and_Gauge_Projector_Value_Table_v1
```
