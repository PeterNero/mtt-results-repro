---
abstract: |
  We record the strongest no-proxy flavor statement presently justified by
  the Theta-closure corpus.  The selected q79 branch fixes a finite CP
  character, while the Theta papers fix the matching scale, gauge-overlap
  ratios, direct lens and nil normalizations, and spectral-gap margins before
  any fermion mass or mixing fit is made.  Combining these facts gives a
  selected overlap-kernel scaffold for flavor: any admissible no-proxy Yukawa
  calculation must use mu_Theta=5 TeV, I2/I1=0.560, I3/I1=0.229, the direct
  lens normalization (f2 R_lens)^2=0.280 R1, the nil normalization
  c=1.439 R1, the gap floor lambda_*=0.25, and the CP character q=79 mod 448.
  This closes the empty-scaffold problem but not the Yukawa magnitude problem.
  The remaining open data are the family zero modes, finite overlap-channel
  lists, channel actions, prefactors, kinetic metrics, and RG/threshold
  matching.
author:
- Peter Nero
date: May 2026
title: |
  Theta-Selected Overlap Kernel Skeleton for No-Proxy Flavor
---

# Purpose

The q79 proof has moved the flavor program past a purely fitted CP benchmark:

```text
selected exact/charge branch -> q = 79 mod 448.
```

The CKM phase bridge then gives a post-hoc compatibility check:

```text
delta_MTT = 2 pi * 79/448,
J_MTT = P sin(delta_MTT).
```

The next frontier is Yukawa magnitude closure.  The point of this note is to
separate what is already selected from what remains open.

We do not yet have the full Yukawa matrices as no-proxy predictions.  We do
have a nonempty, audited scaffold that any no-proxy Yukawa kernel must obey.

# Selected Theta Data

The Theta gauge-sector papers fix the following data before any use of
fermion masses or CKM angle magnitudes:

```text
mu_Theta = 5 TeV,
I2/I1 = 0.560,
I3/I1 = 0.229,
lambda_* = 0.25.
```

The shared circle gives:

```text
I1 = 2 pi R1,
0 < R1 <= 2.
```

In the direct geometric realization, the lens overlap is:

```text
I2^(0) = 4 pi (f2 R_lens)^2.
```

Matching `I2/I1=0.560` therefore gives:

```text
(f2 R_lens)^2 = 0.280 R1.
```

The associated lens gap is:

```text
lambda_lens >= 2/(0.280 R1).
```

Since `R1 <= 2`, the endpoint lower bound is:

```text
lambda_lens >= 3.571... > 0.25.
```

For the nil sector, the direct realization uses:

```text
g_nil = a^2 sigma1^2 + b^2 sigma2^2 + c^2 sigma3^2,
sigma1 = dx,
sigma2 = dy,
sigma3 = dz - x dy,
a = b = 1.
```

The leading nil overlap is:

```text
I3^(0) = c.
```

Matching `I3/I1=0.229` gives:

```text
c = 1.439 R1.
```

For `R1 <= 2`, this implies `c <= 2.878`, and the nil spectral lower bound in
the Theta II paper gives:

```text
lambda_1 >= 2 pi + 4 pi^2 / c^2 >= 11.05... > 0.25.
```

# Selected CP Character

The terminal q79 certificate fixes the CP character independently:

```text
Gamma_CP ~= Z64 x Z7 ~= Z448,
q64 = 15,
q7 = 2,
q = 79 mod 448.
```

Thus a no-proxy flavor kernel cannot choose its CP phase after the fact.  Its
finite character must restrict to the selected q79 branch or explain why a
different selected quotient replaces it.

# Kernel Form

The current no-proxy flavor criterion requires a selected overlap kernel of the
form:

```text
Y_abc(Theta) =
  sum_{gamma in Gamma_abc(Theta)}
    A_gamma(Theta) exp(-S_gamma(Theta)) chi_gamma(Theta).
```

The Theta/q79 scaffold fixes the outer environment in which this formula must
be evaluated:

