# Electroweak No-Knob Bridge Audit v1

## Purpose

The internal `rho_UV` branch is now closed as a dimensionless selected
Iwasawa/Flux/Strominger response:

```text
R_*     = 4.440528182269818
rho_UV  = 0.164530397543639
```

This audit asks the next question:

```text
Can the closed rho_UV number be used, without knobs, to close electroweak
data such as gauge coupling normalization, threshold matching, or
sin^2(theta_W)?
```

The answer at this stage is no. The bridge is now well formulated, but the
corpus does not yet contain the selected electroweak kernel that maps
`rho_UV` to a gauge threshold or weak-angle boundary condition.

## Source-Certified Inputs

### Closed internal branch

The final selected-radius theorem proves:

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2,
F_H2(R)   = rho_UV(R) + R^2/30,
R_*       = argmin F_H2,
rho_UV    = 0.164530397543639.
```

This is an internal dimensionless result. It is not yet an electroweak
observable.

### Theta weak-angle route

The Theta V paper contains a valuable electroweak program:

```text
g_1(mu_Theta)^2 / g_2(mu_Theta)^2 = I_2(Theta) / I_1(Theta),
g_3(mu_Theta)^2 / g_2(mu_Theta)^2 = I_2(Theta) / I_3(Theta).
```

It also records a numerical tree-level weak-angle result near:

```text
sin^2(theta_W)(M_Z) ~= 0.23120.
```

But the same paper states that strict non-circular closure requires computing
`g_1(mu_Theta)` and `g_2(mu_Theta)` internally. Its numerical path fixes
`g_2` from electroweak inputs such as `(G_F,m_W)` and includes an effective
threshold parameter `Delta r_eff`. Therefore the current Theta route is a
conditional redundancy test, not a fully no-knob electroweak closure.

### Topology-only Standard Model constraints

The topology-only corpus gives genuine rigorous SM structure:

```text
exact SM hypercharges,
absence of the SU(2) Witten anomaly for three families,
local gauge/gravitational anomaly cancellation,
qualitative one-loop beta-function signs.
```

These are strong boundary constraints on any electroweak closure. They do not
fix absolute gauge coupling normalization or low-energy threshold corrections.

### Heterotic flux/gauge kinetic route

The heterotic flux corpus gives a natural location for an electroweak bridge:

```text
f = S,
g^{-2} = Re S up to threshold corrections.
```

It also gives Bianchi identities involving `alpha'`, curvature, and flux rows.
However, it explicitly does not compute the relevant higher-alpha-prime and
one-loop threshold corrections. Therefore it supplies the right structural
place for the bridge, not the bridge value itself.

## Gate Classification

| Gate | Status | Reason |
|---|---|---|
| Internal `rho_UV` value | `CLOSED_INTERNAL` | Selected by the H2 horizontal scale law, with no target data. |
| `rho_UV -> electroweak threshold` | `OPEN_NO_SOURCE_BRIDGE` | No source-certified kernel maps `rho_UV` to `Delta r_eff`, gauge thresholds, or `sin^2(theta_W)`. |
| High-scale `sin^2(theta_W)=3/8` | `STRUCTURAL_IDENTITY` | Useful modal-symmetry boundary identity, not a low-energy prediction without RG and thresholds. |
| Theta overlap ratios | `STRUCTURAL_RATIO` | Ratios such as `I_2/I_1` are meaningful, but absolute normalization remains external or primitive. |
| Theta V weak-angle number | `CONDITIONAL_NOT_NO_KNOB_CLOSED` | Uses electroweak inputs and threshold assumptions; does not use `sin^2(theta_W)` directly, but is not fully internal. |
| Gauge absolute normalization | `PRIMITIVE_OR_OPEN` | A universal prior normalization may be acceptable only under primitive-constant discipline. |
| Import old threshold coefficient | `FORBIDDEN_SYMBOL_COLLISION` | Threshold-profile coefficients cannot be reused as electroweak matching corrections without a source-certified map. |

## No-Knob Rule

The following are forbidden as electroweak proof moves:

```text
choose Delta r_eff to match sin^2(theta_W),
choose a gauge normalization from the same coupling being predicted,
identify rho_UV with an electroweak threshold by name similarity,
reuse Execution-I threshold coefficients as electroweak matching data,
fit a matching scale after looking at the target weak angle.
```

The following would be acceptable:

```text
derive a selected electroweak threshold kernel K_EW from the same branch,
derive gauge kinetic normalization from finite topology/flux/action data,
derive the matching scale from Theta or Flux/Strominger closure before
  evaluating electroweak observables,
use one universal primitive normalization only if it is prior, shared across
  sectors, audited, non-redundant, and prediction-rich.
```

## Correct Way Forward

The electroweak closure problem should be reduced to one explicit theorem:

```text
Selected Electroweak Threshold Kernel Theorem
```

It must provide, from selected MTT data alone:

```text
1. the matching scale mu_Theta or an internally selected scale relation,
2. the gauge kinetic normalization or a permitted universal primitive,
3. the ratio matrix I_a(Theta) with normalization conventions fixed,
4. the threshold/matching kernel replacing Delta r_eff,
5. a downward RG map with scheme stated before comparison to data.
```

Only after these are fixed may the program compute:

```text
g_1(M_Z), g_2(M_Z), g_3(M_Z),
sin^2(theta_W)(M_Z),
and eventually alpha_EM and electroweak-scale boundary data.
```

## Verdict

The rho_UV branch complements the electroweak program, but it does not yet
change the status of the Theta weak-angle calculation into a full no-knob
prediction. What has been achieved is a closed internal UV-response constant
and a much sharper electroweak target:

```text
find the selected kernel that sends internal UV response data into
gauge kinetic normalization and electroweak threshold matching.
```

Until that kernel is supplied, full electroweak closure remains open.
