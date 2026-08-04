# Shared Knob Cross-Encoding Ledger for MTT/MMT

## Purpose

If MTT/MMT is treated as a superset over several theory encodings, then the
most useful objects are not arbitrary adjustable parameters. They are selected
data that several encodings read in different ways.

This ledger records those shared data and separates three layers:

```text
selected shared data,
encoding dictionary,
encoding-specific open observables.
```

This prevents a common overclaim: a shared selected invariant can constrain
many theories, but it does not automatically compute every observable in each
theory.

## Main Rule

The allowed cross-encoding workflow is:

```text
selected MTT/MMT data
-> encoding dictionary
-> theory-specific observable,
```

with every remaining encoding-specific datum listed before a prediction is
claimed.

The forbidden workflow is:

```text
selected MTT/MMT data
-> assume the missing theory-specific matrices or thresholds
-> claim full closure.
```

## Shared Knob Ledger

| Shared knob | Status | Selected data | SM/flavor reading | String/flux reading | QG/spectral/topology reading |
|---|---|---|---|---|---|
| `q79_cp_character` | closed | `q=79 mod 448`, from `q64=15`, `q7=2` | CKM CP label and channel-character filter | combined dyadic/Mukai character | finite unitary character of selected quotient |
| `z64_exact_central_circle_carrier` | closed exact | `K64=C[Z64]`, lag `S^-1`, gap `9` | dyadic CP component | shared-circle/deck carrier | exact coherent block, zero Schur leakage |
| `z7_mukai_fuyau_charge_block` | closed charge sector | Mukai Gram `[[2,1],[1,4]]`, determinant `7` | sevenfold CP component | Fu-Yau/Strominger charge sector | discriminant group `A_P ~= Z7` |
| `theta_overlap_scaffold` | scaffold closed, kernel data open | `mu_Theta=5 TeV`, `I2/I1=0.560`, `I3/I1=0.229`, `lambda_*=0.25` | pre-flavor Yukawa/CKM scaffold | geometry and overlap normalization | spectral gap/admissibility floor |
| `iwasawa_rank_one_yukawa_seed` | tree seed closed, corrections open | `lambda_123=1`, rank `1`, representative `E33` | heavy-family seed | heterotic `E6 27^3` trilinear | harmonic-representative overlap |
| `single_higgs_projection` | formulated, open data remain | `H_u -> H`, `H_d -> H^dagger` | one low-energy SM Higgs doublet | post-E6 low-energy projection | NCG finite connection/Yukawa carrier |
| `channel_weight_formula` | formulated, values open | `W=A exp(-S) chi` on finite channel sets | raw/canonical Yukawa rule | instanton/alpha-prime/flux action slots | holonomy character and overlap amplitude rule |
| `c1_alpha1_curvature_driver` | support closed, values open | `Tr_grav R_+^2=v1_tilde alpha_1` | C1 rank-lift candidate | Green-Schwarz `R_+` curvature row | selected Hessian/coherent response row |
| `finite_c1_response_assembly` | finite assembly reduced, values open | six primitive `3x3` blocks per sector | C1 response matrices | alpha-prime overlap response | executable primitive-contraction interface |

## What The Ledger Achieves

The ledger makes the current program portable. Instead of asking separately in
each domain "what is the parameter?", we can ask:

```text
which selected shared datum is this encoding reading?
```

For example:

```text
q=79 mod 448
```

has several readings:

```text
SM flavor:       CKM CP character candidate,
topology:        unitary character of Z448,
string/flux:     dyadic x Mukai/Fu-Yau charge character,
QG/spectral:     finite coherent quotient retained by the exact block.
```

Likewise:

```text
Tr_grav R_+^2 = v1_tilde alpha_1
```

has several readings:

```text
string/flux:     selected Green-Schwarz curvature support,
SM flavor:       C1 rank-lift source candidate,
QFT overlap:     linear-response insertion into Yukawa overlaps,
QG/spectral:     perturbation passed through Hess_Xi and Pi_coh.
```

## Current Strongest Cross-Encoding Achievements

The strongest closed cross-encoding data are:

```text
Z64 exact central-circle carrier,
Z7 Mukai/Fu-Yau charge block,
q=79 mod 448,
Theta scaffold fixed ratios and gap floor,
Iwasawa rank-one tree Yukawa seed.
```

These are not merely analogies. They are machine-audited objects in the repo.

The strongest formulated but value-open cross-encoding data are:

```text
finite channel weight rule W=A exp(-S) chi,
C1 alpha_1 curvature driver,
finite C1 matrix assembly.
```

These are real structural reductions, but they still require selected
primitive data before numerical mass or mixing claims.

## How To Use This For Other Encodings

For any proposed encoding, make a small table:

```text
observable in target theory,
candidate shared knob,
source certificate,
encoding map,
remaining open target-specific data,
forbidden proxy inputs.
```

Then classify the target result as:

```text
CLOSED:       shared knob and target-specific data are both closed,
FORMULATED:  encoding map exists but values are open,
PARTIAL:     support/source is closed but contractions or metrics are open,
OPEN:        no source certificate yet.
```

## Important Consequence

This changes the research posture. We should not build one-off explanations
inside each theory. We should build shared selected data first, then ask how
each theory reads it.

That is precisely what the current q79/C1/Yukawa work has achieved: it turns a
large phenomenological target into a set of reusable selected invariants,
operator rows, and finite calculation interfaces.
