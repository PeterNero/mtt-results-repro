# MTT Selected BCTFormulaImport or SelectedThresholdRowDerivation v1

Status: `MTT_SELECTED_BCTFORMULAIMPORT_OR_SELECTEDTHRESHOLDROWDERIVATION_BUILT_EXTERNAL_BCT_ROWS_ACCEPTED_SELECTED_DERIVATION_OPEN`.

Both requested lanes were tried.

```text
external BCT formula/table import closed : true
accepted BCT external map rows           : 3
selected BCT Rtheta source rows          : 0
same-source selected derivation closed   : false
```

The external lane now has bottom, charm, and tau map rows attached to the
provisional `R_theta^(1,diag)` validation harness.  The selected-source lane
still requires `SelectedRouteCStromingerGalerkinResidualSolve`; formal-lift
diagnostics pass, but the honest selected-source payload remains unpromoted.

Next artifact: `MTT_Selected_BCTSelectedSourceRepair_or_FullProfileUpgrade_v1`.
