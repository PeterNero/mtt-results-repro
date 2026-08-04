---
abstract: |
  We turn the remaining no-proxy flavor problem into a precise selected
  overlap-kernel certificate.  The q=79 CP branch is already closed on the
  exact/charge branch, but CKM angle magnitudes, Yukawa singular values,
  charged-lepton masses, neutrino data, and PMNS data are not yet derived.
  This note defines the missing object: a single selected MTT source map whose
  output fixes matter zero-mode spaces, kinetic metrics, finite overlap
  channels, action costs, prefactors, holonomy characters, nil/coherence
  projectors, and RG matching before comparison with measured masses or
  mixings.  Once this certificate is supplied, the resulting Yukawa matrices
  are no-proxy outputs.  Until then, existing flavor matrices remain benchmark
  or compatibility data rather than a full Standard Model closure theorem.
author:
- Peter Nero
date: June 2026
title: |
  Selected Overlap-Kernel Certificate for No-Proxy Flavor Closure
---

# Purpose

The q79 work closed the finite CP branch:

```text
Z64 exact central-circle branch + Z7 Fu-Yau/Mukai charge branch
-> q=79 mod 448.
```

The next frontier is different.  We must not merely place this phase into a
Yukawa benchmark.  We need the selected MTT geometry to generate the actual
overlap kernels whose singular values and mixing matrices become the observed
flavor data.

This note defines the certificate that would make that statement rigorous.

# Closed Input

The selected CP input is:

```text
Gamma_CP ~= Z64 x Z7 ~= Z448,
q=79,
chi_q(g)=exp(2 pi i q g/448).
```

This is imported from:

```text
Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md
Z64_Exact_Central_Circle_Branch_Certificate_v1.md
Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md
```

The CKM phase bridge then gives:

```text
delta_MTT = 2 pi 79/448.
```

That is already a no-proxy CP contact point because `q=79` is not chosen by
fitting CKM data.

# Missing Object

The missing object is a selected source map:

```text
Sigma_MTT:
  selected exact/charge branch
  -> FlavorOverlapKernelCertificate.
```

Its output must include:

```text
FlavorOverlapKernelCertificate:
  geometry:
    X_sel
    theta/lens/nil/shared-circle data
    exact/charge branch id
    compactification or charge-sector realization

  representations:
    H_Q, H_u, H_d, H_L, H_e, H_nu, H_Hu, H_Hd
    family labels
    Standard Model charges
    anomaly and tadpole constraints

  zero modes:
    psi_Q[i], psi_u[j], psi_d[j], psi_L[i], psi_e[j], psi_nu[j]
    Higgs modes h_u, h_d
    kinetic metrics G_Q, G_u, G_d, G_L, G_e, G_nu, G_Hu, G_Hd

  projectors:
    Pi_coh
    P_nil
    P_anchor
    P_cancel
    P_fl
    all commutator or leakage bounds needed for selected execution

  finite channels:
    Gamma_u[i,j]
    Gamma_d[i,j]
    Gamma_e[i,j]
    Gamma_nu[i,j]
    Gamma_R[i,j] if the neutral sector is Majorana

  channel weights:
    action cost S_gamma
    prefactor A_gamma
    holonomy character chi_gamma
    orientation/retarded sign epsilon_gamma
    nil-survivor status n_gamma
    anchor/cancellation status c_gamma

  output discipline:
    no entry, phase, distance, width, normalization, or threshold may be
    adjusted after Sigma_MTT is fixed.
```

# Kernel Formula

For each sector `x in {u,d,e,nu,R}`, the raw selected overlap matrix is:

```text
Y_x,raw[i,j] =
  sum_{gamma in Gamma_x[i,j]}
    A_gamma
    exp(-S_gamma)
    chi_gamma
    epsilon_gamma
    n_gamma
    c_gamma.
```

The finite CP branch enters through the selected character:

```text
chi_gamma = chi_q(w_gamma)
          = exp(2 pi i q w_gamma / 448)
```

whenever the channel carries CP weight `w_gamma in Z448`.

Canonical normalization is then mandatory:

```text
Y_u = G_Q^{-1/2} Y_u,raw G_u^{-1/2} G_Hu^{-1/2},
Y_d = G_Q^{-1/2} Y_d,raw G_d^{-1/2} G_Hd^{-1/2},
Y_e = G_L^{-1/2} Y_e,raw G_e^{-1/2} G_Hd^{-1/2},
Y_nu = G_L^{-1/2} Y_nu,raw G_nu^{-1/2} G_Hu^{-1/2}.
```

If the neutral sector is Majorana, also compute:

```text
M_nu,eff = - v_u^2 Y_nu M_R^{-1} Y_nu^T.
```

