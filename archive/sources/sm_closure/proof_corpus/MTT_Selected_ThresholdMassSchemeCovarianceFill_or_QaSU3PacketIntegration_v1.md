# MTT Selected ThresholdMassSchemeCovarianceFill or QaSU3PacketIntegration v1

Status: `MTT_SELECTED_THRESHOLDMASSSCHEMECOVARIANCEFILL_OR_QASU3PACKETINTEGRATION_BUILT_INTERNAL_BENCHMARK_CLOSED`.

The diagnostic RG engine now has an internal RK convergence benchmark:

```text
max delta 256->512 = 1.554400e-15
tolerance          = 1.0e-12
internal benchmark = True
```

This closes the local integrator sanity check only. Accepted `M_Z` Yukawa/Higgs
values still require threshold matching, mass-scheme conversion, covariance or
profile-likelihood execution, and benchmark validation.

The Qa/SU3 color/operator packet remains a separate source-side gate.

Next artifact: `MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1`.
