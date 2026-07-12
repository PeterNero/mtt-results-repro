# MTT Selected CentralValueTolerancePolicyExecution or FullCovarianceProfile v1

Status: `MTT_SELECTED_CENTRALVALUETOLERANCEPOLICYEXECUTION_OR_FULLCOVARIANCEPROFILE_BUILT_SM_PARITY_TIER_CLOSED`.

The central-value tolerance policy is now executed for the SM-parity tier:

```text
tier 0 central replay          = closed
tier 1 uncertainty sidecars    = closed for current parity audit
tier 2 profile likelihood      = open
SM-parity blocker reduced      = covariance/tolerance policy removed
```

The current SM-parity blockers are now:

```text
[
  "common_scale_Yukawa_and_Higgs_transport",
  "final_integrated_empirical_replay_audit",
  "selected_SM_packet_certificate_integration"
]
```

This does not close full covariance/profile-likelihood equivalence.

Next artifact: `MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1`.
