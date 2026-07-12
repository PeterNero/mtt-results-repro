# MTT Selected HiggsRouteADerivativeEngineExecution or PrecisionDecision v1

Status: `MTT_SELECTED_HIGGSROUTEADERIVATIVEENGINEEXECUTION_OR_PRECISIONDECISION_BUILT_LEPTONIC_DERIVATIVES_QCD_EW_OPEN`.

This artifact executes the first route-A Higgs derivative engines: the tree-level
leptonic rows `H_to_tau_tau` and `H_to_mu_mu`.

For each row it records:

- the analytic formula;
- the central partial width from downstream reference inputs;
- analytic derivatives with respect to `G_F`, `M_H`, and the lepton mass;
- first-order uncertainty propagation;
- a diagnostic comparison against the imported profile, with no source
  selection or fitting.

This closes the leptonic derivative block only. QCD fermionic rows, loop rows,
off-shell rows, electroweak/radiative corrections, total precision Higgs
closure, true SM equivalence, and no-knob closure remain open.
