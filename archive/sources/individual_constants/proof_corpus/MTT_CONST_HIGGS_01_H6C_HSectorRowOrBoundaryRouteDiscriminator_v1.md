# MTT CONST HIGGS 01 H6C H-Sector Row Or Boundary Route Discriminator v1

Status: `MTT_CONST_HIGGS_01_H6C_ROW_ABSENT_BOUNDARY_ROUTE_IDENTIFIED`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-HSECTOR-ROW-OR-BOUNDARY-ROUTE-DISCRIMINATOR`

## Result

```text
actual K_H^(4)[12,12,12,12] row found            False
D-term boundary route identified                 True
standard boundary factor                         1/8
old 1/4 factor high by two under SM convention   True
selected beta/tan_beta source                    False
Higgs quartic numeric value                      False
strict no-knob Higgs closure                     False
```

## Route Split

Route A remains the intrinsic finite-row route:

```text
emit K_H^(4)[12,12,12,12]
```

Route B is the corpus-supported boundary route:

```text
lambda = (g^2 + g'^2) cos^2(2 beta) / 8
```

The old Theta execution text used a factor `1/4`; the verification/correction
notes already identify the standard SM-normalized MSSM tree-level factor as
`1/8` for `V=-m^2 |H|^2 + lambda |H|^4`.

## Meaning

This is progress because it prevents two different meanings of "Higgs quartic"
from being mixed.  The intrinsic row route and D-term boundary route are both
legal superset paths, but neither can use measured Higgs mass or target
`lambda_H` as a selector.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-SELECTED-DTERM-BOUNDARY-OR-BETA-SOURCE`
