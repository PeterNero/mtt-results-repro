# Selected Qa/SU3 Color Connection Local System Torsion Interface

## Purpose

The previous gate reduced Qa/SU3 to selected operator data.  This note builds
the executable interface for those data.  It does not supply the selected data.

Open template:

```text
certificates/selected_qa_su3_color_connection_local_system_torsion.template.json
```

## Allowed Branches

The template accepts exactly three branch types:

```text
selected_su3_color_connection_spectrum
acyclic_local_system_torsion
global_section_measure
```

These correspond to the three legal routes isolated in the previous gate:

```text
selected SU3 color connection,
Ray-Singer/Reidemeister torsion of an acyclic local system,
global-section or fundamental-domain measure.
```

## Accounting

For a selected spectrum, the determinant response is:

```text
sum_j multiplicity_j * index_weight_j * log(eigenvalue_j / reference_scale_squared)
```

For analytic torsion, the response is:

```text
1/2 * sum_q (-1)^q * q * weight_q * zeta_derivative_at_zero_q
```

For a global-section measure, the response is:

```text
log(selected_global_section_or_fundamental_domain_measure / local_FP_slice_measure)
```

## Required Source Data

The template refuses to compute until it has:

```text
selected branch,
selected SU3 color bundle or local system,
selected connection/curvature/endomorphism or selected global measure,
BRST physical domain and zero-mode/ghost rules,
selected spectrum modes or analytic torsion finite parts.
```

This is the precise remaining data package.

## No-Knob Rules

The selected data must be supplied before Qa/SU3 target comparison.

The template may not be filled by using the known residual:

```text
-0.19453293407759187
```

The canonical Nil Weitzenbock term and the local FP/BRST quotient may not be
counted a second time.

## Verdict

The interface is built and intentionally open:

```text
interface built: yes
selected values available: no
numeric response computable now: no
```

Next artifact:

```text
Fill_Selected_Qa_SU3_Color_Connection_or_Torsion_Template_From_Source_Data
```
