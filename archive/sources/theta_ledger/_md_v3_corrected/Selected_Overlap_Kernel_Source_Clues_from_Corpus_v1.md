---
abstract: |
  We extract the overlap-kernel source clues already present in the corrected
  corpus.  The existing flavor papers do not yet compute no-proxy Yukawa
  matrices, but they do identify the right source variables: matter curves and
  triple intersections, pairwise line bundles, a holonomy phase sum rule,
  localization graph, flux-controlled widths, finite instanton or exceptional
  channel classes, Majorana real-structure criterion, and the finite q79 CP
  character.  These are assembled here as the current best candidate shape for
  the missing selected source map Sigma_MTT.
author:
- Peter Nero
date: June 2026
title: |
  Corpus Clues for the Selected Overlap-Kernel Source Map
---

# Purpose

The selected overlap-kernel certificate says that full no-proxy flavor closure
requires a source map:

```text
Sigma_MTT -> FlavorOverlapKernelCertificate.
```

This note records what the corrected corpus already supplies for that map.

# Corpus Source Variables

The corrected Execution corpus supplies the following flavor-source structure:

```text
B_fl =
(
  G_loc,
  {L_ij},
  {rho_gamma},
  W,
  I
).
```

where:

```text
G_loc       allowed localization graph of zero modes
L_ij        pairwise overlap line bundles
rho_gamma   flat holonomy characters
W           wavefunction width data fixed by calibrated geometry
I           finite instanton or exceptional-cycle channel classes
```

This is the right skeleton for `Sigma_MTT`.

# Matter Curve Source

The flavor benchmark section uses string-like matter localization:

```text
C_ij = S_i cap S_j.
```

Yukawa couplings arise from triple intersections or overlap integrals of
localized wavefunctions.  Therefore the no-proxy source map must compute:

```text
matter supports C_Q, C_u, C_d, C_L, C_e, C_nu, C_Hu, C_Hd;
triple overlap points or channel classes;
zero-mode bases on those supports.
```

# Pairwise Bundle and Holonomy Sum Rule

The topology-only layer supplies:

```text
L_12 tensor L_23 tensor L_31 ~= C.
```

Thus holonomies obey:

```text
arg det U_12 + arg det U_23 + arg det U_31 in 2 pi Z.
```

This is crucial.  It prevents arbitrary independent CP phases in the quark,
lepton, and neutrino sectors.

After q79 closure, the allowed CP-sensitive holonomies must also factor
through:

```text
tau^w,  tau=exp(2 pi i 79/448),  w in Z448.
```

# Gaussian/Theta-Function Kernel Clue

The corpus gives the schematic magnetized-brane or split-HYM form:

```text
Y_ij ~ exp[-d_ij^2/sigma^2] theta[delta_ij, phi_ij](tau_cx).
```

In the no-proxy reading:

```text
d_ij       must come from G_loc;
sigma      must come from flux/width data W;
delta_ij   must come from discrete charges and finite channel data;
phi_ij     must come from rho_gamma and q79 character data;
tau_cx     must be fixed by the selected geometry.
```

None of these may be selected entry by entry after looking at masses.

# Majorana Criterion

The corpus gives the topology-only Majorana criterion:

```text
L tensor L ~= C.
```

Therefore the neutral sector has a hard branch:

```text
if the selected neutral line/bundle sector satisfies L^2 ~= C:
  Majorana or seesaw channel is allowed;
else:
  the neutral sector must be Dirac or higher-operator in origin.
```

This criterion must be applied before PMNS and neutrino mass comparisons.

# Finite Wilson/Deck CP Carrier

The corrected q79 branch forbids reading the finite `Z64` CP data as ordinary
nonzero scalar Fourier zero modes.  The safe carrier is:

```text
K_64 ~= C[Z64]
```

retained as a finite Wilson/deck/equivariant character sector inside the
coherent projector.

Combining with the Mukai `Z7` character source gives:

```text
Gamma_CP ~= Z64 x Z7 ~= Z448.
```

Thus the CP part of `rho_gamma` is not arbitrary:

```text
rho_gamma,CP = tau^{w_gamma}.
```

# Candidate Source Map

The best current candidate is:

```text
Sigma_MTT =
(
  exact central-circle Wilson/deck carrier K_64,
  Fu-Yau/Mukai charge-sector character A_P ~= Z7,
  pairwise line-bundle data {L_ij},
  localization graph G_loc,
  selected lens/nil/flux width data W,
  finite instanton or exceptional-cycle classes I,
  nil/coherence/anchor projectors,
  neutral real-structure test L^2 ~= C
).
```

It should output:

```text
Gamma_x[i,j],
S_gamma,
A_gamma,
w_gamma,
c_gamma,
G_x
```

for each flavor sector.

# What This Closes

```text
source vocabulary for Sigma_MTT                         EXTRACTED
holonomy phases constrained by pairwise bundle rule      PROVED/IMPORTED
q79 character algebra as CP phase source                 PROVED/IMPORTED
Majorana branch criterion                                IMPORTED
entry-wise phase fitting forbidden                       PROVED BY CONSTRAINTS
```

# What Remains

```text
derive G_loc from selected MTT/proto-spinor geometry      OPEN
derive W from lens/nil/flux widths without mass input     OPEN
derive finite channel classes I                           OPEN
derive action costs and prefactors                        OPEN
derive kinetic metrics                                    OPEN
decide neutral-sector branch                              OPEN
```

# Next Proof Target

The next proof should construct:

```text
SelectedLocalizationGraphTheorem:
  theta/lens/nil/shared-circle/proto-spinor data
  -> G_loc and family zero-mode supports.
```

This is the first missing gate that can turn the certificate from an interface
into a calculation.

