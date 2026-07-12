# MTT CONST EW 02 Weak Mixing B16 Source Operator Or Torsion Payload v1

Status: `MTT_CONST_EW_02_B16_PROJECTOR_AND_INTERNAL_FINITEPART_IMPORTED_OPERATOR_TABLES_OPEN`

Label: `CONST-EW-02 / WEAK-MIXING / B16-SOURCE-OPERATOR-OR-TORSION-PAYLOAD`

## Result

B16 imports the current strongest threshold-payload ingredients.

Closed now:

```text
P_perp = I - (1/3)J on the selected rank-3 U1 carrier
Tr(P_perp)/Tr(I_3) = 2/3
selected SU2 index = 1
internal p_a = 29.201650332199108
ordinary rank-one q64 torsion route = rejected
```

The internal finite-part value is:

```text
8*log((2*pi/3)^2) + 8*log(2*(2*pi/3)^2)
```

## What Still Blocks Weak Mixing Closure

This still does not emit `xL`.  The missing strict source objects are:

```text
selected U1Y operator tables
selected D_E/Riesz/Green/dotD or equivalent response data
selected positive spectrum, zeta/heat/torsion finite part
same-scheme SU2 row or cancellation
physical K_gauge anchor
matching scale and RG/threshold scheme
```

## Next

`CONST-EW-02 / WEAK-MIXING / B17-OPERATOR-TABLES-OR-PHYSICAL-MATCHING`
