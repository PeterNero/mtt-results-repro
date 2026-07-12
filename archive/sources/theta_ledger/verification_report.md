# Verification Report: Theta-Closure & Execution Program

Date checked: 2026-05-17

This is a technical audit of the claims in the Markdown-converted papers in `_md`.
I checked arithmetic, internal logical dependence, and a small set of external factual
comparisons against current PDG/CMB references.

## High-confidence checks that pass

### Gauge coupling extraction and one-loop running

Source: `_md/Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md`

Using the paper's inputs

- `alpha(M_Z)^-1 = 127.95`
- `sin^2 theta_W(M_Z) = 0.23122`
- `alpha_s(M_Z) = 0.1179`
- `M_Z = 91.1876 GeV`
- `mu_Theta = 5000 GeV`
- one-loop beta coefficients `(41/10, -19/6, -7)`

I recomputed:

```text
L = ln(5000 / 91.1876) = 4.0042742685
g1(MZ) = 0.4614324401
g2(MZ) = 0.6517365667
g3(MZ) = 1.2171996941

g1(5 TeV) = 0.4719990075
g2(5 TeV) = 0.6305836836
g3(5 TeV) = 0.9853482045

I2/I1 = (g1/g2)^2 = 0.5602691537
I3/I1 = (g1/g3)^2 = 0.2294577400
```

This verifies the quoted `0.560` and `0.229` overlap-ratio targets. One correction:
the paper prints `L approx 3.999`; the correct value is about `4.00427`. The difference
does not materially affect the rounded couplings.

### Direct geometric overlap arithmetic

Source: `_md/Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md`

Given the definitions used in the paper:

- `I1 = 2 pi R1`
- `I2 = 4 pi (f2 R_lens)^2`
- `I3 = c`

the matching arithmetic checks:

```text
I2/I1 = 0.560  =>  (f2 R_lens)^2 = 0.280 R1
I3/I1 = 0.229  =>  c = 0.229 * 2 pi R1 = 1.43885 R1
```

The spectral-margin arithmetic also checks:

```text
lambda_lens >= 2 / (0.280 R1)
for R1 <= 2, lambda_lens >= 3.57

for c <= 2.878,
2 pi + 4 pi^2 / c^2 >= 11.05
```

### Gravity/cosmology arithmetic

Source: `_md/Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md`

The volume coefficient checks:

```text
(2 pi)(4 pi)(0.280)(1.439) = 31.8133
```

The tensor-ratio bound arithmetic also checks under the paper's assumption
`Lambda_Theta = 5 TeV`:

```text
(5e3 / 2.4e18)^2 = 4.34e-30
(3e3 / 2.4e18)^2 = 1.56e-30
(1e4 / 2.4e18)^2 = 1.74e-29
```

## Claims that are conditional rather than established

### "Prediction" of sin^2 theta_W

Source: `_md/Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md`

The Section 3 value

```text
sin^2 theta_W(MZ) = 0.2312108882
```

is reproduced from the rounded boundary values `g1(5 TeV)=0.4720`,
`g2(5 TeV)=0.6306`.

But the paper itself correctly notes that this is a round-trip check, not an independent
prediction, because those boundary values came from upward running from the same electroweak
inputs. The phrase "agreement within experimental uncertainty" is numerically true but
should not be presented as an independent overconstraint unless the non-circular route is
the headline.

For the non-circular route using `(G_F, m_W)` plus a threshold parameter, I recomputed:

```text
Delta r_eff = 0      => sin^2 theta_W = 0.231198
Delta r_eff = 0.02   => sin^2 theta_W = 0.231573
Delta r_eff = 0.036  => sin^2 theta_W = 0.231873
Delta r_eff = 0.05   => sin^2 theta_W = 0.232137
```

This does not support the paper's statement that scanning `Delta r_eff in [0.02, 0.05]`
keeps `sin^2 theta_W = 0.2312 +/- O(1e-4)`. The scan shifts the result by roughly
`4e-4` to `9e-4` relative to `0.2312`.

### Cosmology bound

The `r < 10^-30--10^-29` result follows from the assumed coherence cutoff
`H << Lambda_Theta ~ 3--10 TeV`. It is not an observationally derived prediction.
It is best stated as:

> If the MTT admissibility cutoff for tensor production is truly at the few-TeV
> scale, then observable primordial tensors are excluded.

That is a conditional falsifier, not a model-independent cosmological result.

