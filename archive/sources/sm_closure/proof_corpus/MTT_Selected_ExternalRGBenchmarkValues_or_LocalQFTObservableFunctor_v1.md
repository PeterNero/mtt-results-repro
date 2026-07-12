# MTT Selected ExternalRGBenchmarkValues or LocalQFTObservableFunctor v1

Status: `MTT_SELECTED_EXTERNALRGBENCHMARKVALUES_OR_LOCALQFTOBSERVABLEFUNCTOR_BUILT_LOCAL_BENCHMARK_AND_FUNCTOR_INTERFACE`.

This artifact advances both allowed lanes:

- the accepted first-pass common-scale values pass an independent local 512-step
  RG replay benchmark against the accepted 256-step packet;
- the local-QFT observable functor interface `Obs_SM^MTT` is typed from the
  SM-sector and QM/QFT/GR recovery interfaces.

This is a superset move. It combines local RG replay, QFT recovery structure,
SM embedding structure, and MTT typed parameter slots. The target is external
reproducibility and observable-interface typing, not source selection.

Still open:

- external literature RG benchmark values
- precision threshold and pole-to-running maps
- full covariance/profile likelihood values
- local QFT observable values/correlator replay
- QM/GR measurement and response interfaces
- actual selected Qa/SU3 operator packet
