# Electroweak No-Knob Closure Source Exhaustion Theorem v1

## Purpose

This theorem closes the present electroweak gate as far as the current corpus
allows. It proves that the current corpus does not yet contain enough selected
data to compute low-energy electroweak observables without importing an
external gauge normalization, electroweak input, or target-fitted threshold.

This is a negative closure theorem, not a failure of the program. It prevents a
false proof and identifies the smallest repair object.

## Theorem

The present corpus does not prove a full no-knob electroweak closure.

More precisely, after the selected internal `rho_UV` branch is closed and the
Theta overlap ratio is fixed, the current corpus still lacks at least one of:

```text
1. internally selected g_2(mu_Theta)^2,
2. internally selected matching scale mu_Theta,
3. internally selected electroweak threshold vector (T_1,T_2),
4. a source-certified map from rho_UV to electroweak inverse-coupling
   threshold entries.
```

Therefore `sin^2(theta_W)(M_Z)`, `alpha_EM(M_Z)`, and the electroweak gauge
couplings are not yet no-knob predictions of the current corpus.

## Source Exhaustion

### Theta I

Theta I defines the overlap framework and extracts the numerical overlap
targets from experimentally measured gauge couplings. It is explicit that no
prediction of the Standard Model gauge couplings is made there. This gives a
consistent target and existence problem, not a no-knob electroweak prediction.

### Theta II

Theta II computes leading-order nonabelian overlap integrals and matches them
to the Theta targets. This is valuable rigidity after the target ratios are
given. But the paper is still matching the target ratios extracted from gauge
data; it does not internally select the absolute gauge normalization.

### Theta III

Theta III gives an independent twistor-action normalization of the nonabelian
overlaps. This is the strongest normalization support in the Theta sequence.
It fixes the overlap normalization convention and cross-checks Route A.

However, it does not compute the absolute four-dimensional gauge coupling
normalization `g_2(mu_Theta)^2` from selected MTT data. Its own scope excludes
Yukawa/flavor and does not supply electroweak threshold matching.

### Theta V

Theta V gives the useful weak-angle route:

```text
g_1(mu_Theta)^2/g_2(mu_Theta)^2 = I_2/I_1.
```

It obtains a tree-level weak-angle value near the observed one when `g_2` is
fixed from electroweak inputs and thresholds are treated externally. It also
states the non-circular requirement: compute `g_1(mu_Theta)` and
`g_2(mu_Theta)` internally.

### Execution I

Execution I introduces a common scale `K` and a volume/gauge combination:

```text
Vol(X_6)/g_10^2 = K/(4pi).
```

But `K` is a Tier-3 calibrated scale from gauge data, and choosing `g_10=1` is
a normalization convention at that stage. This is not a no-knob prediction of
absolute electroweak normalization.

### Heterotic Flux Corpus

The heterotic flux corpus gives the correct structural home:

```text
f = S,
g^{-2}=Re(S) up to threshold corrections.
```

It explicitly does not compute the relevant alpha-prime and one-loop threshold
corrections. Thus it supplies the bridge location, not the bridge value.

## Underdetermination Lemma

Let:

```text
r = g_1(mu_Theta)^2/g_2(mu_Theta)^2.
x = g_2(mu_Theta)^2.
```

At one loop:

```text
1/g_1(M_Z)^2 = 1/(r x) + A_1 + T_1,
1/g_2(M_Z)^2 = 1/x     + A_2 + T_2.
```

The weak angle is:

```text
sin^2(theta_W)(M_Z)
  = (3/5)g_1(M_Z)^2 / ((3/5)g_1(M_Z)^2+g_2(M_Z)^2).
```

For fixed `r`, the low-energy weak angle changes when `x`, `T_1`, or `T_2`
changes. Hence the ratio alone does not select a unique low-energy weak angle.

This proves that the current corpus cannot close electroweak observables from
Theta overlap ratios alone.

## Forbidden Shortcut

It is not valid to set:

```text
rho_UV = Delta r_eff,
rho_UV = T_a,
K = observed gauge normalization,
g_10 = 1 as a physical prediction,
mu_Theta = 5 TeV because it gives a good weak angle.
```

Any such move would be a calibration or notation collision unless a source
theorem derives the map before comparison to electroweak data.

## Smallest Repair

The smallest object that could close the gate is:

```text
Selected_Electroweak_Threshold_Kernel_Theorem_v1
```

It must prove:

```text
K_EW(selected MTT branch) -> (mu_Theta, x, T_1, T_2, scheme),
```

where:

```text
x = g_2(mu_Theta)^2.
```

The theorem may use one universal primitive normalization only if it passes the
primitive-constant discipline:

```text
universal,
prior,
audited,
non-redundant,
not a target backsolve,
prediction-rich across sectors.
```

## Verdict

The current electroweak branch is closed negatively:

```text
Full no-knob electroweak closure is not proved by the present corpus.
```

The positive achievement is sharp:

```text
rho_UV is internally closed,
Theta overlap ratios are structurally supported,
topology-only SM constraints are rigorous,
and the remaining electroweak proof obligation is exactly K_EW.
```

The next work is not to search for another weak-angle formula. It is to build
the finite selected electroweak threshold/gauge-normalization kernel.
