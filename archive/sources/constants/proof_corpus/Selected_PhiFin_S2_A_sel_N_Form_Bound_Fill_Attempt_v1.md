# Selected PhiFin S2 A_sel,N Form Bound Fill Attempt v1

## Result

Status: `FORM_BOUND_NUMERICALLY_WITHIN_BUDGET_PROVENANCE_OPEN`

The full plan was executed across the three routes:

1. selected source theorem route,
2. explicit selected `A_sel,N` route,
3. quadratic form-bound route.

## Diagnostic Eta

The existing 27-mode matrices are not selected yet, but if provenance were
supplied their diagnostic bound would be:

```text
max diagnostic eta = 1.0
threshold = 2.1932454224643014
passes threshold numerically = True
selected source verified in all sectors = False
```

This is the crucial result: the remaining problem is provenance, not size.

## Sector Eta Values

```json
{
  "H": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 1.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  },
  "L": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 0.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  },
  "N": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 0.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  },
  "Q": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 0.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  },
  "d": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 0.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  },
  "e": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 0.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  },
  "u": {
    "accepted_as_selected_proof": false,
    "eta_if_treated_as_A_sel_N": 0.0,
    "passes_eta_threshold": true,
    "selected_source_verified": false
  }
}
```

## Why It Still Does Not Close

The diagnostic eta cannot be promoted because the current 27-mode matrices are
still model-active scaffold data. The small Strominger solve is rejected because
it is not on the 27-mode `B_N` basis.

## Minimal Fix

```text
Selected_PhiFin_S2_27_Mode_Provenance_Theorem_v1
```

Prove that the existing 27-mode matrices are the finite selected
Phi_fin/Strominger Galerkin compression of the S0 selected smooth source. If
that proof lands, the eta budget is already numerically good enough.
