# MTT Selected HiggsImportedProfileReplay or OfficialLHCHXSWGLikelihood v1

Status: `MTT_SELECTED_HIGGSIMPORTEDPROFILEREPLAY_OR_OFFICIALLHCHXSWGLIKELIHOOD_BUILT_IMPORTED_PROFILE_REPLAY_OFFICIAL_LIKELIHOOD_OPEN`.

This artifact propagates the imported published Higgs decay covariance profile
through the already built total-width and branching-ratio replay Jacobian.

The replay is a locked SM-parity covariance construction:

- input: published ten-channel decay covariance in the repo Higgs basis;
- map: `Gamma_total = sum_i Gamma_i`, `BR_i = Gamma_i / Gamma_total`;
- output: observable covariance/correlation over total width and ten branching
  ratios by `J Cov(Gamma) J^T`.

This closes the imported-profile replay gate. It does not import or claim an
official LHCHXSWG machine-readable likelihood, and it does not close no-knob or
route-A partial-width formula differentiation.
