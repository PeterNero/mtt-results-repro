# Selected Electroweak Kernel Interface Theorem v1

## Purpose

This theorem builds the selected electroweak threshold/gauge-normalization
kernel as far as the present corpus and standard string-threshold structure
allow.

The result is an executable interface:

```text
K_EW(selected branch) -> electroweak inverse-coupling data.
```

It does not yet close the numeric Standard Model constants. It does close the
form of the missing object and prevents the kernel from being rebuilt
ambiguously.

## Kernel Variables

Work in GUT-normalized hypercharge. Let:

```text
a = 1,2,3
g_1 = sqrt(5/3) g'
```

Define selected inverse-coupling entries at a matching scale `mu_Theta`:

```text
G_a(mu_Theta) := 1/g_a(mu_Theta)^2.
```

The selected electroweak/gauge kernel has the form:

```text
G_a(mu_Theta) = kappa_EW * zeta_a + Delta_a^sel.
```

where:

```text
zeta_a        = selected overlap/gauge kinetic weights,
kappa_EW      = common gauge kinetic normalization,
Delta_a^sel   = selected finite threshold/matching correction.
```

At one loop, the low-scale entries are:

```text
G_a(M_Z) = G_a(mu_Theta)
         + b_a/(8 pi^2) log(mu_Theta/M_Z)
         + delta_a^EW(M_Z,mu_Theta).
```

The `delta_a^EW` term may be absorbed into `Delta_a^sel` if the kernel is
defined directly between the selected high scale and `M_Z`. The split is a
scheme convention; the combined vector must be fixed before comparison to data.

## Source Support

The corpus supports the following pieces.

### Zeta ratios

The Theta papers support ratio data:

```text
g_1^2/g_2^2 = I_2/I_1,
g_3^2/g_2^2 = I_2/I_3.
```

Equivalently, in inverse-coupling form:

```text
G_1/G_2 = I_1/I_2,
G_3/G_2 = I_3/I_2.
```

This fixes zeta ratios but not the common normalization.

### Common normalization

The roadmap and Execution I use:

```text
alpha_a^{-1} = K zeta_a,
Vol(X_6)/g_10^2 = K/(4pi).
```

But the current `K` is calibrated from gauge data. Therefore the source supports
the slot `kappa_EW`, not its no-knob value.

### Threshold shape

Execution I supplies a threshold-profile shape, including a bulk direction:

```text
log(tau_a) - average(log tau),
```

and an exceptional correction vector. This gives a structural threshold slot.
It is not yet a no-knob electroweak threshold vector because its coefficients
are not derived from selected topology/flux data.

### Heterotic/string-threshold shape

The standard heterotic structure has:

```text
g_a^{-2} = Re(S) + finite one-loop threshold_a + ...
```

The MTT heterotic flux corpus has the same structural home:

```text
f=S,
g^{-2}=Re(S) up to threshold corrections.
```

But the source explicitly does not compute the alpha-prime and one-loop
thresholds. Thus the string side confirms the kernel form, not the missing
values.

### rho_UV

The closed internal value:

```text
rho_UV = 0.164530397543639
```

may enter `Delta_a^sel`, `kappa_EW`, or `mu_Theta` only through a source-
certified map. Directly setting any threshold equal to `rho_UV` is forbidden.

## Built Kernel Interface

The selected kernel interface is:

```text
K_EW[B] =
  {
    mu_Theta[B],
    zeta[B] = (zeta_1,zeta_2,zeta_3) up to common scale,
    kappa_EW[B],
    Delta^sel[B] = (Delta_1,Delta_2,Delta_3),
    scheme[B]
  }
```

and its prediction map is:

```text
G_a(M_Z;B)
  = kappa_EW[B] zeta_a[B]
  + Delta_a^sel[B]
  + b_a/(8pi^2) log(mu_Theta[B]/M_Z).
```

From `G_1,G_2`, the weak angle is:

```text
sin^2(theta_W)(M_Z)
  = (3/5)/G_1 / ((3/5)/G_1 + 1/G_2).
```

## Selection Conditions

For this to become a no-knob closure theorem, the following must all be true:

```text
1. mu_Theta[B] is selected before electroweak comparison.
2. kappa_EW[B] is selected internally or is one permitted universal primitive.
3. Delta^sel[B] is computed from selected threshold data.
4. zeta ratios are inherited from Theta/twistor/geometric overlap data.
5. the RG and threshold scheme is fixed before comparison.
6. no observed electroweak coupling, weak angle, G_F, m_W, or M_Z-derived
   target value is used to select kappa_EW or Delta^sel.
```

## Candidate Sources for the Missing Entries

The present corpus leaves three viable repair paths.

### Path A: Primitive common normalization

Accept one universal primitive:

```text
kappa_EW = kappa_0.
```

This is credible only if `kappa_0` is shared across gauge, gravity, axion,
and cosmology sectors and has predictive surplus. It would not be a pure
no-knob closure.

### Path B: Flux/Strominger threshold computation

Compute:

```text
Delta_a^sel = finite determinant/torsion/threshold functional
```

on the selected heterotic flux branch. This is the best strict no-knob route,
but it requires the selected spectrum or analytic torsion data.

### Path C: rho_UV response bridge

Prove a selected response map:

```text
Phi_EW(rho_UV, branch data) -> (kappa_EW, Delta^sel, mu_Theta).
```

This would be powerful, but it is not present yet.

## Verdict

The electroweak kernel is built as a formal executable interface:

```text
G_a(M_Z)=kappa_EW zeta_a + Delta_a^sel
        + b_a/(8pi^2) log(mu_Theta/M_Z).
```

The current corpus supports `zeta` ratios and the structural threshold home.
It does not yet select `kappa_EW`, `Delta^sel`, or `mu_Theta` without external
calibration.

Therefore the next true closure step is:

```text
compute selected (kappa_EW, Delta^sel, mu_Theta)
```

from one of Paths A--C, with no target-value backsolve.
