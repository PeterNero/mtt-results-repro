# MTT Selected BottomCharmTauFormulaImport or RThetaMassSchemeDerivation v1

Status: `MTT_SELECTED_BOTTOMCHARMTAUFORMULAIMPORT_OR_RTHETAMASSSCHEMEDERIVATION_BUILT_FORMULA_FAMILIES_IMPORTED_ROWS_OPEN`.

This artifact imports the external formula/provenance families for b/c/tau map
rows.

```text
external formula source families imported : true
b/c quark running family closed           : true
tau running table/formula family closed   : true
accepted b/c/tau map rows                 : 0
selected Rtheta derivation closed         : false
```

The useful gain is provenance.  RunDec/CRunDec and running fermion-mass table
families are now accepted as formula sources for future replay, but they do not
emit rows by themselves and do not select the MTT branch.

Next artifact: `MTT_Selected_BottomCharmTauRunDecReplay_or_RThetaMassSchemeRows_v1`.
