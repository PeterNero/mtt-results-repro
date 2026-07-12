# MTT Selected PrecisionEquivalenceRows or TrueSMClosureAudit v1

Status: `MTT_SELECTED_PRECISIONEQUIVALENCEROWS_OR_TRUESMCLOSUREAUDIT_POST_PEW_LEDGER_REBUILT_PRECISION_OPEN`.

## Closed Since Previous Precision Table

```text
strict P_EW source rows              = 1
strict direct K_threshold.Omega_H    = 1
strict zero-primitive K ledger       = 10/10
```

This supersedes older precision/QCD/neutrino packets that still listed strict
`P_EW` as open.

## Updated Counts

```text
non-neutrino including QCD theta          = 18
minimal PMNS including QCD theta          = 24
Dirac massive neutrino including QCD theta= 25
Majorana completion including QCD theta   = 27
```

## Remaining True-Precision Blockers

```text
- threshold_mass_scheme_source_rows: OPEN
- full_covariance_profile_likelihood: OPEN
- multi_loop_rg_transport_values: OPEN
- local_qft_precision_observables: TREE_TIER_CLOSED_PRECISION_OPEN
- selected_qasu3_operator_packet: OPEN
- neutrino_absolute_majorana_policy: MINIMAL_OSCILLATION_CLOSED_ABSOLUTE_OPEN
- qcd_theta_strong_cp: SM_PARITY_SLOT_ADMITTED_STRONG_CP_OPEN
- global_true_sm_audit: OPEN_UNTIL_PRECISION_ROWS_CLOSE
```

Accepted true-equivalence precision rows remain `0`; the strict core is closed
but full true-SM precision equivalence is not yet claimed.

Next artifact: `MTT_Selected_PrecisionTransportCovarianceRows_or_FinalTrueSMAudit_v1`.
