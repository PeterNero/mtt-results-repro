# MTT Selected AllBCTExternalRows or FullSMConventionReconciliation v1

Status: `MTT_SELECTED_ALLBCTEXTERNALROWS_OR_FULLSMCONVENTIONRECONCILIATION_BUILT_THREE_ROWS_FULLSM_PROFILE_OPEN`.

This artifact assembles the accepted external b/c/tau mass-scheme rows and
compares them to Huang-Zhou EFT and full-SM `M_Z` table values.

```text
accepted b/c/tau external rows : 3
EFT/full-SM matrix built        : true
full-SM profile closed          : false
selected Rtheta rows closed     : false
```

The gain is that b/c/tau row availability is no longer the blocker.  The
remaining blocker is reconciliation: charm differs from the Huang-Zhou EFT table
at the rowwise table level, and tau has a large EFT-vs-full-SM convention split.

Next artifact: `MTT_Selected_BCTProfileReconciliation_or_RThetaMassSchemeDerivation_v1`.
