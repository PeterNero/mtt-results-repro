# MTT Selected HiggsOfficialProfile or RouteAFormulaDifferentiation v1

Status: `MTT_SELECTED_HIGGSOFFICIALPROFILE_OR_ROUTEAFORMULADIFFERENTIATION_BUILT_REPLAY_JACOBIAN_FORMULA_DIFF_OPEN`.

This artifact does not find or import an official full Higgs likelihood/profile.
Instead it constructs the differentiable replay layer for the current
source-derived covariance model:

- `Gamma_total = sum_i Gamma_i`;
- `BR_i = Gamma_i / Gamma_total`;
- covariance propagates by `J Cov(Gamma) J^T`.

This closes replay-map differentiation only. It does not differentiate the
underlying route-A physics partial-width formulas and does not promote Higgs
precision total-width or branching-ratio closure.