```text
scale:          mu_Theta = 5 TeV,
circle:         I1 = 2 pi R1, 0 < R1 <= 2,
lens:           I2 = 4 pi (f2 R_lens)^2, (f2 R_lens)^2 = 0.280 R1,
nil:            I3 = c, c = 1.439 R1, a=b=1,
gap floor:      lambda_* = 0.25,
gap margins:    lambda_lens >= 3.571..., lambda_nil >= 11.05... at R1=2,
CP character:   q = 79 mod 448.
```

This is already a real restriction: the future Yukawa calculation may not
introduce an arbitrary scale, arbitrary internal normalization, arbitrary CP
phase, or arbitrary gap regime.

# The Scaffold Theorem

#### Theorem

Assume the selected exact/charge q79 branch and the direct Theta-closure
geometry of Papers I-II.  Then the no-proxy flavor program has a closed
Theta-selected overlap-kernel scaffold with:

```text
mu_Theta = 5 TeV,
I2/I1 = 0.560,
I3/I1 = 0.229,
0 < R1 <= 2,
(f2 R_lens)^2 = 0.280 R1,
c = 1.439 R1,
lambda_* = 0.25,
q = 79 mod 448.
```

For every `R1 in (0,2]`, the direct lens and nil gap bounds remain strictly
above the admissibility floor.  Therefore the selected q79 CP character is
compatible with a nonempty Theta-admissible flavor-kernel environment.

#### Proof

The q79 terminal certificate supplies `q=79 mod 448` from the exact/charge
branch.  Theta I supplies the matching scale, target ratios, shared-circle
overlap, and spectral floor.  Theta II supplies the direct geometric
normalizations for the lens and nil overlaps.

Substituting `I1=2 pi R1` into `I2/I1=0.560` and
`I2=4 pi (f2 R_lens)^2` gives `(f2 R_lens)^2=0.280 R1`.
The lens spectral bound is then `lambda_lens >= 2/(0.280 R1)`, whose minimum
on `0 < R1 <= 2` is `2/0.560 = 3.571... > 0.25`.

Substituting `I3=c` into `I3/I1=0.229` gives
`c ~= 0.229 * 2 pi R1 = 1.439 R1`.  With `a=b=1` and `R1 <= 2`, the nil
bound gives
`lambda_1 >= 2 pi + 4 pi^2/(2.878)^2 = 11.05... > 0.25`.

All listed quantities are fixed before any fermion mass or mixing comparison.
Hence they form a no-proxy scaffold for the subsequent overlap-kernel
calculation.

# What Is Closed

The following are closed at scaffold level:

```text
Theta matching scale,
gauge-overlap ratios,
direct lens overlap normalization,
direct nil overlap normalization,
spectral admissibility margins,
finite CP character q=79 mod 448.
```

This is more than a benchmark.  It is a pre-flavor constraint package.  It says
where the Yukawa calculation must live.

# What Remains Open

The following are not yet closed:

```text
family zero-mode basis,
matter and Higgs supports,
finite channel sets Gamma_u, Gamma_d, Gamma_e, Gamma_nuD,
channel actions S_gamma,
prefactors A_gamma,
q79 channel orientation/nonzero status for C6 channels,
kinetic metrics and canonical normalization,
neutral real/Majorana or Dirac structure,
RG and threshold matching from mu_Theta to comparison scales.
```

These data are exactly what must be supplied before quark masses, charged
lepton masses, CKM angle magnitudes, neutrino splittings, or PMNS data count as
derived.

# Correct Next Step

The next calculation should not tune matrix entries.  It should build the
first concrete channel certificate:

```text
1. list the family zero modes selected by the Theta/q79 branch;
2. use the formulated finite channel sets Gamma_u,d,e,nuD;
3. compute A_gamma, S_gamma, C6 orientations, and nonzero status from the selected geometry;
4. canonically normalize using the selected kinetic metrics;
5. run RG/threshold matching;
6. compare to masses and mixings only after the above data are frozen.
```

# Bottom Line

The present result does not solve the full Yukawa problem.  It does something
more disciplined and still significant: it turns the mass problem from an
open-ended fit into an explicit geometric computation inside a fixed
Theta/q79 environment.

The next missing object is no longer vague.  It is the selected overlap-channel
certificate.
