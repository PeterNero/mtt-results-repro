---
title: Selected Electroweak C1 Response Fill Attempt
author:
- Peter Nero
date: May 2026
---

# Claim

The current corpus does not contain enough selected local threshold data to fill

```text
certificates/selected_electroweak_c1_response.template.json.
```

This is a negative closure result, but a useful one: it prevents a false
electroweak closure and identifies the exact primitive data still needed.

# Attempted Fill

The template requires selected per-`v1_tilde` raw threshold response vectors in
the `(U1,SU2,SU3)` basis for:

```text
local_determinant,
torsion_curvature,
bundle_index,
scheme_counterterm,
basis_transport.
```

The weak-angle split only needs

```text
lambda_12 = p_1 - p_2,
```

so any purely universal trace contribution is irrelevant for the split.
However, non-universal components of any of the five terms would affect
`lambda_12` and must be selected rather than guessed.

# Source Audit

## Heterotic/Flux Source

The heterotic flux source supplies the correct structural home:

```text
g^{-2} = Re S
```

up to threshold corrections, and says torsional effects enter through higher
`alpha'` and one-loop thresholds.

But it also says these thresholds are not computed in the current construction.
Therefore it cannot fill the local determinant, torsion-curvature, or
scheme-dependent non-universal response vectors.

## Execution I Source

Execution I supplies the exceptional basis

```text
chi_1 = (1,-1,0),
chi_2 = (0,1,-1),
```

but the coefficients are obtained by solving exact matching conditions:

```text
c1 = 0.31,
c2 = -0.27.
```

These are valid diagnostics, not selected primitive threshold data.  Using them
to fill the template would import the answer from gauge matching.

## Superset/Threshold Source

The superset threshold source gives a minimum-norm trace-free threshold vector
subject to crossing conditions.  This is a constrained fit/diagnostic, not a
selected local `alpha_1` response computation.

# Term Status

| Template term | Status | Reason |
|---|---|---|
| `local_determinant` | `OPEN` | No selected analytic torsion, spectrum, or determinant ratio is provided. |
| `torsion_curvature` | `OPEN_SCALAR_SOURCE_ONLY` | The scalar source `v1_tilde alpha_1` is selected, but the electroweak response vector is not. |
| `bundle_index` | `OPEN_FOR_THRESHOLDS` | Topology fixes charges/anomalies, not the non-universal local threshold amplitude. |
| `scheme_counterterm` | `TRACE_IRRELEVANT_NONUNIVERSAL_OPEN` | Universal trace drops from `lambda_12`; non-universal scheme response is not selected. |
| `basis_transport` | `OPEN` | No selected electroweak threshold basis-transport vector is supplied. |

# Consequence

The template remains intentionally open.  The diagnostic fixture remains useful
only as a calculator test.

The exact next data object is:

```text
SelectedElectroweakC1PrimitiveResponseCertificate:
  local_determinant: [p1,p2,p3]
  torsion_curvature: [p1,p2,p3]
  bundle_index: [p1,p2,p3]
  scheme_counterterm: [p1,p2,p3]
  basis_transport: [p1,p2,p3]
```

with each vector derived from selected local threshold data and with no
observed electroweak couplings, weak angle, or Execution I fitted exceptional
coefficients used as inputs.

# Certified Status

```text
PEW_ALPHA1_TEMPLATE_FILL_BLOCKED_SELECTED_THRESHOLD_DATA_MISSING
```

