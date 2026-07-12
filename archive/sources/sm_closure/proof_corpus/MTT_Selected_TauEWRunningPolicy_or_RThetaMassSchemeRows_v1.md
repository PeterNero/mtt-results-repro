# MTT Selected TauEWRunningPolicy or RThetaMassSchemeRows v1

Status: `MTT_SELECTED_TAUEWRUNNINGPOLICY_OR_RTHETAMASSSCHEMEROWS_BUILT_TAU_EFT_TABLE_ROW_FULLSM_RTHETA_OPEN`.

This artifact imports the Huang-Zhou charged-lepton running-mass table and
accepts the EFT `M_Z` tau row as the external `tau_pole_rest_to_running_lepton`
map row.

```text
tau EFT MZ mass               : 1.74743 GeV
tau EFT MZ Yukawa             : 0.010036726570212717
accepted b/c/tau external rows: 3
full-SM tau convention closed : false
selected Rtheta row closed    : false
```

The row is accepted only as an external map row in the same low-energy `M_Z`
mass-scheme layer as the b/c transport rows.  The full-SM tau row remains
reserved for convention/profile reconciliation.

Next artifact: `MTT_Selected_AllBCTExternalRows_or_FullSMConventionReconciliation_v1`.