Current CMB constraints are around `r < 0.036--0.038` at 95% CL in recent
Planck/BICEP/Keck combinations, so the paper's broad statement
`r lesssim 10^-1--10^-2` is too loose but directionally correct. The projected
future sensitivity statement `10^-4--10^-3` is plausible as an order-of-magnitude
claim.

## Claims that do not verify

### Printed quark Yukawa matrices do not produce the printed CKM matrix

Source: `_md/Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md`

Using the real matrices printed in the paper and diagonalizing `Y_u Y_u^T` and
`Y_d Y_d^T`, I get:

```text
up singular values:
1.2751e-05, 1.6849e-03, 5.3002e-01

down singular values:
2.2216e-04, 5.5781e-03, 1.1024e-01

|V_CKM| =
[[0.99897, 0.04538, 0.00147],
 [0.04540, 0.99810, 0.04169],
 [0.00043, 0.04171, 0.99913]]
```

The paper claims:

```text
[[0.9743, 0.2250, 0.0036],
 [0.2249, 0.9735, 0.0411],
 [0.0087, 0.0403, 0.9991]]
```

The printed matrices therefore do not verify the claimed Cabibbo angle or CKM
structure. The mass singular values are close to the printed mass hierarchy, but
the mixing matrix is not.

### Printed lepton/neutrino matrices do not produce the printed PMNS matrix or masses

Using the printed `Y_e`, `Y_nu`, and diagonal `M_R`, I get:

```text
|U_PMNS| =
[[0.99825, 0.05914, 0.00073],
 [0.05905, 0.99722, 0.04550],
 [0.00342, 0.04537, 0.99896]]

angles:
theta12 = 3.39 deg
theta23 = 2.61 deg
theta13 = 0.04 deg
```

The paper claims:

```text
|U_PMNS| =
[[0.821, 0.547, 0.149],
 [0.430, 0.599, 0.677],
 [0.374, 0.585, 0.717]]

theta12 = 33.4 deg
theta23 = 46.8 deg
theta13 = 8.6 deg
```

The printed neutrino setup also gives an extremely hierarchical light-neutrino
spectrum. Normalizing `m3` to `0.050 eV` gives approximately:

```text
m1 = 3.4e-09 eV
m2 = 6.8e-07 eV
m3 = 0.050 eV
```

not the claimed `(0.0025, 0.0087, 0.050) eV`.

### Higgs quartic boundary appears inconsistent with the usual MSSM tree-level formula

The paper uses

```text
lambda = (g^2 + g'^2) / 4 * cos^2(2 beta)
```

The standard SM-normalized MSSM tree-level matching is usually

```text
lambda = (g^2 + g'^2) / 8 * cos^2(2 beta)
```

depending on Higgs potential convention. With the common convention
`V = -m^2 |H|^2 + lambda |H|^4`, the paper's boundary value is high by a factor
of two. This directly affects the claimed running to `m_h ~= 125 GeV`.

## Structural issues to fix before publication

1. Clarify dimensions in `(f2 R_lens)^2 = 0.280 R1`. If `R1` carries length
   dimension, the equation is dimensionally inconsistent. If all internal radii
   are dimensionless in chosen units, state that explicitly.

2. Clarify the "lens" sector. The papers reference `L(3,1)` but then model the
   layer as a round `S^2`. `L(3,1)` is a three-dimensional lens space, not a
   two-sphere. If `S^2` is an effective base or quotient, the reduction should be
   stated.

3. Tone down independent-prediction language around `sin^2 theta_W` unless the
   non-circular calculation is repaired and made the primary calculation.

4. Replace the Execution II CKM/PMNS benchmark matrices or recompute the printed
   matrices from the stated local parameters. As printed, the core flavor claims fail.

5. Recheck the Higgs quartic convention and include the exact convention for
   the Higgs potential. If using the nonstandard factor, explain it.

## External reference checks

- PDG 2025 electroweak review gives `alpha_s(M_Z) = 0.1177 +/- 0.0009`, with
  SM-fit value `0.1179 +/- 0.0009`; the paper's `0.1179` is fine for a 2024/2025
  representative value.
- PDG summary values list `sin^2 theta_W(M_Z)_MS = 0.23129(4)`, while the papers
  use `0.23122`. This is close but should be cited with scheme and source.
- Recent Planck/BICEP/Keck combinations quote roughly `r < 0.036--0.038` at 95% CL,
  tighter than the paper's broad `10^-1--10^-2` statement.

