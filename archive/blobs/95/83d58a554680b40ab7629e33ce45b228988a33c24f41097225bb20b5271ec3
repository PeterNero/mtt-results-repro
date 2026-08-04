---
abstract: |
  We convert Route C into an executable finite selected-connection solve
  scaffold.  The scaffold is deliberately not a selected solution: it defines
  the unknown blocks, residual gates, branch packet, finite mesh size
  accounting, guardrails, and downstream validator order required for a direct
  HYM/Strominger construction of D_E.  A complete residual certificate must
  carry either the m=1/q=79/F packet or the m=2/q=369/F* packet, while retaining
  the conjugate packet for antiunitary comparison.  At mesh N=1 the closed
  Iwasawa cell has 64 nodes, 192
  boundary-face incidences, 144 unique rho_E boundary matrices in a table
  ansatz, and a rank-three identity-rho smoke quotient of dimension 3.  A new
  residual validator is introduced for source-side checks: rho_E cocycle,
  metric compatibility, integrability, HYM primitivity, alpha1 Bianchi,
  Strominger residual, MTT selection gradient, Hessian positivity, Riesz gap,
  and no observed-flavor inputs.  Once a candidate passes this source gate, the
  existing validators take over: rho_E mesh, rho_E metric, sector maps, D_E
  action, Riesz gap, reduced Green, and dotD response.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Route C: Finite Selected-Connection Solve Scaffold
---

# Purpose

The source hunt closed the question:

```text
the current corpus does not contain a computable selected D_E.
```

Route C turns this into a constructive finite problem:

```text
derive D_E by solving finite selected connection constraints directly.
```

This note builds the scaffold for that problem.  It does not claim a selected
solution.

# Finite Mesh Accounting

Use the standard closed Iwasawa cell from the existing FE gluing skeleton.
For mesh `N`, closed nodes are:

```text
(N+1)^6.
```

For the first tiny execution mesh:

```text
N = 1,
closed nodes = 64,
boundary-face incidences = 192,
unique rho_E boundary matrices in a table ansatz = 144,
complex rho_E entries in the table ansatz = 1296,
corner nodes with multiple boundary faces = 57,
Hermitian metric real entries in a full node table = 576.
```

The identity-rho smoke quotient gives:

```text
scalar quotient dofs = 1,
rank-three bundle quotient dofs = 3.
```

This is only size accounting.  Identity `rho_E` remains a schema smoke test,
not the selected bundle.

# Unknown Blocks

The finite solve must determine:

```text
branch packet,
rho_E,
Hermitian metric H,
sector projectors P_Q,...,P_H,
A^(0,1) or D_E action,
dotD_alpha1.
```

# Branch Packet Gate

The residual certificate is now branch-aware.  A complete Route C candidate
must choose exactly one of:

```text
current_q79_orientation:
  m=1,
  q=79,
  SU(5) orientation F,
  Q,L carry orientation 1,
  u,d,e,N carry orientation 2,
  H carries the trivial Higgs-line orientation 0.

conjugate_q369_orientation:
  m=2,
  q=369,
  SU(5) orientation F*,
  Q,L carry orientation 2,
  u,d,e,N carry orientation 1,
  H carries the trivial Higgs-line orientation 0.
```

The candidate must also retain the antiunitary conjugate branch for comparison.
This keeps the conjugate-pair structure visible even if a later selected
operator chooses one representative.

The branch packet is not a free sign choice.  The same selected branch must feed
the operator domain, sector projectors, `D_E`, and `dotD_alpha1`:

```text
dotD_alpha1 = d D_E(branch, epsilon) / d epsilon |_{epsilon=0}.
```

The downstream format is already fixed by validators:

```text
validate_iwasawa_rhoE_mesh.py,
validate_iwasawa_rhoE_metric.py,
validate_iwasawa_sector_maps.py,
validate_iwasawa_de_action.py,
validate_iwasawa_riesz_gap.py,
validate_iwasawa_reduced_green.py,
validate_iwasawa_dotd_response.py.
```

# Source Residual Gate

Before any downstream matrix is allowed to count as selected, the candidate
must pass:

```text
validate_iwasawa_route_c_residuals.py.
```

The required residuals are:

```text
branch_packet,
rho_cocycle,
metric_compatibility,
integrability_F02,
hym_primitive,
bianchi_alpha1,
strominger_residual,
mtt_gradient.
```

The required positive gates are:

```text
mtt_hessian_min_eigenvalue > 0,
riesz_gap_min > 0.
```

The guardrails are:

```text
no observed masses or mixings,
no Execution II benchmark matrices,
no diagnostic h1=3 sparse candidate promoted to selected,
no external tangent-bundle instanton promoted to the visible SM bundle.
```

# Validator Order

The complete Route C execution order is:

```text
1. Route C residuals,
2. rho_E mesh gluing,
3. rho_E Hermitian metric,
4. sector projectors,
5. D_E sector action,
6. Riesz/gap,
7. reduced Green,
8. dotD response,
9. primitive C1 contractions.
```

The first eight are now executable contracts.  The ninth is the existing C1
matrix target.

# What This Closes

This closes:

```text
Route C problem layout,
finite mesh accounting,
branch-aware residual certificate format,
source residual certificate format,
downstream validator order.
```

It leaves open:

```text
actual selected rho_E,
actual selected branch packet,
actual selected Hermitian metric,
actual selected A^(0,1) or D_E action,
actual residual pass,
actual zero modes,
actual primitive C1 matrices,
full SM closure.
```

# Immediate Next Step

The next step is a small-`N` nonlinear or symbolic ansatz search that fills:

```text
certificates/iwasawa_route_c_residuals.template.json
```

with one branch packet, and then the downstream finite data files.

The first admissible search should be conservative:

```text
N=1 or N=2,
unitary or metric-compatible rho_E ansatz,
anti-Hermitian connection coefficients,
integrability and HYM residuals in the finite basis,
alpha1 Bianchi driver retained,
selection/Hessian positivity required,
no flavor data as inputs.
```

Only after this source gate passes can the existing spectral pipeline turn the
candidate into selected zero modes and C1 responses.
