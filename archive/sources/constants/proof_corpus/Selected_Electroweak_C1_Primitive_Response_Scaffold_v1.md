---
title: Selected Electroweak C1 Primitive Response Scaffold
author:
- Peter Nero
date: May 2026
---

# Claim

The electroweak C1 primitive-response problem can be reduced from five template
terms to three physical source terms, without using observed electroweak data.

The reduced open template is:

```text
certificates/selected_electroweak_c1_response_reduced.template.json
```

# Fixed Basis

The response calculator defines the raw response directly in the gauge-factor
basis

```text
(U1, SU2, SU3).
```

Therefore no additional basis-transport vector is needed in this interface.
The basis transport term is fixed to

```text
basis_transport = (0,0,0).
```

This is not a dynamical claim.  It is a coordinate convention: any future
calculation that uses a moving or non-canonical basis must first convert its
result back into the selected fixed gauge-factor basis.

# Canonical Scheme

Finite non-universal counterterms would act exactly like adjustable threshold
parameters unless selected by an independent source.  The no-knob discipline
therefore fixes the canonical matching convention:

```text
scheme_counterterm = (0,0,0).
```

Universal trace terms are irrelevant for the weak split anyway, since

```text
lambda_12 = p_1 - p_2.
```

Non-universal finite scheme terms are not allowed as primitive data unless a
future source selects them before comparison with electroweak observables.

# Remaining Physical Terms

The remaining terms are:

```text
local_determinant,
torsion_curvature,
bundle_index.
```

They are the only live contributors to the selected C1 electroweak response in
the reduced interface:

```text
p = p_det + p_torsion + p_bundle.
```

For full vector closure:

```text
P_EW(alpha_1) = trace_free(p) in the (chi_1,chi_2) basis.
```

For the weak-angle split alone:

```text
lambda_12
  = (p_det,U1 - p_det,SU2)
  + (p_torsion,U1 - p_torsion,SU2)
  + (p_bundle,U1 - p_bundle,SU2).
```

# Current Status

The reduced template still refuses to compute because the three physical source
vectors are not supplied by the current corpus.

This is progress because the remaining object is no longer a five-term
threshold ambiguity.  It is exactly:

```text
Selected local determinant response,
selected torsion-curvature threshold response,
selected bundle-index/local threshold response.
```

# Certified Status

```text
PEW_ALPHA1_PRIMITIVE_RESPONSE_REDUCED_TO_THREE_SOURCE_TERMS
```

