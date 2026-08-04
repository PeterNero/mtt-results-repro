# Selected Physical Gauge Anchor and Electroweak Threshold Vector v1

## Result

The physical electroweak match is not closed yet.  It is reduced to the exact
remaining source objects.

```text
physical_electroweak_matching_closed = false
physical_anchor_closed = false
threshold_vector_closed = false
convention_reconciliation_closed = false
target_fitting_used = false
```

## Theorem

```text
SelectedPhysicalGaugeAnchorAndElectroweakThresholdVectorGate
```

Given the selected internal kernel I=(2/3,1,log(2008)) and K_gauge,int=1, full no-knob electroweak matching is equivalent to supplying two same-branch physical objects: a compactification/action anchor K_phys (or physical modal-gap unit) and an index-weighted local determinant threshold vector Delta_a^sel, with RG scheme and matching scale fixed before comparison. The present repositories identify the slots but do not emit their values.

## Selected Internal Inputs

```text
I_U1 = 2/3
I_SU2 = 1
I_Qa_or_SU3 = log(2008)
K_gauge,int = 1
```

## Diagnostic Only

If one ignores physical thresholds, running, and convention reconciliation, the
internal inverse weights imply:

```text
g1^2/g2^2 = 3/2
sin^2(theta_W)_tree,GUT = 9/19
sin^2(theta_W)_tree,GUT numeric = 0.47368421052631576
status = DIAGNOSTIC_ONLY_NOT_PHYSICAL_PREDICTION
```

This is deliberately not a physical weak-angle prediction:

```text
It assumes no physical threshold vector, no running, and no convention reconciliation with the older Theta representative ratio.
```

## Physical Anchor Gate

```text
status = OPEN
required_source = selected Omega_0 or ell_p/kappa_11/alpha_prime/action unit from the same branch
mtheory_slot = f_ab = (1/(2 kappa_11^2)) int_X7 omega_a wedge *_7 omega_b
current_reduction = REDUCED_NOT_CLOSED
```

## Threshold Vector Gate

```text
status = OPEN
required_source = selected index-weighted local determinant / analytic torsion response
weak_split_minimal_scalar = lambda_12 = p_U1 - p_SU2
known_selected_prefactor_v1_tilde = 0.405623467693425
formula_if_lambda12_selected = Delta_G,12 = v1_tilde * lambda_12 / (4*pi)
diagnostic_target_witness_lambda12 = 2.194153126940556
diagnostic_target_witness_delta_g12 = 0.07082394967589342
target_witness_status = FORBIDDEN_AS_PROOF_INPUT
```

## Convention Reconciliation Gate

```text
status = OPEN
issue = The selected internal inverse weights imply a tree-level internal ratio, while older Theta electroweak notes quote a representative overlap ratio in their own convention. A proof must name the hypercharge normalization, embedding map, and matching convention before comparing either ratio to data.
required_output = one typed map from selected U1/SU2/Qa carriers to GUT-normalized electroweak variables
```

## Cross-Repo Checks

```text
internal_kernel_closed = True
internal_K_equals_one = True
kernel_interface_built = True
kernel_numeric_selection_open = True
threshold_reduction_requires_kernel = True
c1_reduced_to_local_determinant = True
local_determinant_template_open = True
fill_attempt_blocks_selected_threshold = True
omega_gap_physical_unit_open = True
mtheory_gauge_slot_identified = True
mtheory_physical_anchor_open = True
```

## Remaining Objects

- K_phys or Omega_0/ell_p/kappa_11/alpha_prime physical anchor
- lambda_12 or full Delta_a^sel selected local determinant vector
- mu_match and fixed RG/threshold scheme
- typed electroweak convention map

## Guardrails

- Do not treat the zero-threshold tree diagnostic 9/19 as a physical weak-angle prediction.
- Do not use the diagnostic lambda_12 target witness as selected determinant data.
- Do not mix internal inverse weights with older Theta ratios until the electroweak convention map is explicit.
- Do not select K_phys from observed alpha_EM, sin^2(theta_W), g2, g3, M_Z, or masses.
- Full no-knob closure requires the physical anchor and threshold vector from the same branch.

## Next Required Object

```text
Selected_Local_Determinant_Threshold_Vector_or_Physical_Omega0_Source_v1
```
