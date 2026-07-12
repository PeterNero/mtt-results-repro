# Selected K Gauge Anchor or Full Electroweak Matching v1

## Result

This solves the frontier in the only currently source-certified scope:

```text
internal_K_gauge_anchor_closed = true
K_gauge,int = 1
selected_internal_kernel_vector_closed = true
physical_K_gauge_anchor_closed = false
measured_electroweak_closure = false
target_fitting_used = false
```

The physical electroweak constants are not yet predicted.  What is now proved
is that there is no additional internal normalization knob left at this layer:
the common gauge normalization is `1` in canonical selected internal action
units, and the remaining physical normalization is the same M-theory/modal-gap
anchor already isolated by the GR/protospinor branch.

## Theorem

```text
SelectedInternalKGaugeAnchorAndPhysicalMatchingReduction
```

In canonical selected internal action units, the common gauge-action normalization is fixed as K_gauge,int=1. This is not a measured electroweak normalization: the physical K_gauge is the compactification/action anchor controlled by the same M-theory modal-gap slot as the GR normalization. Therefore the internal kernel is closed, while full measured electroweak matching is reduced to the single physical anchor plus selected threshold/RG data.

Internal unit anchor:

```text
K_gauge,int = 1
```

Why this is allowed:

```text
The non-SM constants repo already certifies canonical internal action units alpha_int=1 and G10_int=1; in those units K_gauge is a unit conversion for the selected internal response functional, not a fitted physical coupling.
```

Why this is not physical electroweak closure:

```text
The protospinor/GR M-theory anchor certificate identifies the gauge kinetic normalization slot but leaves ell_p/kappa_11/alpha_prime or the physical modal-gap unit open.
```

## Selected Internal Kernel

Formula:

```text
G_a^int = K_gauge,int * I_a with K_gauge,int=1, before physical thresholds/running
```

Exact entries:

```text
U1: 2/3
SU2: 1
Qa_or_SU3: log(2008)
```

Numeric entries:

```text
U1: 0.666666666667
SU2: 1
Qa_or_SU3: 7.60489448081
```

Scope:

```text
dimensionless selected internal action units; not M_Z couplings and not a physical high-scale fit
```

## Physical Kernel Still Required

Formula:

```text
G_a^phys(mu) = K_phys * I_a + Delta_a^sel + b_a/(8*pi^2)*log(mu_match/mu) in a fixed scheme
```

Source slot:

```text
M-theory compactification/action slot, e.g. kappa_11^{-2} times the selected harmonic Gram matrix with conventions fixed
```

Still missing:

- target-independent physical modal-gap / ell_p / kappa_11 / alpha_prime anchor
- selected matching scale mu_match
- selected threshold vector Delta_a^sel
- fixed RG and threshold scheme
- sector-resolved SU3 identification if Qa is used as the SU3 payload

## Cross-Repo Checks

```text
qa_finite_response_closed = True
qa_delta_is_log2008 = True
u1_su2_index_pair_closed = True
nonsm_kernel_interface_built = True
nonsm_numeric_electroweak_open = True
rho_uv_bridge_open = True
mtheory_gauge_slot_identified = True
mtheory_physical_anchor_open = True
sm_gauge_couplings_downstream = True
```

## Guardrails

- K_gauge,int=1 is an internal action-unit statement, not a measured coupling prediction.
- Do not compare the internal vector (2/3,1,log(2008)) directly to measured inverse couplings.
- Do not use observed alpha_EM, sin^2(theta_W), g2, g3, masses, or M_Z-derived fits to select K_phys or Delta^sel.
- The physical gauge anchor must be shared with the GR/M-theory compactification normalization if claimed as no-knob.
- Thresholds and RG scheme must be fixed before any electroweak data comparison.

## Next Required Object

```text
Selected_Physical_Gauge_Anchor_and_Electroweak_Threshold_Vector_v1
```
