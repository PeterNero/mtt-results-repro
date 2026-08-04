# MTT Selected Multi-Loop Common-Source Precision Transport or Official Joint Likelihood v1

## Theorem

Select the SMDR v1.3 tadpole-free pure MSbar scheme and the locked measured
source point. SMDR performs the on-shell/low-energy-to-MSbar matching and the
known multi-loop Standard Model running. At the fixed common scale
`Q = 172.5590883453979 GeV`, differentiate the complete numerical map and
propagate the declared source covariance:

```text
C_out = J C_source J^T.
```

The source has `15` coordinates and the output has `8` common-scheme rows:

```text
y_b, y_c, y_tau, lambda, y_t, g_2, g_Y, g_3  at Q = M_t.
```

The result is a positive-definite `8x8` covariance. All `36` symmetric entries
are determined. All `15` BCT-WZH cross entries are nonzero after full matching
and running; none remain missing. This supersedes the first-pass one-loop
structural-zero approximation.

Under the repository's adopted diagonal-input profile theorem, the eight rows
are accepted as true-equivalence precision transport rows at the declared
one-shared-physical-primitive/profile tier. This closes the selected multi-loop
threshold/mass-scheme transport exit.

## Convention Decision

The old WZH replay used `M_W` as an input. The selected SMDR precision scheme
instead uses `G_F`, `M_Z`, low-energy `alpha`, hadronic vacuum polarization,
`alpha_s`, and fermion masses, and predicts `M_W`. A direct numerical pull
between those two coordinate systems is therefore rejected.

The independently locked direct-K Higgs row remains a lawful postcheck:

```text
lambda_direct-K = 0.1260400000
lambda_SMDR     = 0.1262892136
pull            = -1.051692554
```

It passes the declared two-sigma gate and was not used to select the scheme.

## Scope

This closes multi-loop common-scheme transport at the adopted profile tier. It
does not import an official joint input-correlation likelihood and does not
derive the empirical source inputs from MTT. Those are stricter upgrades, not
reasons to reopen the transport calculation.

Implementation references: [SMDR project](https://davidgrobertson.github.io/SMDR/)
and [Martin-Robertson, arXiv:1907.02500](https://arxiv.org/abs/1907.02500).

Next: `MTT_Selected_FinalGlobalTrueSMClosureAudit_AfterMultiLoopPrecision_v1`.
