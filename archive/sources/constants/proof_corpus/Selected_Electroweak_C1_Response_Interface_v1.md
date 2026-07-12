---
title: Selected Electroweak C1 Response Interface
author:
- Peter Nero
date: May 2026
---

# Claim

The selected electroweak C1 response map can be computed from a finite raw
three-factor threshold response vector.

The current corpus does not provide that vector, so the calculator refuses the
open template.  This is the correct rigorous status.

# Algebra

Let the raw per-`v1_tilde` threshold response of the selected `alpha_1`
curvature row be

```text
p = (p_1,p_2,p_3)
```

in the gauge-factor basis

```text
(U1, SU2, SU3).
```

The universal trace

```text
<p> (1,1,1)
```

renormalizes the common gauge-normalization slot and must not be confused with
the trace-free electroweak exceptional split.  Therefore the selected
exceptional response is

```text
q = p - <p>(1,1,1).
```

In the selected basis

```text
chi_1 = (1,-1,0),
chi_2 = (0,1,-1),
```

the coordinates are

```text
m1 = q_1,
m2 = -q_3.
```

Thus

```text
P_EW(alpha_1) = (m1,m2),
c1 = v1_tilde m1,
c2 = v1_tilde m2.
```

For the weak-angle split alone, the trace cancels:

```text
lambda_12 = 2m1 - m2 = q_1 - q_2 = p_1 - p_2.
```

and

```text
Delta_G,12 = v1_tilde lambda_12/(4pi).
```

# Executable Interface

The calculator is:

```text
scripts/compute_electroweak_c1_response.py
```

The open source-data template is:

```text
certificates/selected_electroweak_c1_response.template.json
```

It requires selected per-`v1_tilde` vectors for:

```text
local_determinant,
torsion_curvature,
bundle_index,
scheme_counterterm,
basis_transport.
```

The terms are additive raw responses in the `(U1,SU2,SU3)` basis.  Each term
must be supplied by selected local threshold data, not by fitting the observed
weak angle or importing Execution I matching coefficients.

# Diagnostic Fixture

The diagnostic fixture

```text
certificates/selected_electroweak_c1_response_diagnostic_fixture.json
```

uses the response vector implied by the Execution I diagnostic:

```text
p = (0.7642555835410925,
     -1.4298975433994635,
      0.6656419598583709).
```

It computes

```text
P_EW(alpha_1) = (0.7642555835410925,-0.6656419598583709),
lambda_12 = 2.194153126940556,
c1 = 0.31,
c2 = -0.27,
Delta_G,12 = 0.07082394967589342.
```

This fixture proves that the calculator implements the reduction correctly.
It does not select the physical response.

# Current Status

The open template currently fails with missing primitive response data.  This
is not a software failure; it is the mathematical gate:

```text
selected local threshold computation
  -> p = (p_1,p_2,p_3)
  -> P_EW(alpha_1)
  -> c1,c2.
```

# Certified Status

```text
PEW_ALPHA1_RESPONSE_INTERFACE_BUILT_VALUES_OPEN
```