If it is Dirac, use the singular values of `Y_nu`.

# Theorem: No-Proxy Flavor from a Selected Kernel

Assume `Sigma_MTT` supplies a certificate satisfying the following gates:

```text
OK.1  selected geometry and charge sector fixed;
OK.2  Standard Model representation spaces fixed;
OK.3  normalized zero-mode bases fixed;
OK.4  kinetic metrics fixed and positive;
OK.5  finite overlap channel sets fixed;
OK.6  all action costs, prefactors, characters, and retarded signs fixed;
OK.7  nil/coherence/anchor/cancellation projectors fixed;
OK.8  RG and threshold matching map fixed;
OK.9  no measured masses or mixings used in any OK.1--OK.8 choice.
```

Then the matrices:

```text
Y_u, Y_d, Y_e, Y_nu, M_R
```

are no-proxy outputs of MTT.  The CKM and PMNS matrices obtained by diagonal
normalization are then predictions:

```text
V_CKM = U_u,L^* U_d,L,
U_PMNS = U_e,L^* U_nu,L.
```

The resulting masses and mixing data may be compared with experiment only
after the certificate is frozen.

# Proof

By OK.1--OK.7 all summands in the raw overlap matrices are selected by
`Sigma_MTT`.  Thus no matrix entry is adjustable after branch selection.

By OK.4 the kinetic metrics admit canonical positive square roots on the
retained zero-mode spaces.  Canonical normalization is therefore an invariant
operation determined by the same source map.

By OK.8 RG and threshold transport are fixed before comparison with low-energy
data.  By OK.9 no observed flavor datum enters the construction.  Therefore
the produced Yukawa singular values, CKM matrix, charged-lepton masses, and
neutral-sector data are outputs rather than fitted inputs.

# Theorem: Current Barrier

The existing q79 proof plus CKM phase bridge does not yet prove full flavor
closure.

Proof.  The q79 certificate fixes the finite CP character.  The CKM phase
bridge computes:

```text
delta_MTT = 2 pi 79/448.
```

However the bridge does not select:

```text
Gamma_x[i,j],
S_gamma,
A_gamma,
G_Q, G_u, G_d, G_L, G_e, G_nu,
M_R or Dirac/Majorana neutral mechanism.
```

These quantities determine the CKM angle magnitudes, Yukawa singular values,
charged-lepton masses, and neutrino data.  Therefore those outputs remain open
until the selected overlap-kernel certificate is supplied.

# Proto-Spinor Simulation Bridge

A proto-spinor particle simulation can be useful as an execution test, but it
does not by itself close the analytic proof.

The simulation state should mirror the certificate variables:

```text
ParticleState:
  theta
  lens
  nil
  shared_circle_phase
  J_closure_cost
  coherence
  anchor_status
  cancellation_status
  finite_CP_weight
  family_label
```

The simulation kernel should use the same form:

```text
K(a,b) =
  Pi_coh Pi_nil Pi_anchor Pi_cancel
  sum_gamma A_gamma exp(-S_gamma) chi_q(w_gamma).
```

If simulated particles show stable family splitting, coherent propagation,
charge conservation, and cancellation/anchor behavior, that is evidence that
the execution rules are coherent.  It becomes proof-relevant only when the
same variables are derived from `Sigma_MTT` and audited as OK.1--OK.9.

# Current Status Ledger

```text
finite CP quotient q=79                         CLOSED
CKM CP phase bridge                             CLOSED/COMPATIBLE
selected overlap-kernel certificate             DEFINED
same-source no-proxy theorem                    PROVED AS SCHEMA
zero-mode spaces                                OPEN
kinetic metrics                                 OPEN
finite overlap channel sets                     OPEN
action costs and prefactors                     OPEN
neutral-sector mechanism                        OPEN
RG and threshold matching                       OPEN
full no-proxy SM flavor closure                 OPEN
```

# Next Computation

The next concrete computation is to instantiate the first nontrivial selected
kernel packet:

```text
MinimalSelectedKernelPacket:
  H_Q, H_u, H_d
  three family labels
  one Higgs mode per sector
  Gamma_u[i,j], Gamma_d[i,j]
  q=79 character weights w_gamma
  symbolic S_gamma and A_gamma from theta/lens/nil data
  explicit kinetic metrics or a proof that they are identity in the selected
  normalized basis
```

This packet should be small enough to compute but strict enough to reject
entry-wise fitting.

# Bottom Line

The q79 branch has closed the selected finite CP phase.  The correct next
proof target is not another phase fit.  It is the construction of
`Sigma_MTT`, the selected source map that produces the full overlap kernel
from the same branch.

