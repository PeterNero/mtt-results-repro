# MTT Selected Step70 HeatTorsionPrefactorBackimport or RowLocalFrontier v1

Status: `MTT_SELECTED_STEP70_HEATTORSION_PREFACTOR_BACKIMPORT_CLOSED_ROWLOCAL_OPEN`.

## What Closed

Step70 back-imports the already selected finite heat/torsion source slot into
the Step69 prefactor contract:

```text
finite heat trace source subslot                    : closed
positive-complement pseudodeterminant source subslot: closed
prefactor factorization rows                        : 10
accepted finite heat/torsion subsources             : 2
accepted full prefactor source rows                 : 0
accepted Omega source rows                          : 0
accepted scalar values                              : 0
```

The prefactor slots are now factored as:

```text
C_HYMthr.* = D_fin.class * L_rowlocal.* * T_scheme.*
```

`D_fin.class` is selected by the finite 27-mode heat/pseudodeterminant response.
The row-local overlap factor `L_rowlocal.*` and convention/threshold factor
`T_scheme.*` remain open.

## Why This Is Not Yet Full Closure

The finite heat/torsion response has only two source classes here:

```text
source classes: ['H_sector', 'family_sector']
prefactor slots: 10
```

It has no generation-resolved labels and no `u/d/e` split inside the family
class.  Therefore it cannot by itself emit the ten row-local prefactor source
rows required by Step69.

As a diagnostic only, the admitted replay prefactors vary inside the family
class by a factor of `26.9415349844`.  This is not used as a
selector; it only confirms that row-local factors are numerically necessary.

## Boundary

The determinant/heat/torsion source subslot is no longer missing.  The live
frontier is now selected row-local HYM overlap/threshold factors plus the
scale/scheme/loop convention and value payloads.

Next artifact: `MTT_Selected_RowLocalHYMOverlapThresholdPrefactors_or_StrictOmegaAcceptance_v1`.
